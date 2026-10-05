# R-006 — Plus Acceptance Gate RC1

**Actualizado:** 2026-10-05. **Estado:** `OPEN`, reservado a finalistas; arquitectura/runtime D-024 no seleccionados. Este contrato concreta ADR-007/008 y la instrucción del propietario del 5 de octubre. Team produce evidencia conductual y una shortlist sin depender de acceso a Plus. Este gate verifica solo diferencias del entorno objetivo. Su nombre de archivo RC0 se conserva para evitar romper referencias; el contenido es RC1.

## Rutas candidatas y economía

| Ruta | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Codex directo + Skill local | UNKNOWN workflow completo en Plus | Potencial 0 incremental; suscripción existente/cupo y local coste por medir | UNKNOWN a escala | Procedimiento mínimo Codex, por evaluar | API como alternativa si continuidad/calidad insuficiente; sin demostrar | YES si gasto adicional |
| Codex app-server con autenticación nativa ChatGPT | UNKNOWN en Plus; discovery Team probado | Potencial 0 incremental; operación/cupo UNKNOWN | UNKNOWN | Codex directo candidato | Control de integración sin probar suficiencia operacional | YES si gasto adicional |
| SIWC uso del plan + app-server | UNKNOWN OAuth/inferencia Plus | Potencial 0 incremental; límite compartido/operación UNKNOWN | UNKNOWN | Codex directo/nativo candidatos | Comparar continuidad/control con API paga si gate falla | YES si gasto adicional |
| OpenAI API con key / SDK | NO como consumo incluido Plus | UNKNOWN facturación por workload | UNKNOWN fijo/variable/mensual/escala | Rutas anteriores, aún no viables probadas | Hipótesis: control/capacidad/continuidad; medir y justificar | YES antes de gasto |
| Anthropic API/Managed Agents | NO como consumo incluido Plus | UNKNOWN facturación; ejecución excluida sin aprobación | UNKNOWN por workload/servicio | Skills públicas portadas hacia Codex | Hipótesis: calidad/operación futura; no probar pagando sin aprobación | YES antes de gasto |

Skills/templates se adquieren gratis/incluidos/propios; inferencia/runtime/datos se evalúan aparte. `PENDING/UNKNOWN` no es elección ni rechazo permanente. Ninguna ruta recibe credenciales de broker, canal de órdenes o autoridad financiera generativa.

## Evidencia necesaria antes de recomendar una ruta PAPER

| Gate | Evidencia requerida | Estado actual |
|---|---|---|
| GP-1 identidad/entitlement | Owner identifica la cuenta objetivo; lectura sanitizada bajo ella confirma Plus individual y cliente/superficie. Sin tokens/email/IDs en repo. | OPEN; Team observado, Plus documental no empírico. |
| GP-2 formato/discovery | Skill desechable versionada aparece en esa ruta; distinguir discovery local de activación del modelo. Conservar versión CLI/schema y errores. | PARTIAL solo investigación: wave 02 formato y wave 03 discovery Team. |
| GP-3 activación/compatibilidad | Smoke test acotado por ruta finalista: inferencia incluida, Skill realmente activada, salida estructurada y herramientas necesarias disponibles. Registrar diferencias de versión/modelo; reutilizar pruebas comparativas Team, sin repetir toda la investigación. | OPEN en Plus; conducta Team se registra aparte. |
| GP-4 permisos del entorno | Confirmar que sandbox, allowlist, herramientas y autenticación de la ruta finalista soportan los límites ensayados. Repetir solo negativos afectados por una diferencia concreta; nunca dar acceso a broker/secretos. | OPEN en Plus; barreras de harness y conducta son evidencias distintas. |
| GP-5 estado/recovery | Contexto/snapshots versionados, reanudación tras caída, expiración/refresh/revocación y recovery de tool; no doble efecto. Verificar APIs de la versión/ruta usada. | OPEN; handshake no equivale a recuperación. |
| GP-6 suficiencia/coste | Carga PAPER propuesta para research/shadow/pedagogía: latencia, cuotas compartidas, turnos/contexto, ventanas y margen operativo medidos; ficha coste/escala. No extrapolar capacidad Team a Plus. | OPEN; workload/criterios por especificar sin fijar umbrales financieros. |
| GP-7 términos/operación | Ruta autorizada para uso local y modo previsto, acceso a modelos/tools, preview/lifecycle y política de datos documentados; ausencia de facturación inadvertida. Cualquier pago va al dueño con comparación ADR-008. | PARTIAL documentación; operación concreta no validada. |

**Fuentes de compatibilidad:** [App Server](https://learn.chatgpt.com/docs/app-server), [SIWC app-server](https://developers.openai.com/siwc/token-sharing-open-source/codex-app-server), [preview](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations), [sesiones/cuota](https://developers.openai.com/siwc/token-sharing-open-source/profiles-and-sessions). Para SIWC, catálogo de modelos no prueba entitlement; OAuth/scope y una inferencia completada son evidencias pendientes. Las limits/tools/refresh de esa ruta no se trasladan automáticamente a Codex nativo.

## Regla de avance

Registrar `AVAILABLE_IN_RESEARCH_ENVIRONMENT` y `AVAILABLE_IN_TARGET_PLUS` por capacidad/subcapacidad. Un fallo temporal se investiga antes de concluir `NO`; un permiso desconocido sigue `UNKNOWN`. No usar la cuenta Team como reemplazo del gate. Si Plus no es suficiente, comparar rediseño/carga Tier 0/1 y alternativa paga con calidad/coste/valor por fase; llevar gasto concreto al propietario. D-024 requiere además madurez global R-006, revisión crítica y gobierno humano; este gate por sí solo no descongela agentes ni implementación.

**Dependencia:** pruebas conductuales Team → shortlist condicional → este gate para finalistas → propuesta de selección/gobierno. No exigir GP-1–7 para iniciar comparación o presentar shortlist. Una cuota insuficiente puede limitar la cadencia agéntica sin detener necesariamente un núcleo local determinístico; esa alternativa permanece abierta. GP-5/6 deben valorar research, shadow y pedagogía intermitentes y distinguir fallos de agentes de incidentes financieros materiales (ADR-002). No presume continuidad desatendida ni disponibilidad Plus.
