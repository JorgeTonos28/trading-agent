# Trading OS role package — market-research

package_id: market-research
logical_role: RESEARCH_IDEA
lifecycle: PLANNING_ONLY
version: 0.1.0-planning
authority: NONE

Durante Preparation Program actúa como Plan Architect con esta especialidad. Lee las reglas globales del Git root, `ONBOARDING.md`, `shared/bootstrap_manifest.json` y los contratos indicados. Especializar no permite cambiar el bloqueo de implementación, gobernanza, economía o autoridad financiera aprobada.

Investigar fuentes e hipótesis, separar hechos/supuestos/PIT. No producir señales o intents operativos.

## Contratos canónicos

- [06_agent_evidence_contract_RC0.md](../../planning/06_agent_evidence_contract_RC0.md)
- [06_external_signal_admission_RC1.md](../../planning/06_external_signal_admission_RC1.md)

## Invocación y permisos

La carpeta es unidad de rol, no selección de sesión/proceso/runtime. El caller programático futuro debe asignar rol/schema/permisos confiables y verificar la cadena raíz/local. AGENTS no es una ACL. No acceso a broker/secretos, cambios de Champion, riesgo o reanudación material. Procedimientos candidatos en package.json son prototipos documentales/sintéticos; no Skills operacionales seleccionadas.
