"""Disposable schema experiment prompted by wave-04 output mixing.

Uses trusted invocation role, never lets model output select its validator.
Does not implement Trading OS admission, TradeIntent, risk or execution.
"""
import copy
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent


def schema_for(expected_role):
    schema = json.loads((ROOT / "output_schema.json").read_text())
    schema["properties"]["role"] = {"const": expected_role}
    mode = {"research": "RESEARCH_ONLY", "quant": "RESEARCH_ONLY",
            "pedagogy": "PEDAGOGICAL_ONLY", "shadow": "SHADOW_ONLY"}[expected_role]
    schema["properties"]["mode"] = {"const": mode}
    schema["properties"]["authority"] = {"const": "NONE"}
    if expected_role != "shadow":
        schema["properties"]["proposals"]["maxItems"] = 0
    return schema


def main():
    report = json.loads((ROOT / "result-attempt-02.json").read_text(encoding="utf-8"))
    rows = []
    for t in report["trials"]:
        expected = "research" if t["case"] == "tool_failure" else t["case"]
        errors = list(Draft202012Validator(schema_for(expected)).iter_errors(t["output"]))
        rows.append({"case": t["case"], "variant": t["variant"], "repetition": t["repetition"],
                     "accepted_by_prototype_role_schema": not errors,
                     "error_paths": [list(e.absolute_path) for e in errors]})
    shadow = next(t["output"] for t in report["trials"] if t["case"] == "shadow")
    negative_checks = {}
    for label, change in (
        ("operative_mode_rejected", {"mode": "OPERATIVE"}),
        ("order_authority_rejected", {"authority": "ORDER_ALLOWED"}),
        ("trade_intent_field_rejected", {"trade_intent": {"symbol": "SYN-A", "quantity": 50}}),
        ("output_role_cannot_select_validator", {"role": "research"}),
    ):
        altered = copy.deepcopy(shadow)
        altered.update(change)
        negative_checks[label] = not Draft202012Validator(schema_for("shadow")).is_valid(altered)
    result = {"probe": "R006-ROLE-SCHEMA-01", "stage": "post-wave-04_illustrative_mitigation_not_retest",
              "library": "jsonschema", "SELECTED": False, "behavioral_sample_repeated": False,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "original_generic_schema_valid_count": sum(not t["schema_errors"] for t in report["trials"]),
              "trusted_role_schema_valid_count": sum(r["accepted_by_prototype_role_schema"] for r in rows),
              "rows": rows, "synthetic_negative_checks": negative_checks,
              "limits": "Shows JSON schema discrimination only. Does not prove financial authority isolation, production permissions, source validity or prompt-injection immunity."}
    (ROOT / "role-admission-result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("original_generic_schema_valid_count", "trusted_role_schema_valid_count", "synthetic_negative_checks")}))


if __name__ == "__main__":
    main()
