from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,shutil,subprocess,time
here=Path(__file__).resolve().parent;root=here.parents[3]
out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
work=root/'.local/ql2-native';work.mkdir(exist_ok=True)
source=root/'.local/lean-source';home=root/'.local/ql0-home'
for name in ['Program.cs','Probe.csproj']:shutil.copyfile(here/name,work/name)
env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}}
env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];rows=[]
def step(label,args,timeout=55):
 global rows
 start=time.monotonic()
 try:
  p=subprocess.run(['dotnet',*args],cwd=work,env=env,capture_output=True,text=True,timeout=timeout)
  raw=p.stdout+'\n'+p.stderr;(work/(label+'-01.log')).write_text(raw,encoding='utf-8')
  diagnostics=[line.replace(str(root),'<research-root>')[:500] for line in raw.splitlines() if re.search(r'\berror\b|NU190[34]',line,re.I)]
  for line in raw.splitlines():
   if line.startswith('QL2_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
  s=dict(label=label,status='PASS' if p.returncode==0 else 'ERROR',exit_code=p.returncode,seconds=round(time.monotonic()-start,3),log_sha256=hashlib.sha256(raw.encode()).hexdigest(),diagnostics=diagnostics[:12])
 except subprocess.TimeoutExpired:s=dict(label=label,status='ERROR',reason='TIMEOUT',seconds=round(time.monotonic()-start,3))
 steps.append(s);return s['status']=='PASS'
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false']
if step('restore',['restore','Probe.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props]):
 if step('build',['build','Probe.csproj','-c','Release','--no-restore',*props]):step('run',[str(work/'bin/Release/net10.0/Probe.dll')],20)
r=dict(captured_utc=datetime.now(timezone.utc).isoformat(),scope='LEAN_NATIVE_COMPONENT_ONLY_FICTITIOUS',source_commit='f3d841e60dfd010ee5fc293ea893e56952484108',source_hashes={name:hashlib.sha256((here/name).read_bytes()).hexdigest() for name in ['Program.cs','Probe.csproj','run_probe.py']},steps=steps,rows=rows,counts={k:sum(x['status']==k for x in rows) for k in ['PASS','FAIL','ERROR']},strategy_trials=0,historical_backtests=0,financial_implementation=False,global_configuration_changed=False,engine_selected=False,QP_integrated_accepted=False,implementation_locked=True,holdout='INTEGRITY_UNKNOWN',target_acceptance='TARGET_ACCEPTANCE_DEFERRED')
with out.open('x',encoding='utf-8') as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'steps':steps,'counts':r['counts'],'rows':rows}))
