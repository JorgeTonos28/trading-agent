---
name: trading-os-bootstrap
description: Inspect and onboard a fresh Trading OS repository environment, compare observed capabilities with target requirements, guide manual setup and record environment readiness during preparation.
---

Use the repository's `ONBOARDING.md` and `planning/07_environment_bootstrap_contract_RC0.md` as the workflow. Find the Git root from the current directory; read its `AGENTS.md` before classifying readiness. If the root is absent, report the incomplete checkout and do not infer global rules.

Keep expected requirements, observed inventory and acceptance evidence separate. ADR-013 defines RESEARCH_AI_ENVIRONMENT=Team and RESEARCH_HOST=INFOTEP institutional Windows workstation; TARGET_PAPER_AI_ENVIRONMENT=individual Plus and TARGET_PAPER_COMPUTE_HOST=owner's personal Windows PC; LIVE remains UNKNOWN. Use `shared/bootstrap_manifest.json`, the active expected profile and `shared/environment_profile.schema.json`. v0.2 profiles are historical; new v0.3 observations distinguish AI plan, compute host and gate phase. Team behavior evidence never proves Plus entitlement or personal-host security. Record design_status, target_acceptance_status and operational_status separately.

During Preparation, perform independent design/read-only checks in Team and preserve UNKNOWN/NOT_TESTED. Do not request Plus access or institutional administrative setup. R-030 target acceptance is deferred to personal Windows/Plus before implementation; integrated load/recovery follows before autonomous PAPER. S2B-ADM-01 is DEFERRED_TO_TARGET_PAPER_HOST; the historical transaction/authorization is not permission to run it here or replay it on another host. Target setup requires owner gate and fresh source/transaction/SID/path binding. No automatic installation or privilege change.

Classify next actions AUTOMATED, USER_ACTION_REQUIRED, UNAVAILABLE, OPTIONAL or FALLBACK_AVAILABLE. Perform permitted read-only checks and synthetic probes; show proposed configuration changes before applying them. Never copy authentication, expose secret values, activate paid API usage, trust hooks or enlarge permissions automatically. Preserve existing user settings.

Reuse native instruction/Skill discovery and inventory tools when available. Local assets can be validated without authentication; model activation requires legitimate authentication and target gates. Do not replace missing tools with a new installer/runtime by default.

Save a sanitized readiness report with source versions/hashes, executed gates, failures and exact remaining owner actions. Agent environment readiness does not unlock implementation or trading. Package roles are reusable instructions/contracts; they do not prescribe sessions, processes or financial authority.
