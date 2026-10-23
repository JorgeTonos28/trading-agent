from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal,InvalidOperation
import csv,hashlib,http.cookiejar,io,json,urllib.request,urllib.parse
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve attempts')
local=root/'.local/kibot-guest-coverage';local.mkdir(exist_ok=True)
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
rows=[];network_calls=0;start=datetime(2004,11,18).date();end=datetime(2004,11,24).date()
def request(params):
 global network_calls
 network_calls+=1
 req=urllib.request.Request('https://api.kibot.com/?'+urllib.parse.urlencode(params),headers={'User-Agent':'TradingOS-Preparation-ReadOnlyProbe/1.0'})
 with opener.open(req,timeout=12) as response:
  data=response.read(65537)
  return response.status,data,response.geturl().startswith('https://api.kibot.com/')
auth=False;logout='NOT_NEEDED'
try:
 status,data,origin=request({'action':'login','user':'guest','password':'guest'}) # vendor-published anonymous credentials, not an owner account
 auth=status==200 and data.lstrip().startswith(b'200') and origin
 rows.append({'id':'PUBLIC_GUEST_ACCESS','status':'PASS' if auth else 'ERROR','http_status':status,'body_code':data[:3].decode('ascii',errors='replace') if len(data)>=3 else None})
 if auth:
  for symbol in ['SPY','QQQ','IWM','EFA','TLT','GLD']:
   try:
    status,data,origin=request({'action':'history','symbol':symbol,'interval':'daily','startdate':'11/18/2004','enddate':'11/24/2004','unadjusted':'1'})
    if not origin or len(data)>65536:raise ValueError('ORIGIN_OR_BODY_LIMIT')
    text=data.decode('ascii');entries=list(csv.reader(io.StringIO(text)));dates=[];valid=True
    for entry in entries:
     if len(entry)!=6:raise ValueError('NON_CSV_OR_API_BODY_ERROR')
     d=datetime.strptime(entry[0],'%m/%d/%Y').date()
     if not start<=d<=end:raise ValueError('DATE_OUTSIDE_APPROVED_SLICE')
     dates.append(d);o,h,l,c,v=map(Decimal,entry[1:]);valid=valid and all(x.is_finite() for x in [o,h,l,c,v]) and min(o,h,l,c)>0 and v>=0 and l<=min(o,c)<=max(o,c)<=h
    valid=valid and len(dates)>0 and len(dates)==len(set(dates)) and dates==sorted(dates)
    if valid:(local/(symbol+'-20041118-24-raw.csv')).write_bytes(data)
    rows.append({'symbol':symbol,'status':'PASS' if valid else 'FAIL','scope':'TINY_RAW_ACCESS_AND_SHAPE_ONLY','http_status':status,'rows_checked':len(dates),'body_sha256':hashlib.sha256(data).hexdigest(),'raw_persisted_local_only':bool(valid),'full_history_coverage_accepted':False,'PIT_accepted':False})
   except Exception as e:rows.append({'symbol':symbol,'status':'ERROR','error_type':type(e).__name__,'reason':str(e) if isinstance(e,ValueError) else 'NETWORK_OR_PARSE_FAILURE_NO_URL_LOGGED'})
except Exception as e:rows.append({'id':'PUBLIC_GUEST_NETWORK','status':'ERROR','error_type':type(e).__name__,'reason':'NETWORK_OR_PARSE_FAILURE_NO_URL_LOGGED'})
finally:
 if auth:
  try:status,_,_=request({'action':'logout'});logout='REQUESTED_HTTP_'+str(status)
  except Exception:logout='REQUEST_ERROR_COOKIE_JAR_DISCARDED'
result={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'PUBLIC_ANONYMOUS_VENDOR_TINY_2004_ACCESS_PROBE_NO_BACKTEST','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'request_window':[str(start),str(end)],'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'network_calls':network_calls,'logout':logout,'private_credentials_used':False,'owner_account_created':False,'spend':0,'raw_prices_printed_or_committed':False,'market_data_slice_requested':True,'holdout_requested':False,'strategy_trials':0,'datasets_admitted':0,'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'counts':result['counts'],'rows':rows,'network_calls':network_calls,'datasets_admitted':0}))
