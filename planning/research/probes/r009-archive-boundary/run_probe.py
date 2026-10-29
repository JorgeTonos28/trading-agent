from datetime import datetime, timezone
from pathlib import Path
import hashlib,json,os,re,shutil,subprocess,time
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
source=root/'.local/lean-source';home=root/'.local/ql0-home';work=root/'.local/ql4-archive-boundary'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=source).decode().strip()=='f3d841e60dfd010ee5fc293ea893e56952484108'
work.mkdir(exist_ok=False)
for name in ['ArchiveProbe.csproj','Program.cs']:shutil.copyfile(here/name,work/name)
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed}
env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];observation={};rows=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def step(label,args,timeout=55):
    global observation,rows
    start=time.monotonic()
    try:
        p=subprocess.run(['dotnet',*args],cwd=work,env=env,capture_output=True,encoding='utf-8',errors='replace',timeout=timeout)
        raw=p.stdout+'\n'+p.stderr;(work/(label+'-01.log')).write_text(raw,encoding='utf-8')
        for line in raw.splitlines():
            if line.startswith('QL4_RESULT='):observation=json.loads(line.split('=',1)[1]);rows=observation['rows']
        diagnostics=[line.replace(str(root),'<research-root>')[:500] for line in raw.splitlines() if re.search(r'\berror\b|NU190[234]',line,re.I)]
        info={'label':label,'status':'PASS' if p.returncode==0 else 'ERROR','exit_code':p.returncode,'seconds':round(time.monotonic()-start,3),'raw_log_sha256':sha(raw.encode()),'diagnostics':diagnostics[:8]}
    except subprocess.TimeoutExpired:info={'label':label,'status':'ERROR','reason':'TIMEOUT','seconds':round(time.monotonic()-start,3)}
    steps.append(info);return info['status']=='PASS'
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false']
if step('restore',['restore','ArchiveProbe.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props]):
    if step('build',['build','ArchiveProbe.csproj','-c','Release','--no-restore',*props]):step('run',[str(work/'bin/Release/net10.0/ArchiveProbe.dll')],20)
assets=work/'obj/project.assets.json';libraries=json.loads(assets.read_text(encoding='utf-8')).get('libraries',{}) if assets.exists() else {}
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'OWN_LAB_NATIVE_ARCHIVE_BOUNDARY_AND_REUSABLE_FORK_NOT_SECURITY_ACCEPTANCE',
 'own_source_hashes':{n:sha((here/n).read_bytes()) for n in ['ArchiveProbe.csproj','Program.cs','run_probe.py']},
 'native_source_sha256':sha((source/'Compression/Compression.cs').read_bytes()),
 'steps':steps,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'native_security_verdict':observation.get('native_unzip_overwrite_safety','NOT_TESTED'),
 'fork_package_observed':[n for n in libraries if n.startswith('ProDotNetZip/')],
 'fork_full_lean_compatibility_accepted':False,'production_patch_applied':False,'pin_accepted':False,
 'no_network_or_licensed_market_API_used_by_test':True,'global_or_OS_permissions_changed':False,
 'fixture_retained':True,'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'steps':steps,'counts':report['counts'],'native_security_verdict':report['native_security_verdict'],'rows':rows}))
