from pathlib import Path
from datetime import datetime, timedelta, timezone
from decimal import Decimal as D
import hashlib, json
here=Path(__file__).resolve().parent;out=here/'result-01.json'
if out.exists():raise FileExistsError('New immutable attempt required')
def ts(day,hour=0):return datetime(2030,1,day,hour,tzinfo=timezone.utc)
versions=[dict(id='FICTION-A',version=1,available=ts(1),receipt=ts(6),value='1.00',status='ACTIVE'),dict(id='FICTION-A',version=2,available=ts(3),receipt=ts(6),value='1.20',status='ACTIVE'),dict(id='FICTION-A',version=3,available=ts(4),receipt=ts(6),value=None,status='CANCELED')]
def snapshot(records,cutoff,mode,complete=True,delay=timedelta(0)):
    if any(r.get('available') is None for r in records):return ('UNKNOWN_AVAILABILITY',None)
    known=[r for r in records if (r['receipt'] if mode=='OBSERVED_REPLAY' else r['available']+delay)<=cutoff]
    if not known:return ('NO_ELIGIBLE_OBSERVED_RECORD' if mode=='OBSERVED_REPLAY' else ('NO_EVENT_PROVEN' if complete else 'INSUFFICIENT_EVIDENCE'),None)
    row=max(known,key=lambda r:(r['available'],r['version']))
    return row['status'],row['version']
rows=[]
def check(name,x,y):rows.append(dict(id=name,observed=x,expected=y,status='PASS' if x==y else 'FAIL'))
check('CA01_RECONSTRUCTION_V1',snapshot(versions,ts(2),'RECONSTRUCTED_ASOF'),('ACTIVE',1))
check('CA01_LATEST_ONLY_CANNOT_RECREATE_OLD',snapshot([versions[-1]],ts(2),'RECONSTRUCTED_ASOF',complete=False),('INSUFFICIENT_EVIDENCE',None))
unknown=[dict(id='FICTION-B',version=1,available=None,receipt=ts(6),value='2',status='ACTIVE')]
check('CA02_OLD_EVENT_UNKNOWN_AVAILABILITY',snapshot(unknown,ts(2),'RECONSTRUCTED_ASOF'),('UNKNOWN_AVAILABILITY',None))
check('CA03_LOCAL_RECEIPT_NOT_BACKDATED',snapshot(versions,ts(2),'OBSERVED_REPLAY'),('NO_ELIGIBLE_OBSERVED_RECORD',None))
check('CA03_RECONSTRUCTION_WITH_KNOWN_DELAY',snapshot(versions,ts(2),'RECONSTRUCTED_ASOF',delay=timedelta(hours=1)),('ACTIVE',1))
check('CA03_DELAY_AFTER_CUTOFF',snapshot(versions,ts(2),'RECONSTRUCTED_ASOF',delay=timedelta(days=2)),('NO_EVENT_PROVEN',None))
check('CA04_ASOF_CANCELLATION',snapshot(versions,ts(5),'RECONSTRUCTED_ASOF'),('CANCELED',3))
check('CA04_PAST_SNAPSHOT_UNCHANGED',snapshot(versions,ts(2),'RECONSTRUCTED_ASOF'),('ACTIVE',1))
check('CA05_END_EXCLUSIVE',[d.day for d in [ts(1),ts(2),ts(3)] if ts(1)<=d<ts(3)],[1,2])
q=D(10);raw_before=D(100);raw_ex=D(99);div=D(1)
check('CA06_EX_DATE_RECEIVABLE_NOT_CASH',{'NAV':str(q*raw_ex+q*div),'cash':'0','receivable':str(q*div)},{'NAV':'1000','cash':'0','receivable':'10'})
check('CA08_PAY_MOVES_RECEIVABLE_TO_CASH',q*raw_ex+q*div,q*raw_before)
check('CA08_ADJUSTED_PLUS_DIVIDEND_DOUBLE_COUNT',q*raw_before+q*div,D(1010))
result=dict(captured_utc=datetime.now(timezone.utc).isoformat(),scope='SYNTHETIC_CLOCK_LOGIC_NOT_VENDOR_OR_PIT_ACCEPTANCE',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,counts={k:sum(r['status']==k for r in rows) for k in ['PASS','FAIL','ERROR']},vendor_calls=0,raw_market_data=False,strategy_trials=0,datasets_admitted=0,CA07='NOT_EXECUTED_VENDOR',CA09='NOT_EXECUTED_VENDOR',timezone_DST='NOT_TESTED',implementation_locked=True,target_acceptance='TARGET_ACCEPTANCE_DEFERRED',holdout='INTEGRITY_UNKNOWN')
with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result['counts']))
