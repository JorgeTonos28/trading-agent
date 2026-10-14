# R-020 — candidatos comparables y recomendación antes de rendimiento — RC2

2026-10-14 · D008 OPEN, D010/011 RESEARCHING. Fichas de diseño comparables, **no candidatos ya admitidos a backtest ni criterio F0 sellado**. O-B aprobado ADR016; no rendimiento histórico nuestro observado. No atribuir entradas propias al creador del video.

## 1. Reglas propuestas para reducir ambigüedad

| ID declarado | Hipótesis y reglas concretas propuestas | Salidas/posición | Aún necesario |
|---|---|---|---|
| S-PRICE-01: VID-PRICE-EOD | Entrada propia por ruptura: close elegible > máximo de126cierres previos, sin incluir t. Universo comparador SPY/QQQ/IWM/EFA/TLT/GLD; instrumentos/inception/data admission primero. Si ya hay posición, señal no añade. Hasta3 posiciones, nuevos elegibles desempate ROC126/ticker estable | Módulo video ratchet escalonado separado; inicial3ATR20 candidato. Protección/expiry/reconciliación tienen precedencia; no ladder de compras en caída en esta variante | Parámetros a/h/b y lote/episode, cadence/sesión/orden/fees/marks/risk budgets.126 representa seis meses aproximados por convención de sesiones; propuesta de diseño, no hallazgo ni parámetro óptimo |
| S-MATR-01: MATR benchmark | Baseline SMA200/ROC126/top3, rebalance semanal y pérdida de elegibilidad, ficha M01–11 | Stop inicial3ATR20, reglas de salida baseline; mismos presupuestos/Risk independientes para comparación futura | Campos M restantes, quote/broker/engine/data; riesgo0.5%/cap25% del borrador no aprobado |
| S-F4-01: VID-F4-EOD | Sólo transacción no derivada P, clase exchange acreditada, issuer/security as-of y owners/footnotes/plan completos; ambiguo=>quarantine. No elegir insiders por retorno. Una oportunidad por hecho económico; activar tras availability/receipt | Módulo común protección/ratchet y H_hold por fijar; no venta automática por insider venta | Data gate primario/vendor/PIT, universo as-of/listaactores exante/filtros plan/H_hold/expiry/params; E1 parcial no los satisface |
| S-CONG-01: VID-CONG-EOD | Compra pública admisible en equity de listaactores exante, documento/version único, no transaction-date. Rangos monetarios no sizing | Módulo común y evento de venta/time exit explícitos a evaluar | Listaactores/history/rights/PIT/mapping/expiry/params; no proxy de toda Smart Money |
| S-13F-01: VID-13F-REBAL | Variación de holding entre dos filings comparables publicados; gestores exante, units/CUSIP/completeness/amendments | Rebalance por publicación/targets determinísticos; no quarter-end compra retrospectiva | Historia PIT/map/confidential data, caducidad/targets/coverage; pocos trimestres pueden ser insuficientes |

Las cifras126/3/top3 son propuestas de comparación y baseline existente, no aprobaciones. Para S-PRICE-01 no se elimina ladder de otras variantes ni se interpreta menorR2 como permiso de añadir: futura variante con adds requiere señal/regla explícita, evaluación integral y aprobación propia. Si el escalonado no obtiene parámetros defensibles, la ficha **no se congela** ni se sustituye silenciosamente por trailing nativo. Variante continua/ATR u otra entrada cuenta como nueva variante. Módulo de salida aislado sin entrada no constituye Strategy V1.

## 2. Comparabilidad y admisión, no ranking de alpha

