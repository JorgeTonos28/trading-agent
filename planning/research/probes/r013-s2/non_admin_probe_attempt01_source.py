"""Disposable Windows security-design probes using only synthetic canaries.

NOT S2 enforcement. No users, ACLs, firewall, secrets, model or broker calls.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[4]
DEST = Path(__file__).with_name('non-admin-attempt-01.json')
if DEST.exists():
    raise SystemExit('Evidence exists: choose a new attempt filename.')

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()

def sha(value):
    return hashlib.sha256(canonical(value)).hexdigest()

checks = []
def record(name, observed, expected, scope):
    checks.append(dict(id=name, observed=observed, expected=expected, passed=observed == expected, scope=scope))

with tempfile.TemporaryDirectory(prefix='r013_synthetic_') as folder:
    taskdir = Path(folder)
    for domain in ('core', 'shadow', 'pedagogical'):
        (taskdir / domain).mkdir()
    synthetic_core = taskdir / 'core' / 'synthetic-core-canary.txt'
    synthetic_core.write_text('SYNTHETIC_ONLY_NO_CREDENTIAL', encoding='utf-8')
    read_child = 'from pathlib import Path; import sys; print(Path(sys.argv[1]).read_text()=="SYNTHETIC_ONLY_NO_CREDENTIAL")'
    observed = subprocess.run([sys.executable, '-I', '-c', read_child, str(synthetic_core)], cwd=taskdir/'shadow', capture_output=True, text=True, timeout=15, check=True)
    record('NA-01-S1-sibling-read', observed.stdout.strip(), 'True', 'Counterexample: separate folder under same developer identity does not protect core canary')

    # No actual environment secrets are accessed: this is a task-only fake variable.
    taskenv = os.environ.copy()
    taskenv['R013_SYNTHETIC_BROKER_CANARY'] = 'SYNTHETIC_ONLY'
    child_env = 'import os; print("R013_SYNTHETIC_BROKER_CANARY" in os.environ)'
    inherited = subprocess.run([sys.executable, '-I', '-c', child_env], env=taskenv, capture_output=True, text=True, timeout=15, check=True)
    record('NA-02-default-env-inheritance', inherited.stdout.strip(), 'True', 'Real subprocess env inheritance, synthetic variable only')
    minimal = {key: os.environ[key] for key in ('SystemRoot', 'WINDIR') if key in os.environ}
    minimal['TEMP'] = minimal['TMP'] = str(taskdir/'shadow')
    sanitized = subprocess.run([sys.executable, '-I', '-c', child_env], env=minimal, cwd=taskdir/'shadow', capture_output=True, text=True, timeout=15, check=True)
    record('NA-03-explicit-env-removal', sanitized.stdout.strip(), 'False', 'Real sanitized subprocess; not protection from readable files or inherited handles')

    common = {'snapshot_id':'SYN-PAIR-001', 'cutoff':'2026-10-05T13:00:00Z', 'holdings':[{'symbol':'SYN','quantity':'1'}], 'cash':'100', 'signals':[{'id':'SIG-SYN-1','source':'SYN-PUBLIC','value':'NEUTRAL','available_at':'2026-10-05T12:59:00Z'}]}
    champion_a = {'action':'OPEN','contemporaneous_reason':'SYN-CHAMPION-CANARY-A'}
    champion_b = {'action':'CLOSE','contemporaneous_reason':'SYN-CHAMPION-CANARY-B'}
    def project(common_context, champion_decision):
        # Deliberate immutable pre-decision export; no fields/hash of champion payload.
        return json.loads(canonical(common_context))
    export_a, export_b = project(common, champion_a), project(common, champion_b)
    record('NA-04-blind-export-invariance', sha(export_a)==sha(export_b), True, 'Toy projection invariance under Champion decision mutation; no model/OS blinding proof')
    record('NA-05-no-champion-marker', b'SYN-CHAMPION' not in canonical(export_a), True, 'Literal leakage scan only, not semantic non-inference')
    # Demonstrate a field allowlist is insufficient if a permitted source is contaminated.
    contaminated = json.loads(canonical(common))
    contaminated['signals'][0]['value'] = champion_a['contemporaneous_reason']
    record('NA-06-allowlist-not-semantic-blinding', b'SYN-CHAMPION' in canonical(project(contaminated, champion_a)), True, 'Counterexample: provenance/dependency graph needed even with stable top-level fields')

    # Shadow writes a proposal; true pairing/join is held by a trusted external evaluator.
    output = taskdir/'shadow'/'proposal.json'
    output.write_text(json.dumps({'mode':'SHADOW','snapshot_hash':sha(common),'target_quantity':'2'}), encoding='utf-8')
    sealed_digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.write_text(json.dumps({'mode':'SHADOW','snapshot_hash':sha(common),'target_quantity':'99'}), encoding='utf-8')
    record('NA-07-post-seal-mutation-detected', hashlib.sha256(output.read_bytes()).hexdigest()!=sealed_digest, True, 'External digest detects toy mutation only while digest outside attacker control')

result = dict(schema_version='r013-nonadmin-v1', observed_at=datetime.now(timezone.utc).isoformat(), source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(), environment='Team developer research, same Windows identity', synthetic_only=True, admin_changes=[], model_calls=0, checks=checks, acceptance={'S2_SECURITY':'NOT_TESTED','S2_BLINDING_OS':'NOT_TESTED','semantic_blinding':'NOT_DEMONSTRATED','scope':'counterexamples and disposable design probes only'}, cleanup='TemporaryDirectory cleaned')
DEST.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'checks':len(checks),'passed':sum(c['passed'] for c in checks),'S2':'NOT_TESTED','admin_changes':[]}, indent=2))
if not all(c['passed'] for c in checks):
    raise SystemExit(1)
