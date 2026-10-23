from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, re, subprocess, time
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-04.json'
if out.exists():raise FileExistsError('Preserve previous attempt')
source=root/'.local/lean-source';home=root/'.local/ql0-home';home.mkdir(exist_ok=True)
pin='f3d841e60dfd010ee5fc293ea893e56952484108'
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip()
assert head==pin and not (source/'Data').exists()
config=home/'NuGet.Config'
config.write_text('<?xml version="1.0" encoding="utf-8"?><configuration><packageSources><clear/><add key="public-nuget" value="https://api.nuget.org/v3/index.json"/></packageSources></configuration>',encoding='utf-8')
env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}}
(home/'AppData/Roaming').mkdir(parents=True,exist_ok=True)
(home/'AppData/Local').mkdir(parents=True,exist_ok=True)
env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE='true',MSBUILDDISABLENODEREUSE='1')
steps=[]
def run(label,args):
    t=time.monotonic()
    try:
        p=subprocess.run(['dotnet',*args],cwd=source,env=env,timeout=55,text=True,capture_output=True)
        raw=p.stdout+'\n'+p.stderr
        local_log=home/f'{label}-04.log';local_log.write_text(raw,encoding='utf-8')
        errors=[line.replace(str(root),'<research-root>')[:500] for line in raw.splitlines() if re.search(r'\berror\b|NU1\d\d\d|NU2\d\d\d',line,re.I)]
        step=dict(label=label,exit_code=p.returncode,seconds=round(time.monotonic()-t,3),status='PASS' if p.returncode==0 else 'ERROR',diagnostics=errors[:12],diagnostic_codes=sorted(set(re.findall(r'\b(?:NU|MSB|CS)\d{4,5}\b',raw))),raw_log_sha256=hashlib.sha256(raw.encode()).hexdigest())
    except subprocess.TimeoutExpired:
        step=dict(label=label,status='ERROR',reason='TIMEOUT_55_SECONDS',seconds=round(time.monotonic()-t,3))
    steps.append(step);return step['status']=='PASS'
restored=True
steps.append(dict(label='restore',status='REUSED_PASS_ATTEMPT03',fresh_restore=False))
if restored:run('build',['build','Common/QuantConnect.csproj','--configuration','Release','-m:1','--no-restore','--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false'])
files=['LICENSE','Common/QuantConnect.csproj','Common/Securities/SecurityPortfolioManager.cs','Common/Securities/Equity/EquityFillModel.cs','Compression/QuantConnect.Compression.csproj','Configuration/QuantConnect.Configuration.csproj','Logging/QuantConnect.Logging.csproj']
hashes={f:hashlib.sha256((source/f).read_bytes()).hexdigest() for f in files if (source/f).is_file()}
result=dict(captured_utc=datetime.now(timezone.utc).isoformat(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),source_commit=head,scope='COMMON_SOURCE_BUILD_ONLY_NO_LAUNCHER_OR_STRATEGY',steps=steps,source_file_hashes=hashes,market_data_accessed=False,history_checked_out=False,new_global_install=False,private_feeds=False,engine_selected=False,full_engine_built=False,strategy_trials=0,implementation_locked=True,target_acceptance='TARGET_ACCEPTANCE_DEFERRED')
with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'scope':result['scope'],'steps':steps}))
