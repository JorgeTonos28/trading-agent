# DataCards — PRICE–MATR/cash/externas RC0

2026-10-14. Estructuras persistentes de admisión, no datasets admitidos. [Cards máquina](datacards/financial_dataset_cards_RC0.json) contienen obligaciones/estado; las hipótesis no reciben datos futuros porque exista este archivo. No cuenta/APIkey o precios históricos consultados.

## DC-ETF-01 — precios y acciones

SPY/QQQ/IWM/EFA/TLT/GLD, instrument IDs/as-of/inception y fuentes por verificar. DesarrolloMATR2005–2018 más warm-up; comparación2019–2022 común; reserva2023–30/09/2026 sin abrir. Claim2005history necesita warm-up precedente, no200datos desde enero2005 e inmediatoPASS. Source/date/currentticker no sustituyen mapeo histórico.

OHLCVraw, calendario/zone/session/availability/revisions; split/distribution events con ex-date/eligibilidad/pay-date y transform/versionas-of. Indicadores split-only as-of propuestos en configs, dividends en ledger una vez. MarcaRisk fresca tiene requisitos distintos de señalEOD; feedEOD no prueba granularidad de protección/gaps/fills. Archivar raw/events/rights/derived outputs permitidos, distinguir licencia del parser de datos.

Provider claim de profundidad no prueba cobertura de cadaETF, quality o snapshots históricos. Cross-check source independiente con tolerancias por unidad/fricción previamente fijadas, lista de discrepancias y cuarentena; no ajustar sólo filas que cambian ganador. All required sessions contabilizadas, missing/stale/halts explícitos; no forwardfill oculto, sustituto ex post o borrar retorno/delisted. No modificar ventanas para satisfacer free tier.

## DC-CASH-01

Fuente/maturity/modelo/basis/daycount/publication/vintage/receipt/roll/costs/rights y calendario. DGS3MO/DTB3/SOFR son rutas documentales, no retorno total realizable admitido. Current revised observations no vistas as-of. El interés real broker tiene su propia política/balance elegible y settlement, no proxy agregado. Cash0 sólo sensibilidad explícita, no único coste de oportunidad.

## DC-MIRROR-01

Depende de ETF/card y estados financieros de candidata conocidos al inicio de cada intervalo, no fecha final de holdings. Marks/fills/time/version permiten reacción factible; ownledger fees/cash/turnover, composição/beta/factores. λEOD sin granularidad puede ser diagnóstico limitado, nunca aceptación confirmatoria adicional de eficiencia.

## DC-F4-01

Conservar Form4/4Araw/header/exhibits/version/PAC/publicchannel/receipt, fila/owners/dedup/security IDs, plan/purchase UNKNOWN y alternativas de hipótesis separadas. [SEC admission](R-021_SEC_availability_admission_RC3.md): quarterly/currentindex revisado no PIT certificado. Parser offline no acredita historial, derechos o timestamps. Universo de acciones dinámico exige price/delistings/corporate actions y benchmark propio, no heredaK2.

## Gate por scope y próxima evidencia

Estados SOURCE_DOCS_ONLY/NOT_ADMITTED, con ACCESS/HISTORY/PIT/RIGHTS/QUALITY/MAPPING/EXECUTION abiertos. Dar evidencia puntual y scope cuando algo pase; no admisión global porfieldexists. Los6ETF requieren6subcards/coverage en la fuente elegida, metadata→raw/events sample de desarrollo autorizado→as-of/crosschecks→repro/parity, antes de datos de selección/confirmación. Keys/contact/terms de cuenta requieren acción legítima cuando se llegue al probe; no credenciales en Git/chats/logs.

R008 ofrece free/paid candidates sin seleccionar y sin concluir que free sea imposible; no construir proveedor desde cero. Quality/retention debe conservar audit, no reducir trazabilidad para declarar viable un free tier. Estos gates siguen abiertos mientras investigación independiente progresa en Team.
