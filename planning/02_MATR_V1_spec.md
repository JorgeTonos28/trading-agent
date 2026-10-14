# 02 — MATR_V1: ficha de candidato RC0

**Fecha:** 2026-10-01. **Estado:** `RESEARCHING`, no seleccionada, aprobada ni congelada. **Decisiones:** D-008/D-010/D-011; dependencias D-012/014/022/023/030. **Autoridad:** la selección y arquitectura final de Strategy V1 necesitan aprobación del propietario. Por ADR-000, esta ficha caracteriza MATR_V1 como candidato/benchmark alternativo; no es contrato de implementación, código ni instrucción de operar.

## 1. Baseline que se conserva

La hoja §18/§21 define un candidato experimental long-only, sin leverage, shorts, opciones, futuros ni cripto. Universo inicial `{SPY, QQQ, IWM, EFA, TLT, GLD}`. Al cierre de cada sesión se evalúan `Close(t) > SMA200(t)` y `ROC126(t) > 0`; los elegibles se ordenan por `ROC126` y se eligen hasta tres. Señal diaria, rebalance semanal y monitoreo de riesgo continuo. Stop inicial `3×ATR20`; presupuesto de riesgo PAPER estimado `0.50%` del equity por posición; cap de `25%` por posición; sin obligación de invertir todo. Entrada en sesión siguiente, nunca al cierre que generó la señal. Salida por stop, pérdida de elegibilidad, pérdida del top 3 en rebalance, kill switch o cierre administrativo. Benchmarks y ventanas propuestas: research 2005–2018, validation 2019–2022, “sealed OOS” 2023–2026-09-30.

**No se presume alpha:** la hoja exige resultado neto, robustez, forward paper y explicación económica antes de promoción. Valores de riesgo PAPER son provisionales y no límites live.

## 2. Semánticas que deben cerrarse antes de backtest válido

| ID | Decisión pendiente | Alternativas viables | Recomendación técnica provisional / prueba |
|---|---|---|---|
| M-01 | Serie para SMA/ROC/ATR | Raw; split-adjusted; dividend-adjusted/total-return; raw con eventos corporativos PIT | Conservar barras raw y eventos como verdad contable; calcular indicadores desde serie ajustada **solo con acciones conocidas en t** y convertir ATR/stop a unidades raw de orden. Comparar señales y P&L con raw+cash dividends. No seleccionar vendor todavía. |
| M-02 | Definición de día y disponibilidad | Fecha de barra; `end_time`; `available_at` real | Exigir calendario de exchange y `available_at <= signal_time`. Retraso configurable tras cierre oficial; ningún dato de t entra en una orden ejecutada en el cierre t. |
| M-03 | SMA/ROC/ATR | Variantes de ventanas y true range | Especificar SMA aritmética de 200 cierres incluyendo t, ROC `C_t/C_(t-126)-1`, ATR20 por Wilder o promedio simple tras prueba de paridad. Registrar warm-up ≥200 y reglas de missing bars. |
| M-04 | Rebalance y desempates | Día fijo semanal; primer día hábil; último cierre semanal; rank stable | Predefinir día/horario según calendario; ranking decreciente con desempate determinístico por ticker; no optimizar por resultado. |
| M-05 | Entradas | MOO; market tras apertura; marketable limit | Elegir tras probar capacidad broker y costes. El backtest debe usar la misma semántica y no adjudicar automáticamente `Open(t+1)` si la orden llegaría tarde. |
| M-06 | Cantidad final | Enteras o fraccionarias; precio de referencia; cash reserve | Definir round-down, notional mínimo, buying power, spread/fee reserve, secuencia de ventas/compras y conflictos; no pedir riesgo superior al cap. |
| M-07 | Stop/exit | Stop broker; stop software; stop-limit; combinación | Separar umbral estratégico de orden real. Un stop no acota pérdida máxima por gap. Simular gap, trigger, parcial y rechazo; broker-side según soporte. |
| M-08 | Cambios intraseamana | Filtro diario puede disparar exit cada día o solo al rebalance | La hoja dice señal diaria y salida al perder filtro, pero no fija instante de evaluación de top 3. Proponer filtro de salida diario y ranking de reemplazo semanal; requiere aprobación. |
| M-09 | Activos y disponibilidad histórica | Universo fijo; entrada por inception; sustitutos | No introducir sustitutos ex post. Validar inception, liquidez y datos 2005; si activo no existe/no tiene warm-up, no es elegible. |
| M-10 | Costes/retorno | Comisiones, spread, slippage, fees, dividendos, cash yield | Tres escenarios preregistrados con cifras derivadas de broker/quotes; benchmark en base total-return comparable. |
| M-11 | OOS/selección | Mantener 2023–2026 como holdout si intacto; reclasificarlo si consultado; forward prospectivo | Auditar exposición previa a resultados. Si no es demostrablemente intacto, etiquetar 2023–2026 **validation retrospectiva**, no OOS sellado, y reservar forward desde fecha de freeze. No fabricar un nuevo pasado “sin mirar”. |

## 3. Contrato provisional de señal y orden

