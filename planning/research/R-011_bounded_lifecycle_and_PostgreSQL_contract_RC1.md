# PAPER — lifecycle finito, PostgreSQL y recuperación RC1

2026-10-29. Detalla ADR-024; **DESIGN_SPECIFICATION_CANDIDATE / POSTGRESQL_NOT_TESTED**. No runtime, SQL productivo, servicios, cuentas, configuración o permisos nuevos. Contratos de autoridad B-RT1/A+/G1+G2 preservados.

## Alcance que evita un motor de workflow general

Un job contiene un procedimiento aprobado, un snapshot inmutable y un deadline original. No DAG, subworkflow recursivo, branching definido por modelo, compensation framework, migración de historia o active-active. Seis transacciones C: materializar job+outbox; claim/attempt/lease; registrar dispatch; registrar output sellado; validar/admitir receipt; terminalizar por fallo/deadline. Cada una es idempotente respecto de sus identidades y versión esperada. Crash no crea otra identidad lógica.

Escalar a comparación Temporal antes de ampliar si aparece cualquiera: workflows anidados/dinámicos, compensaciones entre efectos financieros, múltiples schedulers activos/failover automático, migración/replay de código histórico, estado dependiente de ejecución de modelos, o recovery que no pueda expresarse por estas transacciones y tablas de casos. Ningún contador arbitrario de líneas decide la selección: revisar coste de ingeniería, pruebas, operación y seguridad de ambas rutas con el caso real. Estos disparadores son límites de diseño, no rechazo automático de ADR-024.

## Ownership y datos durables

| Store/actor confiable | Autoridad y registros | Acceso que se niega |
|---|---|---|
| F / Risk y Execution | version de cartera/reservas, autorizaciones/commands, broker mapping, fills/correcciones, outbox F, pausas y auditoría financiera | C y jobs no escriben ni leen secretos/estado excluido |
| C / supervisor y admission | reglas/slots, jobs, manifests, attempts, deadlines, outbox C, leases/generaciones/epochs, outputs/veredictos/receipts y enlaces de evidencia | Jobs no tienen SQL/rol/token de DB; scheduler no modifica autoridad financiera |
| Reader analítico autorizado | exports mínimos versionados a Parquet/DuckDB según licencia/blinding | Ningún writeback a F/C ni acceso implícito al servidor SQL |
| Administrador del propietario | instalación, roles, backups y recovery según gate | No credencial de administración en runtime/job/Git |

