from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,subprocess,time,shutil
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-02.json';assert not out.exists()
first=json.loads((here/'result-01.json').read_text(encoding='utf-8'));assert first['steps'][-1]['status']=='ERROR' and not first['rows']
work=root/'.local/ql8-contract-preserving-host';source=work/'source';smoke=work/'smoke';original=root/'.local/ql5-pin-remediation/source';home=root/'.local/ql0-home'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name,digest in first['base_export_file_hashes'].items():
 expected=first['source_repair_sha256'] if Path(name).as_posix()=='Compression/Compression.cs' else digest
 assert sha(source/name)==expected
assert sha(smoke/'Program.cs')==first['own_fixture_sha256']
added={}
for p in original.rglob('*.cs'):
 rel=p.relative_to(original)
 if any(x in ('bin','obj','.git') for x in rel.parts) or rel.parts[0]=='Data' or 'Data' not in rel.parts:continue
 assert not p.is_symlink() and rel.suffix=='.cs'
 target=source/rel
 if target.exists():continue
 target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target);added[str(rel)]=sha(target)
assert added and all(Path(name).parts[0]!='Data' for name in added)
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed};env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
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
  if line.startswith('QL8_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
 info={'step':label,'status':'PASS' if code==0 else 'ERROR','exit_code':code,'reason':reason,'seconds':round(time.monotonic()-start,3),'log_sha256':sha(log),'diagnostics':[line.replace(str(root),'<research-root>')[:550] for line in raw.splitlines() if re.search(r': error |NU190[234]|NU1605|NETSDK1206',line,re.I)][:12]};steps.append(info);print(json.dumps(info),flush=True);return code==0
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false','-m:1']
if step('build',['build','RemediationSmoke.csproj','-c','Release','--no-restore',*props],240):step('run',[str(smoke/'bin/Release/net10.0/RemediationSmoke.dll')],20)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'controller_sha256':sha(Path(__file__)),'first_capture_sha256':sha(here/'result-01.json'),'scope':'SAME_HOST_SECOND_REPAIR_RESTORE_OMITTED_CSHARP_NAMESPACE_FILES_ONLY_NOT_DATASETS','added_source_file_hashes':added,'prior_source_patch_and_fixture_hashes_verified':True,'source_repair_sha256':sha(source/'Compression/Compression.cs'),'steps':steps,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'artifact_sha256':{str(p.relative_to(work)):sha(p) for p in [smoke/'bin/Release/net10.0/RemediationSmoke.dll',work/'host/bin/Release/net10.0/LeanRemediationHostProbe.dll',source/'Compression/bin/Release/QuantConnect.Compression.dll'] if p.exists()},'no_Engine_Run_Main_or_Algorithm_invoked':True,'pin_security_and_parity_accepted':False,'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'restored_CSharp_sources':len(added)}))
