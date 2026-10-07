# R-029 — Pre-Live Environment Migration & Acceptance Gate

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-05. **P3 / DEFERRED**, D-039; ADR-010. Reclasifica el Plus Acceptance Gate anterior, conservado en `R-006_plus_runtime_gate_RC0.md` como contrato histórico. No gate PAPER ni DoR de implementación Team.

## Activación

Solo cuando arquitectura aprobada, sistema implementado, PAPER Team validado y flujo operacional probado, y el dueño decida preparar la migración. `FUTURE_LIVE_ENVIRONMENT = ChatGPT Plus individual` es candidato, no despliegue final aprobado. Autorización LIVE/capital/broker/riesgo es distinta de aceptación del entorno.

## Migración reproducible

Release/tag aprobado del repo + manifest/config/roles versionados → clone nuevo → Bootstrap Mode para FUTURE_LIVE_ENVIRONMENT → diff Team/Plus → configuración permitida y acciones manuales → smoke/deltas → workload/recovery → reporte comparativo de readiness. Nunca migrar secretos/auth por Git; usar login/consentimiento oficial del dueño.

| Gate PRE-LIVE | Evidencia requerida al activarse |
|---|---|
| ML-1 identidad/entitlement | Cuenta Plus individual y superficie/cliente reales, lectura sanitizada |
| ML-2 assets/config/discovery | Release/tag exacto, perfiles esperado/observado, raíz/rol/Skills/overrides, plugins/MCP necesarios |
| ML-3 compatibilidad | Roles/schemas/tools finales funcionan; reusar conducta Team, regresión solo de diferencias materiales |
| ML-4 permisos/seguridad | Políticas seleccionadas conservadas, ninguna autoridad financiera adicional; secretos fuera de entorno agéntico/Git |
| ML-5 persistencia/recovery | Contextos/versiones/políticas coherentes tras restart, fallos/auth/cuota/late/duplicados contabilizados |
| ML-6 suficiencia/economía | **Workload del sistema ya validado**, no adoptar automáticamente los 40/63 jobs de un fixture antiguo; cuotas compartidas/continuidad/latencia coste por medir |
| ML-7 operación/aceptación | Términos de ruta, readiness auditable, rollback Team, responsable, aprobación del dueño; LIVE gate separado |

Si Plus no cumple, comparar conservar Team u otra ruta OpenAI/Anthropic económicamente justificada; no degradar invariantes ni contratar sin aprobación. Los resultados actuales Plus permanecen UNKNOWN donde no hay evidencia real.

## Fuentes y evidencia histórica

[Gate Plus RC3 anterior](R-006_plus_runtime_gate_RC0.md), [entitlement documental](R-006_plus_entitlement_evidence_2026-10-02.md), [ADR-007](../decisions/ADR-007-r006-openai-anthropic-plus-scope.md), [ADR-009](../decisions/ADR-009-environment-bootstrap-portability.md), [ADR-010](../decisions/ADR-010-team-paper-and-prelive-plus-migration.md). No borrar ni modificar resultados de probes publicados para esta reclasificación.
