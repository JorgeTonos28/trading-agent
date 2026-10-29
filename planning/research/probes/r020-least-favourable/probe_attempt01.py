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
r={'scope':'SYNTHETIC_LEAST_FAVOURABLE_SCREEN_NOT_STATISTICAL_ACCEPTANCE','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'observed_on':'2026-10-14','checks':[],'strategy_trials':0,'method_validated':False}
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
M=160;n=1008;burn=512;B=999;seed=20261016;L=20
r['settings']={'MC':M,'n':n,'burn':burn,'B':B,'block':L,'seed':seed,'method':'percentile','size':.95,'phi':.4,'correlation':.8,'margins_fixed_ADR019':True}
rng=np.random.default_rng(seed);start=time.monotonic();rows=[]
cases=[('NI_NULL',[.07,.08,.04],0.,.4,0),('CASH_NULL',[.04,0.,.04],.03,.4,1),('ES_NULL',[.12,.02,.04],.02,.8,2)]
for label,g,cash,ratio,target_index in cases:
 mu_case=np.log1p(g)/252;goal=ratio*analytic_es(mu_case[2],sigM);lo,hi=.00001,.02
 for _ in range(70):
  mid=(lo+hi)/2
  if analytic_es(mu_case[0],mid)>goal:hi=mid
  else:lo=mid
 sig_case=np.array([(lo+hi)/2,sigB,sigM])
 population=np.array([g[0]-g[1]+.01,g[0]-cash-.01,.8*analytic_es(mu_case[2],sigM)-analytic_es(mu_case[0],sig_case[0])])
 def current_contrasts(logs):
  cagr=np.expm1(252*logs.mean(axis=0));simple=np.expm1(logs)
  return np.array([cagr[0]-cagr[1]+.01,cagr[0]-cash-.01,.8*es(-simple[:,2])-es(-simple[:,0])])
 check(label+'_POPULATION_ONE_NULL_OTHER_POSITIVE',abs(population[target_index])<1e-12 and all(population[i]>0 for i in range(3) if i!=target_index))
 counts=np.zeros(3,int);andcount=0;errors=0
 for attempt in range(M):
  common=rng.normal(size=(n+burn,1));own=rng.normal(size=(n+burn,3));innov=(math.sqrt(.8)*common+math.sqrt(.2)*own)*sig_case
  centered=np.zeros_like(innov)
  for t in range(1,len(centered)):centered[t]=.4*centered[t-1]+math.sqrt(1-.4*.4)*innov[t]
  logs=centered[burn:]+mu_case
  try:
   if not np.isfinite(logs).all():raise ValueError('NONFINITE_INPUT')
   lower=StationaryBootstrap(L,logs,seed=seed+attempt).conf_int(current_contrasts,B,method='percentile',size=.95,tail='lower')[0]
   if not np.isfinite(lower).all():raise ValueError('NONFINITE_BOUND')
   passed=lower>=0;counts+=passed;andcount+=bool(passed.all())
  except Exception:errors+=1
 row={'case':label,'target_null_index':target_index,'population_contrasts':population.tolist(),'sigma':sig_case.tolist(),'MC_total':M,'errors':errors,'endpoint_pass_counts':counts.tolist(),'AND_false_qualification_count':andcount,'MC_intervals':[]}
 for count in [int(counts[target_index]),andcount]:
  low,high=proportion_confint(count,M,alpha=.05,method='wilson');row['MC_intervals'].append({'count':count,'rate':count/M,'Wilson95':[float(low),float(high)]})
 rows.append(row)
 print(label+' completed',flush=True)
r['screen']=rows;check('CAPTURED_THREE_NULL_CASES_NOT_COVERAGE_PASS',len(rows)==3)
r.update(pass_count=sum(c['status']=='PASS' for c in r['checks']),total=len(r['checks']),elapsed_seconds=time.monotonic()-start,blocked_network_events=blocked,versions={'numpy':np.__version__,'arch':'8.0.0','statsmodels':'0.15.0'})
with out.open('x',encoding='utf-8') as f:f.write(json.dumps(r,indent=2,allow_nan=False)+'\n')
print(json.dumps({'checks':r['pass_count'],'total':r['total'],'screen_errors':sum(z['errors'] for z in rows),'elapsed':r['elapsed_seconds']}))
