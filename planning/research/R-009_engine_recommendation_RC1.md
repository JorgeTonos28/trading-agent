# R-009 — recomendación de motor y contratos de paridad RC1

2026-10-23. D023 RESEARCHING; **recomendación condicionada, ningún motor seleccionado**. Investigación ejecutada de componentes, sin estrategias/backtests históricos o datos de mercado. No comparar cantidades de checks como score entre motores: los scopes son distintos.

## Evidencia efectivamente obtenida

| Motor/ruta | Evidencia | Límite |
|---|---|---|
| Nautilus1.231.0 | [QE2 matching nativo](probes/r009-matching-components/README.md): stop-market95→gap90 llena90; stop-limit95/94 no llena en90 y llena tras recuperación. Mismo OHLC con distinto orden high/low produjo no-fill versus fill. Cuenta CASH/posición ficticia previa; ninguna Strategy ni BacktestEngine.run | QP3/4 parcialmente contrastados en L1; no broker, calendarios, fees/PIT/corporate-action/recovery ni QP completo |
| Nautilus liquidez | QE2-02=7PASS/1FAIL; repetición03 mismo trace económico. Expectativa de consumo≤5 falló: modelo llenó6 desde L1size5 con consumo activo | Source del mismo wheel aplica continuación sintética a otro nivel para market orders. L1 no contiene profundidad completa: no es prueba de6acciones imposibles ni bug universal, sí refuta asumir cap estricto por flag. Modelo de impacto/liquidez requiere adaptación/aceptación |
| LEAN source | [QL0/QL1](probes/r009-lean-source/README.md): pin f3d841e60dfd010ee5fc293ea893e56952484108, sparse source sin Data, .NET10.0.302; Common build04 PASS; QL1 restore y Engine component build PASS con DLL/hash, NuGet público, sin CLI/Cloud/Docker/admin | QL1 retiró una referencia a Algorithm.CSharp según manifest, sin ejecutar Launcher/algoritmo. No distribución stock/runtime/paridad aceptados. Errores XML/env y timeout previos preservados |
| LEAN cash/actions | [Source fijado](https://github.com/QuantConnect/Lean/blob/f3d841e60dfd010ee5fc293ea893e56952484108/Common/Securities/SecurityPortfolioManager.cs): ApplyDividend reconoce ausencia de pay-date model y en backtest Raw/SplitAdjusted acredita cash al aplicar evento; live depende de cash sync | Native default no satisface automáticamente receivable/ex-date/pay-date. Requiere ADAPT y prueba de no doble crédito; no declarar que Raw soluciona contabilidad |
| LEAN fills | [EquityFillModel](https://www.quantconnect.com/docs/v2/writing-algorithms/reality-modeling/trade-fills/supported-models/equity-model) documenta gap/stop y restricciones de tiempo/stale | DOCS_ONLY para este probe, no equivalencia a QE2. Historia intrabar no inferida de OHLC |

QL0 auditó dependencias realmente restauradas: warning NU1903 DotNetZip1.16 y NU1904 System.Drawing.Common4.7. [DotNetZip advisory](https://github.com/advisories/GHSA-xhg6-9j5j-w4vf) exige resolver extracción de inputs no confiables; no probar exploits. [System.Drawing advisory](https://github.com/advisories/GHSA-rxg9-xrhp-64gj) limita ese CVE a macOS/Linux: **no afirmar exploit en Windows** por severidad genérica. Reachability, sustitución/actualización y licencia/SBOM antes de admitir un pin; sin vulnerabilidad «aceptada» por compilar. Nautilus/deps también necesitan revisión de target, no se presume libre de vulnerabilidades por no mostrar warnings de NuGet.

## Recomendación fundamentada y alcance

**LEAN raw source como candidato principal de investigación de backtesting; Nautilus como alternativa y conformance comparator acotado.** Motivo: demanda ETF, calendarios/actions/normalización y ecosistema de modelos equity documentados; existe ruta de compilación local gratuita de Common y componentes Engine. Contrapesos: .NET+Python/packaging, dependencias a remediar y contabilidad de dividendos a adaptar. No recomendar CLI pago para evitar esos trabajos.

Nautilus tiene ventaja de acceso Python/wheel y matching ejecutado aquí; sigue viable si se resuelven actions/receivables, liquidez y mappings con menor carga total. No se exige mantener dos motores completos en producción. No engine propio general: reutilizar motor y adaptar contratos específicos; un oráculo Decimal no sustituye el simulador.

Esta recomendación no concede aceptación al commit de master ni decide live Execution. D023 conserva recomendación técnica revisable, no DECIDED: falta validar distribución/packaging, pin/deps remediados, QP integrado/coste y gobernar el impacto de stack cuando el paquete esté suficiente. No pedir ahora permiso de instalación, datos o gasto. Modelos de ambos deben satisfacer la misma contabilidad, clocks y broker mapping; escoger por rendimiento histórico está excluido. La compilación reduce incertidumbre de acceso/toolchain, no prueba ventaja económica o fidelidad frente a Nautilus.

## Contrato de paridad: trace mínimo y oracle

Trace protegido por escenario: engine/build/source+fixture+model hashes; evento/available/receipt/process clocks; security/order/attempt/parent/group IDs; raw price/qty/tick/currency; before/after filled/remainder; desired/confirmed protection; costes/cash disponible/receivable/encumbrances; motivo de rechazo/incertidumbre y fila causal. UUID/tiempo de captura separados de determinismo económico. Cada qty/coste entra exactamente una vez por agregación (RiskRC3).

Oráculos preregistrados por caso, independientes del P&L del engine. QP1 disponibilidad/next opportunity; QP2 acciones y payable; QP3 gap/trigger/fill; QP4 ambigüedad intrabar; QP5 parciales/grupos/recovery; QP6 cash/fees/rounding; QP7 revisiones/IDs; QP8 calendario/DST; QP9 replay/export; QP10 carga/repeatability. PASS componente no cierra el conjunto; discrepancia de modelo exige explicar/adaptar o NO_ADMISSION, nunca modificar fixture/expectativa para ocultarla.

Importador/cash book/fee/slippage/order/broker model deben declararse explícitamente. Engine no otorga autoridad financiera ni resuelve B3; no backfill de protección o ejecución al stop por defecto. Trace maestro de Champion no se exporta sin filtrar al Shadow; usar contratos existentes de blinding/snapshot por rol, sin reabrir arquitectura agéntica.

## Build-vs-Reuse y economía

LEAN engine=REUSE_AS_IS + WRAP/ADAPT; Common source disponible/build parcial YES; target UNKNOWN; technically compatible CONDITIONAL; selected NO. Nautilus=REUSE_AS_IS + WRAP/ADAPT, componente nativo observado YES, resto CONDITIONAL. CLI/Cloud=REFERENCE_ONLY reserva paga; engine propio general BUILD no justificado.

PAPER_V1_VIABLE_FREE=CONDITIONAL engine/data/ops; PAPER_V1_COST engines0 licencias fuente, dependencias/build/integración/almacenamiento/QA y mensual real UNKNOWN. LIVE_COST producto/escala/operación UNKNOWN. FREE_ALTERNATIVE otro motor OSS. PAID_INCREMENTAL_VALUE soporte/setup/continuidad si brecha y beneficio medidos. ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. Lock-in APIs/normalización/traces/catalog y coste de salida por medir. Un investigador/seisETF no define carga real; registrar fijo/variable/mensual/escala, todas cinco escalas2k/5k/10k/25k/50k y20celdas hipotéticas, sin seleccionar celda favorable. No gasto ni target acceptance.
