"""Read-only public API documentation; no data endpoint/account/credentials."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

URL='https://api.quiverquant.com/docs/schema.json'
result={'captured_at':datetime.now(timezone.utc).isoformat(),
    'scope':'PUBLIC_DOCUMENTATION_METADATA_ONLY','url':URL,'requests':1,
    'authentication_sent':False,'data_endpoint_called':False,'spend':0,
    'provider_selected':False,'dataset_access_proven':False,'PIT_quality_proven':False,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
try:
    request=Request(URL, headers={'User-Agent':'TradingOS-Preparation-public-docs/1.0','Accept':'application/json'})
    with urlopen(request,timeout=20) as response:
        payload=response.read(4*1024*1024+1)
        if len(payload)>4*1024*1024:raise ValueError('metadata size limit')
        result.update(http_status=response.status,content_type=response.headers.get('Content-Type'),
            response_bytes=len(payload),response_sha256=hashlib.sha256(payload).hexdigest())
    schema=json.loads(payload)
    result.update(openapi_version=schema.get('openapi'),api_version=schema.get('info',{}).get('version'),
        license_reference=schema.get('info',{}).get('license'),clock_metadata={})
    for name in ('Form4Entry','CongressionalTrade','InstitutionalHolding'):
        model=schema.get('components',{}).get('schemas',{}).get(name)
        if model is None:
            result['clock_metadata'][name]={'exists':False,'interpretation':'UNKNOWN_SCHEMA_NAME_NOT_DATASET_ABSENCE'}
            continue
        fields={}
        for key,value in model.get('properties',{}).items():
            if any(term in key.lower() for term in ('date','upload','timestamp','filed','reported','seen')):
                fields[key]={'type':value.get('type'),'format':value.get('format'),
                    'required':key in model.get('required',[])}
        result['clock_metadata'][name]={'exists':True,'fields':fields}
    path='/beta/historical/congresstrading/{ticker}'
    result['congress_endpoint_security_declared']=bool(schema.get('paths',{}).get(path,{}).get('get',{}).get('security'))
    result['verdict']='METADATA_OBSERVED_NOT_DATASET_ADMITTED'
except Exception as error:
    result.update(error_class=type(error).__name__,verdict='ERROR_METADATA_ONLY')
    if isinstance(error,HTTPError):result['http_status']=error.code
(Path(__file__).parent/'result-01.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':result['verdict'],'status':result.get('http_status')}))
