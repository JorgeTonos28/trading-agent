"""Synthetic screening of actual endpoint functionals, never trading implementation."""
from pathlib import Path
import hashlib,json,math,sys,time
from statistics import NormalDist
source=Path(__file__);out=source.with_name('result-01.json')
if out.exists():raise FileExistsError('Preserve captured attempt')
sys.path.insert(0,sys.argv[1]);blocked=[]
def audit(event,args):
 if event in {'socket.connect','socket.getaddrinfo','socket.gethostbyname'}:
  blocked.append(event);raise RuntimeError('NETWORK_DISABLED')
sys.addaudithook(audit)
import numpy as np
from arch.bootstrap import StationaryBootstrap
from statsmodels.stats.proportion import proportion_confint
nd=NormalDist();q=.95;tau=1-q;z=nd.inv_cdf(tau)
def analytic_es(mu,sigma):return 1-math.exp(mu+sigma*sigma/2)*nd.cdf(z-sigma)/tau
mu=np.log1p([.05,.06,.04])/252;sigB=.008;sigM=.004;target=.8*analytic_es(mu[2],sigM)
lo,hi=.00001,.02
for _ in range(70):
 mid=(lo+hi)/2
 if analytic_es(mu[0],mid)>target:hi=mid
 else:lo=mid
sigS=(lo+hi)/2;sig=np.array([sigS,sigB,sigM])
r={'scope':'SYNTHETIC_ENDPOINT_SCREEN_NOT_STATISTICAL_ACCEPTANCE','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'observed_on':'2026-10-14','checks':[],'strategy_trials':0,'method_validated':False}
def check(name,ok):r['checks'].append({'id':name,'status':'PASS' if bool(ok) else 'FAIL'})
def es(loss):
 x=np.sort(np.asarray(loss,float))[::-1];mass=tau*len(x);k=int(math.floor(mass));f=mass-k
 return (x[:k].sum()+(f*x[k] if k<len(x) else 0))/mass
def contrasts(logs):
 cagr=np.expm1(252*logs.mean(axis=0));simple=np.expm1(logs)
 return np.array([cagr[0]-cagr[1]+.01,cagr[0]-.04-.01,.8*es(-simple[:,2])-es(-simple[:,0])])
check('NI_POPULATION_BOUNDARY',abs(math.expm1(252*mu[0])-math.expm1(252*mu[1])+.01)<1e-12)
check('CASH_POPULATION_BOUNDARY',abs(math.expm1(252*mu[0])-.04-.01)<1e-12)
check('ES_POPULATION_BOUNDARY',abs(analytic_es(mu[0],sigS)-target)<1e-12)
check('TAIL_POSITIVE_REFERENCE',analytic_es(mu[2],sigM)>0)
check('FRACTIONAL_MASS_NO_TIE_OVERCOUNT',math.isclose(es([10]*19+[0]),10))
path=np.array([100.,110.,90.,95.,105.]);hwm=np.maximum.accumulate(path);dd=1-path/hwm
check('DRAWDOWN_BASE_NOT_RESET_AT_YEAR',math.isclose(dd[-1],1-105/110))
check('RECOVERY_CENSORED_NOT_ZERO',path[-1]<hwm[-1] and dd[-1]>0)
M=80;n=1008;burn=512;B=499;seed=20261015;L=20
r['settings']={'MC':M,'n':n,'burn':burn,'B':B,'block':L,'seed':seed,'method':'basic','size':.95,'correlation_innovations':.8,'population_CAGR':[.05,.06,.04],'sigma_log_daily':sig.tolist(),'q':q,'annualization_fixture':252,'margins_not_fitted':True}
r['population_ES']={'S':analytic_es(mu[0],sigS),'M':analytic_es(mu[2],sigM),'target_ratio':.8,'boundary_residual':analytic_es(mu[0],sigS)-target}
rng=np.random.default_rng(seed);start=time.monotonic();rows=[]
for label,phi in [('IID_LOGNORMAL',0.),('AR_LOGNORMAL_04',.4)]:
 counts=np.zeros(3,int);andcount=0;errors=0
 for attempt in range(M):
  common=rng.normal(size=(n+burn,1));own=rng.normal(size=(n+burn,3));innov=(math.sqrt(.8)*common+math.sqrt(.2)*own)*sig
  centered=innov.copy()
  if phi:
   centered=np.zeros_like(innov)
   for t in range(1,len(centered)):centered[t]=phi*centered[t-1]+math.sqrt(1-phi*phi)*innov[t]
  logs=centered[burn:]+mu
  try:
   if not np.isfinite(logs).all():raise ValueError('NONFINITE_INPUT')
   lower=StationaryBootstrap(L,logs,seed=seed+attempt).conf_int(contrasts,B,method='basic',size=.95,tail='lower')[0]
   if not np.isfinite(lower).all():raise ValueError('NONFINITE_BOUND')
   passed=lower>=0;counts+=passed;andcount+=bool(passed.all())
  except Exception:errors+=1
 row={'DGP':label,'MC_total':M,'errors':errors,'endpoint_boundary_rejections':counts.tolist(),'AND_boundary_rejections':andcount,'MC_intervals':[]}
 for count in list(counts)+[andcount]:
  lower,upper=proportion_confint(int(count),M,alpha=.05,method='wilson');row['MC_intervals'].append({'count':int(count),'rate':float(count/M),'Wilson95':[float(lower),float(upper)]})
 rows.append(row)
r['screen']=rows;check('CAPTURED_TWO_DGPS_NOT_COVERAGE_PASS',len(rows)==2)
r.update(pass_count=sum(c['status']=='PASS' for c in r['checks']),total=len(r['checks']),elapsed_seconds=time.monotonic()-start,blocked_network_events=blocked,versions={'numpy':np.__version__,'arch':'8.0.0','statsmodels':'0.15.0'})
with out.open('x',encoding='utf-8') as f:f.write(json.dumps(r,indent=2,allow_nan=False)+'\n')
print(json.dumps({'checks':r['pass_count'],'total':r['total'],'screen_errors':sum(z['errors'] for z in rows),'elapsed':r['elapsed_seconds']}))
