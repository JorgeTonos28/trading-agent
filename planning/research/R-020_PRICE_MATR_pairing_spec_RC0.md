# PRICE–MATR — base común y atribución RC0

2026-10-14 · diseño de investigación, sin dataset/código operativo/backtest ni Strategy seleccionada. [ScorecardRC2](R-020_comparable_candidate_scorecard_RC2.md) y [contrato económicoRC3](R-020_economic_qualification_contract_RC3.md) gobiernan pendientes. F0 no sellado.

## PAIR-01: comparación integral

Mismo universo6ETF/as-of/inception, bar/feed/calendario y clocks, corporate actions, cartera inicial simbólica/cash unitizado, costs/fees/settlement/dividendos, Risk budgets y método de cantidad. No introducir capital real o porcentajes del borrador como aprobados. Signales después de availability, ejecución siguiente oportunidad versionada; MOO y post-open son escenarios distintos, no fills Open ficticios indistintos. Benchmark/cash/λ idénticos por contrato.

S-PRICE-01: ruptura126closes anteriores excluyendo t, módulo de posición inspirado en video; S-MATR-01: baseline SMA200/ROC126/top3 y salidas/rebalance de fichaM. Reportar entradas, duración/posiciones, exposure/turnover, stopmodel y deadlines; si exits/ranking/protección difieren, **atribución integral**, no «efecto puro del entry». No adscribir señales propias al video. S-PRICE-01 a/h/b y episode/ordermapping siguen OPEN; no variante ejecutable mientras falten.

## PAIR-02: ablation propuesta, no variante ejecutada

Para aislar entrada, elaborar variantes manteniendo exits/ranking/stop/calendar/sizing/missing iguales y cambiar únicamente filtro de entradaPRICE vsMATR. Para aislar ratchet, mantener las mismas reglas y calendario de entrada, política de sizing/riesgo y ejecución, cambiando únicamente módulo fijo vs escalonado. Los ledgers de posiciones, entradas efectivamente admisibles, cash y riesgo posteriores pueden divergir porque el stop cambia las salidas. No forzar mismas cantidades/posiciones realizadas para presentar una cartera factible. Si se fijan entradas/cantidades exógenas para estudiar mecánica, etiquetar MODULE_ONLY: no calificación económica de cartera. Each variant obtiene ID/hash/config/family/attempts y trialbook antes de resultados; no sumar sólo las dos finalistas a búsqueda. Ladder de compras en caída es otra variante, no incluida por defecto ni aprobada por menorR2.

No confundir baselineMATR con MATR+ratchet o con benchmarkSPY. CandidateConfig final debe fijar cada campo y matriz de cambios; hasta entonces no declarar aislamiento causal ni conjunto de parámetros preregistrado. VecindariosSMA180/200/220,ROC105/126/147,ATR2.5/3/3.5 del roadmap son diagnóstico preregistrado, no optimizador ni selección implícita de mejor vecino.

## Episodios y protección — propuesta técnica a contrastar

Una episode por security desde primerfill a flat reconciliado, un entryintent vivo por instrumento, sin topups en variante mínima. Parciales del mismo intent no son nuevas señales. p0/HWM/ATR/qty y splitrebase se versionan, sin reset por gap o pérdida deeligibilidad sólo para embellecerretorno. El módulo debe definir si ratchet usa cada lote o aggregate: propuesta simple a contrastar es **sellar entry** después de fillcompleto o cancelremainder confirmado antes de activar aggregate ratchet, con p0 de fills reconciliados y HWM desde seal. No hereda highs previos a la existencia de la cantidad ni espera seal para exigir protección de parciales.

Stop inicial/cobertura de filledqty permanece obligación inmediata desde autorizacióncondicional→fill/ack; brokerpartialmap se prueba B3. Stopdesired no stopconfirmado; if missing/crossed/unconfirmed=>UNCERTAIN/R2nulleval, no adicionar ni fabricar0. HWM por high de barra cerrada sólo cambia stop después de availability/validación/confirmación, no protege retrospectivamente movimiento intrabar. Splitadjustar rawprecios/qty y preservarcashdividends una vez. Core siempre supervise protección, no jobAI.

La propuesta seal puede perder mejoras de ratchet durante entrylargo y exige medir ese coste; otra regla por lote podría ser necesaria. No selección silenciosa ni gatebroker pasado por facilidad. Gobierno de Strategy freeze valida esa semántica tras test broker/engine/source, sin administrar workstation ni implementar.

## Readiness técnica

Propuestas SMA/ROC/WilderATR/strictfilters se especifican en semánticasRC1; aún faltan paridadengine y fuentes. Broker/data costs/latency/freshness/entryexpiry/risknums yparamsratchet no se cierran desde un escenario sintético. Esta pairing spec reduce demanda/ambigüedad, no afirma backtest admission ni prescribe alcance de Form4; su cohorte exige DataCard/universe propio.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](../decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Benchmark reproducible — wave06

[Benchmark reproducible](R-020_K2_benchmark_book_RC0.md) añade especificación y límites; Q057 aprobado en paquete, Q058 números propuestos. Sin fuente/modelo/Strategy admitidos ni performance. E4 sólo cálculo/meanpilot, no cobertura CAGR/ES/DD; M11 parcial/holdoutUNKNOWN. Versiones/declaraciones anteriores conservadas, no rehash histórico.

## Avance técnico posterior — wave07

[R-020_PRICE_MATR_rule_configurations_RC0.md](R-020_PRICE_MATR_rule_configurations_RC0.md) especifica propuestas/gates, no método/dataset/Strategy admitidos. M1 aprobado/ADR019; Q059 guardrails distintas propuestas. E5/E6screens no statisticalacceptance, costos/scale/fuente/financialtarget pendientes. Versiones anteriores conservadas; no benchmark/margen cambiados por resultados.
