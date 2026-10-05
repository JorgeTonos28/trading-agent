# R-006 — Plus Acceptance Gate RC3

**RECLASIFICADO / HISTÓRICO — ADR-010:** este contrato Plus y sus criterios originales se preservan. Su dependencia PAPER queda SUPERSEDED; es P3 PRE-LIVE, [R-029](R-029_pre_live_environment_migration_gate_RC0.md)/D-039 DEFERRED. El gate activo PAPER es [Team TP1–7](R-006_team_runtime_acceptance_RC0.md). No pedir acceso Plus ni bloquear D-020/D-024/implementación/PAPER por este archivo.

## Contrato anterior conservado

**Actualizado:** 2026-10-05. **Estado:** `OPEN`, reservado a finalistas; arquitectura/runtime D-024 no seleccionados. Este contrato concreta ADR-007/008 y la instrucción del propietario del 5 de octubre. Team produce evidencia conductual y shortlist sin depender de Plus. Este gate verifica diferencias del entorno objetivo. Nombre RC0 conservado para referencias, contenido RC3. [Shortlist RC1](R-006_shortlist_RC1.md) y [workload/matriz RC0](R-006_workload_acceptance_RC0.md) definen la cohorte y criterios propuestos; no se ejecutó gate target.

## Rutas candidatas y economía

| Ruta | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Codex directo + Skill local | UNKNOWN workflow completo en Plus | Potencial 0 incremental; suscripción existente/cupo y local coste por medir | UNKNOWN a escala | Procedimiento mínimo Codex, por evaluar | API como alternativa si continuidad/calidad insuficiente; sin demostrar | YES si gasto adicional |
| Codex app-server con autenticación nativa ChatGPT | UNKNOWN en Plus; discovery Team probado | Potencial 0 incremental; operación/cupo UNKNOWN | UNKNOWN | Codex directo candidato | Control de integración sin probar suficiencia operacional | YES si gasto adicional |
| C-029 Codex SDK sobre CLI/auth nativo | UNKNOWN workflow Plus; un smoke Team Python | 0 licencia; potencial cuota incluida y local por medir | UNKNOWN escala/modelos/tools | C-025a/C-010 con gates | Continuidad/control adicionales por probar | YES si dependencia paga |
| SIWC uso del plan + app-server | UNKNOWN OAuth/inferencia Plus | Potencial 0 incremental; límite compartido/operación UNKNOWN | UNKNOWN | Codex directo/nativo candidatos | Comparar continuidad/control con API paga si gate falla | YES si gasto adicional |
| OpenAI API con key / SDK | NO como consumo incluido Plus | UNKNOWN facturación por workload | UNKNOWN fijo/variable/mensual/escala | Rutas anteriores, aún no viables probadas | Hipótesis: control/capacidad/continuidad; medir y justificar | YES antes de gasto |
| Anthropic API/Managed Agents | NO como consumo incluido Plus | UNKNOWN facturación; ejecución excluida sin aprobación | UNKNOWN por workload/servicio | Skills públicas portadas hacia Codex | Hipótesis: calidad/operación futura; no probar pagando sin aprobación | YES antes de gasto |

Skills/templates se adquieren gratis/incluidos/propios; inferencia/runtime/datos se evalúan aparte. `PENDING/UNKNOWN` no es elección ni rechazo permanente. Ninguna ruta recibe credenciales de broker, canal de órdenes o autoridad financiera generativa.

## Evidencia necesaria antes de recomendar una ruta PAPER

| Gate | Evidencia requerida | Estado actual |
|---|---|---|
| GP-1 identidad/entitlement | Owner identifica la cuenta objetivo; lectura sanitizada bajo ella confirma Plus individual y cliente/superficie. Sin tokens/email/IDs en repo. | OPEN; Team observado, Plus documental no empírico. |
| GP-2 formato/discovery | Skill desechable versionada aparece en esa ruta; distinguir discovery local de activación del modelo. Conservar versión CLI/schema y errores. | OPEN Plus; formato/activación Team waves 02–06 ejecutados, no prueba entitlement. |
| GP-3 activación/compatibilidad | Smoke test acotado por ruta finalista: inferencia incluida, Skill realmente activada, salida estructurada y herramientas necesarias disponibles. Registrar diferencias de versión/modelo; reutilizar pruebas comparativas Team, sin repetir toda la investigación. | OPEN en Plus; conducta Team se registra aparte. |
| GP-4 permisos del entorno | Confirmar que sandbox, allowlist, herramientas y autenticación de la ruta finalista soportan los límites ensayados. Repetir solo negativos afectados por una diferencia concreta; nunca dar acceso a broker/secretos. | OPEN en Plus; barreras de harness y conducta son evidencias distintas. |
| GP-5 estado/recovery | Contexto/snapshot/rol idénticos tras restart; intentos y entregas auditadas, máximo un resultado admitido por job, outputs tardíos/duplicados visibles. Auth expirada/refresh/revocación se verifica con método permitido y contexto sanitizado; no revocar sesión del dueño sin acción explícita. Tool/quota/auth failure no dispara API paga ni efecto financiero. | OPEN; schemas/clasificación offline no son persistencia/recovery real. |
| GP-6 suficiencia/coste | Ejecutar workload representativo propuesto WL-R de la matriz: 40 jobs base/día, demanda interactiva/reserva hasta 63, bundles ≤32 KiB, ventanas/deadlines y ≥95% on-time propuestos, 100% accounting y checks críticos. Medir cuota compartida/reset y carga durante sesiones suficientes (propuesta 5 sesiones/≥7 días); rebaselinar con Strategy V1. No usar tamaño/token/latencia Team como cupo. | OPEN; criterios especificados, carga target no ejecutada ni SLA/cadencia financiera aprobada. |
| GP-7 términos/operación | Ruta autorizada para uso local y modo previsto, acceso a modelos/tools, preview/lifecycle y política de datos documentados; ausencia de facturación inadvertida. Cualquier pago va al dueño con comparación ADR-008. | PARTIAL documentación; operación concreta no validada. |