| Criterio previo | PRICE / MATR: cohorte ETF propuesta | F4 / Congreso /13F: cohorte disclosures propuesta |
|---|---|---|
| Fuente/señal | Raw/as-of prices + corporate actions, sin input LLM financiero | Filings/events + precio y universe/mapping, varias dependencias |
| Historia/rights/PIT | Ningún dataset admitido; Starter durable incompatible, otras rutas UNKNOWN | Clocks/rights/history sin acreditar; normalizador no demuestra source availability |
| Comparación directa | Mismo universo, calendario, presupuestos, costs/contabilidad/feed y2019–2022; warm-up sin P&L | Sólo si admitida misma ventana y misma base económica; benchmark representativo de su universo, no CAGR cross-period contra ETF |
| Horizonte/latencia | EOD + próxima oportunidad autorizada; no asumir Open ideal | Evento disponible y holding declarado; economic decay no inferido de antigüedad filing |
| Complejidad/mantenimiento | Menos canales/map externos; no prueba de rentabilidad ni operación free completa | Mayor carga clocks/normalización/actores/map; puede aportar señal distinta, evidencia pendiente |
| Interpretabilidad | Regla de entrada/stop/latencia reproducible para pedagogía | Puede explicar documento/filtros/desconocidos; narrativa de insider no es señal automáticamente |
| Autoridad/seguridad | Signal/TradeIntent determinísticos, Risk único, PM shadow | Igual; ningún disclosure/ResearchAgent obtiene autoridad de órdenes |
| Estado comparador | DESIGN_COMPARABLE_CONDITIONAL; DATA_NOT_ADMITTED, PERFORMANCE_NOT_EVALUATED | DESIGN_SCOPED; DATA_NOT_ADMITTED, PERFORMANCE_NOT_EVALUATED |

Fuentes2016+ pueden cubrir2019–2022 con warm-up pero **no todo desarrollo2005–2018 MATR**. No recortar ese bloque para declarar completada su evaluación. Instrumento/actor/universo diferente exige explicar benchmark/exposición; atribución dentro de familia vs comparación global se separan. Si distintos datasets no preservan misma base, no existe scorecard financiero directo aún; registrar no comparabilidad, no inventar ganador.

## 3. Recomendación fundamentada y criterios

Recomiendo completar primero **PRICE frente a MATR en cohorte ETF común**, manteniendo F4 como primera ruta externa a intentar admitir y Congreso/13F en tracks paralelos. Razón: reglas determinísticas e inputs verificables más acotados permiten aislar utilidad del módulo inspirado en video sin confundirlo con múltiples fuentes. No sustituye la intención de Smart Money del sistema ni aprueba precio-only como Strategy final. Si F4 obtiene datos admisibles y evidencia suficiente, puede entrar a comparación antes de selección. Proveedores especializados se comparan, no se presume SEC gratis suficiente.

La recomendación es de **orden de investigación**, no «PRICE gana» ni «MATR funciona». No seleccionar por código simple si no demuestra economía/robustez; no privilegiar disclosures por intuición de Smart Money. Primer checkpoint D008 debe incluir Configs completas, DataCards, EvidenceRequirementCards, casos broker/riesgo, scorecard de criterio y alternativas, con review y owner. Hasta ahí selected_strategy=null.

Criterios ya obligatorios ADR016: rights/PIT/coverage, toda búsqueda registrada, independencia, base comparable, muestra efectiva, robustness temporal/costs/latency, risk/execution y pedagogía. Criterios estadísticos **propuestos, no sellados** en RC2: endpoint/efecto mínimo, dependencia/power/precision, error familia, clusters/regímenes/folds. [Q056](D-011_economic_endpoint_decision_RC0.md) prepara la decisión material sobre qué mejora económica queremos demostrar; no fijar esa preferencia desde CAGR visto. Fechas de selección/confirmación se preservan, reserva UNKNOWN.

## 4. Ruta de evidencia sin circularidad

Diseño/especificación/admisión/metodología en Team; backtests reales/carga/integración y validación operacional en PC personal. D008 selección de diseño necesita gobierno y contrato congelado, no alpha inventada antes de probar. DoR/target acceptance antes de implementación; evidence forward/PAPER/promoción antes de autonomía/LIVE. Gate estadístico de suficiencia no se sustituye por aprobación de owner ni por objetivo pedagógico.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](../decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Avance posterior wave05

Q056 aprobado/ADR017. [PAIR-01/02](R-020_PRICE_MATR_pairing_spec_RC0.md) aclara base común y cambios de entry/exits/ratchet; no retorno comparado ni causalidad por sólo igualar universo. [RC3](R-020_economic_qualification_contract_RC3.md) y [Q057](D-011_benchmark_qualification_decision_RC0.md) proponen referencia ETF y gates; [F4RC2](R-021_Form4_semantic_admission_RC2.md) conserva gaps de planes/semántica y alternativa plan-agnostic no ejecutada. Registry8 declara hipótesis/ablations, no ocho finalistas admitidos; todos sin performance ni configuración completa.
