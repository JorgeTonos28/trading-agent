# ADR-017 — objetivo económico: eficiencia retorno/riesgo

**Fecha:** 2026-10-14. **Estado:** DECIDED / aprobación conceptual acotada. **Autoridad:** propietario, instrucción directa. Q-056 DECIDED; D-011 global RESEARCHING; Strategy V1 OPEN. Complementa ADR-016/O-B, ADR-015/R2 y controles independientes. No selecciona margen, parámetro, modelo estadístico, estrategia, capital, broker/datos, implementación ni operación.

## Objetivo aprobado

Estrategia económicamente útil y sostenible: retorno neto suficientemente competitivo y reducción material de riesgo frente a referencias adecuadas. **No minimizar riesgo independientemente de rentabilidad** ni escoger ganador obligatorio.

## Ocho condiciones del propietario

1. Retorno respecto a benchmark apropiado dentro de margen de no inferioridad predefinido, técnicamente justificado y **aprobado por owner antes de observar resultados relevantes**.
2. Reducción material mediante métricas adecuadas de drawdown, volatilidad, pérdidas extremas y recuperación; diferencia aislada/frágil no prueba éxito. Efectos mínimos/modelos pendientes.
3. Coste de oportunidad: cash/T-bills u otra referencia monetaria apropiada; medir retorno neto adicional frente a efectivo. Una estrategia desinvertida no gana sólo por drawdown bajo.
4. Exposición comparable: separar eficiencia real de reducir exposición; benchmarks/comparadores de exposición/riesgo sin leverage/shorts no autorizados.
5. A sigue como evaluación secundaria: retorno incremental neto/CAGR/risk-adjusted y benchmarks; ninguna métrica individual selecciona automáticamente.
6. C es gate operacional independiente: funcionamiento confiable no demuestra utilidad económica ni autoriza promoción.
7. Preregistrar márgenes, efecto mínimo de riesgo, incertidumbre/power/suficiencia y PASS/FAIL/INSUFFICIENT_EVIDENCE antes de resultados. No márgenes por conveniencia ex post; F0 sigue incompleto.
8. Si nadie cumple, **NO_STRATEGY_QUALIFIED**, con motivos/estados por candidato; no relajar objetivos ni elegir al menos malo para avanzar. Todos insuficientes no equivalen a demostrar que todas las hipótesis son falsas.

## Estado y secuencia

[Propuesta Q056](../research/D-011_economic_endpoint_decision_RC0.md) conserva alternativas y review. [EvalRC2](../research/R-020_evaluation_protocol_RC2.md) y EvidenceRequirementCard deben concretar endpoint/benchmark/margen/cash/exposición/risk/inferencia conjunta y requisitos de muestra, con propuesta material fundamentada a owner antes de cierre. PRICE–MATR base común y Form4 primera fuente externa candidata continúan; no normalizar riesgo con leverage ni admitir fuente por parsePASS.

Holdout PROPOSED_RESERVE / INTEGRITY_UNKNOWN hasta exposure ledger/M11. `implementation_locked=true`, TARGET_ACCEPTANCE_DEFERRED. No precios históricos/resultados de estrategias, Plus/admin institucional, gasto, main/release o investigación agéntica fundamental nuevos autorizados. Diseño/investigación/probes sintéticos necesarios pueden continuar autónomamente; no solicitar nueva decisión humana salvo propuesta material fundamentada de márgenes/criterios económicos/selección u otro gate real de gobierno.
