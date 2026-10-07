"""H8 synthetic fixture only; not a Trading OS scheduler."""
import argparse
import hashlib
import importlib.metadata
import json
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_MISSED
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def callback(fixture, logical_id):
    with sqlite3.connect(Path(fixture)/'receipts.db') as connection:
        connection.execute('insert into receipts values (?)', (logical_id,))


def stage(fixture):
    with sqlite3.connect(fixture/'receipts.db') as connection:
        connection.execute('create table receipts (logical_id text primary key)')
    scheduler = BackgroundScheduler(jobstores={'default':SQLAlchemyJobStore(url='sqlite:///'+(fixture/'jobs.db').as_posix())}, timezone=timezone.utc)
    scheduler.start(paused=True)
    due = datetime.now(timezone.utc)+timedelta(seconds=1)
    for logical_id, grace in (('eligible',30),('expired',1)):
        scheduler.add_job('calendar_probe:callback', 'date', run_date=due,
            args=[str(fixture),logical_id], id=logical_id, misfire_grace_time=grace)
    ids = [j.id for j in scheduler.get_jobs()]
    scheduler.shutdown(wait=True)
    return {'persisted_ids':sorted(ids)}


def restart(fixture):
    events=[]
    scheduler=BackgroundScheduler(jobstores={'default':SQLAlchemyJobStore(url='sqlite:///'+(fixture/'jobs.db').as_posix())}, timezone=timezone.utc)
    scheduler.add_listener(lambda e:events.append({'id':e.job_id,'code':'EXECUTED' if e.code==EVENT_JOB_EXECUTED else 'MISSED'}), EVENT_JOB_EXECUTED|EVENT_JOB_MISSED)
    scheduler.start()
    deadline=time.monotonic()+6
    while time.monotonic()<deadline and len(events)<2:
        time.sleep(0.05)
    ids=[j.id for j in scheduler.get_jobs()]
    scheduler.shutdown(wait=True)
    return {'events':events,'remaining_ids':ids}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--mode',choices=['stage','restart','inspect'])
    parser.add_argument('--fixture')
    args=parser.parse_args()
    if args.mode:
        fixture=Path(args.fixture).resolve()
        approved=(ROOT/'.local/h8-fixtures').resolve()
        if not fixture.is_relative_to(approved):
            raise ValueError('fixture outside declared workspace root')
        if args.mode=='stage': data=stage(fixture)
        elif args.mode=='restart': data=restart(fixture)
        else:
            scheduler=BackgroundScheduler(jobstores={'default':SQLAlchemyJobStore(url='sqlite:///'+(fixture/'jobs.db').as_posix())}, timezone=timezone.utc)
            scheduler.start(paused=True)
            data={'remaining_ids':[j.id for j in scheduler.get_jobs()]}
            scheduler.shutdown(wait=True)
        print(json.dumps(data)); return
    fixture=ROOT/'.local/h8-fixtures'/('trial-'+str(time.time_ns()))
    fixture.mkdir(parents=True,exist_ok=False)
    observations={}; failure=None
    env={k:v for k,v in os.environ.items() if k.upper() in ('SYSTEMROOT','WINDIR','TEMP','TMP','PYTHONPATH','PATH')}
    def child(mode):
        run=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--mode',mode,'--fixture',str(fixture)],env=env,capture_output=True,text=True,timeout=15)
        if run.returncode!=0:
            raise RuntimeError('bounded fixture child failed: '+mode)
        return json.loads(run.stdout)
    try:
        observations['stage']=child('stage')
        time.sleep(3)
        observations['restart']=child('restart')
        observations['inspect']=child('inspect')
        with sqlite3.connect(fixture/'receipts.db') as connection:
            observations['receipts']=[r[0] for r in connection.execute('select logical_id from receipts')]
            try:
                connection.execute('insert into receipts values (?)',('eligible',))
                observations['duplicate_rejected']=False
            except sqlite3.IntegrityError:
                observations['duplicate_rejected']=True
    except Exception as exc:
        failure=type(exc).__name__
    events=observations.get('restart',{}).get('events',[])
    criteria={
        'H8-1':observations.get('stage',{}).get('persisted_ids')==['eligible','expired'],
        'H8-2':events.count({'id':'eligible','code':'EXECUTED'})==1 and observations.get('receipts')==['eligible'],
        'H8-3':events.count({'id':'expired','code':'MISSED'})==1,
        'H8-4':observations.get('inspect',{}).get('remaining_ids')==[],
        'H8-5':observations.get('duplicate_rejected') is True,
        'H8-6':failure is None}
    result={'captured_at':datetime.now(timezone.utc).isoformat(),'scope':'SYNTHETIC_CALENDAR_NOT_WORKFLOW_OR_PAPER_ACCEPTANCE',
        'versions':{p:importlib.metadata.version(p) for p in ('APScheduler','SQLAlchemy','tzlocal')},
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'criteria':{k:'PASS' if v else 'FAIL' for k,v in criteria.items()},'observations':observations,
        'error_class':failure,'fixture_retained':True,'fixture_locator_private':'.local/h8-fixture-binding.json',
        'in_flight_recovery_tested':False,'paper_runtime_accepted':False,'OS_admin_changes':[]}
    (ROOT/'.local/h8-fixture-binding.json').write_text(json.dumps({'path':str(fixture)}),encoding='utf-8')
    (HERE/'result-01.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'criteria':result['criteria'],'error_class':failure}))
    raise SystemExit(not all(criteria.values()))


if __name__=='__main__':main()
