# 02 — Strategy V1 Selection: protocolo RC0

**Estado:** OPEN (D-008, P0). **Fecha:** 2026-10-01. Ninguna estrategia seleccionada; no se han consultado backtests de MATR_V1 según declaración del propietario. El enfoque del video es el **primer candidato que descomponemos y robustecemos**, no la arquitectura ni la estrategia aprobada. Este protocolo se fija **antes** de pruebas comparativas. ADR-000 establece el alcance. La selección final requiere aprobación humana.

## Candidatos mínimos

| ID | Candidato | Estado | Qué debe quedar especificado |
|---|---|---|---|
| S-VID | Familia Video-Inspired Strategy V1 | Descompuesta desde la transcripción primaria en `research/video_inspired_strategy.md` | VID-TS (stop/ladder incompleto), VID-CONG (disclosures), VID-ALERT (alertas autorizadas) y VID-WHEEL (opciones, fuera de alcance V1). Infraestructura y SIGNAL no son estrategias. Ninguna variante entra a scorecard cuantitativo sin reglas falsables. |
| S-MATR | MATR_V1 | Ficha RC0 | Reglas de §18 y pendientes M-01–M-11 en `02_MATR_V1_spec.md`; sigue como candidato/benchmark, no seleccionado. |
| S-NEW | Otros candidatos con fundamento | Admisión abierta | Hipótesis económica, reglas, datos PIT, restricciones PAPER y motivo de inclusión previo a backtest. |

La *wheel* de opciones del video no es elegible para PAPER V1 bajo el alcance actual (sin derivados). Puede investigarse como componente separado P4; solo entra en selección si el dueño aprueba cambio de alcance. Una conexión directa Codex–broker tampoco es estrategia y no satisface el invariante de autoridad financiera. Las rentabilidades alegadas de 164,99% de una cuenta y ~72% en un dashboard congresual se registran `NO VERIFICADO` y **no generan investigación autónoma para auditarlas**. Congreso es una fuente externa entre otras; R-023/R-025 investigan Smart Money como familia amplia.

## Gates de admisión antes de comparar resultados

1. **Reglas completas:** universo, señal, entrada, salida, sizing, calendario, capital, costes y condiciones de suspensión determinables sin interpretación retrospectiva.
2. **PIT y disponibilidad:** fuente, publicación/recepción y momento de uso demostrables. Para disclosures, usar fecha pública, nunca fecha de operación del tercero como si fuera conocida.
3. **Alcance:** long-only sin leverage ni derivados para PAPER V1, salvo CR y aprobación humana.
4. **Seguridad:** ninguna variante exige LLM con autoridad directa para ordenar o modificar límites.
5. **Datos y testabilidad:** historia suficiente y derechos de uso razonables; benchmark y costes aplicables; posible replay reproducible.
6. **Complejidad operativa:** ejecución, monitoreo y fallos manejables en la primera plataforma PAPER.
7. **Encaje con el sistema:** el candidato puede usar contratos de señal, datos, riesgo, ejecución, auditoría y explicación pedagógica sin crear autoridad financiera paralela.

Un candidato que falla un gate no se descarta por intuición: se registra `DEFERRED` o `REJECTED_FOR_V1` con motivo y evidencia. Un candidato incompleto no recibe reglas inventadas para forzarlo a competir.

## Comparación cualitativa previa a backtest

Para los candidatos admitidos se documentarán: (a) claridad y fundamento de la hipótesis, (b) riesgo de sesgos y overfitting, (c) datos/licencia/coste, (d) fidelidad de replay→paper, (e) riesgos de ejecución y gap, (f) complejidad del control determinístico, (g) capacidad pedagógica y (h) valor de construir infraestructura reutilizable. Los pesos/umbrales y cualquier tie-break se aprobarán **antes** de abrir un holdout. El rendimiento histórico no será el criterio único ni se usará para alterar retroactivamente esta matriz.

## Política de evidencia y OOS

