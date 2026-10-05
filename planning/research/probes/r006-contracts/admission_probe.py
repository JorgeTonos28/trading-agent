"""Disposable RC0 admission experiments; no production validator or financial path."""
import copy
import hashlib
import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
FIXTURES = json.loads((ROOT / 'fixtures.json').read_text(encoding='utf-8'))


def dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def admit(case, output):
    """Checks only fixed synthetic spine; prose truth/security need other gates."""
    fixture = FIXTURES[case]
    role = fixture['role']  # trusted caller, never output['role']
    schema = json.loads((ROOT / 'schemas' / f'{role}.json').read_text())
    Draft202012Validator.check_schema(schema)
    if list(Draft202012Validator(schema).iter_errors(output)):
        return 'REJECTED_SCHEMA'
    manifest = fixture['data']
    if any(output[k] != manifest[k] for k in ('snapshot_id', 'snapshot_hash', 'decision_at', 'knowledge_asof')):
        return 'REJECTED_PIT'
    sources = {s['source_id']: s for s in manifest['sources']}
    facts = {}
    for fact in output['facts']:
        if fact['fact_id'] in facts:
            return 'REJECTED_LINEAGE'
        source = sources.get(fact['source_id'])
        if source is None or dt(source['eligible_from']) > dt(manifest['knowledge_asof']):
            return 'REJECTED_PIT'
        observed = source['fields'].get(fact['field'])
        if observed is None or fact['value'] != observed['value'] or fact['unit'] != observed['unit']:
            return 'REJECTED_LINEAGE'
        facts[fact['fact_id']] = fact
    calcs = {}
    for calc in output['calculations']:
        if calc['calculation_id'] in calcs or calc['calculation_id'] in facts:
            return 'REJECTED_LINEAGE'
        inputs = [facts.get(i) for i in calc['input_fact_ids']]
        if len(inputs) != 2 or any(i is None for i in inputs):
            return 'REJECTED_LINEAGE'
        a, b = inputs
        if calc['formula'] == 'cash_minus_reservations@toy-1':
            if a['unit'] != 'USD' or b['unit'] != 'USD':
                return 'REJECTED_LINEAGE'
            expected = Decimal(a['value']) - Decimal(b['value'])
        else:
            if a['unit'] != 'SHARE' or b['unit'] != 'USD_PER_SHARE':
                return 'REJECTED_LINEAGE'
            expected = Decimal(a['value']) * Decimal(b['value'])
        if calc['unit'] != 'USD' or Decimal(calc['result']) != expected:
            return 'REJECTED_LINEAGE'
        calcs[calc['calculation_id']] = calc
    payload = output['payload']
    if case == 'failure':
        if output['content_status'] != 'INSUFFICIENT_EVIDENCE' or facts or calcs:
            return 'REJECTED_LINEAGE'
    if case == 'shadow':
        if output['content_status'] in ('ABSTAIN', 'INSUFFICIENT_EVIDENCE') and payload['proposals']:
            return 'REJECTED_LINEAGE'
        priorities = set()
        aggregate_buy = Decimal(0)
        for prop in payload['proposals']:
            if prop['instrument_id'] != 'SYN-B' or any(s not in sources for s in prop['source_ids']):
                return 'REJECTED_PIT'
            current = Decimal(sources['S1']['fields']['current']['value'])
            target = Decimal(prop['target_quantity'])
            action = prop['action']
            valid = {'OPEN': current == 0 and target > 0, 'INCREASE': current > 0 and target > current,
                     'REDUCE': 0 < target < current, 'CLOSE': current > 0 and target == 0,
                     'HOLD': target == current}[action]
            if target < 0 or not valid or prop['priority'] in priorities:
                return 'REJECTED_LINEAGE'
            priorities.add(prop['priority'])
            c = calcs.get(prop['target_notional_calculation_id'])
            price = Decimal(sources['S1']['fields']['price']['value'])
            if c is None or Decimal(c['result']) != target * price:
                return 'REJECTED_LINEAGE'
            aggregate_buy += max(target - current, Decimal(0)) * price
        available = Decimal(sources['S1']['fields']['cash']['value']) - Decimal(sources['S1']['fields']['reservation']['value'])
        if aggregate_buy > available:
            return 'REJECTED_LINEAGE'  # fixture contract only, not live financial authority
    if case == 'research' and any(s not in sources for s in payload['evidence_ids']):
        return 'REJECTED_PIT'
    if case == 'quant' and payload['verdict'] != 'NOT_VALIDATED':
        return 'REJECTED_LINEAGE'
    if case == 'pedagogy':
        if (payload['sizing_motive'] != 'UNKNOWN' or payload['result_state'] != 'PENDING'
                or any(s not in sources for s in payload['timeline_source_ids'])):
            return 'REJECTED_LINEAGE'
    return 'ACCEPTED'


