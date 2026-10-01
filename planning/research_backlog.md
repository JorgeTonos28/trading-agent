# Research Backlog v0 — 2026-10-01

Prioridad: P0 arquitectura, P1 implementación, P2 paper autónomo, P3 live, P4 futuro. Cada investigación produce un dossier con fuentes fechadas, hechos frente a supuestos, alternativas, criterios, coste/licencia, pruebas cuando proceda, riesgo, recomendación y enlace a decisión/ADR. Ningún candidato citado en la hoja queda seleccionado por aparecer aquí.

| ID | P | Cierra | Investigación / prueba y entregable |
|---|---|---|---|
| R-019 | P0 | D-009 | RESEARCHING: transcripción primaria revisada; usar `research/video_inspired_strategy.md` para extraer capacidades y reglas útiles. Más pantallas/prompts solo si aclaran nuestro diseño; claims de retorno `NO VERIFICADO`, sin auditoría dedicada. |
| R-020 | P0 | D-008/011 | Preregistrar criterios y comparar variantes video viables, MATR_V1 y otros candidatos; el sistema y contratos comunes gobiernan admisión. No seleccionar por aparecer en el video; `02_strategy_v1_selection.md` y aprobación humana. |
| R-021 | P0 | D-014/018/008 | Factibilidad PIT para **familias de señales externas** que puedan alimentar V1: timestamps de evento/publicación/recepción, cobertura histórica, derechos y primera operación posible. Congreso y alertas de terceros son casos, no el conjunto completo; coordinar con R-023/025. |
| R-022 | P0 | D-015/016/018/019 | DECIDED para D-015/016/019: `paper_v1_capability_contract_RC1.md` registra A+ y ADR-001; D-018 PIT por familia sigue R-023/021. |
| R-023 | P0 | D-018/014 | RESEARCHING: taxonomía y contrato de señales Smart Money/alternative data; separar Congreso, Form 4, 13F, hedge funds, options flow, block/dark pool, analyst revisions, fund flows y nuevos datos; `research/smart_money_data_landscape.md`. |
| R-024 | P0 | D-019/015/016 | DECIDED en alcance funcional: contrato RC1 vincula explicación a rastro y currículo §55 sin autoridad financiera; formato detallado, privacidad y evals se completarán como P1. |
| R-001 | P0 | D-010/011 | RESEARCHING: MATR_V1 RC0 es ficha candidata, no Strategy V1 seleccionada; faltan convenciones, datos, timing y protocolo OOS comparativo. |
| R-002 | P0 | D-012/017 | D-017 DECIDED en ADR-002: G1+G2 y reanudación humana tras pausa material. `03_risk_policy_RC1.md` conserva D-012 RESEARCHING para precedencia, reservas, clasificación, umbrales y pruebas. |
| R-003 | P0 | D-013/015 | RESEARCHING: `04_order_contract_RC0.md` define identidades, autorización, idempotencia y fallos; faltan máquina formal y pruebas contra broker. |
| R-004 | P0 | D-014 | RESEARCHING: `05_data_contract_RC0.md` define clocks, revisiones, snapshots y gates PIT; faltan muestras y convenciones por proveedor/estrategia. |
| R-005 | P0 | D-016 | DECIDED en alcance: contrato RC1 §5 mapea B0–B7 y §57; traceability requisito→test y umbrales detallados permanecen P1/P2 antes del DoR. |
| R-006 | P1 | D-020/024 | RESEARCHING: ver fichas iniciales C-001–006 en `capability_landscape.md`; faltan Codex/otras capacidades financieras, otros labs, open source, quant, brokers, datos, acceso/coste/licencias y clasificación final. |
| R-007 | P1 | D-021 | OPEN (marco RC0): Alpaca/IBKR/Tradier/tastytrade/TradeStation/otros, todos abiertos. API, PAPER, paridad live, streaming, stops/brackets/trailing, estabilidad, RD, equities, opciones futuras, costes y seguridad; `research/broker_selection.md`, scorecard y ADR humano. |
| R-008 | P1 | D-022 | Market data primario/validador: broker-native, Databento, Massive, Nasdaq Data Link, Tiingo, Alpha Vantage y nuevos candidatos; timestamps, ajustes, históricos, licencia, precios y muestras cruzadas. |
| R-009 | P1 | D-023 | Backtesting: LEAN, NautilusTrader, vectorbt, Backtrader y mínimo propio; reproducibilidad, PIT, modelo órdenes y coste de adaptación; benchmark desechable. |
| R-010 | P1 | D-024 | Runtime de planificación y agentes: Codex/Agents SDK/LangGraph/direct model calls/otros; permisos, observabilidad, evals, portabilidad, licencia y plugin format. |
| R-011 | P1 | D-025 | Workflow/scheduler: Temporal y alternativas, recuperación tras fallos, replay, disponibilidad, coste y carga operativa. |
| R-012 | P1 | D-026 | Storage/event/audit: PostgreSQL, Parquet/DuckDB, Redis y alternativas; reconstrucción PIT, retención, backup/restore y costos. |
| R-013 | P1 | D-027 | Threat model y security architecture: secretos, entornos, supply chain, plugin/MCP trust, prompt injection, control de deploy. |
| R-014 | P1 | D-028/029 | Observabilidad, runbooks, pruebas financieras, integración, replay, caos, evaluaciones de agentes y criterios de aceptación. |
| R-015 | P2 | D-030/031/032 | Probes y calibración PAPER: orden siguiente sesión, brackets/stops, fills parciales, incidentes y gate de autonomía. |
| R-016 | P3 | D-040/041/042 | Broker live, jurisdicción, costos, impuestos/documentación, capital, disaster recovery y gates paper→shadow→live. |
| R-017 | P4 | D-050 | Investigación **incremental futura** de alpha/Challengers para familias externas que no entren en alcance V1; factibilidad arquitectónica y selección de fuentes V1 se adelantan a R-021/023/025. |
| R-025 | P1 | D-033/020/022 | RESEARCHING: proveedores Smart Money/alternative data (Quiver, Unusual Whales, Capitol Trades, SEC/EDGAR directo y especialistas adicionales); API, historia, PIT, latencia, cobertura, coste, restricciones, calidad y backtesting por dataset; `research/smart_money_data_landscape.md`. |
| R-026 | P1 | D-034 | OPEN: esquema y aislamiento técnico del Portfolio Manager shadow; comparación pareada PIT con Champion, métricas preregistradas, costes/fills hipotéticos, reproducibilidad y errores. Descubrir frameworks/evals reutilizables antes de BUILD. |
| R-018 | P4 | D-051 | Opciones/short/leverage/cripto/futuros/regímenes avanzados: investigar solo tras alcance PAPER. |

## Protocolo de Capability Discovery (R-006)

Por cada capacidad se registrará `EXISTS`, `AVAILABLE_TO_US`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE`, `SELECTED` por separado; descripción, versión/fecha, fuente primaria, licencia/portabilidad, permisos requeridos, datos transmitidos, coste total, integración, mantenimiento, pruebas propias y disposición `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT`. `SELECTED=false` hasta ADR; `unknown` no se interpreta como `false`. Ninguna Skill, plugin o MCP recibe acceso de escritura al broker por el hecho de instalarse.

Orden de trabajo: R-022 fija mapa y fronteras del sistema; R-002/003/004/005 y R-023/024 cierran riesgo, ejecución, datos externos, PAPER V1 y pedagogía. R-019 aporta inspiración funcional sin auditar rentabilidades. R-006 y R-025/R-007 descubren capacidades/proveedores/broker contra contratos comunes. R-020 preregistra comparación de Strategy V1 **antes** de ver resultados; R-021 prueba PIT de fuentes candidatas y R-001 caracteriza MATR. R-008–R-014 completan stack/operabilidad. R-015 precede paper autónomo. R-016/017/018 no retrasan P0/P1 salvo nueva evidencia de alcance.