- Preservar declaración del dueño: hasta 2026-10-01 no se ha visto ningún backtest de MATR_V1 en ningún período.
- Separar *diseño de candidato* de *test estadístico*. Registrar cada variante ensayada, incluso fallida, y congelar reglas/criterios antes de consultar la muestra reservada.
- Si se mira un período para escoger entre candidatos, ese período deja de ser evidencia independiente de la estrategia elegida; se requerirá un forward/OOS nuevo para confirmación.
- Las alegaciones de rentabilidad del video, si las hay, no cuentan como rendimiento validado sin datos, método, costes y resultados reproducibles.

## Entregable de decisión

El futuro paquete al propietario mostrará cada candidato, evidencia primaria, reglas exactas, gate de admisión, scorecard, pruebas, sensibilidad, riesgos, costes, alternativas, recomendación y la pregunta única: **“¿Qué estrategia autorizamos como primera Strategy V1 para especificar y construir en PAPER?”** Se registrará ADR con fecha y aprobador. Hasta entonces, `selected_strategy: null`.

## Avance R-020 posterior ADR-011 — 2026-10-05

[Preregistro RC1](research/R-020_strategy_admission_preregistration_RC1.md), [CandidateRuleCards video](research/R-020_video_candidate_rule_cards_RC0.md) y [DatasetCard SEC](research/R-020_SEC_dataset_admissibility_RC0.md) avanzan admisión antes de rendimiento. VID-TS no define entrada; trailing porcentual/absoluto y ladder/stop tienen conflictos explicitados. SEC público no implica clock de primera disponibilidad histórico; acceptance no sustituye publication/receipt. MATR sigue candidato/benchmark. **Strategy V1 Selection=OPEN**, ningún backtest, riesgo numérico, broker/datos o estrategia aprobados.

## Avance financiero — 2026-10-13

[Alternativas de reglas RC1](research/R-020_candidate_rules_RC1.md) separan VID-CONG-EOD/F4-EOD/13F-REBAL y VID-PRICE-ENTRY propio, módulo de posición y MATR benchmark. Campos config/corporateactions/episodio/partial/top-up obligatorios todavía OPEN. [Datos externos](research/R-021_external_dataset_admission_RC1.md) y [market data wave02](research/R-008_market_data_evidence_wave02_2026-10-13.md) prueban disponibilidad documental, no datasets PIT/rights admitidos. [Engine shortlist](research/R-009_backtesting_reuse_RC0.md) y [broker/protection](research/R-007_order_protection_matrix_RC1.md) diferencian rutas y pruebas target.

Strategy V1 sigue OPEN; no selección/retorno/holdout. El siguiente gobierno material Q-054 resuelve referencia de medición de riesgo común a sizing, no estrategia ganadora. No política numérica, broker o engine aprobados.

## Vigencia wave03 — 2026-10-13

Q054 referenciaR2 DECIDED por ADR015; D035 restante abierto. [Cálculos comunes RC1](research/R-020_shared_calculation_semantics_RC1.md) propuesta técnica sin Strategy seleccionada; [O-B/Q055](research/D-011_OOS_policy_decision_RC0.md) READY_FOR_DECISION conceptual, no fechas reinterpretadas. [E1](research/R-021_edgartools_findings_2026-10-13.md) estructuralPARTIAL y [retención](research/R-008_data_retention_gate_RC1.md) restringen admisión, no eligen al ganador. Strategy V1 OPEN. Reserva2023–2026-09-30 INTEGRITY_UNKNOWN hasta exposure ledger/M11, no nuevos resultados/dataset confirmatorio en wave03.

## Aprobación vigente O-B — 2026-10-14

[ADR-016](decisions/ADR-016-strategy-evaluation-O-B.md) registra Q055 DECIDED conceptual; D011 global RESEARCHING, Strategy OPEN. Reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11; alternativa prospectiva con gobierno si contaminada. Ensayos incluidos descartes, suficiencia/INSUFFICIENT_EVIDENCE, comparabilidad, walk-forward/sensibilidad/costes/retrasos y horizonte/latencia/caducidad quedan exigidos antes de resultados. Ningún modelo/umbral/estrategia/broker/data aprobado; lock y target deferral vigentes. Continúa paquete financiero sin solicitar Plus/admin ni investigación agéntica general.

## Wave04 — comparación previa a rendimiento

