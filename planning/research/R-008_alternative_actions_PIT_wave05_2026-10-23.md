# R-008 — fuente alternativa de acciones corporativas y admisión PIT, wave05

2026-10-23. P1/D-022 RESEARCHING. Investigación documental independiente de las consultas Twelve/EODHD. **DOCUMENTATION_ONLY / NOT_ADMITTED**: sin cuenta, SDK nuevo, descarga de muestra, API, precios, backtest, holdout o gasto. No cierra D-022 ni el preregistro F0. Continúan B/K2/M1/G-R1, nominal10k y costes en las cinco escalas.

## Evidencia oficial y límite de cada hallazgo

| ID | Fuente consultada 2026-10-23 | Hallazgo y alcance |
|---|---|---|
| DB-A | [Dataset corporate actions](https://databento.com/docs/datasets/corporate-actions) | Historia anunciada desde 2018-05-01, actualización cuatro veces al día, registros por listing. Es cobertura documental global, no prueba de seis ETF, completitud o derechos |
| DB-B | [API get_range Python](https://databento.com/docs/api-reference-data/corporate-actions/corporate-actions-get-range?lang=python) | pit=False por defecto conserva última versión por event_unique_id/ts_record; pit=True conserva revisiones. Rango start inclusivo/end exclusivo, index por defecto event_date, alternativo ex_date/ts_record; índice NULL excluye filas. symbols omitido puede abarcar todo; allocate_isins=True puede consumir nuevas asignaciones en planes limitados. Semántica exacta de filas descartadas/asignación debe probarse antes de usar |
| DB-C | [Schema](https://databento.com/docs/schemas/corporate-actions) | ts_record es última modificación UTC; ts_created es alta del registro por Databento. Fechas del evento son locales al exchange. listing/security/event tienen identidades distintas, event_action expresa estado |
| DB-D | [Producto y FAQ](https://databento.com/corporate-actions) | Declara EDI y exchanges como fuentes; uso interno display/non-display, sin redistribución externa por archivos/API. Menciona free credits y planes limitados por ISIN. No demuestra licencia para enviar extractos a IA externa ni retención post-cancelación |
| DB-E | [Pricing](https://databento.com/pricing) | Precio depende de producto/uso; crédito promocional de alta no implica servicio recurrente gratis. La lectura no produjo cotización completa del producto corporate-actions para seis ETF; no trasladar precio de otro feed ni de un blog antiguo |

Fuentes distintas de databento.com aparecidas en búsquedas no se utilizan para inferir producto, licencia o precio. No copiar un ejemplo de API ni activar un crédito para resolver una ambigüedad de derechos.

## Consecuencia para PRICE–MATR y alternativas

**Inferencia de diseño, no medición:** la fecha anunciada DB-A no resuelve por sí sola desarrollo2005–2018 ni warm-up previo. Podría aportar acciones corporativas a2019–2022 o un cross-check, si pasan todos los gates; no abrir2023–30/09/2026 por esa posibilidad. Security-master con otra profundidad o historia general de precios no amplía automáticamente la de acciones corporativas.

Mantener fijas ventanas y universo; no unir años/vendors sin IDs, fechas, moneda, revisión, ajuste y reconciliación cruzada. Unir precios de un vendor con acciones de otro exige licencia y evidencia de ambos, más detección de doble dividendo/split. El derecho sobre reference-data no se transfiere a precios ni a datos de broker. La independencia del validador debe comprobarse: dos marcas comerciales pueden compartir upstream.

**Build-vs-Reuse propuesto:** WRAP condicionado para API/cliente existentes; REFERENCE_ONLY ahora para documentación y diseño. No seleccionar, instalar o construir proveedor propio. Una sola fuente no tiene que cubrir todas las funciones, pero una composición requiere demostrar integridad temporal/contable, coste y ruta de salida. No se ha agotado el universo gratuito.

## Clocks y controles a incorporar a la admisión

Estos requisitos especializan ADR-004/contrato de datos, sin cambiar política financiera:

1. Separar event/effective/ex/payment dates, reloj de revisión, alta del registro en vendor, disponibilidad demostrable al cliente y recepción local. Ni event_date ni ts_record son prueba suficiente de disponibilidad histórica. La fecha de alta posterior puede revelar backfill: no declararlo conocido antes sólo por el evento antiguo.
2. pit=True es necesario para conservar revisiones de esta ruta, pero no certifica por sí solo PIT. Verificar qué reloj ordena/filtra cada versión, backfills y cancelaciones, zonas/DST, límites de intervalo y paginación/completitud.
3. Separar **replay observado** (snapshots/receipts históricos conservados) de **reconstrucción as-of** (disponibilidad vendor justificada + retraso modelado). Una descarga recibida hoy no fue recibida por nuestro sistema en2005; tampoco obliga a rechazar toda reconstrucción histórica. Declarar estimando, evidencia y supuestos por ruta; si el primer acceso no puede acreditarse, no llamarlo PIT probado.
4. Conservar versiones originales, cancelaciones y procedencia. No deduplicar sólo event_id si hay pagos/opciones/listings distintos; no fusionar un ticker sin mappings as-of. Registrar esquema/params exactos y hashes cuando su retención esté licenciada.
5. Separar actualización anunciada de deadline operativo: la disponibilidad efectiva/latencia de señal y ejecución se evaluará según Decision Horizon. No inferir freshness para Risk desde acciones corporativas EOD.
6. Una consulta de lectura puede cambiar asignaciones/cuota. Antes de una llamada real: scope de símbolos explícito, presupuesto/licencia y semántica de allocate_isins verificados; modo que evite asignaciones puede omitir filas y no se tratará como dato completo. No se autoriza ninguna llamada con esta nota.

## Acceptance matrix previa, sin ejecutar

Casos de laboratorio ficticios; no son datos Databento ni validación del vendor. **Todos NOT_EXECUTED** en esta wave. Reutilizar harness/contratos existentes antes de añadir código. El objetivo es distinguir errores de reconstrucción, no producir señales.

| Caso | Preparación / error que se intenta detectar | Evidencia requerida |
|---|---|---|
| CA01 | Evento con v1 disponible en t1 y corrección v2 posterior a cutoff | Vista en cutoff conserva v1; latest-only no sirve para reconstruirla; no rellenar v1 ausente |
| CA02 | Evento antiguo, registro añadido después del cutoff | No certificar disponibilidad por event_date/ts_record; marcar evidencia temporal faltante o backfill explícito |
| CA03 | Recepción local tardía frente a disponibilidad vendor | Replay observado respeta recepción; reconstrucción usa disponibilidad/retraso justificados y etiqueta distinta |
| CA04 | Cancelación/revisión y varias payment options/listings | Historial conservado, claves/orden documentados; sin doble evento ni eliminación silenciosa |
| CA05 | Filtrado por fecha de evento versus fecha de revisión; NULL; frontera end | Rango y semántica declarados; detectar exclusiones y revisar controles de completitud |
| CA06 | Cambio de zona/DST y ex-date distinto de pay-date | No cash antes de su derecho/fecha efectiva correspondiente; no usar UTC como calendario de bolsa |
| CA07 | symbols omitido/ISIN no asignado, límites y respuestas parciales | No llamada real sin gate; detectar scope amplio, filas omitidas y cuotas antes de inferir cobertura |
| CA08 | Acciones/retornos ajustados y ledger de dividendos | Paridad de raw→actions→NAV con una contabilización y sin ajuste conocido después del cutoff |
| CA09 | Cruce de dos vendors o feeds con upstream compartido | IDs/unidades/cobertura y linaje; diferencias conciliadas, independencia no presupuesta |

Una matriz especificada no es PASS de componente, de dataset ni de motor. Antes de ejecutar con datos reales hacen falta licencia y plan de exposición M11; fixtures sin secretos pueden avanzar sin esperar respuestas externas.

## Scorecard por fase: candidato corporate-actions, no paquete de precios

| Campo | Evaluación actual |
|---|---|
| PAPER_V1_VIABLE_FREE | UNKNOWN para entrega durable suficiente; free credit no prueba continuidad ni licencia |
| PAPER_V1_COST | UNKNOWN: producto/plan, fijo, uso/asignaciones, licencias, almacenamiento y QA. Ningún coste real asumido |
| LIVE_COST | UNKNOWN: dataset/escala/retención, integración, continuidad y derechos operacionales por cotizar |
| FREE_ALTERNATIVE | Broker/otros vendors/archivos públicos de emisores, candidatos por admitir; no equivalencia de calidad afirmada |
| PAID_INCREMENTAL_VALUE | Versionado de eventos/mappings y menor mantenimiento si se prueba fidelidad/PIT/cobertura; beneficio no medido |
| ECONOMIC_JUSTIFICATION_REQUIRED | YES antes de gasto o activación; metodología/software libre no concede derechos de datos |

Escenario de demanda: un investigador, seis ETF/listings por verificar, historia y actualizaciones según contrato; volumen efectivo, fijo/variable, coste mensual estimado y según escala **UNKNOWN**, no cero. Evaluar todos los modelos admitidos/estrés en USD2k/5k/10k/25k/50k y mantener20celdas hipotéticas previas. Nominal10k no elige a posteriori escala favorable ni exige PASS en todas.

Lock-in/salida: IDs propietarios, revisiones y cuotas de símbolos, dependencia de upstream, transformaciones y retención no resueltos. Justificar pago sólo si una brecha free material queda probada, beneficio/coste y salida son defendibles y el propietario lo aprueba. LIVE conserva esta opción; no REJECT permanente por coste PAPER.

## Estado y siguiente trabajo

[Revisión independiente](R-008_wave09_independent_review_2026-10-23.md): sin P0/P1 materiales en este scope documental; no aceptación técnica/contractual ni cierre D-022.

La investigación reduce incertidumbre concreta de una alternativa sin esperar Twelve/EODHD. Mantener consultas READY_FOR_OWNER_SEND, NOT_SENT; ninguna respuesta aún. Todas las DataCards/subcards NOT_ADMITTED. Pendientes: semántica efectiva de disponibilidad/alta/backfill por versión, derechos/retención/IA, cobertura/quality real, precio aplicable y paridad. No admisión por claim comercial de PIT.

Paquete siguiente válido: casos CA con fixtures cuando hagan falta para resolver una implementación candidata; mapa de demanda por ventana/componente y evidencias de otras rutas; broker/protection y QP por gaps documentados; Risk/parámetros y métodos/preregistro según RC6. No nueva investigación agéntica general. implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED, INTEGRITY_UNKNOWN.
