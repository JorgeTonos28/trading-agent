# R-020 — siguiente P0 Strategy V1: admisión y preregistro RC1

2026-10-05. R-020 P0 **RESEARCHING**, D-008/selección OPEN. Avance independiente de permisos finales D-027 y Plus. [RC0](../02_strategy_v1_selection.md), ADR-000, ADR-004/005/006 y A+ gobiernan. No ejecutar backtests ni construir Trading OS en este documento.

## 1. Separar lo que mostró el video

La transcripción y fotogramas ya analizados en [dossier del video](video_inspired_strategy.md) distinguen: VID-TS gestión trailing/ladder con entrada exógena y reglas incompletas; VID-CONG disclosures; VID-ALERT señales de tercero con acceso/licencia desconocidos; VID-WHEEL derivados fuera del alcance V1; SIGNAL/SDK/mobile infra/metodología. No forzar estos componentes a una estrategia. 164.99%/72.3% NO VERIFICADOS; no se abre auditoría promocional.

Primer candidato de investigación continúa siendo **familia inspirada en video**: controles de posiciones + señales externas posibles, ahora señales/intents operativos determinísticos. PM shadow aporta comparación, jamás completa reglas operativas ausentes. MATR_V1 sigue benchmark/candidato; sus M-01–11 no se eliminan por aprobación de runtime.

## 2. Paquetes de evidencia antes de scorecard de rendimiento

| Paquete | Qué investigar autónomamente | Cierre necesario |
|---|---|---|
| VID-TS | Tabla de escenarios de stop/ladder/compra en caída y contradicciones; entry-rule todavía ausente | Diseñar alternativas completas, no inferir una entrada del prompt del creador. Parámetros/sizing y conflictos aprobados antes de Champion |
| VID-EXT (incluye VID-CONG, no sinónimo de Smart Money) | Matriz cobertura PIT, latencia, historia, license, coste para SEC Form4/13F, congreso, options/block/analyst/flows; R-023/025 | Fuente/familia admitida ADR-005; transforms y reglas determinísticas, salida y failure-mode completas. LLM no produce intent operativo |
| VID-ALERT | Disponibilidad pública/autorizada y reproducibilidad de timestamps/parser | Sin credenciales privadas/licencia/historia no hacer supuesto de backtest; DEFERRED si acceso material faltante |
| MATR | Resolver cálculos/calendario/warm-up, missing/revisiones y orden/riesgo con fuentes/engine candidate | No aprobar implícitamente porcentajes del borrador; D-031 numérico aparte |
| Comparación plataforma | Dataset sintético de escenarios y contratos frente a motores quant existentes R-009 | Reuse/paridad primero; no BUILD backtester propio ni crear broker adapter en preparación |

## 3. Preregistro antes de mirar resultados

Cada variante requiere ID/parent/hash, hipótesis económica, universo as-of/inception, señales y transform deterministas, cash/protección/orden, clocks, data/price adjustments/dividend/cost rules, calendario/fills/gaps, fallos/pausa/dependencias, benchmarks y plan de sensibilidad. Registrar cada ensayo/fallido y exposición previa al dataset.

Congelar separación design/train/selection-validation/untouched confirmation y reglas de selección antes de consultar sus resultados. Una muestra usada para elegir candidato deja de ser confirmatoria; reservar forward/OOS nuevo. Criterios de scorecard/weights/tie-break y thresholds de continuación aún propuestos para gobierno antes del holdout. No inventar período completo hasta septiembre 2026 sin dataset correspondiente ni esconder visualización previa. Mantener declaración owner: nunca se vio backtest MATR en ningún período.

Evaluar primero reglas, calidad/PIT/licencia, costes/replay, riesgo/operación, interpretabilidad pedagógica y complejidad. Solo candidatos admitidos reciben comparación cuantitativa; no favorecer al que tenga benchmark histórico atractivo pero timestamps indeterminados. Foco research siguiente: disponibilidad de historia PIT y reglas faltantes, no elegir rentabilidad de político/persona ex post.

## 4. Dependencias y siguientes entregables

R-025/R-007 datos alimentan admisión; D-011 protocolo de validación y R-009 paridad motor; broker D-021 limita ejecución reproducible; risk numérico P2 D-031 distinto del riesgo conceptual aprobado. D-008 puede avanzar especificación sin esperar D-024, pero selección final de Strategy V1 requiere evidencia/gobierno. No hay circularidad que permita implementar primero. Corrección de referencia 2026-10-07: el texto original decía D-009, que corresponde a extracción del video, no broker.

Entregables siguientes: `CandidateRuleCard` por variante, `DatasetAdmissibilityCard` por fuente histórica y scorecard pre-resultados, variantes preregistradas y escenarios de conflicto. Campos mínimos: estado/evidence/source, clocks y missing, reglas completas vs OPEN, autoridad y dependencia-failure contract, costos/free alternative, engine/order assumptions, owner decisions restantes. Las fichas son documentos del repo; no estrategias productivas ni elección final. Investigación de acceso/datos puede continuar después de decisión de aislamiento sin activar broker/API paga.

## Avance documental del paquete

[CandidateRuleCards del video](R-020_video_candidate_rule_cards_RC0.md) especifican ambigüedades y escenarios de stops/ladder/señales sin inventar entrada. [DatasetCard SEC](R-020_SEC_dataset_admissibility_RC0.md) verifica camino público de extracción y registra ausencia de timestamp first-available; no backtest/dataset/API probe ejecutado ni familia/proveedor seleccionado.

## Avance 2026-10-07 y registro de exposición

[Demanda RC1](R-020_candidate_data_workload_contract_RC1.md) enlaza candidatos/clocks/engine/órdenes/failures y waves broker/data/Smart Money; D-009 cerrado solo extracción funcional. No backtests ni resultados de MATR/variantes vistos. Al comprobar una referencia de inception de ETF, páginas públicas de emisores incluyeron retornos del fondo/benchmark: exposición incidental registrada, no usada para seleccionar/ajustar candidatos. No equivale a un backtest de estrategia ni certifica intacta ninguna muestra; el futuro preregistro debe considerar la exposición previa pertinente.

## Propuesta de evaluación wave03 — 2026-10-13

[O-B/Q055](D-011_OOS_policy_decision_RC0.md) READY_FOR_DECISION sólo arquitectura development/selection/confirmation/cohorts, reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11. Criterios mínimos/metrics/sample/costs siguen OPEN antes de resultados; no Strategy/config/holdout certificado. [Semánticas comunes RC1](R-020_shared_calculation_semantics_RC1.md) pendientes de paridad/config. E1 no resuelve PIT y Starter durable no satisface rights; admisión se verifica por dataset sin alterar safety/economía.
