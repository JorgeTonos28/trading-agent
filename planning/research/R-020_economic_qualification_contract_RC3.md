# R-020 / D-011 — contrato económico de calificación RC3

2026-10-14 · propuesta técnica bajo ADR-017; no márgenes/modelo/benchmark finales aprobados. F0 NOT_FROZEN, Strategy OPEN, holdout INTEGRITY_UNKNOWN. Ningún rendimiento de candidato consultado. Este documento concreta B, no pide otra aprobación conceptual equivalente a Q056.

## 1. Cuatro dimensiones independientes

Registrar diseño/data admission, calificación económica, integridad confirmatoria y aceptación operacional por separado. Operación confiable (C) no valida economía. Datos inválidos no prueban hipótesis económica falsa. Evaluación A se conserva secundaria. Si ninguna estrategia cumple => NO_STRATEGY_QUALIFIED con razón por candidata; no escoger menor defecto ni recortar márgenes tras resultados. Hoy todas siguen NOT_EVALUATED, no FAIL económico.

## 2. Benchmarks propuestos para PRICE–MATR

USD como moneda **de comparación propuesta**, no elección de capital operativo ni tratamiento fiscal. Misma fecha/calendario/feed/costs/dividendos/settlement y equity total incluidos cash/reservas/fees. Mismo período2019–2022 para comparación; conservar desarrolloMATR2005–2018 y reserva condicional2023–2026-09-30.

| ID | Regla de referencia propuesta | Papel y límite |
|---|---|---|
| B-EW6-BH | SPY/QQQ/IWM/EFA/TLT/GLD a igual peso inicial, buy-and-hold con pesos que derivan, política corporativa/dividendos/cash versionada | Referencia principal propuesta de oportunidad del mismo universo, preservando benchmark baseline equal-weight buy-and-hold. Incluye costes/cash por eventos; no fill ficticio ni índice gratis sin fricción |
| B-EW6-MONTHLY | Igual universo/peso con rebalance primer evento autorizado de cada mes desde información anterior | **Referencia nueva propuesta**, distinta de B-EW6-BH; sólo sensibilidad/alternativa, no reemplaza baseline ni se selecciona por retorno |
| B-CASH | Referencia monetaria USD pública, calendario/lag/base/roll/fees explícitos | Hurdle obligatorio; retorno broker real del cash se registra aparte. Referencia no acredita accesibilidad/retorno ejecutable para la cuenta RD |
| B-LAMBDA-REAL | Antes de cada intervalo usar fracción arriesgada conocida de S, λ∈[0,1], y cesta de referencia en esa fracción; resto **carry real equivalente al cash de S**, con ledger propio/costs | Atribución de exposición: no usa λ futuro ni escala S con leverage. Extra-turnover del espejo se muestra; espejo no es estrategia autónoma desplegada. No imputar T-bill proxy al ledger S |
| B-SPY / SMA200-SPY | Buy-and-hold y regla SMA200 predefinida, costes/dividendos iguales | Contexto secundario, no sustituir referencia principal si falla ni seleccionar benchmark por resultados |

B-EW6-BH puede invertir más posiciones/exposición que Champion top3; esa diferencia se muestra y B-LAMBDA-REAL la contrasta. No afirmar presupuesto/autoridad Risk idénticos de buy-and-hold100% y candidato capado: benchmark de oportunidad es hipotético, no intent operativo ni permiso de saltar límites. Un comparador adicional con mismos caps operativos puede definirse antes de resultados, sin reemplazar el principal oportunistamente.

`r_lambda,t = λ_(t-1)*r_basket_GROSS,t + (1-λ_(t-1))*r_cash_REAL,t - cost_MIRROR,t` sólo es descomposición diagnóstica de intervalo con supuestos explícitos: basketGROSS excluye cash/fricciones, costMIRROR son **costes totales propios** del espejo, no otro débito sobre retorno EW ya neto. Para admisión usar ledger completo de weights/shares/acciones/cash/fees/rebalance, evitando doble coste/carry. No es fórmula productiva. Espejo con cash de oportunidad podría reportarse aparte B-LAMBDA-OPPORTUNITY; no mezclarlo con attributionREAL ni crédito a S. Si λ usa holdings finales/volatilidad futura, ORACLE_DIAGNOSTIC, nunca evidencia contemporánea.

