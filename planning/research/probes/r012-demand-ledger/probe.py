from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib,json,sqlite3,time

here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
work=root/'.local/h9-demand-ledger';work.mkdir(exist_ok=False)
db=work/'ledger.db';rows=[]
def case(id,observed,expected):rows.append({'id':id,'observed':observed,'expected':expected,'status':'PASS' if observed==expected else 'FAIL'})
def connect(path=db):
    c=sqlite3.connect(path,timeout=10,isolation_level=None)
    c.execute('PRAGMA synchronous=FULL');c.execute('PRAGMA foreign_keys=ON')
    return c
c=connect();mode=c.execute('PRAGMA journal_mode=DELETE').fetchone()[0]
c.executescript('''
CREATE TABLE jobs(id TEXT PRIMARY KEY, state TEXT NOT NULL, generation INTEGER NOT NULL, attempt TEXT, deadline INTEGER NOT NULL);
CREATE TABLE outbox(job TEXT PRIMARY KEY REFERENCES jobs(id), kind TEXT NOT NULL);
CREATE TABLE receipts(job TEXT PRIMARY KEY REFERENCES jobs(id), attempt TEXT NOT NULL, epoch INTEGER NOT NULL, bodyhash TEXT NOT NULL);
CREATE TABLE rejection_log(job TEXT, reason TEXT NOT NULL);
''');c.close()
ids=[f'fixture:{role}:{slot}' for slot in range(300) for role in ['research','quant','shadow','ped']]
def insert(job):
    c=connect()
    try:
        c.execute('BEGIN IMMEDIATE')
        inserted=c.execute('INSERT OR IGNORE INTO jobs VALUES (?, ?, ?, ?, ?)',(job,'QUEUED',0,None,100)).rowcount
        if inserted:c.execute('INSERT INTO outbox VALUES (?,?)',(job,'WAKEUP'))
        c.execute('COMMIT');return inserted
    finally:c.close()
start=time.monotonic()
with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(insert,ids+ids))
elapsed=round(time.monotonic()-start,3)
c=connect();nj=c.execute('SELECT count(*) FROM jobs').fetchone()[0];no=c.execute('SELECT count(*) FROM outbox').fetchone()[0]
case('LOGICAL_JOBS_DEDUP_CONCURRENT_PROPOSALS',{'jobs':nj,'outbox':no,'inserted':sum(results)},{'jobs':1200,'outbox':1200,'inserted':1200})
c.execute('BEGIN IMMEDIATE');c.execute('INSERT INTO jobs VALUES (?,?,?,?,?)',('abort','QUEUED',0,None,100));c.execute('INSERT INTO outbox VALUES (?,?)',('abort','WAKEUP'));c.execute('ROLLBACK')
case('ROLLBACK_JOB_AND_OUTBOX',c.execute("SELECT count(*) FROM jobs WHERE id='abort'").fetchone()[0],0)
job=ids[0]
c.execute('BEGIN IMMEDIATE')
n=c.execute("UPDATE jobs SET state='RUNNING', generation=generation+1,attempt=? WHERE id=? AND generation=? AND state='QUEUED'",('a1',job,0)).rowcount
c.execute('COMMIT')
case('CAS_FIRST_ATTEMPT',n,1)
case('CAS_STALE_GENERATION_REJECTED',c.execute("UPDATE jobs SET attempt='a2' WHERE id=? AND generation=0",(job,)).rowcount,0)
c.close()
current_epoch=1
def admit(job,attempt,generation,epoch,received,bodyhash):
    c=connect()
    try:
        c.execute('BEGIN IMMEDIATE')
        state,gen,cur,deadline=c.execute('SELECT state,generation,attempt,deadline FROM jobs WHERE id=?',(job,)).fetchone()
        existing=c.execute('SELECT 1 FROM receipts WHERE job=?',(job,)).fetchone()
        if epoch!=current_epoch:reason='STALE_INCARNATION'
        elif received>deadline:reason='LATE'
        elif existing:reason='DUPLICATE'
        elif state!='RUNNING' or cur!=attempt or gen!=generation:reason='STALE_ATTEMPT'
        else:reason=None
        if reason:c.execute('INSERT INTO rejection_log VALUES (?,?)',(job,reason))
        else:
            c.execute('INSERT INTO receipts VALUES (?,?,?,?)',(job,attempt,epoch,bodyhash))
            c.execute("UPDATE jobs SET state='SUCCEEDED' WHERE id=?",(job,))
        c.execute('COMMIT');return reason or 'ACCEPTED'
    finally:c.close()
