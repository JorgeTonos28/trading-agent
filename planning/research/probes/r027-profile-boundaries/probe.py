from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal as D,ROUND_FLOOR
import hashlib,json
here=Path(__file__).resolve().parent;out=here/'result-01.json';assert not out.exists()
scales=[]
for capital in (2000,5000,10000,25000,50000):
 c=D(capital);price=D(100);distance=D(6)
 target=int((c/3/price).to_integral_value(rounding=ROUND_FLOOR));exposure=int((c*D('.25')/price).to_integral_value(rounding=ROUND_FLOOR));risk=int((c*D('.005')/distance).to_integral_value(rounding=ROUND_FLOOR));q=min(target,exposure,risk)
 scales.append({'capital_USD':capital,'target_qty':target,'exposure_cap_qty':exposure,'remaining_risk_cap_qty':risk,'quantity_before_costs':q,'three_equal_positions_notional':str(3*q*price),'gross_fraction':str(3*q*price/c),'baseline_risk_budget_USD':str(c*D('.005')),'shock_10percent_at_gross_cap75percent_fraction_NAV':str(D('.75')*D('.10'))})
avg=(D(4)*100+D(6)*90)/10;previous=D(94);desired=max(previous,avg-6);mark=D(90)
rows=[]
def check(id,ok):rows.append({'id':id,'status':'PASS' if ok else 'FAIL'})
check('ALL_FIVE_CAPITALS_PRESENT',[x['capital_USD'] for x in scales]==[2000,5000,10000,25000,50000])
check('PRINCIPAL_10K_IS_EIGHT_SHARES_BEFORE_FEES',scales[2]['quantity_before_costs']==8)
check('PRINCIPAL_THREE_FILLS_24PERCENT_NOT_75PERCENT',D(scales[2]['gross_fraction'])==D('.24'))
check('SHOCK_LOSS_NOT_CAPPED_BY_DAILY_TRIGGER',D('.75')*D('.10')==D('.075')>D('.02'))
check('PARTIAL_WEIGHTED_AVERAGE_IS_94',avg==94)
check('DESIRED_DOES_NOT_LOOSEN_WHEN_NEW_FILL_LOWER',desired==previous and desired>avg-6)
check('STOP_ALREADY_CROSSED_IMPLIES_UNKNOWN_NOT_ZERO',mark<desired)
check('FILL_TO_SEPARATE_STOP_IS_POSITIVE_CAUSAL_WINDOW',D('1.3')-D('1.0')>0)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'controller_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'SYNTHETIC_ARITHMETIC_NOT_RISK_THRESHOLDS_CALIBRATION_OR_BROKER','baseline_profile_owner_approved':False,'scales':scales,'partial_case':{'filled_qty':10,'p0_running':str(avg),'desired':str(desired),'mark':str(mark),'confirmed_protection':False,'R2_status':'UNCERTAIN'},'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'strategy_trials':0,'datasets_admitted':0,'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'principal_10k':scales[2]}))