**Fuentes de compatibilidad:** [App Server](https://learn.chatgpt.com/docs/app-server), [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk), [SIWC app-server](https://developers.openai.com/siwc/token-sharing-open-source/codex-app-server), [preview](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations), [sesiones/cuota](https://developers.openai.com/siwc/token-sharing-open-source/profiles-and-sessions). App-server/SDK nativo y SIWC OAuth son rutas separadas: catálogo no prueba acceso. Verificar modo local/uso permitido/lifecycle y términos actualizados; documentación nativa no autoriza un servicio hosted/comercial. No copiar limits/tools/refresh entre rutas. No leer/exportar tokens para probarlo.

## Regla de avance

Registrar `AVAILABLE_IN_RESEARCH_ENVIRONMENT` y `AVAILABLE_IN_TARGET_PLUS` por capacidad/subcapacidad. Un fallo temporal se investiga antes de concluir `NO`; un permiso desconocido sigue `UNKNOWN`. No usar la cuenta Team como reemplazo del gate. Si Plus no es suficiente, comparar rediseño/carga Tier 0/1 y alternativa paga con calidad/coste/valor por fase; llevar gasto concreto al propietario. D-024 requiere además madurez global R-006, revisión crítica y gobierno humano; este gate por sí solo no descongela agentes ni implementación.

**Dependencia:** pruebas conductuales Team → shortlist condicional → este gate para finalistas → propuesta de selección/gobierno. No exigir GP-1–7 para iniciar comparación o presentar shortlist. Una cuota insuficiente puede limitar la cadencia agéntica sin detener necesariamente un núcleo local determinístico; esa alternativa permanece abierta. GP-5/6 deben valorar research, shadow y pedagogía intermitentes y distinguir fallos de agentes de incidentes financieros materiales (ADR-002). No presume continuidad desatendida ni disponibilidad Plus.

## Cohorte propuesta de aceptación — 2026-10-05

[Shortlist RC1](R-006_shortlist_RC1.md) propone C-010 baseline, familia C-025a/C-029 transporte oficial mínimo y cuatro procedimientos research/quant/shadow/pedagogía. SDK Python se probó con un smoke Team, no todas las Skills/tools. MCP/Data reservas solo si necesidad concreta. GP1–7 OPEN/PARTIAL target. No convertir mock restart en recovery real ni gate Plus en validación de estrategia/seguridad/DoD pedagógico. C-025b SIWC OAuth permanece reserva documental, requiere gate propio si se justifica como finalista.

### Secuencia ejecutable cuando el propietario habilite Plus

1. Identificar cuenta/superficie y registrar versión/plan sanitizados; confirmar que no se usa Team o API key. No cambiar login de esta sesión automáticamente.
2. Elegir ruta activa de la familia según tools/caller/jobs necesarios; SDK si cubre contrato, app-server por gaps documentados. No duplicar toda la matriz entre wrappers del mismo backend.
3. GP2–4: cuatro smoke de Skills/caller/estructura/tools necesarios y negativos solo del delta de entorno; source/fixture/Skill/schema pins. Si modelo/version difiere materialmente, regresión focalizada con baseline.
4. GP5: rehidratar snapshot tras restart, auth/quota/tool fail controlados, outputs late/no-output/duplicate, sin broker ni credenciales; acción sensible sobre auth del dueño requiere su participación.
5. GP6–7: corpus/carga WL-R/ventanas, uso interactivo/reset observables, suficiencia y operación legítima sin gasto; si no alcanza, paquete de alternativas/coste antes de pedir pago.
6. Persistir/commit/push resultados y fallos; revisión crítica/seguridad y decisión final humana D-020/D-024. No abrir implementación.

## Nuevo gate de portabilidad — RC3 / ADR-009

Cohorte RC1 aprobada para aceptación, no selección. [Bootstrap EB1–8](../07_environment_bootstrap_contract_RC0.md) y [packaging](../07_agent_packaging_contract_RC0.md) son prerrequisitos D-024/DoR. GP1–7 se ejecutan desde clone/manifest/perfil de entorno con raíz+rol verificados, assets/versiones sellados, actions y readiness sanitizados. Team aporta evidencia conducta/discovery; Plus target permanece UNKNOWN.

GP2/4 comprueban root/cwd/overrides/Skill/allowlists en superficie elegida; GP5 añade lifecycle/cleanup de procesos y replay de perfil sin duplicar configuración/admisión. GP6/7 mantienen ventana/cuotas y operación legítima. Los cinco smoke R-028 no prueban GP target; cleanup TEMP WinError 32 se conserva como caso lifecycle pendiente. No repetir todo R-006, solo deltas relevantes.

[ONBOARDING](../../ONBOARDING.md) es entry point; no cambiar auth de Team ni copiarla. Preparación agéntica parcial sin inferencia puede continuar con inventario local. READY_AGENT_ENVIRONMENT no equivale a READY_FOR_IMPLEMENTATION/PAPER/LIVE.

**R-028 fresh clone — evidencia reutilizable:** seis cadenas de instrucciones/Skill común y dos smoke de rol desde commit 9e0dbed en CLI Team; hash Git distingue 31 EOL changes. GP2 verifica solo diferencias en la superficie Plus seleccionada, incluyendo desktop/SDK si relevantes. GP5 lifecycle recoge cleanup Windows observado. No usar profile PARTIAL de investigación como aceptación target. Paquete autónomo completo; siguiente requisito acceso Plus.
