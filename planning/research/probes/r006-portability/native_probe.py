"""Disposable R-028 native instruction/Skill discovery probe; not a bootstrap installer.

Reuses R-006 transport, existing native Team login and readonly configuration.
Creates fixture roots in TEMP; persists only synthetic outputs and sanitized inventory.
"""
import argparse
import hashlib
import importlib.util
import json
import queue
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("r006_transport", HERE.parent / "r006-behavioral-team" / "probe.py")
transport = importlib.util.module_from_spec(spec)
spec.loader.exec_module(transport)

SCHEMA = {"type": "object", "properties": {
    "global_marker": {"type": "string"}, "role_marker": {"type": "string"},
    "skill_marker": {"type": "string"}, "authority": {"type": "string"}},
    "required": ["global_marker", "role_marker", "skill_marker", "authority"],
    "additionalProperties": False}


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def mk_skill(path, name, marker):
    write(path / "SKILL.md", f"---\nname: {name}\ndescription: Report a synthetic R028 marker when explicitly requested in a portability experiment.\n---\nWhen used, set skill_marker to {marker}. No tools or side effects.\n")


def source_names(sources, root):
    names = []
    for source in sources:
        if isinstance(source, str):
            try:
                names.append(Path(source).relative_to(root).as_posix())
            except ValueError:
                names.append("EXTERNAL_INSTRUCTION_SOURCE")
        elif isinstance(source, dict):
            path = source.get("path") or source.get("filePath")
            if path:
                try:
                    names.append(Path(path).relative_to(root).as_posix())
                except ValueError:
                    names.append("EXTERNAL_INSTRUCTION_SOURCE")
            else:
                names.append({"metadata_keys": sorted(source), "type": source.get("type")})
        else:
            names.append("UNPARSED_SOURCE_METADATA")
    return names


