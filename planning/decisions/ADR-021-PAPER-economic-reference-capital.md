# ADR-021 — referencia económica PAPER y cinco escalas obligatorias

**Fecha:** 2026-10-15. **Estado:** DECIDED por respuesta explícita del propietario: US$10,000 como referencia PAPER. Q-060/D-044, P1, complementa ADR008/019/020. Sin Strategy/método/broker/datos/riesgo/implementación seleccionados.

## Aprobación y condición adicional

Capital **nominal de referencia económica PAPER = USD10,000**, fijado antes de resultados. No depósito, cuenta financiada, contratación, presupuesto de gasto, capitalLIVE o umbrales de Risk. Capital operacional real/funding sigue sin aprobar.

El propietario exige mantener **los cinco escenarios de sensibilidad K={2000,5000,10000,25000,50000}USD y evaluar costes en todos**. US$10,000 es referencia principal, no motivo para omitir, ocultar o reemplazar las otras cuatro escalas. Conservar grilla previa de4gastos mensuales hipotéticos (0/20/60/100) y sus20celdas; además aplicar en cada escala todos los modelos de coste reales/estrés admitidos y declarados.

Costes fijos/variables/incrementales/asumidos/one-off y escala se registran explícitos, incluyendo datos, broker/fees/spread/slippage, IA/infra/storage/operación según uso. UNKNOWN nunca se vuelve cero. Celdas no calculables se reportan como NOT_EVALUATED/UNKNOWN con razón, no desaparecen. No elegir capital retrospectivamente para hacer pasar una candidata. Capitales no son muestras independientes; usar sensibilidades para seleccionar variantes exige registro/control de multiplicidad.

No se exige silenciosamente que toda escala pase el mismo gate: la calificación tiene scope/escala explícitos y referencia principal10k, todas las sensibilidades evaluadas/reportadas. Un PASS10k no constituye viabilidad universal; deterioros/costes de las otras escalas son visibles. Si se desea exigirPASSenlas5, sería otro criterio y no está aprobado por esta decisión.

## Economía y trazabilidad

La tabla12F/K es carga anual normalizada aproximada, **no** diferencia exacta deCAGR. A20USD/mes:4.8%en5k,2.4%en10k,.96%en25k; no cotización de un proveedor ni rentabilidad. NI/cash necesitan ledger económico/accrual/modelos admitidos, no restar ese porcentaje aCAGR. Benchmarks pagan sus propios costes; no asignarles overhead delTradingOS para mejorar comparación.

[SC0](../research/R-020_cost_scale_scenarios_RC0.md) conserva las20celdas previas y la nueva referencia. Los costes reales siguen UNKNOWN; definirK no los acepta ni producePASS. Configuración/broker/datasets/estadística/DoR siguen abiertos.

HoldoutINTEGRITY_UNKNOWN, implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED. Sin Plus/admin/gasto/main o autoridad financiera nueva.