[Fichas comparables RC2](research/R-020_comparable_candidate_scorecard_RC2.md) y [protocolo](research/R-020_evaluation_protocol_RC2.md): cinco hipótesis declaradas, sin datos admitidos/retornos/selección, registrytrials0. Prioridad de investigación PRICE vs MATR y F4 como fuente externa a admitir, no resultado ni cierre D008. Q056 preferencia retorno/riesgo READY conceptual, criterios numéricos/métodos/Configs aún abiertos; F0 no sellado. Reserva UNKNOWN/M11, baselineMATR2005+ intacto.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Comparación económica posterior — 2026-10-14

[PAIR-01/02](research/R-020_PRICE_MATR_pairing_spec_RC0.md) y [RC3](research/R-020_economic_qualification_contract_RC3.md) desarrollan PRICE vs MATR con ledger/benchmark/cash/clock común y ablations explícitas. [Q057](research/D-011_benchmark_qualification_decision_RC0.md) propone referencia primaria de esta cohorte, no selección Strategy. Form4 primera externa sigue candidata NOT_ADMITTED; plan-agnostic es nueva hipótesis, no relajación silenciosa del filtro. Strategy V1 OPEN, F0 incompleto, holdout UNKNOWN.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Protocolo económico wave06

[BookK2](research/R-020_K2_benchmark_book_RC0.md)/[RC4](research/R-020_statistical_method_contract_RC4.md) desarrollan paquete aprobado: beta/factores/streams/costs y métricas explícitas; [Q058](research/D-011_economic_margins_proposal_RC0.md) propuesta numérica, no selección ni marginal aprobado. Fuentes aún no admitidas; [M11](research/R-020_M11_repository_audit_RC0.md) parcial. StrategyV1 OPEN, F0 incompleto, target/lock intactos.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.

## Rulepresets y evidencia wave07

[Configurations](research/R-020_PRICE_MATR_rule_configurations_RC0.md) conIDs hijos dePRICE/MATR, numparams propuestos sin aprobar/seleccionar yfinancialtarget/risk/broker/source pendientes. [DataCards](research/R-020_dataset_cards_RC0.md)allNOT_ADMITTED, [RC5](research/R-020_evaluation_contract_RC5.md) diseño sin métodoaceptado yQ059 controles nuevos. Registry10declaraciones,0trials; no Strategy recomendada porretorno ni selección implícitaMATR.

## Vigencia G-R1 — ADR-020, 2026-10-15

[ADR-020](decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md): Q-059/G-R1 DECIDED en preferencia económica ex ante: no deterioro de DD frente a EW6-BH completo ni de volatilidad diaria frente al espejo K2 admisible. ES95/M1 primario y NI/cash/K2 conjuntos; recuperación/underwater/pérdidas/gaps/slippage/extremos obligatorios. DD exige estimando/horizonte/path/incertidumbre y aplicabilidad válidos; una trayectoria/bootstrap genérico no demuestra futuro. Volatilidad incluye upside/downside. Guardrails relativas no son límites absolutos Risk D-031. G-R2 no aprobado ni fallback. Estados separados y NO_STRATEGY_QUALIFIED; ningún método/dato/broker/Strategy/F0/implementación aceptado. Continuar P0/P1 financieros en checkpoints agrupados; holdout UNKNOWN/lock/targetdeferral.

## Referencia PAPER y cobertura de costes — ADR-021, 2026-10-15

[ADR-021](decisions/ADR-021-PAPER-economic-reference-capital.md): propietario fija nominalUSD10,000 antes de resultados y exige costes evaluados/reportados en las cinco escalasUSD2k/5k/10k/25k/50k, conservando20celdas hipotéticas previas. Todas las fuentes/modelos de coste admitidos se aplican a cada escala; UNKNOWN explícito, no0/omisión ni capital favorable elegido después. Principal10k no prometePASSuniversal ni exigePASSen5como nuevo gate implícito. Sin depósito/funding/capitalLIVE/gasto/risknumbers; costes reales/método/data/Strategy no aceptados. HoldoutUNKNOWN/lock/targetdeferral.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](research/R-020_preregistration_readiness_RC6.md), [configEQ3](research/R-020_configuration_completion_RC1.md), [DataCards](research/R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](research/R-007_protection_dependency_contract_RC2.md), [RiskRC2](research/R-027_risk_formula_spec_RC2.md) y [engine/QE0](research/R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](research/R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.
