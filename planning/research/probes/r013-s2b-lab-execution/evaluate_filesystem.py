"""Disposable, external FS evidence assessment; no provisioning or native calls.

Run after owner setup/login and external ACL/identity verification. Raw BASE
reports are candidates, not adversarial-proof logs. Never infer aggregate S2-B
acceptance. No secrets, network, model calls or financial actions.
"""
import argparse
import hashlib
import json
from pathlib import Path

SOURCE_SHA = "ce2a39ad0bfc7ad7cb86fd8e2a78d570bdafc6bd9c5117f37569ca45cf24fb93"
ROOT = Path("C:/ProgramData/TradingOS-S2B-Probe/trial-01")
GATE = "S2B-ADM-01"
TXN = "s2b-20261006-a6d74b2b"
SCOPE = "FS_THREAD_CONTEXTS_ONLY_NOT_PROCESS_OR_CODEX_ACCEPTANCE"


def assess(operator, base, externally_verified=False):
    """Input metadata/positives qualify observations, never authorize execution."""
    problems = []
    for actor, report in (("OPERATOR", operator), ("BASE", base)):
        if (report.get("actor") != actor or report.get("gate") != GATE
                or report.get("scope") != SCOPE
                or report.get("source_sha256") != SOURCE_SHA
                or report.get("schema_version") != "r013-s2b-filesystem-evidence-v1"):
            problems.append(f"{actor}_METADATA_INVALID")
        if report.get("status") != "OBSERVATIONS_CAPTURED_NOT_AGGREGATE_PASS":
            problems.append(f"{actor}_PROBE_ERROR")
    if not operator.get("binding_sha256") or operator.get("binding_sha256") != base.get("binding_sha256"):
        problems.append("PAIRED_BINDING_MISMATCH")
    metadata_valid = not any(p.endswith("METADATA_INVALID") or p == "PAIRED_BINDING_MISMATCH" for p in problems)
    if not externally_verified:
        problems.append("EXTERNAL_ACL_IDENTITY_AND_SCRATCH_POSITIVES_NOT_VERIFIED")

    def find(report, context, resource, mask=1):
        rows = [o for o in report.get("observations", []) if
                o.get("context") == context and o.get("resource") == resource and o.get("mask") == mask
                and o.get("result") in ("ACCESS_GRANTED", "ACCESS_DENIED", "OS_ERROR")]
        return rows[0] if len(rows) == 1 else None

    def positive(report, ctx, path, mask=1):
        r = find(report, ctx, path, mask)
        return bool(r and r.get("result") == "ACCESS_GRANTED" and r.get("winerror") == 0)

    targets = ("financial-canary/core-marker.txt", "shadow/export/snapshot.json", "pedagogy/export/champion-marker.json")
    op_positive = all(positive(operator, "OPERATOR", p) for p in targets)
    if not op_positive:
        problems.append("OPERATOR_POSITIVE_INVALID")
    base_positive = all(positive(base, "BASE", p) for p in targets[1:]) and positive(base, "BASE", "code/local-binding.json")
    if not base_positive:
        problems.append("BASE_EXPORT_CODE_POSITIVE_INVALID")
    run = base.get("run", "")
    own_positive = {}
    for label, own in (("JOB_SHADOW", "shadow"), ("JOB_PEDAGOGY", "pedagogy")):
        f = "snapshot.json" if own == "shadow" else "champion-marker.json"
        own_positive[label] = (positive(base, label, f"{own}/export/{f}")
                               and positive(base, label, f"{own}/scratch/{run}-own.txt", 2)
                               and positive(base, label, f"{own}/scratch/{run}-broad.txt"))
        if not own_positive[label]:
            problems.append(f"{label}_OWN_POSITIVE_INVALID")

    checks = []

    def check(name, ctx, path, mask=1, prerequisites=True):
        r = find(base, ctx, path, mask)
        if r is None:
            state = "NOT_TESTED"
        elif r.get("result") == "ACCESS_GRANTED" and r.get("winerror") == 0:
            state = "FAIL" if metadata_valid else "ERROR"
            # A grant from mismatched sources/identity is an unattributed signal,
            # never a confirmed failure of this realization. Preserve and block.
        elif r.get("result") == "ACCESS_DENIED" and r.get("winerror") == 5:
            state = "PASS_SCOPED" if prerequisites and not problems else "INVALID_POSITIVE"
        else:
            state = "ERROR"  # Missing, sharing violation and malformed NT/API calls are not denial.
        checks.append({"id": name, "context": ctx, "resource": path, "mask": mask, "state": state,
                       "unattributed_grant": bool(r and r.get("result") == "ACCESS_GRANTED" and not metadata_valid)})

    check("LF03_BASE_FINANCIAL_READ", "BASE", targets[0], prerequisites=op_positive)
    for label, own, peer in (("JOB_SHADOW", "shadow", "pedagogy"), ("JOB_PEDAGOGY", "pedagogy", "shadow")):
        peer_f = "champion-marker.json" if peer == "pedagogy" else "snapshot.json"
        prereq = op_positive and base_positive and all(own_positive.values())
        check(f"LF06_{label}_PEER_EXPORT", label, f"{peer}/export/{peer_f}", prerequisites=prereq)
        check(f"LF06_{label}_FINANCIAL", label, targets[0], prerequisites=prereq)
        # Descriptor-only peer positive is required for the broad child traversal case.
        obj = [o for o in base.get("observations", []) if o.get("context") == label and
               o.get("resource") == f"{peer}/scratch/{run}-broad.txt" and o.get("result") == "OBJECT_ONLY_GRANTED"]
        check(f"LF09_{label}_PEER_BROAD_CHILD", label, f"{peer}/scratch/{run}-broad.txt", prerequisites=prereq and len(obj) == 1)
        own_f = "snapshot.json" if own == "shadow" else "champion-marker.json"
        for resource in ("code", "code/local-binding.json", f"{own}/export", f"{own}/export/{own_f}",
                         "financial-canary", targets[0], "trusted-evidence", "raw-results"):
            for mask in (2, 0x40, 0x10000, 0x40000, 0x80000):
                if mask == 0x40 and resource in ("code/local-binding.json", f"{own}/export/{own_f}", targets[0]):
                    continue  # FILE_DELETE_CHILD applies to directories, not these files.
                check(f"LF07_{label}_MASK_{mask}_{resource}", label, resource, mask, prereq)

    states = [c["state"] for c in checks]
    return {
        "schema_version": "s2b-filesystem-external-evaluation-v1", "gate": GATE, "transaction_id": TXN,
        "scope": SCOPE, "metadata_or_positive_problems": problems, "checks": checks,
        "counts": {s: states.count(s) for s in ("PASS_SCOPED", "FAIL", "ERROR", "INVALID_POSITIVE", "NOT_TESTED")},
        "aggregate_security_acceptance": "NOT_ACCEPTED", "full_process_security": "NOT_TESTED",
        "native_team_compatibility": "NOT_TESTED", "external_verification_claimed": externally_verified,
        "remaining_manual_coverage": ["LF07_ROOT_RENAME_REPLACE", "LF09_ACTUAL_DACL_AND_NORMAL_CHILD_PEER",
                                      "LF10_REVOCATION_SURVIVOR_RELAUNCH", "LF11_EXTERNAL_SEAL", "LF12_ROLLBACK"],
        "trust_limit": "TRUSTED_QUIESCENT_HARNESS_NOT_ADVERSARIAL_PROCESS_AUDIT",
        "ignored_not_applicable": "FILE_DELETE_CHILD_0x40_ON_FILES",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--operator-run", required=True)
    p.add_argument("--base-run", required=True)
    args = p.parse_args()
    for r in (args.operator_run, args.base_run):
        if not r or len(r) > 40 or any(ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-" for ch in r):
            raise SystemExit("Invalid run ID")
    # Read-only assessment defaults unverified. External operator records actual
    # DACL/identity/target positives separately, then reconciles this evaluation.
    paths = [ROOT / "trusted-evidence" / (args.operator_run + ".json"), ROOT / "raw-results" / (args.base_run + ".json")]
    docs = [json.loads(f.read_text(encoding="utf-8")) for f in paths]
    result = assess(*docs)
    result["raw_evidence_sha256"] = [hashlib.sha256(f.read_bytes()).hexdigest() for f in paths]
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
