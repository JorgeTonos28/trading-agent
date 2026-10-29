from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,subprocess,time,difflib
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-03.json';assert not out.exists()
source=root/'.local/ql5-pin-remediation/source';work=root/'.local/ql7-extraction-repair-normalized';home=root/'.local/ql0-home'
work.mkdir(exist_ok=False);component=work/'component';smoke=work/'smoke';component.mkdir();smoke.mkdir()
before=(source/'Compression/Compression.cs').read_text(encoding='utf-8')
start=before.index('                foreach (var zipEntry in archive.Entries)',before.index('private static List<string> UnzipToFolder('))
end=before.index('\n            }\n            catch',start)
after=before[:start]+'''                archive.ExtractToDirectory(outFolder, overwriteFiles: true);
                files.AddRange(archive.Entries.Where(e => !string.IsNullOrEmpty(e.Name))
                    .Select(e => Path.GetFullPath(Path.Combine(outFolder, e.FullName))));'''+before[end:]
assert before!=after
(component/'Compression.cs').write_text(after,encoding='utf-8')
(component/'ZipStreamWriter.cs').write_bytes((source/'Compression/ZipStreamWriter.cs').read_bytes())
(component/'Repair.csproj').write_bytes((here/'Repair.csproj').read_bytes())
for name in ['Smoke.csproj','Program.cs']:(smoke/name).write_bytes((here/name).read_bytes())
program=(smoke/'Program.cs').read_text(encoding='utf-8')
old='Path.GetFullPath(paths[0])==Path.Combine(safe,"nested/f.txt")'
new='Path.IsPathFullyQualified(paths[0])&&Path.GetFullPath(paths[0])==Path.GetFullPath(Path.Combine(safe,"nested/f.txt"))'
assert old in program
program=program.replace(old,new).replace('Console.WriteLine("QL7_RESULT="','Console.WriteLine("PATH_DIAGNOSTIC="+JsonSerializer.Serialize(new{actual=paths[0],expected_normalized=Path.GetFullPath(Path.Combine(safe,"nested/f.txt")),expected_original=Path.Combine(safe,"nested/f.txt")}));\nConsole.WriteLine("QL7_RESULT="')
(smoke/'Program.cs').write_text(program,encoding='utf-8')
logging=source/'Logging/bin/Release/QuantConnect.Logging.dll';assert logging.exists()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed};env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),DOTNET_CLI_HOME=str(home),USERPROFILE=str(home),HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];rows=[]
def step(label,args,budget):
 global rows
 start=time.monotonic();log=work/(label+'.log')
 with log.open('w',encoding='utf-8') as f:
  p=subprocess.Popen(['dotnet',*args],cwd=smoke,env=env,stdout=f,stderr=subprocess.STDOUT)
  try:code=p.wait(timeout=budget);reason=None
  except subprocess.TimeoutExpired:p.kill();p.wait();code=None;reason='TIMEOUT'
 text=log.read_text(encoding='utf-8',errors='replace')
 for line in text.splitlines():
  if line.startswith('QL7_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
 info={'step':label,'status':'PASS' if code==0 else 'ERROR','exit_code':code,'reason':reason,'seconds':round(time.monotonic()-start,3),'log_sha256':sha(log),'diagnostics':[line.replace(str(root),'<research-root>')[:550] for line in text.splitlines() if re.search(r'\berror\b|NU190[234]|NU1605',line,re.I)][:12]};steps.append(info);return code==0
props=['-p:OriginalLogging='+str(logging),'--disable-build-servers','-m:1','/p:UseSharedCompilation=false']
if step('restore',['restore','Smoke.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props],45):
 if step('build',['build','Smoke.csproj','-c','Release','--no-restore',*props],45):step('run',[str(smoke/'bin/Release/net10.0/Smoke.dll')],20)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'controller_sha256':sha(Path(__file__)),'source_pin':'f3d841e60dfd010ee5fc293ea893e56952484108','scope':'ISOLATED_COMPRESSION_COMPONENT_SECOND_PATH_REPAIR_NOT_FULL_ENGINE','patch_diff':''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/Compression.cs',tofile='b/Compression.cs')),'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':sha(component/'Compression.cs'),'logging_dll_sha256':sha(logging),'steps':steps,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'fixture_expected_and_actual_paths_normalized':True,'prior_02_failure_preserved':True,'full_host_or_pin_accepted':False,'original_exports_modified':False,'no_engine_or_strategy_run':True,'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'steps':steps,'counts':report['counts']}))
