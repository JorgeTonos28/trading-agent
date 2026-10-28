from datetime import datetime,timezone
from pathlib import Path
import difflib,hashlib,io,json,os,re,shutil,subprocess,tarfile,time
here=Path(__file__).resolve().parent;root=here.parents[3];out=here/'result-01.json'
if out.exists():raise FileExistsError('Preserve attempt')
origin=root/'.local/lean-source';home=root/'.local/ql0-home';work=root/'.local/ql5-pin-remediation';source=work/'source';host=work/'host'
PIN='f3d841e60dfd010ee5fc293ea893e56952484108'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=origin).decode().strip()==PIN
work.mkdir(exist_ok=False);source.mkdir();host.mkdir()
allowed_dirs=['Algorithm','AlgorithmFactory','Api','Brokerages','Common','Compression','Configuration','Engine','Indicators','Logging','Launcher','Messaging','Queues']
archive=subprocess.check_output(['git','archive',PIN,*allowed_dirs,'LICENSE'],cwd=origin)
exported=[]
with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
    for member in tar.getmembers():
        relative=Path(member.name)
        assert not relative.is_absolute() and '..' not in relative.parts and not member.issym() and not member.islnk()
        target=(source/relative).resolve();assert target.is_relative_to(source.resolve())
        if member.isdir():target.mkdir(parents=True,exist_ok=True)
        elif member.isfile():
            target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(tar.extractfile(member).read());exported.append(member.name)
        else:raise ValueError('Unexpected archive member')
