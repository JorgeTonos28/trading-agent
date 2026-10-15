# D035/D031 — fórmulas, targets y reservas RC2

2026-10-15. **Especificación candidata**, no Risk Engine ni números operativos aprobados. ADR006 controles independientes/mínimo, ADR015 R2, G1+G2 intactos. D035 RESEARCHING; D031 límites absolutos separados de G-R1.

## Magnitudes y dominios

Todas las cantidades/marks/raw/currency/tick/event-clock/version son verificables y coherentes. Filled q>0, mark m fresco y protección efectiva confirmada de qty/stop s con 0<s<m. Si falta/caduca/cancela/cruza sin fill verificado => UNCERTAIN; `max(0,m−s)` **no** sanea un stop cruzado. Protección parcial cubre sólo su cantidad; resto visible y no certeza de riesgo0. Dividend receivable no es cash gastable.

- R2 filled: `q*(m−s) + costes_futuros_exclusivos_de_salida`. P&L entrada→mark/realizado y fees ya pagados se registran aparte, no se restan dos veces de R2. R1/atribución desde entrada continúa aunque R2 baje.
- Pending/new: `u*(p_auth−s_cond)+costes_futuros_exclusivos_entry_exit`, sólo si s_cond/p_auth/regla/units válidos y futuro mapping admisible. Es protección **condicional**, no orden confirmada. No usar mark favorable del subyacente para rebajar p_auth ya autorizado.
- Exposición: posiciones a mark conservador + compras pendientes a p_auth, qty separadas de reservas; cash/margen elegibles por ledger/settlement. Never reinterpret exposure as R2.
- Escenario conjunto gap/slippage: pérdida de NAV actual a NAV_scenario, con cash/fills/fees/qty y precio efectivo conservador. Si incluye stop-to-gap, no sumar otra vez pérdida mark-to-stop completa a esa pérdida integral. El exceso respecto del stop puede desglosarse, sin convertirlo en una cota garantizada.
- Liquidez: cuota/participación/spread/ADV y frescura del dato con unidades/ventana; fórmula y parámetros a fijar por fuente/estrategia, no hardcode hipotético. Escenarios correlacionados de varios ETF no son seis riesgos independientes sumables por diversificación supuesta.

## Target de Strategy versus capacidad Risk

Strategy propone target determinístico según su regla; Risk restringe bajo cada control aplicable. Conceptualmente elegir la mayor cantidad **≤target** en el conjunto factible de cash/exposición/R2/gaps/liquidez/reservas, sujeto a lotes y monotonicidad/solver probado. No presupone dividir todos los budgets por un mismo stopdistance, ni que restricciones no lineales sean reducibles a `min` de escalares sin prueba. Si conjunto vacío=>REJECT; input material incierto=>UNCERTAIN, no reducir a0 como «aprobado». Risk no crea señales, top-ups o compras por capacidad libre.

Por ello una propuesta equal-notional de research y un límite financiero de exposición son parámetros distintos. Si una candidata pide target mayor que límites, registrar REDUCED y tamaño realizado; jamás subir límite para igualar su backtest. La comparación de reglas de cartera requiere ledgers factibles, no mismos fills impuestos.

## Claim exclusivo y transacción

Cada unidad está en exactamente uno de filled/pending/live-claim/cancel-confirmed según semántica de ledger. No sumar `pending6 + reserva6` para las mismas6 unidades. Si claim propio c_old ya está reservado y se revalida **autorización no despachada**, evaluar delta c_new−c_old manteniendo reserva vieja hasta commit; no liberar antes ni restar c_old dos veces. Capacidad contra otras claims/filled se calcula de un mismo snapshot/version durables; compare-and-commit/epoch/expiry/fencing en D026.

Órdenes enviadas vivas no son claims libres reutilizables: no resend bajo nuevo ID o liberar por timeout. Broker fill/cancel/bust/revision y corrección de saldo requieren reconciliación/version; ack no es fill, cancel request no es cancel confirmed. El grafo de protección también restringe G2 en [RC2 broker](R-007_protection_dependency_contract_RC2.md). Reintento idempotente no significa transacción distribuida exactly-once.

## Aceptación aún necesaria

Extender [escenarios R2](R-027_R2_scenarios_RC1.md): ganancias/perdedoras/top-up permitido o rechazado, parcial/remainder, gap/cross/rebote, split/dividendo, costes y reservas concurrentes. Arithmetic/properties sintéticas no aceptan inputs/solver/transacciones/broker. Presupuestos/umbrales, p_auth buffer/expiry/quote freshness, colas de shock/slippage, intervalo no protegido y prioridades numéricas siguen explícitamente OPEN, antes del scope que los requiera. Ningún porcentaje de borrador ni G-R1 los aprueba. Parámetros necesarios para configurar/admitir la estrategia son P1 antes de F0/implementación, aunque calibración operacional integrada sea P2.

Build-vs-Reuse: Decimal/schema/ledger/SDK/engine antes de BUILD; Risk del engine reutilizado no se adopta como única autoridad del proyecto sin contrato/paridad. No implementación, cuenta/credencial, gasto o aceptación target.
