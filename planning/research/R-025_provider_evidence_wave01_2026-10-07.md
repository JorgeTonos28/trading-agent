# R-025 — Smart Money/alternative data, evidencia wave 01

2026-10-07 · D-033/022/008 abiertos. Sin proveedor/familia seleccionados ni gasto. Public website/docs accesibles no prueban API/data entitlement o PIT.

## Candidatos y evidencia

- **Quiver:** API pública documentada con Congreso, insider/Form4, holdings/13F y otros datasets. Oferta personal Hobbyist US$30/mes mensual, Trader US$75/mes mensual; Trader anuncia insider/holdings. Ambos sin derechos comerciales. Anual equivalente US$25/62.50 por mes con pago anual US$300/750, no mensual cancelable. MCP incluido por plan no convierte API en free. [Pricing](https://api.quiverquant.com/pricing/).
- **Unusual Whales:** anuncia API para flow/options, off-lit/NBBO, Congreso, insider, institutional holdings y ETF/flows, REST y streaming. Son categorías/ejemplos anunciados, no auditoría de latencia, historia o calidad. Precio aplicable/backfill/licencia UNKNOWN en esta wave; tokens pagos, no creados ni servicios activados. [Developers](https://unusualwhales.com/developers).
- **Capitol Trades:** continúa candidato congresual de referencia, no Smart Money completo. Aperturas actuales de about-us/disclaimer dieron error de herramienta; fuentes anteriores preservadas, disponibilidad API/terms/history/timestamps no confirmada. No asumir permiso de scraping ni rechazar plataforma por error de acceso.
- **SEC/EDGAR:** fuente primaria gratuita pública para filings; no normaliza por sí sola señales/lista de trades. SEC no ofrece timestamp first-available sec.gov y no garantiza lag acceptance→publication. Canal de recepción propio y disponibilidad histórica deben distinguirse. [FAQ](https://www.sec.gov/about/webmaster-frequently-asked-questions), [DatasetCard](R-020_SEC_dataset_admissibility_RC0.md).

Congreso, Form4, 13F/hedge-fund holdings, unusual options, blocks/off-exchange, revisions, flows y otras familias siguen **separadas**. La wave prioriza clock/integración, no demostrar alpha. 13F holdings ≠ compra conocida en fecha de fin de trimestre; prints/options ≠ dirección inversora conocida. Normalización/reglas pendientes de familia específica.

## Probe S1 sin auth: schema público Quiver

[Protocolo](probes/r025-public-schema/README.md), [fuente](probes/r025-public-schema/schema_probe.py), [captura](probes/r025-public-schema/result-01.json): GET único HTTPS, HTTP200, 238296 bytes, JSON OpenAPI3.0.3/versionv1. Content-Type text/html aunque payload parsea JSON: no asumir headers exactos. Sin datos financieros descargados, tokens/auth/account/MCP/Skill install.

Form4 schema declara Date/fileDate y uploaded opcional; Congreso ReportDate/TransactionDate opcionales. Es existencia de campos, no garantía de first-seen inmutable, revisions as-of ni timestamp que cliente pudo consultar. El schema describe fileDate como filing/publicación; **declaración del proveedor** no resuelve la ausencia de timestamp público SEC ni latencia/canal de entrega al cliente. InstitutionalHolding no se encontró bajo ese nombre de schema; UNKNOWN de mapping, no ausencia de producto 13F. [Schema público](https://api.quiverquant.com/docs/schema.json).

R-021 debe exigir muestras primario-vendor pareadas, clocks de cada canal, document_id/revision/enmiendas, precisión/timezone, historial de correcciones/backfill, limites/rights y no acceso a información futura. Un campo date-time no prueba precisión intradía; required tampoco prueba calidad real de valores. Proveedor premium con PIT demostrado puede aportar valor; no prometer que uploaded equivale a available_at o que restaura lo que el usuario veía históricamente.

## Scorecard y disposiciones provisionales

EXISTS Quiver/UW/SEC YES; Capitol portal conocido, integración UNKNOWN. AVAILABLE_TO_US solo docs/public assets; datasets API UNKNOWN/no contratado. TECHNICALLY_COMPATIBLE=CONDITIONAL; ECONOMICALLY_REASONABLE=UNKNOWN/por demanda; SELECTED=NO.

| Ruta | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED | Disposición actual |
|---|---|---|---|---|---|---|---|
| Quiver API | NO API gratuita demostrada | US$30/75 mensual personal anunciado; no gasto aprobado | Mismo precio solo si licencia/escala aplican; comercial cotización/plan, variables UNKNOWN | SEC/filings oficiales por familia, Congress official por investigar | Normalización/history/coverage/PIT si demostrado | YES, excepción PAPER y rights antes de gasto | REFERENCE_ONLY ahora, WRAP futuro candidato |
| UW API | NO free API demostrado | UNKNOWN; pago no aprobado | Fijo/variable/backfill/scale UNKNOWN | Filings oficiales para parte; free flow equivalente UNKNOWN | Flow/quote context/latencia/history si validado | YES | REFERENCE_ONLY / WRAP condicional |
| Capitol Trades | UNKNOWN uso/integración | UNKNOWN | UNKNOWN | Fuentes oficiales Congreso | Limpieza/entidades/history, por medir | YES si gasto | REFERENCE_ONLY |
| SEC directo | CONDITIONAL público; PIT/source route por verificar | Acceso US$0 + normalización/hardware/operación UNKNOWN | Source US$0 + operación/scale UNKNOWN | Misma fuente; vendors son alternativas con gaps/cost | Mejor canal/history/normalización/continuidad solo con evidencia | YES si complemento pago | WRAP / ADAPT candidato; no BUILD parser general sin reuse |

Estimación mensual = precios publicados **solo para un usuario no comercial y datasets de ese plan**; no permiso de uso bajo Team institucional/LLM/cloud/redistribución. Escala/request rate/add-ons/almacenamiento y lock-in/exit UNKNOWN. Beneficio esperado es reducir esfuerzo/error o cubrir datos útiles, sin retorno cuantificado. Justificar pago requeriría gap material vs fuente free, clocks/quality/rights verificables y owner aprobación. API/MCP de proveedor se investiga como interfaz de datos; no ampliar el universo de frameworks/Skills AI fuera OpenAI/Anthropic.

## Siguiente wave

Completar mapping13F/schema y derechos/timestamps, fuentes primarias Congress y proveedores especializados revisions/flows/blocks; evaluar reutilización de normalizadores SEC públicos/licencias antes de construir. No escoger ganador por amplitud comercial ni pedir cuenta paga ahora. R-021/020 admite solo fuentes compatibles con hipótesis/cadencia real; alternativas pueden permanecer research/pedagogía sin señal operativa.
