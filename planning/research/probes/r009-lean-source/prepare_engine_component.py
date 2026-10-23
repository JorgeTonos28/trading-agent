from pathlib import Path, PurePosixPath
import hashlib, json, re, subprocess, xml.etree.ElementTree as ET
here=Path(__file__).resolve().parent;root=here.parents[3];repo=root/'.local/lean-source'
out=here/'engine-source-manifest.json'
if out.exists():raise FileExistsError('Manifest already captured')
pin='f3d841e60dfd010ee5fc293ea893e56952484108'
base=['git','-c','credential.helper=','-c','http.sslBackend=schannel','-c','http.version=HTTP/1.1']
pending=['Engine/QuantConnect.Lean.Engine.csproj'];projects={};dropped=[]
while pending:
    name=pending.pop()
    if name in projects:continue
    raw=subprocess.check_output(base+['show',f'{pin}:{name}'],cwd=repo,text=True,timeout=30)
    tree=ET.fromstring(raw);refs=[]
    for node in tree.findall('.//ProjectReference'):
        rel=node.attrib['Include'].replace('\\','/')
        parts=[]
        for bit in (str(PurePosixPath(name).parent)+'/'+rel).split('/'):
            if bit=='..':parts.pop()
            elif bit not in ['','.']:parts.append(bit)
        target='/'.join(parts)
        if target.startswith('Algorithm.CSharp/'):
            dropped.append(dict(project=name,reference=node.attrib['Include']))
        else:refs.append(target);pending.append(target)
    projects[name]=dict(source_sha256=hashlib.sha256(raw.encode()).hexdigest(),references=refs)
dirs=sorted(set(name.split('/')[0] for name in projects))
assert not set(dirs)&{'Data','Tests','Algorithm.CSharp','Launcher'}
subprocess.run(base+['sparse-checkout','set',*dirs],cwd=repo,check=True,timeout=55)
for item in dropped:
    p=repo/item['project'];raw=p.read_text(encoding='utf-8-sig')
    pattern=r'^.*<ProjectReference Include="'+re.escape(item['reference'])+r'"\s*/>\s*\n'
    adjusted,n=re.subn(pattern,'',raw,flags=re.M)
    assert n==1,(item,n)
    p.write_text(adjusted,encoding='utf-8',newline='\n')
assert not (repo/'Data').exists() and not (repo/'Algorithm.CSharp').exists()
manifest=dict(scope='ENGINE_COMPONENT_WITH_SAMPLE_PROJECT_REFERENCES_REMOVED',source_commit=pin,projects=projects,directories=dirs,dropped_project_references=dropped,modified_project_hashes={x['project']:hashlib.sha256((repo/x['project']).read_bytes()).hexdigest() for x in dropped},data_checked_out=False,strategies_executed=0)
with out.open('x',encoding='utf-8') as f:json.dump(manifest,f,indent=2);f.write('\n')
print(json.dumps({'projects':len(projects),'directories':dirs,'excluded_sample_references':len(dropped)}))
