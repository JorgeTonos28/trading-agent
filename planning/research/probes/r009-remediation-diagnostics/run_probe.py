from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os,re,subprocess,time
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-01.json'
assert not out.exists()
prior=root/'planning/research/probes/r009-pin-remediation'
first=json.loads((prior/'result-01.json').read_text(encoding='utf-8'))
source=root/'.local/ql5-pin-remediation/source';work=root/'.local/ql6-remediation-diagnostics';home=root/'.local/ql0-home'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for item in first['source_transformations']:assert sha(source/item['path'])==item['after_sha256']
assert (source/'Directory.Build.targets').read_text(encoding='utf-8')==first['added_targets']
work.mkdir(exist_ok=False);host=work/'host';smoke=work/'smoke';host.mkdir();smoke.mkdir()
(host/'PatchedHost.csproj').write_bytes((prior/'PatchedHost.csproj').read_bytes())
(host/'Directory.Build.targets').write_text(first['added_targets'],encoding='utf-8')
(smoke/'Directory.Build.targets').write_text(first['added_targets'],encoding='utf-8')
project=(prior/'RemediationSmoke.csproj').read_text(encoding='utf-8').replace('Include="PatchedHost.csproj"','Include="../host/PatchedHost.csproj"')
(smoke/'RemediationSmoke.csproj').write_text(project,encoding='utf-8')
program=(prior/'Program.cs').read_text(encoding='utf-8')
extra='''
var extraRoot=Path.Combine(lab,"unzip-to-folder");
var extraExtract=Path.Combine(extraRoot,"extract");Directory.CreateDirectory(extraExtract);
var extraCanary=Path.Combine(extraRoot,"sibling-canary.txt");
using(var buffer=new MemoryStream())
{
    using(var zip=new ZipArchive(buffer,ZipArchiveMode.Create,true))
    using(var writer=new StreamWriter(zip.CreateEntry("../sibling-canary.txt").Open()))writer.Write("OWN_SYNTHETIC_SECOND_PATH");
    var paths=QuantConnect.Compression.UnzipToFolder(buffer.ToArray(),extraExtract);
    Check("OBSERVE_SECOND_UNREMEDIATED_EXTRACTION_PATH",File.Exists(extraCanary)&&File.ReadAllText(extraCanary)=="OWN_SYNTHETIC_SECOND_PATH");
    Check("SECOND_CANARY_STILL_INSIDE_OWN_LAB",Path.GetFullPath(extraCanary).StartsWith(lab+Path.DirectorySeparatorChar,StringComparison.OrdinalIgnoreCase));
}
'''
program=program.replace('Console.WriteLine("QL5_RESULT="',extra+'\nConsole.WriteLine("QL6_RESULT="')
(smoke/'Program.cs').write_text(program,encoding='utf-8')
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed}
env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];rows=[]
def step(label,args,budget):
    global rows
    logfile=work/(label+'.log');start=time.monotonic()
    with logfile.open('w',encoding='utf-8') as f:
        p=subprocess.Popen(['dotnet',*args],cwd=smoke,env=env,stdout=f,stderr=subprocess.STDOUT)
        try:code=p.wait(timeout=budget);reason=None
        except subprocess.TimeoutExpired:
            p.kill();p.wait();code=None;reason='TIMEOUT'
    raw=logfile.read_text(encoding='utf-8',errors='replace')
    for line in raw.splitlines():
        if line.startswith('QL6_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
    info={'label':label,'status':'PASS' if code==0 else 'ERROR','exit_code':code,'reason':reason,'seconds':round(time.monotonic()-start,3),'log_sha256':sha(logfile),'diagnostics':[line.replace(str(root),'<research-root>')[:600] for line in raw.splitlines() if re.search(r'\berror\b|NU190[234]|NU1605|NETSDK1206',line,re.I)][:16]}
    steps.append(info);print(json.dumps(info),flush=True);return code==0
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false','-m:1']
if step('restore',['restore','RemediationSmoke.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props],45):
    if step('build',['build','RemediationSmoke.csproj','-c','Release','--no-restore',*props],180):
        step('run',[str(smoke/'bin/Release/net10.0/RemediationSmoke.dll')],20)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'ISOLATED_SOURCE_HOST_REPACKAGING_AND_EXTRACTION_SCOPE_DIAGNOSTIC_ONLY','controller_sha256':sha(Path(__file__)),'source_pin':first['source_commit'],'prior_result_sha256':sha(prior/'result-01.json'),'prior_transformation_hashes_verified':True,'source_transformations':first['source_transformations'],'source_modified_by_this_attempt':False,'packaging_changed_from_QL5':True,'timeout_cause_proven':False,'steps':steps,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'second_path_security':'FAIL_BOUNDARY_DEMONSTRATED' if any(r['id']=='OBSERVE_SECOND_UNREMEDIATED_EXTRACTION_PATH' and r['status']=='PASS' for r in rows) else 'NOT_DEMONSTRATED','artifact_sha256':{str(p.relative_to(work)):sha(p) for p in [host/'bin/Release/net10.0/LeanRemediationHostProbe.dll',smoke/'bin/Release/net10.0/RemediationSmoke.dll'] if p.exists()},'pin_accepted':False,'no_engine_or_algorithm_run':True,'no_production_patch':True,'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'second_path_security':report['second_path_security']}))
