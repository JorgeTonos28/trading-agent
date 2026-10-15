"""Disposable FS-A harness for S2B-ADM-01 AFTER explicit setup approval.

Never creates accounts or provisions ACL/policies. Must be copied to the new
lab code directory by its operator. Tests thread tokens, NOT process isolation.
Only fixed synthetic fixture paths; new own scratch files with test descriptors.
NOT executed during preparation. No model, network, shell, broker or real secrets.
"""
import argparse,ctypes as c,hashlib,json,os
from ctypes import wintypes as w
from pathlib import Path
from datetime import datetime,timezone

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--actor',choices=['BASE','OPERATOR'],required=True)
ap.add_argument('--run',required=True,help='Unique report/scratch basename; alphanumeric and hyphen only')
a=ap.parse_args()
if os.name!='nt':raise SystemExit('Windows-only, no simulated result')
if not a.run or len(a.run)>40 or any(ch not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-' for ch in a.run):raise SystemExit('Invalid run ID')
ROOT=Path('C:/ProgramData/TradingOS-S2B-Probe/trial-01')
if Path(__file__).resolve().parent!=ROOT/'code':raise SystemExit('Run only reviewed copy in the authorized new lab, never from development checkout')
binding_path=ROOT/'code'/'local-binding.json'
b=json.loads(binding_path.read_text(encoding='utf-8'))
if b['gate']!='S2B-ADM-01' or not b['owner_approval_reference']:raise SystemExit('Missing reviewed administrative gate record; self-claimed JSON is not approval')
if b['root']!=str(ROOT) or b['source_sha256']!=hashlib.sha256(Path(__file__).read_bytes()).hexdigest():raise SystemExit('Source/root mismatch')
if b['bindings']['BASE']==b['bindings']['OPERATOR']:raise SystemExit('Domains must differ')
out=ROOT/('trusted-evidence' if a.actor=='OPERATOR' else 'raw-results')/(a.run+'.json')
if out.exists():raise SystemExit('Preserve old evidence; new run ID required')
adv=c.WinDLL('advapi32',use_last_error=True);k=c.WinDLL('kernel32',use_last_error=True)
class SID_ATTR(c.Structure):_fields_=[('Sid',c.c_void_p),('Attributes',w.DWORD)]
class LUID(c.Structure):_fields_=[('LowPart',w.DWORD),('HighPart',w.LONG)]
class PRIV(c.Structure):_fields_=[('Luid',LUID),('Attributes',w.DWORD)]
class SA(c.Structure):_fields_=[('nLength',w.DWORD),('lpSecurityDescriptor',c.c_void_p),('bInheritHandle',w.BOOL)]
class GM(c.Structure):_fields_=[('GenericRead',w.DWORD),('GenericWrite',w.DWORD),('GenericExecute',w.DWORD),('GenericAll',w.DWORD)]
class FILEINFO(c.Structure):_fields_=[('Attributes',w.DWORD),('Creation',w.FILETIME),('Access',w.FILETIME),('Write',w.FILETIME),('Volume',w.DWORD),('SizeHigh',w.DWORD),('SizeLow',w.DWORD),('Links',w.DWORD),('IndexHigh',w.DWORD),('IndexLow',w.DWORD)]
class US(c.Structure):_fields_=[('Length',w.USHORT),('MaximumLength',w.USHORT),('Buffer',w.LPWSTR)]
class OA(c.Structure):_fields_=[('Length',w.ULONG),('RootDirectory',w.HANDLE),('ObjectName',c.POINTER(US)),('Attributes',w.ULONG),('SecurityDescriptor',c.c_void_p),('SecurityQualityOfService',c.c_void_p)]
class IOS(c.Structure):_fields_=[('StatusOrPointer',c.c_void_p),('Information',c.c_size_t)]
nt=c.WinDLL('ntdll',use_last_error=True)
nt.NtCreateFile.argtypes=[c.POINTER(w.HANDLE),w.DWORD,c.POINTER(OA),c.POINTER(IOS),c.c_void_p,w.ULONG,w.ULONG,w.ULONG,w.ULONG,c.c_void_p,w.ULONG];nt.NtCreateFile.restype=w.LONG
nt.RtlNtStatusToDosError.argtypes=[w.LONG];nt.RtlNtStatusToDosError.restype=w.ULONG
k.GetCurrentProcess.restype=w.HANDLE
k.CloseHandle.argtypes=[w.HANDLE];k.CloseHandle.restype=w.BOOL
k.LocalFree.argtypes=[c.c_void_p];k.LocalFree.restype=c.c_void_p
adv.OpenProcessToken.argtypes=[w.HANDLE,w.DWORD,c.POINTER(w.HANDLE)];adv.OpenProcessToken.restype=w.BOOL
adv.GetTokenInformation.argtypes=[w.HANDLE,c.c_int,c.c_void_p,w.DWORD,c.POINTER(w.DWORD)];adv.GetTokenInformation.restype=w.BOOL
adv.ConvertSidToStringSidW.argtypes=[c.c_void_p,c.POINTER(c.c_void_p)];adv.ConvertSidToStringSidW.restype=w.BOOL
adv.ConvertStringSidToSidW.argtypes=[w.LPCWSTR,c.POINTER(c.c_void_p)];adv.ConvertStringSidToSidW.restype=w.BOOL
adv.CreateRestrictedToken.argtypes=[w.HANDLE,w.DWORD,w.DWORD,c.POINTER(SID_ATTR),w.DWORD,c.POINTER(PRIV),w.DWORD,c.POINTER(SID_ATTR),c.POINTER(w.HANDLE)];adv.CreateRestrictedToken.restype=w.BOOL
adv.DuplicateToken.argtypes=[w.HANDLE,c.c_int,c.POINTER(w.HANDLE)];adv.DuplicateToken.restype=w.BOOL
adv.ImpersonateLoggedOnUser.argtypes=[w.HANDLE];adv.ImpersonateLoggedOnUser.restype=w.BOOL
adv.RevertToSelf.argtypes=[];adv.RevertToSelf.restype=w.BOOL
adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes=[w.LPCWSTR,w.DWORD,c.POINTER(c.c_void_p),c.POINTER(w.DWORD)];adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.restype=w.BOOL
k.CreateFileW.argtypes=[w.LPCWSTR,w.DWORD,w.DWORD,c.POINTER(SA),w.DWORD,w.DWORD,w.HANDLE];k.CreateFileW.restype=w.HANDLE
k.ReadFile.argtypes=[w.HANDLE,c.c_void_p,w.DWORD,c.POINTER(w.DWORD),c.c_void_p];k.ReadFile.restype=w.BOOL
k.WriteFile.argtypes=[w.HANDLE,c.c_void_p,w.DWORD,c.POINTER(w.DWORD),c.c_void_p];k.WriteFile.restype=w.BOOL
k.GetFinalPathNameByHandleW.argtypes=[w.HANDLE,w.LPWSTR,w.DWORD,w.DWORD];k.GetFinalPathNameByHandleW.restype=w.DWORD
k.GetFileInformationByHandle.argtypes=[w.HANDLE,c.POINTER(FILEINFO)];k.GetFileInformationByHandle.restype=w.BOOL
adv.AccessCheck.argtypes=[c.c_void_p,w.HANDLE,w.DWORD,c.POINTER(GM),c.c_void_p,c.POINTER(w.DWORD),c.POINTER(w.DWORD),c.POINTER(w.BOOL)];adv.AccessCheck.restype=w.BOOL
handles=[];allocations=[];observations=[];sealed_parents={};root_handle=None
def require(ok,op):
    if not ok:raise OSError(c.get_last_error(),op)
def info(token,kind):
    n=w.DWORD();adv.GetTokenInformation(token,kind,None,0,c.byref(n));require(n.value>0,'Token info size')
    buf=c.create_string_buffer(n.value);require(adv.GetTokenInformation(token,kind,buf,n,c.byref(n)),'Token info');return buf
def user(token):
    buf=info(token,1);sid=c.cast(buf,c.POINTER(SID_ATTR)).contents.Sid;ptr=c.c_void_p()
    require(adv.ConvertSidToStringSidW(sid,c.byref(ptr)),'Token user conversion')
    try:return c.wstring_at(ptr)
    finally:k.LocalFree(ptr)
def canonical_handle(h,expected):
    buf=c.create_unicode_buffer(4096);n=k.GetFinalPathNameByHandleW(h,buf,len(buf),0)
    require(0<n<len(buf),'Final path')
    final=buf.value
    if final.startswith('\\\\?\\'):final=final[4:]
    if os.path.normcase(final)!=os.path.normcase(str(expected)):raise RuntimeError('Reparse/alias scope drift; stop')
def pin_create_ancestors(path):
    # Trusted, quiescent laboratory only. Check and retain all ancestor handles
    # before CREATE_NEW, with no write/delete sharing. Not an adversarial sandbox:
    # a path-based create still has a residual TOCTOU assumption (no other writers).
    if not path.is_relative_to(ROOT) or path.parent not in (ROOT/'shadow'/'scratch',ROOT/'pedagogy'/'scratch',ROOT/'raw-results',ROOT/'trusted-evidence'):
        raise RuntimeError('Creation parent outside fixed allowlist')
    pinned=[]
    try:
        for parent in reversed(path.parent.parents):
            h=k.CreateFileW(str(parent),0x80,1,None,3,0x02200000,None)
            if h==w.HANDLE(-1).value:raise OSError(c.get_last_error(),'Cannot seal creation ancestor')
            pinned.append(h);canonical_handle(h,parent)
            meta=FILEINFO();require(k.GetFileInformationByHandle(h,c.byref(meta)),'Ancestor metadata')
            if meta.Attributes&0x400 or not meta.Attributes&0x10:raise RuntimeError('Creation ancestor reparse or not directory; no create')
        h=k.CreateFileW(str(path.parent),0x80,1,None,3,0x02200000,None)
        if h==w.HANDLE(-1).value:raise OSError(c.get_last_error(),'Cannot seal immediate creation parent')
        pinned.append(h);canonical_handle(h,path.parent)
        meta=FILEINFO();require(k.GetFileInformationByHandle(h,c.byref(meta)),'Creation parent metadata')
        if meta.Attributes&0x400 or not meta.Attributes&0x10:raise RuntimeError('Creation parent reparse or not directory; no create')
        return pinned
    except BaseException:
        for h in reversed(pinned):k.CloseHandle(h)
        raise
def operation(context,rel,mask=1,write_new=False,sd=None):
    # rel supplied only by fixed catalog below, never by output/model.
    path=ROOT/rel;assert path.is_relative_to(ROOT)
    if not rel or '..' in Path(rel).parts or ':' in rel or '\\' in rel:raise RuntimeError('Invalid fixed relative name')
    # Trusted BASE/OPERATOR pinned these paths before entering a restricted thread.
    # No checking under a role token that cannot inspect OS ancestor metadata.
    if write_new and path.parent not in sealed_parents:raise RuntimeError('Missing pre-create trusted ancestor seal; no create')
    pinned=[]
    # User-mode documented NtCreateFile RootDirectory route. Only fixed relative
    # names under this lab; root handle retained by trusted harness, not an agent.
    # No global ACL changes, absolute path fallback, backup intent or file-id opens.
    directory=rel in ('code','shadow/export','pedagogy/export','financial-canary','trusted-evidence','raw-results')
    name=c.create_unicode_buffer(rel.replace('/','\\'));u=US(len(name.value)*2,c.sizeof(name),c.cast(name,w.LPWSTR))
    attr=OA(c.sizeof(OA),root_handle,c.pointer(u),0x40,sd,None);ios=IOS();h=w.HANDLE()
    desired=mask|0x100000 # SYNCHRONIZE, required by FILE_SYNCHRONOUS_IO_NONALERT
    status=nt.NtCreateFile(c.byref(h),desired,c.byref(attr),c.byref(ios),None,0x80,7,2 if write_new else 1,0x20|(1 if directory else 0x200040),None,0)
    if status<0:
        err=nt.RtlNtStatusToDosError(status)
        for parent_handle in reversed(pinned):k.CloseHandle(parent_handle)
        observations.append({'context':context,'resource':rel,'mask':mask,'desired_access':desired,'ntstatus':hex(status&0xffffffff),'result':'ACCESS_DENIED' if err==5 else 'OS_ERROR','winerror':err,'observed_at':datetime.now(timezone.utc).isoformat()});return
    try:
        canonical_handle(h,path)
        record={'context':context,'resource':rel,'mask':mask,'desired_access':desired,'ntstatus':hex(status&0xffffffff),'result':'ACCESS_GRANTED','winerror':0,'observed_at':datetime.now(timezone.utc).isoformat()}
        if mask==1:
            buf=c.create_string_buffer(128);n=w.DWORD();require(k.ReadFile(h,buf,len(buf),c.byref(n),None),'Read synthetic fixture')
            record['sample_length']=n.value;record['sample_sha256']=hashlib.sha256(buf.raw[:n.value]).hexdigest()
        if write_new:
            payload=b'S2B synthetic own-scratch marker';n=w.DWORD();require(k.WriteFile(h,payload,len(payload),c.byref(n),None),'Write own synthetic scratch')
            record['bytes_written']=n.value
        observations.append(record)
    finally:
        k.CloseHandle(h)
        for parent_handle in reversed(pinned):k.CloseHandle(parent_handle)
def object_only_read(sd,token,context,resource):
    mapping=GM(0x120089,0x120116,0x1200a0,0x1f01ff);priv=c.create_string_buffer(4096);size=w.DWORD(len(priv));granted=w.DWORD();allowed=w.BOOL()
    require(adv.AccessCheck(sd,token,0x100001,c.byref(mapping),priv,c.byref(size),c.byref(granted),c.byref(allowed)),'Child descriptor-only AccessCheck')
    observations.append({'context':context,'resource':resource,'mask':1,'result':'OBJECT_ONLY_GRANTED' if allowed else 'OBJECT_ONLY_DENIED','scope':'DESCRIPTOR_ONLY_NO_PARENT_TRAVERSAL','observed_at':datetime.now(timezone.utc).isoformat()})
    if not allowed:raise RuntimeError('Peer child-object positive failed: traversal test invalid')
def restricted(label,base):
    buf=info(base,3);count=c.cast(buf,c.POINTER(w.DWORD)).contents.value
    existing=c.cast(c.addressof(buf)+4,c.POINTER(PRIV));deletes=(PRIV*count)(*[PRIV(existing[i].Luid,0) for i in range(count)])
    sid=c.c_void_p();require(adv.ConvertStringSidToSidW(b['bindings'][label],c.byref(sid)),'Job fixture SID');allocations.append(sid)
    restrict=SID_ATTR(sid,0);tok=w.HANDLE()
    require(adv.CreateRestrictedToken(base,0,0,None,count,deletes,1,c.byref(restrict),c.byref(tok)),'Transient restricted token deleting all privileges');handles.append(tok)
    imp=w.HANDLE();require(adv.DuplicateToken(tok,2,c.byref(imp)),'Duplicate restricted thread token');handles.append(imp)
    if user(imp)!=b['bindings']['BASE']:raise RuntimeError('Unexpected TokenUser')
    privbuf=info(imp,3)
    if c.cast(privbuf,c.POINTER(w.DWORD)).contents.value:raise RuntimeError('Privileges remain; do not silently change policy')
    return imp
result={'schema_version':'r013-s2b-filesystem-evidence-v1','gate':'S2B-ADM-01','actor':a.actor,'run':a.run,'captured_at':datetime.now(timezone.utc).isoformat(),'scope':'FS_THREAD_CONTEXTS_ONLY_NOT_PROCESS_OR_CODEX_ACCEPTANCE','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'binding_sha256':hashlib.sha256(binding_path.read_bytes()).hexdigest(),'actual_approval_is_external':True,'configuration_provisioned_by_this_script':[],'model_calls':0,'aggregate_acceptance':'NOT_EVALUATED_REQUIRES_EXTERNAL_POSITIVES','LF10_revocation_LF12_rollback':'EXTERNAL_OPERATOR_PROCEDURES_NOT_PROVEN_BY_THIS_RUN'}
try:
    base=w.HANDLE();require(adv.OpenProcessToken(k.GetCurrentProcess(),0xA,c.byref(base)),'Own token');handles.append(base)
    if user(base)!=b['bindings'][a.actor]:raise SystemExit('Wrong OS principal: abort without resource/output mutation, no substitute developer run')
    root_handle=k.CreateFileW(str(ROOT),0xa0,1,None,3,0x02200000,None)
    if root_handle==w.HANDLE(-1).value:raise OSError(c.get_last_error(),'Trusted laboratory root handle')
    handles.append(root_handle);canonical_handle(root_handle,ROOT)
    meta=FILEINFO();require(k.GetFileInformationByHandle(root_handle,c.byref(meta)),'Root metadata')
    if meta.Attributes&0x400 or not meta.Attributes&0x10:raise RuntimeError('Root must be plain directory')
    if a.actor=='OPERATOR':
        sealed_parents[ROOT/'trusted-evidence']=pin_create_ancestors(out)
        operation('OPERATOR','financial-canary/core-marker.txt')
        operation('OPERATOR','shadow/export/snapshot.json')
        operation('OPERATOR','pedagogy/export/champion-marker.json')
        operation('OPERATOR','trusted-evidence',2)
    else:
        for parent in (ROOT/'raw-results',ROOT/'shadow'/'scratch',ROOT/'pedagogy'/'scratch'):
            sealed_parents[parent]=pin_create_ancestors(parent/'seal-placeholder.txt')
        for rel in ('financial-canary/core-marker.txt','shadow/export/snapshot.json','pedagogy/export/champion-marker.json','code/local-binding.json'):
            operation('BASE',rel)
        for rel in ('financial-canary/core-marker.txt','financial-canary','trusted-evidence'):
            for mask in (2,0x40,0x10000,0x40000,0x80000):operation('BASE',rel,mask)
        tokens={label:restricted(label,base) for label in ('JOB_SHADOW','JOB_PEDAGOGY')}
        for label,own,peer in [('JOB_SHADOW','shadow','pedagogy'),('JOB_PEDAGOGY','pedagogy','shadow')]:
            token=tokens[label];require(adv.ImpersonateLoggedOnUser(token),'Enter own restricted thread context')
            try:
                own_file='snapshot.json' if own=='shadow' else 'champion-marker.json'
                peer_file='snapshot.json' if peer=='shadow' else 'champion-marker.json'
                operation(label,f'{own}/export/{own_file}')
                operation(label,f'{peer}/export/{peer_file}')
                operation(label,'financial-canary/core-marker.txt')
                operation(label,f'{own}/scratch/{a.run}-own.txt',2,True)
                for rel in ('code','code/local-binding.json',f'{own}/export',f'{own}/export/{own_file}','financial-canary','financial-canary/core-marker.txt','trusted-evidence','raw-results'):
                    for mask in (2,0x40,0x10000,0x40000,0x80000):operation(label,rel,mask)
                # Broad child-object grant test stays inside own scratch. No parent/global ACL assignment.
                peer_label='JOB_PEDAGOGY' if label=='JOB_SHADOW' else 'JOB_SHADOW'
                sddl=f"O:{b['bindings']['BASE']}G:BUD:P(A;;0x1301bf;;;{b['bindings']['BASE']})(A;;0x1301bf;;;{b['bindings'][label]})(A;;0x120089;;;{b['bindings'][peer_label]})(A;;0x120089;;;BU)(A;;0x1f01ff;;;SY)(A;;0x1f01ff;;;BA)(A;;0x1f01ff;;;{b['bindings']['OPERATOR']})(A;;0x0;;;OW)"
                sd=c.c_void_p();n=w.DWORD();require(adv.ConvertStringSecurityDescriptorToSecurityDescriptorW(sddl,1,c.byref(sd),c.byref(n)),'Scratch test descriptor')
                try:
                    object_only_read(sd,tokens[peer_label],peer_label,f'{own}/scratch/{a.run}-broad.txt')
                    operation(label,f'{own}/scratch/{a.run}-broad.txt',2,True,sd)
                finally:k.LocalFree(sd)
                operation(label,f'{own}/scratch/{a.run}-broad.txt')
                if own=='pedagogy':operation(label,f'{peer}/scratch/{a.run}-broad.txt')
                # SHADOW peer read deferred until PED's file/positive exists.
            finally:
                if not adv.RevertToSelf():raise SystemExit('FATAL RevertToSelf failure: operator must terminate this process; no continuation')
        # Repeat SHADOW after PED created its scratch so the opposite target exists.
        token=tokens['JOB_SHADOW'];require(adv.ImpersonateLoggedOnUser(token),'Final shadow context')
        try:operation('JOB_SHADOW','pedagogy/scratch/'+a.run+'-broad.txt')
        finally:
            if not adv.RevertToSelf():raise SystemExit('FATAL RevertToSelf failure; terminate process')
    result['status']='OBSERVATIONS_CAPTURED_NOT_AGGREGATE_PASS'
except Exception as exc:
    result['status']='PROBE_ERROR_NOT_SECURITY_ACCEPTANCE';result['error']={'type':type(exc).__name__,'operation':str(exc)}
finally:
    for h in reversed(handles):k.CloseHandle(h)
    for ptr in allocations:k.LocalFree(ptr)
result['observations']=observations
if out.parent not in sealed_parents:sealed_parents[out.parent]=pin_create_ancestors(out)
try:
    with out.open('x',encoding='utf-8') as report:report.write(json.dumps(result,indent=2)+'\n')
finally:
    for pinned in sealed_parents.values():
        for h in reversed(pinned):k.CloseHandle(h)
print(json.dumps({'status':result['status'],'actor':a.actor,'observations':len(observations),'aggregate_acceptance':result['aggregate_acceptance']}))
if result['status']!='OBSERVATIONS_CAPTURED_NOT_AGGREGATE_PASS':raise SystemExit(1)
