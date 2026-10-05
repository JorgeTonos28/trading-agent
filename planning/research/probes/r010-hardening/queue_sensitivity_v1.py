"""Virtual-time sensitivity only; NO live Codex jobs or operational scheduler."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
source=ROOT/'planning/research/probes/r006-team-paper/result-attempt-02.json'
wave=json.loads(source.read_text(encoding='utf-8'))
durations={}
for x in wave['trials']:
 if x['case']!='failure':durations[x['case']]=max(durations.get(x['case'],0),x['service_seconds'])
def run(jobs,multiplier):
 pending=list(jobs);clock=0;done=[]
 while pending:
  ready=[x for x in pending if x['arrival']<=clock]
  if not ready:clock=min(x['arrival'] for x in pending);continue
  x=min(ready,key=lambda x:({'shadow':0,'pedagogy':1,'quant':2,'research':3}[x['role']],x['arrival'],x['id']))
  start=clock;clock+=durations[x['role']]*multiplier;pending.remove(x)
  done.append({**x,'wait_s':round(start-x['arrival'],3),'total_s':round(clock-x['arrival'],3),
              'on_time':clock<=x['arrival']+x['window']})
 return {'multiplier':multiplier,'required':len(jobs),'accounted':len(done),'on_time':sum(x['on_time'] for x in done),'jobs':done}
base=json.loads((HERE/'result.json').read_text())['simulation_runs'][0]['jobs']
regular=[{'id':x['job'],'role':x['role'],'arrival':x['arrival'],'window':120 if x['role']=='shadow' else 600 if x['role']=='pedagogy' else 86400} for x in base]
reserve=regular+[{'id':f'I{i}','role':'research','arrival':i*2100+5,'window':86400} for i in range(10)]
# 13 reserve attempts must also consume queue service, without new financial decisions.
reserve += [{'id':f'RA{i}','role':('shadow','pedagogy','research','quant')[i%4],
             'arrival':i*1700+10,'window':120 if i%4==0 else 600 if i%4==1 else 86400} for i in range(13)]
burst=[{'id':'long-Q','role':'quant','arrival':0,'window':86400},
       {'id':'S1','role':'shadow','arrival':0.1,'window':120},
       {'id':'S2','role':'shadow','arrival':0.1,'window':120},
       {'id':'P1','role':'pedagogy','arrival':0.1,'window':600}]
out={'probe':'H3_QUEUE_SENSITIVITY','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'hypothetical nonpreemptive single worker; roles/service from wave07; virtual timing; no quota or capacity acceptance',
     'wave07_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'assumptions':'10 owner interactions as research cost proxy; 13 reserve attempts illustrative mix, not observed/final; shadow priority among ready only',
     'reserve63':[run(reserve,m) for m in (1,2,4)],'background_then_burst':[run(burst,m) for m in (1,2,4)],
     'checks':{'63_accounted':all(run(reserve,m)['accounted']==63 for m in (1,2,4)),
               'burst_accounted':all(run(burst,m)['accounted']==4 for m in (1,2,4))},
     'interpretation':'Priority cannot preempt in-flight long quant/research. Real isolation/capacity probe needed before selecting concurrency/deadlines.'}
(HERE/'queue-sensitivity.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:[{'multiplier':x['multiplier'],'on_time':x['on_time'],'required':x['required']} for x in out[k]] for k in ('reserve63','background_then_burst')}))
