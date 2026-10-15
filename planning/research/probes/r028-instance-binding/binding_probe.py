"""Disposable B1 probe. Fake scope only; never an operational readiness verifier."""
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / 'shared/environment_profile.schema.json'
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
CHECKER = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
INSTANCE = '00000000-0000-4000-8000-000000000001'
FINGERPRINT = 'a' * 64
REQUIREMENTS = frozenset(('FAKE-1', 'FAKE-2'))


def admit_fixture(profile):
    if list(CHECKER.iter_errors(profile)):
        return False
    if (profile['schema_version'] != '0.3.0-planning'
            or profile['environment_kind'] != 'TARGET_PAPER_ENVIRONMENT'
            or profile['observed_plan'] != 'Plus'
            or profile['compute_host'] != 'OWNER_PERSONAL_WINDOWS'
            or profile['environment_instance_id'] != INSTANCE
            or profile['effective_fingerprint'] != FINGERPRINT
            or profile['target_acceptance_status'] != 'ACCEPTED'):
        return False
    requirements = profile['requirement_results']
    if len(requirements) != len(REQUIREMENTS) or {r['id'] for r in requirements} != REQUIREMENTS:
        return False
    for requirement in requirements:
        if (requirement['required'] is not True or requirement['result'] != 'PASSED'
                or not requirement['evidence_refs']):
            return False
        tests = [t for t in profile['acceptance_tests'] if t['gate_id'] == requirement['id']]
        if len(tests) != 1:
            return False
        test = tests[0]
        if (test['result'] != 'PASSED' or not test['evidence_refs']
                or test['environment_kind'] != 'TARGET_PAPER_ENVIRONMENT'
                or test['gate_phase'] != 'TARGET_ENVIRONMENT_ACCEPTANCE'
                or test['environment_instance_id'] != INSTANCE
                or test['effective_fingerprint'] != FINGERPRINT
                or not set(requirement['evidence_refs']).issubset(test['evidence_refs'])):
            return False
    return all(a['status'] in ('COMPLETED', 'NOT_APPLICABLE') for a in profile['action_plan'])


historical = json.loads((ROOT / 'planning/research/probes/r006-team-paper/environment-profile-PAPER-Team-RC0.json').read_text(encoding='utf-8'))
positive = copy.deepcopy(historical)
positive.update(schema_version='0.3.0-planning', environment_kind='TARGET_PAPER_ENVIRONMENT',
                expected_plan='Plus', observed_plan='Plus', ai_environment='ChatGPT Plus individual',
                compute_host='OWNER_PERSONAL_WINDOWS', decision_reference='ADR-013_D-043',
                design_status='DESIGN_DECIDED', target_acceptance_status='ACCEPTED',
                operational_status='NOT_IMPLEMENTED', environment_instance_id=INSTANCE,
                effective_fingerprint=FINGERPRINT, action_plan=[],
                readiness_state='READY_AGENT_ENVIRONMENT', readiness_scope='PAPER_AGENT_ENVIRONMENT',
                blocked_by=[], selected_fallbacks=[])
positive['requirement_results'] = [dict(id=r, required=True, result='PASSED', evidence_refs=['FAKE-'+r]) for r in sorted(REQUIREMENTS)]
positive['acceptance_tests'] = [dict(gate_id=r, result='PASSED', version='FAKE-ONLY',
    evidence_refs=['FAKE-'+r], environment_kind='TARGET_PAPER_ENVIRONMENT',
    gate_phase='TARGET_ENVIRONMENT_ACCEPTANCE', environment_instance_id=INSTANCE,
    effective_fingerprint=FINGERPRINT) for r in sorted(REQUIREMENTS)]

cases = []


def check(name, mutate, expected=False):
    fixture = copy.deepcopy(positive)
    mutate(fixture)
    actual = admit_fixture(fixture)
    cases.append(dict(id=name, expected=expected, observed=actual,
                      result='PASS' if actual == expected else 'FAIL'))


check('B1-positive-FAKE-subset-only', lambda p: None, True)
check('B1-missing-instance', lambda p: p.pop('environment_instance_id'))
check('B1-missing-fingerprint', lambda p: p.pop('effective_fingerprint'))
check('B1-malformed-UUID', lambda p: p.update(environment_instance_id='not-an-instance'))
check('B1-cross-instance-test', lambda p: p['acceptance_tests'][0].update(environment_instance_id='00000000-0000-4000-8000-000000000002'))
check('B1-cross-fingerprint-test', lambda p: p['acceptance_tests'][0].update(effective_fingerprint='b'*64))
check('B1-design-phase-test', lambda p: p['acceptance_tests'][0].update(gate_phase='DESIGN'))
check('B1-research-environment-test', lambda p: p['acceptance_tests'][0].update(environment_kind='RESEARCH_ENVIRONMENT'))
check('B1-empty-tests', lambda p: p.update(acceptance_tests=[]))
check('B1-invented-scope', lambda p: p['requirement_results'][0].update(id='FAKE-EXTRA'))
check('B1-missing-refs', lambda p: p['acceptance_tests'][0].update(evidence_refs=[]))
check('B1-deferred-status', lambda p: p.update(target_acceptance_status='TARGET_ACCEPTANCE_DEFERRED'))
check('B1-pending-owner-action', lambda p: p.update(action_plan=[dict(id='FAKE-ACTION', requirement_id='FAKE-1', classification='USER_ACTION_REQUIRED', status='PENDING', instruction='FAKE ONLY', requires_owner_approval=True, evidence_refs=[])]))
check('B1-Team-renamed-PAPER', lambda p: p.update(observed_plan='team'))
cases.append(dict(id='B1-original-v02-schema-remains-valid', expected=True,
    observed=not list(CHECKER.iter_errors(historical)),
    result='PASS' if not list(CHECKER.iter_errors(historical)) else 'FAIL'))
cases.append(dict(id='B1-original-v02-not-current-PAPER', expected=False,
    observed=admit_fixture(historical), result='PASS' if not admit_fixture(historical) else 'FAIL'))
result = dict(captured_at=datetime.now(timezone.utc).isoformat(),
    scope='SYNTHETIC_FAKE_REQUIREMENTS_ONLY_NOT_ENVIRONMENT_ACCEPTANCE',
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    schema_sha256=hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest(),
    cases=cases, failures=sum(c['result'] != 'PASS' for c in cases),
    real_environment_identity_created=False, paper_runtime_accepted=False,
    protected_store_or_authenticity_proven=False)
(HERE / 'result-01.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'cases':len(cases), 'failures':result['failures'], 'scope':result['scope']}))
raise SystemExit(bool(result['failures']))
