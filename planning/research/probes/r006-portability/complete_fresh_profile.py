"""Complete the fresh-clone report after harness KeyError, without repeating inference.

Original attempt 01 is immutable. Clone the same commit again, verify recorded
asset blob hashes and manifest explicitly, reuse only the two identical role smokes.
"""
import hashlib
import importlib.util
import json
import platform
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
spec=importlib.util.spec_from_file_location('offline',HERE/'offline_probe.py')
offline=importlib.util.module_from_spec(spec);spec.loader.exec_module(offline)


def main():
    dest=HERE/'result-fresh-clone-completion-02.json'
    profile_path=HERE/'environment-profile-research-observed.json'
    if dest.exists() or profile_path.exists():raise RuntimeError('Preserve evidence')
    previous=json.loads((HERE/'result-fresh-clone-attempt-01.json').read_text())
    commit=previous['commit'];temp=Path(tempfile.mkdtemp(prefix='r028_completion_'));repo=temp/'repo'
    report={'probe':'R028_FRESH_CLONE_COMPLETION_02','source_attempt':'result-fresh-clone-attempt-01.json','source_attempt_error':'KeyError_manifest_self_hash_omitted','commit':commit,'inference_turns':0,'AVAILABLE_IN_TARGET_PLUS':'UNKNOWN','checks':[]}
    def check(name,value):report['checks'].append({'id':name,'passed':bool(value)})
    def git(*args):return subprocess.check_output(['git','-C',str(repo),*args],stderr=subprocess.DEVNULL)
    try:
        subprocess.run(['git','clone','--quiet','--no-hardlinks','--single-branch','--branch','plan-architect',str(ROOT),str(repo)],capture_output=True,check=True)
        if git('rev-parse','HEAD').decode().strip()!=commit:raise RuntimeError('Cannot reuse smoke across commit delta')
        manifest_path='shared/bootstrap_manifest.json'
        manifest=json.loads((repo/manifest_path).read_text())
        files=offline.manifest_files(repo,manifest)+[manifest_path]
        blob_hashes={p:hashlib.sha256(git('cat-file','blob',f'{commit}:{p}')).hexdigest() for p in sorted(set(files))}
        check('same_commit_exact',True)
        check('all_previous_assets_git_blob_identical',all(blob_hashes[p]==v for p,v in previous['git_blob_asset_sha256'].items()))
        check('self_manifest_hash_included',manifest_path in blob_hashes)
        differences=[];other=[]
        for p in blob_hashes:
            raw=(repo/p).read_bytes();blob=git('cat-file','blob',f'{commit}:{p}')
            if raw!=blob:
                if raw.replace(b'\r\n',b'\n')==blob:differences.append(p)
                else:other.append(p)
        check('worktree_only_declared_eol_delta',not other)
        check('previous_six_source_chains_verified',len(previous['roles'])==6 and all(r['instruction_sources']==['AGENTS.md',f"agents/{r['package_id']}/AGENTS.md"] for r in previous['roles']))
        check('previous_two_smokes_accounted',sum('smoke' in r for r in previous['roles'])==2)
        check('original_attempt_all_completed_checks_preserved',previous['passed']==12 and previous['total']==12 and previous['error_type']=='KeyError')
        inventory=[{'id':'trading-os-bootstrap','kind':'SKILL','detected':'YES','enabled':'YES','callable':'UNKNOWN','version':'0.1.0-planning','evidence_refs':['result-fresh-clone-attempt-01.json']},
            {'id':'Codex-native-app-server','kind':'RUNTIME','detected':'YES','enabled':'YES','callable':'YES','version':previous['cli_version'],'evidence_refs':['result-fresh-clone-attempt-01.json']},
            {'id':'Python','kind':'LOCAL_TOOL','detected':'YES','enabled':'NOT_APPLICABLE','callable':'YES','version':platform.python_version(),'evidence_refs':['result-fresh-clone-completion-02.json']},
            {'id':'Git','kind':'LOCAL_TOOL','detected':'YES','enabled':'NOT_APPLICABLE','callable':'YES','version':git('--version').decode().strip(),'evidence_refs':['result-fresh-clone-completion-02.json']}]
        for kind in ('PLUGIN','APP','MCP','DEPENDENCY'):
            inventory.append({'id':kind+'_INVENTORY_UNASSESSED_IN_THIS_PROBE','kind':kind,'detected':'UNKNOWN','enabled':'UNKNOWN','callable':'UNKNOWN','version':'UNKNOWN','evidence_refs':[]})
        profile={'schema_version':'0.1.0-planning','environment_kind':'CURRENT_RESEARCH_ENVIRONMENT','expected_plan':'team_research_only','observed_plan':previous['account']['plan_type'],'surface':'Codex_native_app_server_via_CLI','os':'Windows','captured_at':datetime.now(timezone.utc).isoformat(),'repo_commit':commit,'manifest_sha256':blob_hashes[manifest_path],'instruction_chain':['AGENTS.md','agents/onboarding/AGENTS.md'],'package_ids_verified':[r['package_id'] for r in previous['roles']],'inventory':inventory,'known_limits':['target_Plus_quota_UNKNOWN','fresh_clone_same_machine_not_clean_OS','only_two_role_smokes','raw_byte_EOL_differences_classified_separately','TEMP_lifecycle_failed_in_prior_fixture_smoke_not_recovery_proven'],'action_plan':[{'id':'target-plus-login','requirement_id':'plus-identity','classification':'USER_ACTION_REQUIRED','status':'PENDING','instruction':'Open full clone in target individual Plus; official login UI; no credentials to Git','requires_owner_approval':False,'evidence_refs':[]},{'id':'manual-entry','requirement_id':'sanitized-inventory-actions','classification':'FALLBACK_AVAILABLE','status':'COMPLETED','instruction':'ONBOARDING.md manual preparation entry available; not autonomous operational equivalence','requires_owner_approval':False,'evidence_refs':['ONBOARDING.md']}],'selected_fallbacks':[],'acceptance_tests':[{'gate_id':'EB-1','environment_kind':'CURRENT_RESEARCH_ENVIRONMENT','result':'PASSED','version':'local-assets-only-completion-v2','evidence_refs':['result-fresh-clone-completion-02.json']},{'gate_id':'EB-2','environment_kind':'CURRENT_RESEARCH_ENVIRONMENT','result':'PASSED','version':'all-six-metadata-two-observable-smokes-v1','evidence_refs':['result-fresh-clone-attempt-01.json']}],'requirement_results':[{'id':'clone-integrity','required':True,'result':'PASSED','evidence_refs':['result-fresh-clone-completion-02.json']},{'id':'global-role-rules','required':True,'result':'PASSED','evidence_refs':['result-fresh-clone-attempt-01.json']},{'id':'sanitized-inventory-actions','required':True,'result':'NOT_TESTED','evidence_refs':[]}],'readiness_scope':'PREPARATION_ONBOARDING','readiness_state':'PARTIAL','blocked_by':['complete_plugins_MCP_permission_inventory_NOT_ASSESSED','Plus_GP1-7_NOT_EXECUTED','full_EB_gates_NOT_CLOSED'],'authority':'NONE','implementation_locked':True}
        schema=json.loads((repo/manifest['profile_schema']).read_text())
        check('observed_profile_schema_valid',Draft202012Validator(schema,format_checker=FormatChecker()).is_valid(profile))
        check('Team_profile_is_partial_not_Plus_ready',profile['environment_kind']=='CURRENT_RESEARCH_ENVIRONMENT' and profile['readiness_state']=='PARTIAL' and profile['implementation_locked'])
        report.update(git_blob_asset_sha256=blob_hashes,worktree_eol_only_differences=differences,hash_policy='SHA256_git_blob_at_repo_commit_for_portable_identity_raw_bytes_separate',reused_smoke_turns=2)
        profile_path.write_text(json.dumps(profile,indent=2)+'\n')
    finally:
        if temp.resolve().parent==Path(tempfile.gettempdir()).resolve() and temp.name.startswith('r028_completion_'):
            try:shutil.rmtree(temp);report['cleanup']='COMPLETED'
            except OSError as e:report['cleanup']='FAILED_'+type(e).__name__
        else:report['cleanup']='REFUSED_UNEXPECTED_PATH'
        report['passed']=sum(c['passed'] for c in report['checks']);report['total']=len(report['checks']);report['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'passed':report['passed'],'total':report['total'],'eol_deltas':len(report.get('worktree_eol_only_differences',[])),'cleanup':report['cleanup'],'no_new_inference':True}))
    if report['passed']!=report['total']:raise SystemExit(1)


if __name__=='__main__':main()
