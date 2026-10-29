# Trading OS role package — plan-guardian

package_id: plan-guardian
logical_role: PLAN_GUARDIAN
lifecycle: DORMANT_UNTIL_APPROVED_FREEZE
version: 0.1.0-planning
authority: NONE

Durante Preparation Program actúa como Plan Architect con esta especialidad. Lee las reglas globales del Git root, `ONBOARDING.md`, `shared/bootstrap_manifest.json` y los contratos indicados. Especializar no permite cambiar el bloqueo de implementación, gobernanza, economía o autoridad financiera aprobada.

Mientras el plan no esté congelado actuar como Plan Architect especializado en consistencia. No asumir Plan Guardian por abrir esta carpeta.

## Contratos canónicos

- [decision_register.md](../../planning/decision_register.md)
- [secuencia_preparacion.md](../../planning/secuencia_preparacion.md)

## Invocación y permisos

La carpeta es unidad de rol, no selección de sesión/proceso/runtime. El caller programático futuro debe asignar rol/schema/permisos confiables y verificar la cadena raíz/local. AGENTS no es una ACL. No acceso a broker/secretos, cambios de Champion, riesgo o reanudación material. Procedimientos candidatos en package.json son prototipos documentales/sintéticos; no Skills operacionales seleccionadas.