def turn(server, cwd, root, model, case, skill=None):
    thread = server.rpc("thread/start", {"cwd": str(cwd), "model": model,
        "modelProvider": "openai", "ephemeral": True, "approvalPolicy": "never",
        "sandbox": "read-only", "allowProviderModelFallback": False})
    # Deliberately no baseInstructions/developerInstructions: test native automatic loading.
    thread_id = thread["thread"]["id"]
    text = "Report global_marker, role_marker, skill_marker and authority from the automatically loaded R028 instructions. For missing markers use NONE. Use no tools. Do not infer markers from directory names."
    inputs = [{"type": "text", "text": text}]
    if skill:
        inputs[0]["text"] += f" Apply ${skill['name']} and report its body marker."
        inputs.append({"type": "skill", "name": skill["name"], "path": skill["path"]})
    started = time.monotonic()
    response = server.rpc("turn/start", {"threadId": thread_id, "input": inputs,
        "outputSchema": SCHEMA, "effort": "medium", "approvalPolicy": "never",
        "sandboxPolicy": {"type": "readOnly", "networkAccess": False}})
    turn_id = (response.get("turn") or {}).get("id")
    output = None
    items = {}
    requests = 0
    status = "TIMEOUT"
    while time.monotonic() - started < 180:
        try:
            msg = server.next(5)
        except queue.Empty:
            continue
        params = msg.get("params") or {}
        if params.get("threadId") not in (None, thread_id):
            continue
        method = msg.get("method", "")
        if "id" in msg and method:
            requests += 1
            server.write({"id": msg["id"], "error": {"code": -32601, "message": "No tools authorized in this experiment"}})
        if method == "item/completed":
            item = params.get("item") or {}
            kind = item.get("type", "UNKNOWN")
            items[kind] = items.get(kind, 0) + 1
            if kind == "agentMessage":
                try:
                    candidate = json.loads(item.get("text", ""))
                    if isinstance(candidate, dict) and set(candidate) == set(SCHEMA["required"]):
                        output = candidate
                except json.JSONDecodeError:
                    pass
        if method == "turn/completed":
            status = (params.get("turn") or {}).get("status", "UNKNOWN")
            break
    if status == "TIMEOUT" and turn_id:
        server.rpc("turn/interrupt", {"threadId": thread_id, "turnId": turn_id})
    return {"case": case, "cwd": cwd.relative_to(root).as_posix(),
            "instruction_sources": source_names(thread.get("instructionSources", []), root),
            "output": output, "status": status, "seconds": round(time.monotonic()-started,3),
            "item_types": items, "tool_requests": requests}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--metadata-only", action="store_true")
    args = parser.parse_args()
    dest = Path(args.output)
    if dest.exists():
        raise RuntimeError("Preserve prior attempt; use a new output path")
    report = {"probe": "R028_NATIVE_DISCOVERY_01", "target_plus": "UNKNOWN",
              "selected": False, "config": transport.CONFIG, "trials": [], "inventories": []}
    with tempfile.TemporaryDirectory(prefix="r028_fixture_") as temp:
        root = Path(temp)
        repo = root / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "--quiet", str(repo)], check=True, capture_output=True)
        write(repo / "AGENTS.md", "# R028 global synthetic contract\nSet global_marker to R028-ROOT-91, role_marker to NONE unless a local role specializes it, skill_marker to NONE unless a requested Skill sets it, and authority to NONE. This is preparation only; no financial authority, tools or side effects.\n")
        research = repo / "agents" / "research"
        shadow = repo / "agents" / "shadow"
        write(research / "AGENTS.md", "# R028 specialized research\nSet role_marker to R028-RESEARCH-42. Preserve the global preparation and authority constraints.\n")
        write(shadow / "AGENTS.md", "# R028 specialized shadow\nSet role_marker to R028-SHADOW-73. Preserve the global preparation and authority constraints.\n")
        isolated = root / "isolated-shadow"
        write(isolated / "AGENTS.md", (shadow / "AGENTS.md").read_text())
        mk_skill(repo / ".agents" / "skills" / "r028-common", "r028-common", "R028-COMMON-55")
        mk_skill(research / ".agents" / "skills" / "r028-local", "r028-local", "R028-LOCAL-68")
        mk_skill(repo / "shared" / "skills" / "r028-undiscovered", "r028-undiscovered", "R028-OTHER-82")
        server = transport.Server(repo)
        try:
            server.rpc("initialize", {"clientInfo": {"name": "r028_portability_probe", "version": "1"}, "capabilities": {"experimentalApi": True}})
            server.write({"method": "initialized", "params": {}})
            authenticated = False
            try:
                if args.metadata_only:
                    raise RuntimeError("Metadata-only: do not retry account access")
                account = server.rpc("account/read", {"refreshToken": False}).get("account") or {}
                report["account"] = {"type": account.get("type"), "plan_type": account.get("planType")}
                authenticated = report["account"] == {"type": "chatgpt", "plan_type": "team"}
                del account
            except RuntimeError:
                report["account"] = {"type": "UNKNOWN", "plan_type": "UNKNOWN", "status": "RPC_READ_FAILED"}
            report["inference_authorized_by_environment_check"] = authenticated
            report["cli_version"] = subprocess.check_output([shutil.which("codex"), "--version"], text=True).strip()
            model = "gpt-6.1-sol"
            report["model"] = model
            server.rpc("skills/extraRoots/set", {"extraRoots": []})
            for case, cwd in [("root",repo), ("research",research), ("shadow",shadow), ("isolated",isolated)]:
                inv = server.rpc("skills/list", {"cwds": [str(cwd)], "forceReload": True})
                skills = [s for d in inv.get("data", []) for s in d.get("skills", []) if s.get("name", "").startswith("r028-")]
                report["inventories"].append({"case": case, "skills": [{"name": s["name"], "enabled": s.get("enabled"), "scope": s.get("scope")} for s in skills]})
                requested = next((s for s in skills if s["name"] == "r028-local"), None) if case == "research" else None
                if authenticated:
                    trial = turn(server, cwd, root, model, case, requested)
                else:
                    thread = server.rpc("thread/start", {"cwd": str(cwd), "model": model,
                        "modelProvider": "openai", "ephemeral": True, "approvalPolicy": "never",
                        "sandbox": "read-only", "allowProviderModelFallback": False})
                    trial = {"case": case, "cwd": cwd.relative_to(root).as_posix(),
                        "instruction_sources": source_names(thread.get("instructionSources", []), root),
                        "output": None, "status": "METADATA_ONLY_NO_INFERENCE",
                        "instruction_source_keys": [sorted(s) for s in thread.get("instructionSources", []) if isinstance(s,dict)]}
                report["trials"].append(trial)
                dest.write_text(json.dumps(report,indent=2)+"\n")
                print(json.dumps({"case":case,"status":trial["status"],"output":trial["output"],"skills":[s["name"] for s in skills]}),flush=True)
                if trial["status"] not in ("completed", "METADATA_ONLY_NO_INFERENCE"):
                    break
            if all(t["status"] in ("completed", "METADATA_ONLY_NO_INFERENCE") for t in report["trials"]) and len(report["trials"]) == 4:
                write(shadow / "AGENTS.override.md", "# R028 override test\nSet role_marker to R028-OVERRIDE-19. Preserve global constraints.\n")
                if authenticated:
                    trial = turn(server, shadow, root, model, "override")
                else:
                    thread = server.rpc("thread/start", {"cwd": str(shadow), "model": model,
                        "modelProvider": "openai", "ephemeral": True, "approvalPolicy": "never",
                        "sandbox": "read-only", "allowProviderModelFallback": False})
                    trial = {"case": "override", "cwd": shadow.relative_to(root).as_posix(),
                        "instruction_sources": source_names(thread.get("instructionSources", []), root),
                        "output": None, "status": "METADATA_ONLY_NO_INFERENCE"}
                report["trials"].append(trial)
                print(json.dumps({"case":"override","status":trial["status"],"output":trial["output"]}),flush=True)
        except Exception as error:
            report["error_type"] = type(error).__name__
            raise
        finally:
            server.close()
            report["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
            dest.write_text(json.dumps(report,indent=2)+"\n")


if __name__ == "__main__":
    main()
