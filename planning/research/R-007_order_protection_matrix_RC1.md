# R-007 — brokers, órdenes y protección PAPER — RC1

2026-10-13 · D-021 RESEARCHING, broker no elegido · [Wave01](R-007_008_provider_evidence_wave01_2026-10-07.md) conservada. Solo fuentes oficiales; no cuenta/auth/API orden, gasto o broker endpoints en AI. No confundir sandbox de integración con simulación económica ni elegibilidad general con KYC aprobado.

| Broker | Evidencia documental nueva / route | Implicación para candidatos y pruebas todavía pendientes |
|---|---|---|
| Alpaca | [Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca): brackets esperan entrada llena, OCO puede tener ambas salidas filled antes de cancelación en mercado rápido; trailing standalone RTH, no trailing-leg bracket/OCO; notional replace no soportado; texto OTO replacement ambiguo | No asumir protección inmediata de parcial ni OCO atómico. Ratchet del video ≠ trailing nativo. Matriz por qty/TIF/session/partial/cancel-replace/reconcile; no cancelar protección automáticamente |
| IBKR | Wave01 paper/country/API routes y sim stop limitations; no nuevas credenciales | Rango de órdenes/promoción LIVE candidato; compatibilidad de combinación y estado real por API route sigue UNKNOWN. RD lista no resuelve cuenta/entitlements/funding/costes |
| Tradier | [Trading](https://docs.tradier.com/docs/trading): market/limit/stop/stop_limit y OTO/OCO/OTOCO; entry OTO no market; equity whole shares. Sandbox/cuenta/delayed y streams diferenciados wave01 | Una entry market + protection pretendida puede no mapear a OTO. Trailing nativo no demostrado aquí; no inventarlo. Parciales/leg quantities/order history/recovery/DR/rights pendientes |
| tastytrade | [Sandbox](https://developer.tastytrade.com/docs/sandbox/): market fills artificiales US$1, resets diarios y sin market data. [Complex orders](https://developer.tastytrade.com/reference/orders/postAccountsAccountNumberComplexOrders/) documenta OTO/OCO/OTOCO y contingent legs | Útil para integración/lifecycle, inadecuado como evidencia P&L económico o recovery multiday sin fixture propio. País RD aparece en snippet oficial, apertura página da CSS Error: elegibilidad actual **UNKNOWN**, no gate KYC pasado |
| TradeStation | [SIM](https://api.tradestation.com/docs/fundamentals/sim-vs-live/) cambia base-url, instant simulated fills. [HTTP streams](https://api.tradestation.com/docs/fundamentals/http-streaming/) documenta cuentas/posiciones/precios y posibles terminaciones | API shape similar no prueba fill/latency/live parity. Spec dinámica no legible en herramienta, protection matrix/DR/account/access/cost UNKNOWN. No asumir bracket de desktop equivale Web API |

RD tasty source a completar: [Supported countries](https://support.tastytrade.com/support/s/solutions/articles/43000435355). Error de render no rechaza broker, ni snippet prueba sección eligible vs ineligible. API/MCP directo a LLM anunciado por algunos proveedores queda fuera del contrato aprobado; investigar adapters determinísticos WRAP.

## Gates B1–B5 concretos para target autorizado

- **B1 acceso/equities:** residencia/entidad/paper route, cuenta/permissions/API/market data/terms; distinguir no-funding trial y cuenta LIVE. Manifest fija PAPER endpoint/account, rechazo de LIVE; secretos en Financial Core.
- **B2 lifecycle:** submit/ack/reject, timeout anterior/posterior a aceptación, lookup/client_id, parcial y duplicate; query/reconciliation antes de retry. IDs cliente no prueban exactly-once.
- **B3 protección:** qty parcial, entry llena, precio/raw/tick-size/session/TIF, replace mientras fill/cancel, doble OCO fill, stop gap/no-fill, expiración/corporate action. Controles positivos y negativos, conservación de protección G1+G2.
- **B4 streams/recovery:** drop/reconnect/poll/replay/ordering, duplicate/corrected fills, broker≠DB, cierre/overnight/asset halt. Posición y reservas verificadas antes de reanudar; humano tras incidente material.
- **B5 economía/modelo:** price/feed/fill diferencias, dividendos/fees/slippage/cash y saldo, simulation reset. Simulación favorable no aprueba retorno; engine tiene modelo independiente.

Protocolo preparado, **B1–B5 NOT_TESTED**, ninguna llamada financiera aquí. Tecnología adapter reusable antes de BUILD; nunca salida SDK broker directo desde agentes. Broker puede variar entre PAPER/LIVE, decisión owner D-021 y LIVE separado.

## Economía y disponibilidad por fase

Para tastytrade/TradeStation: EXISTS=YES documentación; AVAILABLE_TO_US=UNKNOWN account-specific; TECHNICALLY_COMPATIBLE=CONDITIONAL; ECONOMICALLY_REASONABLE=UNKNOWN; SELECTED=NO. PAPER_V1_VIABLE_FREE=UNKNOWN; PAPER_V1_COST=UNKNOWN fijos/variables/mensual/ruta; LIVE_COST=UNKNOWN fees/data/funding/scale; FREE_ALTERNATIVE=Alpaca/IBKR/Tradier por validar; PAID_INCREMENTAL_VALUE=coverage/controls/continuity si probado; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. Disposición APIs WRAP candidatas, sandbox REFERENCE_ONLY para resultados económicos. Escenario un usuario equities/ETF, volumen no fijado; exit cost mappings/auth/feed por medir. No broker desaparece de comparación por costes PAPER.

## Resultado y dependencia

Se recomienda reducir primero las variantes a reglas/protección/data factibles, comparar Alpaca e IBKR como primeras rutas documentales integrables **sin seleccionar ninguno**, y mantener restantes ante gaps. Elegibilidad/cuenta real/costes y negativa de orden en target pueden cambiar shortlist. D-008 puede diseñar reglas ahora; freeze requerirá contrato broker concreto, no etiqueta «supports stops».

## Evidencia temporal wave03 — 2026-10-14

[Timing/data/broker](R-007_008_timing_evidence_2026-10-14.md) verifica delayedhistoricalSIP/Basic y rutaIBKR auth/presets/cancelstates. Source/feed/deadline/coverage/rights y Riskfreshness separados, B1–5target aún NOT_TESTED. No broker/proveedor seleccionado ni cuenta/config/autenticación/data call. Rutas gratuitas no resuelven2005+ ni audit rights automáticamente.
