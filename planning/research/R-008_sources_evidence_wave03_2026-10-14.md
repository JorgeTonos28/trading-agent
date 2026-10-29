# R-008 — alternativas de histórico, derechos y presupuesto wave03

2026-10-14. Fuentes primarias públicas; ninguna cuenta/APIkey, datos de precios o trial abierto, gasto o proveedor seleccionado. Mantener ventanas MATR2005–2018/2019–2022 y reserva UNKNOWN. Comparación de documentación, no QA real ni dictamen legal.

## Alternativas adicionales

| Ruta | Evidencia primaria | Disposición acotada y gaps |
|---|---|---|
| EODHD free/paid | [Pricing](https://eodhd.com/pricing): free20calls/día, historia1año; EOD19.99/mes o199/año, profundidad30+años anunciada según API. [Terms](https://eodhd.com/financial-apis/terms-conditions): permite almacenamiento/análisis personal privado, prohíbe compartir acceso/distribuir; declara datos indicativos y limitación de fuentes | Free no satisface historia propuesta. Paid WRAP/REFERENCE_ONLY condicional: feed/quality/rights/retention/as-of requieren evidencia; no admitir como única verdad de fills o protección por30años anunciados. Retención post-cancelación no certificada; ningún gasto |
| Twelve Data free | [Pricing](https://twelvedata.com/pricing): $0,8credits/minute,800/día; docs de [historia](https://support.twelvedata.com/en/articles/5656039-how-to-get-historical-prices) anuncian daily desde primera negociación para muchos símbolos y outputsize5000 | CONDITIONAL candidato research, no cobertura real de seisETF. Credits no igual calls para todos endpoints. [Ajustes](https://support.twelvedata.com/en/articles/5179064-are-the-prices-adjusted) describen daily split-adjusted e intradayraw; dividend/raw/adjustversion/availability y endpoints por plan pendientes |
| Twelve rights | [Terms](https://twelvedata.com/terms) §§12.5/16: eliminación al terminar, límites por suscripción y terceros, excepción compliance/audit | No ruta de retención durable tras salida aceptada; excepción compliance no se presume aplicable a research privado ni licencia universal de derived outputs. CONDITIONAL_NOT_ADMITTED, pago no elimina gate de derechos |
| Norgate US | [Packages](https://norgatedata.com/stockmarketpackages.php): Silver270/año10años, Gold360/año20años, Platinum630/año1990+delisted/index history, Diamond787.50/año1950. [FAQ](https://norgatedata.com/data-package-faq.php): ventana rolling se reinicia por año; ajustes/eventos tienen semántica propia. [Content](https://norgatedata.com/data-content-tables.php) distingue metadata actual/dividendos incorporados | WRAP/ADAPT/REFERENCE_ONLY paid reserve, no PAPER free por defecto. Gold no garantiza2005/warm-up desde2026. Platinum profundidad útil anunciada, no prueba PIT/rights/muestras. Fundamentals actuales no historia PIT; dividend ya incorporado no se suma de nuevo |
| Norgate integration | [Subscription](https://norgatedata.com/subscribe/) enumera Python Windows/export ASCII limitado a precios; [trial](https://norgatedata.com/freetrial.php)2años | Target compatibility/retención/redistribución y raw actions UNKNOWN; trial no sustituye ventana. URL supuesta terms devolvió error, no inferir permiso por silencio |
| Nasdaq Data Link | [SEP](https://data.nasdaq.com/databases/SEP) y [API](https://data.nasdaq.com/tools/api) dieron superficie sin contenido útil a herramienta | Inventario conservado, precio/entitlement/coverage/rights UNKNOWN; no rechazo, scraping/bypass ni selección |

Fuentes gratuitas restantes no están agotadas. Alpaca2016+ puede cubrir la selección común, no research2005+; Yahoo/Stooq siguen UNKNOWN derechos/calidad, no descartados por código o acceso bloqueado. No juntar proveedores/años sin versionar ajustes/lineage/cross-validation ni alterar ventanas para encajar en free tier.

## Economía por fase, escenario seisETF/un investigador

| Ruta | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| EODHD | NO para historia completa free; paid no autorizado | Free0, paid19.99mensual/199anual+operación UNKNOWN | Producto/feed/uso compatible por verificar | Broker/públicas/OSS candidatas, no suficientes certificadas | Depth/continuidad si calidad/derechos superan gaps | YES antes de gasto |
| Twelve | CONDITIONAL a historia/rights/quality | Free0+ops; Grow79/Pro229/Ultra999mensuales en pricing, sin activar | Tier/add-ons/escala/retención por cotizar | Otras rutas candidatas | Cobertura/limits si derechos durables y calidad demostrados | YES |
| Norgate | NO full history por ruta paid | Anuales270/360/630/787.50; equivalentes22.50/30/52.50/65.625mensual amortizado, no oferta mensual; hardware/ops UNKNOWN | Idem más usage/rights/escala UNKNOWN | Otros históricos candidatos | Delisted/constituents/QA anunciados, no medidos | YES |
| Nasdaq | UNKNOWN | UNKNOWN | UNKNOWN | Primarias/broker/otrosvendors | UNKNOWN hasta ficha | YES |

Fijos son acceso publicado, variables/fees/export/storage/calidad/tiempo UNKNOWN; sin presupuesto/capital/volumen final. Lock-in de símbolos, ajuste/catálogo/terminación y coste de salida deben valorarse. Pagar sólo si gap free material + beneficio/coste/rights demostrados y owner aprueba. Software/APIs existentes antes de BUILD proveedor; ningún MCP/Skill premium activado ni nueva investigación agéntica general.

**Conclusión:** ni profundidad ni gratuidad equivalen a admisión. Sigue faltando una ruta reproducible y durable con raw/events/as-of/calendario. Esta wave reduce incertidumbres concretas, no declara imposible PAPER gratis ni propone contratar todavía.
