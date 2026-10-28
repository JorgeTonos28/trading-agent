# D-023 — paquete de selección de motor de backtesting RC2

**Actualización 2026-10-28:** Q-062/A aprobado en ADR-023 como familias de diseño Alpaca Paper Only + LEAN source; la propuesta/pregunta anterior es histórica. Gates técnicos/target abiertos. Twelve/EODHD ya respondieron según resumen del propietario; ver R-008_vendor_evidence_and_plan_scope_RC1.md. No se admite ningún dataset.

2026-10-23. **READY_FOR_DECISION en familia/dirección de stack**, no pin/distribución/modelos admitidos. Propuesta agrupada [Q062](D-021_023_PAPER_stack_decision_RC0.md). No Strategy seleccionada ni histórico ejecutado. Engine financial Risk nativo no reemplaza el Risk del proyecto.

## Evidencia ejecutable comparada

| Dimensión | LEAN source | Nautilus1.231.0 |
|---|---|---|
| Acceso/coste | Apache2, clone pinf3d841e…; Common y Enginecomponent compilados, una referencia de ejemplos retirada enQL1; sin CLI/Cloud/Docker | LGPL3, wheel observado/hash, Python disponible; docs2.xRC no aplicables sin mapping a1.x |
| Fills | [QL2](probes/r009-lean-components/README.md): componente nativo9checksPASS; gap95→90, stoplimitno-fill y recuperación, rechazo de barend≤ordertime | QE2 matcher nativo7PASS/1FAIL repetible, pathsOHLC distintosejecuciones, stopgap/limit contrastados |
| Liquidez/parciales | QL2 observó defaultfillqty10 sobre volume5: ausencia de partialmodel nativo admisible, no liquidez real probada | QE2 hardcapL1 supuesto falló6vs5 por continuación sintética; no universalbug. Requiere modelo declarado |
| Actions/cash | QL2 splitquantity10→20/entry100→50; rawdividend añade cash10 inmediatamente; doble llamada añade2×; adjusted no añade. Son llamadas nativas, no flujo full engine | Corporate actions/pay-date/receivables/import y mapping de catálogo requieren más adaptación/evidencia |
| Controles de fechas | QL2 clock ybarUTC/AlwaysOpen ficticios; noUSAcalendar/DST admitidos | QE2 quotesficticias, no calendarios/as-ofdataset admitidos |
| Instalación/mantenimiento | .NET10+posiblePythoninterop; compilationgratis demostrada, packaging/Windows target no aceptado | Pythonwheel más simple como superficie, pero datos/actions/projectmapping siguen por hacer |
| Riesgo de dependencias | DotNetZip/System.Drawing warnings registrados; plataforma/reachability/remediación antes de pin admitido | Dependencias/licencias/securityaudit también pendientes; no presumir limpio por noNuGetwarn |

Los scopes no son iguales: **no sumar PASS ni usar9vs7 como ranking**. QL2 no ejecutó Algorithm/Launcher/backtest, estrategia o broker. Duplicate ApplyDividend revela ausencia de dedupe **en esa llamada**; no prueba que el engine integrado entregue duplicados. Constructorcash fixture/leverage1 no valida cash/settlementbroker. [QP1–10](R-009_backtesting_reuse_RC0.md) sigue integrado NOT_ACCEPTED.

## Recomendación

Seleccionar **LEAN source como familia principal de backtesting**, reutilizar su event engine y adaptar import/as-of/corporateactions/pay-date/fees/liquidez/traces. Nautilus reserva técnica/comparador acotado, no segundo engine productivo obligatorio. La razón es cobertura equity/actions/calendarios e integración de contabilidad ya visible y ejecutable, con más ingeniería .NET; no retorno de estrategia o counts. No construir simulador general ni contratar CLI.

Una aprobación de familia **no acepta el pin actual**. Gate de pin exige fuente/licencia/deps/SBOM, ruta de datos/import sin extracción insegura, remediación o exclusión demostrada de paths vulnerables, packaging y regresiones de componentes. Cambiar familia por incompatibilidad material se documenta/gobierna; no cambiar silenciosamente a Nautilus ni ignorar dividendos para cerrar paridad.

## Adaptaciones requeridas antes de admitir configuraciones

- Dividendos: receivable por entitlement/ex-date, cash elegible sólo al pay-date verificado; model ledger distingue eventID/revision/supersession y duplicate. No usar earlycash nativo ni crear cash disponible de dividendos que el brokerpaper no acredita.
- Splits: raw units y costes, órdenes protectoras/remainder/tick/fractions/cash-in-lieu reconciliados; native arithmetic no confirma modificación broker.
- Fills: modelo de quote/spread/gap/latencia/partial/replace y orden de eventos preregistrado. OHLC desconocido→ambigüedad/cota o granularidad admisible, no path real inventado.
- Snapshots/audit: metadata/IDs/clocks/modelos/pins y entradas exportables con policy de datos. Proveedor audit rights separado del código Apache2.
- Paridad: trace maestro de R009RC1, QP1–10 y B3 con causas; defaultengine no otorga permiso financiero, no outputsLLM a órdenes.

BuildvsReuse=REUSE_AS_IS motor + WRAP/ADAPT contratos/modelos. EXISTS/source access YES; componentexecutedYES; TARGEThostUNKNOWN; compatibleCONDITIONAL; SELECTED=NO hastaQ062. PAPER_V1_VIABLE_FREE=CONDITIONAL; sourceengine0, integración/ops/data/mensualUNKNOWN; LIVE_COSTUNKNOWN. FREE_ALTERNATIVENautilus; PAID_INCREMENTAL_VALUE soporte/setup si medido, ECONOMIC_JUSTIFICATION_REQUIREDYES. Retener cinco escalas/20celdas y coste de lock-in de APIs/catalog/traces, no asumir gratis total.
