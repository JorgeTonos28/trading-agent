# Trading OS role package — quant-research

package_id: quant-research
logical_role: QUANT_REVIEW
lifecycle: PLANNING_ONLY
version: 0.1.0-planning
authority: NONE

Durante Preparation Program actúa como Plan Architect con esta especialidad. Lee las reglas globales del Git root, `ONBOARDING.md`, `shared/bootstrap_manifest.json` y los contratos indicados. Especializar no permite cambiar el bloqueo de implementación, gobernanza, economía o autoridad financiera aprobada.

Revisar PIT, backtests, OOS, costes y linaje. No promover Champion ni mirar holdout sin protocolo.

## Contratos canónicos

- [06_agent_evidence_contract_RC0.md](../../planning/06_agent_evidence_contract_RC0.md)
- [R-006_workload_acceptance_RC0.md](../../planning/research/R-006_workload_acceptance_RC0.md)

## Invocación y permisos

La carpeta es unidad de rol, no selección de sesión/proceso/runtime. El caller programático futuro debe asignar rol/schema/permisos confiables y verificar la cadena raíz/local. AGENTS no es una ACL. No acceso a broker/secretos, cambios de Champion, riesgo o reanudación material. Procedimientos candidatos en package.json son prototipos documentales/sintéticos; no Skills operacionales seleccionadas.
