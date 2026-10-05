"""Disposable behavioral benchmark using included native ChatGPT/Codex auth.

Not a broker integration, runtime implementation or delegated agent. Never saves
raw account responses, auth material, stderr, reasoning or internal session IDs.
Only synthetic read_evidence is serviced. Uses jsonschema, not a new validator.
"""
import argparse
import hashlib
import json
import os
import queue
import shutil
import subprocess
import tempfile
import threading
import time
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
CONFIG = {
    "forced_login_method": "chatgpt", "model_provider": "openai",
    "features.shell_tool": False, "features.unified_exec": False,
    "features.multi_agent": False, "features.apps": False,
    "features.skill_mcp_dependency_install": False,
    "web_search": "disabled", "mcp_servers": {}, "plugins": {},
    "history.persistence": "none",
}


def toml_value(v):
    if isinstance(v, dict):
        return "{}"
    return json.dumps(v)


class Server:
    def __init__(self, cwd):
        binary = shutil.which("codex")
        if not binary:
            raise RuntimeError("Codex unavailable")
        command = [binary]
        for key, value in CONFIG.items():
            command.extend(["-c", f"{key}={toml_value(value)}"])
        command.extend(["app-server", "--listen", "stdio://"])
        # Avoid an API-key route even if an unrelated parent tool has one.
        env = {k: v for k, v in os.environ.items()
               if not k.upper().endswith(("API_KEY", "ACCESS_TOKEN"))}
        self.process = subprocess.Popen(
            command, cwd=cwd, env=env, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            encoding="utf-8", errors="replace", bufsize=1,
        )
        self.messages = queue.Queue()
        self.counter = 0
        self.diagnostic_lines = 0
        self.stashed = []

        def reader():
            for line in self.process.stdout:
                try:
                    self.messages.put(json.loads(line))
                except json.JSONDecodeError:
                    self.diagnostic_lines += 1

        def drain():
            for _ in self.process.stderr:
                self.diagnostic_lines += 1

        threading.Thread(target=reader, daemon=True).start()
        threading.Thread(target=drain, daemon=True).start()

    def write(self, message):
        self.process.stdin.write(json.dumps(message) + "\n")
        self.process.stdin.flush()

    def rpc(self, method, params):
        self.counter += 1
        request_id = self.counter
        self.write({"id": request_id, "method": method, "params": params})
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            msg = self.messages.get(timeout=max(.01, deadline - time.monotonic()))
            if msg.get("id") == request_id and "method" not in msg:
                if "error" in msg:
                    raise RuntimeError(f"RPC {method} rejected; code={msg['error'].get('code')}")
                return msg["result"]
            self.stashed.append(msg)
        raise TimeoutError(f"RPC {method} timeout")

    def next(self, timeout):
        if self.stashed:
            return self.stashed.pop(0)
        return self.messages.get(timeout=timeout)

    def close(self):
        try:
            self.process.stdin.close()
            self.process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            self.process.wait(timeout=5)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def skill_for(case):
    if case in ("research", "tool_failure"):
        return ROOT.parent / "r006-idea-generation-sandbox" / "SKILL.md", "r006-research-idea-sandbox"
    names = {"quant": ("quant-review", "r006-quant-review-prototype"),
             "pedagogy": ("pedagogy-trace", "r006-pedagogy-trace-prototype"),
             "shadow": ("shadow-thesis", "r006-shadow-thesis-prototype")}
    directory, name = names[case]
    return ROOT / "skills" / directory / "SKILL.md", name


