# Q-056 / D-008–011 — objetivo económico del comparador

2026-10-14 · **DECIDED opción B por owner, ADR-017; propuesta original conservada**. Este problema es distinto de O-B ya aprobado. Strategy OPEN; no resultados de candidatos vistos. [Scorecard](R-020_comparable_candidate_scorecard_RC2.md) y [protocolo](R-020_evaluation_protocol_RC2.md).

## Problema que necesita gobierno

La hoja §23 exige lógica explicable, resultado neto OOS y riesgo/robustez, y §22 prohíbe promover por una sola métrica. Falta concretar **qué mejora económica primaria** queremos exigir: más retorno neto a riesgo comparable o preservar retorno reduciendo pérdidas/exposición. Sin esa elección no puede fijarse efecto económico mínimo ni diseñar potencia/precisión suficiente para el endpoint. El Plan Architect puede especificar tests, pero no inventar la preferencia retorno/riesgo del propietario ni ajustar el objetivo al resultado observado.

No es necesario que el propietario escoja alpha/power/fórmula ahora. Primero elegir dirección económica, luego elaborar propuesta técnica numérica y contract preregistrable antes de resultados. No elegir ganador, broker, thresholds de riesgo o un modelo estadístico por esta pregunta.

| Dirección | Qué sería éxito económico, además de gates | Trade-off |
|---|---|---|
| A — retorno incremental | Mejorar retorno neto frente a benchmark definido con presupuesto/exposición/riesgo comparables; drawdown/costes como restricciones independientes | Fácil confundir beta/exposición con alpha; exige efecto mínimo/risk normalization y suficiente muestra |
| **B — eficiencia retorno/riesgo (recomendada)** | Conservar retorno neto dentro de margen de no inferioridad preregistrado y reducir riesgo definido, frente a benchmark común; ambos endpoints requeridos | No prometemos superar CAGR; puede aceptar menor retorno dentro de margen a cambio de reducción material de riesgo. Margen/medida/muestra por definir |
| C — demostración operacional sólo | Escoger diseño por claridad/data/operación y aprender, sin afirmación de mejora económica | Útil para prototipo, pero no satisface por sí solo gates de mejora/promotion ni confirma alpha; no elimina metodología ni backtests |

**Recomendación:** B para una primera estrategia long-only con control determinístico, A como lectura secundaria; no ordenar automáticamente por Sharpe/Calmar. Es una recomendación normativa sobre objetivo, no evidencia de que un candidato mejore riesgo o retorno. En B retorno neto y riesgo medido usan misma base/calendario; margen de no inferioridad y reducción mínima de riesgo se fijan antes de resultados, no se deducen del mejor candidato. Máximo drawdown es path-dependent: el método/intervalo necesita validación, no un t-test de trades ni una cifra aislada. Cash/uninvested periods se incluyen; no igualar riesgo mediante leverage/short no autorizados. Las exposiciones y drawdown tolerables de Risk Policy siguen separados.

Podemos continuar documentando fuentes/brokers y pruebas de contratos independientemente, pero cerrar el endpoint primario de F0 y declarar candidatos estadísticamente comparables exige esta preferencia material. Alcance de aprobación pedida: **A/B/C dirección del objetivo de evaluación**, no muestra/p-values/márgenes/umbral numérico todavía. Formalizar contrato técnico después; owner aprueba los cambios materiales que correspondan. No reinterpretar B como permiso de pérdidas nuevas ni exención de resultado neto OOS/§23. Separar estas opciones del **probe E2** estadístico, que sólo es evidencia sintética.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](../decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.
