"""Disposable official MCP SDK probe: local synthetic stdio, no AI inference.

Predeclared checks: read-only tool listing, same fixture bytes/clocks after fresh
process restart, unknown order tool rejected, malformed bundle rejected, read
failure surfaced. No broker, production connector, credential or entitlement.
"""
import argparse
import asyncio
import hashlib
import importlib.metadata
import json
import os
import sys
from pathlib import Path

# pip --target on Windows does not activate pywin32 .pth files automatically.
dep = Path(os.environ["TEMP"]) / "r006-mcpdeps"
for extra in (dep, dep / "win32", dep / "win32/lib", dep / "pywin32_system32"):
    sys.path.insert(0, str(extra))
os.environ["PATH"] = str(dep / "pywin32_system32") + os.pathsep + os.environ["PATH"]
if hasattr(os, "add_dll_directory"):
    dll_handle = os.add_dll_directory(str(dep / "pywin32_system32"))

from mcp import Client, StdioServerParameters, types
from mcp.server import MCPServer

ROOT = Path(__file__).resolve().parent


def server():
    service = MCPServer("r006-disposable-synthetic-readonly")

    @service.tool(annotations=types.ToolAnnotations(
        read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False))
    def read_evidence(bundle: str) -> dict:
        """Return a synthetic fixture; never orders or external data."""
        fixtures = json.loads((ROOT / "fixtures.json").read_text(encoding="utf-8"))
        if bundle not in fixtures:
            raise ValueError("Unknown synthetic bundle")
        if bundle == "tool_failure":
            raise RuntimeError("Synthetic permanent read timeout")
        return fixtures[bundle]["data"]

    service.run(transport="stdio")


async def probe(output):
    parameters = StdioServerParameters(command=sys.executable, args=[str(Path(__file__).resolve()), "--server"],
                                      env={"PYTHONPATH": os.pathsep.join(sys.path[:4]), "PATH": os.environ["PATH"]})
    report = {"probe": "R006-MCP-LOCAL-01", "sdk": "official modelcontextprotocol/python-sdk",
              "sdk_version": importlib.metadata.version("mcp"), "license": "MIT",
              "transport": "stdio", "model_inference": False,
              "target_Plus_host_integration": "UNKNOWN", "SELECTED": False,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "checks": {}, "warnings": ["Tool annotations are hints, not access-control enforcement.",
                "Mock restart is not runtime/authentication/position recovery.",
                "SDK pip-target Windows initially required explicit pywin32 path activation."]}
    payloads = []
    for repetition in (1, 2):
        async with Client(parameters, read_timeout_seconds=20) as client:
            listed = await client.list_tools()
            tool_list = listed.tools if hasattr(listed, "tools") else listed
            names = [t.name for t in tool_list]
            report["checks"][f"only_read_tool_{repetition}"] = names == ["read_evidence"]
            annotations = tool_list[0].annotations
            report["checks"][f"readonly_annotation_{repetition}"] = annotations.read_only_hint is True
            read = await client.call_tool("read_evidence", {"bundle": "research"})
            # Store synthetic payload only; no protocol/session identifiers.
            payload = read.structured_content
            payloads.append(payload)
            report["checks"][f"read_success_{repetition}"] = not read.is_error
            for label, name, arguments in (
                ("unknown_order_rejected", "place_order", {"symbol": "SYN-A", "quantity": 50}),
                ("invalid_bundle_rejected", "read_evidence", {"bundle": "missing"}),
                ("read_failure_surfaced", "read_evidence", {"bundle": "tool_failure"}),
            ):
                result = await client.call_tool(name, arguments)
                report["checks"][f"{label}_{repetition}"] = result.is_error
    report["checks"]["identical_data_after_mock_restart"] = payloads[0] == payloads[1]
    report["fixture_payload"] = payloads[0]
    report["all_checks_pass"] = all(report["checks"].values())
    Path(output).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"sdk_version": report["sdk_version"], "checks": report["checks"], "all_checks_pass": report["all_checks_pass"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.server:
        server()
    else:
        asyncio.run(probe(args.output))