case('STALE_ATTEMPT_NOT_ADMITTED',admit(job,'a0',0,1,99,'h0'),'STALE_ATTEMPT')
case('LATE_OUTPUT_NOT_ADMITTED',admit(job,'a1',1,1,101,'h1'),'LATE')
# Capture backup before admitting the output to create a known recovery gap.
c=connect();backup=sqlite3.connect(work/'before-receipt.db');c.backup(backup);backup.close();c.close()
case('VALID_OUTPUT_RECEIPT',admit(job,'a1',1,1,99,'h1'),'ACCEPTED')
case('DUPLICATE_NOT_SECOND_RECEIPT',admit(job,'a1',1,1,99,'h1'),'DUPLICATE')
c=connect();case('EXACTLY_ONE_RECEIPT_IN_FIXTURE',c.execute('SELECT count(*) FROM receipts WHERE job=?',(job,)).fetchone()[0],1)
case('SQLITE_INTEGRITY',c.execute('PRAGMA integrity_check').fetchone()[0],'ok');c.close()
# External fixture evidence notes that h1 was acknowledged after the backup.
(work/'outside-backup-anchor.json').write_text(json.dumps({'job':job,'acknowledged_bodyhash':'h1','epoch':1}),encoding='utf-8')
restored=work/'restored.db';old=sqlite3.connect(work/'before-receipt.db');new=sqlite3.connect(restored);old.backup(new);old.close();new.close()
current_epoch=2
case('OLD_ATTEMPT_AFTER_RESTORE_NOT_CURRENT',admit(job,'a1',1,1,99,'h1'),'STALE_INCARNATION')
# The call above targets the original ledger, solely testing external epoch enforcement.
restore_conn=connect(restored)
lost=restore_conn.execute('SELECT count(*) FROM receipts WHERE job=?',(job,)).fetchone()[0]==0
case('BACKUP_RECEIPT_GAP_VISIBLE',{'receipt_missing':lost,'anchor_acknowledged':True},{'receipt_missing':True,'anchor_acknowledged':True})
case('RESTORED_SQLITE_INTEGRITY',restore_conn.execute('PRAGMA integrity_check').fetchone()[0],'ok');restore_conn.close()
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'SYNTHETIC_LOCAL_LEDGER_WORKLOAD_NOT_SELECTED_ENGINE_OR_OPERATIONAL_ACCEPTANCE',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sqlite_version':sqlite3.sqlite_version,
 'journal_mode':mode,'synchronous':'FULL','logical_jobs':1200,'insert_proposals':2400,'producer_threads':4,
 'insertion_elapsed_seconds':elapsed,'performance_gate':'NOT_DEFINED_NOT_PASSED',
 'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'fixture_retained':True,'external_epoch_is_fixture_not_security_boundary':True,
 'restore_acceptance':'RECOVERY_GAP_DEMONSTRATED_NOT_OPERATIONAL_RECOVERY_ACCEPTED',
 'WAL_reset_bug_reproduced_or_fixed':False,'PostgreSQL_or_powerloss_or_FSYNC_proven':False,
 'server_service_admin_or_account_used':False,'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'elapsed':elapsed,'failed':[r for r in rows if r['status']!='PASS']}))
