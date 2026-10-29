# R-008 — rutas de retención permanente y datos utilizables RC0

2026-10-23. D022 RESEARCHING; ningún dataset admitido. Complementa wave06 con **dos alternativas concretas** al modelo de suscripción con borrado obligatorio. No compras, consultas enviadas, cuentas privadas, muestras de pago ni precios históricos de candidatos recibidos.

## Hechos nuevos, disposición y huecos

| Ruta | Evidencia primaria | Conclusión en scope |
|---|---|---|
| **Kibot guest EOD** | [Acceso](https://www.kibot.com/api/api-access.html) documenta guest anónimo sin registro para daily US stocks/ETF, raw opcional; [free samples](https://www.kibot.com/free-historical-intraday-data.html) excluye ajustes del guest | **WRAP candidato / acceso histórico NO_DEMONSTRADO aquí**. KD1 loginPASS; seis consultas no CSV. Diagnóstico de una consulta: HTTP200 con body401, ningún bar. No inferir cobertura o causa de fallo; detener retries. No precio/raw recibido ni guardado |
| Kibot derechos | [Licencia](https://www.kibot.com/license.html): uso interno, dos equipos, archivo con notices; datos entregados conservables incluso tras terminar suscripción, restricciones de transferencia/redistribución persisten | Supera documentalmente la objeción de borrado por expiración, **no admisión legal global**. Raw a IA externa/non-display/derivados por producto no acreditados. No subir raw a Git, no confundir guest con permiso comercial irrestricto |
| **FirstRate Data** | [Licencia completa](https://firstratedata.com/about/license) declara licencia perpetua/almacenamiento y proveedores que actúan por cuenta del suscriptor; permite derivados/research con atribución, mantiene restricciones raw. [ETF bundle](https://firstratedata.com/b/17/etf-complete-historical-intraday) anuncia2000–2026, seisETF listados, GLD desde2004-11-18 y TLT2002-07-30 | **REFERENCE_ONLY reserva paga / WRAP condicionado**. Permiso de service provider no equivale automáticamente a aceptar términos de cualquier IA. Licencia muestra, producto/usuario, coste inicial aplicable y calidad por comprobar; ninguna compra/descarga |
| FirstRate acciones/calidad | [FAQ](https://firstratedata.com/about/FAQ): raw y split-only/fulladjusted, splits/dividendos en archivos separados, ex-date/amount y effective-date/ratio; no mergers/spinoffs. Historia ajustada se recalcula | No pay-date/announcement/vintage demostrado; totaladjusted no es serie as-of. Requiere datos raw+eventos, cash/pay-date complementario y filtrado RTH. Historia anunciada no valida todas las filas o inception |

La fuente [dataset card del proveedor](https://firstratedata.com/ai/datasets/us-stocks-intraday) declara limitaciones de revisiones, extended session y raw sólo1min/daily. Es card de **stocks**, no prueba independiente de los seisETF: transferir únicamente preguntas de QA, no calidad/cobertura acreditada. Proveedor de históricos no sustituye feed operacional de quotes.

## KD1: prueba práctica, no rechazo global

[Protocolo/capturas](probes/r008-kibot-access/README.md): request2004-11-18–24, seisETF, dailyraw; sin señales/returns/backtest. Resultado01=1PASS de login y6ERROR de parsing. [Diagnóstico](probes/r008-kibot-access/diagnostic-01.json) una request del mismo scope observó body401, no CSV. No cambiar transporte/auth/host para eludirlo ni pedir credenciales owner; guest publicado no es secreto/cuenta del propietario. Se desconoce por qué login e history difieren. El status apropiado es **ACCESS_NOT_ESTABLISHED_IN_RESEARCH_ENVIRONMENT**, no FAIL de datos/REJECT; target accesoUNKNOWN. Ningún raw en ignored.local ni Git. No abrir selección/holdout para probar acceso.

## Separar cuatro admisiones

1. **Licencia local/archivo**: retención permanente es relevante, no suficiente. Comparar producto, usos, notices/backups, cancelación, origen y restricciones.
2. **Input financiero**: rawRTH, corporate actions, pay-date/receivable, calendario/IDs, coverage y revisiones; observar qué sabía cada cutoff. Metadata ex-date no demuestra availability histórica.
3. **Transmisión a IA**: **DENY por defecto** para cualquier contenido cuyo permiso no esté acreditado. Uso local y permiso a IA son campos distintos. No exigir enviar toda fuente raw al LLM para que el núcleo determinístico funcione; snapshots por rol sólo con campos permitidos. Si Shadow/Ped necesita un campo excluido, la capability queda limitada/no disponible para ese dato, nunca se inventa equivalencia desde agregados.
4. **Calificación económica/operacional**: feed de broker, histórico y corrector independiente pueden ser proveedores diferentes. IEX/NBBO/consolidated/RTH/extended tienen semánticas distintas; diferencias deben medirse, no neutralizarse cambiando reglas después de resultados.

## Economía obligatoria

[Escenarios publicados](source_cost_scenarios_wave11.json) conserva2k/5k/10k/25k/50k y referencia10k; veinteceldas previas intactas. Kibot EOD14USD/mes ([delivery](https://www.kibot.com/delivery/data-updates.html)) es reserva paga:168 por12meses, no guestgratuito ni quoteoperacional; acciones/paydates/entitlement siguen UNKNOWN. FirstRate ETF updates59.95USD/mes es opcional tras mes incluido: **719.40 por12meses de updates en régimen**, o659.45 por11meses de updates en primer año tras mes incluido, más **precio inicial UNKNOWN**. Ninguno es coste total. Impuestos/FX/integración/otros datos/host quedan UNKNOWN; no anualizar un mes de compra como si se hubiera contratado un año.

| Campo | Kibot | FirstRate |
|---|---|---|
| PAPER_V1_VIABLE_FREE | CONDITIONAL guest raw, historia aquí no entregada; actions/paydate no resueltos | NO fullbundlefree demostrado; sólo muestras no descargadas |
| PAPER_V1_COST | Guest publicaccess0 anunciado; totalUNKNOWN; paidEOD14/mo no autorizado | InicialUNKNOWN; updates opcionales59.95/mo; totalUNKNOWN |
| LIVE_COST | Datos históricos no feedlive; stack/uso/escalaUNKNOWN | Idem, LIVE no seleccionado |
| FREE_ALTERNATIVE | Guest/otras rutas y SECeventos por admitir; no equivalencia de producto | Kibot/otras fuentes por admitir |
| PAID_INCREMENTAL_VALUE | Actions/entitlements/cadencia por verificar | Cobertura/minutebars/retención permanente, valor incremental por medir |
| ECONOMIC_JUSTIFICATION_REQUIRED | YES antes de gasto/contrato | YES antes de gasto/contrato |

Lock-in/exit: archivos conservables reducen dependencia de renovación para replay, pero no aseguran updates o corrección de acciones. Snapshots/hashes/versiones propios no crean vintages históricos faltantes. No admitir un dataset por términos favorables o FAQ;4DataCards+6subcards permanecen NOT_ADMITTED. Twelve/EODHD siguen AWAITING_VENDOR_RESPONSE sin permiso inferido.
