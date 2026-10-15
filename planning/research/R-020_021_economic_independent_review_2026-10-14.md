# Revisión independiente — contrato económico y Form4, wave05

2026-10-14 · reviewer `independent_hardening_review`, separado del Plan Architect. Lectura crítica de documentos/source/capturas/registry; no ejecución, instalación, edición, consulta de datasets o administración. No aprobación owner ni verificación target.

## Hallazgos y reparaciones

| Prioridad | Hallazgo | Reparación del Plan Architect |
|---|---|---|
| P1 | Cash del espejo podía confundirse con oportunidad monetaria | RC3/R008 separan REAL equivalente al ledger S de hurdle B-CASH y espejo de oportunidad opcional |
| P1 | Fórmula podía descontar costes dos veces | Basket GROSS excluye fricciones/cash; espejo tiene ledger y costes totales propios |
| P1 | Rebalance mensual parecía baseline buy-and-hold; λEOD no iguala exposición intraday | B-EW6-BH preservado, monthly propuesta distinta; clocks/intervalos por cambios/fills, diagnóstico limitado si no admisible |
| P1 | ES no estimable/replicas inválidas y estados insuficientes podían producir FAIL o ratio0 | Convención/cola/ties/replicas en MethodApplicability previa; NO_ESTIMABLE como diagnóstico, mapeo RC2 y cash-only condicional |
| P1 | Ablation de ratchet exigía mismas posiciones realizadas aunque stops cambien salidas | Mismas reglas/políticas, ledgers divergentes; entradas/cantidades exógenas MODULE_ONLY, no cartera factible |
| P1 | Espejos/gates no específicos por opción Q057 | K1 SPY+SPY-λREAL; K2 EW6BH+EW6BH-λREAL; K3 NI y reducción contra ambos |
| P2 | E3 no ensaya constant/nonfinite conf_int previsto | NOT_TESTED documentado; ratioNaN no sustituto; fuente/captura sin cambios ni rerun |
| P2 | FULL_MARKUP F2 sólo verifica cuatro substrings | Preservación completa/byte idéntico NOT_TESTED; nombre de check histórico intacto |

El Architect además documentó ERROR inicial de QA por EOL histórico CRLF frente a blobs Git LF. Registry conserva raw SHA y añade EOL/hash Git portable; no sobrescribe declaraciones antiguas para pasar. Nuevas declaraciones se verifican contra el mismo commit antes de reportar completado.

## Conclusión del reviewer después de reparaciones

**No queda un P0/P1 identificado que impida presentar Q-057/K2.** La referencia es decisión material concreta, fundada en universo común/baseline, no en rendimiento. No se repite Q056. Lectura y coincidencia de hashes/source/capturas no prueban alpha, inferencia conjunta, PIT/rights/dataset, target o independencia del holdout.

E3 **19/19** y F2 **13/13** son fixtures/componentes; F2 registró un connect bloqueado, no aislamiento OS. Registry8 declaraciones/0trials, F0 incompleto, fuentes no admitidas. Revisión no exhaustiva de transitivas/licencias, de power/coverage/bootstrap ni de implementación (no existe sistema productivo).

## Estado de gobierno

Q057 **READY_FOR_DECISION** de referencia/gates PRICE–MATR; D008 OPEN, D011 RESEARCHING. Métrica primaria, márgenes/efectos/α/muestra/modelos siguen sin aprobar. Holdout INTEGRITY_UNKNOWN; implementation_locked=true y TARGET_ACCEPTANCE_DEFERRED. [Propuesta](D-011_benchmark_qualification_decision_RC0.md), [RC3](R-020_economic_qualification_contract_RC3.md).
