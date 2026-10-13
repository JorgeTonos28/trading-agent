# R-011/012/014 — demanda financiera para workflow/storage/observabilidad — RC1

2026-10-13 · P1 D-025/026/028/029 y D-034 · Diseño transversal, **no expansión R-006/010/013**. ADR-014 arquitectura agéntica fundamental completa; mecanismos y aceptación host/Plus R-030 diferidos. No engine/store/cadencia/SLO seleccionados ni instalación/implementación.

## Unidades de demanda y propietarios

| Flujo | Unidad/trigger y estado durable | Demanda por determinar con Strategy/data | Fallo y evidencia |
|---|---|---|---|
| Market data | Barra/quote/evento corporate + clocks/version + ingest eligibility | N_assets, granularity, sessions, actual latency/revisions/bursts | Datos obligatorios stale/unknown bloquean nueva exposición; raw/revision snapshots sin reescribir pasado |
| Filings externos | Documento/versión/fila/entity mapping y canal availability | Eventos EOD, amendments/joint owners/normalización/export bytes | No receipt futuro retrospectivo ni compra por fecha de operación; quarantine/retry bounded/cached |
| Señal/intent determinístico | Decision slot + config/data/portfolio snapshot, filtro/rank/razón, target deltas | N_candidates durante research, Champion único inicial, posiciones/lotes y órdenes concurrentes | Misma identidad/versión; nueva aprobación Risk ante cambio, sin interpretación LLM operativa |
| Reservas/Risk | Claims exclusivos/authorizations/generations y validación de estado | Frecuencia por intent/reprice/recovery y límite concurrente | Transactional constraint/CAS/outbox, no cash esperado de salida ni claim doble; D-035 propuesta pendiente |
| Orden/fill/protección | Broker lifecycle/event/reconciliation, client/server IDs y attempts | Eventos streaming/polls/session/order rates/cancel/partial/replace | UNKNOWN no retry con nuevoID, G1+G2, protección preservada y humano tras material pause |
| Shadow/Quant/Ped | Jobs/snapshots/admission/lineage versionados ADR-014 | Decision slots/bursts, tamaño payload, latency/deadline/quota compartida | No-output ≠ HOLD; paired context no Champion contemporáneo; explanation desde hechos posteriores autorizados |

## Comparación de motores y stores: criterio de elección

R-011 elige motor determinístico bajo contratos ya aprobados; [comparación anterior](R-010_workflow_storage_comparison_RC1.md) y H7/H8 preservados como semánticas diferentes. EOD calendar alone no da retry/leases/fencing/admission; añadir explícitamente ledger confiable/outbox, no middleware agéntico. Temporal candidate implica servicio/ops y deployment coste; APS candidate implica desarrollar controles faltantes WRAP/ADAPT, coste de esa integración por medir. No llamar0al coste de cualquiera porque licencia OSS.

R-012 separa ledger/event state financiero F, jobs/admission/audit C y analytical snapshots. PostgreSQL/SQLite transaccionales candidatos, Parquet/DuckDB analíticos; Redis opcional, no authority de presupuesto/receipt. Elección debe demostrar atomicidad requerida dentro de cada dominio y reconciliación/outbox entre dominios, backups/incarnation/restore/lostreceipts. Agentes sin acceso SQL/write financiero. Reserva aceptada pero persistencia outbox fallida no autoriza envío; receipt externo no implica snapshot financiero correcto.

Estimación documental de carga: `bars=N_assets*N_sessions*bars_per_session`, `events=publications+amendments+broker_events`, `agent_jobs=required_decision_slots*roles_at_slot+research_jobs`, `storage=sum(raw_bytes+revision_bytes+trace_bytes+attempt_bytes)*retention` antes de compresión. No usar promedios como peor burst; medir tail, retries y sesiones de outages. Retención depende licencia/privacy/economía y audit de fuente/versiones, no número arbitrario. WL-R sintético anterior no se convierte en ritmo real de estrategia.

## Observabilidad financiera y runbooks pendientes

- Dataset: recepción vs event/publication/eligibility, stale/missing/correcciones, drop/retry y quarantines, source quality y derechos vigentes.
- Órdenes/protección: accepted/unknown/partial/cancel/replace/fill timestamps, cobertura q real, stop desired vs confirmed, riesgo/gap y cash/reservas reconciliados, mismatch observado.
- Estado riesgo: exposición, mark-to-protection propuesto vs entry attribution, buffers/scenarios/limits/version y motivos; UNKNOWN fuera de ratios calculados, no cero.
- Jobs: queued/attempt/late/no-output/accepted y cobertura funcional con denominadores; failed/abstain no éxito pedagógico por parser PASS. Observabilidad/límites no otorgan autoridad alternativa.
- Runbooks: disconnect/feedstale/missingprotection/doublefill/DBunavailable/corruptsnapshot/restore/quotas; controles verificables antes de reanudar y owner tras incidente material, sin G3.

SLO/RTO/RPO/deadlines/retries/alerts/cadencias y costes se eligen con demanda/horario de protección, no se aprueban aquí. R-030 ejecuta host/runtime acceptance; pruebas operacionales financieras/reconciliation/carga prolongada después del sistema construido P2. Protocolos y finales de diseño P1 siguen trabajo financiero Team, no diseño agéntico reabierto.

## Protocolo siguiente antes de selección técnica

DatasetCard+CandidateConfig completos → unidades/burst/retención y failure contracts → matrices engine/store cost/exit/mappings → fixtures de atomicidad/recovery/paridad/corporateactions fuera de mercados reales → revisión crítica → decisiones técnicas/gobierno según materialidad → target+DoR. Risk measurement owner Q-054 es gobierno material de sizing; no seleccionar sus valores mediante workload benchmark.
