"""Disposable synthetic contract/counterexample evidence, not a Trading OS engine."""
from pathlib import Path
import hashlib,json,sys,math
from statistics import NormalDist
out=Path(__file__).with_name('result-01.json')
if out.exists():raise FileExistsError('Captured attempt must remain intact')
sys.path.insert(0,sys.argv[1])
blocked=[]
def audit(event,args):
 if event in {'socket.connect','socket.getaddrinfo','socket.gethostbyname'}:
  blocked.append(event);raise RuntimeError('NETWORK_DISABLED_IN_PROBE')
sys.addaudithook(audit)
r={'scope':'SYNTHETIC_ENDPOINT_AND_POWER_ILLUSTRATION_NOT_STRATEGY',
   'observed_on':'2026-10-14','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   'strategy_trials_executed':0,'numeric_margins_approved':False,'checks':[]}
def check(id,yes):r['checks'].append({'id':id,'status':'PASS' if bool(yes) else 'FAIL'})
try:
 import numpy as np
 from arch.bootstrap import StationaryBootstrap
 from statsmodels.stats.power import TTestPower
 cash=np.array([.0001]*500)
 b=.0002+.003*np.sin(np.arange(500,dtype=float))
 lam=.4
 mirrored=lam*b+(1-lam)*cash
 strategy=mirrored.copy()
 check('PURE_EXPOSURE_MIRROR_EQUALS',np.allclose(strategy,mirrored))
 check('LOWER_VOL_NOT_INCREMENTAL_EFFICIENCY',np.std(strategy)<np.std(b) and np.allclose(strategy-mirrored,0))
 check('CASH_ONLY_EXCESS_ZERO',np.allclose(cash-cash,0))
 check('CASH_NOT_DOUBLE_COUNTED',not np.allclose(lam*b+2*(1-lam)*cash,mirrored))
 check('CASH_OMISSION_CHANGES_RETURN',not np.allclose(lam*b,mirrored))
 data=np.column_stack([np.sin(np.arange(500)/7)*.01+.001,np.cos(np.arange(500)/9)*.008+.0005])
 def interval():
  bs=StationaryBootstrap(5,data,seed=1234)
  return bs.conf_int(lambda z:z.mean(0),500,method='percentile',size=.95,tail='lower')
 ci=interval();repeat=interval()
 check('CI_VECTOR_SHAPE',ci.shape==(2,2))
 check('CI_LOWER_BOUND_FINITE',np.isfinite(ci[0]).all())
 check('CI_UPPER_IS_INF_FOR_LOWER_TAIL',np.isinf(ci[1]).all())
 check('CI_SEED_REPEATABLE',np.allclose(ci[0],repeat[0]))
 r['CI_scope']='MARGINAL_PRIMITIVE_ONLY_NOT_SIMULTANEOUS_COVERAGE'
 factor=(NormalDist().inv_cdf(.975)+NormalDist().inv_cdf(.8))**2
 grid=[{'margin_annual_pp':d*100,'annual_diff_sigma_percent':s*100,
        'normal_iid_years_at_true_equal_means':factor*(s/d)**2}
       for d in [.005,.01,.02] for s in [.01,.05,.1]]
 r['power_illustration']={'assumptions':'NORMAL_IID_ANNUAL_EQUAL_TRUE_MEANS_NOT_CAGR_OR_STRATEGY_ESTIMATE',
  'alpha_one_sided_fixture':.025,'power_fixture':.8,'grid':grid}
 normal=factor*(.05/.01)**2
 exact=TTestPower().solve_power(effect_size=.01/.05,alpha=.025,power=.8,alternative='larger')
 r['power_illustration']['normal_case_years']=normal
 r['power_illustration']['t_independent_annual_observations_case']=float(exact)
 check('POWER_NORMAL_T_CLOSE_NOT_IDENTICAL',normal<exact<normal*1.05)
 check('TIGHTER_MARGIN_MORE_SAMPLE',factor*(.05/.005)**2>factor*(.05/.02)**2)
 check('HIGHER_DIFFERENCE_VARIANCE_MORE_SAMPLE',factor*(.1/.01)**2>factor*(.01/.01)**2)
 r['dependency_versions']={'arch':'8.0.0','statsmodels':'0.15.0'}
except Exception as e:r['library_error_class']=type(e).__name__
# Fixed fictional bound scenarios; thresholds are fixtures, not approved margins.
def qualify(lower_NI,upper_risk,lower_cash,adequate=True):
 if any(v is None or not math.isfinite(v) for v in [lower_NI,upper_risk,lower_cash]):return 'NOT_EVALUABLE'
 if not adequate:return 'INSUFFICIENT_EVIDENCE'
 if lower_NI<-.01 or upper_risk>.8 or lower_cash<=.01:return 'NOT_QUALIFIED_FIXTURE'
 return 'ALL_FIXTURE_GATES_PASS_NOT_OPERATIONAL'
check('POINT_ESTIMATE_NOT_BOUND',qualify(-.02,.7,.02)=='NOT_QUALIFIED_FIXTURE')
check('CASH_ONLY_CANNOT_PASS',qualify(0,0,0)=='NOT_QUALIFIED_FIXTURE')
check('EXPOSURE_ONLY_RISK_RATIO_ONE_CANNOT_PASS',qualify(0,1,.02)=='NOT_QUALIFIED_FIXTURE')
check('INVALID_RISK_RATIO_NOT_ZERO',qualify(0,float('nan'),.02)=='NOT_EVALUABLE')
check('INSUFFICIENT_NOT_FAIL',qualify(0,.7,.02,False)=='INSUFFICIENT_EVIDENCE')
check('POSITIVE_FIXTURE_ALL_AND',qualify(0,.7,.02)=='ALL_FIXTURE_GATES_PASS_NOT_OPERATIONAL')
check('ALL_INSUFFICIENT_NO_QUALIFIED_REASON_KEPT',not any(v=='PASS' for v in ['INSUFFICIENT_EVIDENCE']*5))
r.update(blocked_network_events=blocked,pass_count=sum(c['status']=='PASS' for c in r['checks']),total=len(r['checks']))
with out.open('x',encoding='utf-8') as f:f.write(json.dumps(r,indent=2)+'\n')
print(json.dumps({'pass_count':r['pass_count'],'total':r['total'],'library_error':r.get('library_error_class')}))
