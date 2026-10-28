# R-008 — Market Data: marco de comparación y economía por fase

**Baseline:** 2026-10-02. **Actualizado:** 2026-10-07. **Estado:** `RESEARCHING`, P1/D-022. [Wave 01](R-007_008_provider_evidence_wave01_2026-10-07.md) actualiza evidencia y economía broker-native; demás fichas pendientes, ningún proveedor elegido. La selección debe satisfacer ADR-004 y las necesidades de candidatos Strategy V1, sin cambiar período/universo ni permitir look-ahead por conveniencia del plan gratuito.

Comparar cobertura histórica/activos/delistings/corporate actions, ajustes/revisiones as-of, timestamps/publicación, granularidad, streaming/backfill, latencia/availability, rate limits, licencia para automatización/backtest/almacenamiento, calidad cruzada y recuperación. Documentar diferencias entre feed paper y live; muestras oficiales cuando sea viable antes de selección.

## Scorecard económico inicial

PAPER: included/free/local-first con calidad suficiente. LIVE: valor económico, fiabilidad y latencia medidos frente a alternativas. Aplicar [ficha común ADR-008](../economic_scorecard.md): fijo/variable/mensual/escala, derechos exchange/non-display si aplican, backfill/add-ons y licencias, integración, lock-in, beneficio y condición para pagar. Investigar opciones pagas está autorizado; contratación/gasto requiere aprobación. Estos candidatos proceden del backlog; ninguna fila confirma oferta gratuita, producto o precio actual.

| Candidato | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Broker-native feeds | UNKNOWN broker/cuenta/feed | UNKNOWN | UNKNOWN | Feeds de otros brokers por probar | Paridad/reconciliación/cobertura/latencia a medir | YES si gasto |
| Databento | UNKNOWN | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Fidelidad/coverage/latencia a demostrar | YES si gasto |
| Massive | UNKNOWN | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Histórico/revisiones/streaming a demostrar | YES si gasto |
| Nasdaq Data Link | UNKNOWN dataset | UNKNOWN | UNKNOWN | Fuente pública del dataset si existe | Calidad/licencia/cobertura a demostrar | YES si gasto |
| Tiingo | UNKNOWN | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Ajustes/history/continuidad a demostrar | YES si gasto |
| Alpha Vantage | UNKNOWN límites/licencia | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Límites/latencia/cobertura a demostrar | YES si gasto |

Todo candidato adicional completa estos campos y dimensiones funcionales antes de preselección. Precios/mensuales permanecen `UNKNOWN` hasta fuente/cotización fechada y escenario de carga; no inventar equivalencia de calidad entre planes gratis y pagos.

## Evidencia y demanda vigente — 2026-10-07

Las filas anteriores son inventario inicial fechado. [Wave broker/data](R-007_008_provider_evidence_wave01_2026-10-07.md) conserva precios documentados y gaps: IEX realtime, SIP histórico retrasado y fill paper NBBO tienen semánticas distintas; pin explícito feed/cobertura/clock, sin transferir paridad. Historia anunciada desde2016 deja sin resolver propuesta MATR 2005–2015 y warm-up. No se cambia protocolo por conveniencia comercial.

[Demanda por candidato RC1](R-020_candidate_data_workload_contract_RC1.md) requiere corporate actions/as-of, raw y contabilidad de dividendos, universo histórico, granularidad de stops/gaps, derechos y validador secundario. No se descargó dataset de precios ni abrió una muestra reservada; calidad real y datasets admitidos UNKNOWN. Reuse de APIs/datasets antes de BUILD, sin selección, gasto o login target.

## Wave02 — 2026-10-13

[Evidencia/data economics](R-008_market_data_evidence_wave02_2026-10-13.md) actualiza Tiingo/Massive/Alpha Vantage con fuentes oficiales. Tiingo Starter merece primer coverage/rights probe por historia gratuita anunciada; no seleccionado. Free Massive/Alpha no resuelve ventanas2005+/warm-up por profundidad. Precios y horarios comerciales no demuestran PIT exacto. No cuentas/datasets/holdout ni gasto.

## Gate durable vigente — 2026-10-13

[R-008 retención RC1](R-008_data_retention_gate_RC1.md) reemplaza la prioridad histórica de Tiingo Starter: REJECT para pipeline persistente, PAPER_V1_VIABLE_FREE=NO en ese scope. Tiingo paid CONDITIONAL; no rechazo permanente ni permiso de gasto. Resto de alternativas gratuitas no certificadas ni descartadas. D-022 RESEARCHING; retención de raw, outputs y derived traces debe ser compatible con replay/auditoría, separando derechos de datos de registros broker propios.

