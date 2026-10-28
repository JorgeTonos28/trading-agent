from datetime import datetime, timezone
from decimal import Decimal as D
from pathlib import Path
import hashlib,json
here=Path(__file__).resolve().parent;out=here/'volume-units-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
rows=[]
def case(id,observed,expected):rows.append({'id':id,'observed':observed,'expected':expected,'status':'PASS' if observed==expected else 'FAIL'})
def historical_volume(current_adjusted_volume,complete_factor):
    if complete_factor is None:return 'UNKNOWN_INCOMPLETE_NORMALIZATION_CHAIN'
    return D(current_adjusted_volume)/D(complete_factor)
v=historical_volume('2000','2')
case('INVERT_FULL_REEXPRESSION_CHAIN',str(v),'1000')
case('PARTICIPATION_WRONG_IF_MIX_UNITS',{'correct':str(D('100')/v),'wrong':str(D('100')/D('2000'))},{'correct':'0.1','wrong':'0.05'})
case('NOTIONAL_LIQUIDITY_WRONG_IF_MIX_UNITS',{'correct':str(D('20')*v),'wrong':str(D('20')*D('2000'))},{'correct':'20000','wrong':'40000'})
case('MISSING_FACTOR_NOT_RAW_VOLUME',historical_volume('2000',None),'UNKNOWN_INCOMPLETE_NORMALIZATION_CHAIN')
actions=[{'effective':'2030-02-01','ratio':D('2')}]
def feature_price(raw,cutoff):
    factor=D('1')
    for a in actions:
        if a['effective']<=cutoff:factor*=a['ratio']
    return D(raw)/factor
case('NO_FUTURE_SPLIT_IN_PRE_EVENT_FEATURE',str(feature_price('20','2030-01-07')),'20')
case('PRE_SPLIT_PRICE_REBASED_AFTER_EVENT',str(feature_price('20','2030-02-02')),'10')
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'OWN_SYNTHETIC_UNIT_NORMALIZATION_NOT_PROVIDER_PIT_OR_QUALITY',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,
 'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'vendor_rows_accessed':0,'PIT_vintage_or_factor_completeness_verified':False,'datasets_admitted':0,
 'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'failed':[r for r in rows if r['status']!='PASS']}))
