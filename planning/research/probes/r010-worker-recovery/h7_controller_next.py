"""H7 preregistered disposable worker crash/retry probe, loopback only."""
import asyncio
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import socket
import sqlite3
import subprocess
import sys
import tempfile
import time
import traceback

from temporalio.client import Client
from temporalio.api.enums.v1 import EventType

HERE = Path(__file__).resolve().parent
EXE = Path(tempfile.gettempdir()) / "r010_temporal_191/source/temporal.exe"
WORKER = HERE / "h7_worker.py"
FLAGS = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


async def main():
    attempt = os.environ.get("H7_ATTEMPT", "01")
    output = HERE / f"attempt-{attempt}.json"
    if output.exists():
        raise RuntimeError("Immutable attempt exists")
    scratch = Path(tempfile.mkdtemp(prefix="r010_h7_")).resolve()
    if scratch.parent != Path(tempfile.gettempdir()).resolve() or not scratch.name.startswith("r010_h7_"):
        raise RuntimeError("Unapproved scratch")
    report = {
        "probe": "H7_WORKER_CRASH_RETRY_SYNTHETIC",
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "scope": "TEMP_LOOPBACK_DEV_NO_LLM_NO_FINANCIAL_OR_SECURITY_ACCEPTANCE",
        "sources": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__), WORKER]},
        "versions": {n: importlib.metadata.version(n) for n in ["temporalio", "protobuf", "nexus-rpc"]},
        "sqlite_version": sqlite3.sqlite_version,
        "checks": {},
        "cleanup": "PENDING_EXTERNAL_VERIFIED_POWERSHELL",
        "admin_changes": [],
    }
    scratch_binding = Path(__file__).resolve().parents[4] / ".local/h7-scratch-binding.json"
    scratch_binding.write_text(json.dumps({"absolute_scratch": str(scratch), "prefix": "r010_h7_"}), encoding="utf-8")
    env = {k: v for k, v in os.environ.items()
           if k.upper() in ("SYSTEMROOT", "WINDIR", "SYSTEMDRIVE", "PATH", "PATHEXT", "COMSPEC", "TEMP", "TMP", "PYTHONPATH")}
    p, http, metrics = port(), port(), port()
    address = f"127.0.0.1:{p}"
    env.update(H7_ADDRESS=address, H7_SCRATCH=str(scratch))
    server = worker = None
    try:
        report["versions"]["temporal_cli"] = subprocess.check_output([str(EXE), "--version"], env=env, text=True, creationflags=FLAGS).strip()
        report["temporal_binary_sha256"] = hashlib.sha256(EXE.read_bytes()).hexdigest()
        server = subprocess.Popen(
            [str(EXE), "--disable-config-file", "--disable-config-env", "server", "start-dev", "--headless",
             "--ip", "127.0.0.1", "--port", str(p), "--http-port", str(http), "--metrics-port", str(metrics),
             "--db-filename", str(scratch / "state.db"), "--sqlite-pragma", "journal_mode=WAL",
             "--sqlite-pragma", "synchronous=FULL", "--log-level", "never"],
            env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=FLAGS)
        started = time.monotonic()
        while True:
            if server.poll() is not None or time.monotonic() - started > 30:
                raise RuntimeError("Server unavailable")
            try:
                with socket.create_connection(("127.0.0.1", p), timeout=.2):
                    break
            except OSError:
                await asyncio.sleep(.1)
        query = f"Get-NetTCPConnection -OwningProcess {server.pid} -State Listen | Select-Object -ExpandProperty LocalAddress | ConvertTo-Json -Compress"
        listeners = json.loads(subprocess.check_output(["pwsh", "-NoProfile", "-Command", query], creationflags=FLAGS, text=True, timeout=15, env=env))
        if isinstance(listeners, str): listeners = [listeners]
        report["checks"]["loopback_only"] = bool(listeners) and all(x in ["127.0.0.1", "::1"] for x in listeners)
        assert report["checks"]["loopback_only"]
        client = await Client.connect(address)
        worker = subprocess.Popen([sys.executable, str(WORKER)], env=env, stdout=subprocess.DEVNULL,
                                  stderr=open(scratch / "worker-error-1.txt", "w", encoding="utf-8"), creationflags=FLAGS)
        handle = await client.start_workflow("SyntheticRecoveryWorkflow", {"job_id": "H7-JOB", "authority": "NONE"},
                                            id="H7-JOB", task_queue="H7-SYNTHETIC", execution_timeout=timedelta(seconds=45))
        until = time.monotonic() + 20
        while not (scratch / "entered-1.json").exists():
            if worker.poll() is not None: raise RuntimeError("First worker exited")
            if time.monotonic() > until: raise TimeoutError("Activity did not enter")
            await asyncio.sleep(.1)
        report["checks"]["first_activity_entered"] = True
        worker.kill(); worker.wait(timeout=10); worker = None
        worker = subprocess.Popen([sys.executable, str(WORKER)], env=env, stdout=subprocess.DEVNULL,
                                  stderr=open(scratch / "worker-error-2.txt", "w", encoding="utf-8"), creationflags=FLAGS)
        result = await asyncio.wait_for(handle.result(), timeout=35)
        report["result"] = result
        report["observed_activity_attempts"] = sorted(json.loads(x.read_text(encoding="utf-8"))["attempt"] for x in scratch.glob("entered-*.json"))
        report["checks"]["worker_redelivery_completed"] = result.get("attempt") == 2 and report["observed_activity_attempts"] == [1, 2]
        report["checks"]["no_financial_authority"] = result.get("authority") == "NONE"
        events = [e async for e in handle.fetch_history_events()]
        report["event_types"] = dict(Counter(EventType.Name(e.event_type) for e in events))
        report["checks"]["workflow_closed_and_activity_completed"] = report["event_types"].get("EVENT_TYPE_WORKFLOW_EXECUTION_COMPLETED") == 1 and report["event_types"].get("EVENT_TYPE_ACTIVITY_TASK_COMPLETED") == 1
        db = sqlite3.connect(scratch / "synthetic_receipt.db")
        db.execute("pragma synchronous=FULL")
        db.execute("create table receipts(job text primary key, output text not null)")
        db.execute("insert into receipts values (?,?)", (result["job_id"], json.dumps(result, sort_keys=True))); db.commit()
        duplicate_rejected = False
        try:
            db.execute("insert into receipts values (?,?)", (result["job_id"], json.dumps(result)))
        except sqlite3.IntegrityError:
            db.rollback(); duplicate_rejected = True
        report["checks"]["external_receipt_duplicate_rejected"] = duplicate_rejected and db.execute("select count(*) from receipts").fetchone()[0] == 1
        db.close()
        report["checks"]["bounded_experiment_completed"] = all(report["checks"].values())
    except Exception as error:
        report["error_class"] = type(error).__name__
        report["error_frames"] = [{"file": Path(f.filename).name, "line": f.lineno} for f in traceback.extract_tb(error.__traceback__)]
        # Raw dependency traceback remains private in TEMP; no host paths or secrets exported.
    finally:
        for proc in [worker, server]:
            if proc is not None and proc.poll() is None:
                proc.kill(); proc.wait(timeout=10)
        report["checks"]["own_processes_stopped"] = all(proc is None or proc.poll() is not None for proc in [worker, server])
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"attempt": attempt, "checks": report["checks"], "error_class": report.get("error_class")}))


if __name__ == "__main__":
    asyncio.run(main())