def sha(b):return hashlib.sha256(b).hexdigest()
patches=[]
def patch(relative,transform):
    path=source/relative;before=path.read_text(encoding='utf-8');after=transform(before)
    assert before!=after
    path.write_text(after,encoding='utf-8',newline='\n')
    patches.append({'path':relative,'before_sha256':sha(before.encode()),'after_sha256':sha(after.encode()),'diff':''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/'+relative,tofile='b/'+relative))})
patch('Compression/QuantConnect.Compression.csproj',lambda s:s.replace('Include="DotNetZip" Version="1.16.0"','Include="ProDotNetZip" Version="1.19.0"'))
def replace_unzip(s):
    start=s.index('                if (!overwrite)',s.index('public static bool Unzip('))
    end=s.index('\n\n                return true;',start)
    return s[:start]+'                System.IO.Compression.ZipFile.ExtractToDirectory(zip, directory, overwrite);'+s[end:]
patch('Compression/Compression.cs',replace_unzip)
patch('Engine/QuantConnect.Lean.Engine.csproj',lambda s:re.sub(r'^.*<ProjectReference Include="\.\.\\Algorithm.CSharp\\QuantConnect.Algorithm.CSharp.csproj" />\r?\n','',s,flags=re.M))
targets='''<Project><ItemGroup>
<PackageReference Include="System.Drawing.Common" Version="4.7.2" />
<PackageReference Include="System.Net.Http.WinHttpHandler" Version="4.5.4" />
<PackageReference Include="System.ServiceModel.Primitives" Version="4.4.4" />
<PackageReference Include="System.Private.ServiceModel" Version="4.4.4" />
</ItemGroup></Project>'''
(source/'Directory.Build.targets').write_text(targets,encoding='utf-8')
(host/'Directory.Build.targets').write_text(targets,encoding='utf-8')
for f in ['PatchedHost.csproj','RemediationSmoke.csproj','Program.cs']:shutil.copyfile(here/f,host/f)
allowed={'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP','PROGRAMFILES','PROGRAMFILES(X86)','PROGRAMW6432','PROGRAMDATA','ALLUSERSPROFILE','SYSTEMDRIVE'}
env={k:v for k,v in os.environ.items() if k.upper() in allowed}
env.update(APPDATA=str(home/'AppData/Roaming'),LOCALAPPDATA=str(home/'AppData/Local'),USERPROFILE=str(home),HOME=str(home),DOTNET_CLI_HOME=str(home),NUGET_PACKAGES=str(home/'packages'),DOTNET_CLI_TELEMETRY_OPTOUT='1',DOTNET_SKIP_FIRST_TIME_EXPERIENCE='1',MSBUILDDISABLENODEREUSE='1')
steps=[];rows=[]
def step(label,args,timeout=55):
    global rows
    start=time.monotonic()
    try:
        p=subprocess.run(['dotnet',*args],cwd=host,env=env,capture_output=True,encoding='utf-8',errors='replace',timeout=timeout)
        raw=p.stdout+'\n'+p.stderr;(host/(label+'-01.log')).write_text(raw,encoding='utf-8')
        for line in raw.splitlines():
            if line.startswith('QL5_RESULT='):rows=json.loads(line.split('=',1)[1])['rows']
        diagnostics=[line.replace(str(root),'<research-root>')[:500] for line in raw.splitlines() if re.search(r'\berror\b|NU190[234]|NU1605|NU1504',line,re.I)]
        info={'label':label,'status':'PASS' if p.returncode==0 else 'ERROR','exit_code':p.returncode,'seconds':round(time.monotonic()-start,3),'raw_log_sha256':sha(raw.encode()),'diagnostics':diagnostics[:12]}
    except subprocess.TimeoutExpired as exc:
        raw=(exc.stdout or b'').decode('utf-8',errors='replace') if isinstance(exc.stdout,bytes) else (exc.stdout or '')
        (host/(label+'-partial-01.log')).write_text(raw,encoding='utf-8')
        info={'label':label,'status':'ERROR','reason':'TIMEOUT','seconds':round(time.monotonic()-start,3),'partial_log_sha256':sha(raw.encode())}
    steps.append(info);return info['status']=='PASS'
props=['-p:LeanSourceRoot='+str(source),'--disable-build-servers','/p:UseSharedCompilation=false','/p:RunAnalyzers=false','-m:1']
if step('restore',['restore','RemediationSmoke.csproj','--configfile',str(home/'NuGet.Config'),'--packages',str(home/'packages'),*props]):
    if step('build',['build','RemediationSmoke.csproj','-c','Release','--no-restore',*props]):step('run',[str(host/'bin/Release/net10.0/RemediationSmoke.dll')],20)
assets=host/'obj/project.assets.json';asset=json.loads(assets.read_text(encoding='utf-8')) if assets.exists() else {}
audit=[{'code':a.get('code'),'library':a.get('libraryId'),'message':a.get('message')} for a in asset.get('logs',[]) if a.get('code','').startswith('NU190')]
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'ISOLATED_SOURCE_REMEDIATION_FEASIBILITY_NOT_PRODUCTION_PATCH_OR_PIN_ACCEPTANCE',
 'source_commit':PIN,'git_archive_sha256':sha(archive),'exported_code_files':len(exported),'Data_exported':False,
 'own_source_hashes':{n:sha((here/n).read_bytes()) for n in ['PatchedHost.csproj','RemediationSmoke.csproj','Program.cs','run_probe.py']},
 'source_transformations':patches,'added_targets':targets,'steps':steps,'rows':rows,
 'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},
 'resolved_candidate_packages':[n for n in asset.get('libraries',{}) if any(x in n for x in ['DotNetZip/','Drawing.Common/','WinHttpHandler/','ServiceModel/','ServiceModel.Primitives/'])],
 'observed_NuGet_audit_warnings_in_host_assets':audit,'audit_warning_absence_is_security_proof':False,
 'full_lean_algorithm_or_broker_parity_accepted':False,'production_checkout_modified':False,'pin_accepted':False,
 'implementation_locked':True,'holdout':'INTEGRITY_UNKNOWN','target_acceptance':'TARGET_ACCEPTANCE_DEFERRED'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'steps':steps,'counts':report['counts'],'resolved_candidate_packages':report['resolved_candidate_packages'],'observed_audit_warnings':audit,'rows':rows}))