Clock λ: valor del estado reconciliado **conocido al inicio de cada intervalo**, con snapshot/mark/qty/equity/source/time. Si S entra/sale intraday, el espejo por λ del cierre anterior no iguala exposición intraday: partir ledger en intervalos por fills/cambios con información entonces disponible, costes propios y precios/clock admisibles. Si sólo hay λEOD/medias ex post, resultado MATCHED_EXPOSURE_DIAGNOSTIC_LIMITED, no gate confirmatorio de eficiencia. No conocer fill futuro para negociar espejo antes; modelo de reacción/delay común explícito.

## 3. Endpoint conjunto propuesto

Retornos diarios de cartera netos de fricciones y cash real, equity total sin flujos externos mezclados con P&L. CAGR = `(V_T/V_0)^(365.25/días_calendario)-1`, con rendimiento unitizado si flujos; no CAGR por días invertidos. Definir precios mark/payout/reinvest y retornos de benchmark igual.

Propuesta conservadora AND, ningún score ponderado puede compensar un gate fallido:

1. **Competitividad:** límite inferior de ΔR = CAGR(S)−CAGR(B-EW6-BH) ≥−δ_NI. δ_NI es pérdida anual máxima aceptable por owner antes de resultados, no función del intervalo observado ni del ganador.
2. **Oportunidad:** límite inferior de Δcash = CAGR(S)−CAGR(B-CASH) > ε_cash, efecto mínimo neto adicional aprobado. ε_cash≥0 no sustituye coste total: presupuestar datos/infra/modelo/operación cuando aplique y mostrar retorno antes/después del coste fijo por capital/escala. No capital seleccionado; relación coste mensual/equity queda parámetro.
3. **Riesgo material:** límite superior de ES(S)/ES(B-LAMBDA-REAL) ≤1−ρ_ES, con ES de pérdida diaria de cartera al nivel q predefinido. λ matched no garantiza beta/mix idénticos: reportar composición/beta/exposición y límites del estimador. Denominador cero/no positivo/inestable => NO_ESTIMABLE, no ratio0. Comparar también riesgo frente a B-EW6-BH completo, sin vender simple reducción de λ como eficiencia adicional.
4. **Guardrails:** drawdown, volatilidad y recuperación/underwater en referencias completas y matched; efectos/bounds especificados antes de resultados. Deterioro material en alguna guardrail no se oculta con ES favorable. Último drawdown no recuperado es censurado, no recovery0. Límites financieros D031 siguen distintos de umbrales de comparación económica.

ES/pérdida extrema es candidato primario por centrarse en downside; volatilidad primaria alternativa puede resultar más estimable pero no describe cola. La elección y q/modelo definitivo siguen propuesta: no elegir métrica que pasó después de abrir resultados. Una mejora sólo frente al benchmark completo, desaparecida frente al espejo λ, queda REDUCED_EXPOSURE_ONLY, no PASS global. Cash-only bajo mismo retorno monetario tiene exceso0 y no cumple ε_cash positivo; cash real distinto del proxy puede tener otro exceso, por lo que no inferir FAIL universal. En cualquier caso σ/DD0 no acredita eficiencia activa y ES inestimable conserva su subestado; una referencia monetaria superior puede ser razón para no seleccionar estrategia.

MethodApplicabilityCard ES: convención loss=−return o clippedloss (distintas, por elegir antes), cuantiles/ties/cola efectiva y regla de réplicas con ESdenominador no positivo/inestable. No eliminar esas réplicas ni clippear ratios para estrechar CI. Reportar proporción problemática y motivo; datos mal escalados/método inválido => INVALID_DATA_OR_METHOD, cola escasa/denominador sin precisión => INSUFFICIENT_EVIDENCE con diagnóstico NO_ESTIMABLE. No ratio0 ni FAIL automático, no método alternativo elegido por resultado.

## 4. Incertidumbre y selección múltiple

Proponer bloques temporales comunes de vectores S/B/CASH/λ, índices/semilla/versiones almacenados; bootstrap de cartera, no trades iid/activos como repeticiones. Recomputar CAGR/ES/DD de cada path; estacionariedad, dependencia/regímenes y cola efectiva deben validarse. La reconstrucción de path por bloques altera episodios y recuperaciones: DD/underwater requieren sensibilidad/censura y no garantizan tail risk futuro. No annualizar ES diario multiplicando252 ni asumir regla√252 para dependencia sin diagnóstico.

