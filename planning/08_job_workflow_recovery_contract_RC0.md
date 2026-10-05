# 08 — workflow, scheduler y recovery de jobs RC0

2026-10-05. D-025/R-011 **RESEARCHING**, D-024 abierto. Contrato candidato tecnológico independiente; implementaciones bloqueadas. ADR-011 exige invocación automática por eventos/calendario, sin aprobación por job rutinario.

## 1. Identidad y disparadores

Regla de trigger versionada fija evento/schedule, rol, snapshot, plazo, prioridad y política de fallo. `job_id` deriva de trigger-version + event-id/schedule-slot + rol + snapshot-id + contract-version; duplicado del evento conserva mismo job, cambio semántico requiere nueva identidad. `attempt_id` distinto por intento; manifest inmutable no lo elige el modelo. Slots con calendario/zone/UTC, DST y cierre/missing schedule explícitos; recuperar missed slots sin inventar observaciones disponibles antes.

Evento financiero y marcador durable de dispatch se registran atómicamente en fuente autorizada o mediante outbox reconciliable. Si se pierde notificación, reconciliador de eventos descubre job faltante; no crear backfill on-time retrospectivo. Schedules de shadow siguen cada evento de decisión requerido, con snapshot pareado sin output Champion visible antes de sellado. Prioridad/plazo del caller; cola acotada: no coalescer ni descartar snapshots obligatorios para pasar carga. Backpressure/missing/late visibles.

`environment_incarnation_id` es identidad confiable de la instancia en dispatch/AttemptManifest/lease/tool receipts/admission, diferente del fingerprint de configuración. **No forma parte de job_id lógico** ni sobrescribe el JobManifest original tras restore. Mantener creation epoch histórico; nuevo intento obtiene envelope con epoch actual. Antes de recibir un output comprobar epoch vigente junto a lease; una recepción de worker viejo no se admite. Outputs previamente admitidos siguen siendo evidencia histórica; no se revocan retroactivamente por reboot. Ver política de restore en [audit](08_audit_versions_deployment_contract_RC0.md).

## 2. Estados, retries y fencing

Separar `job_state` (QUEUED/RUNNING/SUCCEEDED/EXHAUSTED/CANCELLED), `attempt_state` (CREATED/RUNNING/COMPLETED/FAILED_TOOL/FAILED_RUNTIME/TIMEOUT/NO_OUTPUT/INTERRUPTED), `admission_state` (ACCEPTED_ON_TIME/REJECTED/LATE_RETROSPECTIVE_ONLY/DUPLICATE/STALE_ATTEMPT) y `content_status`. ABSTAIN puede ser contenido válido ante insuficiencia y no un éxito funcional con datos suficientes. Métricas cuentan cada eje y denominador.

Un lease con generación/fencing incrementada se asigna atómicamente por job. Debe validar también `current_attempt_id`, `lease_owner`, `lease_expires_at` y lifecycle admisible: no basta generación igual. Output vencido, cancelado/exhausted o de worker antiguo no se admite aunque siga vivo. Primer output **válido, del intento vigente con lease vivo, persistido y recibido antes del deadline** se elige mediante transacción/unique constraint; recepción repetida → DUPLICATE preservado. Verificar lease/lifecycle/clock y elegir output en la misma transacción; una cancelación concurrente se serializa en ese store. Deadline efectivo no se amplía por retry, excepción requiere nueva tarea/manifest marcada retrospectiva. Timestamp admisión/recepción del host, jamás claim del modelo; monotonic para elapsed en proceso, UTC persistido y drift de reloj detectado para restart.

No afirmar exactamente una ejecución del LLM: el caller puede repetir una inferencia tras crash. Garantía propuesta: **at-least-once attempts, máximo un output admitido por job**, autoridad financiera cero siempre. Resultado tardío/conflictivo se conserva sin sustituir el elegido. Crash después de guardar output y antes de ack produce relectura/dedup, no inferencia ni efectos financieros nuevos por defecto. Crash antes de evidencia durable produce estado de incertidumbre de intento y retry acotado si aún admisible. Uso de cuota duplicado posible y se contabiliza.

Política de errores: bounded retries/backoff versionados, techo attempts/deadline/recursos; transitorio elegible si no agota deadline; schema/PIT/permiso/hash/identidad mismatch no auto-repair privilegiado; auth revoked/config drift → circuit abierto y acción del owner; cuota → registrar rate-limit/reset cuando disponible, diferir tareas diferibles, no compra/cambio proveedor. Solo operador autorizado puede aprobar cambio material. LLM no decide retries, refresh secrets o reanudar core.

Valores finales de attempts/backoff/cola/circuit-breaker/plazos dependen de carga y Strategy V1; aún no aprobados. Una dependencia agéntica estratégica obligatoria necesita su propia regla determinística de fallo antes de selección. Ausencia no es HOLD; advisory no se transforma en mandatory por el scheduler.

## 3. Reconstrucción y límites de failure isolation

Fuente de verdad: release/manifest + snapshots/eligibility + tool trace + todos los outputs/veredictos. Native chat/thread resume es conveniencia, no estado financiero ni única recuperación. Rehidratar nueva sesión efímera desde evidencia; replay del admission usa versión original y no vuelve a consultar fuente mutable. Snapshot faltante/integridad rota bloquea job/admisión.

### Versionado de estados — aclaración de revisión independiente

`job_state` en la sección 2 es **workflow_state**, no reemplaza el `job_status` de [06 evidence](06_agent_evidence_contract_RC0.md). Especificación propuesta `delivery-contract-v2`: se preservan estados canónicos anteriores y se agrega `RUNTIME_FAILED` (antes no tenía representación); attempts/lifecycle son ejes internos adicionales. Evidencia/probes v1 conservan sus enums, no se reescriben. Consumers deberán declarar versión y rechazar estados desconocidos.

