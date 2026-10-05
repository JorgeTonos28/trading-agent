# Scorecard económico común — ADR-008

**Vigencia actual — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

**Fecha:** 2026-10-02. **Estado:** estructura de investigación; no precios ni presupuestos aprobados. Aplicable a brokers, market/alternative data, modelos/runtimes, conectores, quant, almacenamiento, infraestructura, observabilidad y cualquier capability externa.

## Campos mínimos por candidato y fase

| Campo | Evidencia/interpretación |
|---|---|
| `PAPER_V1_VIABLE_FREE` | `YES / NO / PARTIAL / UNKNOWN`: la ruta incluida/gratuita cumple funcionalidad, calidad, licencia, acceso, límites y continuidad requeridos para PAPER; gratuidad comercial por sí sola no prueba viabilidad. |
| `PAPER_V1_COST` | Coste incremental respecto de suscripciones existentes; fijo, variable y mensual bajo carga PAPER documentada. Desglosar coste total/asignado de suscripción, infraestructura y operación aunque el incremental sea cero. |
| `LIVE_COST` | Fijo, variable, estimado mensual y costes por escala de operación LIVE, usando fuente/cotización fechada y supuestos explícitos. `UNKNOWN` hasta evidencia. |
| `FREE_ALTERNATIVE` | Candidato incluido/público/local/free-tier y evidencia de suficiencia; si no existe alternativa razonable, justificarlo por requisitos. |
| `PAID_INCREMENTAL_VALUE` | Diferencia observable de calidad, fiabilidad, datos, cobertura, latencia, continuidad, seguridad o capacidad; distinguir claim del proveedor, hipótesis y evidencia de probe. |
| `ECONOMIC_JUSTIFICATION_REQUIRED` | `YES` para cualquier gasto incremental propuesto, contratación o coste LIVE por justificar; indicar disparador, alternativa y dueño humano. `NO` solo para adquisición/uso realmente sin gasto adicional, no exime otras revisiones. |

## Detalle que acompaña a esos seis campos

```yaml
candidate_id: null
phase: PAPER_V1_or_LIVE
layer: methodology_or_runtime_or_data_or_infrastructure
pricing_source_and_observed_on: UNKNOWN
currency_and_tax_basis: UNKNOWN
existing_subscription_entitlement: UNKNOWN
fixed_cost: UNKNOWN
variable_cost_units_and_rates: UNKNOWN
monthly_workload_assumptions: UNKNOWN
estimated_monthly_cost: UNKNOWN
scale_scenarios: UNKNOWN
integration_and_maintenance_effort: UNKNOWN
lock_in_and_exit_cost: UNKNOWN
expected_operational_benefit_and_evidence: UNKNOWN
condition_justifying_payment: UNKNOWN
spend_approval_reference: NONE
PAPER_V1_VIABLE_FREE: UNKNOWN
PAPER_V1_COST: UNKNOWN
LIVE_COST: UNKNOWN
FREE_ALTERNATIVE: UNKNOWN
PAID_INCREMENTAL_VALUE: UNKNOWN
ECONOMIC_JUSTIFICATION_REQUIRED: YES_if_spend_proposed
```

Estimar mensual = fijo + suma(unidades × tarifa) + mínimos/fees/add-ons/overages + infraestructura aplicable. Anotar costes iniciales, descuentos/temporales, restricciones free-tier y supuestos; evitar doble contar fees ya incluidos en simulación de trades. Coste humano/mantenimiento se registra por separado si no se monetiza. Para cuotas compartidas Plus, coste incremental cero no implica capacidad ilimitada ni disponibilidad garantizada.

## Economía unitaria y decisión LIVE

Elegir unidades que expliquen el servicio: coste por research run/propuesta shadow/explicación, activo-día o evento utilizable, orden reconciliada, GB retenido, hora operativa. Registrar carga base y escenarios de crecimiento sin inventar escala aprobada. Comparar beneficio **neto de costes** con incertidumbre y sensibilidad: mayor cobertura/calidad puede mejorar investigación sin demostrar alpha; fiabilidad/protección puede justificar gasto por reducción de fallos antes de disponer de evidencia de retorno.

Una recomendación paga debe identificar una condición comprobable (por ejemplo, la alternativa gratuita incumple el requisito de latencia/cobertura/recuperación bajo la carga requerida) y evidenciar la mejora. No fijar ROI mínimo ni precio máximo sin decisión posterior. Investigar está autorizado; activar facturación, contratar o gastar requiere autorización humana explícita bajo ADR-008. Skills/templates tienen coste de adquisición cero como regla independiente de sus dependencias.
