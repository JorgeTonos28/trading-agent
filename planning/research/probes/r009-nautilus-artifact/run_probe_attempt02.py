from pathlib import Path
import os,subprocess,sys
root=Path(__file__).resolve().parents[4];home=root/'.local/qe0-home';home.mkdir(exist_ok=True)
env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP'}};env.update(USERPROFILE=str(home),HOME=str(home))
p=subprocess.run([sys.executable,str(Path(__file__).with_name('probe_attempt02.py'))],cwd=home,env=env,timeout=40,capture_output=True,text=True)
print('process_exit_code',p.returncode);print(p.stdout);print('stderr_lines',len(p.stderr.splitlines()));raise SystemExit(p.returncode)