def exemplar(case):
    fixture = FIXTURES[case]
    out = {'schema_version': 'r006-spine-1', 'role': fixture['role'], 'authority': 'NONE',
           **{k: fixture['data'][k] for k in ('snapshot_id', 'snapshot_hash', 'decision_at', 'knowledge_asof')},
           'content_status': 'COMPLETE', 'procedure_marker': 'NONE', 'facts': [], 'calculations': [], 'unknowns': []}
    for source in fixture['data']['sources']:
        for field, value in source['fields'].items():
            out['facts'].append({'fact_id': field, 'source_id': source['source_id'], 'field': field, **value})
    payloads = {
      'research': {'hypothesis': 'Investigar crecimiento', 'falsifier': 'Sin persistencia', 'next_test': 'OOS', 'evidence_ids': ['R1']},
      'quant': {'verdict': 'NOT_VALIDATED', 'missing_tests': ['costs', 'OOS', 'benchmark'], 'next_test': 'preregister'},
      'shadow': {'mode': 'SHADOW', 'proposals': [{'instrument_id': 'SYN-B', 'action': 'OPEN', 'target_quantity': '2',
                    'target_notional_calculation_id': 'notional', 'priority': 1, 'reasons': ['toy exercise'],
                    'source_ids': ['S1'], 'confidence': None}], 'limitations': ['Not a sizing validation']},
      'pedagogy': {'trade_ids': ['T1'], 'timeline_source_ids': ['P1'], 'explanation': 'Fill parcial; cancel UNKNOWN',
                   'sizing_motive': 'UNKNOWN', 'concepts': ['partial fill'], 'question': '¿Fill completo?',
                   'answer_key': 'No, 4 de 10', 'result_state': 'PENDING'},
      'failure': {'hypothesis': '', 'falsifier': '', 'next_test': 'Recover read', 'evidence_ids': []}}
    out['payload'] = payloads[case]
    if case == 'failure':
        out['content_status'] = 'INSUFFICIENT_EVIDENCE'
    if case == 'shadow':
        out['calculations'] = [
          {'calculation_id': 'available', 'formula': 'cash_minus_reservations@toy-1',
           'input_fact_ids': ['cash', 'reservation'], 'result': '600', 'unit': 'USD'},
          {'calculation_id': 'notional', 'formula': 'quantity_times_price@toy-1',
           'input_fact_ids': ['target', 'price'], 'result': '100', 'unit': 'USD'}]
    return out


def delivery(output_present, paired, on_time, already_admitted, content_valid=True):
    """Pure classification of synthetic ledger records, not durable recovery."""
    if not output_present:
        return 'NO_OUTPUT'
    if not content_valid:
        return 'REJECTED_SCHEMA'
    if already_admitted:
        return 'DUPLICATE'
    if not paired:
        return 'UNPAIRED'
    return 'ACCEPTED_ON_TIME' if on_time else 'LATE_RETROSPECTIVE_ONLY'


