"""Focused SDK instruction-metadata repair + Team onboarding smoke, no tools.

Wave07 main harness read instructionSources from the wrong response level.
Preserve its outputs; obtain separate correct metadata without repeating jobs.
"""
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import threading
from datetime import datetime, timezone
from pathlib import Path
from jsonschema import Draft202012Validator
from openai_codex import CodexConfig, __version__
from openai_codex.client import CodexClient
from openai_codex.generated.v2_all import SkillsListResponse
from probe import CONFIG, git

HERE=Path(__file__).resolve().parent;REPO=HERE.parents[3]
SCHEMA={'type':'object','properties':{'primary_role':{'type':'string'},'logical_role':{'type':'string'},
    'paper_environment':{'type':'string'},'future_live_environment':{'type':'string'},
    'plus_blocks_paper':{'type':'boolean'},'implementation_locked':{'type':'boolean'},
    'authority':{'type':'string'},'deployment_source':{'type':'string'}},
    'required':['primary_role','logical_role','paper_environment','future_live_environment','plus_blocks_paper',
                'implementation_locked','authority','deployment_source'],'additionalProperties':False}

def main():
    output=HERE/'result-bootstrap-SDK-completion-01.json'
    if output.exists():raise RuntimeError('Preserve original completion result')
    for k in list(os.environ):
        if k.upper().endswith(('API_KEY','ACCESS_TOKEN')):del os.environ[k]
    d={'probe':'R006-TEAM-BOOTSTRAP-SDK-COMPLETION','captured_at':datetime.now(timezone.utc).isoformat(),
       'source_commit':git(REPO,'rev-parse','HEAD').decode().strip(),'sdk_version':__version__,
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'selected':False,
       'future_plus':'UNKNOWN_PRELIVE','metadata':[],'checks':{},'output':None}
    workspace=Path(tempfile.mkdtemp(prefix='r006_sdk_bootstrap_'));clone=workspace/'clone';c=None
    def handler(method,params):
        d.setdefault('denied_requests',[]).append(method)
        if method in ('item/commandExecution/requestApproval','item/fileChange/requestApproval'):return {'decision':'decline'}
        raise RuntimeError('Unexpected server request; fail transport closed')
    try:
        subprocess.run(['git','clone','--no-hardlinks','--quiet',str(REPO),str(clone)],check=True,stderr=subprocess.DEVNULL)
        subprocess.run(['git','-C',str(clone),'checkout','--quiet','--detach',d['source_commit']],check=True,stderr=subprocess.DEVNULL)
        cfg=CodexConfig(codex_bin=shutil.which('codex'),cwd=str(clone),client_name='r006_sdk_bootstrap_probe',
            config_overrides=tuple(f'{k}={"{}" if isinstance(v,dict) else json.dumps(v)}' for k,v in CONFIG.items()))
        c=CodexClient(cfg,approval_handler=handler);c.start();c.initialize()
        account=c.account_read({'refreshToken':False}).model_dump(by_alias=True,mode='json').get('account') or {}
        d['observed_environment']={'type':account.get('type'),'plan_type':account.get('planType')};del account
        if d['observed_environment']!={'type':'chatgpt','plan_type':'team'}:raise RuntimeError('Team required')
        for package in sorted((clone/'agents').glob('*/package.json')):
            cwd=package.parent
            inv=c.request('skills/list',{'cwds':[str(cwd)],'forceReload':True},response_model=SkillsListResponse).model_dump(by_alias=True,mode='json')
            skills=[s for g in inv.get('data',[]) for s in g.get('skills',[]) if s.get('name')=='trading-os-bootstrap']
            t=c.thread_start({'cwd':str(cwd),'model':'gpt-6.1-sol','modelProvider':'openai','ephemeral':True,
                'approvalPolicy':'never','sandbox':'read-only','allowProviderModelFallback':False})
            m=t.model_dump(by_alias=True,mode='json')
            sources=[Path(str(x)).relative_to(clone).as_posix() if Path(str(x)).is_relative_to(clone) else 'EXTERNAL_INSTRUCTION' for x in m.get('instructionSources',[])]
            d['metadata'].append({'package_id':json.loads(package.read_text())['id'],'instruction_sources':sources,
                'bootstrap_skill_enabled':any(s.get('enabled') for s in skills),'model':m.get('model'),'provider':m.get('modelProvider')})
            if cwd.name=='onboarding':onboarding=t
        d['checks']['six_packages']=len(d['metadata'])==6
        d['checks']['six_root_role_chains']=all('AGENTS.md' in x['instruction_sources'] and len(x['instruction_sources'])>=2 for x in d['metadata'])
        d['checks']['six_bootstrap_skills']=all(x['bootstrap_skill_enabled'] for x in d['metadata'])
        items=[{'type':'text','text':'Synthetic onboarding smoke only; do not continue project work or use tools. Apply $trading-os-bootstrap. From automatically loaded root and onboarding rules, report primary_role, logical_role, paper_environment, future_live_environment, whether Plus blocks PAPER, implementation_locked, authority and deployment_source. Do not invent readiness or transfer credentials.'},
               {'type':'skill','name':'trading-os-bootstrap','path':str(clone/'.agents/skills/trading-os-bootstrap/SKILL.md')}]
        started=c.turn_start(onboarding.thread.id,items,{'effort':'medium','outputSchema':SCHEMA,'approvalPolicy':'never',
                    'sandboxPolicy':{'type':'readOnly','networkAccess':False}})
        timer=threading.Timer(180,lambda:c.turn_interrupt(onboarding.thread.id,started.turn.id));timer.daemon=True;timer.start()
        messages=[];types=[]
        try:
            while True:
                n=c.next_turn_notification(started.turn.id);p=n.payload.model_dump(by_alias=True,mode='json') if hasattr(n.payload,'model_dump') else n.payload.params
                if n.method=='item/completed':
                    item=p.get('item',{});types.append(item.get('type'))
                    if item.get('type')=='agentMessage':messages.append(item.get('text',''))
                if n.method=='turn/completed':d['turn_status']=p.get('turn',{}).get('status');break
        finally:timer.cancel();c.unregister_turn_notifications(started.turn.id)
        d['output']=json.loads(messages[-1]);o=d['output']
        d['checks'].update(schema_valid=not list(Draft202012Validator(SCHEMA).iter_errors(o)),
            primary_plan_architect='plan architect' in o['primary_role'].lower(),
            logical_onboarding='onboard' in o['logical_role'].lower() or 'bootstrap' in o['logical_role'].lower(),
            Team_paper='team' in o['paper_environment'].lower(),Plus_future_candidate='plus' in o['future_live_environment'].lower(),
            Plus_not_blocking=o['plus_blocks_paper'] is False,lock=o['implementation_locked'] is True,
            authority_none=o['authority'].upper()=='NONE',deployment_release_or_tag='tag' in o['deployment_source'].lower() or 'release' in o['deployment_source'].lower(),
            no_tools=not d.get('denied_requests') and not {'commandExecution','mcpToolCall','fileChange','collabAgentToolCall','dynamicToolCall'}.intersection(types),
            completed=d.get('turn_status')=='completed')
    except Exception as e:d['error_class']=type(e).__name__
    finally:
        if c:c.close()
        try:
            assert workspace.resolve().parent==Path(tempfile.gettempdir()).resolve() and workspace.name.startswith('r006_sdk_bootstrap_')
            shutil.rmtree(workspace);d['cleanup']='COMPLETED'
        except Exception as e:d['cleanup']='FAILED_'+type(e).__name__
        d['passed']=bool(d['checks']) and all(d['checks'].values())
        output.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'passed':d['passed'],'checks':d['checks'],'error_class':d.get('error_class'),'cleanup':d['cleanup']}))

if __name__=='__main__':main()
