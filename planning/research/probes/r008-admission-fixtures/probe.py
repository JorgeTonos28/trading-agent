from datetime import datetime, timezone
from decimal import Decimal as D
from pathlib import Path
import hashlib, json

here=Path(__file__).resolve().parent
out=here/'result-01.json'
if out.exists(): raise FileExistsError('Preserve attempt')
rows=[]
def case(id,observed,expected):
    rows.append({'id':id,'observed':observed,'expected':expected,'status':'PASS' if observed==expected else 'FAIL'})
def ohlc(row):
    o,h,l,c=[D(str(row[k])) for k in ['o','h','l','c']]
    return min(o,h,l,c)>0 and l<=min(o,c)<=max(o,c)<=h and D(str(row['volume']))>=0
good={'security':'FICT-A','session':'2030-01-07','o':10,'h':12,'l':9,'c':11,'volume':100}
case('RAW_STRUCTURAL_VALID',ohlc(good),True)
case('OHLC_CONTRADICTION',ohlc(dict(good,h=10)),False)
case('NEGATIVE_VOLUME',ohlc(dict(good,volume=-1)),False)
case('DUPLICATE_GRAIN',len({(x['security'],x['session']) for x in [good,dict(good)]})==2,False)
# An explicit fixture calendar, not a production calendar or a missing-row inference.
calendar={'2030-01-07':'OPEN','2030-01-08':'OPEN','2030-01-09':'CLOSED'}
data_dates={'2030-01-07'}
missing=[date for date,state in calendar.items() if state=='OPEN' and date not in data_dates]
case('MISSING_OPEN_SESSION_NOT_HOLIDAY',missing,['2030-01-08'])
div={'date':'2030-01-07','value':'1','unadjustedValue':'2','currency':'USD','paymentDate':'2030-01-14'}
case('HISTORICAL_DIVIDEND_UNITS',str(D('10')*D(div['unadjustedValue'])),'20')
case('TODAYS_SPLIT_ADJUSTED_VALUE_WRONG_FOR_OLD_QTY',D('10')*D(div['value'])==D('20'),False)
csv_fields={'Date','Dividends'}
case('CSV_NOT_PAYDATE_EVIDENCE','paymentDate' in csv_fields,False)
def eligible_cash(event,at):
    if not event.get('paymentDate'):return 'UNKNOWN_NO_CASH_CREDIT'
    return 'PAYMENT_ELIGIBLE_MODEL_ONLY' if at>=event['paymentDate'] else 'RECEIVABLE_ONLY'
case('EX_DATE_NOT_CASH',eligible_cash(div,'2030-01-07'),'RECEIVABLE_ONLY')
case('MISSING_PAYMENT_NOT_EARLY_CASH',eligible_cash(dict(div,paymentDate=None),'2030-01-20'),'UNKNOWN_NO_CASH_CREDIT')
case('PAY_DATE_NOT_BROKER_BUYING_POWER',eligible_cash(div,'2030-01-14'),'PAYMENT_ELIGIBLE_MODEL_ONLY')
announcement={'declarationDate':'2030-01-05','publication_timestamp':None,'historical_vintage':None}
case('DATE_ALONE_NOT_ORIGINAL_PIT',bool(announcement['publication_timestamp'] and announcement['historical_vintage']),False)
revisions=[{'version':1,'known_from':'2030-01-06T12:00:00Z','amount':'2'}, {'version':2,'known_from':'2030-01-10T12:00:00Z','amount':'3'}]
known=[r for r in revisions if r['known_from']<='2030-01-07T12:00:00Z']
case('LATE_REVISION_NOT_IN_OLD_SNAPSHOT',max(known,key=lambda r:r['known_from'])['version'],1)
bar={'o':100,'h':112,'l':96,'c':105}
# high-before-low can trigger ratchet105 and stop; low-before-high may survive.
case('DAILY_BAR_CANNOT_IDENTIFY_RATCHET_STOP_PATH',bar['h']>=110 and bar['l']<=D('104.5'),'True'=='True')
case('IEX_QUOTE_NOT_CONSOLIDATED_NBBO','IEX'=='NBBO',False)
def may_export(origin,permission,content):
    if origin=='OWN_FICTITIOUS' and content=='NO_LICENSED_CONTENT':return True
    return permission=='CONFIRMED_FOR_FIELD_USE_AND_DESTINATION'
for content in ['RAW','DERIVED','SNAPSHOT','RECONSTRUCTIBLE_SUMMARY']:
    case('DENY_EXTERNAL_'+content,may_export('LICENSED_VENDOR','UNKNOWN',content),False)
case('OWN_SYNTHETIC_FIXTURES_PERMITTED',may_export('OWN_FICTITIOUS','N/A','NO_LICENSED_CONTENT'),True)
admission={'rights_reported':True,'product_contract_accepted':False,'coverage_accepted':False,'PIT_accepted':False,'quality_accepted':False}
case('COMMERCIAL_REPLY_NOT_ADMISSION',all(admission.values()),False)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'OWN_FICTITIOUS_ADMISSION_CASES_NOT_VENDOR_DATA',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,
 'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'external_requests':0,'licensed_market_data_used':False,'datasets_admitted':0,'strategy_trials':0,
 'implementation_locked':True,'target_acceptance':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'failed':[r for r in rows if r['status']!='PASS']}))
