from pathlib import Path
from decimal import Decimal as D, getcontext
from itertools import permutations
import hashlib,json,platform,socket
from datetime import date
getcontext().prec=40
def deny(*a,**k): raise RuntimeError('NETWORK_DISABLED_IN_PROBE_NOT_OS_ISOLATION')
socket.socket=deny; socket.create_connection=deny
here=Path(__file__).resolve().parent
out=here/'result-01.json'
if out.exists(): raise RuntimeError('APPEND_NEW_ATTEMPT_DO_NOT_OVERWRITE_CAPTURE')
checks=[]
def check(name,ok,actual=None): checks.append({'id':name,'pass':bool(ok),'actual':str(actual) if actual is not None else None})
def path(rs):
    v=[D(1)]
    for r in rs:
        if not r.is_finite() or r<=-1: raise ValueError('INVALID_RETURN_OR_NONPOSITIVE_NAV')
        v.append(v[-1]*(1+r))
    return v
def mdd(v,prior_peak=None):
    if not v or any(not x.is_finite() or x<=0 for x in v): raise ValueError('INVALID_NAV')
    peak=max(v[0],prior_peak) if prior_peak is not None else v[0]
    dd=D(0)
    for x in v: peak=max(peak,x); dd=max(dd,1-x/peak)
    return dd
def es95(rs):
    losses=sorted([-x for x in rs],reverse=True); mass=D(len(rs))*D('.05'); left=mass; total=D(0)
    for x in losses:
        take=min(D(1),left);total+=take*x;left-=take
        if left==0:break
    return total/mass
def var(rs):
    mu=sum(rs)/len(rs);return sum((x-mu)**2 for x in rs)/(len(rs)-1)
a=list(map(D,['.1','.1','-.1','-.1']));b=list(map(D,['.1','-.1','.1','-.1']))
av,bv=path(a),path(b); da,db=mdd(av),mdd(bv)
check('ORDERED_MDD_ORACLE',da==D('.19') and db==D('.109'),[str(da),str(db)])
check('SAME_TERMINAL_WEALTH',av[-1]==bv[-1]==D('.9801'),av[-1])
check('SAME_MARGINAL_ES95',es95(a)==es95(b)==D('.1'),es95(a))
check('SAME_SAMPLE_VARIANCE',var(a)==var(b),var(a))
check('INITIAL_NAV_COUNTS',mdd([D(1),D('.9')])==D('.1'))
check('INHERITED_PEAK_SEPARATE',mdd([D(1),D(1)],D('1.25'))==D('.2') and mdd([D(1),D(1)])==0)
# Recovery from time0 peak: final below it => right censored, observed lower bound2, not exact0.
cv=path([D('-.1'),D('.01')]); recover=next((i for i,x in enumerate(cv[1:],1) if x>=cv[0]),None)
check('RECOVERY_CENSORED_NOT_ZERO',recover is None and len(cv)-1==2,{'right_censored':recover is None,'observed_duration_lower_bound':len(cv)-1})
rows=[{'returns':[str(x) for x in r],'MDD':str(mdd(path(r)))} for r in sorted(set(permutations(a)))]
mean_dd=sum(D(x['MDD']) for x in rows)/len(rows)
check('FINITE_POPULATION_ENUMERATION',len(rows)==6 and min(D(x['MDD']) for x in rows)==D('.1') and max(D(x['MDD']) for x in rows)==D('.19'),mean_dd)
check('PAIRED_IDENTICAL_PATH_ZERO',all(mdd(path(r))-mdd(path(r))==0 for r in set(permutations(a))))
check('UNPAIRED_ORDER_CHANGES_CONTRAST',da-db==D('.081'),da-db)
observed=[D(1),D('1.1')]; common_prefix=list(observed)
future_good=mdd(observed+[D('1.1')])-mdd(common_prefix+[D('1.1')])
future_adverse=mdd(observed+[D('.55')])-mdd(common_prefix+[D('.99')])
check('PREFIX_DOES_NOT_IDENTIFY_FUTURE',future_good==0 and future_adverse==D('.4'),[str(future_good),str(future_adverse)])
for name,rs in [('NONPOSITIVE_NAV_REJECT',[D('-1')]),('NONFINITE_REJECT',[D('NaN')])]:
    try:path(rs);check(name,False)
    except ValueError:check(name,True)
calendar_bound=(date(2005,1,1)-date(2004,11,18)).days+1
check('GLD_WARMUP_CALENDAR_UPPER_BOUND',calendar_bound<200,calendar_bound)
result={'observed_on':'2026-10-15','attempt':'E7-01','scope':'ARITHMETIC_SYNTHETIC_PATH_PROPERTIES_ONLY','python':platform.python_version(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'pass_count':sum(x['pass'] for x in checks),'total':len(checks),'finite_population_MDD':rows,'finite_population_expected_MDD':str(mean_dd),'method_validated':False,'statistical_calibration':False,'engine_tested':False,'strategy_trials':0,'history_accessed':False,'incremental_spend':0,'implementation_locked':True,'target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({'checks_pass':result['pass_count'],'total':result['total'],'method_validated':False}));raise SystemExit(0 if all(x['pass'] for x in checks) else 1)
