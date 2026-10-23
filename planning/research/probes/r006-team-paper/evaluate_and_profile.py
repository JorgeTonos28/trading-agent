"""Evaluate immutable wave07 results and publish sanitized pinned Team profile.

Synthetic ledger classification is explicitly separate from durable implementation.
"""
import hashlib
import importlib.util
import json
import statistics
import subprocess
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

HERE=Path(__file__).resolve().parent;REPO=HERE.parents[3]
SPINE=HERE.parent/'r006-contracts'
spec=importlib.util.spec_from_file_location('admission',SPINE/'admission_probe.py')
spine=importlib.util.module_from_spec(spec);spec.loader.exec_module(spine)

def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def ref(name):return 'planning/research/probes/r006-team-paper/'+name

def main():
    d=load(HERE/'result-attempt-02.json');b=load(HERE/'result-bootstrap-SDK-completion-02.json')
    rs=d['trials'];shadow=[t for t in rs if t['case']=='shadow']
    def signature(t):return [(p['instrument_id'],p['action'],p['target_quantity'],p['priority']) for p in t['output']['payload']['proposals']]
    # Evaluate reception at one logical job, not re-label the original trial job IDs.
    ledger=[];seen=set();logical='SYN-OFFLINE-RECOVERY'
    for trial in shadow:
        classification=spine.delivery(True,True,True,logical in seen,trial['admission']=='ACCEPTED')
        ledger.append({'logical_job':logical,'original_trial_job':trial['job_id'],'classification':classification})
        if classification=='ACCEPTED_ON_TIME':seen.add(logical)
    negatives={'late':spine.delivery(True,True,False,False),'missing':spine.delivery(False,True,True,False),
               'unpaired':spine.delivery(True,False,True,False),'invalid':spine.delivery(True,True,True,False,False)}
    checks={'eight_recorded':len(rs)==8,'eight_passed':all(t['passed'] for t in rs),
        'seven_functional_one_control':sum(t['case']!='failure' for t in rs)==7,
        'source_clone_equal':d['source_commit']==d['clone_commit'],
        'shadow_snapshot_equal':shadow[0]['snapshot_hash']==shadow[1]['snapshot_hash'],
        'shadow_numeric_signature_equal':signature(shadow[0])==signature(shadow[1]),
        'restarted':d['restart_before_shadow_B'],'no_unexpected_tools':all(not t['unexpected_requests'] for t in rs),
        'failure_two_reads':len(rs[-1]['tool_trace'])==2 and all(not x['success'] for x in rs[-1]['tool_trace']),
        'onboarding_completion':b['passed'],'six_package_metadata':len(b['metadata'])==6,
        'duplicate_classification_offline':ledger[-1]['classification']=='DUPLICATE',
        'late_classification_offline':negatives['late']=='LATE_RETROSPECTIVE_ONLY',
        'nooutput_classification_offline':negatives['missing']=='NO_OUTPUT',
        'unpaired_classification_offline':negatives['unpaired']=='UNPAIRED',
        'invalid_classification_offline':negatives['invalid']=='REJECTED_SCHEMA'}
    summary={'checks':checks,'passed':all(checks.values()),'n_checks':len(checks),'selected':False,
        'scope':'bounded feasibility and pinned Team clone; ledger classifier offline, no durable runtime',
        'functional_jobs':7,'control_jobs':1,'schema_admitted':sum(t['admission']=='ACCEPTED' for t in rs),
        'service_mean_seconds':statistics.mean(t['service_seconds'] for t in rs),'service_sum_seconds':round(sum(t['service_seconds'] for t in rs),3),
        'service_max_seconds':max(t['service_seconds'] for t in rs),'burst_max_total_seconds':max(t['total_seconds'] for t in rs[3:6]),
        'shadow_numeric_signature_equal':checks['shadow_numeric_signature_equal'],'complete_shadow_proposal_equal':d['shadow_restart_comparison']['canonical_proposals_equal'],
        'offline_ledger':ledger,'offline_negatives':negatives,'future_Plus':'UNKNOWN_PRELIVE'}
    manifest_bytes=subprocess.check_output(['git','show',b['source_commit']+':shared/bootstrap_manifest.json'])
    manifest=json.loads(manifest_bytes)
    evidence=[ref('result-attempt-02.json'),ref('result-bootstrap-SDK-completion-02.json')]
    profile={'schema_version':'0.2.0-planning','environment_kind':'PAPER_RUNTIME_ENVIRONMENT','expected_plan':'Team',
        'observed_plan':'team','surface':'Codex_native_CLI_app_server_via_Python_SDK','os':'Windows',
        'captured_at':b['captured_at'],'repo_commit':b['source_commit'],'manifest_sha256':hashlib.sha256(manifest_bytes).hexdigest(),
        'instruction_chain':['AGENTS.md','agents/onboarding/AGENTS.md'],
        'package_ids_verified':[x['package_id'] for x in b['metadata']],
        'inventory':[
            {'id':'native_Codex_CLI','kind':'RUNTIME','detected':'YES','enabled':'YES','callable':'YES','version':d['cli_version'],'evidence_refs':evidence},
            {'id':'official_Python_SDK_external_temporary_dependencies','kind':'DEPENDENCY','detected':'YES','enabled':'YES','callable':'YES','version':d['sdk_version'],'evidence_refs':evidence},
            {'id':'trading-os-bootstrap','kind':'SKILL','detected':'YES','enabled':'YES','callable':'YES','version':'repo_commit_'+b['source_commit'],'evidence_refs':[ref('result-bootstrap-SDK-completion-02.json')]},
            {'id':'optional_plugins_apps_inventory','kind':'PLUGIN','detected':'UNKNOWN','enabled':'UNKNOWN','callable':'UNKNOWN','version':'UNKNOWN_not_required_for_candidate_jobs','evidence_refs':evidence},
            {'id':'optional_MCP_host_inventory','kind':'MCP','detected':'UNKNOWN','enabled':'UNKNOWN','callable':'UNKNOWN','version':'UNKNOWN_not_required_for_candidate_jobs','evidence_refs':evidence}],
        'known_limits':['8 bounded jobs; sustained WL-R/quota reset/auth lifecycle NOT_TESTED','shared Team use 30% before, 32% after; not attributable to jobs alone','external auth/SDK/local dependencies not supplied by Git clone','profile pins tested c53a130 assets; later changes require scoped drift review'],
        'action_plan':[
            {'id':'architecture-governance','requirement_id':'final-selection-approval','classification':'USER_ACTION_REQUIRED','status':'PENDING','instruction':'Decide proposed ADR-011 PAPER native jobs direction; do not select or freeze by silence.','requires_owner_approval':True,'evidence_refs':['planning/decisions/ADR-011-paper-team-agentic-direction-proposed.md']},
            {'id':'security-and-runtime-spec','requirement_id':'team-TP1-7','classification':'AUTOMATED','status':'PENDING','instruction':'After direction, complete P1 permissions/workflow/storage/version protocols; material security approval separately.','requires_owner_approval':True,'evidence_refs':['planning/research/R-006_native_job_boundary_RC0.md']},
            {'id':'sustained-paper-operation','requirement_id':'team-TP1-7','classification':'AUTOMATED','status':'PENDING','instruction':'P2 after DoR/implementation: financial integration, sustained final workload, quota/auth/recovery and educational validation.','requires_owner_approval':False,'evidence_refs':['planning/research/R-006_team_runtime_acceptance_RC0.md']},
            {'id':'manual-preparation-fallback','requirement_id':'portability-EB1-8','classification':'FALLBACK_AVAILABLE','status':'COMPLETED','instruction':'Explicit root/role/contract reading supports preparation; not selected as autonomous PAPER-equivalent.','requires_owner_approval':False,'evidence_refs':['ONBOARDING.md']}],
        'selected_fallbacks':[],
        'acceptance_tests':[
            {'gate_id':'TP-1_native_identity','environment_kind':'PAPER_RUNTIME_ENVIRONMENT','result':'PASSED','version':'wave07_scoped','evidence_refs':evidence},
            {'gate_id':'TP-2_3_synthetic_workflows','environment_kind':'PAPER_RUNTIME_ENVIRONMENT','result':'PASSED','version':'wave07_scoped','evidence_refs':evidence},
            {'gate_id':'EB-1_2_5_clone_rules_metadata_smoke','environment_kind':'PAPER_RUNTIME_ENVIRONMENT','result':'PASSED','version':'SDK_completion02_scoped','evidence_refs':[ref('result-bootstrap-SDK-completion-02.json')]},
            {'gate_id':'TP-4_financial_OS_isolation','environment_kind':'PAPER_RUNTIME_ENVIRONMENT','result':'NOT_TESTED','version':'not_closed_by_synthetic_harness','evidence_refs':evidence},
            {'gate_id':'TP-5_durable_recovery','environment_kind':'PAPER_RUNTIME_ENVIRONMENT','result':'NOT_TESTED','version':'context_restart_only','evidence_refs':evidence},
            {'gate_id':'TP-6_sustained_operational_capacity','environment_kind':'PAPER_RUNTIME_ENVIRONMENT','result':'NOT_TESTED','version':'bounded_feasibility_only','evidence_refs':evidence}],
        'requirement_results':[], 'readiness_scope':'PAPER_AGENT_ENVIRONMENT','readiness_state':'PARTIAL',
        'blocked_by':['final-selection-approval','team-TP1-7','portability-EB1-8'], 'authority':'NONE','implementation_locked':True}
    for req in manifest['requirements']:
        ident=req['id'];ok=ident in ('clone-integrity','global-role-rules','team-identity','sanitized-inventory-actions')
        profile['requirement_results'].append({'id':ident,'required':'PAPER_AGENT_ENVIRONMENT' in req['required_scopes'],
                    'result':'PASSED' if ok else 'NOT_TESTED','evidence_refs':evidence})
    schema=load(REPO/'shared/environment_profile.schema.json')
    Draft202012Validator(schema,format_checker=FormatChecker()).validate(profile)
    for x in profile['requirement_results']:
        for p in x['evidence_refs']:assert (REPO/p).is_file()
    assert profile['readiness_state']!='READY_AGENT_ENVIRONMENT'
    summary['profile_schema_valid']=True
    save(HERE/'evaluation.json',summary);save(HERE/'environment-profile-PAPER-Team-RC0.json',profile)
    print(json.dumps({'passed':summary['passed'],'checks':len(checks),'profile_valid':True,'readiness':'PARTIAL'}))

if __name__=='__main__':main()
