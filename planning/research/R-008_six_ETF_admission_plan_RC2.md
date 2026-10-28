# Datos — admisión por rol y QA de seis ETF RC2

2026-10-28. Cuatro DataCards+seis subcards **NOT_ADMITTED**. Protocolo y fixtures verificables, sin cuenta, API de mercado, dataset licenciado o backtest. [Evidencia comercial](R-008_vendor_evidence_and_plan_scope_RC1.md) no sustituye controles.

## Productos y roles independientes

| Rol | Fuente candidata prioritaria | Requisito y límite |
|---|---|---|
| Señales/indicadores EOD | EODHD EOD19.99 condicionado; alternativas previas conservadas | Seis ETF raw OHLC + transform split-only causal. No exigir técnico API premium para calcular indicadores localmente |
| Acciones/dividendos | EODHD eventos JSON; complemento primario/issuer si hace falta | Unidades históricas, ex/record/payment/declaration y revisiones; pay-date ausente no cash temprano |
| Gaps/stops/ratchet/parciales/paridad | Granularidad y quotes/trades por admitir; EOD+Intraday29.99 sólo candidato | Daily OHLC no ordena eventos intrabar; trade bars no demuestran NBBO/queue o fill. No asumir que un plan cubre todo |
| PAPER operacional | Alpaca IEX/otros permisos efectivos y stream broker | Distinguir señalfeed y entorno de matching; límites del simulador explícitos. No extrapolar a LIVE |
| Form4/PIT externo | SEC/EDGAR directo, wrappers públicos ya investigados | Accession/acceptance/publicación/recepción/correcciones; código P/plan/universo y muestra propios. No comprar All-in-One sólo por insider endpoint |
| Referencia monetaria | Fuentes oficiales y modelos de cash ya registrados | Yield≠total return; cash comparador≠interés de cuenta, vintage/basis/roll/costes propios |
| Costes | Tarifas aplicables y modelos de ejecución/operación | Fees/spread/slippage/impacto/data/infra; UNKNOWN no cero, cinco escalas obligatorias |

## Errores de unidades a impedir

[EOD schema](https://eodhd.com/financial-apis/api-for-historical-data-and-volumes) documenta OHLC as-traded, adjusted_close con dividendos/splits y volumen ajustado por splits. No usar close raw×volume ajustado como liquidez histórica raw. Invertir una cadena completa de reexpresión podría reconstruir unidades, pero exige verificar dirección/factores/coverage y corroboración; sin eso, volumen no admitido para liquidity cap. Esa normalización no reconstruye vintages/revisiones faltantes.

[Dividends JSON](https://eodhd.com/financial-apis/api-splits-dividends) distingue value reexpresado y unadjustedValue histórico; CSV pierde campos de fecha. Para qty histórica usar importe de esas unidades, no valor ajustado actual. `fmt=json` en minúscula y schema/version se fijan en el contrato; ejemplos de documentación no prueban completitud de nuestros ETF.

## Matriz aplicable individualmente a SPY/QQQ/IWM/EFA/TLT/GLD

| Gate | Evidencia necesaria antes de admisión | Defecto/estado |
|---|---|---|
| DA01 derechos | Plan/producto/usuario/usos/local/retención/backups + versión de términos y confirmación aplicable | Scope incompleto=RIGHTS_PENDING. No admisión por ventas |
| DA02 transmisión | Policy por campo, uso, destino y linaje | DENY por defecto para raw/licenciado/derivado/reempaquetado/reconstruible sin permiso |
| DA03 identidad/inception | Security ID, listing/inception y cambios de ticker, moneda/mercado/unidades | No alias actual para toda historia ni filas preinception |
| DA04 cobertura | Calendario admitido, sessions esperadas/entregadas y huecos por instrumento/ventana | No missing=holiday ni forward-fill oculto. GLD no requiere historia imposible: feature NOT_READY según warmupW0 |
| DA05 schema/grain | Clave security/session/source/version, tipos, timezone, duplicados y revisions | Error de grain/parse/row implica quarantine, no cast silencioso |
| DA06 precios/unidades | OHLC positivo/orden, raw/split-only/full-adjusted y volumen; tick/moneda | No double dividend ni rawprice×latest-adjustedvolume |
| DA07 eventos | Split ratio/dirección, dividend entitlement/importe/moneda/ex/record/pay/declaration, cash-in-lieu | Missing pay-date no cash libre; actions incompletas no ajuste inventado |
| DA08 temporalidad | Event/known/receipt/revision y alcance de reconstrucción histórica | declarationDate o delay arbitrario no repara falta de vintage; exact replay y reconstrucción diferenciados |
| DA09 corroboración | Comparación autorizada con fuente independiente de precios/eventos y casos alrededor de splits/dividendos/gaps | Umbrales por unidad/fuente antes de datos; outlier no se borra por afectar resultados |
| DA10 motor | Import y trace equivalente, calendario/EndTime/adjustments/fees/cash/payment | Parse PASS no acepta contabilidad/paridad |
| DA11 oportunidad | Horizontes, caducidad y disponibilidad compatibles con señales/fills | Si lag altera señal/economía, simularlo y registrar admisibilidad |
| DA12 reproducibilidad | Manifest/hash local, versión, rights policy, raw/revisions preservados según licencia, restore | Hash no acredita veracidad; no raw en Git o cloud sin derechos |

Por cada subcard registrar counts esperados/observados y denominadores, huecos pre/postinception, primera sesión elegible PRICE/MATR, defectos y materialidad. No umbral porcentual genérico permite omitir una fila que cambie señal/stop. Incidencia material sin resolver bloquea el rol afectado; admisión parcial requiere scope explícito y no sustituye evidencia de otra ventana.

Muestras futuras empiezan fuera de selección/confirmación y con querymanifiesto. No abrir holdout para comprobar acceso. QA local con datos licenciados no imprime raws al modelo: runner no agéntico entrega sólo reporte permitido por derechos; si tampoco puede exportar métricas derivadas, revisión local del propietario. Los permisos no se infieren de anonimizar o resumir.

## Qué se ejecutó ahora

DA-S2:21 casos sintéticos de schema, grain, missingness, units, pay-date, PIT, correcciones y egress. DA-S3:6 de normalización de volumen/precio. [Fixtures](probes/r008-admission-fixtures/README.md) y capturas preservadas. Son aritmética/guardas de contrato, no27 controles pasados por EODHD, seis ETF completos o un protocolo PIT admitido. No se llama a endpoints demo o privados.

Timezone/parsing/DST sigue NOT_TESTED: aparece como requisito DA05 pero no fue ejercido por DA-S2. Se preserva explícitamente como caso pendiente, sin repetir fixtures para inflar cobertura.
