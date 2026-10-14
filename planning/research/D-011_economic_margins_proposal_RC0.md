# Q-058 — márgenes y efecto mínimo económico PRICE–MATR

2026-10-14 · READY_FOR_DECISION tras revisión independiente; propuesta nueva, no aprobada. Q056/B y Q057/K2 decididos; no se vuelven a preguntar. D011 RESEARCHING, fuentes no admitidas, F0 incompleto y reserva UNKNOWN.

## Decisión material propuesta

Recomendar **M1** para la cohorte ETF, a aprobar antes de observar resultados relevantes:

| Magnitud | M1 recomendado | Significado |
|---|---|---|
| δ_NI | **1 punto porcentual de CAGR/año** | Máxima inferioridad competitiva frente a EW6-BH que el bound debe excluir superar; no basta el point estimate |
| ε_cash | **1 punto porcentual de CAGR/año neto adicional** | Exceso mínimo frente a B-CASH, después de fricciones y costes incrementales asignados; efectivo pasivo no satisface sólo por bajo DD |
| ρ_ES | **20% de reducción de ES diario** frente a espejo apropiado | Diferencia material, no una mejora decimal aislada; comparación positiva/estimable y defendible por composición/beta/factores |
| q_ES | **95%** | Media de la peor masa5% de pérdidas diarias, fractional/ties definidos; no VaR ni pérdida máxima |

M1 **no** selecciona estrategia, dataset/cashsource/broker/capital, método de inferencia/bloques/α definitivo, límites financieros o implementación. Guarda las condiciones de K2/B; la aprobación económica no afirma poder demostrar M1 con2019–2022. Guardrails DD/vol/recuperación se especificarán antes de F0 y no pueden quedar omitidos porque ES pase.

## Fundamento de utilidad, sin datos observados

No existe un paper que determine cuánto retorno desea ceder el propietario por riesgo. Estos son presupuestos de utilidad propuestos, no constantes estadísticas óptimas. δ1pp limita deterioro de oportunidad: con benchmarks hipotéticos5–10% CAGR y4años, una estrategia exactamente1pp inferior termina aproximadamente3.6–3.8% por debajo en riqueza relativa. Permitir2pp ampliaría esa pérdida alrededor7.1–7.4%;0.5pp la reduciría a1.8–1.9%. No son forecasts ni retornos observados; la elección requiere owner.

ε1pp establece una utilidad adicional que debe quedar después del coste de oportunidad y del coste operativo incremental pertinente. K no seleccionado: coste fijo anualF representa aproximadamenteF/K puntos de retorno, además de fees/slippage ya en ledger. Con F240USD ficticio, carga anual sería2.4pp en K10000USD y0.96pp en K25000USD. No aprobar esos capitales/presupuestos ni restar dos veces fees. Si costes/source/scale desconocidos, economía operacional no certificada aunque la métrica de trading pase.

NI y cash evalúan S **net_after_incremental_ops**; ES financiero evalúa **net_trading**, igual al espejo en convención de mercado. Ambos streams visibles; benchmarks con sus costes propios, sin repartirles overhead de agentes para borrar oportunidad. F se asigna a S según uso/escala y accrual preregistrados, no cargo financiero real autorizado. Capital/costes UNKNOWN => NOT_EVALUATED para claim económico operacional; aprobar ε no los admite ni selecciona.

ρ20% es una diferencia que afecta el downside en vez de premiar una mejora pequeña: por cada ESref positivo de1unidad, objetivo≤0.8unidades, con bound y estabilidad. 10% exige menos,30% más; ninguno se escoge mirando ganador. Cola95 ofrece nominalmente50.4observaciones extremas en1008sesiones frente25.2a97.5 y10.08a99. Esto **no** demuestra50clusters independientes ni cobertura; motiva candidato95 antes de resultados, con sensibilidad/tails/guardrails y riesgos no observados visibles.

## Alternativas explícitas

- **M0 más restrictivo en retorno:** δ0.5pp, ε1pp, ρ20%, q95. Menor pérdida de oportunidad, más evidencia para NI; no garantiza mejor estrategia.
- **M1 recomendado:** δ1pp, ε1pp, ρ20%, q95. Presupuesto pequeño de retorno frente a mejora de riesgo sustantiva y cash premium positivo.
- **M2 mayor tolerancia de retorno:** δ2pp, ε1pp, ρ20%, q95. Permite un coste de oportunidad aproximadamente doble; no recomendado por facilidad de muestra. No alterar ε/ρ para hacer pasar.

También es válido rechazar los números o proponer otro presupuesto antes de resultados. No aprobar «elegir el que la muestra soporte»: precisión insuficiente mantiene INSUFFICIENT_EVIDENCE / NO_STRATEGY_QUALIFIED.

## Evidencia estadística y límites

[RC4](R-020_statistical_method_contract_RC4.md) distingue ES(S)-ES(M) de ES(S-M), contraste sin ratio pero referencia positiva/estimable, familia y bloques. [E4](R-020_E4_findings_2026-10-14.md) muestra que independencia falsa puede inflar rechazo y que cuatro años ficticios no garantizan potencia. No usar sus tasas para escoger márgenes ni prometer que M1 se demostrará. La simulación no valida CAGR/ES/DD, α conjunta, block20 o cuotas target.

Después de decisión: completar guardrails y MethodApplicabilityCard, precisiones/muestra/familia/errores con calibración adecuada a los estimandos, fuente prices+corporate events+cash y paridad. Todos se congelan antes de evaluar. Integridad UNKNOWN bloquea confirmación, sin modificar ventanas ni abrir reserva para estimar potencia. **No se pide otra preferencia económica abstracta**, sino un nuevo límite numérico de pérdida/beneficio aceptable.
