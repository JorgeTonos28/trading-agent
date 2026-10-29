from pathlib import Path
import os,subprocess,sys
root=Path(__file__).resolve().parents[1]
home=root/'.local/r020-eval-home'
home.mkdir(exist_ok=True)
env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP'}}
env.update(USERPROFILE=str(home),HOME=str(home))
process=subprocess.run([sys.executable,str(root/'planning/research/probes/r020-evaluation/probe_attempt01.py'),str(root/'.local/r020-eval-deps')],cwd=root,env=env,timeout=40,capture_output=True,text=True)
print('exit_code:',process.returncode)
print(process.stdout)
print('stderr_lines:',len(process.stderr.splitlines()))
