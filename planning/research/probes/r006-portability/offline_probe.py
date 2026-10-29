"""Disposable contract/readiness simulation. No installer, credentials or runtime.

Uses versioned manifest + jsonschema. Synthetic profiles cannot close Plus gates.
"""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

from jsonschema import Draft202012Validator, FormatChecker

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MANIFEST_PATH = ROOT / "shared" / "bootstrap_manifest.json"
MANIFEST = json.loads(MANIFEST_PATH.read_text())
SCHEMA = json.loads((ROOT / MANIFEST["profile_schema"]).read_text())
CHECKER = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def safe_path(root, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        raise ValueError("Noncanonical path")
    p = PurePosixPath(relative)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("Path escapes root")
    resolved = (root / relative).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError("Resolved path escapes root")
    return resolved


def manifest_files(root, manifest):
    files = [manifest[k] for k in ("root_instruction", "entry_point", "profile_schema", "expected_profile")]
    files += manifest["contracts"] + manifest["packages"] + manifest["shared_skills"]
    ids = []
    for entry in manifest["packages"]:
        p = json.loads(safe_path(root,entry).read_text())
        ids.append(p["package_id"])
        files += [p["instruction_path"],p["global_instruction_path"],p["permissions_contract"]] + p["contracts"]
        if p["candidate_procedure_path"]:
            files.append(p["candidate_procedure_path"])
        if p["authority"] != "NONE":
            raise ValueError("Role authority exceeds contract")
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate role IDs")
    return sorted(set(files))


def simulated_profile():
    scope = "PAPER_AGENT_ENVIRONMENT"
    required = [r["id"] for r in MANIFEST["requirements"] if scope in r["required_scopes"]]
    return {"schema_version":"0.1.0-planning", "environment_kind":"TARGET_PLUS_ENVIRONMENT",
        "expected_plan":"ChatGPT_Plus_individual", "observed_plan":"plus", "surface":"SYNTHETIC_FIXTURE",
        "os":"SYNTHETIC", "captured_at":"2026-10-05T12:00:00Z", "repo_commit":"a"*40,
        "manifest_sha256":hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest(),
        "instruction_chain":["AGENTS.md","agents/onboarding/AGENTS.md"],
        "package_ids_verified":["onboarding"],"inventory":[],"known_limits":["SYNTHETIC_NOT_REAL_PLUS"],
        "action_plan":[],"selected_fallbacks":[],
        "acceptance_tests":[{"gate_id":g,"environment_kind":"TARGET_PLUS_ENVIRONMENT","result":"PASSED","version":"synthetic-v1","evidence_refs":["SYNTHETIC:"+g]} for g in MANIFEST["required_gates"]],
        "requirement_results":[{"id":r,"required":True,"result":"PASSED","evidence_refs":["SYNTHETIC:"+r]} for r in required],
        "readiness_scope":scope,"readiness_state":"READY_AGENT_ENVIRONMENT","blocked_by":[],
        "authority":"NONE","implementation_locked":True}


def readiness_errors(profile):
    """Planning-only simulation of external admission; not a trusted operational gate."""
    errors = ["SCHEMA" for _ in CHECKER.iter_errors(profile)]
    if errors:
        return errors
    results = profile["requirement_results"]
    lookup = {r["id"]:r for r in results}
    if len(lookup) != len(results):
        errors.append("DUPLICATE_REQUIREMENT")
    for required in MANIFEST["requirements"]:
        if profile["readiness_scope"] in required["required_scopes"]:
            result = lookup.get(required["id"])
            if not result or result["result"] != "PASSED" or not result["required"] or not result["evidence_refs"]:
                errors.append("REQUIREMENT:"+required["id"])
    if profile["manifest_sha256"] != hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest():
        errors.append("MANIFEST_DRIFT")
    if "AGENTS.md" not in profile["instruction_chain"]:
        errors.append("GLOBAL_RULES_MISSING")
    for action in profile["action_plan"]:
        if action["requirement_id"] in lookup and lookup[action["requirement_id"]]["required"] and action["status"] in ("PENDING","BLOCKED"):
            errors.append("PENDING_ACTION:"+action["id"])
    if profile["readiness_scope"] == "PAPER_AGENT_ENVIRONMENT":
        if profile["environment_kind"] != "TARGET_PLUS_ENVIRONMENT" or profile["observed_plan"] != "plus":
            errors.append("TARGET_IDENTITY")
        for gate in MANIFEST["required_gates"]:
            entries = [t for t in profile["acceptance_tests"] if t["gate_id"] == gate]
            if len(entries)!=1 or entries[0]["environment_kind"]!="TARGET_PLUS_ENVIRONMENT" or entries[0]["result"]!="PASSED" or not entries[0]["evidence_refs"]:
                errors.append("GATE:"+gate)
    return errors


def main():
    output = HERE / "result-offline-attempt-01.json"
    if output.exists():
        raise RuntimeError("Preserve result")
    checks = []
    def check(name, value):
        checks.append({"id":name,"passed":bool(value)})
    Draft202012Validator.check_schema(SCHEMA)
    files = manifest_files(ROOT,MANIFEST)
    check("all_manifest_assets_exist",all(safe_path(ROOT,p).is_file() for p in files))
    check("six_unique_documentary_packages",len(MANIFEST["packages"])==6)
    check("root_plus_role_within_documented_default_budget",all((ROOT/'AGENTS.md').stat().st_size+safe_path(ROOT,json.loads(safe_path(ROOT,p).read_text())['instruction_path']).stat().st_size < 32768 for p in MANIFEST['packages']))
    for path in ("../outside.txt","/outside.txt","C:/Users/private","agents/../../outside","agents\\onboarding\\AGENTS.md"):
        try:
            safe_path(ROOT,path)
            rejected=False
        except ValueError:
            rejected=True
        check("reject_path:"+path,rejected)
    good = simulated_profile()
    check("synthetic_complete_profile_schema",CHECKER.is_valid(good))
    check("synthetic_complete_profile_semantics",not readiness_errors(good))
    bad_cases=[]
    def case(name,mutate):
        p=copy.deepcopy(good); mutate(p);bad_cases.append({"case":name,"profile":p}); check(name,bool(readiness_errors(p)))
    case("team_cannot_pass_target",lambda p:p.update(observed_plan="team",environment_kind="CURRENT_RESEARCH_ENVIRONMENT"))
    case("unknown_plan_not_ready",lambda p:p.update(observed_plan="UNKNOWN"))
    case("empty_results_not_ready",lambda p:p.update(requirement_results=[]))
    case("report_cannot_downgrade_required",lambda p:p['requirement_results'][0].update(required=False))
    case("unknown_required_not_ready",lambda p:p['requirement_results'][0].update(result="UNKNOWN"))
    case("failed_required_not_ready",lambda p:p['requirement_results'][0].update(result="FAILED"))
    case("empty_evidence_not_ready",lambda p:p['requirement_results'][0].update(evidence_refs=[]))
    case("global_rule_missing",lambda p:p.update(instruction_chain=[]))
    case("manifest_drift_invalidates",lambda p:p.update(manifest_sha256="0"*64))
    case("gate_team_evidence_not_target",lambda p:p['acceptance_tests'][0].update(environment_kind="CURRENT_RESEARCH_ENVIRONMENT"))
    case("missing_gate_not_ready",lambda p:p['acceptance_tests'].pop())
    case("not_tested_gate_not_ready",lambda p:p['acceptance_tests'][0].update(result="NOT_TESTED"))
    case("duplicate_gate_not_ready",lambda p:p['acceptance_tests'].append(copy.deepcopy(p['acceptance_tests'][0])))
    case("financial_authority_forbidden",lambda p:p.update(authority="EXECUTION"))
    case("cannot_unlock_implementation",lambda p:p.update(implementation_locked=False))
    case("secret_field_schema_rejected",lambda p:p.update(api_key="SYNTHETIC_FAKE_SECRET_NOT_REAL"))
    action={'id':'login','requirement_id':'plus-identity','classification':'USER_ACTION_REQUIRED','status':'PENDING','instruction':'Official UI login; no secrets to repo','requires_owner_approval':True,'evidence_refs':[]}
    case("pending_login_not_ready",lambda p:p['action_plan'].append(copy.deepcopy(action)))
    p=copy.deepcopy(good);p['action_plan'].append({**action,'id':'optional-plugin','requirement_id':'optional-data','classification':'OPTIONAL'})
    check('missing_optional_does_not_block',not readiness_errors(p))
    p=copy.deepcopy(good);p['selected_fallbacks']=[{'requirement_id':'plus-GP1-7','candidate_id':'manual','selection_status':'PROPOSED','evidence_refs':[]}];p['requirement_results'][-2]['result']='UNKNOWN'
    check('proposed_fallback_does_not_pass_unknown',bool(readiness_errors(p)))
    # Same serialized input produces same errors; this does not prove durable runtime recovery.
    p=bad_cases[0]['profile'];check('simulated_restart_same_classification',readiness_errors(p)==readiness_errors(json.loads(json.dumps(p))))
    hashes={p:hashlib.sha256(safe_path(ROOT,p).read_bytes()).hexdigest() for p in files}
    check('manifest_snapshot_repeatable',hashes=={p:hashlib.sha256(safe_path(ROOT,p).read_bytes()).hexdigest() for p in files})
    report={'probe':'R028_OFFLINE_CONTRACT_01','evidence_kind':'SYNTHETIC_SIMULATION_NOT_TARGET_ACCEPTANCE','selected':False,'AVAILABLE_IN_TARGET_PLUS':'UNKNOWN','checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'asset_sha256':hashes,'limitations':['not entitlement or model activation','not ACL or general secret detection','not durable recovery or installer','evidence_refs existence/trust remains real gate responsibility']}
    output.write_text(json.dumps(report,indent=2)+'\n')
    (HERE/'fixtures-readiness.json').write_text(json.dumps({'evidence_kind':'SIMULATED_NOT_EXECUTED_TARGET','complete_fixture':good,'negative_fixtures':bad_cases},indent=2)+'\n')
    print(json.dumps({'passed':report['passed'],'total':report['total']}))
    if report['passed']!=report['total']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
