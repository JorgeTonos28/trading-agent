# Q-063 — workflow y persistencia PAPER: propuesta de stack

2026-10-28. **READY_FOR_DECISION de dirección**, propietario; D-025/D-026 aún RESEARCHING. No seleccionado por redactarlo. No reabre B-RT1 ni cambia autoridad, permisos o target. Recomendación material porque cambia la huella operacional respecto del candidato Temporal del roadmap.

## A — recomendado: APScheduler3.x acotado + PostgreSQL

Un scheduler confiable en C, calendario/wakeups de APScheduler; PostgreSQL para ledger C y store F con principales/DB/permisos separados; snapshots/artefactos locales versionados con Parquet/DuckDB analíticos. No Redis ni Temporal obligatorios para PAPER inicial. Redis/Temporal permanecen reservas y LIVE se reevalúa por valor, no precio cero.

APScheduler **no** es el workflow durable. Registros de due jobs, manifest, outbox, attempts, leases/fencing, deadlines, veredictos/receipts son autoridad de ledger C. Triggers/callables están fijados por código/config confiables; no aceptar pickle/callable/path/import generado por modelo. Scheduler en memoria reconstruye wakeups desde reglas y due-state persistidos; perder una notificación no pierde el job. Escanear tras restart no convierte un missed job en on-time. Un único scheduler propietario, sin compartir jobstore entre procesos.

PAPER necesita procedimientos/versiones finitos ya aprobados, no DAGs arbitrarios ni workflow authoring por agentes. Se reutilizan calendario/DB/transacciones y contratos existentes, no un framework general propio. F emite eventos/outbox; C recibe eventos con IDs/dedup y posee admission. No transacción distribuida C/F ficticia: cada outbox es atómico con su fuente y la entrega es reconciliable/at-least-once. Un actor C nunca escribe estado financiero ni comparte credenciales de F.

## B — conservar Temporal self-hosted + PostgreSQL

Reutiliza historia/replay/timers/Activities/retries y workflows durables, con mayor servicio/configuración/upgrade a operar. El ledger/admission C sigue requerido: un retry de Activity no es exactamente un output o efecto. `start-dev`/SQLite embedded no es fallback operacional de PAPER; [Temporal lo limita a desarrollo/pruebas](https://docs.temporal.io/self-hosted-guide/embedded-server). Despliegue sostenido exige servicio/persistencia/endurecimiento adecuados. Ruta nativa Windows de producción **no verificada**, no se declara imposible ni se impone Docker/WSL/VM. Toda dependencia adicional necesita evidencia y gate antes de configuración.

| Criterio | A: APS + PostgreSQL | B: Temporal + PostgreSQL |
|---|---|---|
| Reuse | Calendario/cron y DB; ledger C ya requerido para admisión | Workflow/history/retry nativos, más ledger C |
| Recovery | State machine finita y outbox/reconciliador explícitos, más responsabilidad en C | Replay de workflow; handlers/receipts y efectos externos siguen explícitos |
| Huella | Un proceso scheduler confiable más DB; sin jobstore pickle externo | Servicio Temporal y configuración/upgrade/persistencia más workers/DB |
| Windows personal | Python/Postgres tienen rutas documentadas, aceptación target pendiente | Servicio operacional Windows no demostrado; alternativas de hosting no autorizadas |
| Complejidad | Menos servicios, pero no equivale automáticamente a menos ingeniería total | Más operación, menos maquinaria de workflow propia |
| Evolución | Reconsiderar si procedimientos se vuelven DAGs/durables complejos o failover múltiple | Mejor encaje para esa demanda si su coste/operación se justifican |

SQLite conserva papel de instrumento de laboratorio; no sustituye silenciosamente PostgreSQL. Redis no aporta necesidad medida que justifique autoridad/persistencia adicional; cache opcional no es ledger. PostgreSQL es elección propuesta de familia, **no versión/pin/configuración aceptados**, ni prueba de permisos/FSYNC por leer docs.

## Evidencia comparable y límites

H7 probó worker real Temporal que reejecuta Activity tras crash; H8 probó calendario persistido/restart/misfire de APS. No son workloads equivalentes ni un ranking por conteos. [H9](probes/r012-demand-ledger/README.md) usa SQLite DELETE/FULL como instrumento:1200 jobs/2400 propuestas con cuatro producers, dedup/job-outbox/receipts y backup. No fuerza colisión simultánea de la misma key; CAS/admisión son chequeos secuenciales, no prueba de carrera de receipts.13 expectativas+6 controles complementarios de copia restaurada.20.14s locales no prueban latencia operacional o capacidad Plus/target/PostgreSQL. Nueva incarnation no repara receipt perdido: hash aislado→RECOVERY_GAP y bloqueo, no job repetido.

SQLite3.50.4 observado está en el rango del [WAL-reset bug](https://www.sqlite.org/wal.html); H9 evita WAL. No se intentó reproducirlo ni certificar su fix. Probes previos conservan su ámbito histórico y no aceptan ese pin. Para cualquier futuro WAL se requiere versión corregida y regresión.

[APScheduler FAQ](https://apscheduler.readthedocs.io/en/3.x/faq.html) prohíbe compartir jobstore; [PostgreSQL Windows](https://www.postgresql.org/download/windows/) describe installer/zip, no instalación realizada aquí. [WAL/FSYNC](https://www.postgresql.org/docs/current/runtime-config-wal.html) define garantías condicionadas a configuración/hardware. Sólo docs para PostgreSQL, sin servidor/cuenta/puerto nuevos en INFOTEP.

## Gates, economía y decisión exacta

La aprobación solicitada sólo fija dirección condicionada de familias/huella. Según D1, antes de cerrar selección/configuración y suficiencia del stack para freeze deben fijarse y justificarse intensidades nominal/ráfaga/estrés, latencias, RPO/RTO y retención; siguen P1 de diseño, no se declaran resueltos ni se ocultan como sólo target. H9 no los mide para PAPER.

Antes de cerrar P1: versión/licencias/SBOM, driver y transacciones/constraints/rollback/roles, scheduler único, due-state/recovery/clock y bootstrap reproducibles; permisos C/F/J preservados; restore/audit/snapshot rights y criterios de fallo definidos. Target R-030 acepta instalación/configuración segura; integración/carga P2 separada. Ninguna aprobación de dirección pasa esos tests.

Ambos: PAPER_V1_VIABLE_FREE=CONDITIONAL; licencias OSS0, coste setup/hardware/backup/operación mensual totalUNKNOWN. LIVE_COSTUNKNOWN. FREE_ALTERNATIVE=la otra fila; PAID_INCREMENTAL_VALUE=continuidad/soporte si medidos; ECONOMIC_JUSTIFICATION_REQUIRED=YES. Lock-in A=contratos/SQL/persistencia de jobs; B=workflow history/determinismo/SDK/operación del server. Cinco escalas obligatorias y nada contratado.

**Decisión solicitada:** aprobar A como dirección de diseño PAPER de workflow/storage, manteniendo Temporal como reserva ante complejidad que lo justifique, y PostgreSQL con aislamiento de stores. Es simplificación de servicios, no eliminación de durabilidad. No autoriza instalar/configurar nada, gastar, aceptar target, ejecutar trading o implementar. Si el propietario prefiere B, concretar su despliegue sostenido antes de freeze; no usar dev server como atajo.
