from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,os,re,subprocess,time
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-02.json'
if out.exists():raise FileExistsError('Preserve continuation')
first=json.loads((here/'result-01.json').read_text(encoding='utf-8'))
assert first['steps'][-1].get('reason')=='TIMEOUT'
work=root/'.local/ql5-pin-remediation';source=work/'source';host=work/'host';home=root/'.local/ql0-home'
def sha(b):return hashlib.sha256(b).hexdigest()
for patch in first['source_transformations']:
    assert sha((source/patch['path']).read_bytes())==patch['after_sha256']
for name in ['PatchedHost.csproj','RemediationSmoke.csproj','Program.cs']:
    assert sha((host/name).read_bytes())==first['own_source_hashes'][name]==sha((here/name).read_bytes())
assert (source/'Directory.Build.targets').read_text(encoding='utf-8')==first['added_targets']
assert (host/'Directory.Build.targets').read_text(encoding='utf-8')==first['added_targets']
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed}
env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];rows=[]
def step(label,args,timeout):
    global rows
    start=time.monotonic()
    try:
        p=subprocess.run(['dotnet',*args],cwd=host,env=env,capture_output=True,encoding='utf-8',errors='replace',timeout=timeout)
        raw=p.stdout+'\n'+p.stderr;(host/(label+'-02.log')).write_text(raw,encoding='utf-8')
        for line in raw.splitlines():
            if line.startswith('QL5_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
        diagnostics=[line.replace(str(root),'<research-root>')[:500] for line in raw.splitlines() if re.search(r'\berror\b|NU190[234]|NU1605|NU1504',line,re.I)]
        info={'label':label,'status':'PASS' if p.returncode==0 else 'ERROR','exit_code':p.returncode,'seconds':round(time.monotonic()-start,3),'raw_log_sha256':sha(raw.encode()),'diagnostics':diagnostics[:12]}
    except subprocess.TimeoutExpired as exc:
        raw=exc.stdout.decode('utf-8',errors='replace') if isinstance(exc.stdout,bytes) else (exc.stdout or '')
        (host/(label+'-partial-02.log')).write_text(raw,encoding='utf-8')
        info={'label':label,'status':'ERROR','reason':'TIMEOUT','seconds':round(time.monotonic()-start,3),'partial_log_sha256':sha(raw.encode())}
    steps.append(info);return info['status']=='PASS'
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false','-m:1']
if step('build',['build','RemediationSmoke.csproj','-c','Release','--no-restore',*props],120):
    step('run',[str(host/'bin/Release/net10.0/RemediationSmoke.dll')],20)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'CONTINUATION_SAME_SOURCE_ONLY_BUILD_BUDGET_EXTENDED_NO_NEW_RESTORE',
 'source_sha256':sha(Path(__file__).read_bytes()),'first_capture_sha256':sha((here/'result-01.json').read_bytes()),
 'same_code_and_expectations_verified':True,'build_timeout_seconds':120,'steps':steps,'rows':rows,
 'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'pin_security_or_full_parity_accepted':False,'production_checkout_modified':False,
 'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'steps':steps,'counts':report['counts'],'rows':rows}))
