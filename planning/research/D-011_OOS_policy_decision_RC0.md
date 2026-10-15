# D-011 / Q-055 — arquitectura de evaluación entre candidatos — propuesta RC0

2026-10-13 · P0 **Q-055 DECIDED por owner2026-10-14, ADR-016; propuesta original conservada** · D-011 global RESEARCHING; Strategy V1 OPEN. No nuevos resultados de estrategias ni dataset confirmatorio consultados en esta wave. No cambios a fechas de MATR por este documento. Selección/validación condicionadas a datos/rights/PIT y configs completas; [R2 ADR-015](../decisions/ADR-015-remaining-risk-reference-R2.md).

## Problema material

Los candidatos tienen fuentes/horizontes diferentes. La ventana2005–2018/2019–2022/2023–2026-09-30 pertenece al baseline MATR, mientras disclosures pueden tener otra cobertura/semántica. El historial de una API no prueba snapshots PIT; [retención](R-008_data_retention_gate_RC1.md) puede impedir reproducibilidad. Usar la muestra final para elegir candidato y luego llamarla confirmación cambia el significado de la evidencia.

La arquitectura de evaluación determina qué candidatos pueden compararse, cómo escoger el primero y qué puede afirmarse después. Proponerla antes de resultados; no elegir por rentabilidad de fuente/video, datos accesibles o defaults engine. No pedir al owner que invente métricas/reglas.

## Alternativas

| Opción | Diseño | Ventaja | Trade-off |
|---|---|---|---|
| O-A ventana uniforme completa | Exigir a todo candidato los tres bloques completos2005+ del baseline | Comparación histórica simple y mismos regímenes | Puede excluir familias por inexistencia/falta de cobertura aunque su hipótesis sea útil; riesgo de confundir fuente con estrategia |
| **O-B cohorts admisibles + confirmation reservada (recomendado)** | Development por candidato previamente declarado antes2019 cuando sea viable; selección comparable2019–2022 sólo para candidatos con coverage/PIT/rights/config suficientes; preservar confirmación2023–2026-09-30 hasta un único candidato/reglas/selector congelados | Conserva baseline MATR y muestra confirmatoria propuesta; separa historia no comparable y prospectivo, evita forzar mezclas de fuentes | No todos podrán entrar a comparación histórica; dataset gates/criterios mínimos pendientes, y puede exigir evidencia prospectiva |
| O-C historia exploratoria y confirmación futura | Usar pasado disponible incluida2023–2026 para investigación/selección, reconocerlo retrospectivo y confirmar desde freeze prospectivo | Permite aprender de más historia/datasets | Renuncia a reserva histórica independiente, alarga validación; no autorizado hoy |

## Contrato propuesto O-B

1. **No modifica MATR**2005–2018 development,2019–2022 selection-validation,2023–2026-09-30 confirmation propuesta. Warm-up anterior sirve a indicadores sin P&L medido en test. Universos/acciones corporativas/retención/versiones y exposure ledger obligatorios.
2. Strategy hypothesis, actor/universe/signal/exit/sizing/costs/engine/failure/data clocks se preregistran por variante, con conteo de ensayos fallidos. Entrada propia distinta cuenta como candidato, no reconstrucción literal del video.
3. Family con data insufficient/PIT no acreditado no participa en scorecard histórico confirmatorio. Puede seguir research/prospectivo/referencia, **sin waivers PIT ni relajación automática de safety**. Ventanas distintas/cohortes no se rankean por CAGR cross-period como si fueran iguales.
4. Comparación2019–2022 usa benchmarks, calendario, contabilidad/dividendos/cash/costs/ejecución comparables y misma base para los candidatos admitidos. Si ese bloque no cumple data/coverage, no inventar periodo nuevo o perder holdout silenciosamente: presentar reevaluación de protocolo al owner antes de mirar resultados.
5. Confirmación2023–2026-09-30 = **PROPOSED_RESERVE / INTEGRITY_UNKNOWN**, hasta revisión del exposure ledger y M-11. La exposición incidental a fichas públicas de emisores ya registrada no se borra. Si no se acredita integridad suficiente, reevaluar protocolo con owner antes de abrir resultados; aprobar O-B no certifica un holdout intacto. Congelar una única configuración y procedimiento de evaluación/criterios antes de acceder a esa reserva. Muestra usada para seleccionar/ajustar/repetir pasa a exploratoria/validation retrospectiva; deja de confirmar independencia de esa selección. Revisión de reglas o nueva selección tras fallo exige nueva evidencia confirmatoria/forward, no rerun maquillado.
6. Actuar como first Strategy **de diseño para implementación** no demuestra alpha ni habilita Champion. Aprobación owner D-008/config congelada + DoR/target acceptance siguen antes de producción; verificación cuantitativa/backtesting/forward/PAPER y promotion gates siguen antes de activar autonomía/proponer LIVE. No implementar core primero para resolver DoR circularmente; probes/desarrollo de spec permitidos, backtests ejecutables PC personal según ADR-013.
7. Métricas de calidad/reproducibilidad/riesgo/costes, criterios mínimos de cobertura/sample y umbrales de continuación aún OPEN; deben fijarse en protocolo final **antes** de la muestra que los juzgará. Elegirlos tras observar rendimiento viola contrato. Esta aprobación conceptual no cierra D-011 completo ni fija Sharpe/p-value/drawdown/regímenes/splits no especificados.

## Recomendación y gobierno

Recomiendo O-B como arquitectura de evaluación, manteniendo O-A/O-C alternativas documentadas. Decisión owner pedida **sólo sobre separación development/selección/confirmación y trato de candidatos con historia incompleta**, no Strategy/broker/data winner ni gasto, ni acceso Plus/admin. Material para selección de primera estrategia y evidencia; AGENTS requiere gobierno cuando alternativas alteran arquitectura/scope. No borrar declaración owner MATR nunca backtesteada; exposición incidental de fichas de emisores ya registrada no acredita untouched OOS por sí sola.

Fundamento metodológico: [CFA Backtesting & Simulation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation) trata hipótesis/reglas, walk-forward, sesgos y escenarios. O-B y ventanas son propuesta propia del proyecto, no recomendación específica de CFA ni garantía de retorno. [Revisión independiente y reparaciones](D-011_R-021_independent_review_2026-10-13.md) habilitan presentar este scope conceptual; no aprobación del owner ni cierre total D-011. Núcleo agéntico ADR-014 completo en su scope, no nueva ronda R-006.

## Aprobación vigente O-B — 2026-10-14

[ADR-016](../decisions/ADR-016-strategy-evaluation-O-B.md) registra Q055 DECIDED conceptual; D011 global RESEARCHING, Strategy OPEN. Reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11; alternativa prospectiva con gobierno si contaminada. Ensayos incluidos descartes, suficiencia/INSUFFICIENT_EVIDENCE, comparabilidad, walk-forward/sensibilidad/costes/retrasos y horizonte/latencia/caducidad quedan exigidos antes de resultados. Ningún modelo/umbral/estrategia/broker/data aprobado; lock y target deferral vigentes. Continúa paquete financiero sin solicitar Plus/admin ni investigación agéntica general.