def run_trial(server, cwd, case, variant, repetition, model, effort, fixture, schema):
    start = time.monotonic()
    entry = {"case": case, "variant": variant, "repetition": repetition,
             "tool_trace": [], "unexpected_tools": [], "output": None,
             "turn_status": "not_started", "schema_errors": [], "usage": None}
    common = (ROOT / "common_contract.txt").read_text(encoding="utf-8")
    tool = {"type": "function", "name": "read_evidence",
            "description": "Read this trial's synthetic as-of evidence bundle. No external access or side effects.",
            "inputSchema": {"type": "object", "properties": {"bundle": {"type": "string"}},
                            "required": ["bundle"], "additionalProperties": False}}
    thread = server.rpc("thread/start", {
        "cwd": str(cwd), "model": model, "modelProvider": "openai",
        "ephemeral": True, "approvalPolicy": "never", "sandbox": "read-only",
        "baseInstructions": common, "developerInstructions": "Synthetic experiment only. No delegation or other tools.",
        "dynamicTools": [tool], "selectedCapabilityRoots": [],
        "allowProviderModelFallback": False,
    })
    if thread.get("modelProvider") != "openai" or thread.get("model") != model:
        raise RuntimeError("Unexpected model/provider; no fallback allowed")
    entry["effective_runtime"] = {"model": thread["model"], "provider": thread["modelProvider"],
                                  "sandbox": thread.get("sandbox"),
                                  "instruction_source_count": len(thread.get("instructionSources", [])),
                                  "disabled_plugin_count": len(thread.get("disabledPluginIds", [])),
                                  "multi_agent_mode": thread.get("multiAgentMode")}
    thread_id = thread["thread"]["id"]
    request = f"Bundle={case}; asof={fixture['data']['asof']}; context_version={fixture['data']['context_version']}. {fixture['task']}"
    inputs = [{"type": "text", "text": request}]
    if variant == "skill":
        path, name = skill_for(case)
        dest = cwd / "skills" / name / "SKILL.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)
        inputs[0]["text"] += f" Apply ${name}."
        inputs.append({"type": "skill", "name": name, "path": str(dest)})
        entry["skill_sha256"] = digest(path)
        entry["skill_bytes"] = path.stat().st_size
    else:
        entry["skill_bytes"] = 0
    entry["request_bytes"] = len(request.encode())
    server.rpc("turn/start", {
        "threadId": thread_id, "input": inputs, "outputSchema": schema,
        "effort": effort, "approvalPolicy": "never",
        "sandboxPolicy": {"type": "readOnly", "networkAccess": False},
    })
    entry["turn_status"] = "started"
    messages = []
    reads = 0
    deadline = time.monotonic() + 210
    while time.monotonic() < deadline:
        try:
            msg = server.next(min(10, max(.01, deadline - time.monotonic())))
        except queue.Empty:
            continue
        method = msg.get("method", "")
        params = msg.get("params") or {}
        if params.get("threadId") not in (None, thread_id):
            continue
        if "id" in msg and method:
            if method == "item/tool/call" and params.get("tool") == "read_evidence":
                reads += 1
                arguments = params.get("arguments")
                if isinstance(arguments, str):
                    try:
                        arguments = json.loads(arguments)
                    except json.JSONDecodeError:
                        arguments = {}
                valid = arguments == {"bundle": case}
                failed = (not valid or reads > 2 or fixture["failure"] == "permanent"
                          or fixture["failure"] == "transient" and reads == 1)
                payload = {"error": "synthetic_read_timeout_or_invalid_request", "retryable": reads < 2} if failed else fixture["data"]
                entry["tool_trace"].append({"tool": "read_evidence", "arguments": arguments,
                                            "attempt": reads, "success": not failed})
                server.write({"id": msg["id"], "result": {
                    "success": not failed,
                    "contentItems": [{"type": "inputText", "text": json.dumps(payload)}],
                }})
            else:
                entry["unexpected_tools"].append({"request_method": method, "tool": params.get("tool", "UNKNOWN")})
                server.write({"id": msg["id"], "error": {"code": -32601, "message": "Forbidden by synthetic probe allowlist"}})
        if method == "item/completed":
            item = params.get("item", {})
            if item.get("type") == "agentMessage":
                messages.append(item.get("text", ""))
            if item.get("type") in ("commandExecution", "mcpToolCall", "collabAgentToolCall"):
                entry["unexpected_tools"].append({"completed_item_type": item["type"]})
        if method == "thread/tokenUsage/updated":
            usage = params.get("tokenUsage", {})
            entry["usage"] = {k: usage.get(k) for k in ("total", "last", "modelContextWindow")}
        if method == "turn/completed":
            entry["turn_status"] = params.get("turn", {}).get("status", "UNKNOWN")
            error = params.get("turn", {}).get("error")
            if error:
                entry["turn_error_kind"] = error.get("codexErrorInfo", "UNKNOWN")
            break
    else:
        server.rpc("turn/interrupt", {"threadId": thread_id, "turnId": params.get("turnId", "")})
        entry["turn_status"] = "timeout"
    # Persist only public synthetic messages; no reasoning/intermediate events.
    final = messages[-1] if messages else ""
    try:
        entry["output"] = json.loads(final)
        entry["schema_errors"] = [e.message for e in Draft202012Validator(schema).iter_errors(entry["output"])]
    except json.JSONDecodeError:
        entry["schema_errors"] = ["No parseable final JSON"]
        # Diagnostics may contain provider/auth data; never persist raw errors.
        if final and entry["turn_status"] == "completed":
            entry["unstructured_synthetic_output"] = final
    entry["duration_seconds"] = round(time.monotonic() - start, 3)
    return entry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    if not 1 <= args.limit <= 20:
        raise ValueError("Fixed maximum 20 research turns")
    fixtures = json.loads((ROOT / "fixtures.json").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "output_schema.json").read_text())
    Draft202012Validator.check_schema(schema)
    report = {"probe": "R006-BEHAVIOR-TEAM-01", "protocol_version": "1",
              "AVAILABLE_IN_TARGET_PLUS": "UNKNOWN", "selected": False,
              "cli_version": subprocess.check_output([shutil.which("codex"), "--version"], text=True).strip(),
              "config_overrides": CONFIG, "fixtures_sha256": digest(ROOT / "fixtures.json"),
              "contract_sha256": digest(ROOT / "common_contract.txt"),
              "schema_sha256": digest(ROOT / "output_schema.json"), "trials": []}
    output = Path(args.output)
    with tempfile.TemporaryDirectory(prefix="r006_behavior_team_") as sandbox:
        server = Server(sandbox)
        try:
            server.rpc("initialize", {"clientInfo": {"name": "r006_behavioral_probe", "version": "1"},
                                      "capabilities": {"experimentalApi": True}})
            server.write({"method": "initialized", "params": {}})
            account = server.rpc("account/read", {"refreshToken": False}).get("account") or {}
            report["account"] = {"type": account.get("type"), "plan_type": account.get("planType")}
            if account.get("type") != "chatgpt" or account.get("planType") != "team":
                raise RuntimeError("Expected native ChatGPT Team; no API/plan fallback authorized")
            del account
            models = server.rpc("model/list", {"includeHidden": False}).get("data", [])
            candidates = [m for m in models if m.get("isDefault")]
            if len(candidates) != 1:
                raise RuntimeError("No unique catalog default; protocol needs explicit revision")
            chosen = candidates[0]
            model = chosen["model"]
            efforts = [x.get("reasoningEffort") for x in chosen.get("supportedReasoningEfforts", [])]
            effort = "medium" if "medium" in efforts else chosen["defaultReasoningEffort"]
            report.update(model=model, effort=effort, environment="CURRENT_RESEARCH_ENVIRONMENT_Team")
            print(json.dumps({"environment": "Team", "model": model, "effort": effort}), flush=True)
            cases = list(fixtures)
            trials = [(case, variant, rep) for rep in (1, 2) for i, case in enumerate(cases)
                      for variant in (("minimal", "skill") if (i + rep) % 2 else ("skill", "minimal"))]
            for number, (case, variant, rep) in enumerate(trials[:args.limit], 1):
                cwd = Path(sandbox) / f"trial-{number}"
                cwd.mkdir()
                entry = run_trial(server, cwd, case, variant, rep, model, effort, fixtures[case], schema)
                report["trials"].append(entry)
                output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
                print(json.dumps({"trial": number, "case": case, "variant": variant,
                                  "status": entry["turn_status"], "schema_errors": len(entry["schema_errors"]),
                                  "reads": len(entry["tool_trace"]), "seconds": entry["duration_seconds"]}), flush=True)
                if entry["turn_status"] != "completed":
                    raise RuntimeError("Noncompleted inference; stop to investigate, no automatic retries")
        finally:
            server.close()
            report["diagnostic_lines_not_persisted"] = server.diagnostic_lines
            report["probe_source_sha256"] = digest(Path(__file__))
            output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
