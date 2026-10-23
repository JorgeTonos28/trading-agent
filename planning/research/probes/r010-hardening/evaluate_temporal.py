"""Evaluate immutable H6 native outputs; no additional server or workflow execution."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=HERE/'temporal-attempt-01.json';d=json.loads(p.read_text())
a=d['workflow_before_restart']['workflowExecutionInfo'];b=d['workflow_after_restart']['workflowExecutionInfo']
s=d['schedule_before_restart'];t=d['schedule_after_restart']
duplicate=next(x for x in d['commands'] if x['args'][:2]==['workflow','start'] and x['exit_code']!=0)
checks={'listeners_loopback':d['checks']['listeners_loopback'],
 'duplicate_rejected_with_existing_workflow_error':duplicate['exit_code']!=0 and 'already' in duplicate['stderr'].lower(),
 'same_workflow_and_run_after_crash':a['execution']==b['execution'],
 'same_history_length_after_crash':a['historyLength']==b['historyLength'],
 'pending_no_worker_status_preserved':a['status']==b['status']=='WORKFLOW_EXECUTION_STATUS_RUNNING',
 'automatic_schedule_started_once':s['info']['actionCount']=='1' and len(s['info']['recentActions'])==1,
 'schedule_same_run_after_crash':s['info']['recentActions'][0]['startWorkflowResult']==t['info']['recentActions'][0]['startWorkflowResult'],
 'schedule_count_preserved':t['info']['actionCount']=='1',
 'schedule_bounded_actions':s['schedule']['state']['limitedActions'] is True,
 'own_server_stopped_and_cleaned':d['process_stopped'] and d['cleanup']=='COMPLETED'}
out={'probe':'H6_OUTPUT_EVALUATION','native_result_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'checks':checks,'passed':sum(checks.values()),'total':len(checks),
     'scope':'pending workflow and one schedule action survived development server restart; no worker activity/retry/model or production stack proof'}
(HERE/'temporal-evaluation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'passed':out['passed'],'total':out['total'],'failed':[k for k,v in checks.items() if not v]}))
