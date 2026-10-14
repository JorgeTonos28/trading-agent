# R-020 / D-011 — protocolo de evaluación RC2

2026-10-14 · RESEARCHING. ADR-016 aprueba O-B conceptual; este protocolo es una **propuesta previa a resultados**, no modelo estadístico definitivo ni preregistro sellado. Strategy V1 OPEN. No backtest de estrategia o dataset confirmatorio consultado. `implementation_locked=true`; target acceptance diferido.

## 1. Estados y orden de gates

Separar `design_status`, `data_admission_status`, `statistical_evidence_status` y `operational_acceptance_status`. Un rechazo de datos no demuestra que una hipótesis económica sea falsa. Estados de evidencia: NOT_EVALUATED, INVALID_DATA_OR_METHOD, INSUFFICIENT_EVIDENCE, INCONCLUSIVE, EVIDENCE_AGAINST, SUPPORT_CONDITIONAL. Ninguno activa Champion automáticamente.

1. Config/hypothesis/failure contract y registry completos.
2. Semántica/rights/PIT/cobertura y engine parity admitidos para el scope de afirmación.
3. **F0 — preregistro de evaluación:** criterios, endpoint principal, comparación, costes, latencias, muestras y métodos congelados antes de resultados de cada fase. F0 no exige elegir ya el ganador D008 ni aceptar Plus/PC personal para cerrar diseño de metodología en Team.
4. Desarrollo2005–2018 para MATR; otros sólo desarrollo declarado y admisible anterior a selección.
5. Selección comparable2019–2022, incluyendo bloques walk-forward; todo resultado de este bloque es evidencia de selección, no confirmación nueva.
6. **F1 — freeze confirmatorio:** después de selección, exposure ledger/M-11 y configuración/selector/protocolo final congelados antes de abrir reserva2023–2026-09-30. Integridad UNKNOWN bloquea apertura; si contaminada, alternativa prospectiva requiere gobierno. Aprobación D008 y permisos efectivos target/DoR son gates propios de estrategia/implementación/operación, no requisitos anticipados de F0.
7. Confirmación independiente, luego target/forward/PAPER/promoción. Cambiar reglas tras confirmación fallida requiere nueva versión y evidencia nueva.

## 2. Registro íntegro y familia de pruebas

[Registry](experiment_registry.json) mantiene ideas/variantes declaradas y **cero backtests ejecutados** actualmente. Antes de cualquier ejecución registrar ID/parent/hypothesis, cambios, source/config/dataset hashes, universo/calendario/feed, clocks, ventanas, engine, costs, selector, exposición previa, seed, responsables y timestamp. Toda ejecución termina con receipt SUCCESS/ERROR/ABORTED/TIMED_OUT/INVALID, artifacts y motivo de descarte; nunca borrar negativos.

Separar `declared_variant_count`, `executed_trial_count`, `unique_spec_count`, `execution_attempt_count` y `selection_dependent_trial_count`. Repetir exactamente una ejecución para recovery cuenta como attempt y debe demostrar identidad; no crea independencia estadística. Cambios de universo, actor, mapping, ventana, indicador, stop, costes o selector informados por resultados son ensayos de selección. Sensibilidades ex ante marcadas DIAGNOSTIC también cuentan si se usan para escoger. Un ensayo sin resultado utilizable queda registrado; no inventar p-value para él ni ocultar un resultado observado antes del fallo.

No usar el número de finalistas como número total de pruebas. Si existen resultados externos relevantes usados para diseñar, registrarlos como exposición; no inventar su búsqueda completa ni tratarlos como ensayos propios observados. Familia confirmatoria y criterio principal deben declararse antes; secundarios descriptivos y ablations no sustituyen el endpoint cuando éste falla.

## 3. Propuesta de estadística y reutilización

[DSR, fuente de autores](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf) considera longitud, momentos de retornos, distribución de Sharpe y ensayos efectivos. [PBO/CSCV](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) estudia si el selector in-sample termina por debajo de alternativas out-of-sample. Ambos son diagnósticos candidatos, no permiso automático ni garantías. No llamar PBO a una fórmula de conteo de trials; necesita matriz comparable completa. CSCV no reemplaza validación cronológica ni acredita PIT.

