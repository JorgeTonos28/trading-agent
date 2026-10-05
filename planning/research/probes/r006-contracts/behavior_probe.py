"""Focal Team regression; reuse wave 04 transport without modifying historical code."""
import hashlib
import importlib.util
import json
import queue
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
PRIOR = ROOT.parent / 'r006-behavioral-team' / 'probe.py'
spec = importlib.util.spec_from_file_location('r006_prior_transport', PRIOR)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
MARKERS = {'research': 'RESEARCH-CONTRACT-V3', 'failure': 'RESEARCH-CONTRACT-V3',
           'quant': 'QUANT-CONTRACT-V2', 'shadow': 'SHADOW-CONTRACT-V2', 'pedagogy': 'PEDAGOGY-CONTRACT-V2'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trial(server, cwd, case, variant, fixture):
    start = time.monotonic()
    record = {'case': case, 'variant': variant, 'output': None, 'tool_trace': [], 'unexpected_tools': [], 'usage': None}
    inputs = [{'type': 'text', 'text': f"Variant={variant}. trusted_role={fixture['role']}; bundle={case}; "
               + json.dumps({k: fixture['data'][k] for k in ('snapshot_id', 'snapshot_hash', 'decision_at', 'knowledge_asof')})
               + '. ' + fixture['task']}]
    if variant == 'skill':
        directory = 'research' if case == 'failure' else case
        name = f'r006-contract-{directory}'
        source = ROOT / 'skills' / directory / 'SKILL.md'
        dest = cwd / 'skills' / name / 'SKILL.md'
        dest.parent.mkdir(parents=True)
        shutil.copyfile(source, dest)
        server.rpc('skills/extraRoots/set', {'extraRoots': [str(cwd / 'skills')]})
        inventory = server.rpc('skills/list', {'cwds': [str(cwd)], 'forceReload': True})
        discovered = [s for group in inventory.get('data', []) for s in group.get('skills', []) if s.get('name') == name]
        if not any(s.get('enabled') for s in discovered):
            raise RuntimeError('Skill discovery unavailable; no inference')
        inputs[0]['text'] += f' Apply ${name}.'
        inputs.append({'type': 'skill', 'name': name, 'path': str(dest)})
        record['skill_sha256'] = digest(source)
        record['skill_discovered_enabled'] = True
    else:
        server.rpc('skills/extraRoots/set', {'extraRoots': []})
    schema_path = ROOT / 'schemas' / f"{fixture['role']}.json"
    schema = json.loads(schema_path.read_text())
    tool = {'type': 'function', 'name': 'read_evidence', 'description': 'Read fixed synthetic bundle, no side effects.',
            'inputSchema': {'type': 'object', 'properties': {'bundle': {'type': 'string'}},
                            'required': ['bundle'], 'additionalProperties': False}}
    thread = server.rpc('thread/start', {'cwd': str(cwd), 'model': 'gpt-6.1-sol', 'modelProvider': 'openai',
                        'ephemeral': True, 'approvalPolicy': 'never', 'sandbox': 'read-only',
                        'baseInstructions': (ROOT / 'common_contract.txt').read_text(),
                        'developerInstructions': 'Synthetic planning only; no other tools or delegation.',
                        'dynamicTools': [tool], 'allowProviderModelFallback': False})
    if thread.get('modelProvider') != 'openai' or thread.get('model') != 'gpt-6.1-sol':
        raise RuntimeError('Unexpected model/provider')
    tid = thread['thread']['id']
    record['effective_runtime'] = {k: thread.get(k) for k in ('model', 'modelProvider', 'sandbox', 'multiAgentMode')}
    started = server.rpc('turn/start', {'threadId': tid, 'input': inputs, 'outputSchema': schema, 'effort': 'medium',
                         'approvalPolicy': 'never', 'sandboxPolicy': {'type': 'readOnly', 'networkAccess': False}})
    turn_id = started['turn']['id']
    deadline = time.monotonic() + 210
    reads = 0
    messages = []
    record['turn_status'] = 'started'
    while time.monotonic() < deadline:
        try:
            msg = server.next(min(10, max(.01, deadline - time.monotonic())))
        except queue.Empty:
            continue
        method, params = msg.get('method', ''), msg.get('params') or {}
        if params.get('threadId') not in (None, tid):
            continue
        if 'id' in msg and method:
            if method == 'item/tool/call' and params.get('tool') == 'read_evidence':
                reads += 1
                args = params.get('arguments')
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except json.JSONDecodeError:
                        args = {}
                success = args == {'bundle': case} and reads <= 2 and fixture['failure'] != 'permanent'
                record['tool_trace'].append({'tool': 'read_evidence', 'arguments': args, 'success': success})
                payload = fixture['data'] if success else {'error': 'synthetic_read_failed', 'retryable': reads < 2}
                server.write({'id': msg['id'], 'result': {'success': success,
                              'contentItems': [{'type': 'inputText', 'text': json.dumps(payload)}]}})
            else:
                record['unexpected_tools'].append({'method': method, 'tool': params.get('tool', 'UNKNOWN')})
                server.write({'id': msg['id'], 'error': {'code': -32601, 'message': 'Rejected by synthetic allowlist'}})
        if method == 'item/completed':
            item = params.get('item') or {}
            if item.get('type') == 'agentMessage':
                messages.append(item.get('text', ''))
            if item.get('type') in ('commandExecution', 'mcpToolCall', 'collabAgentToolCall'):
                record['unexpected_tools'].append({'item_type': item['type']})
        if method == 'thread/tokenUsage/updated':
            usage = params.get('tokenUsage') or {}
            record['usage'] = {k: usage.get(k) for k in ('total', 'last', 'modelContextWindow')}
        if method == 'turn/completed':
            record['turn_status'] = params.get('turn', {}).get('status', 'UNKNOWN')
            break
    else:
        server.rpc('turn/interrupt', {'threadId': tid, 'turnId': turn_id})
        record['turn_status'] = 'timeout'
    try:
        record['output'] = json.loads(messages[-1]) if messages else None
    except json.JSONDecodeError:
        record['output'] = None  # never dump provider diagnostics
    record['schema_error_count'] = len(list(Draft202012Validator(schema).iter_errors(record['output'])))
    record['duration_seconds'] = round(time.monotonic() - start, 3)
    record['schema_sha256'] = digest(schema_path)
    return record


def main():
    fixtures = json.loads((ROOT / 'fixtures.json').read_text(encoding='utf-8'))
    output = ROOT / 'result-team-attempt-01.json'
    if output.exists():
        raise RuntimeError('Never overwrite historical attempt')
    report = {'probe': 'R006-CONTRACT-TEAM-01', 'protocol_version': '1', 'selected': False,
              'AVAILABLE_IN_TARGET_PLUS': 'UNKNOWN', 'trials': [], 'model': 'gpt-6.1-sol', 'effort': 'medium',
              'cli_version': subprocess.check_output([shutil.which('codex'), '--version'], text=True).strip(),
              'fixtures_sha256': digest(ROOT / 'fixtures.json'), 'common_contract_sha256': digest(ROOT / 'common_contract.txt'),
              'transport_source_sha256': digest(PRIOR), 'config_overrides': prior.CONFIG}
    with tempfile.TemporaryDirectory(prefix='r006_contract_team_') as sandbox:
        server = prior.Server(sandbox)
        try:
            server.rpc('initialize', {'clientInfo': {'name': 'r006_contract_probe', 'version': '1'},
                                     'capabilities': {'experimentalApi': True}})
            server.write({'method': 'initialized', 'params': {}})
            account = server.rpc('account/read', {'refreshToken': False}).get('account') or {}
            if account.get('type') != 'chatgpt' or account.get('planType') != 'team':
                raise RuntimeError('Native Team required; no auth/plan/API fallback')
            report['environment'] = {'type': account['type'], 'plan_type': account['planType']}
            del account
            models = server.rpc('model/list', {'includeHidden': False}).get('data', [])
            if not any(m.get('model') == 'gpt-6.1-sol' and any(x.get('reasoningEffort') == 'medium'
                       for x in m.get('supportedReasoningEfforts', [])) for m in models):
                raise RuntimeError('Preregistered model/effort unavailable')
            for index, (case, fixture) in enumerate(fixtures.items()):
                for variant in (('minimal', 'skill') if index % 2 == 0 else ('skill', 'minimal')):
                    cwd = Path(sandbox) / f'trial-{len(report["trials"]) + 1}'
                    cwd.mkdir()
                    record = trial(server, cwd, case, variant, fixture)
                    report['trials'].append(record)
                    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
                    print(json.dumps({'case': case, 'variant': variant, 'status': record['turn_status'],
                                     'schema_errors': record['schema_error_count'], 'seconds': record['duration_seconds']}), flush=True)
                    expected = MARKERS[case] if variant == 'skill' else 'NONE'
                    if record['turn_status'] != 'completed' or (record['output'] or {}).get('procedure_marker') != expected:
                        raise RuntimeError('Noncompleted turn or missing delivery marker; retain attempt')
        finally:
            server.close()
            report['source_sha256'] = digest(Path(__file__))
            report['diagnostic_lines_not_persisted'] = server.diagnostic_lines
            output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
