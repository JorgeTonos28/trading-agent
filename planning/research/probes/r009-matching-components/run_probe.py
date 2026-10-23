from pathlib import Path
import os, subprocess, sys
here=Path(__file__).resolve().parent;root=here.parents[3]
home=root/'.local/qe2-home';home.mkdir(exist_ok=True)
env={k:v for k,v in os.environ.items() if k.upper() in {'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP'}}
env.update(USERPROFILE=str(home),HOME=str(home))
attempt=sys.argv[1] if len(sys.argv)>1 else '01'
source='probe.py' if attempt=='01' else 'probe_attempt02.py'
p=subprocess.run([sys.executable,str(here/source),attempt],cwd=home,env=env,capture_output=True,text=True,timeout=45)
print('exit_code',p.returncode);print(p.stdout)
if p.returncode: print(p.stderr[-3000:])
else: print('stderr_lines',len(p.stderr.splitlines()))
raise SystemExit(p.returncode)
