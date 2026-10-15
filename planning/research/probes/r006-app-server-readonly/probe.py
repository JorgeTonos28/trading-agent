"""Disposable R-006 protocol probe. No inference, login, broker or paid API call.

Only these RPCs are permitted: initialize/initialized, account/read (no refresh),
skills/list, and process-local skills/extraRoots/set. Raw account replies and
stderr stay in memory and are never persisted or printed.
"""
import argparse
import hashlib
import json
import queue
import shutil
import subprocess
import tempfile
import threading
import time
from pathlib import Path


ALLOWED = {
    "initialize", "initialized", "account/read", "skills/list",
    "skills/extraRoots/set",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    binary = shutil.which("codex")
    if not binary:
        raise RuntimeError("Codex binary unavailable")
    fixture_skill = Path(__file__).resolve().parents[1] / "r006-idea-generation-sandbox"
    report = {
        "probe": "R006-APP-SERVER-READONLY-01",
        "environment": "CURRENT_RESEARCH_ENVIRONMENT",
        "AVAILABLE_IN_TARGET_PLUS": "UNKNOWN",
        "cli_identity_matches_target": "UNKNOWN",
        "cli_version": subprocess.check_output([binary, "--version"], text=True).strip(),
        "inference_turns_started": 0,
        "rpc_methods_sent": [],
        "raw_account_or_token_data_persisted": False,
        "persistent_skill_configuration_written": False,
        "checks": {},
    }
    with tempfile.TemporaryDirectory(prefix="r006_appserver_readonly_") as sandbox:
        task_root = Path(sandbox)
        skill_root = task_root / "skill-roots"
        skill_root.mkdir()
        shutil.copytree(fixture_skill, skill_root / "r006-research-idea-sandbox")
        schema_root = task_root / "schema"
        subprocess.run(
            [binary, "app-server", "generate-json-schema", "--out", str(schema_root)],
            check=True, capture_output=True, text=True, timeout=20,
        )
        schema = json.loads((schema_root / "v2" / "SkillsListParams.json").read_text())
        report["skills_list_schema_fields"] = sorted(schema.get("properties", {}))
        report["skill_sha256"] = hashlib.sha256((fixture_skill / "SKILL.md").read_bytes()).hexdigest()
        report["skills_list_schema_sha256"] = hashlib.sha256(
            (schema_root / "v2" / "SkillsListParams.json").read_bytes()
        ).hexdigest()
        process = subprocess.Popen(
            [binary, "app-server", "--listen", "stdio://"], cwd=task_root,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, encoding="utf-8", errors="replace", bufsize=1,
        )
        replies = queue.Queue()
        diagnostic_count = [0]

        def read_stdout():
            for line in process.stdout:
                try:
                    replies.put(json.loads(line))
                except json.JSONDecodeError:
                    diagnostic_count[0] += 1

        def drain_stderr():
            for _ in process.stderr:
                diagnostic_count[0] += 1

        threading.Thread(target=read_stdout, daemon=True).start()
        threading.Thread(target=drain_stderr, daemon=True).start()

        def send(method, params, request_id=None):
            if method not in ALLOWED:
                raise RuntimeError("RPC outside fixed read-only probe allowlist")
            if method == "account/read" and params.get("refreshToken") is not False:
                raise RuntimeError("Token refresh forbidden")
            report["rpc_methods_sent"].append(method)
            message = {"method": method, "params": params}
            if request_id is not None:
                message["id"] = request_id
            process.stdin.write(json.dumps(message) + "\n")
            process.stdin.flush()
            if request_id is None:
                return None
            deadline = time.monotonic() + 15
            while time.monotonic() < deadline:
                try:
                    reply = replies.get(timeout=max(0.01, deadline - time.monotonic()))
                except queue.Empty:
                    break
                if reply.get("id") == request_id and "method" not in reply:
                    return reply
            raise TimeoutError("Read-only RPC deadline exceeded")

        try:
            before = send("skills/list", {"cwds": [str(task_root)]}, 0)
            report["checks"]["preinitialize_rejected"] = "error" in before
            report["checks"]["preinitialize_error_code"] = before.get("error", {}).get("code")
            init = send("initialize", {
                "clientInfo": {"name": "r006_readonly_probe", "title": "R006 planning probe", "version": "0.1"},
            }, 1)
            report["checks"]["initialize_succeeded"] = "result" in init
            if "result" not in init:
                raise RuntimeError("Initialization rejected")
            send("initialized", {})
            account_reply = send("account/read", {"refreshToken": False}, 2)
            account = account_reply.get("result", {}).get("account") or {}
            report["account_read"] = {
                "succeeded": "result" in account_reply,
                "account_type": account.get("type", "UNKNOWN"),
                "observed_plan_type": account.get("planType", "UNKNOWN"),
            }
            del account_reply, account
            roots_reply = send("skills/extraRoots/set", {"extraRoots": [str(skill_root)]}, 3)
            report["checks"]["process_local_extra_root_accepted"] = "result" in roots_reply
            skills_reply = send("skills/list", {"cwds": [str(task_root)], "forceReload": True}, 4)
            items = skills_reply.get("result", {}).get("data", [])
            found = [skill for item in items for skill in item.get("skills", [])
                     if skill.get("name") == "r006-research-idea-sandbox"]
            report["checks"]["disposable_skill_discovered"] = bool(found)
            report["checks"]["disposable_skill_enabled"] = all(s.get("enabled") is True for s in found) if found else False
            report["checks"]["discovery_error_count"] = sum(len(item.get("errors", [])) for item in items)
            report["behavior_and_authority_tested"] = False
        finally:
            process.stdin.close()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.terminate()
                process.wait(timeout=3)
            report["diagnostic_lines_not_persisted"] = diagnostic_count[0]
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
