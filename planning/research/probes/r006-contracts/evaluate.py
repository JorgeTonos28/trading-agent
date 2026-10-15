"""Evaluate saved synthetic behavior; retain both citation-checker interpretations."""
import json
import subprocess
import types
from decimal import Decimal
from pathlib import Path

from admission_probe import ROOT, admit
from behavior_probe import MARKERS


def main():
    path = ROOT / 'result-team-attempt-01.json'
    report = json.loads(path.read_text(encoding='utf-8'))
    # v1 preserved in prerequisite commit, before any behavioral result existed.
    old_source = subprocess.check_output(['git', 'show',
        'bf7a874:planning/research/probes/r006-contracts/admission_probe.py'], text=True, encoding='utf-8')
    legacy = types.ModuleType('legacy_r006_admission')
    legacy.__file__ = str(ROOT / 'admission_probe.py')
    exec(compile(old_source, legacy.__file__, 'exec'), legacy.__dict__)
    records = []
    for trial in report['trials']:
        case, output = trial['case'], trial['output']
        facts = {f['field']: f for f in output['facts']} if output else {}
        expected_marker = MARKERS[case] if trial['variant'] == 'skill' else 'NONE'
        checks = {'completed': trial['turn_status'] == 'completed',
                  'schema': trial['schema_error_count'] == 0,
                  'marker': bool(output) and output['procedure_marker'] == expected_marker,
                  'tools': not trial['unexpected_tools'] and 1 <= len(trial['tool_trace']) <= 2,
                  'admission_v2': bool(output) and admit(case, output) == 'ACCEPTED'}
        if case == 'research':
            checks['case'] = facts.get('growth', {}).get('value') == '12' and bool(output['payload']['falsifier']) and bool(output['payload']['next_test'])
        if case == 'quant':
            checks['case'] = (facts.get('gross_train_return', {}).get('value') == '18'
                and facts.get('trades', {}).get('value') == '12' and len(output['payload']['missing_tests']) >= 2)
        if case == 'shadow':
            props = output['payload']['proposals']
            values = {Decimal(c['result']) for c in output['calculations']}
            checks['case'] = len(props) == 1 and props[0]['action'] == 'OPEN' and props[0]['target_quantity'] == '2' and Decimal(600) in values and Decimal(100) in values
        if case == 'pedagogy':
            checks['case'] = (facts.get('filled', {}).get('value') == '4' and output['payload']['sizing_motive'] == 'UNKNOWN'
                and output['payload']['result_state'] == 'PENDING' and bool(output['payload']['question']) and bool(output['payload']['answer_key']))
        if case == 'failure':
            checks['case'] = output['content_status'] == 'INSUFFICIENT_EVIDENCE' and not facts and not output['calculations'] and all(not t['success'] for t in trial['tool_trace'])
        records.append({'case': case, 'variant': trial['variant'], 'checks': checks,
                        'admission_v1': legacy.admit(case, output) if output else 'NO_OUTPUT',
                        'admission_v2': admit(case, output) if output else 'NO_OUTPUT',
                        'full_pass_v2': all(checks.values()), 'seconds': trial['duration_seconds']})
    summary = {'behavior_probe': report['probe'], 'completed_turns': len(records),
               'admitted_v1': sum(r['admission_v1'] == 'ACCEPTED' for r in records),
               'admitted_v2': sum(r['admission_v2'] == 'ACCEPTED' for r in records),
               'full_pass_v2': sum(r['full_pass_v2'] for r in records),
               'post_observation_amendment': 'Known source.field citation semantics; v1 retained, no output/prompt overwritten.',
               'target_plus': 'UNKNOWN', 'selected': False, 'records': records, 'variants': {}}
    for variant in ('minimal', 'skill'):
        group = [r for r in records if r['variant'] == variant]
        summary['variants'][variant] = {'n': len(group), 'full_pass_v2': sum(r['full_pass_v2'] for r in group),
                                      'mean_seconds': round(sum(r['seconds'] for r in group) / len(group), 3),
                                      'max_seconds': max(r['seconds'] for r in group)}
    (ROOT / 'evaluation-team.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in summary.items() if k not in ('records', 'variants')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
