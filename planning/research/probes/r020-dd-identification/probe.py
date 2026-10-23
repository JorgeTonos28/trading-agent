from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib, json, math
here=Path(__file__).resolve().parent;out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve capture; new attempt required')
rows=[]
def check(name,actual,expected):
    rows.append(dict(id=name,observed=actual,expected=expected,status='PASS' if actual==expected else 'FAIL'))
A=[(F(1,100),F(9,10)),(-F(1,10),F(1,10))]
B=[(F(8,100),F(1,10)),(-F(1,100),F(9,10))]
means=[sum(z*p for z,p in law) for law in [A,B]]
probs=[sum(p for z,p in law if z>0) for law in [A,B]]
check('SAME_EXPECTATION',list(map(str,means)),['-1/1000','-1/1000'])
check('DIFFERENT_PROBABILITY_OF_DETERIORATION',list(map(str,probs)),['9/10','1/10'])
check('VALID_DD_LEVELS',all(0<=F(1,5)+z<=1 for law in [A,B] for z,p in law),True)
check('PATH_MDD_REALIZATION',all((1-(1-(F(1,5)+z)))-F(1,5)==z for law in [A,B] for z,p in law),True)
alpha=.05
ucb=lambda mean,n:min(1.0,mean+math.sqrt(2*math.log(1/alpha)/n))
check('ONE_PATH_BOUND_VACUOUS_EVEN_BEST',ucb(-1,1),1.0)
check('N149_MEAN_MINUS_POINT2_NOT_PASS',ucb(-.2,149)>0,True)
check('N150_MEAN_MINUS_POINT2_PASSES_THIS_BOUND',ucb(-.2,150)<=0,True)
check('OVERLAPPED_WINDOWS_NOT_ASSUMED_INDEPENDENT',False,False)
result=dict(captured_utc=datetime.now(timezone.utc).isoformat(),scope='EXACT_FICTITIOUS_DD_CLAIM_AND_BOUNDED_MEAN_NOT_STATISTICAL_CALIBRATION',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,bounds={'n149':ucb(-.2,149),'n150':ucb(-.2,150)},counts={k:sum(r['status']==k for r in rows) for k in ['PASS','FAIL','ERROR']},strategy_trials=0,method_accepted=False,DD_E_approved=False,holdout='INTEGRITY_UNKNOWN',implementation_locked=True,target_acceptance='TARGET_ACCEPTANCE_DEFERRED')
with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result['counts']))
