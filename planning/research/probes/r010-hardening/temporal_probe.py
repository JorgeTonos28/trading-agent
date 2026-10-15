"""H6 standalone Temporal development-server experiment, no worker/models/finance."""
import hashlib,json,os,socket,subprocess,tempfile,time,traceback,shutil
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
DIST=Path(tempfile.gettempdir())/'r010_temporal_191'
EXE=DIST/'source/temporal.exe'
def free_port():
 with socket.socket() as s:s.bind(('127.0.0.1',0));return s.getsockname()[1]
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='\n')
def main():
 attempt=os.environ.get('H6_ATTEMPT','01');output=HERE/f'temporal-attempt-{attempt}.json'
 if output.exists():raise RuntimeError('Attempt immutable')
 asset=DIST/'temporal_cli_1.9.1_windows_amd64.zip'
 report={'probe':'H6_TEMPORAL_DEV_PERSISTENCE','captured_at':datetime.now(timezone.utc).isoformat(),
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'asset_sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),'license':'MIT CLI v1.9.1',
    'scope':'loopback dev server, pending workflow without worker, automatic schedule and persistence; no production or Codex scheduler selection',
    'retrieval_history':['urllib download failed TLS connection reset WinError10054','curl verified TLS first connection timed out, retry succeeded'],
    'checks':{},'commands':[]}
 assert report['asset_sha256']=='babb65844835045c91fb98930fe10b81de28db80c8c609180473d2c0b18c7589'
 scratch=Path(tempfile.mkdtemp(prefix='r010_temporal_dev_')).resolve()
 assert scratch.parent==Path(tempfile.gettempdir()).resolve() and scratch.name.startswith('r010_temporal_dev_')
 env={k:v for k,v in os.environ.items() if k.upper() in ('SYSTEMROOT','WINDIR','SYSTEMDRIVE','PATH','PATHEXT','COMSPEC','TEMP','TMP')}
 flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
 port=free_port();http=free_port();metrics=free_port();proc=None
 server=[str(EXE),'--disable-config-file','--disable-config-env','server','start-dev','--headless','--ip','127.0.0.1',
    '--port',str(port),'--http-port',str(http),'--metrics-port',str(metrics),'--db-filename',str(scratch/'state.db'),
    '--sqlite-pragma','journal_mode=WAL','--sqlite-pragma','synchronous=FULL','--log-level','never']
 common=[str(EXE),'--disable-config-file','--disable-config-env','--address',f'127.0.0.1:{port}',
         '--output','json','--command-timeout','10s']
 def command(args,expected=0):
  p=subprocess.run(common+args,env=env,capture_output=True,text=True,timeout=20,creationflags=flags)
  report['commands'].append({'args':args,'exit_code':p.returncode,'stdout':p.stdout[:16000],'stderr':p.stderr[:3000]})
  save(output,report)
  if expected is not None:assert p.returncode==expected
  return p
 def start():
  p=subprocess.Popen(server,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=flags)
  until=time.monotonic()+35
  while time.monotonic()<until:
   if p.poll() is not None:raise RuntimeError('development server exited')
   try:
    with socket.create_connection(('127.0.0.1',port),timeout=.2):return p
   except OSError:time.sleep(.2)
  p.kill();p.wait();raise TimeoutError('start timeout')
 try:
  report['version']=subprocess.check_output([str(EXE),'--version'],env=env,text=True,creationflags=flags).strip()
  proc=start()
  # Inspect only this spawned PID; no unrelated host/process/network details stored.
  query=f'Get-NetTCPConnection -OwningProcess {proc.pid} -State Listen -ErrorAction Stop | Select-Object LocalAddress,LocalPort | ConvertTo-Json -Compress'
  listeners=subprocess.run(['powershell','-NoProfile','-Command',query],capture_output=True,text=True,timeout=15,creationflags=flags)
  report['listeners']=json.loads(listeners.stdout)
  bindings=report['listeners'] if isinstance(report['listeners'],list) else [report['listeners']]
  report['checks']['listeners_loopback']=bool(bindings) and all(x['LocalAddress'] in ('127.0.0.1','::1') for x in bindings)
  assert report['checks']['listeners_loopback']
  command(['workflow','start','--workflow-id','H6-SYN-JOB','--type','SyntheticReadOnlyNoWorker','--task-queue','H6-no-worker',
           '--input','{"authority":"NONE"}','--execution-timeout','5m','--fail-existing'])
  before=command(['workflow','describe','--workflow-id','H6-SYN-JOB'])
  duplicate=command(['workflow','start','--workflow-id','H6-SYN-JOB','--type','SyntheticReadOnlyNoWorker',
           '--task-queue','H6-no-worker','--execution-timeout','5m','--fail-existing'],None)
  report['checks']['duplicate_start_rejected']=duplicate.returncode!=0
  command(['schedule','create','--schedule-id','H6-SYN-SCHEDULE','--workflow-id','H6-AUTO-JOB',
           '--type','SyntheticReadOnlyNoWorker','--task-queue','H6-no-worker','--interval','5s',
           '--remaining-actions','1','--overlap-policy','BufferAll','--execution-timeout','5m','--catchup-window','10s'])
  time.sleep(6)
  scheduled=command(['schedule','describe','--schedule-id','H6-SYN-SCHEDULE'])
  report['schedule_before_restart']=json.loads(scheduled.stdout)
  report['workflow_before_restart']=json.loads(before.stdout)
  proc.kill();proc.wait(timeout=10);proc=None
  proc=start()
  after=command(['workflow','describe','--workflow-id','H6-SYN-JOB'])
  schedule_after=command(['schedule','describe','--schedule-id','H6-SYN-SCHEDULE'])
  report['workflow_after_restart']=json.loads(after.stdout)
  report['schedule_after_restart']=json.loads(schedule_after.stdout)
  report['checks']['workflow_describable_after_abrupt_restart']=bool(report['workflow_after_restart'])
  report['checks']['schedule_describable_after_restart']=bool(report['schedule_after_restart'])
  # Detailed run/action equality is evaluated separately against native output, without guessing JSON shape.
 except Exception as e:
  report['error_class']=type(e).__name__;report['error_frames']=[{'file':Path(f.filename).name,'line':f.lineno} for f in traceback.extract_tb(e.__traceback__)]
 finally:
  if proc:
   proc.kill();proc.wait(timeout=10)
  try:shutil.rmtree(scratch);report['cleanup']='COMPLETED'
  except Exception as e:report['cleanup']='FAILED_'+type(e).__name__
  report['process_stopped']=proc is None or proc.poll() is not None
  save(output,report)
 print(json.dumps({k:report.get(k) for k in ('version','checks','error_class','cleanup','process_stopped')}))
if __name__=='__main__':main()
