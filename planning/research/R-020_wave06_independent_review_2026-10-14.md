# Revisión independiente — wave06 y Q058

2026-10-14. Reviewer `independent_hardening_review`, lectura separada del Plan Architect conforme roadmap§3.16. No ejecución/instalación/edición, datos históricos o pruebas target. ADR018 aprobado, no se reabre K2.

## Hallazgos y reparaciones

| Prioridad | Hallazgo | Reparación |
|---|---|---|
| P1 | Coste operativo podía asignarse también al benchmark pasivo, ocultando oportunidad; streams de gates ambiguos | NI/cash de S net_after_incremental_ops frente a benchmark owncosts; ES financiero net_trading igual a espejo; ambos reportados. F/uso/K/accrual previo, UNKNOWN => no calificación económica operacional |
| P2 | Equal initial budgets incluyendo fees podían parecer pesos netos exactos iguales | Targets1/6, realizados/residual por fees/rounding registrados; no llamar realización exact equal-weight sin evidencia |

Advertencias incorporadas: contraste ES(S)-(1-ρ)ES(M) no ES(S-M); eliminar ratio no resuelve riesgo de referencia no positivo/cola escasa; dividend reinvest no equalize weights; λ/beta/factores no equivalentes; SEC/currentindex/acceptance no receipt; datos privados no auditados M11.

## Conclusión final de lectura

**No se identifica P0/P1 restante que impida presentar Q058 exclusivamente como decisión numérica de utilidad y cola.** M1 está explicada para revisión humana; no óptima ni demostrable de forma garantizada. δ/ε después de coste operativo, 20% sobre ES financiero net_trading, pesos targets/realizados y coste económico separados.

E4 SHA coincide con captura14/14 componentes. MC160/499 y comportamiento Inf están acotados; no cobertura CAGR/ES/DD, potencia real, jointcoverage o block20 validados. No se auditaron fuentes/datasets/rights ni transitivas exhaustivas. Las fichas de proveedores son documentales, no paridad o selection.

## Gobierno y pendientes

Q058 **READY_FOR_DECISION**: recomendar1ppNI/1ppcash/20%ES/cola95, antes de resultados. Aprobarlos no aprueba métodos/suficiencia, guardrails pendientes, datos/estrategia/capital ni F0. Q056/Q057 DECIDED, D008 OPEN/D011 RESEARCHING. [Propuesta](D-011_economic_margins_proposal_RC0.md), [RC4](R-020_statistical_method_contract_RC4.md), [book](R-020_K2_benchmark_book_RC0.md).

INSUFFICIENT_EVIDENCE no autoriza ampliar margen; NO_STRATEGY_QUALIFIED preservado. Holdout INTEGRITY_UNKNOWN, implementation_locked=true y TARGET_ACCEPTANCE_DEFERRED.
