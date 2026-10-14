# SC0 — escala y costes ex ante, sin capital seleccionado

2026-10-14. ADR019 exige escenarios previos. Grilla candidata de investigación, no presupuesto/contratación/capital o escenario operacional aceptado. Ningún precio/resultado de estrategia consultado para escogerla.

## Matriz fija de sensibilidad

K hipotéticoUSD={2000,5000,10000,25000,50000}; fijo mensual incrementalF={0,20,60,100}. Ejecutar/reportar todas las20combinaciones admitidas, sin escoger ex post el K que pasa. Escenario principal operacional no elegido: debe declararse por gobierno antes de resultados pertinentes. En absence de ese input, comparabilidad por escenario es condicional, calificación operacional NOT_EVALUATED.

| K USD hipotético | F0/mes | F20/mes | F60/mes | F100/mes |
|---|---|---|---|---|
| 2000 | 0% | 12% | 36% | 60% |
| 5000 | 0% | 4.8% | 14.4% | 24% |
| 10000 | 0% | 2.4% | 7.2% | 12% |
| 25000 | 0% | 0.96% | 2.88% | 4.8% |
| 50000 | 0% | 0.48% | 1.44% | 2.4% |

Tabla12F/K es **carga anual aproximada sobre equity inicial**, no CAGR exacto, forecast de rentabilidad o aprobación de proveedor. Reconstruir equity económico con accrual previo para NI/cash; no simplemente restar a CAGR después. Si equity económico no positivo, identificar insolvencia económica/modelo inaplicable, no borrar meses ni convertir a retorno válido. No mover dinero del broker desde una tabla de atribución.

## Clasificación y no doble conteo

- **Asumido/sunk:** hardware comprado y suscripciones ya pagadas para otros usos. Registrar costo total y asignación económica de sensibilidad; incremental puede0 sólo si evidencia confirma que no aumenta factura/consumo. Team actual no prueba coste/entitlement de Plus objetivo.
- **Incremental fijo:** servicio adicional imprescindible, observabilidad/data/infra o cuota de modelo permitida. F0 es escenario, no afirmación de que todo el sistema cuesta0. No activar plan/API paga.
- **Variable:** broker/fees/spread/slippage por transacción en net_trading; model/data calls, electricidad/compute/almacenamiento o volumen incremental en net_after_ops según origen. Fuente y escalaUNKNOWN quedan así.
- **One-off:** instalación/migración/ingeniería/recovery inicial separadas del gasto mensual, amortización y horizonte de sensitivity declarados antes; no omitir coste de mantenimiento por ser OSS.
- **Tiempo del propietario:** reportar workload y sensibilidad de valoración, sin asumir sueldo/opportunity-cost0 o precio elegido tras resultados.

No cargar overhead AI/core a EW6-BH/SPY/cash pasivo para mejorar comparación. Cada referencia conserva sus propios costes. λ usa NAV financiero; ES financiero net_trading. NI/cash after_incremental_ops separa función económica de Risk y no cambia capital/riesgo financiero aprobado.

Cost matrix de ejecución/spread debe provenir de feeds/broker/cantidad y establecer escenarios conservadores/costdelay antes de resultados, no de esta grillaF. Rotación/notional equivale a costes variables, no fees fijos repetidos dos veces. Paid source candidates tienen scorecards documentales, no costes de operación completos.

Reportar passing/insufficient/no-evaluation por **todas** las celdas pertinentes y frontera de viabilidad; no «strategyqualified» global por una celda. Selección real K/costs necesita datos y gobierno aparte. PAPERzero/lowincremental primero, LIVEeconomicvalue posteriormente sin descartar pago permanentemente.
