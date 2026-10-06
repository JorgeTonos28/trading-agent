"""Disposable Win32 AccessCheck/token semantics, not an operational sandbox.

Only transient handles and synthetic in-memory security descriptors. No users,
filesystem/process ACL assignment, profiles, child jobs, firewall, auth or network.
"""
import ctypes as c
from ctypes import wintypes as w
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import os

OUT = Path(__file__).with_name('common-sid-attempt-01.json')
if OUT.exists():
    raise SystemExit('Original evidence exists; select a new attempt filename.')
if os.name != 'nt':
    raise SystemExit('Windows-only probe; no result simulated.')

adv = c.WinDLL('advapi32', use_last_error=True)
kernel = c.WinDLL('kernel32', use_last_error=True)
class SID_AND_ATTRIBUTES(c.Structure):
    _fields_ = [('Sid', c.c_void_p), ('Attributes', w.DWORD)]
class GENERIC_MAPPING(c.Structure):
    _fields_ = [('GenericRead', w.DWORD), ('GenericWrite', w.DWORD), ('GenericExecute', w.DWORD), ('GenericAll', w.DWORD)]

kernel.GetCurrentProcess.restype = w.HANDLE
kernel.CloseHandle.argtypes = [w.HANDLE]
kernel.CloseHandle.restype = w.BOOL
kernel.LocalFree.argtypes = [c.c_void_p]
kernel.LocalFree.restype = c.c_void_p
adv.OpenProcessToken.argtypes = [w.HANDLE,w.DWORD,c.POINTER(w.HANDLE)]
adv.OpenProcessToken.restype = w.BOOL
adv.DuplicateToken.argtypes = [w.HANDLE,c.c_int,c.POINTER(w.HANDLE)]
adv.DuplicateToken.restype = w.BOOL
adv.GetTokenInformation.argtypes = [w.HANDLE,c.c_int,c.c_void_p,w.DWORD,c.POINTER(w.DWORD)]
adv.GetTokenInformation.restype = w.BOOL
adv.ConvertSidToStringSidW.argtypes = [c.c_void_p,c.POINTER(c.c_void_p)]
adv.ConvertSidToStringSidW.restype = w.BOOL
adv.ConvertStringSidToSidW.argtypes = [w.LPCWSTR,c.POINTER(c.c_void_p)]
adv.ConvertStringSidToSidW.restype = w.BOOL
adv.CreateRestrictedToken.argtypes = [w.HANDLE,w.DWORD,w.DWORD,c.POINTER(SID_AND_ATTRIBUTES),w.DWORD,c.c_void_p,w.DWORD,c.POINTER(SID_AND_ATTRIBUTES),c.POINTER(w.HANDLE)]
adv.CreateRestrictedToken.restype = w.BOOL
adv.IsTokenRestricted.argtypes = [w.HANDLE]
adv.IsTokenRestricted.restype = w.BOOL
adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes = [w.LPCWSTR,w.DWORD,c.POINTER(c.c_void_p),c.POINTER(w.DWORD)]
adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.restype = w.BOOL
adv.AccessCheck.argtypes = [c.c_void_p,w.HANDLE,w.DWORD,c.POINTER(GENERIC_MAPPING),c.c_void_p,c.POINTER(w.DWORD),c.POINTER(w.DWORD),c.POINTER(w.BOOL)]
adv.AccessCheck.restype = w.BOOL

class LUID(c.Structure):
    _fields_=[('LowPart',w.DWORD),('HighPart',w.LONG)]
class LUID_AND_ATTRIBUTES(c.Structure):
    _fields_=[('Luid',LUID),('Attributes',w.DWORD)]
adv.LookupPrivilegeValueW.argtypes=[w.LPCWSTR,w.LPCWSTR,c.POINTER(LUID)]
adv.LookupPrivilegeValueW.restype=w.BOOL

handles, allocations, tests = [], [], []
def require(ok, operation):
    if not ok:
        # Do not emit token SIDs/descriptor strings/user metadata.
        raise OSError(c.get_last_error(), operation)

def token_user(handle):
    length=w.DWORD()
    adv.GetTokenInformation(handle,1,None,0,c.byref(length))
    require(length.value>0,'GetTokenInformation size')
    buf=c.create_string_buffer(length.value)
    require(adv.GetTokenInformation(handle,1,buf,length,c.byref(length)),'GetTokenInformation TokenUser')
    sid=c.cast(buf,c.POINTER(SID_AND_ATTRIBUTES)).contents.Sid
    text=c.c_void_p()
    require(adv.ConvertSidToStringSidW(sid,c.byref(text)),'ConvertSidToStringSid')
    try:
        return c.wstring_at(text)
    finally:
        kernel.LocalFree(text)

