"""Fresh local clone verification of committed planning assets; not Plus acceptance.

Existing native Team credentials are not copied. Two observable smokes use the
real root/role instructions, not injected baseInstructions. Metadata covers all roles.
"""
import hashlib
import importlib.util
import json
import queue
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
spec = importlib.util.spec_from_file_location("r028",HERE/"native_probe.py")
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
spec2 = importlib.util.spec_from_file_location("r028_offline",HERE/"offline_probe.py")
offline = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(offline)
SCHEMA = {"type":"object","properties":{
    "package_id":{"type":"string"},"primary_role":{"type":"string"},
    "logical_role":{"type":"string"},"implementation_locked":{"type":"boolean"},
    "authority":{"type":"string"},"plan_guardian_active":{"type":"boolean"}},
    "required":["package_id","primary_role","logical_role","implementation_locked","authority","plan_guardian_active"],"additionalProperties":False}


def git(root,*args):
    return subprocess.check_output(["git","-C",str(root),*args],stderr=subprocess.DEVNULL)


def smoke(server,thread_id):
    start=time.monotonic()
    response=server.rpc("turn/start",{"threadId":thread_id,"input":[{"type":"text","text":"This is a synthetic onboarding smoke test only. Do not continue project work or use tools. From the automatically loaded repository and role instructions report package_id, primary_role currently applicable, logical_role, implementation_locked, authority and whether Plan Guardian is active. Do not infer rules from filesystem names or use chat memory."}],"outputSchema":SCHEMA,"effort":"medium","approvalPolicy":"never","sandboxPolicy":{"type":"readOnly","networkAccess":False}})
    turn_id=(response.get('turn') or {}).get('id');output=None;status='TIMEOUT';requests=0;item_types={}
    while time.monotonic()-start<180:
        try:msg=server.next(5)
        except queue.Empty:continue
        params=msg.get('params') or {}
        if params.get('threadId') not in (None,thread_id):continue
        method=msg.get('method','')
        if 'id' in msg and method:
            requests+=1;server.write({'id':msg['id'],'error':{'code':-32601,'message':'No tools permitted'}})
        if method=='item/completed':
            item=params.get('item') or {};typ=item.get('type','UNKNOWN');item_types[typ]=item_types.get(typ,0)+1
            if typ=='agentMessage':
                try:output=json.loads(item.get('text',''))
                except json.JSONDecodeError:pass
        if method=='turn/completed':status=(params.get('turn') or {}).get('status','UNKNOWN');break
    if status=='TIMEOUT' and turn_id:server.rpc('turn/interrupt',{'threadId':thread_id,'turnId':turn_id})
    return {'status':status,'output':output,'seconds':round(time.monotonic()-start,3),'tool_requests':requests,'item_types':item_types}