Para cada ETF y cierre de sesión `t`, calcular solo con observaciones con `available_at <= decision_time`. Una serie incompleta, stale o que no alcanza warm-up no genera elegibilidad. Filtrar `C_t > SMA200_t` y `ROC126_t > 0`; rank entre elegibles y seleccionar máximo tres. La transición de posición se calcula respecto al estado de cartera reconciliado, no respecto a la cartera simulada de la víspera. Registrar `data_snapshot_id`, versión de reglas, calendario, valores de indicadores, ranking, razones y timestamp. La señal produce `TradeIntent`, no orden; riesgo determinístico puede rechazar o reducir notional. No se crea una nueva entrada si la sesión siguiente carece de datos frescos o broker/risk no están sanos.

Para una entrada PAPER, cantidad teórica `floor(min(0.005×equity / stop_distance, 0.25×equity / reference_price, buying_power / reference_price))`, sujeto a regla de lotes y reserva de costes aún por definir. Esto **reformula** la intención de §18, no fija una política aprobada. La distancia `3×ATR20` debe expresarse en precio raw ejecutable en el instante de la orden. Una pérdida real puede superar el presupuesto estimado por gap/slippage. Si `ATR<=0`, precio inválido, orden mínima imposible o quote stale, la entrada se rechaza y se audita.

## 4. Política de validación propuesta

1. Preregistrar código/spec, dataset/versiones, universo, calendario, parámetros, costes, benchmarks, métricas y número de experimentos **antes** de consultar cualquier período reservado.
2. Investigación 2005–2018 y validación 2019–2022 tal como propone la hoja, condicionadas a calidad/inception. Registrar también intentos fallidos. Vecindario de parámetros de §21 sirve para robustez, no para elegir ganador por CAGR.
3. El propietario confirmó el 2026-10-01 que nadie del proyecto ha ejecutado ni visto backtests de MATR_V1 o variantes cercanas para 2023–2026 ni otro período. Registrar esta declaración como evidencia de proceso. Todavía se debe preregistrar el protocolo de selección entre candidatos: consultar resultados de una opción y después ajustar criterios puede contaminar la comparación. Si una muestra reservada se usa para elegir estrategia/parámetros, reclasificarla y fijar forward test prospectivo desde freeze.
4. Comparar, en misma base temporal/contable, con SPY buy-and-hold, SPY SMA200, universo equal-weight, cash/T-bill proxy, MATR sin ranking y sin stop (estos dos últimos solo attribution). Todos reciben costes y tratamiento de dividendos coherentes.
5. Reportar distribución de resultados, drawdown, exposición, turnover, número de decisiones y operaciones, sensitivity, stress de costes, delay de una barra, crisis y dependencia de mejores trades. Una única métrica favorable no basta. El número de ensayos y la selección entre variantes deben registrarse para evaluar sesgo de búsqueda.
6. Criterios numéricos de continuación y horizonte de paper siguen abiertos; deben fijarse antes de ver la muestra que los calificará. Un test con pocas operaciones no puede respaldar con fuerza una afirmación de alpha.

## 5. Casos de aceptación exigidos (sin implementar aún)

- Barra t llega después de `decision_time`: no cambia señal ya emitida.
- Dividendo/split en t+1: serie de indicadores y unidades de orden/stop se mantienen coherentes; no hay doble contabilización.
- `C_t == SMA200_t` o `ROC126_t == 0`: no elegible (`>` estricto).
- Empate del tercer puesto: resultado reproducible según regla predeclarada.
- Menos de 200 observaciones válidas: no elegible; no rellenar datos futuros.
- Apertura t+1 con gap que cruza stop: fill model no fuerza precio de stop ni pérdida igual a 0.50%.
- Entrada y salida simultáneas / efectivo insuficiente / intent duplicado: una sola transición financiera autorizada y auditable.
- Cierre de viernes feriado o early close: calendario y rebalance se determinan antes, no por filas disponibles ex post.

## 6. Evidencia consultada y límites

