# Research Backlog v0 — 2026-10-01

Prioridad: P0 arquitectura, P1 implementación, P2 paper autónomo, P3 live, P4 futuro. Cada investigación produce un dossier con fuentes fechadas, hechos frente a supuestos, alternativas, criterios, coste/licencia, pruebas cuando proceda, riesgo, recomendación y enlace a decisión/ADR. Ningún candidato citado en la hoja queda seleccionado por aparecer aquí.

| ID | P | Cierra | Investigación / prueba y entregable |
|---|---|---|---|
| R-019 | P0 | D-009 | RESEARCHING: transcripción primaria revisada; usar `research/video_inspired_strategy.md` para extraer capacidades y reglas útiles. Más pantallas/prompts solo si aclaran nuestro diseño; claims de retorno `NO VERIFICADO`, sin auditoría dedicada. |
| R-020 | P0 | D-008/011 | Preregistrar criterios y comparar variantes video viables, MATR_V1 y otros candidatos; el sistema y contratos comunes gobiernan admisión. No seleccionar por aparecer en el video; `02_strategy_v1_selection.md` y aprobación humana. |
| R-021 | P0 | D-014/018/008 | Factibilidad PIT para **familias de señales externas** que puedan alimentar V1: timestamps de evento/publicación/recepción, cobertura histórica, derechos y primera operación posible. Congreso y alertas de terceros son casos, no el conjunto completo; coordinar con R-023/025. |
| R-022 | P0 | D-015/016/018/019 | DECIDED: contrato PAPER V1 RC1 y ADR-001 cierran A+ D-015/016/019; ADR-005 cierra roles/admisión abstracta D-018, mientras R-021/025 prueba datasets. |
| R-023 | P0 | D-018/014 | DECIDED en contrato abstracto ADR-005/`06_external_signal_admission_RC1.md`: familias separadas, roles graduados y gates PIT/licencia/OOS; R-021 y R-025 siguen pruebas por dataset/proveedor. |
| R-024 | P0 | D-019/015/016 | DECIDED en alcance funcional: contrato RC1 vincula explicación a rastro y currículo §55 sin autoridad financiera; formato detallado, privacidad y evals se completarán como P1. |
| R-001 | P0 | D-010/011 | RESEARCHING: MATR_V1 RC0 es ficha candidata, no Strategy V1 seleccionada; faltan convenciones, datos, timing y protocolo OOS comparativo. |
| R-002 | P0 | D-012/017 | DECIDED en alcance conceptual: D-017/ADR-002 G1+G2 y reanudación humana; D-012/ADR-006 opción B compuesta. Umbrales, escenarios, fórmulas concretas y pruebas siguen D-031/D-021/026/030. |
| R-003 | P0 | D-013/015 | DECIDED en contrato abstracto: `04_order_contract_RC1.md` y ADR-003 fijan identidades, eventos, autorización, `UNKNOWN` y G2; semántica/probes del broker candidato siguen D-021/030/031. |
| R-004 | P0 | D-014 | DECIDED en contrato abstracto: `05_data_contract_RC1.md` y ADR-004 fijan clocks por canal, `eligible_from`, revisiones y ajustes as-of; muestras/delays/proveedor siguen R-021/025/008. |
| R-005 | P0 | D-016 | DECIDED en alcance: contrato RC1 §5 mapea B0–B7 y §57; traceability requisito→test y umbrales detallados permanecen P1/P2 antes del DoR. |
| R-006 | P0 | D-020/024 | **FOCO INMEDIATO / RESEARCHING** bajo ADR-007: IA/agentes solo OpenAI y Anthropic; prioridad Plus/Codex y activos públicos Tier 0/1, sin probes API facturables. Inventario, acceso empírico, licencia/coste, portabilidad Anthropic, probes prioritarios y Build-vs-Reuse. D-024 no puede cerrarse antes de revisión de madurez R-006. |
| R-007 | P1 | D-021 | OPEN (marco RC0): Alpaca/IBKR/Tradier/tastytrade/TradeStation/otros, todos abiertos. API, PAPER, paridad live, streaming, stops/brackets/trailing, estabilidad, RD, equities, opciones futuras, costes y seguridad; `research/broker_selection.md`, scorecard y ADR humano. |
| R-008 | P1 | D-022 | Market data primario/validador: broker-native, Databento, Massive, Nasdaq Data Link, Tiingo, Alpha Vantage y nuevos candidatos; timestamps, ajustes, históricos, licencia, precios y muestras cruzadas. |
| R-009 | P1 | D-023 | Backtesting: LEAN, NautilusTrader, vectorbt, Backtrader y mínimo propio; reproducibilidad, PIT, modelo órdenes y coste de adaptación; benchmark desechable. |
| R-010 | P1 | D-024 | Comparativa de arquitectura agéntica **OpenAI/Codex Tier 0/1**, incluyendo SIWC plan usage/Codex app-server solo si prueba entitlement y operación, y activos Anthropic portados/adaptados. Agents SDK/API con clave son `REFERENCE_ONLY` Tier 2 sin excepción. Inicia tras mapa R-006 maduro; sin preselección. |
| R-011 | P1 | D-025 | Workflow/scheduler: Temporal y alternativas, recuperación tras fallos, replay, disponibilidad, coste y carga operativa. |
| R-012 | P1 | D-026 | Storage/event/audit: PostgreSQL, Parquet/DuckDB, Redis y alternativas; reconstrucción PIT, retención, backup/restore y costos. |
| R-013 | P1 | D-027 | Threat model y security architecture: secretos, entornos, supply chain, plugin/MCP trust, prompt injection, control de deploy. |
| R-014 | P1 | D-028/029 | Observabilidad, runbooks, pruebas financieras, integración, replay, caos, evaluaciones de agentes y criterios de aceptación. |
| R-015 | P2 | D-030/031/032 | Probes y calibración PAPER: orden siguiente sesión, brackets/stops, fills parciales, incidentes y gate de autonomía. |
| R-016 | P3 | D-040/041/042 | Broker live, jurisdicción, costos, impuestos/documentación, capital, disaster recovery y gates paper→shadow→live. |
| R-017 | P4 | D-050 | Investigación **incremental futura** de alpha/Challengers para familias externas que no entren en alcance V1; factibilidad arquitectónica y selección de fuentes V1 se adelantan a R-021/023/025. |
| R-025 | P1 | D-033/020/022 | RESEARCHING: proveedores Smart Money/alternative data (Quiver, Unusual Whales, Capitol Trades, SEC/EDGAR directo y especialistas adicionales); API, historia, PIT, latencia, cobertura, coste, restricciones, calidad y backtesting por dataset; `research/smart_money_data_landscape.md`. |
| R-026 | P1 | D-034 | OPEN: esquema y aislamiento técnico del Portfolio Manager shadow; comparación pareada PIT con Champion, métricas preregistradas, costes/fills hipotéticos, reproducibilidad y errores. Descubrir frameworks/evals reutilizables antes de BUILD. |
| R-027 | P1 | D-035 | OPEN: especificar y probar en papel fórmulas, unidades, redondeos, precedencia, concurrencia y estados no evaluables de opción B; separar parámetros numéricos D-031 de semántica del algoritmo antes del DoR. |
| R-018 | P4 | D-051 | Opciones/short/leverage/cripto/futuros/regímenes avanzados: investigar solo tras alcance PAPER. |