| Estado interno | Proyección canónica de evidence / admission |
|---|---|
| workflow QUEUED/RUNNING/SUCCEEDED/CANCELLED | job_status homónimo; SUCCEEDED es transporte, no éxito funcional/admisión/resultado financiero |
| workflow EXHAUSTED | job_status de causa final observada (TOOL_FAILED/AUTH_BLOCKED/QUOTA_BLOCKED/TIMED_OUT/NO_OUTPUT/RUNTIME_FAILED), más workflow_state=EXHAUSTED |
| attempt FAILED_TOOL/FAILED_RUNTIME/TIMEOUT/NO_OUTPUT/INTERRUPTED | TOOL_FAILED/RUNTIME_FAILED/TIMED_OUT/NO_OUTPUT/CANCELLED, con causa y attempt original preservados |
| attempt COMPLETED | SUCCEEDED de transporte, admission separado |
| REJECTED interno | reason code exacto REJECTED_SCHEMA/ROLE/PIT/LINEAGE/AUTHORITY existentes, o nuevos REJECTED_IDENTITY/SNAPSHOT/LEASE/LIFECYCLE; nunca perder motivo en un REJECTED genérico |
| STALE_ATTEMPT | REJECTED_LEASE, con stale generation/current attempt/expiry como razón |
| ACCEPTED_ON_TIME/LATE_RETROSPECTIVE_ONLY/DUPLICATE | estados canónicos homónimos; UNPAIRED de v1 sigue disponible |

`content_status` y clases Shadow/Pedagogical no cambian. Exhausted/missing no se proyecta a HOLD/ABSTAIN por inferencia. Este mapping es especificación de planificación, no schema productivo seleccionado.

Fallo de job se aísla del core conforme A+/G1+G2; no nueva aprobación por operación válida ni salida financiera por falta de pedagogía. Incertidumbre de posiciones/protección/inputs financieros sigue su política material. Falta persistente de shadow/report hace fallar aceptación PAPER, aunque no otorgue autoridad para operar. El gate de readiness agéntico tampoco reanuda una pausa financiera.

## 4. Reutilización antes de construir

| Motor | Qué reutiliza | Gap / coste / estado |
|---|---|---|
| **Temporal self-hosted** (candidato del roadmap) | Historia/replay durable, schedules/timers/Activities/retries | CLI público MIT verificado v1.9.1; licencia/deps del artefacto server final se fijarán. Software local sin cuota SaaS, setup/operación/hardware por medir. LLM en Activity; retries default ilimitados deben acotarse. Probar server durable/versiones; no usar start-dev como aprobación producción |
| APScheduler 3.x + store/outbox autorizado | Triggers calendarios y persistencia básica, OSS MIT | No compartir jobstore entre procesos según FAQ 3.x; no aporta por sí solo fencing/recepción/audit durable. Master 4.x diferente no inferir estable. ADAPT candidato simple, no seleccionado |
| Scheduler OS + DB/outbox | Autostart/event/calendar disponible, DB durable | Requiere recovery de jobs propio más amplio; REFERENCE_ONLY hasta necesidad/benchmark. No BUILD motor durable desde cero sin gap probado |

Preferencia provisional: ensayar Temporal original antes de sustituirlo; el ledger SQLite H1/H2 solo prueba semántica, no selecciona motor/store. [Temporal self-host](https://docs.temporal.io/self-hosted-guide), [retries](https://docs.temporal.io/encyclopedia/retry-policies), [APScheduler 3.x FAQ](https://apscheduler.readthedocs.io/en/3.x/faq.html). Capa workflow determinística fuera del límite de frameworks IA OpenAI/Anthropic.

P1: elección motor con deployment compatible con aislamiento, finitud/identidades/estados/retención especificados y probe de restart de motor candidato antes de cierre D-025; reviewer. P2: workflow/core integrado con crashes en cada boundary, disconnect, quota/auth, leases y rollback; contar todos los outputs. D-025 permanece abierto a investigación: no selección por documentación.

## S2 — launch, lifecycle y capacidad

[S2 RC1](08_S2_isolation_spec_RC1.md): launcher/workflow/collector confiables C fuera del proceso/modelo; no broker credentials. Job identity/runtime completa en R/S/P, no task que hereda token de desarrollo. Credencial de lanzamiento y logon rights mínimos requieren gate administrativo específico, no permiso implícito del scheduler. Reuse [Windows Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects) candidato para controlar descendientes/cleanup/recursos; comprobar breakaway/WMI/nesting y permisos de cada proceso, no confundir job object con sandbox. Wrapper no expone process/* al modelo.

Antes del gate de carga nativa: incluir serialización/revocación de vistas cuando jobs comparten SID y pruebas de reuso/caches (SI-16/BL-06). Concurrencia insegura no demuestra TP-6. Cambio de tokens/policy/epoch exige relanzar proceso y revalidar footprint, no reciclar worker privilegiado. Reboot/restore conserva históricos/receipt, invalida attempts antiguos según epoch; no reanuda core pausado. Próximas pruebas con identidades requieren ADM-01/02/03; no servicio/task Windows instalado por este contrato.

**Persistencia SID:** cleanup del export/kill de procesos no borra copias guardadas en perfil/cache/TEMP. SI-16/BL-06 obliga canary→relaunch bajo frontera que impida estado excluido; survivors (auth y research reexportado permitido) versionados. No aceptar serialización como prueba única de blinding/cross-job isolation ni cerrar RB-02 sin ese caso.