def access(token, grantees):
    # Descriptor describes a private synthetic object; it is never assigned to a file/process.
    sddl='O:SYG:SYD:P'+''.join('(A;;0x1;;;'+sid+')' for sid in grantees)
    sd=c.c_void_p(); size=w.DWORD()
    require(adv.ConvertStringSecurityDescriptorToSecurityDescriptorW(sddl,1,c.byref(sd),c.byref(size)),'Convert synthetic SD')
    try:
        mapping=GENERIC_MAPPING(1,2,4,7)
        privileges=c.create_string_buffer(4096);plen=w.DWORD(len(privileges));granted=w.DWORD();allowed=w.BOOL()
        require(adv.AccessCheck(sd,token,1,c.byref(mapping),privileges,c.byref(plen),c.byref(granted),c.byref(allowed)),'AccessCheck API')
        return {'allowed':bool(allowed.value),'granted_mask':granted.value}
    finally:
        kernel.LocalFree(sd)

def check(name, observed, expected):
    tests.append({'id':name,'observed':observed,'expected':expected,'passed':observed==expected})

result={'schema_version':'r013-s2b-common-sid-v1','captured_at':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_commit_base':'b0d6818d057a024bd6fbc2573a8d9bd06c254353','environment':'Team research, current developer Windows identity','configuration_changes':[],'model_calls':0,'probe_scope':'Win32 token/descriptor AccessCheck only, no process launch or real object ACL enforcement','limitations':['Not native Codex compatibility','Not filesystem/process/network/IPC enforcement','Not a new Agent Runner or account','Not audit generation or bootstrap','No operational security/blinding PASS']}
try:
    base=w.HANDLE(); require(adv.OpenProcessToken(kernel.GetCurrentProcess(),0x0008|0x0002,c.byref(base)),'Open own token'); handles.append(base)
    plain=w.HANDLE();require(adv.DuplicateToken(base,2,c.byref(plain)),'Duplicate own impersonation token');handles.append(plain)
    user=token_user(plain)
    r_strings=['S-1-5-21-42424242-43434343-44444444-11001','S-1-5-21-42424242-43434343-44444444-11002']
    restricted=[]
    for r_string in r_strings:
        sid=c.c_void_p();require(adv.ConvertStringSidToSidW(r_string,c.byref(sid)),'Synthetic restrict SID');allocations.append(sid)
        restriction=SID_AND_ATTRIBUTES(sid,0)
        token=w.HANDLE()
        # DISABLE_MAX_PRIVILEGE (0x1), deliberately not WRITE_RESTRICTED (0x8).
        # DuplicateToken returns a query/impersonate handle; use the own primary
        # handle with TOKEN_DUPLICATE to create the restricted token, then duplicate
        # for AccessCheck. No privilege added or process token changed.
        require(adv.CreateRestrictedToken(base,0x1,0,None,0,None,1,c.byref(restriction),c.byref(token)),'Create transient restricted primary token')
        handles.append(token)
        imp=w.HANDLE();require(adv.DuplicateToken(token,2,c.byref(imp)),'Duplicate restricted impersonation token')
        handles.append(imp);restricted.append(imp)
    check('AC-01-same-base-user',all(token_user(t)==user for t in restricted),True)
    check('AC-02-restrictions-present',all(bool(adv.IsTokenRestricted(t)) for t in restricted),True)
    objects={'shadow_export':[user,r_strings[0]],'pedagogy_trace':[user,r_strings[1]],'financial_canary':['S-1-5-21-42424242-43434343-44444444-11003']}
    for name in ('shadow_export','pedagogy_trace'):
        check('AC-plain-'+name,access(plain,objects[name])['allowed'],True)
    for i,role in enumerate(('shadow','pedagogy')):
        for name in ('shadow_export','pedagogy_trace','financial_canary'):
            expected=(i==0 and name=='shadow_export') or (i==1 and name=='pedagogy_trace')
            check('AC-'+role+'-'+name,access(restricted[i],objects[name])['allowed'],expected)
    # Common restricting SID may permit runtime reads; it also broadens any data
    # descriptor that grants that SID. These are synthetic descriptors, not paths.
    common_sid_string='S-1-5-32-545' # BUILTIN Users, public identifier; no group changed.
    common_sid=c.c_void_p()
    require(adv.ConvertStringSidToSidW(common_sid_string,c.byref(common_sid)),'Common restricting SID')
    allocations.append(common_sid)
    common_tokens=[]
    for role_sid in allocations[:2]:
        restricts=(SID_AND_ATTRIBUTES*2)(SID_AND_ATTRIBUTES(role_sid,0),SID_AND_ATTRIBUTES(common_sid,0))
        tok=w.HANDLE()
        require(adv.CreateRestrictedToken(base,0x1,0,None,0,None,2,restricts,c.byref(tok)),'Create common-SID transient token')
        handles.append(tok)
        imp=w.HANDLE();require(adv.DuplicateToken(tok,2,c.byref(imp)),'Duplicate common-SID token')
        handles.append(imp);common_tokens.append(imp)
    focused=[]
    def focused_check(name,obs,exp,meaning):
        focused.append({'id':name,'observed_allowed':obs,'expected_observation':exp,'observation_matched':obs==exp,'meaning':meaning})
    descriptors={
        'private_shadow':[user,r_strings[0]],
        'private_pedagogy':[user,r_strings[1]],
        'shared_runtime_read':[user,common_sid_string],
        'peer_trace_with_broad_common_grant':[user,common_sid_string],
    }
    actors=[('tight_shadow',restricted[0]),('common_shadow',common_tokens[0]),('common_pedagogy',common_tokens[1])]
    for actor,tok in actors:
        for target,grants in descriptors.items():
            expected=(target=='private_shadow' and actor in ('tight_shadow','common_shadow')) or (target=='private_pedagogy' and actor=='common_pedagogy') or (target in ('shared_runtime_read','peer_trace_with_broad_common_grant') and actor.startswith('common_'))
            meaning='EXCLUDED_PEER_DATA_EXPOSED_BY_BROAD_GRANT_COUNTEREXAMPLE' if target=='peer_trace_with_broad_common_grant' and actor=='common_shadow' else 'DESCRIPTOR_PERMISSION_OBSERVATION_ONLY'
            focused_check(actor+'-'+target,access(tok,grants)['allowed'],expected,meaning)
    def privileges(token):
        length=w.DWORD();adv.GetTokenInformation(token,3,None,0,c.byref(length))
        require(length.value>=4,'TokenPrivileges size')
        buf=c.create_string_buffer(length.value)
        require(adv.GetTokenInformation(token,3,buf,length,c.byref(length)),'Read own transient token privileges')
        count=c.cast(buf,c.POINTER(w.DWORD)).contents.value
        values=c.cast(c.addressof(buf)+4,c.POINTER(LUID_AND_ATTRIBUTES))
        return [(v.Luid.LowPart,v.Luid.HighPart,v.Attributes) for v in [values[i] for i in range(count)]]
    change=LUID();require(adv.LookupPrivilegeValueW(None,'SeChangeNotifyPrivilege',c.byref(change)),'Lookup public privilege identifier')
    standard=privileges(common_tokens[0])
    defaults_has_change=any(lo==change.LowPart and hi==change.HighPart and attr&2 for lo,hi,attr in standard)
    original_privileges=privileges(base)
    deletes=(LUID_AND_ATTRIBUTES*len(original_privileges))(*[LUID_AND_ATTRIBUTES(LUID(lo,hi),0) for lo,hi,attr in original_privileges])
    no_priv=w.HANDLE()
    one=SID_AND_ATTRIBUTES(allocations[0],0)
    # Flags=0: DeletePrivilege list applies. DISABLE_MAX_PRIVILEGE ignores it.
    require(adv.CreateRestrictedToken(base,0,0,None,len(deletes),deletes,len([one]),c.byref(one),c.byref(no_priv)),'Create transient all-privileges-deleted token')
    handles.append(no_priv)
    no_priv_list=privileges(no_priv)
    result['focused_observations']=focused
    result['focused_observation_count']=len(focused)
    result['privilege_observations']={'DISABLE_MAX_PRIVILEGE_keeps_enabled_SeChangeNotify':defaults_has_change,'explicit_delete_all_remaining_privileges':len(no_priv_list),'current_process_token_changed':False}
    result['new_privilege_expected_checks']={'retained_traverse':defaults_has_change,'deleted_all':len(no_priv_list)==0}
    result['base_checks_are_regression_not_new_evidence']=True
    result['scope_note']='Common-SID in-memory descriptors and transient privilege removal only; no actual runtime/path traversal/child/filesystem test'
    if not all(x['observation_matched'] for x in focused) or not defaults_has_change or no_priv_list:
        raise RuntimeError('Focused semantic observation differed from preregistered expectation')
    result['tests']=tests
    result['expected_checks']=len(tests)
    result['passed_checks']=sum(t['passed'] for t in tests)
    result['status']='PASS_SEMANTIC_SCOPE_ONLY' if all(t['passed'] for t in tests) else 'FAILED_SEMANTIC_CHECK'
except Exception as exc:
    result['status']='PROBE_ERROR_NOT_SECURITY_FAILURE'
    result['error']={'type':type(exc).__name__,'winerror':getattr(exc,'errno',None),'operation':str(exc)}
    result['tests']=tests
finally:
    for token in reversed(handles):
        kernel.CloseHandle(token)
    for pointer in allocations:
        kernel.LocalFree(pointer)
    result['cleanup']='Transient handles closed and in-memory SID/descriptors freed; no persistent setup'
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'checks':len(tests),'passed':sum(t['passed'] for t in tests),'configuration_changes':[],'S2_B_acceptance':'NOT_TESTED'},indent=2))
if result['status']!='PASS_SEMANTIC_SCOPE_ONLY':
    raise SystemExit(1)