Recomendación candidata: retornos diarios **de cartera**, netos y alineados, más diferencia pareada frente a benchmark; intervalos por bloques temporales comunes preservando dependencia entre activos/candidatos. No bootstrap iid de trades superpuestos. [arch](https://bashtage.github.io/arch/bootstrap/timeseries-bootstraps.html) ofrece stationary/circular; [block length](https://bashtage.github.io/arch/bootstrap/generated/arch.bootstrap.optimal_block_length.html) es una estimación con supuestos y requiere sensibilidad. No cruzar artificialmente gaps/regímenes/folds sin regla explícita.

[statsmodels multipletests](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html) ofrece Holm/Bonferroni; `method='holm'` explícito, sin confiar en default distinto. Propuesto controlar familia de inferencias con p-values válidos para dependencia temporal; un ajuste no arregla p-values mal calculados. DSR/PSR y PBO complementan la lectura cuando sus inputs son suficientes. No elegir el método que resulte favorable. `N_effective_trials` desconocido no se sustituye por1; sensibilidad conservadora y estado NO_ESTIMABLE si no defendible.

Build-vs-Reuse: arch y statsmodels son candidatos **REUSE_AS_IS + WRAP** para primitives, SELECTED=NO, compatibilidad target/versiones UNKNOWN. Licencias públicas [arch](https://raw.githubusercontent.com/bashtage/arch/main/LICENSE.md), [statsmodels](https://raw.githubusercontent.com/statsmodels/statsmodels/main/LICENSE.txt); retener avisos si se distribuyen. Métodos públicos DSR/PBO REFERENCE_ONLY hasta implementation/source/license/paridad validadas. No pagar por metodología ni construir suite estadística general antes de evaluar primitives existentes.

Economía por candidato software: PAPER_V1_VIABLE_FREE=CONDITIONAL, PAPER_V1_COST=licencia0+hardware/integración UNKNOWN, LIVE_COST=licencia0+escala/operación UNKNOWN, FREE_ALTERNATIVE=primitives OSS/papers de referencia, PAID_INCREMENTAL_VALUE=soporte/ejecución sólo si gap material demostrado, ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. No instalado ni seleccionado paquete por este documento; fixture propio pequeño sólo prueba contratos, no sustituye estimador robusto.

## 4. Suficiencia antes de interpretar

Coverage: todas las sesiones/eventos exigidos por regla tienen datos válidos o estado de abstención/reconciliación contabilizado; los huecos no se eliminan selectivamente. Quarantined/missing/delisted/splits/halts y no-trades quedan en denominadores. Rights/PIT/ambiguous fills son gates independientes, no compensables por Sharpe.

Reportar sesiones, señales únicas, episodios de posición, fills, holding overlap, clusters por fecha/actor/issuer y concentración de P&L. Fills parciales no aumentan señales; tres compras de un mismo evento no son tres observaciones independientes. Para13F, reportar publicaciones/trimestres efectivos; número de filas o activos no multiplica historia temporal. Autocorrelación/cluster dependence se diagnostican; **no existe mínimo universal de30/100 trades que acredite alpha**.

`EvidenceRequirementCard` se debe cerrar antes de resultados con: efecto económico mínimo relevante/endpoint, benchmark, error familia/power o precisión requerida, método de dependencia, mínimo de clusters/regímenes/folds y banda de incertidumbre admisible. Estos valores siguen OPEN, no escogerlos después para pasar. [Power statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestPower.solve_power.html) exige efecto, alpha, power/n y supuestos; no aplicar iid t-test a trades correlacionados como si resolviera la muestra.

Propuesta de reglas determinísticas: requisitos ausentes => NOT_EVALUATED y F0 no congelable; requisito declarado pero muestra efectiva/precision/regímenes insuficientes => INSUFFICIENT_EVIDENCE. La interpretación compara el endpoint con **efecto económico mínimo preregistrado**, no sólo con cero: intervalo compatible con alcanzar y no alcanzar ese efecto => INCONCLUSIVE; evidencia válida contraria a ese criterio => EVIDENCE_AGAINST. SUPPORT_CONDITIONAL exige inputs/método/muestra válidos y satisfacer el criterio del endpoint, con scope SELECTION o CONFIRMATION explícito; soporte de selección no certifica alpha confirmada. Selección operacional de un demostrador no equivale a afirmación de alpha; la promoción exige sus gates.

## 5. Walk-forward, sensibilidad y costes

Propuesta calendario: folds de evaluación2019,2020,2021,2022; cualquier entrenamiento/calibración de un fold usa sólo pasado anterior al cutoff. Desarrollo de MATR anterior2019 conserva baseline. Si se ajusta a partir de un fold ya visto, siguientes folds pueden ser forward para esa versión, pero no se reetiquetan resultados previos como no vistos ni se oculta selección al juntar cuatro años. Config fija puede evaluarse por bloques sin llamarlo entrenamiento ML. Warm-up no produce P&L scored; estado/cash/posiciones en bordes se modelan con política común, sin reseteos favorables.

Purga de labels/episodios que usan futuro al estimar modelos; embargo y warm-up se derivan de horizonte/lookback/dependencia, no default elegido por retorno. Bootstrap/CSCV exploratorios no habilitan mezclar pasado/futuro en live simulation. Vecindarios de parámetros declarados antes, cambios one-at-a-time o diseño factorial con presupuesto de ensayos explícito; prohibido escoger el mejor vecino silenciosamente. Costes escenarios0/1/2× sólo diagnósticos propuestos,0 nunca caso principal; magnitudes spread/fees/slippage reales pendientes de broker/feed. Cash/dividendos/benchmark reinversión, taxes scope y fills conservadores coherentes.

## 6. Horizonte, retrasos y checklist de freeze

[Contrato temporal RC0](R-020_decision_horizon_latency_RC0.md) exige separar disponibilidad de fuente, recepción, cálculo, queue, Risk, dispatch, ack y fill. Delays0/1/2/5 sesiones propuestos para EOD/disclosures; intraday/auction usa cortes temporales propios. Simular retraso cambia dato utilizable y fill, no sólo restar coste a mismo precio ideal. Expiración, cancel/reconcile, protección/cash y cuantiles de workload target deben coincidir con backtest assumptions. Late Shadow es LATE, no contemporáneo ni HOLD implícito.

Checklist F0: configs evaluables por candidato, admisión por dataset/scope, registry/exposure conocido, EvidenceRequirementCard, métodos/versiones/semillas, calendario/folds, benchmark/cost/latency y engine parity protocol. F1 añade candidato/selector final e integridad confirmatoria auditada. Permisos efectivos/target acceptance, DoR y aprobación de Strategy/implementación se conservan en sus gates separados, sin exigirlos para investigar/completar F0 en Team. Este RC2 no cierra D011 por sí mismo ni cambia fechas/números de riesgo.

[E2 posterior](R-020_eval_findings_2026-10-14.md) prueba dos primitives y estados sintéticos19/19, sin seleccionar método ni alcanzar F0. [EvidenceRequirementCard](EvidenceRequirementCard_RC0.json) mantiene explícitos campos aún nulos; [Q056](D-011_economic_endpoint_decision_RC0.md) propone decisión sobre preferencia económica retorno/riesgo antes de elaborar efecto mínimo y muestra. Esta card no es un preregistro sellado ni permiso de abrir resultados.

## MethodApplicabilityCard obligatoria

Por método registrar frecuencia/annualización/benchmark, endpoint y dependencia serial/cross-sectional, momentos/longitud de muestra, familia completa y inputs faltantes. PSR/DSR requieren justificar además dependencia de retornos y estimación entre trials; no reemplazar T por N_effective sin derivación validada. CSCV/PBO necesita matriz/cohorte/selector completos y particiones válidas para dependencia temporal: la limitación de autocorrelación del paper §5.1 se evalúa, no se sortea barajando sesiones. Holm exige p-values válidos y familia previa; no corrige por sí solo búsqueda adaptativa oculta. Inaplicabilidad => NO_ESTIMABLE con motivo; no sustituir por otro método favorable después de mirar resultados. Valores/modelo final continúan OPEN.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](../decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Especialización económica posterior — RC3

Q056 DECIDED/ADR017. [RC3](R-020_economic_qualification_contract_RC3.md) concreta endpoint conjunto, cash/λ propios, estados/NO_ESTIMABLE, incertidumbre y familia. [Q057](D-011_benchmark_qualification_decision_RC0.md) es referencia material propuesta, no números aprobados; EvidenceCard todavía null en benchmarks/márgenes/modelos y F0 no congelable. Mantener F0/F1, holdout UNKNOWN y distinción aceptación target. E3 demuestra componentes, no cobertura estadística.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](../decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Inferencia y streams posteriores — wave06

[Inferencia y streams posteriores](R-020_statistical_method_contract_RC4.md) añade especificación y límites; Q057 aprobado en paquete, Q058 números propuestos. Sin fuente/modelo/Strategy admitidos ni performance. E4 sólo cálculo/meanpilot, no cobertura CAGR/ES/DD; M11 parcial/holdoutUNKNOWN. Versiones/declaraciones anteriores conservadas, no rehash histórico.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](../decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.
