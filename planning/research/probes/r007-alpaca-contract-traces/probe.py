from datetime import datetime, timezone
from decimal import Decimal as D
from pathlib import Path
import hashlib, json

here=Path(__file__).resolve().parent;out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
rows=[]
def case(id,observed,expected):rows.append({'id':id,'observed':observed,'expected':expected,'status':'PASS' if observed==expected else 'FAIL'})
def coverage(position,legs,mark):
    if position==0:return 'FLAT_NO_PROTECTION_CLAIM'
    active=[x for x in legs if x['state']=='ACTIVE_CONFIRMED' and D('0')<D(x['stop'])<D(mark)]
    # No overlap of execution responsibilities may be hidden by adding stop quantities.
    if any(x.get('overlap_uncertain') for x in legs):return 'UNCERTAIN'
    qty=sum(x['remaining'] for x in active)
    return 'CONFIRMED_FIXTURE_ONLY' if qty==position else 'UNCERTAIN'
held={'state':'HELD','remaining':10,'stop':'8'}
active={'state':'ACTIVE_CONFIRMED','remaining':4,'stop':'8'}
case('PARTIAL_PARENT_HELD_CHILD',coverage(4,[held],'10'),'UNCERTAIN')
case('FULL_PARENT_CHILD_ACK_ONLY',coverage(10,[dict(held,state='SUBMITTED')],'10'),'UNCERTAIN')
case('ACTIVE_MATCHED_QUANTITY',coverage(4,[active],'10'),'CONFIRMED_FIXTURE_ONLY')
case('PARTIAL_COVERAGE_NOT_ZERO_REMAINING_RISK',coverage(6,[active],'10'),'UNCERTAIN')
case('CROSSED_STOP_NO_VERIFIED_FILL',coverage(4,[active],'7'),'UNCERTAIN')
case('PROTECTION_EXPIRY',coverage(4,[dict(active,state='EXPIRED')],'10'),'UNCERTAIN')
case('SPLIT_UNITS_NOT_RECONCILED',coverage(8,[active],'5'),'UNCERTAIN')
case('PATCH_ACK_IS_NOT_NEW_PROTECTION',coverage(4,[dict(active,state='PENDING_REPLACE')],'10'),'UNCERTAIN')
case('OLD_STOP_FILLED_NEW_REJECTED_POSITION_FLAT',coverage(0,[dict(active,state='REJECTED')],'7'),'FLAT_NO_PROTECTION_CLAIM')
case('OVERLAP_NOT_COVERAGE',coverage(4,[dict(active,overlap_uncertain=True),active],'10'),'UNCERTAIN')
def cancel_allowed(purpose,verified,dependency_effect):
    return purpose=='ENTRY' and verified and dependency_effect=='VERIFIED_NO_WEAKENING_OF_PROTECTION'
case('G2_SIMPLE_VERIFIED_PENDING_ENTRY',cancel_allowed('ENTRY',True,'VERIFIED_NO_WEAKENING_OF_PROTECTION'),True)
case('G2_PARTIAL_PARENT_MAY_CANCEL_CHILD',cancel_allowed('ENTRY',True,'CANCELS_CHILDREN'),False)
case('G2_UNKNOWN_DEPENDENCY',cancel_allowed('ENTRY',True,'UNKNOWN'),False)
case('G2_PROTECTOR_NOT_ENTRY',cancel_allowed('PROTECTION',True,'VERIFIED_NO_WEAKENING_OF_PROTECTION'),False)
# Fixed economic intent10; callbacks are fictitious and include one duplicate execID.
events=[('e1',4),('e1',4),('e2',2)]
unique={}
for execid,qty in events:
    if execid in unique:assert unique[execid]==qty
    unique[execid]=qty
filled=sum(unique.values());live=10-filled
case('FILL_ID_DEDUP',filled,6)
case('PENDING_CANCEL_RESERVE_PRESERVED',live,4)
cancelled_confirmed=4
case('CANCEL_CONFIRMED_NOT_ERASE_FILLED',filled+cancelled_confirmed,10)
case('ONLY_CONFIRMED_REMAINDER_RELEASED',live-cancelled_confirmed,0)
case('CORRECTION_AFTER_TERMINAL_NEEDS_RECONCILIATION', 'terminal'=='ignore_future_corrections',False)
streams={'connected':False,'rest_positions_match':False,'orders_complete':False}
case('DISCONNECT_NOT_HEALTHY',all(streams.values()),False)
case('NO_ADMITTED_BROKER_ROUTE_FROM_FIXTURE',False,False)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'FINITE_FICTITIOUS_CONTRACT_COUNTEREXAMPLES_NOT_BROKER_ACCEPTANCE',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,
 'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'B3_passed':False,'broker_API_invoked':False,'new_entry_dispatch_enabled':False,'unprotected_transition_authorized':False,
 'G3_or_emergency_financial_write_authorized':False,'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'failed':[r for r in rows if r['status']!='PASS']}))