Diseño inicial de una instancia PostgreSQL con databases C/F y principales separados es candidato, no prueba de aislamiento. Revocar acceso público por defecto; sin superuser, CREATEDB, CREATEROLE, BYPASSRLS, membership/SET ROLE cruzado, extensiones/FDW/dblink/COPY PROGRAM o funciones peligrosas desde runtime. Owner/migration roles separados de escritores; search_path y ejecución de funciones explícitos. RLS no basta: [owners/superusers pueden eludirla](https://www.postgresql.org/docs/current/ddl-rowsecurity.html). Verificar catálogo/permisos efectivos y pruebas negativas desde cada principal y desde Agent Runner; conexión denegada por rol tampoco prueba aislamiento OS de credenciales. R030 sigue requerido.

No transacción distribuida F/C: F persiste evento+outbox en su commit; import C deduplica y reconoce sólo después de su commit. IDs/envelopes autorizados; C puede pedir una exportación permitida, no ejecutar SQL arbitrario contra F. La salida del LLM nunca es una orden, ni un receipt C es autorización financiera.

## Agenda y admisión

APScheduler usa MemoryJobStore para wakeups confiables regenerables. Las reglas versionadas y el watermark de materialización viven en C: al arrancar, enumerar slots vencidos hasta ahora y materializarlos con unique key; slots perdidos conservan deadline y estado MISSED/LATE. No guardar pickle del modelo ni import/callable/path configurable desde un output. Un único scheduler propietario; ownership DB cercado y nueva generación no demuestran por sí solos que el proceso viejo murió: todo write/dispatch verifica generación y lifecycle vigentes. No se comparte jobstore APS entre procesos.

Las transacciones de claim/admission comprueban juntos job, attempt vigente, lease_owner, fencing, epoch, deadline, cancelación y hash/versión del snapshot. Una constraint UNIQUE(job_id) para receipt admitido resuelve colisión, no valida contenido ni instante por sí sola. Contenido inválido/late se conserva aparte. Retry del LLM puede repetir cálculo, nunca revivir deadline. Después de output durable, recuperar/dedup antes de inferir de nuevo; no-output no es HOLD. Bloqueo o rollback de DB no produce éxito ni ack prematuro.

## Tabla de crash/recovery que se debe validar

| Corte/fallo | Evidencia durable posible | Acción permitida y prohibición |
|---|---|---|
| Antes de commit job/outbox | Ninguno de ambos | Redescubrir slot/evento; no dispatch desde memoria |
| Después de commit, notificación perdida | Job+outbox, sin wakeup | Scanner reconstruye; identidad/deadline originales |
| Después de claim, antes de dispatch | Attempt/lease sin entrega | Marcar interrupción o recuperar con fencing; no dos attempts vigentes |
| Dispatch con ack perdido | Inferencia posiblemente iniciada | Consultar/reconstruir attempt; repetición acotada consume cuota, máximo un output admitido |
| Output escrito, receipt no commit | Blob quizá huérfano o staged | Hash/manifest/lease/deadline y transacción de admisión; no éxito por existencia del archivo |
| Receipt commit, ack perdido | Receipt histórico ya seleccionado | Releer mismo receipt; no nueva inferencia o ganador |
| Cancel/deadline y admisión concurrentes | Orden serial de commits | Un veredicto compatible; late nunca on-time retrospectivo |
| Lease viejo, reloj atrasado, restart | Generación/epoch/clock inciertos | Cercar/quarantine; monotonic sólo local, UTC/clock drift validado al restart |
| F commit antes de envío broker | Command/outbox sin ack | Consultar evidencia; enviar sólo si se demuestra no despachado y sigue autorizado |
| Broker recibe, respuesta/DB caen | Efecto externo UNKNOWN | Reconciliar IDs/orders/activities/positions; jamás resend ciego, ni exactly-once por SQL |
| Restore anterior a receipt/orden | Backup menor que evidencia externa | Nueva incarnation + RECOVERY_GAP, comparar anchors/historia/broker; humano tras incidente material |
| Escritura/commit/disco/WAL/backup fallan | Garantía desconocida | No ack/dispatch nuevo; G1, G2 sólo si puede registrarse/ejecutarse con estado confiable; proteger lo ya vigente |

El scanner de recuperación es una consulta del lifecycle finito; no reconstruye resultados desconocidos desde un hash. Backlog guarda cada job requerido y su resultado factual, no se coalescen snapshots Shadow para ocultar insuficiencia.

## Durabilidad y backups — configuración candidata

Familia PostgreSQL estable soportada; versión exacta/driver/pin/SBOM/config se aceptarán antes de freeze/uso. C/F críticos usan tablas logged, `fsync=on`, `full_page_writes=on`, `synchronous_commit=on`; no RAM-disk ni settings de import que alteren garantía del store operativo. Verificar config efectiva por sesión/rol; [PostgreSQL documenta pérdida de transacciones sin commit síncrono](https://www.postgresql.org/docs/current/non-durability.html). Eso no garantiza disco/controlador/energía ni supervivencia a pérdida total de disco.

Backups físicos/base + archivo continuo WAL para PITR son candidatos de reutilización; `pg_dump` es export lógico, **no base para WAL replay** ([documentación](https://www.postgresql.org/docs/current/continuous-archiving.html)). Verificar backup, cadena WAL, timeline, copia externa al disco de origen y restauración real, no sólo exit0 del comando. Snapshots/blobs requieren conjunto coherente con DB y derechos de retención; no borrar evidencia mientras un backup incompleto la referencie. Medir bytes/crecimiento/WAL/disco libre; bloquear admisiones/entradas afectadas ante insuficiencia. No compresión, cifrado o réplica se dan por instalados.

El [envelope D2](R-010_workload_and_durability_envelope_RC1.json) fija propuestas numéricas de ingeniería antes de pruebas. RPO de commit reconocido tras crash local y RPO de desastre son distintos. Restore se considera terminado para diagnóstico en PAUSED, no permiso de trading: RTO nunca promete reanudación automática/humana en un plazo.

## Acceptance restante

P1 diseño: schema/constraints/txns, matriz permisos, configuración/pins, medidas/denominadores y D2 con revisión/suficiencia. P1 target: instalar/configurar bajo gate y comprobar binarios/roles/config/secretos/fresh clone; ninguna instalación aquí. P2 integrado: inyección segura de fallos en cada corte, aislamiento/backup/restore/ledger avanzado-broker, carga nominal/ráfaga/degradada, pérdidas de conectividad y disco, sin riesgo de operar sobre target LIVE. PASS requiere evidencia sobre PostgreSQL real; fixtures H9/H10 no lo sustituyen.

Costes adquisición OSS0 en cinco escalas; hardware/backup/operación y mensual total UNKNOWN. No licencia cero=coste cero. LIVE se reevalúa; Temporal reserva, sin servicio premium/Redis obligatorio. No SLO de protección/orden se deduce de latencia SQL.
