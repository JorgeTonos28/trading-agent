# Checkpoint — arquitectura agéntica de diseño PAPER

2026-10-07 · **READY_FOR_DECISION**, no aprobado · D-024/D-027/D-037 · ADR-013 vigente.

## Dictamen y alcance exacto

R-006 es **MATURE_FOR_DESIGN_DECISION**. Cobertura relevante OpenAI/Anthropic, licencias/costes, capacidades reales en research, procedimientos comparados, PIT/lineage, failures/injection, autoridad, packages y fresh clone tienen evidencia y límites registrados. D-020 conserva las disposiciones aprobadas; no reiniciar discovery por el cambio de target. No hay una nueva selección de framework AI ni gasto.

Recomiendo aprobar [B-RT1](08_agentic_runtime_realization_RC1.md) como **realización de diseño candidata** bajo ADR-011/012: supervisor/control externo C, Runner A y contexto restringido J por intento; transporte oficial nativo, tools mínimas con stubs sin privilegios, binding/ledger externo, auth nativa mínima y estado por job. Especifica concretamente la dirección S2-B ya aprobada; no solicita repetir A+/G1+G2/S2-B ni autorizar usuarios/ACL/login aquí. [ADR-014 propuesto](decisions/ADR-014-agentic-design-checkpoint-proposed.md).

Si el propietario aprueba esta realización, puede declararse **AGENTIC_ARCHITECTURE_DESIGN_COMPLETE en este scope**: contratos de capacidades/roles y fronteras de integración/autoridad, launcher/auth/state/failure/recovery requeridos y ruta de aceptación reproducible. No equivale a cerrar todos los P1 del sistema, elegir versiones operacionales finales, congelar Plan/permiso efectivo ni implementar.

Actualmente: `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE = PENDING_OWNER_DESIGN_CHECKPOINT`; `PAPER_RUNTIME_ACCEPTED = false`; `implementation_locked = true`. Mantener estados principales D-024/D-027/D-037 abiertos hasta sus cierres completos, con dimensiones separadas. No convertir un readiness de investigación en aceptación target.

## Qué se resolvió en Team

| Pregunta material | Resultado de diseño / evidencia |
|---|---|
| ¿LLM residente o per-job? | Dirección aprobada: core always-on local, scheduler automático y jobs por evento/calendario; sin approval rutinario |
| ¿Qué reutilizar? | RC2 aprobado: Codex/AGENTS/Skills REUSE_AS_IS; SDK WRAP; Anthropic idea-generation/thesis-tracker ADAPT/PORT; Quant/Ped/Bootstrap propios ADAPT; MCP reserva con necesidad concreta; API/plugin premium sin gasto |
| ¿Dónde viven supervisor/auth/handlers/ledger? | B-RT1: F/C/A/J, sin broker secrets en AI; stubs J, operaciones C, recepción y fencing en una transacción ledger C |
| ¿Cómo evitar persistencia accidental? | HOME mínimo auth/config fijo readonly, redirects por job; namespace keyring deriva HOME según source pinada; WinCred carrier explícito BL-AUTH. Compatibilidad/eficacia NOT_TESTED |
| ¿Qué sucede al fallar? | Timeout/quota/tool/protocol/late/no-output explícitos; ausencia ≠ HOLD; admission externo, sin duplicar efectos financieros ni autoridad alternativa |
| ¿Cómo viajar sin chat? | ONBOARDING/manifest/role packages + binding instancia/fingerprint/fase; B1 16 casos sintéticos, no verificador productivo ni Plus bootstrap |
| ¿El workflow reusable recupera trabajo? | H6 persistence; H7 Temporal worker redelivery intento2; H8 APS calendario/restart/misfire. Semánticas diferentes, no workload PAPER ni elección de engine |
| ¿Qué revisión independiente falta? | [Revisión](research/R-006_design_independent_review_2026-10-07.md): reparaciones documentales incorporadas, propuesta apta para presentar a owner, sin aprobación humana/técnica implícita |

## Incógnitas separadas

**Target acceptance R-030, no acción ahora:** Plus/entitlement/modelos/tools/cuota, auth/keyring/refresh, launch cross-user y derechos concretos, home readonly/redirects/cache/credential carriers, token/process/handles/desktop/IPC/egress, filesystem ACL reales, blinding, fresh clone/pins y recovery de fixtures. Cada gate debe enlazar instancia/fingerprint/versión/fase; no heredar PASS Team. S2B-ADM-01 DEFERRED_TO_TARGET_PAPER_HOST. Si una prueba exige más confianza, persistencia compartida, servicio privilegiado, login por job o permisos amplios, reabrir diseño/gobierno; A/S3 no migraciones automáticas.

**Diseño transversal todavía resoluble Team:** D-025 engine/workflow y parámetros ligados a Strategy; D-026 store/retención/backups; D-028 SLO/RPO/RTO/deployment; D-029 evaluación integrada; D-034 metrics/engine shadow y D-035 fórmulas riesgo. Son P1 auténticos, no diferidos por falta de Plus. Solo pueden ser elegidos preservando ownership/interfaces B-RT1; cambios de trust/authority requieren reabrir este checkpoint. [Comparación](research/R-010_workflow_storage_comparison_RC1.md).

**Operacional posterior a implementación:** carga/cadencia sostenida con Strategy V1, integración/reconciliación, backtests ejecutables, broker/data/failure injection, report Pedagogy completo, shadow counterfactual y PAPER validado. Nunca aceptación por smoke. LIVE entorno/host no seleccionados.

## Secuencia y endpoint de este paquete

1. Corrección ADR-013 persistida y sincronizada; artefactos históricos conservados.
2. Diseño B-RT1/binding y probes independientes completados; crítica y fuentes registradas.
3. Avanzar un paquete documental financiero independiente: demanda de candidatos y evidencia primaria broker/data, sin cuenta/credenciales/backtest/selección. No esperar Plus.
4. **HUMAN_ACTION_REQUIRED** solo para aprobar/revisar B-RT1/ADR-014 como scope de diseño material. El owner no debe dar acceso Plus ni hacer administración INFOTEP. Si aprueba, registrar DESIGN_DECIDED/TARGET_ACCEPTANCE_DEFERRED, cambiar foco principal a Strategy V1/datos/broker/backtest/riesgo y completar P0/P1 restantes.

Antes de anunciar hitos: consistencia, commit/push plan-architect; main estable y ningún release/merge automático.
