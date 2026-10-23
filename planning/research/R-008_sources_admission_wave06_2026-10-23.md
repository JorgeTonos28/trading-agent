# R-008 — alternativas, derechos y reconstrucción PIT: wave06

2026-10-23. Investigación pública y CA-S1 ficticio; **ningún dataset admitido, adquirido o descargado**. Doce hipótesis, cero trials. Twelve Data/EODHD siguen AWAITING_VENDOR_RESPONSE por declaración del propietario; fecha exacta no indicada. No respuestas/licencias inferidas, ni contacto adicional.

## Alternativas acotadas a la demanda ETF

| Candidato | Hallazgo verificado | Disposición actual / incertidumbre |
|---|---|---|
| Alpha Vantage | [Documentación](https://www.alphavantage.co/documentation/) TIME_SERIES_DAILY distingue compact100 gratuito de full histórico premium; DAILY_ADJUSTED es premium. Profundidad anunciada no demuestra cobertura de nuestros seis ETF | REFERENCE_ONLY; free no sustituye historia diaria completa. Coste del plan apropiado UNKNOWN, no crear cuenta/API key. No reconstruir daily desde weekly para simular stops |
| Norgate | [Paquetes](https://norgatedata.com/stockmarketpackages.php): Gold20años móviles; Platinum desde1990, USD630/año o346.50/6meses. Se investigó precio publicado, no cotización aceptada | Reserva paga REFERENCE_ONLY. Veinte años móviles no garantizan 2005 más warm-up en2026. Platinum es escenario de coste, no paquete seleccionado |
| Norgate: metadatos/calidad | [FAQ de datos](https://norgatedata.com/data-package-faq.php): assetid estable en integraciones compatibles; sin historia de tickers; cambios históricos por correcciones. Describe close ETF/NBBO y cambios de metodología | No convertir base revisada en vintages as-of. Requiere QA de seisETF, versión, eventos y disponibilidad. StableID no prueba PIT de todas las columnas |
| Sharadar | [Fuente del proveedor](https://sharadar.com/prices): **SFP funds**, separado de SEP stocks; incluye ETF y fondos deslistados, historia anunciada desde1997, entrega diaria17:30/23:30ET. OHLCV split-adjusted; raw/fulladjusted exigen imputación para todos los campos; lastupdated es fecha | REFERENCE_ONLY / WRAP condicionado. No asumir SEP=ETF ni lastupdated=vintage completo. Tarifas aplicables, retención, IA, snapshots de revisión, seisETF y rawOHLC real UNKNOWN |
| Stooq | Páginas públicas de términos/base devuelven challenge en esta superficie | RIGHTS_UNKNOWN / NOT_ADMITTED, no REJECT por imposibilidad de lectura. Sin bypass, scraping o historia descargada |
| SEC/EDGAR | Fuente pública ya estudiada en R-021, separación acceptance/event/filing y semántica por fila | Form4 permanece candidato externo independiente; no parte automática de PRICE/MATR, benchmark y evidencia propios. Accesibilidad pública no suministra precios ni reconstruye planes históricos ausentes |

La comparación no produce aún una alternativa gratuita que **demuestre conjuntamente** rawOHLC, acciones/vintages, cobertura, retención y derechos requeridos. Es una falta de evidencia de admisión, no prueba de inexistencia del mercado ni razón para contratar.

## Norgate: separación de usos y retención

El [EULA20261002](https://norgatedata.com/subscribe/eula.php), cláusulas2/8, permite procesamiento personal mediante terceros sujeto a no concederles uso independiente; eso exige comprobar términos/configuración del procesador, no autoriza automáticamente enviar datos a cualquier IA. Cláusula21 exige eliminar Content/Information, exports y backups al expirar; conserva Derived Data bajo definición restrictiva. No tratar snapshots/candles/audit con datos reversibles como derivados libres. [FAQ de suscripción](https://norgatedata.com/faq.php) confirma borrado en sistemas externos y no excepción de retención tras expirar.

**Inferencia de diseño:** Norgate no satisface por sí solo el rol de archivo bruto reproducible tras terminar suscripción. Mantener reserva de servicio activo/futuro, con dependencia de renovación y salida documentada; no alterar el requisito de auditoría para acomodarlo. Backtests/resultados derivados pueden conservarse en el scope contractual; no equivalen a poder reproducirlos sin insumos. No aceptación legal/contractual global por esta lectura.

## Economía por fase y todas las escalas

[Escenario publicado](source_cost_scenarios_wave06.json): Platinum630USD/año amortiza52.50USD/mes; **no es oferta mensual**. Carga anual simple fija en2k/5k/10k/25k/50k =31.5/12.6/6.3/2.52/1.26%; no es CAGR ni retorno esperado. Impuestos, FX, variables, otros datos/modelos/infra y coste de integración siguen UNKNOWN. Las20celdas hipotéticas anteriores permanecen; cada modelo real/stress que se admita debe evaluarse en las cinco escalas, referencia10k sin elección retrospectiva.

| Campos económicos | Registro actual |
|---|---|
| PAPER_V1_VIABLE_FREE | AlphaVantagefullhist NO; Norgate NO; Sharadar UNKNOWN; Stooq UNKNOWN; SEC fuente pública candidata, stack total UNKNOWN |
| PAPER_V1_COST | Norgate escenario fijo publicado630/año, coste total UNKNOWN; resto plan aplicable/variable/mensual UNKNOWN, nunca0 implícito |
| LIVE_COST | Revalidar planes, licencias non-display, escala y necesidades LIVE; no trasladar selección PAPER |
| FREE_ALTERNATIVE | SEC para filings, otras rutas de precios aún no admitidas; no sustituye productos de naturaleza diferente |
| PAID_INCREMENTAL_VALUE | Posible cobertura/actions/calidad/continuidad; beneficio incremental no medido |
| ECONOMIC_JUSTIFICATION_REQUIRED | YES para cualquier pago; beneficio y lock-in/retención deben justificar coste, owner antes de gasto |

## Evidencia de clocks efectivamente ejecutada

[CA-S1](probes/r008-pit-reconstruction/README.md): intento01 ERROR de serialización preservado, intento02 doce checks ficticios PASS. Distingue revisión conocida as-of, latest-only insuficiente, recepción observada frente a reconstrucción, cancelación y rango exclusivo. La identidad de NAV del pago **no ejecuta transición ni idempotencia**; NOT_TESTED. Ausencia de registro utilizable no prueba inexistencia del evento. CA07cuotas/CA09independencia y timezone/DST no contrastados con proveedor.

Siguiente admisión requiere contrato aplicable por producto/uso, retención brutos/derivados/snapshots/backups/audit, procesador local versus IA externa, muestra técnicamente verificable, coverage/calidad/PIT y costes. Respuesta comercial genérica no basta. El trabajo de broker/engine/Risk/método continúa sin esperar correos.
