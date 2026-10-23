# ADR-016 — evaluación y comparación de candidatos: O-B

**Fecha:** 2026-10-14. **Estado:** DECIDED / aprobación conceptual acotada. **Autoridad:** propietario, instrucción directa. **Q-055:** DECIDED. **D-011 global:** RESEARCHING; **Strategy V1:** OPEN. Complementa ADR-004/005/015. No selecciona estrategia, datos, broker, parámetros, modelo estadístico ni acredita rentabilidad.

## Decisión

Conservar ventanas propuestas MATR: desarrollo2005–2018, selección-validación2019–2022 y reserva confirmatoria2023–2026-09-30. Otros candidatos participan sólo con datos, cobertura, derechos y semántica PIT admisibles. La comparación directa usa períodos/base económica homogéneos. La confirmación es independiente de la selección.

## Siete condiciones del propietario

1. **Integridad:** reserva2023–2026-09-30 sigue `PROPOSED_RESERVE / INTEGRITY_UNKNOWN` hasta auditar exposure ledger/M-11. No declararla intacta por ausencia de backtests. Si está contaminada, presentar alternativa prospectiva al propietario antes de usar resultados; tampoco abrirla mientras la integridad no esté resuelta.
2. **Múltiples pruebas:** registrar todas las estrategias, variantes, parámetros, experimentos y resultados descartados. Evaluar sesgo de selección y robustez estadística; no escoger sólo CAGR/Sharpe observado ni omitir ensayos fallidos.
3. **Muestra:** fijar cobertura, número efectivo de señales/operaciones, regímenes y evidencia mínima antes de consultar resultados. Insuficiencia produce `INSUFFICIENT_EVIDENCE`, no conclusión favorable/desfavorable artificial.
4. **Comparabilidad:** mismos períodos, benchmarks, costes, calendario y contabilidad para comparación directa. No rankear retornos de épocas distintas como equivalentes.
5. **Tiempo y robustez:** incluir walk-forward, sensibilidad de parámetros y costes/retrasos apropiados. Congelar configuración y protocolo antes de confirmación; cambios posteriores requieren nueva evidencia confirmatoria.
6. **Decision Horizon & Latency:** registrar horizonte de decisión, latencia admisible, caducidad, disponibilidad/generación/ejecución y simulaciones de retraso por candidato. Retorno de backtest no demuestra viabilidad operacional; protección local continúa independientemente de jobs AI.
7. **Historia insuficiente:** mantener investigación o validación prospectiva, sin waivers PIT ni selección informal mediante holdout.

## Dependencias y gobierno

[Propuesta original](../research/D-011_OOS_policy_decision_RC0.md) conserva alternativas O-A/O-C y review. Q055 cerrado sólo en arquitectura conceptual; D011 necesita protocolo estadístico, muestra/criterios/ensayos/exposure ledger, costes/latencias/datasets/engine y evidencia. D008 necesita candidatos comparables y recomendación fundamentada, no ranking de retornos. D010/021/022/023/025/026/028/029/033/034/035 y D030/031/032 mantienen sus scopes pendientes.

`implementation_locked=true`; `TARGET_ACCEPTANCE_DEFERRED`. No gasto, broker/auth/admin/Plus, implementación ni promoción main/release. R006/010/013 fundamentales no se reabren. Precios/backtests ejecutables/aceptación operational target PC personal; diseño, metodología, documentación y probes sintéticos sin secretos pueden continuar en Team.
