# R-007/R-008 — Broker y market data, evidencia primaria wave 01

2026-10-07 · P1 D-021/D-022 **RESEARCHING**, ninguna selección. Research documental en Team/INFOTEP; API/data/órdenes/credenciales no conectadas. Account-specific y semántica se validarán en target autorizado, sin bloquear comparación ahora. No asesoramiento de inversión ni gate LIVE aprobado.

## Hechos observados y gaps

| Candidato | Evidencia oficial | Lo que NO establece / siguiente gate |
|---|---|---|
| Alpaca Paper Only | Cuenta simulada gratis/global y API; claves y endpoint distintos de live. Datos realtime IEX. Fills paper usan NBBO y no verifican cantidad contra profundidad disponible; simulación omite dividendos, impacto, cola y slippage por latencia | Paper no valida liquidez real ni coste/P&L económico completo. Elegibilidad LIVE RD, órdenes protectoras/TIF/carreras y streams/recovery no demostrados para owner. [Paper](https://docs.alpaca.markets/us/docs/paper-trading) |
| Alpaca data Trading API individual | Basic gratis, IEX realtime, 30 símbolos streaming, 200 historical calls/min, historia anunciada desde 2016. Algo Trader Plus anunciado US$99/mes con mayor cobertura/límites | No inferir cobertura as-of, activos delistados/revisiones/licencia de almacenamiento/LLM. No cubre por anuncio el período MATR 2005–2015. [Oferta](https://docs.alpaca.markets/us/docs/about-market-data-api) |
| Alpaca históricos/feed | SIP histórico sin suscripción exige end al menos 15 minutos anterior; latest SIP requiere entitlement. Feed default depende suscripción | Pin explícito feed/cobertura/clock en DatasetCard; no confundir IEX realtime con consolidated realtime. Datos admitidos para backtest pueden no ser los disponibles para señales live. [FAQ](https://docs.alpaca.markets/us/docs/market-data-faq) |
| IBKR | República Dominicana aparece en lista oficial de países disponibles. Paper ligado a cuenta y replica permissions/subscriptions; stops complejos y fills simulados con limitaciones | Lista no aprueba KYC del propietario, entidades/productos ni coste. Trial, cuenta aprobada/fondeada y API son rutas distintas por investigar. [Países](https://www.interactivebrokers.com/en/accounts/open-account-country-list.php), [paper](https://www.ibkrguides.com/advisorportal/aboutpapertradingaccount.htm), [TWS limitations](https://www.interactivebrokers.com/docs/tws-api/doc/notes-limitations/tws-api-limitations) |
| Tradier | Sandbox separado, tokens para cuenta brokerage; datos equities/options delayed 15 minutos. API sin cargo para account holders, pero no delayed **market-data stream** paper en FAQ | Elegibilidad RD/cuenta requerida/coste total UNKNOWN. No concluir ausencia de **account-events stream**: documentación distingue live/sandbox y eventos de trades; probar continuidad/replay por separado. [Endpoints](https://docs.tradier.com/docs/endpoints), [data](https://docs.tradier.com/docs/market-data), [FAQ](https://docs.tradier.com/docs/faq), [streaming](https://docs.tradier.com/docs/streaming-data) |

Esta wave no elimina tastytrade/TradeStation ni proveedores independientes Databento/Massive/Tiingo/Alpha Vantage/Nasdaq. Fichas equivalentes y comparación de protection/order lifecycle/historia/licencias siguen pendientes antes de selección. Fuentes versionless actuales preferidas frente a rutas versionadas antiguas; capturadas esta fecha, no contrato perpetuo.

## Disponibilidad y reutilización

EXISTS=YES documentado para las tres familias. AVAILABLE_TO_US=PAPER Alpacadocumented global signup **CONDITIONAL a cuenta/entitlement**, IBKR/Tradier UNKNOWN account-specific; TECHNICALLY_COMPATIBLE=CONDITIONAL, ECONOMICALLY_REASONABLE=UNKNOWN hasta demanda/semántica/licencia; SELECTED=NO. Broker APIs/SDKs son candidatos **WRAP**, datos **WRAP / REFERENCE_ONLY** hasta admisión, nunca tool directo de agente ni desarrollo de broker propio.

Un broker PAPER gratis puede servir a integración y no a validación de alpha. El backtest debe modelar costes/dividendos/gaps/liquidez independientemente y reconciliar diferencias, sin ajustar el modelo para replicar fills demasiado favorables. Esto es una inferencia de diseño desde las limitaciones documentadas, no un fallo observado del broker.

## Economía por fase

| Candidato/scope | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Alpaca paper/Basic | CONDITIONAL a requisitos | API/paper/feed Basic US$0 publicado; infraestructura/operación UNKNOWN | Broker fees/datos/capital/funding UNKNOWN | Otras filas + datos públicos según clocks | Full consolidated quote/coverage si demanda lo requiere | YES antes de gasto |
| Alpaca Algo Trader Plus data | NO en preferencia gratuita; reserva paga | US$99/mes anunciado; no activado | US$99/mes plan actual, más costes externos UNKNOWN | Basic delayed históricos/IEX con gaps | Realtime consolidated, símbolos/límites mayores; utilidad por estrategia no probada | YES expresa antes de considerar excepción PAPER |
| IBKR | UNKNOWN ruta/entitlements | UNKNOWN; software/simulator ≠ coste total cero | Fijo/variable/FX/subscriptions/fees UNKNOWN | Alpaca/otras por verificar | Cobertura/órdenes/instrumentos/servicio, por medir | YES si gasto |
| Tradier | CONDITIONAL cuenta/semántica | API US$0 para holders; otros costes UNKNOWN | Fees/subscriptions/funding UNKNOWN | Alpaca/IBKR | Paridad/orden/types/data por medir | YES si gasto |

Escenario económico observado: un usuario/API individual, V1 equities/ETF, sin leverage/derivados. US$99 es coste fijo mensual de **Alpaca**, ajeno a ChatGPT Plus. Variables/add-ons/impuestos/escala y tiempo de mantenimiento no cotizados; lock-in mappings/feeds y salida via exports deben puntuarse. No justificar pago solo por mayor cobertura anunciada: requiere gap material medido, alternativa free insuficiente y beneficio operativo estimado; LIVE conserva paid candidates. No cuentas, financiación, gasto ni email a terceros realizados.

## Próximo trabajo independiente

Antes de D-021: fichas completas candidatos restantes, RD por entidad/ruta y order/protection matrix. Antes de D-022: historia 2005/warm-up, corporate actions/as-of, clocks/revisiones/delistings, licence/storage/AI use y validador secundario. Describir probes read-only y de órdenes sintéticas target, no ejecutarlos desde AI/research host. Dependencias Strategy y datos se comparan conjuntamente, sin seleccionar por resultado histórico ni free tier solamente.
