from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, re, shutil, subprocess, time

here=Path(__file__).resolve().parent
root=here.parents[3]
PIN='f3d841e60dfd010ee5fc293ea893e56952484108'
out=here/'result-01.json'
if out.exists(): raise FileExistsError('Immutable attempt already exists')
source=root/'.local/lean-source'; work=root/'.local/ql3-local-source'
home=root/'.local/ql0-home'
def digest(b): return hashlib.sha256(b).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=source)
assert git('rev-parse','HEAD').decode().strip()==PIN
assert not (source/'Data').exists(), 'No historical Data checkout for this probe'
source_names=['Launcher/Program.cs','Launcher/QuantConnect.Lean.Launcher.csproj','Launcher/config.json',
 'Messaging/QuantConnect.Messaging.csproj','Queues/QuantConnect.Queues.csproj',
 'Engine/QuantConnect.Lean.Engine.csproj','Engine/Initializer.cs','Engine/DataFeeds/DefaultDataProvider.cs']
manifest={}
for name in source_names:
    actual=(source/name).read_bytes(); canonical=git('show',PIN+':'+name)
    manifest[name]={'checkout_sha256':digest(actual),'canonical_blob_content_sha256':digest(canonical),
     'equal_after_EOL_normalization':actual.replace(b'\r\n',b'\n')==canonical.replace(b'\r\n',b'\n')}
assert all(v['equal_after_EOL_normalization'] for n,v in manifest.items() if n!='Engine/QuantConnect.Lean.Engine.csproj')
project_diff=git('diff','--','Engine/QuantConnect.Lean.Engine.csproj').decode('utf-8')
changed_lines=[line for line in project_diff.splitlines() if line[:1] in '+-' and not line.startswith(('+++','---'))]
assert len(changed_lines)==1 and changed_lines[0].startswith('-') and 'Algorithm.CSharp' in changed_lines[0]
nuget=(home/'NuGet.Config').read_text(encoding='utf-8')
assert 'packageSourceCredentials' not in nuget and 'https://api.nuget.org/v3/index.json' in nuget
work.mkdir(exist_ok=True)
for f in ['LocalSourceHost.csproj','MetadataSmoke.csproj','MetadataSmoke.cs']:
    shutil.copyfile(here/f,work/f)
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed}
env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[]; rows=[]
def step(label,args,timeout=55):
    global rows
    start=time.monotonic()
    try:
        p=subprocess.run(['dotnet',*args],cwd=work,env=env,capture_output=True,encoding='utf-8',errors='replace',timeout=timeout)
        raw=p.stdout+'\n'+p.stderr
        (work/(label+'-01.log')).write_text(raw,encoding='utf-8')
        for line in raw.splitlines():
            if line.startswith('QL3_RESULT='): rows=json.loads(line.split('=',1)[1])['rows']
        diagnostics=[line.replace(str(root),'<research-root>')[:600] for line in raw.splitlines() if re.search(r'\berror\b|NU190[34]',line,re.I)]
        info={'label':label,'status':'PASS' if p.returncode==0 else 'ERROR','exit_code':p.returncode,
         'seconds':round(time.monotonic()-start,3),'raw_log_sha256':digest(raw.encode()),'diagnostics':diagnostics[:12]}
    except subprocess.TimeoutExpired:
        info={'label':label,'status':'ERROR','reason':'TIMEOUT','seconds':round(time.monotonic()-start,3)}
    steps.append(info); return info['status']=='PASS'
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false']
if step('restore',['restore','MetadataSmoke.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props]):
    if step('build',['build','MetadataSmoke.csproj','-c','Release','--no-restore',*props]):
        step('metadata_smoke',[str(work/'bin/Release/net10.0/LeanMetadataSmoke.dll')],20)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'LOCAL_SOURCE_MINIMAL_HOST_BUILD_AND_METADATA_NOT_ENGINE_EXECUTION',
 'source_commit_preflight':PIN,'source_manifest_preflight':manifest,
 'prior_source_patch':'QL1_ENGINE_PROJECT_ONE_UNUSED_ALGORITHM_CSHARP_EXAMPLE_REFERENCE_REMOVED',
 'project_kind':'LAB_MINIMAL_PROJECT_COMPILES_UNMODIFIED_PUBLIC_LAUNCHER_PROGRAM_NOT_STOCK_SOLUTION',
 'own_source_hashes':{f:digest((here/f).read_bytes()) for f in ['LocalSourceHost.csproj','MetadataSmoke.csproj','MetadataSmoke.cs','run_probe.py']},
 'steps':steps,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'Launcher_Main_invoked':False,'Engine_Run_invoked':False,'algorithm_or_historical_backtest':False,
 'CLI_Cloud_account_or_billing_used':False,'market_dataset_read':False,'global_config_changed':False,
 'pin_or_target_accepted':False,'implementation_locked':True,'target_acceptance':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'steps':steps,'counts':report['counts'],'rows':rows}))
