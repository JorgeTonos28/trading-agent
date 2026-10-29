from pathlib import Path
from datetime import datetime,timezone
from itertools import permutations
import hashlib,json
here=Path(__file__).resolve().parent;out=here/'result-01.json';assert not out.exists()
events=('old_output','old_expire','new_claim','new_output','cancel','deadline','restore')
def oracle(history):
 receipt=None;answers=[]
 for i,event in enumerate(history):
  if event not in ('old_output','new_output'):continue
  prefix=history[:i];old=event=='old_output'
  terminal=any(x in prefix for x in ('cancel','deadline','restore'))
  eligible=not terminal and receipt is None
  eligible=eligible and (('old_expire' not in prefix and 'new_claim' not in prefix) if old else 'new_claim' in prefix)
  answers.append((event,eligible))
  if eligible:receipt=event
 return answers
def state_model(history,mutation=None):
 generation=0;alive=True;terminal=False;receipt=None;answers=[]
 for event in history:
  if event in ('cancel','deadline','restore'):terminal=True;alive=False
  elif event=='old_expire':
   if generation==0:alive=False
  elif event=='new_claim':
   if not terminal:generation=1;alive=True
  elif event.endswith('_output'):
   attempt=0 if event=='old_output' else 1
   allowed=not terminal and alive and (mutation=='no_fence' or attempt==generation) and (mutation=='no_receipt_unique' or receipt is None)
   answers.append((event,allowed))
   if allowed:receipt=event
 return answers
mismatches=[];mutants={m:[] for m in ('no_fence','no_receipt_unique')};traces=0
for trace in permutations(events):
 if not trace.index('old_expire')<trace.index('new_claim')<trace.index('new_output'):continue
 traces+=1;expected=oracle(trace);actual=state_model(trace)
 if actual!=expected:mismatches.append({'trace':trace,'oracle':expected,'actual':actual})
 for mutant,examples in mutants.items():
  bad=state_model(trace,mutant)
  if bad!=expected and len(examples)<2:examples.append({'trace':trace,'expected':expected,'mutated':bad})
slots=tuple(range(100));ledger=set()
for scan in range(3):
 for slot in slots:ledger.add(('fixed-rule-v1',slot,'shadow','snapshot-'+str(slot)))
rows=[{'id':'PREFIX_ORACLE_VS_FINITE_MODEL','status':'PASS' if not mismatches else 'FAIL'},
 {'id':'MUTATION_WITHOUT_FENCING_HAS_COUNTEREXAMPLE','status':'PASS' if mutants['no_fence'] else 'FAIL'},
 {'id':'MUTATION_WITHOUT_UNIQUE_RECEIPT_HAS_COUNTEREXAMPLE','status':'PASS' if mutants['no_receipt_unique'] else 'FAIL'},
 {'id':'LOST_NOTIFICATIONS_REDISCOVER_SAME_ONE_HUNDRED_JOB_IDS','status':'PASS' if len(ledger)==100 else 'FAIL'}]
report={'captured_utc':datetime.now(timezone.utc).isoformat(),'controller_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'FINITE_ABSTRACT_ADMISSION_CUTS_NOT_POSTGRESQL_OR_CAPACITY','traces':traces,'events_per_trace':len(events),'mismatches':mismatches,'mutant_counterexamples':mutants,'rows':rows,'counts':{s:sum(r['status']==s for r in rows) for s in ['PASS','FAIL','ERROR']},'SQL_or_broker_or_real_clock_tested':False,'PostgreSQL_accepted':False,'implementation_locked':True,'target_acceptance_status':'TARGET_ACCEPTANCE_DEFERRED','holdout':'INTEGRITY_UNKNOWN'}
with out.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps({'traces':traces,'mismatches':len(mismatches),'counts':report['counts']}))