## Evidencia temporal wave03 — 2026-10-14

[Timing/data/broker](R-007_008_timing_evidence_2026-10-14.md) verifica delayedhistoricalSIP/Basic y rutaIBKR auth/presets/cancelstates. Source/feed/deadline/coverage/rights y Riskfreshness separados, B1–5target aún NOT_TESTED. No broker/proveedor seleccionado ni cuenta/config/autenticación/data call. Rutas gratuitas no resuelven2005+ ni audit rights automáticamente.

## Referencia monetaria — wave05

[Referencia monetaria](R-008_cash_benchmark_admission_RC0.md) añade condiciones de semántica, disponibilidad histórica/PIT y costes; no admisión de fuente ni selección de proveedor. E3/F2 sólo fixtures/componentes; datos/historia/rights y target no probados. Las fuentes restantes conservan su prioridad/alcance, no exclusión general por este probe.

## Alternativas/rights adicionales — wave06

[Alternativas/rights adicionales](R-008_sources_evidence_wave03_2026-10-14.md) añade especificación y límites; Q057 aprobado en paquete, Q058 números propuestos. Sin fuente/modelo/Strategy admitidos ni performance. E4 sólo cálculo/meanpilot, no cobertura CAGR/ES/DD; M11 parcial/holdoutUNKNOWN. Versiones/declaraciones anteriores conservadas, no rehash histórico.

## Avance técnico posterior — wave07

[R-020_dataset_cards_RC0.md](R-020_dataset_cards_RC0.md) especifica propuestas/gates, no método/dataset/Strategy admitidos. M1 aprobado/ADR019; Q059 guardrails distintas propuestas. E5/E6screens no statisticalacceptance, costos/scale/fuente/financialtarget pendientes. Versiones anteriores conservadas; no benchmark/margen cambiados por resultados.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](R-020_preregistration_readiness_RC6.md), [configEQ3](R-020_configuration_completion_RC1.md), [DataCards](R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](R-007_protection_dependency_contract_RC2.md), [RiskRC2](R-027_risk_formula_spec_RC2.md) y [engine/QE0](R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.

## Fuente alternativa/PIT — 2026-10-23

[Wave05](R-008_alternative_actions_PIT_wave05_2026-10-23.md) examina acciones corporativas Databento como alternativa complementaria: revisión/alta/disponibilidad/recepción y replay observado versus reconstrucción se distinguen. Matriz CA01–09 especificada, NOT_EXECUTED; ninguna API/muestra/cuenta. WRAP condicionado/REFERENCE_ONLY actual; no source selected ni admisión. Derechos de retención/IA, cobertura/calidad, costes y paridad siguen pendientes. No esperar respuestas Twelve/EODHD para continuar P0/P1; envío automático prohibido. Las notas anteriores de autorización de comunicación son históricas, sustituidas por entrega personal del propietario.

## Actualización wave11 — 2026-10-23

[RetenciónpermanenteRC0](R-008_perpetual_retention_sources_RC0.md) agrega Kibot/FirstRate con derechos restringidos; KD1no recibióCSV, no fuenteadmitida. Twelve/EODHD awaiting; no esperar correos para decidir engine/broker. Docs2026/livefeed/PIT/cash separados.

## 2026-10-28 — Q-062 aprobado y proveedores actualizados

El propietario aprueba Alpaca Paper Only + LEAN source como **familias de diseño PAPER**, IBKR/Nautilus reservas: [ADR-023](../decisions/ADR-023-paper-broker-and-backtesting-families.md). B1–B5/QP1–QP10, pin/modelos/protección efectiva/target siguen pendientes; sin cuentas, gasto, implementación o LIVE. B3 no admisible implica no entradas.

[Evidencia comercial](R-008_vendor_evidence_and_plan_scope_RC1.md) disponible desde 2026-10-28, fecha real de recepción UNKNOWN y correos originales no inspeccionados. Twelve=VENDOR_INFORMATION_REQUESTED, aclaración del propietario pendiente de envío. EODHD=VENDOR_RESPONSE_RECEIVED / PLAN_SCOPE_CLARIFICATION_PENDING / TECHNICAL_ADMISSION_PENDING; todos los datasets NOT_ADMITTED, raw a IA externa DENY_UNCONFIRMED. Tres precios públicos19.99/29.99/99.99 incorporados a las cinco escalas; se prioriza EOD económico si cumple. No se espera respuesta para avanzar research.