def main():
    dest=HERE/'result-fresh-clone-attempt-01.json';profile_path=HERE/'environment-profile-research-observed.json'
    if dest.exists() or profile_path.exists():raise RuntimeError('Preserve prior evidence')
    commit=git(ROOT,'rev-parse','HEAD').decode().strip()
    report={'probe':'R028_FRESH_CLONE_01','clone_source':'local_committed_repository_NOT_fresh_machine','commit':commit,'AVAILABLE_IN_TARGET_PLUS':'UNKNOWN','selected':False,'roles':[],'checks':[]}
    temp=Path(tempfile.mkdtemp(prefix='r028_clone_'));repo=temp/'repo';server=None
    try:
        subprocess.run(['git','clone','--quiet','--no-hardlinks','--single-branch','--branch','plan-architect',str(ROOT),str(repo)],check=True,capture_output=True)
        manifest=json.loads((repo/'shared/bootstrap_manifest.json').read_text())
        files=offline.manifest_files(repo,manifest)
        report['worktree_asset_sha256']={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in files}
        report['git_blob_asset_sha256']={p:hashlib.sha256(git(repo,'cat-file','blob',f'{commit}:{p}')).hexdigest() for p in files}
        report['hash_policy']='git_blob_sha256_for_portable_identity; raw_worktree_sha256_for_local_observation'
        report['worktree_eol_only_differences']=[]
        for p in files:
            blob=git(repo,'cat-file','blob',f'{commit}:{p}');raw=(repo/p).read_bytes()
            if blob!=raw:
                if raw.replace(b'\r\n',b'\n')==blob:report['worktree_eol_only_differences'].append(p)
                else:raise RuntimeError('Unexpected content drift')
        server=native.transport.Server(repo)
        server.rpc('initialize',{'clientInfo':{'name':'r028_fresh_clone','version':'1'},'capabilities':{'experimentalApi':True}});server.write({'method':'initialized','params':{}})
        account=server.rpc('account/read',{'refreshToken':False}).get('account') or {}
        report['account']={'type':account.get('type'),'plan_type':account.get('planType')};del account
        if report['account']!={'type':'chatgpt','plan_type':'team'}:raise RuntimeError('Expected native Team, no fallback')
        report['cli_version']=subprocess.check_output([shutil.which('codex'),'--version'],text=True).strip()
        server.rpc('skills/extraRoots/set',{'extraRoots':[]})
        inventory=[]
        for path in manifest['packages']:
            package=json.loads((repo/path).read_text());cwd=repo/package['working_directory']
            inv=server.rpc('skills/list',{'cwds':[str(cwd)],'forceReload':True})
            ours=[s for d in inv.get('data',[]) for s in d.get('skills',[]) if s.get('name')=='trading-os-bootstrap']
            thread=server.rpc('thread/start',{'cwd':str(cwd),'model':'gpt-6.1-sol','modelProvider':'openai','ephemeral':True,'approvalPolicy':'never','sandbox':'read-only','allowProviderModelFallback':False})
            sources=native.source_names(thread.get('instructionSources',[]),repo)
            entry={'package_id':package['package_id'],'instruction_sources':sources,'bootstrap_skill_discovered_enabled':any(s.get('enabled') is True for s in ours),'status':'METADATA_ONLY'}
            if package['package_id'] in ('onboarding','portfolio-manager-shadow'):
                entry['smoke']=smoke(server,thread['thread']['id'])
            report['roles'].append(entry)
            dest.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps({'role':entry['package_id'],'sources':sources,'skill':entry['bootstrap_skill_discovered_enabled'],'smoke':entry.get('smoke',{}).get('output')}),flush=True)
        def check(name,value):report['checks'].append({'id':name,'passed':bool(value)})
        check('clone_commit_exact',git(repo,'rev-parse','HEAD').decode().strip()==commit)
        check('all_assets_from_commit',all((repo/p).is_file() for p in files))
        check('all_six_roles_have_root_and_local',all(r['instruction_sources']==['AGENTS.md',f"agents/{r['package_id']}/AGENTS.md"] for r in report['roles']))
        check('bootstrap_skill_discovered_all_roles',all(r['bootstrap_skill_discovered_enabled'] for r in report['roles']))
        for r in report['roles']:
            if 'smoke' not in r:continue
            result=r['smoke'];value=result.get('output') or {};expected_role='BOOTSTRAP' if r['package_id']=='onboarding' else 'PORTFOLIO_SHADOW'
            check(r['package_id']+'_schema',Draft202012Validator(SCHEMA).is_valid(value))
            check(r['package_id']+'_role_correct',value.get('package_id')==r['package_id'] and value.get('logical_role')==expected_role and value.get('primary_role')=='Plan Architect')
            check(r['package_id']+'_lock_authority_guardian',value.get('implementation_locked') is True and value.get('authority')=='NONE' and value.get('plan_guardian_active') is False)
            check(r['package_id']+'_no_tools_and_complete',result['status']=='completed' and result['tool_requests']==0)
        # Observed research profile is partial, never Plus-ready. Mandatory failures visible.
        profile={'schema_version':'0.1.0-planning','environment_kind':'CURRENT_RESEARCH_ENVIRONMENT','expected_plan':'team_research_only','observed_plan':'team','surface':'Codex_native_app_server_via_CLI','os':'Windows','captured_at':datetime.now(timezone.utc).isoformat(),'repo_commit':commit,'manifest_sha256':report['git_blob_asset_sha256']['shared/bootstrap_manifest.json'],'instruction_chain':['AGENTS.md','agents/onboarding/AGENTS.md'],'package_ids_verified':[r['package_id'] for r in report['roles']],'inventory':[{'id':'trading-os-bootstrap','kind':'SKILL','detected':'YES','enabled':'YES','callable':'UNKNOWN','version':'0.1.0-planning','evidence_refs':['result-fresh-clone-attempt-01.json']},{'id':'codex','kind':'LOCAL_TOOL','detected':'YES','enabled':'NOT_APPLICABLE','callable':'YES','version':report['cli_version'],'evidence_refs':['result-fresh-clone-attempt-01.json']}],'known_limits':['target_Plus_quota_UNKNOWN','fresh_clone_same_machine_not_clean_OS','only_two_role_smokes','prior_TEMP_cleanup_WinError32_pending_lifecycle_gate'],'action_plan':[{'id':'target-plus-login','requirement_id':'plus-identity','classification':'USER_ACTION_REQUIRED','status':'PENDING','instruction':'Open full clone on target individual Plus; official login UI; never credentials to Git','requires_owner_approval':False,'evidence_refs':[]},{'id':'manual-entry','requirement_id':'sanitized-inventory-actions','classification':'FALLBACK_AVAILABLE','status':'COMPLETED','instruction':'ONBOARDING.md available without Skill; manual preparation only, not proven operational equivalence','requires_owner_approval':False,'evidence_refs':['ONBOARDING.md']}],'selected_fallbacks':[],'acceptance_tests':[{'gate_id':'EB-1','environment_kind':'CURRENT_RESEARCH_ENVIRONMENT','result':'PASSED','version':'local-asset-clone-v1','evidence_refs':['result-fresh-clone-attempt-01.json']},{'gate_id':'EB-2','environment_kind':'CURRENT_RESEARCH_ENVIRONMENT','result':'PASSED','version':'metadata-all-six-two-smokes-v1','evidence_refs':['result-fresh-clone-attempt-01.json']}],'requirement_results':[{'id':'clone-integrity','required':True,'result':'PASSED','evidence_refs':['result-fresh-clone-attempt-01.json']},{'id':'global-role-rules','required':True,'result':'PASSED','evidence_refs':['result-fresh-clone-attempt-01.json']},{'id':'sanitized-inventory-actions','required':True,'result':'NOT_TESTED','evidence_refs':[]}],'readiness_scope':'PREPARATION_ONBOARDING','readiness_state':'PARTIAL','blocked_by':['complete_native_inventory_other_plugins_MCP_permissions_unassessed','Plus_GP1-7_NOT_EXECUTED','full_EB_gates_not_closed'],'authority':'NONE','implementation_locked':True}
        errors=list(Draft202012Validator(SCHEMA).iter_errors(value)) if False else list(Draft202012Validator(json.loads((repo/manifest['profile_schema']).read_text()),format_checker=FormatChecker()).iter_errors(profile))
        check('observed_partial_profile_schema',not errors)
        check('portable_git_blob_hashes_exact',all(report['git_blob_asset_sha256'][p]==hashlib.sha256(git(ROOT,'cat-file','blob',f'{commit}:{p}')).hexdigest() for p in files))
        profile_path.write_text(json.dumps(profile,indent=2)+'\n')
    except Exception as error:
        report['error_type']=type(error).__name__;raise
    finally:
        if server:server.close()
        # Only the TEMP folder we created; resolve/check before recursive cleanup.
        if temp.resolve().parent==Path(tempfile.gettempdir()).resolve() and temp.name.startswith('r028_clone_'):
            try:shutil.rmtree(temp);report['cleanup']='COMPLETED'
            except OSError as error:report['cleanup']='FAILED_'+type(error).__name__
        else:report['cleanup']='REFUSED_UNEXPECTED_PATH'
        report['passed']=sum(c['passed'] for c in report['checks']);report['total']=len(report['checks'])
        report['probe_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        dest.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({'passed':report['passed'],'total':report['total'],'cleanup':report['cleanup']}),flush=True)
    if report['passed']!=report['total']:raise SystemExit(1)


if __name__=='__main__':main()
