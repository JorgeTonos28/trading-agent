# R-008 — market data, historia y clocks — wave02

2026-10-13 · P1 D-022 RESEARCHING · documentación pública, no cuentas/tokens/requests a datasets/precios ni gasto. [Wave01 broker feeds](R-007_008_provider_evidence_wave01_2026-10-07.md) y periodo MATR2005+ preservados. Claims de cobertura son del proveedor, no tests de calidad/availability.

| Ruta | Evidencia actual de fuente primaria | Gate todavía sin probar |
|---|---|---|
| Tiingo EOD | [Docs](https://www.tiingo.com/documentation/end-of-day) raw/adjusted y splits/dividendos; anuncia datos después de sesión y correcciones durante la noche. [Pricing](https://www.tiingo.com/about/pricing) Starter US$0 y30+ años,500 símbolos/mes,50 requests/hora,1000/día,1GB/mes; Power personal US$30/mes o300/anual | Datos de cada ETF/universo2005, revisions as-of/availability/timestamps/licencia automatizada/storage/AI/quality cross-check UNKNOWN. Horas «EST» del texto no resuelven DST/actual receipt. Redownload adjusted history reescribe presente, no restaura vista histórica |
| Massive Stocks | [Pricing](https://massive.com/pricing): Basic US$0/mes,2años/EOD/5callsmin; Starter29/mes5años, Developer79/mes10años, Advanced199/mes20+años/realtime. [History](https://massive.com/knowledge-base/article/how-much-historical-stock-data-does-massive-have) anuncia captura listedUS desde2003-09-10, acceso por plan | Basic no cubre2005/warm-up ni ventana confirmatoria completa propuesta. Archive total ≠ entitlement. Corporate actions/delistings/PIT/rights/individual nonpro/coverage real por ticker y datos delistados no demostrados |
| Alpha Vantage | [Docs](https://www.alphavantage.co/documentation/) daily raw compact100puntos gratis, full histórico premium; daily-adjusted premium. [Support](https://www.alphavantage.co/support/) free25requests/día, excepción educativa/OSS requiere verificación | Free nominal no cumple SMA200/warm-up ni años de investigación por compact. Exención no concedida. Funciones/news/realtime/adjusted no asumidas gratis; precio premium aplicable UNKNOWN |
| Databento/Nasdaq Data Link/otros | Inventario preservado | Fichas/precios/licences/history/quality siguen pendientes; no descartar ni seleccionar por esta wave parcial |

No modificar ventanas/reglas ni rellenar años para encajar en free tier. Tiingo merece la **primera ficha/probe de histórico gratuito** por cobertura anunciada, no selección D-022; validar acceso/corporate actions/raw y licencia antes de muestras. Receipts actuales no acreditan PIT de correcciones históricas. El validador secundario y calendarios/corporate actions deben ser independientes cuando sea posible.

## Economía por fase y disposiciones

| Candidato | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Tiingo Starter/Power | CONDITIONAL Starter a licencia/calidad/límites | Acceso0 Starter, Power30mensual/300anual no aprobado; hardware/operación UNKNOWN | Oferta personal30mensual; commercial50mensual/499anual publicada, rights/scale aplicables UNKNOWN | Starter/broker feeds con gaps por medir | Límites/coverage/servicio si gap medido | YES antes de gasto |
| Massive Basic/paid | PARTIAL Basic historia corta | Basic0;29/79/199mensual por plan, ningún gasto aprobado | Idem solo si rights individual/entitlement aplican; business cotización/variable UNKNOWN | Tiingo/broker feeds/cobertura por verificar | Más historia/realtime/trades/quotes si requerido | YES |
| Alpha Vantage | PARTIAL free/UNKNOWN suficiencia | free limitado0, premium precio aplicable UNKNOWN | Price/licence/data/escala UNKNOWN | Tiingo/broker feeds | Profundidad/funciones si material y validado | YES |

Escenario un investigador, seisETF benchmark + universo de variantes aún no fijado. Fijo/mensual citado solo acceso plan, variables/add-ons/exchange/storage/fiscalidad/time maintenance UNKNOWN. No asumir usuariosTeam institucional cumplen individual/nonpro, ni que derecho raw autoriza envío LLM. Lock-in symbols/adjustments/feed; exit raw snapshots+versioned events y migración por medir. LIVE conserva opciones pagas con valor/fiabilidad medidos, sin compra automática.

EXISTS=YES docs, AVAILABLE_TO_US=docs YES / datasets UNKNOWN; TECHNICALLY_COMPATIBLE=CONDITIONAL; ECONOMICALLY_REASONABLE=UNKNOWN hasta workload/quality/rights; SELECTED=NO. Disposición WRAP APIs y ADAPT imports/contabilidad, REFERENCE_ONLY hasta admisión, no BUILD proveedor. Prioridad free suficiente, nunca omitir datos requeridos para evitar coste.

## Señales externas especializadas

Massive [pricing](https://massive.com/pricing) anuncia Benzinga news/analyst ratings US$99/mes por dataset y NYSE imbalances49/mes; son alternativas pagas a investigar para revisiones/flow-context, **no Smart Money ni PIT automáticamente probados**, sin gasto. Calidad/histórico/canal/rights/costo variable y utilidad incremental UNKNOWN. FREE_ALTERNATIVE=fuentes primarias/eventos públicos por investigar; PAPER_V1_VIABLE_FREE=NO ruta paga; PAPER_V1_COST/LIVE_COST=precios anunciados más operación UNKNOWN; ECONOMIC_JUSTIFICATION_REQUIRED=YES. No habilitar MCP ni pay-per-request anunciado.

## Alcance y siguientes pasos

API examples y snippets comerciales pueden contener números/precios, no se llamaron endpoints ni se consultó backtest/holdout. Exposición previa de fichas emisores ya documentada; ningún retorno usado para ajustar estos criterios. Próxima wave: rights/coverage por ticker, muestras cross-source y clocks (en entorno/autorización apropiados), normalizador filings offline, pins/paridad engine y config completa. Costes y datos se evalúan conjuntamente con hipótesis, no elegir por plan más barato.

## Adenda de vigencia — retención, 2026-10-13

[Gate de retención RC1](R-008_data_retention_gate_RC1.md) **supersede la recomendación de primer probe gratuito y la celda CONDITIONAL de Starter para el rol persistente**. Tiingo Starter PAPER_V1_VIABLE_FREE=NO, REJECT durable core/audit/backtest bajo términos observados. Power/otros pagos siguen condicionales a rights/retención/economía; no contratación autorizada. Oferta/historia anunciadas anteriores se preservan como evidencia comercial, no licencia suficiente. No concluir ausencia de alternativas gratis; Yahoo/Stooq/otros con rights/calidad UNKNOWN, broker-native y proveedores pendientes siguen comparación.
