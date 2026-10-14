# Q-057 — referencias y contrato de calificación PRICE–MATR

2026-10-14 · READY_FOR_DECISION tras revisión crítica independiente; propuesta no aprobada. Q056/B aprobado; **no se repite** elección retorno/riesgo. D008/011 siguen OPEN/RESEARCHING; márgenes/modelos/datos y F0 no aprobados. Holdout INTEGRITY_UNKNOWN.

## Problema concreto

La no inferioridad no tiene significado hasta fijar **contra qué cartera**, con qué cash y qué mejora de riesgo se exige. El roadmap enumera SPYbuy-and-hold, SPY_SMA200, equal-weightbuy-and-hold ycash; no congela una referencia primaria única para esta comparación. Elegir primario distinto cambia qué pérdida de oportunidad se acepta y qué reducción es útil. No decidir ese criterio a partir del mejor resultado observado.

## Propuesta recomendada — paquete K2

Para la **cohorte ETF PRICE–MATR únicamente**:

1. **B-EW6-BH primario**: seis ETF comunes a igual peso inicial, buy-and-hold con drift/corporateevents/dividendos/costs/cash y calendario definidos. Conserva referencia del baseline. SPY ySPY_SMA200 secundarios; EW6-MONTHLY es variante de sensibilidad distinta, no reemplazo automático.
2. **B-CASH obligatorio**: oportunidad monetaria apropiada con fuente/returnmodel/rights/PIT admitidos. Interés broker real se mantiene separado; no dar a S proxyyield inexistente. Medir exceso neto y coste total/escala, no premiar desinversión.
3. **B-EW6-BH-LAMBDA-REAL obligatorio** para separar menor exposición de eficiencia: espejo con estados/intervalos conocidos, cash real equivalente, ledger/costs propio. Sin intradaylambda/precios/clock apropiados, sólo diagnóstico limitado y no pasar gate de matchedrisk. No leverage/shorts.
4. **Calificación conjunta AND**: retorno competitivo al primario, exceso material sobre cash, reducción material de riesgo válida y guardrailsDD/volatility/tails/recovery. No compensación por score ni elegir al menos malo. Estadística insuficiente conserva su estado y permite NO_STRATEGY_QUALIFIED.

ES como métrica primaria de cola y volatilidad como alternativa están investigadas en RC3, **no seleccionadas por esta decisión**. Contrato exige forma matemática/modelo/cola efectivos antes de δ/ρ/criterios definitivos. No usar checks sintéticos o vectorCI marginal para afirmar prueba económica conjunta.

## Alternativas y trade-offs

| Paquete | Referencia principal | Diferencia material |
|---|---|---|
| K1 | SPYbuy-and-hold primario; NI contra SPY y reducción contra SPY-LAMBDA-REAL, más cash/AND | Oportunidad amplia equitiesUS, pero compara cartera6activos (incluye bonds/gold) contra equity100%; requiere explicar beta/mix, no identidad de riesgo |
| **K2 recomendado** | EW6-BH primario; NI contra EW6-BH y reducción contra EW6-BH-LAMBDA-REAL, más cash/AND | Mismo conjunto de activos, referencia simplesin rebalance mensual añadido y separación de exposure. Puede aceptar que SPY supere a ambos; no exige superar100%USstocks como única finalidad |
| K3 | NI contra SPY **y** EW6-BH; reducción válida contra **ambos** espejos SPY-LAMBDA-REAL/EW6-BH-LAMBDA-REAL; cash y todos los gates AND | Mayor exigencia y oportunidad explícita; más criterios/muestra necesaria. No switchingbenchmark si uno falla |

Razón de recomendación K2: vínculo del benchmark con el universo definido de ambos candidatos y preservación de baselineEW_BH; permite leer retorno/risks/opportunity sin seleccionar activos/épocas retrospectivamente. No evidencia de que EW6 o una estrategia tenga mejor rendimiento. No aplicar K2 a Form4/congreso/13F por defecto: esos candidatos requieren universo/benchmark propios antes de comparación.

## Evidencia y alcance de aprobación

[RC3](R-020_economic_qualification_contract_RC3.md) define cash/gross-cost/λ/estados; [cash sources](R-008_cash_benchmark_admission_RC0.md) distingue yields de retornos; [E3](R-020_economic_probe_findings_2026-10-14.md) demuestra counterexample de exposure/cash en fixtures y sensibilidad de muestra. [Pairing](R-020_PRICE_MATR_pairing_spec_RC0.md) conserva cambios/variantes; [Form4](R-021_Form4_semantic_admission_RC2.md) queda candidata no admitida. Ningún backtest histórico/candidato/resultados de reserva observado. La evidencia funda el **diseño del criterio**, no rentabilidad de las referencias.

Decisión pedida sólo: **K1/K2/K3 de referencia primaria y gates conjuntos para PRICE–MATR**. No aprobar δ_NI/εcash/ρ/q/α, capital, modelos, Strategy/broker/data, implementación/operación/target. Después presentar márgenes y efectos técnicos con utilidad y muestra, antes de resultados; no ensancharlos por factibilidad. No nueva ronda abstracta de dirección B ni solicitud Plus/admin. Trading OS sigue bloqueado, main estable.
