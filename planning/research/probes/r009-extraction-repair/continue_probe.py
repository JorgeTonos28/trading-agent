from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,subprocess,time
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-02.json';assert not out.exists()
first=json.loads((here/'result-01.json').read_text(encoding='utf-8'))
assert first['steps'][0]['status']=='ERROR' and not first['rows']
work=root/'.local/ql7-extraction-repair';component=work/'component';smoke=work/'smoke';home=root/'.local/ql0-home'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(component/'Compression.cs')==first['after_sha256']
for name in ['Smoke.csproj','Program.cs']:assert sha(smoke/name)==sha(here/name)
assert sha(component/'Repair.csproj')==sha(here/'Repair.csproj')
logging=root/'.local/ql5-pin-remediation/source/Logging/bin/Release/QuantConnect.Logging.dll';assert sha(logging)==first['logging_dll_sha256']
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed};env.update(DOTNET_CLI_HOME=str(home),USERPROFILE=str(home),HOME=str(home),APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];rows=[]
def step(label,args,budget):
 global rows
 start=time.monotonic();log=work/(label+'-02.log')
 with log.open('w',encoding='utf-8') as f:
  p=subprocess.Popen(['dotnet',*args],cwd=smoke,env=env,stdout=f,stderr=subprocess.STDOUT)
  try:code=p.wait(timeout=budget);reason=None
  except subprocess.TimeoutExpired:p.kill();p.wait();code=None;reason='TIMEOUT'
 raw=log.read_text(encoding='utf-8',errors='replace')
 for line in raw.splitlines():
  if line.startswith('QL7_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
 info={'step':label,'status':'PASS' if code==0 else 'ERROR','exit_code':code,'reason':reason,'seconds':round(time.monotonic()-start,3),'log_sha256':sha(log),'diagnostics':[line.replace(str(root),'<research-root>')[:550] for line in raw.splitlines() if re.search(r'\berror\b|NU190[234]|NU1605',line,re.I)][:12]};steps.append(info);return code==0
props=['-p:OriginalLogging='+str(logging),'--disable-build-servers','-m:1','/p:UseSharedCompilation=false']
if step('restore',['restore','Smoke.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props],45):
 if step('build',['build','Smoke.csproj','-c','Release','--no-restore',*props],45):step('run',[str(smoke/'bin/Release/net10.0/Smoke.dll')],20)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'controller_sha256':sha(Path(__file__)),'first_capture_sha256':sha(here/'result-01.json'),'scope':'SAME_COMPONENT_FIXTURE_ONLY_APPDATA_LOCALAPPDATA_ADDED_TO_SANITIZED_ENV','same_code_verified':True,'steps':steps,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'artifact_sha256':{str(p.relative_to(work)):sha(p) for p in [component/'bin/Release/net10.0/LeanCompressionRepairProbe.dll',smoke/'bin/Release/net10.0/Smoke.dll'] if p.exists()},'full_host_or_pin_accepted':False,'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'steps':steps,'counts':report['counts']}))
