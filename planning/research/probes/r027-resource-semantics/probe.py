from pathlib import Path
from decimal import Decimal as D
from datetime import datetime, timezone
import hashlib, json
here=Path(__file__).resolve().parent;out=here/'result-01.json'
if out.exists(): raise FileExistsError('New immutable attempt required')
rows=[]
def norm(x):
    if isinstance(x,D): return str(x.normalize())
    if isinstance(x,(list,tuple)): return [norm(v) for v in x]
    if isinstance(x,dict): return {k:norm(v) for k,v in x.items()}
    return x
def check(name,value,expected):
    value=norm(value);expected=norm(expected)
    rows.append(dict(id=name,observed=value,expected=expected,status='PASS' if value==expected else 'FAIL'))
f,l,c=D(4),D(6),D(0);mark=D(110);price=D(100)
check('F4_L6_EXPOSURE',f*mark+l*price,D(1040))
check('CLAIM_IS_NOT_EXTRA_QTY',f*mark+l*price+l*price,D(1640))
check('PARTIAL_FILL_CASH_FREE',D(1000)-f*price-l*price,D(0))
check('PENDING_CANCEL_RETAINS_HOLD',D(600)-D(600),D(0))
check('CANCEL_REMAINDER_KEEPS_FILLED',(f,D(600)-D(0)),(D(4),D(600)))
check('STALE_CASH_RETAINS_FILL_DEBIT',D(1000)-D(400)-D(600),D(0))
check('JOINT_FIXED_EXIT_FEE',(D(4)/10*5+D(6)/10*5),D(5))
check('GAIN_R2_NOT_ENTRY_RISK',(D(10)*(D(120)-D(110)),D(0)),(D(100),D(0)))
check('GAP_FROM_CURRENT_NAV',D(10)*(D(100)-D(80)),D(200))
check('STOP_PLUS_EXCESS_GAP',D(10)*(D(100)-D(90))+D(10)*(D(90)-D(80)),D(200))
check('DO_NOT_ADD_WHOLE_GAP_TO_STOP',D(100)+D(200),D(300))
check('PARTIAL_COVERAGE_KNOWN_PART_AND_UNKNOWN_TOTAL',{'covered':D(4)*(100-90),'uncovered_qty':6,'aggregate_status':'UNCERTAIN'},{'covered':D(40),'uncovered_qty':6,'aggregate_status':'UNCERTAIN'})
check('CROSSED_STOP_DOMAIN_VALID',0<D(90)<D(80),False)
check('PENDING_AUTH_PRICE_NOT_FAVORABLE_MARK',D(6)*(D(105)-D(90)),D(90))
for a in [D(2),D('0.5')]:
    check('SPLIT_R2_INVARIANT_'+str(a),(D(10)*a)*(D(100)/a-D(90)/a),D(100))
grid=[]
for filled in range(11):
    for canceled in range(11-filled):
        live=10-filled-canceled
        base=D(1000)-D(100)*filled
        free=base-D(100)*live
        stale_free=D(1000)-D(100)*filled-D(100)*live
        expo=D(110)*filled+D(100)*live
        unit_sum=sum([D(110)]*filled+[D(100)]*live,D(0))
        grid.append(dict(filled=filled,live=live,canceled=canceled,pass_cash=free==D(100)*canceled,pass_stale=stale_free==free,pass_exposure=expo==unit_sum))
check('FINITE_GRID_66_CONSERVATION',len(grid)==66 and all(r['pass_cash'] and r['pass_stale'] and r['pass_exposure'] for r in grid),True)
target=15;lot=2;cash=D(35)
feasible=[q for q in range(0,target+1,lot) if (D(0) if q==0 else D(7)*q+D(2))<=cash]
check('LOT_FEE_ENUMERATION',max(feasible),4)
costs=[0,10,30,20,40];feasible=[q for q,cost in enumerate(costs) if cost<=25]
check('NONMONOTONE_FEASIBLE_SET',feasible,[0,1,3])
lo,hi=0,4
while lo<hi:
    mid=(lo+hi+1)//2
    if costs[mid]<=25:lo=mid
    else:hi=mid-1
check('BINARY_WITHOUT_PROOF_MISSES_FEASIBLE',{'binary':lo,'enumerated':max(feasible)},{'binary':1,'enumerated':3})
check('UNKNOWN_REQUIRED_IS_NOT_ZERO',all(v is not None for v in [D(5),None,D(7)]),False)
result=dict(captured_utc=datetime.now(timezone.utc).isoformat(),scope='SYNTHETIC_RESOURCE_ALGEBRA_NOT_RISK_ENGINE',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows,grid=grid,counts={k:sum(r['status']==k for r in rows) for k in ['PASS','FAIL','ERROR']},financial_interfaces=0,network_calls=0,strategy_trials=0,thresholds_approved=False,D035_closed=False,implementation_locked=True,target_acceptance='TARGET_ACCEPTANCE_DEFERRED')
with out.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
print(json.dumps(result['counts']))
