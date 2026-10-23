"""Disposable evidence for library primitives and synthetic protocol states only."""
from pathlib import Path
import hashlib,json,sys,importlib.metadata
output=Path(__file__).with_name('result-01.json')
if output.exists():raise FileExistsError('Never overwrite a captured attempt')
sys.path.insert(0,sys.argv[1])
blocked=[]
def audit(event,args):
    if event in {'socket.connect','socket.getaddrinfo','socket.gethostbyname'}:
        blocked.append(event)
        raise RuntimeError('NETWORK_DISABLED_IN_PROBE')
sys.addaudithook(audit)
result={'observed_on':'2026-10-14','scope':'SYNTHETIC_PRIMITIVES_NOT_STRATEGY_BACKTEST',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'strategy_trials_executed':0,'target_acceptance':False,'checks':[]}
def check(name,value):result['checks'].append({'id':name,'status':'PASS' if bool(value) else 'FAIL'})
try:
    import numpy as np
    from statsmodels.stats.multitest import multipletests
    from arch.bootstrap import StationaryBootstrap
    result['versions']={n:importlib.metadata.version(n) for n in ['statsmodels','arch','numpy','scipy','pandas']}
    reject,pvals,*_=multipletests([.01,.04,.20],alpha=.05,method='holm')
    check('HOLM_KNOWN_VECTOR',np.allclose(pvals,[.03,.08,.20]))
    check('HOLM_FAKE_ALPHA_ONLY',reject.tolist()==[True,False,False])
    _,permuted,*_=multipletests([.20,.01,.04],alpha=.05,method='holm')
    check('HOLM_PRESERVES_CALLER_IDS',np.allclose(permuted,[.20,.03,.08]))
    try:
        _,nanvals,*_=multipletests([.01,np.nan,.2],method='holm')
        result['NaN_library_behavior']='RETURNED_NAN' if np.any(np.isnan(nanvals)) else 'RETURNED_VALUES'
    except Exception as e:result['NaN_library_behavior']=type(e).__name__
    check('EXTERNAL_REJECT_NAN_REQUIRED',not np.isfinite([.01,np.nan,.2]).all())
    check('EXTERNAL_REJECT_EMPTY_REQUIRED',len([])==0)
    a=np.arange(120,dtype=float)
    b=3*a
    def sample():
        boot=StationaryBootstrap(5,a,b,seed=1234)
        data,_=next(boot.bootstrap(1))
        return data
    first=sample();second=sample()
    check('BLOCK_PAIRED_COLUMNS',np.array_equal(first[1],3*first[0]))
    check('BLOCK_LENGTH_PRESERVED',len(first[0])==120)
    check('BLOCK_SEED_REPEATABLE',np.array_equal(first[0],second[0]))
    check('BLOCK_SAMPLE_NOT_ORIGINAL_ORDER',not np.array_equal(first[0],a))
except Exception as e:result['library_error_class']=type(e).__name__

# Paper fixture: numeric minutes are fictional, not exchange or broker deadlines.
def state(available,signal,dispatch,expiry,deadline,coverage=True):
    if None in [available,signal,dispatch,expiry,deadline]:return 'NOT_EVALUATED'
    if not coverage:return 'UNCERTAIN'
    if signal<available:return 'NOT_AVAILABLE'
    if dispatch<signal:return 'INVALID_CLOCK_ORDER'
    if dispatch>expiry:return 'EXPIRED'
    if dispatch>=deadline:return 'MISSED_DEADLINE'
    return 'ELIGIBLE_SYNTHETIC_ONLY'
cases=[('AVAILABLE_LATE',(15,10,20,40,30,True),'NOT_AVAILABLE'),
       ('EXPIRED',(5,10,45,40,50,True),'EXPIRED'),
       ('DEADLINE_MISSED',(5,10,30,40,30,True),'MISSED_DEADLINE'),
       ('COVERAGE_UNKNOWN',(5,10,20,40,30,False),'UNCERTAIN'),
       ('MISSING_CONTRACT',(None,10,20,40,30,True),'NOT_EVALUATED'),
       ('VALID_TIME_ORDER',(5,10,20,40,30,True),'ELIGIBLE_SYNTHETIC_ONLY'),
       ('REVERSE_TIME',(5,10,8,40,30,True),'INVALID_CLOCK_ORDER')]
for name,args,expected in cases:check(name,state(*args)==expected)
def evidence(required,observed):
    if required is None or observed is None:return 'NOT_EVALUATED'
    return 'INSUFFICIENT_EVIDENCE' if observed<required else 'SAMPLE_COUNT_ONLY_NOT_ALPHA'
check('SAMPLE_INSUFFICIENT',evidence(10,2)=='INSUFFICIENT_EVIDENCE')
check('SAMPLE_UNSPECIFIED',evidence(None,200)=='NOT_EVALUATED')
check('SAMPLE_COUNT_NOT_ALPHA',evidence(10,20)=='SAMPLE_COUNT_ONLY_NOT_ALPHA')
result.update(blocked_network_events=blocked,pass_count=sum(c['status']=='PASS' for c in result['checks']),
              total=len(result['checks']),risk_or_strategy_engine_tested=False)
with output.open('x',encoding='utf-8') as f:f.write(json.dumps(result,indent=2)+'\n')
print(json.dumps({'pass_count':result['pass_count'],'total':result['total'],'library_error':result.get('library_error_class'),'NaN_behavior':result.get('NaN_library_behavior')}))