[arch confidence intervals](https://bashtage.github.io/arch/bootstrap/confidence-intervals.html) permite one-sided/elementwise intervals. **Vector de intervalos95% no implica cobertura conjunta95%**. Propuesta de inferencia AND/intersection-union: éxito requiere todos endpoints; error global entre candidatos/familias se controla adicionalmente. Un ajuste Holm/Bonferroni no valida bootstrap ni búsqueda adaptativa. Método/α/reps/block selection y familia se preregistran antes; one-sided tests no reutilizan confirmación.

[NI, referencia metodológica FDA](https://www.fda.gov/media/78504/download): fijar margen/efecto justificables antes y planificar muestra; es analogía estadística, **no** estándar financiero ni transferencia de márgenes clínicos. Para Trading OS, δ/ε/ρ expresan utilidad/pérdida aceptable del owner y calidad de evidencia propia; literatura no los aprueba.

## 5. Estados y límites de evidencia

- DATA_OR_METHOD_INVALID: clocks/rights/inputs/estimador inválidos => no evaluación económica admisible.
- NOT_EVALUATED: faltan parámetros/benchmarks/criterios aprobados, no F0 congelable.
- INSUFFICIENT_EVIDENCE: cola/clusters/regímenes/precision/power preregistrados insuficientes; no convertir ausencia de significancia en prueba de inferioridad.
- INCONCLUSIVE: inputs/muestra/método adecuados pero incertidumbre cruza criterio; no PASS.
- FAIL: evidencia válida de violación del criterio predefinido o guardrail material incumplida; presentar razón. Fallar calificación no equivale siempre a estrategia con pérdida absoluta.
- PASS_SCOPE_SELECTION / PASS_SCOPE_CONFIRMATION: todos gates cumplidos para scope declarado, modelo/thresholds registrados; no activación/promoción ni LIVE automática. En estados RC2 se representa SUPPORT_CONDITIONAL con scope y gates; no reemplaza el registro de evidencia.

Mapeo a RC2: DATA_OR_METHOD_INVALID corresponde INVALID_DATA_OR_METHOD; NO_ESTIMABLE es diagnóstico, no resultado económico standalone. FAIL inferencial corresponde EVIDENCE_AGAINST para criterio explícito, mientras no superar un bound por incertidumbre puede ser INCONCLUSIVE/INSUFFICIENT, nunca FAIL estadístico automático. Un guardrail determinístico violado tiene motivo propio. Retener estado de cada endpoint y agregado, no traducir todos los noPASS a estrategia «mala».

NO_STRATEGY_QUALIFIED es agregado: ninguna PASS económica válida; conservar subestados para distinguir todo insuficiente de evidencia contra todos. Gate operacional separado OP_NOT_TESTED/OP_PASS/OP_FAIL nunca completa PASS económico. Confirmación sigue bloqueada por integridad UNKNOWN.

## 6. Justificación previa de márgenes y muestra

Preparar δ_NI en puntos porcentuales/año y pérdida de oportunidad en unidades de equity, comparándolo con ε_cash, efecto de riesgo y costes/escala. No derivarlo del Sharpe del ganador ni ampliarlo para que cuatro años basten. ρ exige mejora que sobreviva modelo/bloques/costs/delays y no sólo decimal en DD. Guardrails/regímenes se congelan sin usar retornos para elegir fechas favorables.

Muestra efectiva: sesiones y eventos/clusters, holding overlap, cantidad de cola q, dispersión entre bloques y calendario de regímenes. Estimar power/coverage bajo hipótesis simuladas diversas con nulidad e inferioridad/cash-only/exposure-only; no extraer efectividad de un único syntheticPASS. Controles de múltiples trials y DSR/PBO de RC2 se preservan cuando aplicables. [Probes de especificación](probes/r020-economic-contract/README.md) verifican direction/contabilidad y sensibilidad de muestra, no desempeño de candidatos.

Números definitivos δ/ε/ρ/q/α, método y mínimos de muestra todavía **no aprobados**. El siguiente checkpoint humano sólo procede con propuesta técnica material y fundamento, conforme ADR017; no volver a pedir la misma dirección conceptual. Con cuatro años no se presume que cualquier margen estrecho sea demostrable.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](../decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Especialización posterior — wave06

[Especialización posterior](R-020_statistical_method_contract_RC4.md) añade especificación y límites; Q057 aprobado en paquete, Q058 números propuestos. Sin fuente/modelo/Strategy admitidos ni performance. E4 sólo cálculo/meanpilot, no cobertura CAGR/ES/DD; M11 parcial/holdoutUNKNOWN. Versiones/declaraciones anteriores conservadas, no rehash histórico.
