from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,http.cookiejar,io,json,re,urllib.parse,urllib.request
here=Path(__file__).resolve().parent;out=here/'diagnostic-01.json'
if out.exists():raise FileExistsError('Preserve evidence')
jar=http.cookiejar.CookieJar();opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar));rows=[]
def get(params):
 with opener.open('https://api.kibot.com/?'+urllib.parse.urlencode(params),timeout=12) as r:
  b=r.read(65537);return r.status,b
try:
 code,b=get({'action':'login','user':'guest','password':'guest'})
 auth=code==200 and b.lstrip().startswith(b'200');rows.append({'id':'LOGIN','status':'PASS' if auth else 'ERROR','http':code,'cookies_count':len(jar)})
 if auth:
  code,b=get({'action':'history','symbol':'SPY','interval':'daily','startdate':'11/18/2004','enddate':'11/24/2004','unadjusted':'1'})
  parsed=list(csv.reader(io.StringIO(b.decode('ascii',errors='replace'))));shapes={}
  for r in parsed:shapes[str(len(r))]=shapes.get(str(len(r)),0)+1
  api_error=re.match(rb'^\s*([45][0-9]{2})\b',b)
  rows.append({'id':'HISTORY_RESPONSE_SHAPE','http':code,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'row_field_count_histogram':shapes,'api_error_code':api_error.group(1).decode() if api_error else None,'has_nonempty_six_column_rows':any(len(r)==6 for r in parsed),'status':'OBSERVED_NOT_ADMISSION'})
except Exception as e:rows.append({'id':'DIAGNOSTIC','status':'ERROR','type':type(e).__name__})
finally:
 try:get({'action':'logout'})
 except Exception:pass
result={'captured_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,'raw_saved':False,'prices_output':False,'retry_or_bypass':False,'strategy_trials':0,'dataset_admitted':False}
with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result))
