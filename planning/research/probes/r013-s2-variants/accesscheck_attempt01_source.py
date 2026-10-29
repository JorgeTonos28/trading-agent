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

OUT = Path(__file__).with_name('accesscheck-attempt-01.json')
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

result={'schema_version':'r013-variants-accesscheck-v1','captured_at':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_commit_base':'46cc4a5889747ddfec9731200283f1a94d2b77bd','environment':'Team research, current developer Windows identity','configuration_changes':[],'model_calls':0,'probe_scope':'Win32 token/descriptor AccessCheck only, no process launch or real object ACL enforcement','limitations':['Not native Codex compatibility','Not filesystem/process/network/IPC enforcement','Not a new Agent Runner or account','Not audit generation or bootstrap','No operational security/blinding PASS']}
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
        require(adv.CreateRestrictedToken(plain,0x1,0,None,0,None,1,c.byref(restriction),c.byref(token)),'Create transient restricted token')
        handles.append(token);restricted.append(token)
    check('AC-01-same-base-user',all(token_user(t)==user for t in restricted),True)
    check('AC-02-restrictions-present',all(bool(adv.IsTokenRestricted(t)) for t in restricted),True)
    objects={'shadow_export':[user,r_strings[0]],'pedagogy_trace':[user,r_strings[1]],'financial_canary':['S-1-5-21-42424242-43434343-44444444-11003']}
    for name in ('shadow_export','pedagogy_trace'):
        check('AC-plain-'+name,access(plain,objects[name])['allowed'],True)
    for i,role in enumerate(('shadow','pedagogy')):
        for name in ('shadow_export','pedagogy_trace','financial_canary'):
            expected=(i==0 and name=='shadow_export') or (i==1 and name=='pedagogy_trace')
            check('AC-'+role+'-'+name,access(restricted[i],objects[name])['allowed'],expected)
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
