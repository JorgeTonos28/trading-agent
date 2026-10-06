"""Offline source/evaluator QA. Synthetic fixtures are NEVER filesystem evidence."""
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREP = HERE.parent / "r013-s2b-lab-prep"
checks = []


def record(name, okay):
    checks.append({"id": name, "state": "PASS" if okay else "FAIL", "scope": "OFFLINE_SOURCE_OR_SYNTHETIC_EVALUATOR_ONLY"})


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


record("PINNED_POLICY_UNCHANGED", sha(PREP / "lab-policy-plan.json") == "ade0ac46b2967c6f2e5e05df3d3d93b41de7e699ed921ffb78beeb636d02d6c7")
record("PINNED_FS_SOURCE_UNCHANGED", sha(PREP / "filesystem_probe.py") == "ce2a39ad0bfc7ad7cb86fd8e2a78d570bdafc6bd9c5117f37569ca45cf24fb93")
ast.parse((PREP / "filesystem_probe.py").read_text(encoding="utf-8"))
record("FILESYSTEM_SOURCE_AST_ONLY", True)
spec = importlib.util.spec_from_file_location("lab_evaluator", HERE / "evaluate_filesystem.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def row(ctx, path, mask=1, result="ACCESS_GRANTED", error=0):
    return {"context": ctx, "resource": path, "mask": mask, "result": result, "winerror": error}


meta = {"gate": mod.GATE, "scope": mod.SCOPE, "source_sha256": mod.SOURCE_SHA,
        "schema_version": "r013-s2b-filesystem-evidence-v1", "binding_sha256": "SYNTHETIC_SHARED",
        "status": "OBSERVATIONS_CAPTURED_NOT_AGGREGATE_PASS", "run": "synthetic"}
op = dict(meta, actor="OPERATOR", observations=[row("OPERATOR", p) for p in
          ("financial-canary/core-marker.txt", "shadow/export/snapshot.json", "pedagogy/export/champion-marker.json")])
base = dict(meta, actor="BASE", observations=[row("BASE", p) for p in
            ("shadow/export/snapshot.json", "pedagogy/export/champion-marker.json", "code/local-binding.json")])
base["observations"].append(row("BASE", "financial-canary/core-marker.txt", result="ACCESS_DENIED", error=5))
for label, own in (("JOB_SHADOW", "shadow"), ("JOB_PEDAGOGY", "pedagogy")):
    f = "snapshot.json" if own == "shadow" else "champion-marker.json"
    base["observations"] += [row(label, f"{own}/export/{f}"), row(label, f"{own}/scratch/synthetic-own.txt", 2),
                             row(label, f"{own}/scratch/synthetic-broad.txt")]

def state(result, check="LF03_BASE_FINANCIAL_READ"):
    return next(c["state"] for c in result["checks"] if c["id"] == check)

record("UNVERIFIED_EXTERNAL_POSITIVES_CANNOT_PASS", state(mod.assess(op, base)) == "INVALID_POSITIVE")
record("DENIAL_WITH_VERIFIED_SYNTHETIC_POSITIVES_SCOPED", state(mod.assess(op, base, True)) == "PASS_SCOPED")
bad_op = copy.deepcopy(op); bad_op["observations"][0]["result"] = "OS_ERROR"
record("FAILED_OPERATOR_POSITIVE_INVALIDATES_DENIAL", state(mod.assess(bad_op, base, True)) == "INVALID_POSITIVE")
bad_base = copy.deepcopy(base); bad_base["binding_sha256"] = "DIFFERENT"
record("BINDING_MISMATCH_INVALIDATES_DENIAL", state(mod.assess(op, bad_base, True)) == "INVALID_POSITIVE")
for error in (2, 3, 32):
    bad_base = copy.deepcopy(base)
    bad_base["observations"][3].update(result="OS_ERROR", winerror=error)
    record(f"MISSING_OR_SHARING_ERROR_{error}_IS_ERROR", state(mod.assess(op, bad_base, True)) == "ERROR")
bad_base = copy.deepcopy(base); bad_base["observations"][3].update(result="ACCESS_GRANTED", winerror=0)
record("FORBIDDEN_GRANT_IS_FAIL_EVEN_WITHOUT_POSITIVES", state(mod.assess(bad_op, bad_base)) == "FAIL")
bad_base["source_sha256"] = "INVALID_SOURCE"
result = mod.assess(op, bad_base, True)
record("UNATTRIBUTED_GRANT_BLOCKS_WITH_ERROR", state(result) == "ERROR" and result["checks"][0]["unattributed_grant"])
bad_base = copy.deepcopy(base); del bad_base["observations"][3]
record("MISSING_OBSERVATION_IS_NOT_TESTED", state(mod.assess(op, bad_base, True)) == "NOT_TESTED")
bad_base = copy.deepcopy(base); bad_base["observations"].append(copy.deepcopy(bad_base["observations"][3]))
record("DUPLICATE_OBSERVATION_CANNOT_PASS", state(mod.assess(op, bad_base, True)) == "NOT_TESTED")
record("AGGREGATE_S2B_NEVER_ACCEPTED", mod.assess(op, base, True)["aggregate_security_acceptance"] == "NOT_ACCEPTED")

print(json.dumps({"mode": "OFFLINE_SYNTHETIC_QA_NOT_NATIVE_FS", "checks": checks,
                  "counts": {s: sum(c["state"] == s for c in checks) for s in ("PASS", "FAIL")},
                  "actual_filesystem_tests_executed": False, "actual_security_acceptance": "NOT_TESTED",
                  "configuration_changes": [], "model_calls": 0,
                  "source_sha256": {p.name: sha(p) for p in (HERE / "evaluate_filesystem.py", Path(__file__))}}, indent=2))
if any(c["state"] != "PASS" for c in checks):
    raise SystemExit(1)
