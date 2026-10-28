"""Repository evidence/contract consistency only; no data/API or trading execution."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
from urllib.parse import unquote
import ast, hashlib, json, re, subprocess, sys

root=Path(__file__).resolve().parents[3]
local_yaml=root/'.local/planning-qa-deps'
if local_yaml.exists():sys.path.insert(0,str(local_yaml))
import yaml
BASE='a249d77';APPROVAL='72ff6de';MAIN='a28d6f3fadeac817591d4fa797d4560046f89a9d'
out=root/'planning/research/financial_phase_final_QA_2026-10-28.json'
if out.exists():raise FileExistsError('Preserve QA capture; use a new version/attempt for repairs')
checks=[]
def git(*args,cwd=root):return subprocess.check_output(['git','-c','core.safecrlf=false',*args],cwd=cwd)
def load(path):return json.loads((root/path).read_text(encoding='utf-8'))
def sha(data):return hashlib.sha256(data).hexdigest()
def check(id,passed,detail=None):checks.append({'id':id,'status':'PASS' if passed else 'FAIL','detail':detail})
changed=set(git('diff','--name-only',BASE).decode().splitlines())
changed.update(git('ls-files','--others','--exclude-standard').decode().splitlines())
files=sorted(f for f in changed if (root/f).is_file())
parsed={'json':0,'yaml':0,'python_ast':0};errors=[]
for name in files:
    try:
        text=(root/name).read_text(encoding='utf-8')
        if name.endswith('.json'):json.loads(text);parsed['json']+=1
        elif name.endswith(('.yaml','.yml')):yaml.safe_load(text);parsed['yaml']+=1
        elif name.endswith('.py'):ast.parse(text);parsed['python_ast']+=1
    except Exception as e:errors.append({'path':name,'error_type':type(e).__name__})
check('STRUCTURED_FILES_PARSE',not errors,{'counts':parsed,'errors':errors})

scope=load('planning/research/probe_scope_evaluation_2026-10-28.json')
for record in scope['captures']:
    path='planning/research/'+record['capture'];r=load(path);folder=(root/path).parent
    check(record['probe']+'_COUNTS_AND_EXPECTATIONS',r['counts']['PASS']==record['reported_PASS'] and r['counts']['FAIL']==0 and r['counts']['ERROR']==0 and len(r['rows'])==record['reported_PASS'])
    if 'source_sha256' in r:
        source=folder/('continue_build.py' if record['probe']=='QL5-02' else 'restore_probe.py' if record['probe']=='H9-RESTORE' else 'volume_units_probe.py' if record['probe']=='DA-S3' else 'probe.py')
        check(record['probe']+'_SOURCE_BYTES',sha(source.read_bytes())==r['source_sha256'])
    else:
        check(record['probe']+'_SOURCE_BYTES',all(sha((folder/n).read_bytes())==v for n,v in r['own_source_hashes'].items()))
    check(record['probe']+'_LOCK_AND_EVIDENCE_LIMITS',r['implementation_locked'] and r['holdout']=='INTEGRITY_UNKNOWN' and r['target_acceptance']=='TARGET_ACCEPTANCE_DEFERRED')
ql4=load('planning/research/probes/r009-archive-boundary/result-01.json')
q5first=load('planning/research/probes/r009-pin-remediation/result-01.json')
q5second=load('planning/research/probes/r009-pin-remediation/result-02.json')
check('QL4_SECURITY_FAILURE_NOT_HIDDEN_BY_EXPECTATIONS',ql4['native_security_verdict']=='FAIL_BOUNDARY_DEMONSTRATED' and not ql4['pin_accepted'] and ql4['counts']['PASS']==6)
check('QL5_FIRST_BUILD_TIMEOUT_NO_SMOKE_PRESERVED',q5first['steps'][0]['status']=='PASS' and q5first['steps'][-1].get('reason')=='TIMEOUT' and not q5first['rows'] and not q5first['pin_accepted'])
check('QL5_CONTINUATION_TIMEOUT_NOT_COMPATIBILITY_FAILURE',q5second['steps'][-1].get('reason')=='TIMEOUT' and not q5second['rows'] and not q5second['pin_security_or_full_parity_accepted'] and q5second['same_code_and_expectations_verified'])
check('QL5_CONTINUATION_LINK_TO_ORIGINAL_CAPTURE',sha((root/'planning/research/probes/r009-pin-remediation/result-01.json').read_bytes())==q5second['first_capture_sha256'])
audit=load('planning/research/probes/r009-archive-boundary/dependency-audit-01.json')
check('AUDIT_COUNTS_NOT_INDEPENDENT_VULNERABILITIES',len(audit['resolved_libraries'])==41 and len(audit['observed_audit_warnings'])==7 and len({url for row in audit['observed_audit_warnings'] for url in row['advisories']})==5 and not audit['pin_security_accepted'])
check('SENTINELS_NOT_BROKER_OR_SOLVER_TESTS',len(next(r for r in scope['captures'] if r['probe']=='B3-S1')['declarative_markers'])==2 and len(next(r for r in scope['captures'] if r['probe']=='R4')['declarative_markers'])==2 and scope['no_composite_acceptance_score'])
check('DA_TIMEZONE_SCOPE_NOT_TESTED',next(r for r in scope['captures'] if r['probe']=='DA-S2')['timezone_parse_DST_acceptance']=='NOT_TESTED_PROTOCOL_CASE_PENDING')
r4=load('planning/research/probes/r027-cap-and-cost-boundaries/result-01.json')
check('R4_NINE_HUNDRED_CELLS_NOT_THRESHOLDS',r4['monotone_parameter_cells']==900 and not r4['mismatches'] and not r4['D031_thresholds_approved'] and not r4['real_solver_accepted'])
h9=load('planning/research/probes/r012-demand-ledger/result-01.json')
check('H9_DELETE_NOT_CAPACITY_OR_POSTGRES',h9['logical_jobs']==1200 and h9['insert_proposals']==2400 and h9['journal_mode']=='delete' and h9['performance_gate']=='NOT_DEFINED_NOT_PASSED' and not h9['PostgreSQL_or_powerloss_or_FSYNC_proven'])
ql3=load('planning/research/probes/r009-lean-local-source/result-01.json')
check('QL3_BUILD_METADATA_NOT_ENGINE_EXECUTION',all(s['status']=='PASS' for s in ql3['steps']) and not ql3['Launcher_Main_invoked'] and not ql3['Engine_Run_invoked'] and not ql3['CLI_Cloud_account_or_billing_used'] and not ql3['pin_or_target_accepted'])
observation=load('planning/research/probes/r009-lean-local-source/build-observation-after-run.json')
binary_dir=root/'.local/ql3-local-source/bin/Release/net10.0'
if binary_dir.exists():check('QL3_LOCAL_DLL_HASHES',all(sha((binary_dir/n).read_bytes())==v for n,v in observation['outputs'].items()))
else:checks.append({'id':'QL3_LOCAL_DLL_HASHES','status':'NOT_CHECKED','detail':'No local research binaries; recorded evidence not target acceptance.'})

registry=load('planning/research/experiment_registry.json');prior=json.loads(git('show',BASE+':planning/research/experiment_registry.json').decode('utf-8'))
check('IMMUTABLE_TWELVE_HYPOTHESES_ZERO_TRIALS',registry['variants']==prior['variants'] and registry['declared_variant_count']==12 and registry['executed_strategy_trial_count']==0 and registry['execution_attempt_count']==0)
config='planning/research/candidate_configs/PRICE_MATR_rules_RC1.json'
check('IMMUTABLE_CONFIG_BYTES', (root/config).read_bytes()==git('show',BASE+':'+config))
dc=load('planning/research/datacards/financial_dataset_cards_RC0.json')['cards']
sub=load('planning/research/datacards/ETF_instrument_admission_RC1.json')['cards']
check('FOUR_PARENT_SIX_INSTRUMENT_CARDS_NOT_ADMITTED',len(dc)==4 and len(sub)==6 and all(c['admission']=='NOT_ADMITTED' and not c['rights_accepted'] and not c['PIT_accepted'] and not c['quality_accepted'] for c in dc+sub))
check('SIX_REQUIRED_ETF_IDENTITIES',set(c['reference_symbol'] for c in sub)=={'SPY','QQQ','IWM','EFA','TLT','GLD'})

costs=load('planning/research/source_cost_scenarios_wave12.json');old_costs=load('planning/research/source_cost_scenarios_wave11.json')
check('PRIOR_COST_MODELS_AND_TWENTY_CELLS_RETAINED',costs['models'][:3]==old_costs['models'] and costs['prior_20_hypothetical_cells_retained'])
capitals=[2000,5000,10000,25000,50000]
cost_ok=len(costs['models'])==6 and costs['mandatory_capitals_USD']==capitals and costs['nominal_reference_USD']==10000
for model in costs['models']:
    monthly=Decimal(model['monthly_component_price_USD']);annual=monthly*12
    cost_ok &= Decimal(model['hypothetical_12_month_component_cost_USD'])==annual and [s['capital_USD'] for s in model['scales']]==capitals and not model['model_selected']
    for s in model['scales']:
        cap=Decimal(s['capital_USD'])
        cost_ok &= Decimal(s['simple_annual_component_cost_percent'])==annual/cap*100
        cost_ok &= s['total_operational_cost']=='UNKNOWN' and s['qualification']=='NOT_EVALUATED'
        if model['name'].startswith('EODHD'):
            cost_ok &= Decimal(s['annual_prepaid_component_cost_percent'])==Decimal(model['published_annual_prepaid_component_USD'])/cap*100
            cost_ok &= Decimal(s['one_month_acquisition_component_cost_percent'])==monthly/cap*100
        if 'first_year_11_month_updates_simple_percent' in s:
            cost_ok &= Decimal(s['first_year_11_month_updates_simple_percent'])==Decimal('659.45')/cap*100
check('SIX_MODELS_ALL_FIVE_CAPITALS_ARITHMETIC',bool(cost_ok),'Component costs only, taxes/FX/operations unknown, not CAGR.')
check('EODHD_PUBLIC_PRICES_NOT_SELECTED_OR_BOUGHT',[m['monthly_component_price_USD'] for m in costs['models'][3:]]==['19.99','29.99','99.99'] and not costs['spend_authorized'] and costs['actual_spend']==0)

vendor=load('planning/research/vendor_inquiries/status.json');evidence=load('planning/research/vendor_inquiries/owner_response_evidence_2026-10-28.json')
check('VENDOR_DATES_NOT_INVENTED',all(i['sent_on'] is None and i['reply_received_on'] is None and i['response_available_for_research_from']=='2026-10-28' for i in vendor['inquiries']) and evidence['actual_vendor_receipt_dates'] is None and evidence['available_for_research_from']=='2026-10-28')
check('VENDOR_NO_MAIL_ACCESS_CONTACT_OR_ADMISSION',not vendor['automatic_send_authorized'] and not evidence['mailbox_accessed'] and not evidence['original_email_or_attachment_inspected'] and all(i['dataset_admission']=='NOT_ADMITTED' for i in vendor['inquiries']))
check('DERIVED_RIGHTS_NO_IMPLICIT_CLOUD_PERMISSION','DERIVED_REPACKAGED_OR_RECONSTRUCTIBLE' in evidence['external_AI_data_policy'] and evidence['EODHD']['reported_confirmations']['private_local_raw_derived_snapshots_audit_backups'].startswith('REPORTED_ALLOWED'))
check('INDIVIDUAL_VENDOR_STATES',vendor['inquiries'][0]['clarification_state']=='VENDOR_INFORMATION_REQUESTED' and vendor['inquiries'][1]['clarification_state']=='PLAN_SCOPE_CLARIFICATION_PENDING' and vendor['inquiries'][1]['technical_state']=='TECHNICAL_ADMISSION_PENDING' and vendor['inquiries'][1]['followup_sent'] is None)

profile=yaml.safe_load((root/'planning/project_profile.yaml').read_text(encoding='utf-8'))
manifest=load('shared/bootstrap_manifest.json');wave=profile['financial_preparation_wave12'];binding=profile['financial_binding_checkpoint_2026_10_28']
check('Q062_DESIGN_APPROVED_Q063_ONLY_PROPOSED',profile['paper_stack_owner_approval_2026_10_28']['state']=='DECIDED_DESIGN_FAMILIES_ONLY' and manifest['financial_stack_selected'] and not manifest['transverse_stack_selected'] and binding['Q063']=='READY_FOR_DECISION_DIRECTION_ONLY')
check('PROFILE_ACTIVE_READINESS17',profile['active_financial_checkpoint']=='financial_preparation_wave12' and wave['readiness']=='planning/17_financial_bindings_and_readiness_RC0.md' and manifest['financial_readiness']==wave['readiness'])
check('NO_IMPLEMENTATION_TARGET_METHOD_OR_B3_ACCEPTANCE',profile['stage']['implementation_locked'] and not profile['stage']['ready_for_implementation'] and not manifest['paper_runtime_accepted'] and not manifest['broker_B3_accepted'] and not manifest['financial_statistical_method_accepted'] and not manifest['financial_configuration_complete'] and wave['confirmation_integrity']=='INTEGRITY_UNKNOWN' and wave['target_acceptance_status']=='TARGET_ACCEPTANCE_DEFERRED')
dd=load('planning/research/DD_E_report_contract_RC0.json')
check('ECONOMIC_DD_GATES_UNCHANGED',not dd['DD_P_threshold_approved'] and not dd['model_method_sufficiency_accepted'] and dd['other_economic_and_Risk_gates_independent'] and dd['holdout']=='INTEGRITY_UNKNOWN')
q=(root/'planning/research/D-025_026_PAPER_workflow_storage_decision_RC0.md').read_text(encoding='utf-8')
d1=(root/'planning/research/R-010_financial_workload_binding_RC0.md').read_text(encoding='utf-8')
check('WORKLOAD_GATE_SCOPE_NOT_ERASED','intensidades nominal/ráfaga/estrés' in q and 'siguen P1 de diseño' in q and 'Q-063' in d1 and 'configuración y suficiencia' in d1)
check('RISK_BASELINE_REMAINING_BUDGET_EXPLICIT','H_j(Y0,0)' in (root/'planning/research/R-027_risk_inputs_and_caps_RC4.md').read_text(encoding='utf-8'))

missing=[];links=0
for name in files:
    if not name.endswith('.md'):continue
    for raw in re.findall(r'\]\(([^)]+)\)',(root/name).read_text(encoding='utf-8')):
        target=raw.strip().split(' "',1)[0].strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://',target) or target.startswith('#'):continue
        target=unquote(target.split('#',1)[0]);links+=1
        if target and not ((root/name).parent/target).resolve().exists():missing.append({'file':name,'target':target})
check('MODIFIED_MARKDOWN_LOCAL_LINKS',not missing,{'checked':links,'missing':missing})
paths=['financial_readiness','master_plan_candidate','candidate_rule_bindings','broker_recommendation','engine_recommendation','latest_source_admission_research','risk_formula_contract','audit_observability_contract','source_cost_scenarios','paper_stack_family_approval']
check('BOOTSTRAP_CURRENT_ARTIFACTS_EXIST',all((root/manifest[p]).is_file() for p in paths))
secret=re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bsk-[A-Za-z0-9_-]{24,}|gh[pousr]_[A-Za-z0-9]{30,}')
matches=[f for f in files if secret.search((root/f).read_text(encoding='utf-8',errors='replace'))]
check('SCOPED_SECRET_MARKERS',not matches,{'matched_files':matches,'limitation':'Scoped marker scan, not a full security audit.'})
check('PLANNING_DOCUMENTATION_ONLY',all(f in ['.gitattributes','AGENTS.md'] or f.startswith(('planning/','docs/master/','shared/')) for f in files))
check('ACTIVE_BRANCH_MAIN_INTACT',git('branch','--show-current').decode().strip()=='plan-architect' and git('rev-parse','main').decode().strip()==MAIN and git('rev-parse','origin/main').decode().strip()==MAIN)
white=subprocess.run(['git','-c','core.safecrlf=false','diff','--check'],cwd=root,capture_output=True,text=True)
check('WORKTREE_WHITESPACE',white.returncode==0,{'exit_code':white.returncode,'output':white.stdout.strip() or white.stderr.strip()})
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'REPO_HASH_STATE_ARITHMETIC_LINK_AND_CONTRACT_CHECKS_NOT_FINANCIAL_ACCEPTANCE',
 'source_sha256':sha(Path(__file__).read_bytes()),'previous_QA_capture':'planning/research/financial_phase_QA_2026-10-28.json','comparison_base':git('rev-parse',BASE).decode().strip(),'approval_commit':git('rev-parse',APPROVAL).decode().strip(),
 'changed_files_checked':len(files),'parse_counts':parsed,'checks':checks,
 'counts':{s:sum(c['status']==s for c in checks) for s in ['PASS','FAIL','NOT_CHECKED']},
 'datasets_admitted':0,'strategy_trials':0,'B3_accepted':False,'method_accepted':False,'PAPER_runtime_accepted':False,
 'implementation_locked':True,'target_acceptance':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN',
 'limitation':'No probe reruns, API calls, dataset rows, trading simulation, administrative action or statistical validation in this check.'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'parsed':parsed,'links':links,'failed':[c for c in checks if c['status']=='FAIL']},ensure_ascii=False,indent=2))
raise SystemExit(1 if report['counts']['FAIL'] else 0)
