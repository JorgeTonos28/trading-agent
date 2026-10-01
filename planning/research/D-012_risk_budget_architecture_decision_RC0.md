# D-012 — Paquete de decisión: arquitectura del presupuesto de riesgo PAPER V1

**Fecha:** 2026-10-01. **Estado:** paquete histórico de alternativas; **opción B aprobada** el 2026-10-01 en [ADR-006](../decisions/ADR-006-composite-risk-architecture.md), sin umbrales. **No implementa Trading OS.** Baseline: [hoja §11 y ejemplo MATR §18.7–18.8](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [riesgo RC1](../03_risk_policy_RC1.md), [ADR-002 G1+G2](../decisions/ADR-002-paper-v1-incident-autonomy.md), [orden ADR-003](../decisions/ADR-003-order-identity-and-recovery.md).

## 1. Decisión exacta

¿Adoptamos para PAPER V1 un **control compuesto determinístico** que limite cada nueva entrada por exposición/notional/cash, pérdida estimada al stop o protección de la estrategia, pérdida bajo escenarios de gap/slippage, y liquidez/frescura, usando el límite más restrictivo y contando posiciones, órdenes pendientes y reservas simultáneas? Esto aprueba la arquitectura de reglas; los porcentajes, escenarios y umbrales concretos quedan para D-031 y para la Strategy V1 aprobada.

El cálculo de sizing `risk_budget / stop_distance` de §18 pertenece a **MATR_V1 como candidato** y no fija el sizing de cualquier Strategy V1. §11.3 ofrece parámetros PAPER iniciales de simulación (25%, 0.50%, 2%, pérdidas/drawdown), sin demostrar que limiten una pérdida real en gap. La selección de estrategia sigue D-008 `OPEN`.

## 2. Evidencia y ejemplo de falla del control único

[FINRA explica que un stop activado puede ejecutar a precio muy diferente del stop, y que un stop-limit puede quedar sin ejecutar](https://www.finra.org/investors/insights/stop-orders-factors-consider-during-volatile-markets). [FINRA también señala que ningún tipo de orden elimina totalmente el riesgo de mercado](https://www.finra.org/investors/investing/investment-products/stocks/order-types). **Inferencia de diseño:** la distancia al stop estima riesgo en un escenario normal; no es cota de pérdida ni sustituye stress y límites de exposición.

Ejemplo puramente ilustrativo: equity $100,000; compra a $100; stop trigger $95; presupuesto de riesgo teórico $500 permite 100 acciones ($10,000 notional). Si el siguiente precio ejecutable fuera $80, la pérdida antes de costes sería $2,000. La cifra no predice un gap ni recomienda un tamaño; muestra que `qty × (entry − stop)` y pérdida bajo gap miden cosas distintas.

## 3. Alternativas

| Opción | Regla principal | Ventaja | Debilidad |
|---|---|---|---|
| A — stop + caps del borrador | `qty ≤ budget/stop_distance`, más notional/cash/gross | Simple e interpretable; útil como una capa | Stop no garantiza fill, especialmente en gap; no prueba riesgo de cartera agregado |
| **B — controles independientes compuestos (recomendado)** | Aplicar el mínimo de caps por notional/cash/gross, stop-risk estimado, escenario de gap/slippage, liquidez y presupuesto agregado, con reserva concurrente | Trata stop como estimación y añade controles explícitos de cola/ejecución; auditable | Requiere diseñar/preregistrar escenarios y puede limitar mucho ciertas estrategias |
| C — VaR/CVaR como autoridad principal | Tamaño por distribución estimada de pérdidas | Resume dependencia estadística si datos/modelo son buenos | Sensible a ventana y régimen; peor trazabilidad para V1 y no sustituye gap/operational risk |

Ninguna opción permite que LLM, Portfolio Manager shadow o broker decidan elevar límites. Opción B puede apoyarse en estadísticas como diagnóstico posterior, sin hacer de VaR/CVaR la autoridad principal de PAPER V1.

## 4. Contrato de cálculo propuesto bajo B

Para una **entrada** long-only se evalúan, en orden: estado `NORMAL`/Champion autorizado; cuenta/órdenes/posiciones reconciliadas; instrumento/mercado/datos PIT aptos; protección requerida conforme a §11; luego límites independientes. `approved_qty` es el mínimo no negativo de:

```text
desired_qty
qty_from_available_cash_and_buying_power
qty_from_position_notional_cap
qty_from_gross_and_aggregate_exposure_caps
qty_from_strategy_allocation_cap
qty_from_estimated_loss_to_stop_or_protection_budget
qty_from_each_approved_gap_slippage_scenario_budget
qty_from_liquidity_spread_participation_constraints
```

Los valores, referencia de equity, elección de escenarios, criterio de liquidez y tratamiento de correlación son parámetros **versionados y pendientes**. Una restricción no evaluable por dato ausente/obsoleto bloquea nueva entrada; no se omite del mínimo. Se usa posición reconciliada + cantidades que podrían llenarse de órdenes vivas + reservas de autorizaciones pendientes, con actualización atómica por cuenta/estrategia. El Risk Engine reduce o rechaza `TradeIntent`; Execution nunca aumenta la cantidad aprobada. `RiskDecision` se vincula al estado/versiones y expira como fija ADR-003.

Para el riesgo estimado al stop se conserva una métrica separada, p. ej. `qty × max(0, entry_reference − planned_exit_trigger)` para long; se etiqueta **estimación condicionada**, no máximo. Para escenarios se calcula pérdida hipotética por posiciones/órdenes que podrían llenarse, precio de shock y costes/slippage versionados; un escenario no es pronóstico ni garantía. La estrategia aprobada define su política de salida y protección conforme al baseline; no se impone ATR de MATR a otros candidatos.

Un hard daily loss/drawdown, una posición incierta o falta de protección activan **solo** la frontera de incidentes ADR-002: G1 y, donde proceda, G2. La aprobación de B **no** autoriza G3, venta automática general ni reanudación sin humano tras pausa material.

## 5. Qué queda pendiente después de aprobar B

| Pendiente | Gate | Evidencia |
|---|---|---|
| Valores de 25%/0.50%/2% y soft/hard o alternativas | D-031 P2; aprobación humana | Stress sobre Strategy V1 y paper, sensibilidad a gap/volatilidad y capital real previsto |
| Scenarios de shock/gap, slippage, liquidez, correlación | D-035 semántica + D-031 calibración | Datos históricos PIT, régimen adverso y criterios preregistrados; no usar holdout contaminado |
| Stop/orden protectora concreta y semántica broker | D-021 P1, D-030 P2 | API oficial, probes paper, paridad/backtest; stop ≠ pérdida garantizada |
| Referencia de equity/mark/cash y simultaneidad | D-035/D-026 | Reconciliación, reservas atómicas, fills parciales, cancelaciones y replay |
| Estrategia y salida autorizada | D-008 P0 | Reglas falsables y aprobación humana; no asumir MATR_V1 |

**Resultado:** el propietario eligió B y la regla de fallar cerrado ante un control necesario no evaluable. No aprobó los parámetros de ingeniería de §11.3 como límites operativos definitivos. Cualquier cambio posterior de arquitectura de riesgo requiere nuevo registro y aprobación humana.

## 6. Build vs. Reuse y verificación

[Open Policy Agent](https://www.openpolicyagent.org/docs/policy-language) puede evaluar políticas declarativas y [registrar decisiones](https://www.openpolicyagent.org/docs/management-decision-logs); queda `REFERENCE_ONLY`/candidato para una parte de reglas, no seleccionado. Broker-side stops/brackets son capacidad posible de APIs candidatas, sujetas a D-021/D-030; no reemplazan el gateway ni escenarios. Frameworks quant y bibliotecas de validación se comparan en R-006/009; no se decide `BUILD` del motor de reglas hasta scorecard y probe. Cualquier implementación deberá superar casos de gap, precio stale, concurrencia, parcial, cancelación G2, broker outage y discrepancia de cuenta sin que se cree orden fuera de presupuesto.
