# R-007 / R-008 — timing, datos y protección: wave03

2026-10-14 · fuentes oficiales leídas, ninguna cuenta/API autenticada/dataset/orden/configuración ejecutada. D021/022 RESEARCHING. Evidencia documental no acepta target ni broker. [Horizonte](R-020_decision_horizon_latency_RC0.md) y [protocolo](R-020_evaluation_protocol_RC2.md).

## Alpaca: rutas que deben distinguirse

[FAQ Market Data](https://docs.alpaca.markets/us/docs/market-data-faq): SIP histórico sin subscription exige `end` al menos15min antiguo; latest SIP requiere subscription, live gratuito es IEX. Feed default depende del entitlement: **pin `feed` explícito**, no heredar «best». Timestamps de barras identifican intervalo, no recepción; `asof` por renombre puede no estar listo el día del cambio. Ejemplo Apple2023-09-29 leído/documentado en exposure ledger, no rendimiento nuestro.

[Planes Trading API](https://docs.alpaca.markets/us/docs/about-market-data-api): Basic gratuito,200historicalcalls/min y30símbolos websocket, history desde2016; Algo Trader Plus99USD/mes y10k/min. Trading API individual no equivale Broker API partner. Acceso a delayed historic SIP **no** cubre2005–2015 ni prueba permiso de persistencia, dataset as-of/correcciones, bar final availability o actual cuenta.

Inferencia propia: una entrada EOD posterior puede tener tiempo para consultar delayedSIP, si se verifica receipt/expiry y no se adjudica fill previo a disponibilidad. No garantiza que15min hagan definitiva la barra. DelayedSIP no se reutiliza como marca actual de Risk/protección. Broker-side stop y quote/feed validados, gap/slippage/marks/datos incidentes siguen independientes; presupuesto libre R2 no permite top-up.

[Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca): OPG/MOO/LOO restringe deadline9:28ET y ejecución auction variable; matriz muestra asteriscos y fractional OPG no. GTC expiry90d/pending_cancel merece test de protección. Ratchet discreto no se equipara a trailing standaloneRTH. Texto genérico no confirma permisos de auction/cancel-replace ni protección parcial. CandidateConfig no puede asumir fillOpen después del cutoff ni protección permanente por `gtc`.

## IBKR TWS: operación, presets y estados

[Reauth](https://www.interactivebrokers.com/docs/tws-api/doc/tws-settings/daily-weekly-reauthentication) describe ciclo semanal y login manual cuando token permanente falta. Auto-restart documentado es opción, **no configuración aprobada aquí**. Debe modelarse outage/recovery/calendario y rol operador en D025/028; no bypass2FA ni secrets en Agent Domain. No contradice jobs Codex rutinarios automáticos: es dependencia broker separada que puede impedir nuevas entradas.

[Child protection](https://www.interactivebrokers.com/docs/tws-api/doc/orders/place-order/adding-a-profit-taker-and-stop-loss) permite children explícitos o PRESET desde TWS. Preset introduce configuración externa a código; preferencia documental candidata por children explícitos/export/version para reproducibilidad, no selection ni garantía partial coverage. [Estados](https://www.interactivebrokers.com/docs/tws-api/doc/order-management/order-status/understanding-order-status-message): PendingCancel/PreCancelled pueden ejecutar; [callbacks](https://www.interactivebrokers.com/docs/tws-api/doc/orders/place-order/order-placement-considerations) exigen atender error/orderStatus/openOrder/execDetails. Cancel request no libera reservas ni confirma ausencia de fill.

[Delayed data](https://www.interactivebrokers.com/docs/tws-api/doc/md/delayed-data):15–20min delayed, callbacks de tipo feed y frozen/delayed-frozen con restricciones. Datos live visibles en TWS no necesariamente habilitan API; no confundir frozen con quote actual. Cuenta/market-data entitlement/costes/RD y ruta concreta siguen B1/selection pendientes. Página de order_submission sugerida dio Internal Error; se usaron rutas oficiales accesibles, sin conclusión de ausencia de funcionalidad.

## Economía y Build-vs-Reuse

| Ruta | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Alpaca delayed historical SIP + liveIEX | CONDITIONAL sólo research/EOD; rights/quality/history/runtime sin aceptar | Acceso Basic0, operación/storage UNKNOWN; sin crear cuenta | Misma ruta condicional0+operación; gaps de cobertura/freshness por medir | IBKR delayed/otros proveedores históricos suficientes por verificar | SIP actual/cobertura/quotas si cumplen necesidad material, no100% alpha | YES antes de gasto |
| Alpaca Algo Trader Plus | NO coste incremental cero |99USD/mes publicado, no aprobado; fixed/variable adicional UNKNOWN |99USD/mes+terms/escala/nonpro por verificar | Delayed histórico + IEX sólo si suficiente | Feed actual consolidado y límites, a demostrar con workload | YES explícito |
| IBKR TWS delayed | CONDITIONAL cuenta/API, no fuente Riskactual aceptada | Account/entitlement/fees/data/operación UNKNOWN | UNKNOWN fixed/variable/monthly/country/escala | AlpacaBasic/otras rutas por validar | Real-time/servicio sólo si requisito y economía justifican | YES |

EXISTS=YES docs; AVAILABLE_TO_US=docsYES/cuenta-datasetUNKNOWN; TECHNICALLY_COMPATIBLE=CONDITIONAL; ECONOMICALLY_REASONABLE=UNKNOWN; SELECTED=NO. APIs/SDK determinísticos WRAP candidatos, nunca broker tools directamente a agentes. Lock-in feeds/IDs/auth/childorderstate, exit via versioned source/ledger y adapters; coste de migración por medir. No reducir snapshots/audit para encajar en free ni asumir licencia de datos por SDK abierto. Alternativas proveedores/brokers wave01/02 conservadas; no broker seleccionado.

## Acceptance ampliado B1–5

Añadir deadline/early-close/DST/queue/expired entry, denyOPG real vsdocs, dailybarrevisions/feedpin/asof rename, GTC90d protection expiry, IBKR weeklyauth/gatewayrestart, cancel-after-fill y hiddenpresets. Todos **NOT_TESTED target**. Config de protección/fees/quotes/durable rights debe cerrar antes de final Strategy/broker freeze; ninguna ruta gratuita ya está aceptada como stack completo.