- [CFA Institute, Backtesting & Simulation (2026)](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation): sesgos look-ahead/survivorship y utilidad de rolling-window, escenarios y sensibilidad. Es guía metodológica, no evidencia de rentabilidad de MATR.
- [Bailey y López de Prado, Deflated Sharpe Ratio](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551): la selección entre muchas pruebas infla resultados reportados. Justifica registrar experimentos y cautela estadística, no imponer aún un umbral DSR.
- [QuantConnect, Data Normalization](https://www.quantconnect.com/docs/v2/writing-algorithms/securities/asset-classes/us-equity/requesting-data) y [Corporate Actions](https://www.quantconnect.com/docs/v2/writing-algorithms/securities/asset-classes/us-equity/corporate-actions): muestra diferencias de modos raw/adjusted/total-return y de tratamiento backtest/live. Es evidencia de semánticas a comparar; no selección de LEAN.
- [SEC Investor.gov, Stop Orders (actualización 2026)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15): el precio stop no garantiza ejecución; stop-limit puede no ejecutarse. Requiere escenarios gap.
- [NYSE, Trading Information](https://www.nyse.com/trade/trading-information): calendario y horarios de sesión/auction necesitan incorporarse al timing. La hora de disponibilidad de nuestro proveedor sigue abierta.
- Antecedentes de revisión 2026-10-01: [SPDR GLD](https://www.spdrgoldshares.com/usa/gld/), [iShares ETF list EFA](https://www.ishares.com/us/products/etf-investments), [iShares TLT factsheet](https://www.ishares.com/us/literature/fact-sheet/tlt-ishares-20-year-treasury-bond-etf-fund-fact-sheet-en-us.pdf) se citaron con inception anterior a2005; no se vuelven a certificar sus fichas individuales en esta ola. **Corrección 2026-10-07:** [IWM oficial](https://www.ishares.com/us/products/239710/ishares-russell-2000-etf) confirma lanzamiento 2000-05-22; el enlace anterior usaba un slug de otro ETF. SPY/QQQ y calidad real/historia/warm-up de todos los datasets siguen por verificar. Inception no demuestra calidad ni disponibilidad de datos.

Exposición de proceso 2026-10-07: la consulta de fichas de emisores para comprobar referencias incluyó retornos públicos de ETF/benchmark, sin buscarlos como criterio ni usarlos para elegir parámetros. No se ha visto resultado de MATR_V1 o variantes; preservar esa distinción y registrar toda exposición pertinente antes de confirmar un holdout.

## 7. Próximo paquete de decisión

Esta ficha alimenta R-020. La decisión siguiente **no** es confirmar MATR_V1 por defecto, sino comparar Video-Inspired Strategy V1, MATR_V1 y otros candidatos justificados mediante criterios preregistrados; después presentar una recomendación de Strategy V1 al propietario. M-01/M-03/M-05/M-07/M-11 siguen requiriendo evidencia y coordinación con D-014/021/022/030. No se aprueba nada por el silencio del propietario.

## Semántica técnica y evaluación propuesta — 2026-10-13

[Cálculos RC1](research/R-020_shared_calculation_semantics_RC1.md) concretan propuesta SMA/ROC/WilderATR/warm-up/raw-vs-adjusted/corporateevents/cash, sin cerrar M03 ni seleccionar MATR; paridad engine y configuración faltantes. [Q055 O-B](research/D-011_OOS_policy_decision_RC0.md) preserva fechas baseline y propone comparación entre candidatos antes de confirmación; INTEGRITY_UNKNOWN hasta exposure ledger/M11, sin resultados nuevos ni waiver. ADR015 aplica referenciaR2 conceptual y p_authnew/pending; porcentajes del borrador no quedan aprobados. D010/011 RESEARCHING.

## Aprobación vigente O-B — 2026-10-14

[ADR-016](decisions/ADR-016-strategy-evaluation-O-B.md) registra Q055 DECIDED conceptual; D011 global RESEARCHING, Strategy OPEN. Reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11; alternativa prospectiva con gobierno si contaminada. Ensayos incluidos descartes, suficiencia/INSUFFICIENT_EVIDENCE, comparabilidad, walk-forward/sensibilidad/costes/retrasos y horizonte/latencia/caducidad quedan exigidos antes de resultados. Ningún modelo/umbral/estrategia/broker/data aprobado; lock y target deferral vigentes. Continúa paquete financiero sin solicitar Plus/admin ni investigación agéntica general.

## Wave04 — comparación previa a rendimiento

[Fichas comparables RC2](research/R-020_comparable_candidate_scorecard_RC2.md) y [protocolo](research/R-020_evaluation_protocol_RC2.md): cinco hipótesis declaradas, sin datos admitidos/retornos/selección, registrytrials0. Prioridad de investigación PRICE vs MATR y F4 como fuente externa a admitir, no resultado ni cierre D008. Q056 preferencia retorno/riesgo READY conceptual, criterios numéricos/métodos/Configs aún abiertos; F0 no sellado. Reserva UNKNOWN/M11, baselineMATR2005+ intacto.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Adenda de investigación — 2026-10-14

Baseline/reglas/ventanas originales conservados. [Pairing](research/R-020_PRICE_MATR_pairing_spec_RC0.md) distingue MATR baseline de MATR+ratchet y referencia EW6-BH de nuevo EW6-MONTHLY; ablations con ledgers divergentes no son misma cartera realizada. [Q057](research/D-011_benchmark_qualification_decision_RC0.md) propuesta previa a márgenes/resultados. MATR candidato/benchmark, no elegido ni backtest ejecutado. Registro conserva hash de declaración previa con EOL/commit, esta adenda no reescribe historia.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Investigación posterior — wave06

Benchmark K2 aprobado como paquete. [Book](research/R-020_K2_benchmark_book_RC0.md) y [RC4](research/R-020_statistical_method_contract_RC4.md) candidatos de realización/modelo; [Q058](research/D-011_economic_margins_proposal_RC0.md) propone números previos, no estrategia/márgenes ya decididos. RawSHA de declaraciónMATR queda anclado a1727470, posteriores adendas no lo sobrescriben. Ningún backtest; fechas/controlholdout conservados.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.
