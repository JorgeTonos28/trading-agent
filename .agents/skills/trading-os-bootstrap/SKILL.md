---
name: trading-os-bootstrap
description: Inspect and onboard a fresh Trading OS repository environment, compare observed capabilities with target requirements, guide manual setup and record environment readiness during preparation.
---

Use the repository's `ONBOARDING.md` and `planning/07_environment_bootstrap_contract_RC0.md` as the workflow. Find the Git root from the current directory; read its `AGENTS.md` before classifying readiness. If the root is absent, report the incomplete checkout and do not infer global rules.

Keep expected requirements, observed inventory and acceptance evidence separate. CURRENT_RESEARCH_ENVIRONMENT and PAPER_RUNTIME_ENVIRONMENT are current Team (ADR-010). Evaluate PAPER against Team TP1–7 and EB1–8. FUTURE_LIVE_ENVIRONMENT is individual Plus candidate; its PRE-LIVE migration gate R-029 must not block PAPER. Team never proves Plus entitlement. Use `shared/bootstrap_manifest.json` and `shared/environment_profile.schema.json`; preserve UNKNOWN/NOT_TESTED for unobserved mandatory requirements.

Classify next actions AUTOMATED, USER_ACTION_REQUIRED, UNAVAILABLE, OPTIONAL or FALLBACK_AVAILABLE. Perform permitted read-only checks and synthetic probes; show proposed configuration changes before applying them. Never copy authentication, expose secret values, activate paid API usage, trust hooks or enlarge permissions automatically. Preserve existing user settings.

Reuse native instruction/Skill discovery and inventory tools when available. Local assets can be validated without authentication; model activation requires legitimate authentication and target gates. Do not replace missing tools with a new installer/runtime by default.

Save a sanitized readiness report with source versions/hashes, executed gates, failures and exact remaining owner actions. Agent environment readiness does not unlock implementation or trading. Package roles are reusable instructions/contracts; they do not prescribe sessions, processes or financial authority.
