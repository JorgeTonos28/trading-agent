# R-008 — referencia monetaria y coste de oportunidad — RC0

2026-10-14 · research, no dataset seleccionado/admitido ni cuenta Treasury/broker creada. ADR017 exige cash; esta comparación no autoriza negociar bills ni añadir activos a V1. No histórico completo/retorno de estrategias observado; páginas oficiales muestran tasas recientes, registradas en exposure ledger.

## Rutas oficiales y distinciones

[H15](https://www.federalreserve.gov/releases/h15/) publica tasas de lunes a viernes16:15, salvo festivos/cierre; no timestamp de barra ni recibo propio histórico. [DTB3](https://fred.stlouisfed.org/series/DTB3) es yield descuento; [DGS3MO](https://fred.stlouisfed.org/series/DGS3MO) inversión/constant maturity interpolada, ambas daily y susceptibles de revisión. Ninguna serie es por sí sola un índice de retorno total de cartera de bills ni interés pagado por broker. FRED etiqueta estas series public-domain con cita; vistas actuales no prueban vintages/availability histórico.

[Treasury pricing](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/) da precio de bill a descuento `P=F*(1-d*D/360)`; `F/P-1` es retorno hasta maturity para ese instrumento, no dailyyield/252. Para daily mark/roll requieren maturity restante, curvas/precios y reinversión/costs; no usar hoy yield futuro para marcar pasado. [FRED realtime](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html) distingue lo conocido en distintas fechas; API/vintage completa/credenciales/licencia por verificar, no APIkey pedida aquí.

[SOFR](https://www.newyorkfed.org/markets/reference-rates/sofr) es coste repo garantizado overnight, publicación aproximadamente08ET; no rendimiento de depósito disponible al usuario. Es alternativa de sensibilidad si scope/historia/vintage adecuados, no alias automático cash2005+.

## Recomendación de especificación

Separar **cash real del ledger** (interés/fees/capital elegible/settlement broker, cero si realmente no paga) de **hurdle de oportunidad monetaria**. No acreditar T-billyield al cash real sin inversión/interés efectivo. Preservar cash, dividends y fees una sola vez. Estándar ideal: cartera bill/índice total-return con derechos y timestamps adecuados; alternativa económica de investigación: proxy de carry DGS3MO último publicado/elegible, regla de day-count/compounding/lag fijada, etiquetada MODELLED_CARRY_NOT_EXECUTABLE_RETURN. Comparar sensibilidad a DTB3 convertido correctamente y cash0, sin usar0 como única oportunidad si rates positivos.

Proxy no puede aprobar confirmación como total-return exacto sin gate explícito. No empalmar índices/ETF nuevos como si existieran2005 ni tomar interpolación de maturity como instrumento negociable. El universoETF común no define cash: S, B-EW6 y B-LAMBDA-REAL usan carryreal equivalente y ledger/costs propios para comparación económica/atribución; B-CASH es hurdle de oportunidad separado, nunca crédito automático al cashreal. Un espejo adicional con opportunityproxy se etiqueta distinto, sin reemplazar al REAL silenciosamente.

## Economía, reutilización y aceptación

EXISTS=YES officialseries/formulas; AVAILABLE_TO_US=docsYES/datahistory-vintagesCONDITIONAL; TECHNICALLY_COMPATIBLE=CONDITIONAL; ECONOMICALLY_REASONABLE=UNKNOWN calidad/operación; SELECTED=NO. API/series WRAP/ADAPT candidato, formulas REFERENCE_ONLY; no proveedor cash construido desde cero.

PAPER_V1_VIABLE_FREE=CONDITIONAL fuentes públicas, PAPER_V1_COST=acceso docs0+normalización/storage/vintages UNKNOWN, LIVE_COST=operación/escala/índice con rights UNKNOWN, FREE_ALTERNATIVE=Fed/FRED/Treasury primarios con gate, PAID_INCREMENTAL_VALUE=total-return/rolls/historia/PIT/continuidad si gap demostrado, ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gastar. Escenario un investigadorUSD/cartera6ETF, volumen no fijado; lock-in curva/base/vintage y salida sourceevents/rawversioned, no compra autorizada.

Gate: cobertura períodosMATR, vintage/availability/release/receipt/dst/holidays, denominaciones%, discount vsinvestment basis, returnconversion/roll/costs, missingreglas, license/citation y secondaryvalidation. Todos NOT_TESTED históricos, benchmark no seleccionado. La página H15 anunció cambio futuro DDP→FRED; registrar dependencia de API/URL, no hardcodear superficie que se retirará. Fechas/impacto operativo se revisarán al seleccionar fuente.
