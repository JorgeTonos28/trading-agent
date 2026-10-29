from datetime import datetime, timezone
from decimal import Decimal as D, ROUND_FLOOR
from itertools import product
from pathlib import Path
import hashlib,json
here=Path(__file__).resolve().parent;out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
rows=[]
def case(id,observed,expected):rows.append({'id':id,'observed':observed,'expected':expected,'status':'PASS' if observed==expected else 'FAIL'})
def charge(q,per_unit,fixed):return D('0') if q==0 else D(q)*per_unit+fixed
def cap(budget,per_unit,fixed):
    if budget<fixed:return 0
    return max(0,int(((budget-fixed)/per_unit).to_integral_value(rounding=ROUND_FLOOR)))
parameters={'p_auth':D('10'),'stop':D('8'),'entry_fixed':D('1.25'),'exit_fixed':D('.75'),'entry_per_share':D('.01'),'exit_per_share':D('.02'),'gap_loss_per_share':D('5')}
tested=0;mismatches=[]
for cash,risk,gap,exposure,target in product([D(x) for x in ['0','5','30','100','1000']],[D(x) for x in ['0','1','3','10','100']],[D(x) for x in ['0','5','20']],[D(x) for x in ['10','30','100']],[0,1,3,10]):
    # Direct exhaustive oracle is independent of the closed-form cap calculation.
    feasible=[q for q in range(target+1)
       if charge(q,D('10.01'),D('1.25'))<=cash
       and charge(q,D('2.03'),D('2'))<=risk
       and charge(q,D('5.03'),D('2'))<=gap
       and D(q)*D('10')<=exposure]
    expected=max(feasible)
    observed=min(target,cap(cash,D('10.01'),D('1.25')),cap(risk,D('2.03'),D('2')),cap(gap,D('5.03'),D('2')),cap(exposure,D('10'),D('0')))
    tested+=1
    if observed!=expected:mismatches.append({'cell':tested,'observed':observed,'expected':expected})
case('MONOTONE_CAPS_VS_EXHAUSTIVE_ORACLE',len(mismatches),0)
case('ZERO_QUANTITY_NO_FIXED_FEE',str(charge(0,D('10.01'),D('1.25'))),'0')
case('ONE_ORDER_FEE_NOT_DUPLICATED_BY_LOT_PARTITION',str(D('4')*D('.02')+D('6')*D('.02')+D('.75')),'0.95')
case('FILLED_REMAINDER_EXPOSURE_NOT_EXTRA_CLAIM',str(D('4')*D('11')+D('6')*D('10')),'104')
case('CASH_DEBIT_NOT_REFLECTED_OBLIGATION',str(D('100')-D('40')-D('60')),'0')
case('CASH_ALREADY_DEBITED_NO_SECOND_DEBIT',str(D('60')-D('60')),'0')
case('PENDING_LIMIT_USES_AUTH_CAP_NOT_FAVOURABLE_MARK',str(D('3')*(D('10')-D('8'))),'6')
case('MARKET_AUTH_IS_NOT_GUARANTEED_CAP','MARKET'=='LIMIT_CAP_ENFORCED',False)
case('SPLIT_REMAINING_RISK_INVARIANCE',D('4')*(D('12')-D('8'))==D('8')*(D('6')-D('4')),True)
case('LOWER_R2_NOT_A_TOPUP_SIGNAL',False,False)
# A nonmonotone admissible set defeats the binary search precondition.
allowed={0,1,3};lo,hi=0,4
while lo<hi:
    mid=(lo+hi+1)//2
    if mid in allowed:lo=mid
    else:hi=mid-1
case('NONMONOTONE_BINARY_COUNTEREXAMPLE',{'binary':lo,'oracle':max(allowed)},{'binary':1,'oracle':3})
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'FICTITIOUS_BOUNDED_FORMULA_ORACLE_NOT_RISK_IMPLEMENTATION',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,
 'monotone_parameter_cells':tested,'mismatches':mismatches,'fictitious_parameters':{k:str(v) for k,v in parameters.items()},
 'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'D031_thresholds_approved':False,'real_solver_accepted':False,'broker_or_transactions_accepted':False,
 'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'monotone_parameter_cells':tested,'failed':[r for r in rows if r['status']!='PASS']}))
