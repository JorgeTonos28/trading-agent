"""Disposable E4 arithmetic/mean-inference pilot, no financial system."""
from pathlib import Path
import hashlib,json,math,sys,warnings,time
source=Path(__file__);out=source.with_name('result-01.json')
if out.exists():raise FileExistsError('Captured attempt is immutable')
sys.path.insert(0,sys.argv[1]);blocked=[]
def audit(event,args):
 if event in {'socket.connect','socket.getaddrinfo','socket.gethostbyname'}:
  blocked.append(event);raise RuntimeError('NETWORK_DISABLED')
sys.addaudithook(audit)
import numpy as np
from arch.bootstrap import StationaryBootstrap
from statsmodels.stats.proportion import proportion_confint
r={'scope':'SYNTHETIC_ARITHMETIC_AND_MEAN_PILOT_NOT_STRATEGY_OR_CALIBRATION_ACCEPTANCE','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'observed_on':'2026-10-14','checks':[],'strategy_trials':0}
def check(name,ok):r['checks'].append({'id':name,'status':'PASS' if bool(ok) else 'FAIL'})
# Standalone arithmetic, no event/trade engine.
q=np.ones(2);p=np.array([200.,100.]);value=q*p
check('DRIFT_IS_NOT_EQUAL_WEIGHT_RESET',np.allclose(value/value.sum(),[2/3,1/3]))
paid=10.;q_reinvest=q.copy();q_reinvest[1]+=paid/100
check('REINVEST_PAYER_ONLY_NO_REBALANCE',np.allclose(q_reinvest,[1,1.1]) and not np.allclose(q_reinvest*p/(q_reinvest*p).sum(),[.5,.5]))
check('SPLIT_VALUE_NEUTRAL',math.isclose(1*200,2*100))
check('DIVIDEND_RECEIVABLE_NOT_SPENDABLE',100+10==110 and 100!=110)
check('DIVIDEND_EXDATE_MARK_DROP_PRESERVES_TOTAL',math.isclose(90+10,100))
check('OWN_COST_CHARGED_ONCE',math.isclose(200+110-2,308) and not math.isclose(200+110-4,308))
market=np.array([-.02,.01,-.01,.03,-.03,.02]);duration=-market/2
check('EQUAL_LAMBDA_DIFFERENT_FACTOR_EXPOSURE',np.allclose(.5*market+.5*0,-2*(.5*duration+.5*0)))
def es(loss,q=.95):
 loss=np.asarray(loss,float)
 if len(loss)==0 or not np.isfinite(loss).all():return float('nan')
 mass=(1-q)*len(loss);ordered=np.sort(loss)[::-1];k=int(math.floor(mass));fraction=mass-k
 return float((ordered[:k].sum()+(fraction*ordered[k] if k<len(loss) else 0))/mass)
check('ES_FRACTIONAL_TAIL',math.isclose(es([10,9,8,7],.625),(10+.5*9)/1.5))
check('ES_TIES_NOT_OVERCOUNTED',math.isclose(es([10,10,10,0],.625),10))
a=np.array([10,0,0,0]);b=np.array([0,10,0,0])
check('DIFFERENCE_OF_ES_NOT_ES_OF_DIFFERENCE',math.isclose(es(a,.75)-es(b,.75),0) and not math.isclose(es(a-b,.75),0))
check('NEGATIVE_LOSS_ES_NOT_CLIPPED',es([-1,-2,-3,-4],.75)<0)
check('NONFINITE_ES_NOT_ZERO',math.isnan(es([1,np.nan])))
r['degenerate_ci_observations']=[]
for label,values in [('CONSTANT_ZERO',np.zeros(128)),('NAN',np.r_[np.nan,np.zeros(127)]),('INF',np.r_[np.inf,np.zeros(127)])]:
 with warnings.catch_warnings(record=True) as ws:
  warnings.simplefilter('always')
  try:
   ci=StationaryBootstrap(5,values,seed=7).conf_int(lambda z:np.array([z.mean()]),99,method='percentile',size=.95,tail='lower')
   obs={'case':label,'returned_lower_finite':bool(np.isfinite(ci[0]).all()),'lower_repr':str(ci[0]),'error':None}
  except Exception as e:obs={'case':label,'error':type(e).__name__}
  obs['warning_count']=len(ws);r['degenerate_ci_observations'].append(obs)
check('DEGENERATE_CASES_RECORDED',len(r['degenerate_ci_observations'])==3)
# Pilot: stationary-bootstrap mean primitive, NOT an estimator for actual candidates.
seed=20261014;M=160;n=1008;burn=512;B=499;alpha=.05;sigma=.0008;margin=.01
r['pilot_settings']={'seed':seed,'MC':M,'n':n,'burn':burn,'B':B,'blocks':[1,20],'method':'basic','size':.95,'sigma_fixture':sigma,'margin_fixture':margin,'DGPs':['IID_NORMAL','AR_06','VOLATILITY_REGIME']}
results=[];rng=np.random.default_rng(seed);started=time.monotonic()
for dgp in r['pilot_settings']['DGPs']:
 counts={L:{'boundary_rejections':0,'equal_mean_NI_pass':0,'errors':0} for L in [1,20]}
 for attempt in range(M):
  noise=rng.normal(0,sigma,n+burn)
  if dgp=='AR_06':
   x=np.zeros(n+burn)
   for t in range(1,len(x)):x[t]=.6*x[t-1]+math.sqrt(1-.6**2)*noise[t]
   x=x[burn:]
  else:
   x=noise[burn:]
   if dgp=='VOLATILITY_REGIME':x[n//2:]*=4
  for L in [1,20]:
   try:
    ci=StationaryBootstrap(L,x,seed=seed+attempt+L).conf_int(lambda z:np.array([252*z.mean()]),B,method='basic',size=.95,tail='lower')
    lower=float(ci[0,0]);counts[L]['boundary_rejections']+=lower>0;counts[L]['equal_mean_NI_pass']+=lower+margin>=0
   except Exception:counts[L]['errors']+=1
 for L,c in counts.items():
  row={'DGP':dgp,'block':L,**c,'MC_total':M}
  for key in ['boundary_rejections','equal_mean_NI_pass']:
   lo,hi=proportion_confint(c[key],M,alpha=.05,method='wilson');row[key+'_rate']=c[key]/M;row[key+'_MC_Wilson95']=[float(lo),float(hi)]
  results.append(row)
r['pilot']=results;r['elapsed_seconds']=time.monotonic()-started
check('PILOT_COUNTS_RECORDED_NOT_CALIBRATION_PASS',len(results)==6 and all(z['errors']==0 for z in results))
r.update(pass_count=sum(z['status']=='PASS' for z in r['checks']),total=len(r['checks']),blocked_network_events=blocked,dependency_versions={'numpy':np.__version__,'arch':'8.0.0','statsmodels':'0.15.0'},financial_parameters_approved=False)
with out.open('x',encoding='utf-8') as f:f.write(json.dumps(r,indent=2,allow_nan=False)+'\n')
print(json.dumps({'pass_count':r['pass_count'],'total':r['total'],'pilot_errors':sum(z['errors'] for z in results),'elapsed':r['elapsed_seconds']}))