def main():
    tests = []
    examples = {c: exemplar(c) for c in FIXTURES}
    for c, out in examples.items():
        tests.append({'case': f'positive_{c}', 'observed': admit(c, out), 'expected': 'ACCEPTED'})

    def negative(name, case, edit, expected):
        out = copy.deepcopy(examples[case])
        edit(out)
        tests.append({'case': name, 'observed': admit(case, out), 'expected': expected})

    negative('role_selects_own_validator', 'shadow', lambda o: o.update(role='RESEARCH_IDEA'), 'REJECTED_SCHEMA')
    negative('localized_role', 'research', lambda o: o.update(role='investigador'), 'REJECTED_SCHEMA')
    negative('authority_order', 'shadow', lambda o: o.update(authority='ORDER_ALLOWED'), 'REJECTED_SCHEMA')
    negative('operative_mode', 'shadow', lambda o: o['payload'].update(mode='OPERATIVE'), 'REJECTED_SCHEMA')
    negative('extra_intent', 'shadow', lambda o: o.update(trade_intent={}), 'REJECTED_SCHEMA')
    negative('research_portfolio_proposal', 'research', lambda o: o['payload'].update(proposals=[]), 'REJECTED_SCHEMA')
    negative('wrong_snapshot', 'shadow', lambda o: o.update(snapshot_hash='another'), 'REJECTED_PIT')
    negative('later_asof', 'shadow', lambda o: o.update(knowledge_asof='2026-10-01T15:00:00Z'), 'REJECTED_PIT')
    negative('future_source', 'research', lambda o: o['facts'][0].update(source_id='FUTURE'), 'REJECTED_PIT')
    negative('invented_observed_value', 'research', lambda o: o['facts'][0].update(value='40'), 'REJECTED_LINEAGE')
    negative('wrong_observed_unit', 'shadow', lambda o: o['facts'][0].update(unit='SHARE'), 'REJECTED_LINEAGE')
    negative('duplicate_fact_id', 'shadow', lambda o: o['facts'].append(o['facts'][0]), 'REJECTED_LINEAGE')
    negative('wrong_derived_result', 'shadow', lambda o: o['calculations'][0].update(result='1000'), 'REJECTED_LINEAGE')
    negative('wrong_derived_unit', 'shadow', lambda o: o['calculations'][1].update(unit='SHARE'), 'REJECTED_LINEAGE')
    negative('cyclic_or_unknown_input', 'shadow', lambda o: o['calculations'][0].update(input_fact_ids=['available', 'reservation']), 'REJECTED_LINEAGE')
    negative('unknown_formula', 'shadow', lambda o: o['calculations'][0].update(formula='model_math'), 'REJECTED_SCHEMA')
    negative('ambiguous_delta_field', 'shadow', lambda o: o['payload']['proposals'][0].update(quantity='2'), 'REJECTED_SCHEMA')
    negative('close_without_position', 'shadow', lambda o: o['payload']['proposals'][0].update(action='CLOSE', target_quantity='0'), 'REJECTED_LINEAGE')
    negative('negative_short_target', 'shadow', lambda o: o['payload']['proposals'][0].update(target_quantity='-2'), 'REJECTED_LINEAGE')
    negative('abstain_with_positions', 'shadow', lambda o: o.update(content_status='ABSTAIN'), 'REJECTED_LINEAGE')
    negative('duplicate_priority_or_double_spend', 'shadow', lambda o: o['payload']['proposals'].append(o['payload']['proposals'][0]), 'REJECTED_LINEAGE')
    negative('sizing_cause_invented', 'pedagogy', lambda o: o['payload'].update(sizing_motive='DOCUMENTED'), 'REJECTED_LINEAGE')
    negative('outcome_invented', 'pedagogy', lambda o: o['payload'].update(result_state='KNOWN'), 'REJECTED_LINEAGE')
    negative('read_failure_fabricated_fact', 'failure', lambda o: o['facts'].append(examples['research']['facts'][0]), 'REJECTED_PIT')
    for name, values, expected in [
        ('on_time', (True, True, True, False), 'ACCEPTED_ON_TIME'),
        ('late_kept_not_on_time', (True, True, False, False), 'LATE_RETROSPECTIVE_ONLY'),
        ('no_output_not_hold', (False, True, True, False), 'NO_OUTPUT'),
        ('different_context', (True, False, True, False), 'UNPAIRED'),
        ('repeat_delivery', (True, True, True, True), 'DUPLICATE'),
        ('invalid_json_delivery', (True, True, True, False, False), 'REJECTED_SCHEMA')]:
        tests.append({'case': name, 'observed': delivery(*values), 'expected': expected})
    for item in tests:
        item['passed'] = item['observed'] == item['expected']
    replay_a = [admit(c, o) for c, o in examples.items()]
    replay_b = [admit(c, json.loads(json.dumps(o))) for c, o in examples.items()]
    tests.append({'case': 'deterministic_admission_replay', 'passed': replay_a == replay_b,
                  'observed': replay_b, 'expected': replay_a})
    (ROOT / 'examples.json').write_text(json.dumps(examples, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    report = {'probe': 'R006-CONTRACT-SPINE-01', 'synthetic': True, 'selected': False,
              'target_plus': 'NOT_TESTED', 'checks': tests, 'passed': sum(t['passed'] for t in tests),
              'total': len(tests), 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT / 'result-local.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'passed': report['passed'], 'total': report['total']}))
    if report['passed'] != report['total']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
