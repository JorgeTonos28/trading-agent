# Revisión crítica independiente — evaluación, retención y normalizador

2026-10-13 · reviewer `independent_hardening_review`, lectura independiente conforme roadmap §3.16. No probes/instalaciones/ediciones por reviewer, no auditoría humana ni aprobación owner. Scope: [O-B/Q-055](D-011_OOS_policy_decision_RC0.md), [retención](R-008_data_retention_gate_RC1.md), [E1](R-021_edgartools_findings_2026-10-13.md) y source/result/hashes. No nueva ronda agéntica general.

| Finding | Prioridad | Reparación persistida |
|---|---|---|
| Cabecera holdout no consultado demasiado categórica frente a exposición incidental histórica | P1 | No **nuevos** resultados/dataset confirmatorio en wave; PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M-11. Si no se acredita integridad, owner reevalúa antes de abrir resultados. O-B no certifica holdout intacto |
| Power no tiene excepción contractual de retención en términos publicados | P2 | Explicitado en gate de retención; paid CONDITIONAL no equivale a retención permanente |
| Rama DerivativeTable/NonDerivativeTable también suministrada por caller | P2 | Explicitado en dossier E1: no detección automática ni end-to-end |

Reviewer no identificó P0 nuevo y consideró O-B apta para presentar **su scope conceptual tras P1**. Verificó SHA de fuente; aceptó límites7/7table-only, factoryerror y connect sin fase. Plan Architect aplicó las tres precisiones a archivos; QA documental/hash adicional, no rerun ni declaración de un segundo review. Q-055 READY_FOR_DECISION; D-011 global RESEARCHING y Strategy V1 OPEN. Esta revisión no cubre exhaustivamente la propuesta ATR/calculaciones RC1 ni acredita broker/dataset/risk/engine/target acceptance.
