from pathlib import Path
import os,subprocess
root=Path(__file__).resolve().parents[1]
home=root/'.local/r021-probe-home'
home.mkdir(exist_ok=True)
env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP'}}
env.update(USERPROFILE=str(home),HOME=str(home),EDGAR_LOCAL_DATA_DIR=str(home/'edgar-data'))
process=subprocess.run(['C:/Python314/python.exe',str(root/'planning/research/probes/r021-edgartools-offline/probe_attempt01.py'),str(root/'.local/r021-edgar-deps')],cwd=root,env=env,timeout=35,capture_output=True,text=True)
print('exit_code:',process.returncode)
print(process.stdout)
print('stderr_lines:',len(process.stderr.splitlines()))
