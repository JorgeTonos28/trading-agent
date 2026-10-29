# Revisión independiente — protocolo y preferencia económica

2026-10-14 · reviewer independent_hardening_review, lectura conforme roadmap §3.16. Sin ejecutar probes/instalar/editar/precios/cuentas/admin. [RC2](R-020_evaluation_protocol_RC2.md), [HorizonCard](R-020_decision_horizon_latency_RC0.md), [scorecard](R-020_comparable_candidate_scorecard_RC2.md), [Q056](D-011_economic_endpoint_decision_RC0.md) y source/result sintéticos.

| Finding | Prioridad | Reparación |
|---|---|---|
| Strategy aprobada/target como requisito del comparador produce circularidad | P1 | F0 evaluación vs F1 confirmación vs DoR/target separados; no exigir ganador antes de comparación |
| Beneficio positivo contra0 no define éxito económico | P1 | Estado frente a endpoint/efecto mínimo, SUPPORT_CONDITIONAL y scope SELECTION/CONFIRMATION explícitos |
| DSR/PBO/Holm sin gate de supuestos puede maquillar resultados | P1 | MethodApplicabilityCard: frecuencia/momentos/dependencia/familia/inputs/NO_ESTIMABLE; Holm no arregla selección adaptativa ni p inválidos |
| Expiry/holding no controla frescura | P1 | Freshness por input/quote/estado obligatoria, stale bloquea antes de expiry |
| Manifest de dependencias ausente en snapshot intermedio del review | P2 | Añadido dependencies01 con15pins/SHA wheels y launcher exacto, QA del Architect sin rerun; licencias transitivas NOT_COMPLETE |
| E2 nombra probe y opción económica | P2 | Probe conserva E2; opciones Q056 se presentan A/B/C |

Reviewer confirmó las cuatro reparaciones P1; no identifica P0/P1 que impida presentar Q056 conceptual. Considera gobierno material genuino: aceptar retorno menor dentro de margen a cambio de menos riesgo es preferencia owner. Propuesta B mantiene §23/resultado positivo OOS/risk/promotion, sin modificación automática del baseline. Scorecard compara diseño/demanda, no ganador ni desempeño.

SHA fuente coincide y19/19 sólo evidencia fixtures/primitives. No prueba intervalos/power/suficiencia/freshness completa/H1–10/alpha/dataset/broker/target. Review inicial de registry/metadata quedó limitado por snapshot intermedio; éstos se validan adicionalmente por QA declarada, no atribuir al reviewer una auditoría de hashes/licencias transitivas o aprobación. F0 NOT_FROZEN y D011 RESEARCHING. Auditoría holdout sigue UNKNOWN, no resultados abiertos.

## Verificación final posterior al snapshot intermedio

Reviewer leyó registry, EvidenceCard, dependencies01, launcher/fuente/captura y naming final A/B/C: confirma cinco hipótesis/trials0/attempts0/history_complete=false/F0incompleto, hashes de las tres especificaciones referenciadas y fuente/launcher,15pins/hash registrados sin credenciales y licencias transitivas incompletas. No P0/P1 restante que impida presentar Q056 conceptual. No verificó cada wheel ni licencias transitivas, ni modelo/dataset/alpha/readiness. No ejecutó ni modificó. Se conserva el límite inicial como historia y esta ampliación explícita; no tratarla como gate operacional.