## Protocolo de Capability Discovery (R-006)

Por cada capacidad se registrará `EXISTS`, `AVAILABLE_IN_RESEARCH_ENVIRONMENT`, `AVAILABLE_IN_TARGET_PLUS`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE`, `SELECTED` por separado; Tier, versión/fecha, fuente primaria, licencia/portabilidad, permisos, datos transmitidos, coste incremental, pruebas y disposición `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT`. El primer entorno es la sesión Team de planificación; el segundo es la cuenta Plus individual que gobernará PAPER V1. `SELECTED=false` hasta ADR; `unknown` no se interpreta como `false`. Para IA/agentes solo OpenAI y Anthropic bajo ADR-007; Tier 2 requiere excepción humana documentada. Brokers/datos/quant/infraestructura mantienen investigaciones separadas. Ninguna Skill, plugin o MCP recibe acceso de escritura al broker por instalarse.

Orden vigente: contratos financieros abstractos D-012–019 establecidos; **R-006/D-020 es el foco inmediato y gate de D-024**. R-025/R-007 siguen descubrimiento de proveedores/broker contra esos contratos. R-020 preregistra comparación de Strategy V1 **antes** de ver resultados; R-021 prueba PIT de fuentes candidatas y R-001 caracteriza MATR. R-008–R-014 completan stack/operabilidad tras incorporar resultados R-006. R-015 precede paper autónomo. R-016/017/018 no retrasan P0/P1 salvo nueva evidencia de alcance.
