from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,re,subprocess,time,shutil,difflib
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-01.json';assert not out.exists()
prior=root/'planning/research/probes/r009-pin-remediation';first=json.loads((prior/'result-01.json').read_text(encoding='utf-8'))
original=root/'.local/ql5-pin-remediation/source';work=root/'.local/ql8-contract-preserving-host';source=work/'source';host=work/'host';smoke=work/'smoke';home=root/'.local/ql0-home'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for change in first['source_transformations']:assert sha(original/change['path'])==change['after_sha256']
work.mkdir(exist_ok=False);source.mkdir();host.mkdir();smoke.mkdir()
copied={}
for p in original.rglob('*'):
 rel=p.relative_to(original)
 if any(part in ('bin','obj','Data','.git') for part in rel.parts):continue
 assert not p.is_symlink()
 if p.is_file():
  target=source/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target);copied[str(rel)]=sha(target)
before=(source/'Compression/Compression.cs').read_text(encoding='utf-8');start=before.index('                foreach (var zipEntry in archive.Entries)',before.index('private static List<string> UnzipToFolder('));end=before.index('\n            }\n            catch',start)
after=before[:start]+'''                archive.ExtractToDirectory(outFolder, overwriteFiles: true);
                files.AddRange(archive.Entries.Where(e => !string.IsNullOrEmpty(e.Name))
                    .Select(e => Path.Combine(outFolder, e.FullName)));'''+before[end:]
(source/'Compression/Compression.cs').write_text(after,encoding='utf-8')
(host/'PatchedHost.csproj').write_bytes((prior/'PatchedHost.csproj').read_bytes())
for place in [host,smoke]:(place/'Directory.Build.targets').write_text(first['added_targets'],encoding='utf-8')
project=(prior/'RemediationSmoke.csproj').read_text(encoding='utf-8').replace('Include="PatchedHost.csproj"','Include="../host/PatchedHost.csproj"')
(smoke/'RemediationSmoke.csproj').write_text(project,encoding='utf-8')
program=(root/'planning/research/probes/r009-extraction-repair/Program.cs').read_text(encoding='utf-8')
program=program.replace('Path.GetFullPath(paths[0])==Path.Combine(safe,"nested/f.txt")','Path.IsPathFullyQualified(paths[0])&&Path.GetFullPath(paths[0])==Path.GetFullPath(Path.Combine(safe,"nested/f.txt"))')
extra='''
var relative=Path.Combine("lab","relative-output");Directory.CreateDirectory(relative);
var relativePaths=QuantConnect.Compression.UnzipToFolder(Zip("nested/f.txt","RELATIVE"),relative);
Check("LEGACY_RELATIVE_OUTPUT_SHAPE",relativePaths.Count==1&&!Path.IsPathFullyQualified(relativePaths[0])&&relativePaths[0]==Path.Combine(relative,"nested/f.txt"));
Check("RELATIVE_OUTPUT_CONTENT",File.ReadAllText(relativePaths[0])=="RELATIVE");
var loaded=System.Reflection.Assembly.Load("LeanRemediationHostProbe");
Check("MAIN_COMPILED_NOT_INVOKED",loaded.EntryPoint?.DeclaringType?.FullName=="QuantConnect.Lean.Launcher.Program");
Check("ENGINE_TYPE_LOAD",System.Reflection.Assembly.Load("QuantConnect.Lean.Engine").GetType("QuantConnect.Lean.Engine.Engine",true)!=null);
using(var encoded=new MemoryStream())
{
 using(var zip=new Ionic.Zip.ZipFile()){zip.AddEntry("f.txt","OWN_TEXT");zip.Save(encoded);}
 encoded.Position=0;using var reader=Ionic.Zip.ZipFile.Read(encoded);using var decoded=new MemoryStream();reader["f.txt"].Extract(decoded);
 Check("FORK_API_WITH_REBUILT_GRAPH",System.Text.Encoding.UTF8.GetString(decoded.ToArray())=="OWN_TEXT");
}
'''
program=program.replace('Console.WriteLine("QL7_RESULT="',extra+'\nConsole.WriteLine("QL8_RESULT="');(smoke/'Program.cs').write_text(program,encoding='utf-8')
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed};env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];rows=[]
def step(label,args,budget):
 global rows
 start=time.monotonic();log=work/(label+'.log')
 with log.open('w',encoding='utf-8') as f:
  p=subprocess.Popen(['dotnet',*args],cwd=smoke,env=env,stdout=f,stderr=subprocess.STDOUT)
  try:code=p.wait(timeout=budget);reason=None
  except subprocess.TimeoutExpired:p.kill();p.wait();code=None;reason='TIMEOUT'
 raw=log.read_text(encoding='utf-8',errors='replace')
 for line in raw.splitlines():
  if line.startswith('QL8_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
 info={'step':label,'status':'PASS' if code==0 else 'ERROR','exit_code':code,'reason':reason,'seconds':round(time.monotonic()-start,3),'log_sha256':sha(log),'diagnostics':[line.replace(str(root),'<research-root>')[:550] for line in raw.splitlines() if re.search(r'\berror\b|NU190[234]|NU1605|NETSDK1206',line,re.I)][:12]};steps.append(info);print(json.dumps(info),flush=True);return code==0
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false','-m:1']
if step('restore',['restore','RemediationSmoke.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props],45):
 if step('build',['build','RemediationSmoke.csproj','-c','Release','--no-restore',*props],240):step('run',[str(smoke/'bin/Release/net10.0/RemediationSmoke.dll')],20)
assets=json.loads((smoke/'obj/project.assets.json').read_text(encoding='utf-8')) if (smoke/'obj/project.assets.json').exists() else {}
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'controller_sha256':sha(Path(__file__)),'scope':'ISOLATED_FULL_MINIMAL_HOST_REBUILD_WITH_TWO_REPAIRS_LEGACY_RETURN_SHAPE_NOT_ENGINE_EXECUTION','source_pin':first['source_commit'],'base_transformation_capture_sha256':sha(prior/'result-01.json'),'base_export_file_hashes':copied,'second_patch_diff':''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/Compression.cs',tofile='b/Compression.cs')),'source_repair_sha256':sha(source/'Compression/Compression.cs'),'own_fixture_sha256':sha(smoke/'Program.cs'),'steps':steps,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'resolved_libraries':sorted(assets.get('libraries',{})),'observed_audit_warnings':assets.get('logs',[]),'artifact_sha256':{str(p.relative_to(work)):sha(p) for p in [smoke/'bin/Release/net10.0/RemediationSmoke.dll',host/'bin/Release/net10.0/LeanRemediationHostProbe.dll',source/'Compression/bin/Release/QuantConnect.Compression.dll'] if p.exists()},'pin_security_and_parity_accepted':False,'original_exports_modified':False,'no_Engine_Run_Main_or_Algorithm_invoked':True,'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'pin_accepted':False}))
