# D-021 — broker PAPER, acceso real y límites RC4

2026-10-23. READY_FOR_DECISION de selección **de diseño PAPER**, B1–5/target no aceptados. Recomendación cambia prioridad técnica de la shortlist: **Alpaca Paper Only primero para PAPER zero/lowcost**; IBKR TWS reserva si gates fallan. LIVE completamente abierto. Ninguna cuenta/orden/login/credencial broker solicitada o usada.

## Comparación y evidencia primaria

| Candidato | Acceso PAPER y orden/protección | Límites materiales |
|---|---|---|
| Alpaca Paper Only | [Docs](https://docs.alpaca.markets/us/docs/paper-trading) permiten signup global/email y API paper gratuito; IEX realtime. REST/streaming; [órdenes](https://docs.alpaca.markets/us/docs/orders-at-alpaca) stop/bracket/OTO y límites detallados enRC3 | Globalpaper no demuestra LIVE RD. Simulador omite dividendos, impacto/cola/slippagelatencia/fees regulatorias; fill feed no equivale a IEX. Child full fill/OTOreplace y stop dependiente del fill no resueltos. No seleccionar bracket conTP artificial |
| IBKR TWS/IBGateway | [Requirements](https://www.interactivebrokers.com/docs/tws-api/doc/notes-limitations/requirements) exige cuenta Pro abierta/fondeada; [Limitations](https://www.interactivebrokers.com/docs/tws-api/doc/notes-limitations/tws-api-limitations) liga paper a cuenta aprobada/fondeada. RD figura en lista pública previa; sesiones/presets/permID/replaceRC3 | Funding es depósito/acción del owner, **no fee ni nominal PAPER 10k autorizado**. Respuesta Campus antigua menciona delayeddata para cuenta aún sin fondos, pero no invalida requirements actuales; ruta aplicable requiere confirmación. Trial no es API paper garantizada. Paper topofbook/stops simulados y remainder puede rechazarse según [guía](https://www.ibkrguides.com/clientportal/aboutpapertradingaccounts.htm) |
| Tradier | Sandbox/API oficial, OTO/OCO/OTOCO, whole equity, datos delayed 15 min y diferencias streaming documentadas | Cuenta/eligibilidadRD/ruta/costes y paridad protectora sin acreditar. No ventaja demostrada que compense mayor incertidumbre frente a paper global Alpaca; mantener reserva, no REJECTgeneral |
| Otros inventariados | tastytrade/TradeStation conservan sus referencias/gaps | No seleccionados por no existir evidencia suficiente de mejor encaje en este scope. No afirmar análisis exhaustivo del mercado o inexistencia de alternativas |

La recomendación es inferencia de **acceso/coste/complejidad para PAPER**, no superioridad de executionlive o capacidad económica. IBKR sigue alternativa fuerte si cuenta/ruta ya elegible y evidencia de órdenes lo justifica, pero no imponer funding para demostrar arquitectura gratuita.

## Cambio vigente de schemas y régimen intradía

El [changelog Trading/Broker API2026-07-06](https://docs.alpaca.markets/us/changelog/2026-07-06-pdt-db49dba) retiró campos PDT/DTBP de account/config. No exigir daytrade_count/pattern_day_trader como campos vigentes ni usar ejemplos versionados viejos para declarar bloqueo automático25k. [FINRA](https://syndication.finra.org/content/understanding-new-intraday-margin-requirements) señala vigencia2026-06-04 con transición de firmas hasta2027-10-20; [SEC34-105226](https://www.sec.gov/rule-release/34-105226) es aprobación de regla. No transferir fecha/regla de Alpaca a IBKR sin evidencia por entidad/cuenta. No se autoriza margin/leverage por esa actualización; CashRisk propio sigue vinculante.

SDK oficial/API es candidatoWRAP, con pin y fixtures de schema actual/errores/stream. Leer modelo SDK no acepta comportamiento de API. Datos, finance endpoints y credenciales quedan sólo en TrustedFinancialCore; ningún tool broker para AI.

## Binding y aceptación imprescindibles

B1: PAPER only account/host/clave/endpoint, cuenta nominal 10k y prohibiciónlive comprobadas; creación futura owner en target. B2: feeds/clock/quote/permissions/freshness y modeloCash/settlement sin usar margin buying power para ampliar posición. B3: entry partials/protección basada enfill, reemplazo/fill/race/cancel/OCO y restore con IDs. B4: costos/actividad/cash/dividendos/actions y divergencias del simulador; B5: sesiones/stream/replay/recovery/carga/security target.

**No inferir cobertura inmediata** ni aprobar ventana sin protección. La selección del broker no autoriza entrydispatch si no existe mapping de protección admisible. Si B3 exige cambiar regla de estrategia, tolerancia de riesgo o permiso de cancel protector, gobierno explícito. MantenerG1+G2, sinG3 ni reanudación material automática. Un ack de replace no equivale a protección nueva confirmada; mantenergrafo viejo/nuevo y reservas hasta reconciliar.

**Economía:** PAPER_V1_VIABLE_FREE=CONDITIONALAlpaca; PAPER_V1_COSTaccesopaper0 documentado, data/variable/infra/integ/mensualtotalUNKNOWN. IBKRfundingno es coste, fees/data/operaciónUNKNOWN; TradierUNKNOWN. LIVE_COSTUNKNOWN, FREE_ALTERNATIVEotrasrutasporadmitir, PAID_INCREMENTAL_VALUEcalidad/coverage/supportsimedido, ECONOMIC_JUSTIFICATION_REQUIREDYES para cualquier gasto. Revalidar todos modelos en2k/5k/10k/25k/50k, sin elegircapitaldespués, veinteceldas intactas.

## Paper financiero versus evidencia económica

No acreditar cash de un dividendo modelado como si fuera saldo broker verificado. Reconciliar posiciones/órdenes/cash **del brokerpaper** y reportar por separado el ledger económico/referencia con costes/actions/PIT admisibles. Este último es análisis y no fuente de buyingpower o nuevas órdenes. Si no son comparables, no declarar paridad o calificación económica desde el P&L del broker. Correcciones/busts/modelos y diferencias tienen linaje; un reset de cuenta cambia incarnation, no borra drawdown de una evaluación o se toma como funding autorizado.
