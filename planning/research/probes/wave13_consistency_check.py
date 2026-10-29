"""Evidence/contract consistency only. No external service, data or runtime acceptance."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import unquote
from decimal import Decimal
import ast,hashlib,json,re,subprocess,sys
root=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(root/'.local/planning-qa-deps'))
import yaml
attempt=sys.argv[1] if len(sys.argv)>1 else '01';assert re.fullmatch(r'\d{2}',attempt)
out=root/f'planning/research/financial_phase_QA_2026-10-29_{attempt}.json';assert not out.exists()
BASE='5eed577';MAIN='a28d6f3fadeac817591d4fa797d4560046f89a9d';checks=[]
def git(*args):return subprocess.check_output(['git','-c','core.safecrlf=false',*args],cwd=root)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name):return json.loads((root/name).read_text(encoding='utf-8'))
def check(id,ok,detail=None):checks.append({'id':id,'status':'PASS' if ok else 'FAIL','detail':detail})
changed=set(git('diff','--name-only',BASE).decode().splitlines())|set(git('ls-files','--others','--exclude-standard').decode().splitlines())
files=sorted(name for name in changed if (root/name).is_file());parse_errors=[];counts={'json':0,'yaml':0,'python_ast':0}
for name in files:
 try:
  text=(root/name).read_text(encoding='utf-8')
  if name.endswith('.json'):json.loads(text);counts['json']+=1
  elif name.endswith(('.yaml','.yml')):yaml.safe_load(text);counts['yaml']+=1
  elif name.endswith('.py'):ast.parse(text);counts['python_ast']+=1
 except Exception as e:parse_errors.append({'file':name,'type':type(e).__name__})
check('STRUCTURED_SOURCE_FILES_PARSE',not parse_errors,{'parsed':counts,'errors':parse_errors})
scope=load('planning/research/probe_scope_evaluation_2026-10-29.json')
for item in scope['captures']:
 name='planning/research/'+item['capture'];d=load(name);folder=(root/name).parent
 check(item['probe']+'_COUNTS_RECORDED_EXACTLY',d['counts']==item['counts'] and all(d['counts'][s]==sum(r['status']==s for r in d['rows']) for s in ['PASS','FAIL','ERROR']))
 check(item['probe']+'_CONTROLLER_RAW_BYTES',sha(folder/item['controller'])==d['controller_sha256'])
 check(item['probe']+'_STEPS_RECORDED_EXACTLY',[s['status'] for s in d.get('steps',[])]==item['step_statuses'])
 check(item['probe']+'_LOCK_TARGET_HOLDOUT',d['implementation_locked'] and d['target_acceptance_status']=='TARGET_ACCEPTANCE_DEFERRED' and d['holdout']=='INTEGRITY_UNKNOWN')
q6=load('planning/research/probes/r009-remediation-diagnostics/result-01.json')
q7a=load('planning/research/probes/r009-extraction-repair/result-01.json');q7b=load('planning/research/probes/r009-extraction-repair/result-02.json');q7c=load('planning/research/probes/r009-extraction-repair/result-03.json')
q8a=load('planning/research/probes/r009-contract-preserving-host/result-01.json');q8b=load('planning/research/probes/r009-contract-preserving-host/result-02.json')
check('QL6_BUILD_SUCCEEDS_SECURITY_FAILURE_REMAINS',all(s['status']=='PASS' for s in q6['steps']) and q6['counts']['PASS']==8 and q6['second_path_security']=='FAIL_BOUNDARY_DEMONSTRATED' and not q6['pin_accepted'])
check('QL7_ERROR01_AND_FAIL02_PRESERVED',q7a['steps'][0]['status']=='ERROR' and not q7a['rows'] and q7b['counts']['FAIL']==1 and next(r for r in q7b['rows'] if r['status']=='FAIL')['id']=='RETURNED_ABSOLUTE_FILE_PATH')
check('QL7_NORMALIZATION_CORRECTION_SEPARATE',q7c['counts']=={'PASS':9,'FAIL':0,'ERROR':0} and q7c['fixture_expected_and_actual_paths_normalized'] and q7c['prior_02_failure_preserved'])
check('QL8_HARNESS_ERROR01_NOT_ERASED',q8a['steps'][-1]['status']=='ERROR' and not q8a['rows'] and not q8a['pin_security_and_parity_accepted'])
check('QL8_CORRECTION02_ONLY_CSHARP_SOURCE_FILES',len(q8b['added_source_file_hashes'])==1171 and all(Path(n).suffix=='.cs' and Path(n).parts[0]!='Data' for n in q8b['added_source_file_hashes']) and q8b['prior_source_patch_and_fixture_hashes_verified'])
check('QL8_BOTH_REPAIRS_AND_LEGACY_RELATIVE_SHAPE',all(s['status']=='PASS' for s in q8b['steps']) and q8b['counts']=={'PASS':14,'FAIL':0,'ERROR':0} and any(row['id']=='LEGACY_RELATIVE_OUTPUT_SHAPE' and row['status']=='PASS' for row in q8b['rows']) and q8b['no_Engine_Run_Main_or_Algorithm_invoked'] and not q8b['pin_security_and_parity_accepted'])
check('CONTINUATION_REFERENCES_ORIGINAL_CAPTURES',q7b['first_capture_sha256']==sha(root/'planning/research/probes/r009-extraction-repair/result-01.json') and q8b['first_capture_sha256']==sha(root/'planning/research/probes/r009-contract-preserving-host/result-01.json'))
manifest=load('planning/research/LEAN_source_repair_candidate_manifest_RC0.json')
hashes=dict(q8a['base_export_file_hashes']);hashes.update(q8b['added_source_file_hashes']);hashes['Compression\\Compression.cs']=q8b['source_repair_sha256']
check('LEAN_CANDIDATE_SOURCE_FINGERPRINT_NOT_ACCEPTED_PIN',manifest['source_hash_fingerprint']==hashlib.sha256(json.dumps(hashes,sort_keys=True,separators=(',',':')).encode()).hexdigest() and manifest['source_files_after_patch']==len(hashes) and not manifest['pin_security_and_parity_accepted'])
for label,folder,d in [('QL8-02','.local/ql8-contract-preserving-host',q8b),('QL6','.local/ql6-remediation-diagnostics',q6)]:
 directory=root/folder
 if directory.exists():check(label+'_LOCAL_ARTIFACT_HASHES',all(sha(directory/name)==digest for name,digest in d['artifact_sha256'].items()))
h10=load('planning/research/probes/r011-admission-cuts/result-01.json');r5=load('planning/research/probes/r027-profile-boundaries/result-01.json')
check('H10_FINITE_ORACLE_AND_MUTATIONS_NOT_PG',h10['traces']==840 and not h10['mismatches'] and all(h10['mutant_counterexamples'].values()) and not h10['PostgreSQL_accepted'] and not h10['SQL_or_broker_or_real_clock_tested'])
capitals=[2000,5000,10000,25000,50000]
check('R5_FIVE_SCALES_NO_NUMERIC_PROFILE_APPROVAL',[s['capital_USD'] for s in r5['scales']]==capitals and r5['scales'][2]['quantity_before_costs']==8 and not r5['baseline_profile_owner_approved'] and r5['partial_case']['R2_status']=='UNCERTAIN')
envelope=load('planning/research/R-010_workload_and_durability_envelope_RC1.json')
check('D2_PAYLOAD_ARITHMETIC_NOT_TOTAL_STORAGE',envelope['capacity_model']['critical_payload_bytes_per_session_at_nominal']==23400*4096 and envelope['capacity_model']['critical_payload_bytes_per_year_at_nominal']==23400*4096*252 and not envelope['capacity_model']['retention_space_and_cost_accepted'])
check('D2_WEEKLY_EXTRA_DENOMINATOR_EXPLICIT',envelope['C_weekly_peak']['required_logical_jobs_on_that_day']==50+3 and envelope['C_weekly_peak']['service_attempt_budget_on_that_day']==53+13 and envelope['C_nominal']['service_attempt_budget_per_day']==50+13)
check('D2_CRASH_DISASTER_RECOVERY_DISTINCT',envelope['durability_proposals']['acknowledged_commit_local_crash_loss_target_count']==0 and envelope['durability_proposals']['disk_disaster_RPO_seconds']==300 and envelope['durability_proposals']['restore_to_PAUSED_diagnostic_RTO_seconds']==3600 and not envelope['durability_proposals']['local_disaster_or_powerloss_accepted'])
registry=load('planning/research/experiment_registry.json');prior=json.loads(git('show',BASE+':planning/research/experiment_registry.json').decode('utf-8'))
check('TWELVE_HYPOTHESES_ZERO_STRATEGY_ATTEMPTS',registry['variants']==prior['variants'] and registry['declared_variant_count']==12 and registry['executed_strategy_trial_count']==0 and registry['execution_attempt_count']==0)
cfg='planning/research/candidate_configs/PRICE_MATR_rules_RC1.json';check('RULE_CONFIG_RAW_BYTES_UNCHANGED',(root/cfg).read_bytes()==git('show',BASE+':'+cfg))
dc=load('planning/research/datacards/financial_dataset_cards_RC0.json')['cards'];sub=load('planning/research/datacards/ETF_instrument_admission_RC1.json')['cards']
check('FOUR_PLUS_SIX_DATACARDS_NOT_ADMITTED',len(dc)==4 and len(sub)==6 and all(c['admission']=='NOT_ADMITTED' and not c['rights_accepted'] and not c['PIT_accepted'] and not c['quality_accepted'] for c in dc+sub))
cost='planning/research/source_cost_scenarios_wave12.json';costs=load(cost)
check('VENDOR_COST_MODELS_REMAIN_UNALTERED',(root/cost).read_bytes()==git('show',BASE+':'+cost) and costs['nominal_reference_USD']==10000 and costs['mandatory_capitals_USD']==capitals)
valid_costs=True
for model in costs['models']:
 valid_costs&=[row['capital_USD'] for row in model['scales']]==capitals and Decimal(model['hypothetical_12_month_component_cost_USD'])==12*Decimal(model['monthly_component_price_USD'])
check('ALL_COST_MODELS_ALL_FIVE_SCALES',valid_costs and costs['prior_20_hypothetical_cells_retained'] and not costs['spend_authorized'])
vendor='planning/research/vendor_inquiries/status.json';check('VENDOR_NO_NEW_REPLY_SEND_DATE_OR_LICENSE_INVENTED',(root/vendor).read_bytes()==git('show',BASE+':'+vendor))
profile=yaml.safe_load((root/'planning/project_profile.yaml').read_text(encoding='utf-8'));bootstrap=load('shared/bootstrap_manifest.json')
check('Q063_APPROVAL_SCOPE_PRESERVED',profile['workflow_storage_owner_approval_2026_10_29']['state']=='DECIDED_CONDITIONAL_DESIGN_DIRECTION_ONLY' and not profile['workflow_storage_owner_approval_2026_10_29']['postgres_accepted'] and bootstrap['workflow_storage_design_direction']['status']=='DECIDED_CONDITIONAL_DIRECTION_ONLY' and bootstrap['transverse_stack_selected'] and not bootstrap['postgres_accepted'])
check('CURRENT_READINESS_Q064_NOT_Q063',profile['active_financial_checkpoint']=='financial_preparation_wave13' and bootstrap['financial_readiness']=='planning/18_financial_hardening_checkpoint_RC0.md' and bootstrap['next_financial_governance']=='Q064_POST_FILL_PROTECTION_POLICY_DIRECTION')
check('NO_FALSE_DOR_B3_METHOD_OR_TARGET_ACCEPTANCE',profile['stage']['implementation_locked'] and not profile['stage']['ready_for_implementation'] and not bootstrap['broker_B3_accepted'] and not bootstrap['engine_pin_and_parity_accepted'] and not bootstrap['paper_runtime_accepted'] and not bootstrap['financial_statistical_method_accepted'] and not bootstrap['financial_configuration_complete'])
pf=(root/'planning/research/R-007_B3_route_and_policy_decision_RC0.md').read_text(encoding='utf-8')
check('PF_NOT_YET_ADMITTED_AND_WORST_REACHABLE_REMAINDER_EXPLICIT','máxima cantidad alcanzable' in pf and 'Antes de ese perfil rige el fail-closed actual' in pf and 'ventana operativa' in pf and 'Sin G3' in pf)
dd=load('planning/research/DD_E_report_contract_RC0.json');check('ECONOMIC_DD_GATES_UNCHANGED',not dd['DD_P_threshold_approved'] and not dd['model_method_sufficiency_accepted'] and dd['holdout']=='INTEGRITY_UNKNOWN')
links=0;broken=[];secret_files=[]
for name in files:
 p=root/name;text=p.read_text(encoding='utf-8')
 if name.endswith('.md'):
  for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
   target=unquote(target.strip().strip('<>')).split('#',1)[0]
   if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('/'):continue
   links+=1
   if not (p.parent/target).resolve().exists():broken.append({'file':name,'target':target})
 if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',text):secret_files.append(name)
check('LOCAL_MARKDOWN_LINKS_RESOLVE',not broken,{'checked':links,'broken':broken})
check('NO_PRIVATE_KEY_BLOCKS_OR_ENV_FILES',not secret_files and not any(Path(n).name=='.env' for n in files))
check('BRANCH_PLAN_ARCHITECT_MAIN_BASELINES_UNCHANGED',git('branch','--show-current').decode().strip()=='plan-architect' and git('rev-parse','main').decode().strip()==MAIN and git('rev-parse','origin/main').decode().strip()==MAIN)
check('DIFF_WHITESPACE_VALID',subprocess.run(['git','diff','--check'],cwd=root,capture_output=True).returncode==0)
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'scope':'REPOSITORY_EVIDENCE_CONSISTENCY_ONLY_NOT_SECURITY_FINANCIAL_STATISTICAL_OR_POSTGRESQL_ACCEPTANCE','controller_sha256':sha(Path(__file__)),'source_parent_commit':BASE,'attempt':attempt,'checks':checks,'counts':{s:sum(c['status']==s for c in checks) for s in ['PASS','FAIL','ERROR']},'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'counts':report['counts'],'failures':[c for c in checks if c['status']=='FAIL']},ensure_ascii=False))
sys.exit(1 if report['counts']['FAIL'] else 0)
