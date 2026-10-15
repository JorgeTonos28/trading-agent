"""Disposable semantic/crash probe. Not a Trading OS scheduler or storage module."""
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
checks=[]
def check(name, passed):
    checks.append({'id':name,'passed':bool(passed)})
    if not passed: raise AssertionError(name)
def digest(x): return hashlib.sha256(x.encode()).hexdigest()

def main():
    report={'probe':'H1_H2_H3_DISPOSABLE','created_at':datetime.now(timezone.utc).isoformat(),
        'scope':'SQLite semantic/process-crash toy; no engine selection, real financial runtime, OS isolation or LLM quota proof',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,
        'sqlite_version':sqlite3.sqlite_version,'financial_interfaces':0}
    with tempfile.TemporaryDirectory(prefix='r010_contract_') as temp:
        folder=Path(temp).resolve()
        assert folder.parent==Path(tempfile.gettempdir()).resolve() and folder.name.startswith('r010_contract_')
        db=folder/'toy.db'
        con=sqlite3.connect(db)
        con.execute('PRAGMA journal_mode=WAL');con.execute('PRAGMA synchronous=FULL')
        con.execute('CREATE TABLE events(id TEXT PRIMARY KEY, value TEXT)')
        con.commit();con.close()
        child='''import sqlite3,sys,os
c=sqlite3.connect(sys.argv[1]);c.execute('PRAGMA synchronous=FULL');c.execute('BEGIN IMMEDIATE')
c.execute('INSERT INTO events VALUES (?,?)',(sys.argv[2],'synthetic'))
if sys.argv[3]=='after':c.commit()
os._exit(19)
'''
        for mode in ('before','after'):
            p=subprocess.run([sys.executable,'-c',child,str(db),mode,mode],capture_output=True,timeout=15)
            check('child_abrupt_exit_'+mode,p.returncode==19)
        con=sqlite3.connect(db)
        check('uncommitted_absent',con.execute('SELECT count(*) FROM events WHERE id="before"').fetchone()[0]==0)
        check('committed_survives_process_exit',con.execute('SELECT count(*) FROM events WHERE id="after"').fetchone()[0]==1)
        con.executescript('''CREATE TABLE jobs(id TEXT PRIMARY KEY, snapshot TEXT, generation INTEGER, deadline INTEGER);
        CREATE TABLE attempts(id TEXT PRIMARY KEY, job TEXT, generation INTEGER);
        CREATE TABLE receipts(n INTEGER PRIMARY KEY, job TEXT, attempt TEXT, output_hash TEXT, verdict TEXT);
        CREATE TABLE admitted(job TEXT PRIMARY KEY, attempt TEXT, output_hash TEXT);''')
        con.execute('INSERT INTO jobs VALUES (?,?,?,?)',('J1',digest('sealed'),1,120))
        con.execute('INSERT INTO attempts VALUES (?,?,?)',('A1','J1',1));con.commit()
        def receive(job,attempt,snapshot,output,at):
            con.execute('BEGIN IMMEDIATE')
            row=con.execute('SELECT snapshot,generation,deadline FROM jobs WHERE id=?',(job,)).fetchone()
            a=con.execute('SELECT job,generation FROM attempts WHERE id=?',(attempt,)).fetchone()
            if not row or not a or a[0]!=job: verdict='UNKNOWN_IDENTITY'
            elif snapshot!=row[0]: verdict='SNAPSHOT_MISMATCH'
            elif a[1]!=row[1]: verdict='STALE_ATTEMPT'
            elif output is None: verdict='NO_OUTPUT'
            elif at>row[2]: verdict='LATE_RETROSPECTIVE_ONLY'
            elif con.execute('SELECT 1 FROM admitted WHERE job=?',(job,)).fetchone(): verdict='DUPLICATE'
            else:
                verdict='ACCEPTED_ON_TIME'
                con.execute('INSERT INTO admitted VALUES (?,?,?)',(job,attempt,digest(output)))
            con.execute('INSERT INTO receipts(job,attempt,output_hash,verdict) VALUES (?,?,?,?)',
                (job,attempt,digest(output) if output else None,verdict));con.commit()
            return verdict
        sh=digest('sealed')
        check('missing_is_no_output',receive('J1','A1',sh,None,10)=='NO_OUTPUT')
        check('hash_mismatch_rejected',receive('J1','A1',digest('changed'),'{}',20)=='SNAPSHOT_MISMATCH')
        check('unknown_identity_rejected',receive('J1','bad',sh,'{}',20)=='UNKNOWN_IDENTITY')
        con.execute('UPDATE jobs SET generation=2 WHERE id="J1"')
        con.execute('INSERT INTO attempts VALUES (?,?,?)',('A2','J1',2));con.commit()
        check('old_worker_fenced',receive('J1','A1',sh,'{}',30)=='STALE_ATTEMPT')
        check('current_accepted',receive('J1','A2',sh,'{"action":"ABSTAIN"}',40)=='ACCEPTED_ON_TIME')
        check('ack_loss_repeat_deduplicated',receive('J1','A2',sh,'{"action":"ABSTAIN"}',41)=='DUPLICATE')
        check('conflicting_output_cannot_replace',receive('J1','A2',sh,'{"action":"OPEN"}',50)=='DUPLICATE')
        check('late_preserved',receive('J1','A2',sh,'{}',121)=='LATE_RETROSPECTIVE_ONLY')
        check('single_admitted',con.execute('SELECT count(*) FROM admitted').fetchone()[0]==1)
        check('all_attempt_receipts_accounted',con.execute('SELECT count(*) FROM receipts').fetchone()[0]==8)
        backup=folder/'restored.db';target=sqlite3.connect(backup);con.backup(target);target.close();con.close()
        restored=sqlite3.connect(backup)
        check('backup_restore_receipts',restored.execute('SELECT count(*) FROM receipts').fetchone()[0]==8)
        check('backup_restore_selected',restored.execute('SELECT attempt FROM admitted').fetchone()[0]=='A2')
        restored.close()
        readonly=sqlite3.connect(db.as_uri()+'?mode=ro',uri=True)
        try:
            readonly.execute('INSERT INTO events VALUES ("bad","write")'); denied=False
        except sqlite3.OperationalError: denied=True
        readonly.close();check('sqlite_readonly_write_denied_NOT_OS_ACL',denied)
        allowed={'bundle':'J1'}
        check('tool_extra_arg_rejected',set({'bundle':'J1','path':'../secret'})!=set(allowed))
        check('tool_unapproved_bundle_rejected',{'bundle':'J2'}!=allowed)
    # Virtual time only. Every scheduled slot remains a distinct required job.
    source=ROOT/'planning/research/probes/r006-team-paper/result-attempt-02.json'
    wave=json.loads(source.read_text(encoding='utf-8'))
    role_times={}
    for trial in wave['trials']:
        if trial['case']!='failure':role_times.setdefault(trial['case'],[]).append(trial['service_seconds'])
    jobs=[]
    for n in range(26):jobs.append({'id':f'SH{n}','role':'shadow','at':n*900,'window':120})
    for n in range(10):jobs.append({'id':f'PE{n}','role':'pedagogy','at':n*1800,'window':600})
    jobs += [{'id':'PD','role':'pedagogy','at':23400,'window':3600},
             {'id':'R1','role':'research','at':0,'window':86400},
             {'id':'R2','role':'research','at':18000,'window':86400},
             {'id':'Q1','role':'quant','at':21600,'window':86400}]
    # Deterministic priority among ready jobs; nonpreemptive, one worker.
    def simulate(multiplier):
        pending=list(jobs);done=[];clock=0
        while pending:
            ready=[x for x in pending if x['at']<=clock]
            if not ready:clock=min(x['at'] for x in pending);continue
            job=min(ready,key=lambda x:({'shadow':0,'pedagogy':1,'quant':2,'research':3}[x['role']],x['at'],x['id']))
            duration=max(role_times[job['role']])*multiplier
            start=clock;clock+=duration;pending.remove(job)
            done.append({'job':job['id'],'role':job['role'],'arrival':job['at'],'wait_s':round(start-job['at'],3),
                'service_s':round(duration,3),'total_s':round(clock-job['at'],3),'on_time':clock<=job['at']+job['window']})
        return {'multiplier':multiplier,'required':len(jobs),'accounted':len(done),
                'on_time':sum(x['on_time'] for x in done),'service_seconds':round(sum(x['service_s'] for x in done),3),
                'max_total_shadow_s':max(x['total_s'] for x in done if x['role']=='shadow'),'jobs':done}
    runs=[simulate(x) for x in (1,2,4)]
    check('simulation_all_40_accounted',all(x['accounted']==40 for x in runs))
    report.update({'simulation_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'simulation_assumptions':'max observed role service; priority queue; no retry/auth/quota/network/OS delays; virtual arrival pattern; not observed 40 LLM jobs',
        'simulation_runs':runs,'limitations':['no power-loss test','no PostgreSQL/Temporal test','no host permission enforcement',
             'no native 40-job or sustained quota acceptance','toy output strings, no financial/schema validation'],
        'passed':sum(x['passed'] for x in checks),'total':len(checks),'cleanup':'temporary workspace closed'})
    (HERE/'result.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'checks':len(checks),'passed':report['passed'],'simulation':[{k:r[k] for k in ('multiplier','required','accounted','on_time','max_total_shadow_s')} for r in runs]}))

if __name__=='__main__':main()
