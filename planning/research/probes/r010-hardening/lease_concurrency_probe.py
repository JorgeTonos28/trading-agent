"""Additional H2 toy SQLite race/lifecycle probe; no real scheduler or OS permissions."""
import hashlib,json,sqlite3,tempfile,threading
from pathlib import Path
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,ok):
 checks.append({'id':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
with tempfile.TemporaryDirectory(prefix='r010_lease_') as temp:
 folder=Path(temp).resolve()
 assert folder.parent==Path(tempfile.gettempdir()).resolve() and folder.name.startswith('r010_lease_')
 db=folder/'toy.db';c=sqlite3.connect(db)
 c.executescript('''PRAGMA journal_mode=WAL;
 CREATE TABLE jobs(id TEXT PRIMARY KEY,state TEXT,generation INTEGER,attempt TEXT,owner TEXT,expiry REAL,deadline REAL);
 CREATE TABLE selected(job TEXT PRIMARY KEY,attempt TEXT,value TEXT);
 CREATE TABLE receipt(n INTEGER PRIMARY KEY,job TEXT,attempt TEXT,verdict TEXT);''')
 for name in ('race','expired','cancelled','exhausted','wrongowner','wrongattempt','stale'):
  c.execute('INSERT INTO jobs VALUES (?,?,?,?,?,?,?)',(name,'RUNNING',2,'A2','W2',90,120))
 c.execute('UPDATE jobs SET state="CANCELLED" WHERE id="cancelled"')
 c.execute('UPDATE jobs SET state="EXHAUSTED" WHERE id="exhausted"');c.commit();c.close()
 def receive(job,attempt='A2',generation=2,owner='W2',at=50):
  con=sqlite3.connect(db,timeout=10)
  try:
   con.execute('BEGIN IMMEDIATE')
   row=con.execute('SELECT state,generation,attempt,owner,expiry,deadline FROM jobs WHERE id=?',(job,)).fetchone()
   if row[0] not in ('RUNNING','SUCCEEDED'): verdict='REJECTED_LIFECYCLE'
   elif at>row[5]:verdict='LATE_RETROSPECTIVE_ONLY'
   elif generation!=row[1] or attempt!=row[2] or owner!=row[3] or at>=row[4]:verdict='REJECTED_LEASE'
   elif con.execute('SELECT 1 FROM selected WHERE job=?',(job,)).fetchone():verdict='DUPLICATE'
   else:
    verdict='ACCEPTED_ON_TIME'
    con.execute('INSERT INTO selected VALUES (?,?,?)',(job,attempt,'synthetic-output'))
    con.execute('UPDATE jobs SET state="SUCCEEDED" WHERE id=?',(job,))
   con.execute('INSERT INTO receipt(job,attempt,verdict) VALUES (?,?,?)',(job,attempt,verdict));con.commit()
   return verdict
  finally:con.close()
 barrier=threading.Barrier(3);responses=[];errors=[];lock=threading.Lock()
 def competitor():
  barrier.wait()
  try:r=receive('race')
  except Exception as e:
   with lock:errors.append(type(e).__name__)
  else:
   with lock:responses.append(r)
 threads=[threading.Thread(target=competitor) for _ in range(2)]
 for t in threads:t.start()
 barrier.wait()
 for t in threads:t.join(15)
 check('both_threads_finish',all(not t.is_alive() for t in threads) and not errors)
 check('concurrent_receipts_exactly_one_selected',sorted(responses)==['ACCEPTED_ON_TIME','DUPLICATE'])
 check('lease_expiry_rejects',receive('expired',at=90)=='REJECTED_LEASE')
 check('cancelled_rejects',receive('cancelled')=='REJECTED_LIFECYCLE')
 check('exhausted_rejects',receive('exhausted')=='REJECTED_LIFECYCLE')
 check('wrong_owner_rejects',receive('wrongowner',owner='W1')=='REJECTED_LEASE')
 check('wrong_attempt_rejects',receive('wrongattempt',attempt='A1')=='REJECTED_LEASE')
 check('stale_generation_rejects',receive('stale',generation=1)=='REJECTED_LEASE')
 check('late_is_retrospective',receive('expired',at=121)=='LATE_RETROSPECTIVE_ONLY')
 con=sqlite3.connect(db)
 check('all_nine_receipts_accounted',con.execute('SELECT count(*) FROM receipt').fetchone()[0]==9)
 check('only_race_has_selected_output',con.execute('SELECT count(*) FROM selected').fetchone()[0]==1)
 con.close()
report={'probe':'H2_LEASE_RACE_ADDITIONAL','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'toy transactional semantics; virtual timestamps and lease identities; no real worker lease renewal/auth/OS proof',
 'checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks),'race_verdicts':responses,
 'limitations':['no concurrent cancellation race executed','no clock-drift/reboot test','no PostgreSQL/Temporal proof'],
 'cleanup':'temporary workspace closed'}
(HERE/'lease-concurrency-result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'passed':report['passed'],'total':report['total'],'race':responses}))
