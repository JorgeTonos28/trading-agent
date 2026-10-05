"""H4 disposable paired public SDK/CLI probe; synthetic evidence, native Team login."""
import hashlib,importlib.util,json,os,shutil,subprocess,tempfile,threading,time,traceback
from pathlib import Path
from datetime import datetime,timezone
from openai_codex import CodexConfig,__version__
from openai_codex.client import CodexClient,_resolve_codex_bin
from openai_codex.generated.v2_all import SkillsListResponse
from jsonschema import Draft202012Validator
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
original=HERE.parent/'r006-team-paper/probe.py'
spec=importlib.util.spec_from_file_location('wave07_reuse',original)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def main():
 attempt=os.environ.get('H4_ATTEMPT','01');output=HERE/f'stable-sdk-attempt-{attempt}.json'
 if output.exists():raise RuntimeError('Attempt immutable')
 for k in list(os.environ):
  if k.upper().endswith(('API_KEY','ACCESS_TOKEN')):del os.environ[k]
 wheel=Path(tempfile.gettempdir())/'r010_cli_0160/openai_codex_cli_bin-0.160.0-py3-none-win_amd64.whl'
 report={'probe':'H4_STABLE_PAIRED_SDK_CLI','captured_at':datetime.now(timezone.utc).isoformat(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'reused_harness_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'sdk':__version__,
         'wheel_sha256':hashlib.sha256(wheel.read_bytes()).hexdigest(),'wheel_size':wheel.stat().st_size,
         'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
         'scope':'two focused Skill/tool regression jobs; no sustained workload, broker, OS isolation or final version selection',
         'trials':[],'unexpected_requests':[],'config_overrides':old.CONFIG}
 assert report['wheel_sha256']=='a1245cc0c7d390d22af4920d512ceae8519dee2cf51d8eec56f3899861a8160a'
 scratch=Path(tempfile.mkdtemp(prefix='r010_stable_sdk_')).resolve();client=None;state={}
 def handler(method,params):
  params=params or {}
  if method=='item/tool/call' and params.get('tool')=='read_evidence':
   args=params.get('arguments')
   if isinstance(args,str):args=json.loads(args)
   state['reads']+=1;ok=args=={'bundle':state['case']} and state['reads']<=2
   state['tools'].append({'tool':'read_evidence','args':args,'allowed':ok})
   return {'success':ok,'contentItems':[{'type':'inputText','text':json.dumps(state['fixture']['data'] if ok else {'error':'DENIED'})}]}
  report['unexpected_requests'].append({'method':method,'tool':params.get('tool')})
  if method in ('item/commandExecution/requestApproval','item/fileChange/requestApproval'):return {'decision':'decline'}
  if method=='item/permissions/requestApproval':return {'permissions':{},'scope':'turn'}
  if method=='mcpServer/elicitation/request':return {'action':'decline','content':None}
  raise RuntimeError('Unknown request denied; no default-accept')
 try:
  clone=scratch/'clone';subprocess.run(['git','clone','--quiet','--no-hardlinks',str(ROOT),str(clone)],check=True,stderr=subprocess.DEVNULL)
  cfg=CodexConfig(cwd=str(clone),client_name='r010_paired_sdk_probe',config_overrides=tuple(f'{k}={"{}" if isinstance(v,dict) else json.dumps(v)}' for k,v in old.CONFIG.items()))
  binary=_resolve_codex_bin(cfg)
  report['default_bundled_resolver']=cfg.codex_bin is None and 'r010_cli_0160' in str(binary)
  report['cli']=subprocess.check_output([str(binary),'--version'],text=True).strip()
  assert report['default_bundled_resolver'] and report['cli']=='codex-cli 0.160.0'
  client=CodexClient(cfg,approval_handler=handler);client.start();client.initialize()
  account=client.account_read({'refreshToken':False}).model_dump(by_alias=True,mode='json').get('account') or {}
  report['account']={'type':account.get('type'),'plan':account.get('planType')}
  assert report['account']=={'type':'chatgpt','plan':'team'};del account
  for case in ('research','shadow'):
   cwd=clone/'agents'/old.PACKAGES[case];skill=cwd/'.agents/skills'/f'r006-contract-{case}'/'SKILL.md'
   skill.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(old.SPINE/'skills'/case/'SKILL.md',skill)
   fixture=old.make_payload(case);old.spine.FIXTURES[case]=fixture
   state.clear();state.update(case=case,fixture=fixture,reads=0,tools=[])
   inventory=client.request('skills/list',{'cwds':[str(cwd)],'forceReload':True},response_model=SkillsListResponse).model_dump(by_alias=True,mode='json')
   discovered=any(s.get('enabled') and s['name']==f'r006-contract-{case}' for g in inventory.get('data',[]) for s in g.get('skills',[]))
   assert discovered
   tool={'type':'function','name':'read_evidence','description':'Read fixed synthetic snapshot, no financial interfaces',
         'inputSchema':{'type':'object','properties':{'bundle':{'type':'string'}},'required':['bundle'],'additionalProperties':False}}
   thread=client.thread_start({'cwd':str(cwd),'model':'gpt-6.1-sol','modelProvider':'openai','ephemeral':True,
            'approvalPolicy':'never','sandbox':'read-only','dynamicTools':[tool],'allowProviderModelFallback':False})
   metadata=thread.model_dump(by_alias=True,mode='json')
   trial={'case':case,'status':'NOT_STARTED','output':None,'skill_discovered':discovered,
          'instruction_sources':[str(x).replace(str(clone),'REPO') for x in metadata.get('instructionSources',[])],
          'effective_model':metadata.get('model'),'provider':metadata.get('modelProvider')}
   report['trials'].append(trial);save(output,report)
   assert trial['effective_model']=='gpt-6.1-sol' and trial['provider']=='openai'
   schema=json.loads((old.SPINE/'schemas'/f"{fixture['role']}.json").read_text())
   text=(old.SPINE/'common_contract.txt').read_text()+f' trusted_role={fixture["role"]}; bundle={case}. '+fixture['task']+f' Apply $r006-contract-{case}. Only spine sources are factual; representative_context is background. Read read_evidence before answering.'
   start=time.monotonic()
   turn=client.turn_start(thread.thread.id,[{'type':'text','text':text},{'type':'skill','name':f'r006-contract-{case}','path':str(skill)}],
          {'effort':'medium','outputSchema':schema,'approvalPolicy':'never','sandboxPolicy':{'type':'readOnly','networkAccess':False}})
   timer=threading.Timer(180,lambda:client.turn_interrupt(thread.thread.id,turn.turn.id));timer.daemon=True;timer.start()
   messages=[];items=[]
   try:
    while True:
     n=client.next_turn_notification(turn.turn.id);payload=n.payload
     p=payload.model_dump(by_alias=True,mode='json') if hasattr(payload,'model_dump') else n.params or {}
     if n.method=='item/completed':
      item=p.get('item',{});items.append(item.get('type'))
      if item.get('type')=='agentMessage':messages.append(item.get('text',''))
     if n.method=='turn/completed':trial['status']=p.get('turn',{}).get('status');break
   finally:timer.cancel()
   trial['service_s']=round(time.monotonic()-start,3);trial['output']=json.loads(messages[-1]) if messages else None
   trial['tool_trace']=state['tools'];trial['item_types']=items
   trial['admission']=old.spine.admit(case,trial['output']) if trial['output'] else 'NO_OUTPUT'
   trial['checks']={'completed':trial['status']=='completed','schema':not list(Draft202012Validator(schema).iter_errors(trial['output'])),
          'admitted':trial['admission']=='ACCEPTED','skill_marker':trial['output']['procedure_marker']==old.MARKERS[case],
          'tool_allowlist':1<=state['reads']<=2 and all(x['allowed'] for x in state['tools']),
          'no_forbidden_items':not {'commandExecution','fileChange','mcpToolCall','collabAgentToolCall'}.intersection(items),
          'no_unexpected_request':not report['unexpected_requests']}
   trial['passed']=all(trial['checks'].values());save(output,report)
   print(json.dumps({'case':case,'passed':trial['passed'],'service_s':trial['service_s']}),flush=True)
 except Exception as error:
  report['error_class']=type(error).__name__;report['error_frames']=[{'file':Path(f.filename).name,'line':f.lineno} for f in traceback.extract_tb(error.__traceback__)]
 finally:
  if client:client.close()
  try:
   assert scratch.parent==Path(tempfile.gettempdir()).resolve() and scratch.name.startswith('r010_stable_sdk_')
   shutil.rmtree(scratch);report['cleanup']='COMPLETED'
  except Exception as error:report['cleanup']='FAILED_'+type(error).__name__
  report['accounting']={'required':2,'recorded':len(report['trials']),'passed':sum(t.get('passed',False) for t in report['trials'])}
  save(output,report)
 print(json.dumps({'accounting':report['accounting'],'error_class':report.get('error_class'),'cli':report.get('cli'),'cleanup':report['cleanup']}))
if __name__=='__main__':main()
