# D1 — demanda financiera para workflow/storage/evals

2026-10-23. Contrato de dimensionamiento propuesto desde EQ3/RiskRC3, no workload medido, SLA aprobado ni motor seleccionado. Complementa [comparación existente](R-010_workflow_storage_comparison_RC1.md), sin reabrir arquitectura agéntica. Ninguna instalación/servicio/daemon/implementación.

## Demanda derivada, no cifras de operación inventadas

- Universo de investigación seisETF; elegibilidad diaria, MATR ranking semanal, PRICE eventos diarios y actualización protectora desde barras admitidas. Máximo tres securities ocupando ranuras, pero **no máximo tres órdenes/eventos**: parciales, remainder, stops, replace, callbacks y reconciliaciones multiplican eventos.
- Núcleo de riesgo/reconciliación/protección procesa eventos broker/mercado según sus clocks y cadencia exigida; daily signals no autorizan polling diario de órdenes ni horas sin supervisión. Streaming/recovery/staleness específicos dependen de broker/fuente y D031.
- Research/Quant/Shadow/Pedagogical son jobs automáticos según evento/agenda aprobados, con deadline/expiry/late/no-output; no requerir aprobación por job. Shadow usa snapshot mínimo pareado, sin Champion contemporáneo excluido. Fallo Codex no crea señal financiera/HOLD por defecto.
- Aproximación de volumen para diseño:6×sesiones del calendario validado×versiones de fuentes/filas; factores de revisión, quotes, eventos, intentos, logs y retención se declaran separadamente. No convertir aproximadamente33k barras diarias en tamaño total de audit ni justificar Redis/cluster por ese cálculo.

## Matriz de carga/recovery a fijar antes del benchmark

| Eje | Workload/negativo obligatorio | Aceptación de contrato |
|---|---|---|
| Reloj/agenda | Holiday/DST/early-close, cierre semanal, market halt; tick de agenda repetido o perdido | Calendario/versiones y deadlines causales; nada de fila faltante=feriado; no doble receipt |
| Broker/eventos | Burst de parciales/replace/cancel/fill/corrección; ejecución tras timeout | Lifecycle/qty/claims separados, orden causal y dedupe con mapping; UNKNOWN conserva obligaciones |
| Concurrencia | Dos intents compiten por mismo cash/R2; varios jobs/attempts y lease viejo | Compare-and-commit/epoch/version; ninguna suma de autorizaciones supera presupuesto por race; modelo sin SQL/credenciales financieras |
| Fallo | Crash antes/después de commit/dispatch/ack/receipt; outbox pendiente | Reconciliar sin resend financiero ciego; at-least-once workflow no se llama exactly-once effect |
| Restore | Backup anterior con broker más avanzado y leases viejos | Nueva incarnation/epoch, reconciliación y pausa material; no replay automático de órdenes |
| Datos/audit | Import/revisión/snapshot/export concurrente con eventos críticos; disco lleno y retención contractual | Inmutabilidad/linaje, cuotas de almacenamiento y fail-closed; analítica separada de writer crítico, no borrado contractual silencioso |
| Agentes | Todos deadlines simultáneos, timeout/cuota/late, output malformado o replay | Preservar admisión externa/límites, no bloquear protección del núcleo; carga sostenida Plus es R030/P2, no Team acceptance |

Las intensidades nominal/ráfaga/estrés, latencias aceptables, RPO/RTO y retención final se vinculan a broker/datos/estrategia/costes antes de seleccionar stack; hoy UNKNOWN donde falta evidencia. Medir tiempo/bytes/CPU/RAM y tasas/dedupe/latencia por etapa; no sólo throughput medio. Sin criterio numérico previo, un benchmark no recibe PASS de suficiencia operacional.

## Implicaciones Build-vs-Reuse

Temporal conserva ventaja de workflow durable ya observada; APScheduler sólo agenda y exige ledger adicional. PostgreSQL candidato transaccional, SQLite alternativa local requiere writer/durabilidad/restore adecuados; Parquet/DuckDB para snapshots/lectura, no autoridad de órdenes. Redis sigue reserva opcional. Reutilizar receipt/outbox/transacciones/backup existentes antes de construir scheduler/DB general. [H7/H8](R-010_workflow_storage_comparison_RC1.md) no prueban workload D1 ni aislamiento.

PAPER_V1_VIABLE_FREE=CONDITIONAL; adquisición OSS0 donde aplicable, operación/setup/backup/hardware y mensual total UNKNOWN. LIVE_COST UNKNOWN; FREE_ALTERNATIVE las rutas comparadas; PAID_INCREMENTAL_VALUE continuidad/soporte sólo si medidos; ECONOMIC_JUSTIFICATION_REQUIRED=YES. Coste de configuración/lock-in/restore importa aunque licencia sea gratuita; modelos de coste en las cinco escalas obligatorias. No escoger stack por performance financiera ni usar base provisional como arquitectura aceptada.

## Aclaración de alcance incluida en Q-063 — 2026-10-28

El requisito anterior de fijar intensidades/latencias/RPO/RTO/retención antes de seleccionar stack se mantiene para cerrar selección/configuración y suficiencia antes de freeze. [Q-063](D-025_026_PAPER_workflow_storage_decision_RC0.md) solicita ahora sólo dirección de familias/huella condicionada, no declara ese cierre. Esta distinción queda incluida explícitamente en el paquete de gobierno; no se certifica viabilidad operacional por elegir familias ni por H9. El envelope numérico, modelos/fallos/configuración y evidencia de suficiencia siguen P1. No se trasladan a un P2 genérico o sólo al host para aparentar DoR. El roadmap Temporal sigue antecedente candidato, no decisión sustituida automáticamente.
