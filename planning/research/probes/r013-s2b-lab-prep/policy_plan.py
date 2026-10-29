"""PLAN_ONLY: render proposed SDDL; validate descriptors in memory, never apply.

No account calls, paths opened outside this source folder, auth, child process,
security assignment, firewall or provisioning. Sample SIDs are never real binding.
"""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path,PurePosixPath,PureWindowsPath
from ctypes import wintypes

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',required=True,help='New JSON basename in this probe folder only')
args=parser.parse_args()
assert Path(args.output).name==args.output and args.output.endswith('.json') and ':' not in args.output and '\\' not in args.output
folder=Path(__file__).resolve().parent
out=folder/args.output
if out.exists():raise SystemExit('Preserve evidence: output already exists')
source=folder/'lab-policy-plan.json'
p=json.loads(source.read_text(encoding='utf-8'))
assert p['status']=='PLAN_ONLY_NOT_AUTHORIZED' and p['implementation_locked'] and p['authority']=='NONE'
assert p['account']['name']=='tos_probe_runner_b' and p['account']['new_only'] and not p['account']['initially_enabled']
assert p['root']=='C:\\ProgramData\\TradingOS-S2B-Probe\\trial-01'
assert len(set(p['sample_bindings'].values()))==4
assert p['sample_bindings']['OPERATOR']!=p['sample_bindings']['BASE']
assert p['test_contexts']['job_os_accounts_created']==0 and not p['test_contexts']['shared_restricting_sid_selected']
if os.name=='nt':
    adv=ctypes.WinDLL('advapi32',use_last_error=True)
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.argtypes=[wintypes.LPCWSTR,wintypes.DWORD,ctypes.POINTER(ctypes.c_void_p),ctypes.POINTER(wintypes.DWORD)]
    adv.ConvertStringSecurityDescriptorToSecurityDescriptorW.restype=wintypes.BOOL
    kernel.LocalFree.argtypes=[ctypes.c_void_p]
    kernel.LocalFree.restype=ctypes.c_void_p
def validate_in_memory(sddl):
    if os.name!='nt':return 'NOT_TESTED_NON_WINDOWS'
    sd=ctypes.c_void_p();length=wintypes.DWORD()
    if not adv.ConvertStringSecurityDescriptorToSecurityDescriptorW(sddl,1,ctypes.byref(sd),ctypes.byref(length)):
        raise OSError(ctypes.get_last_error(),'Synthetic SDDL conversion')
    kernel.LocalFree(sd)
    return 'VALID_SYNTACTIC_DESCRIPTOR_ONLY'
rendered=[]
for r in p['resources']:
    rel=r['relative_path'];parts=PurePosixPath(rel).parts
    assert not PurePosixPath(rel).is_absolute() and '..' not in parts and ':' not in rel and '\\' not in rel
    assert r['owner']=='BA' and r['group']=='BA' and r['dacl_protected'] and r['state']=='NOT_CREATED'
    grants=p['common_protected_control']+r['extra_allow']
    aces=[]
    for g in grants:
        sid=p['sample_bindings'].get(g['principal'],g['principal'])
        assert g['principal'] in set(p['sample_bindings'])|{'SY','BA'}
        mask=p['rights_masks'][g['rights']]
        if g['principal'] in ('BASE','JOB_SHADOW','JOB_PEDAGOGY'):
            assert not mask&0x40000 and not mask&0x80000 # WRITE_DAC/WRITE_OWNER protected objects
        assert g['inherit'] in ('','OICI')
        flags=g["inherit"] if r["kind"]=="directory" else ""
        aces.append(f"(A;{flags};0x{mask:x};;;{sid})")
    sddl='O:BAG:BAD:P'+''.join(aces)+'(A;;0x0;;;OW)'
    rendered.append({'relative_path':rel,'planned_path':str(PureWindowsPath(p['root'])/PureWindowsPath(rel)),'synthetic_SDDL':sddl,'syntax_validation':validate_in_memory(sddl),'actual_object_created':False})
parents=[]
assert len(p['bootstrap_parents'])==1
for parent in p['bootstrap_parents']:
    assert parent['absolute_path']=='C:\\ProgramData\\TradingOS-S2B-Probe' and parent['new_only']
    assert parent['owner']=='BA' and parent['group']=='BA' and parent['dacl_protected'] and parent['owner_rights_mask']==0 and parent['state']=='NOT_CREATED'
    assert parent['extra_allow']==p['resources'][0]['extra_allow']
    assert parent['delete_policy']=='TRANSACTION_CREATED_EMPTY_NO_REPARSE_NONRECURSIVE_ONLY'
    # Exact protected bootstrap parent shares root's already-validated grant template.
    sddl=rendered[0]['synthetic_SDDL']
    parents.append({'planned_path':parent['absolute_path'],'synthetic_SDDL':sddl,'syntax_validation':validate_in_memory(sddl),'actual_object_created':False,'new_only':True})
result={'schema_version':'r013-s2b-rendered-plan-v1','mode':'PLAN_ONLY','gate':'S2B-ADM-01','administrative_authorization':False,'configuration_changes':[],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'policy_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'bindings':'SYNTHETIC_NOT_APPLICABLE_REAL_ENVIRONMENT','resources':rendered,'resource_count':len(rendered),'bootstrap_parents':parents,'bootstrap_parent_count':len(parents),'synthetic_descriptor_count':len(rendered)+len(parents),'actual_security_acceptance':'NOT_TESTED'}
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'mode':'PLAN_ONLY','resources':len(rendered),'bootstrap_parents':len(parents),'all_synthetic_sddl_valid':all(x['syntax_validation']=='VALID_SYNTACTIC_DESCRIPTOR_ONLY' for x in rendered+parents),'configuration_changes':[],'S2_B_acceptance':'NOT_TESTED'},indent=2))
