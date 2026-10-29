# Datasets — admisión por instrumento, warm-up, PIT y derechos

2026-10-15. R008/D022 RESEARCHING. **Ningún dataset admitido**, ninguna descarga de precios/acciones/holdout, cuenta o gasto. [Subcards](datacards/ETF_instrument_admission_RC1.json) separan6instrumentos y gates verificables; metadata de emisor no es cobertura del vendor.

## Warm-up e inception: corrección concreta

[GLD/emisor](https://www.spdrgoldshares.com/usa/gld/) publica listado e inception18-11-2004, ISIN US78463V1070. Por pura cota de calendario hay45días entre18nov y1ene inclusive: no pueden existir200sesiones anteriores a2005. Ni un vendor pago puede fabricar esa historia. No sustituir GLD por oro spot/futuros/otroETF o usar proxy sin variante/gobierno.

**Propuesta técnica W0 para preservar ventanas:** universo fijo de6, pero cada señal exige la historia válida de sus propios indicadores; miembro no preparado=`NOT_READY_INSUFFICIENT_HISTORY`, no dato0/forward-fill ni universo cambiado. PRICE necesita127cierres para breakout previo126/ROC126; MATR necesita200 paraSMA y ATR/TR según contrato. Puede haber primeras fechas de elegibilidad distintas. No alterar2019–2022 común ni2005–2018 del desarrollo para encajar en providerfree; reportar la cobertura/eligibilidad exacta del tramo inicial. Un benchmark BH no necesitaSMA200 para comprar, pero sí datos/cash/calendario de ejecución admitidos.

W0 permite describir el período con elegibilidad parcial conocida, **no afirmar seis activos con warm-up completo desde enero2005**. Si se exige retrospectivamente una cohorte con todos listos desde el inicio, cambiar a un inicio común posterior es otra especificación y debe registrarse antes de resultados; no reemplazar ventana silenciosamente. El cross-check efectivo de fechas usa calendario/listado/dataset, no bdays genérico. Para otras5fechas/mappings, UNKNOWN hasta evidencia por subcard; no inferirlas por antigüedad del ticker.

## Gate de admisión por entrega y uso

| Gate | Evidencia necesaria antes de usar | Estado actual |
|---|---|---|
| Rights | Términos efectivos para usuario/host/uso, raw/derived retention, backup/exit, uso por modelo/cloud y redistribución diferenciados | UNKNOWN/CONDITIONAL por vendor |
| Coverage |6symbols/IDs, sesiones requeridas+warm-up, OHLCVraw/actions/paydates, missing/delisted/mappings | NOT_TESTED |
| PIT | event/available/receipt/revision time y versión usada; reconstrucción justificada as-of, no adjustedlatest=as-of | NOT_TESTED |
| Quality | calendario/units/duplicates/missing/stale, actions y reconciliation, independiente secundario | NOT_TESTED |
| Replay | archivo permitido/hash/version transform, raw→indicador→snapshot→ledger; prueba en engine/modelo admitido | NOT_TESTED |

Separar first-delivery histórico **UNKNOWN** de una reconstrucción de raw/events con hipótesis explícitas; no llamar a esta última PIT probado. Declarar resultado de sensibilidad frente a correcciones/availability, intervalos de publicación y sesgo potencial. Para señales externas Form4 el clock de acceso/publicación sigue gate estricto R021, no sólo la fecha transacción. Datos EOD no prueban fresh quotes de Risk o fill/protección intradía.

## Rights: hallazgos oficiales, no licencia inferida

| Ruta | Verificado2026-10-15 | Consecuencia actual |
|---|---|---|
| Twelve | [Terms](https://twelvedata.com/terms) §§12.5/16 requieren borrar Data al terminar; derived compliant pertenece al cliente, audit/compliance tiene excepción limitada | No asumir archivo perpetuo para replay privado ni permiso de compartir raw con LLM. Requiere aclaración aplicable/terms. CONDITIONAL_NOT_ADMITTED; no resuelto por pagar |
| EODHD | [Terms](https://eodhd.com/financial-apis/terms-conditions) permiten storage/manipulation/análisis privado no comercial, restringen compartir/retransmitir y distinguen personal/comercial | Research en host institucional/Team no presume licencia personal. Retención tras terminación/uso cloud/modelos y origen de datos indicativos siguen por aclarar. Paid reserve, sin suscripción |
| Alpha Vantage | [Terms oficiales](https://www.alphavantage.co/terms_of_service/) leídos, no hallazgo suficiente de archivo durable/uso concreto en esta wave | Derechos no admitidos; profundidad/plan requiere ficha previa, no declarar licencia por clienteOSS |
| Stooq | [Ruta terms](https://stooq.com/terms.html) no devolvió contenido útil | UNKNOWN; acceso público o librería descargadora no conceden licencia. Sin scraping de precios ni rechazo global |
| Alpaca/IBKR | Fuentes broker R007/008 existentes, historia/feeds/entitlements/documentación | Cuenta/API/datos/retención y ámbito cloud por producto; no asimilar registros de propias ejecuciones a redistribución de market data |

No se envió consulta a proveedores. Preguntas listas para futura aclaración autorizada: seisETF/2004+raw/actions/paydate; snapshots/revisions/PIT; archivo privado reproducible y retención después de cancelar; derived traces/backup; procesamiento por un agente en nube bajo cuenta personal versus investigaciónTeam; límites non-display y ausencia de redistribución pública. Guardar respuesta fechada/contrato, no aceptar marketing como permiso. Si requiere contacto/cuenta/gasto se presenta gate concreto, sin detener trabajo técnico independiente.

## Economía y reuse por fase

PAPER_V1_VIABLE_FREE permanece CONDITIONAL/UNKNOWN según ruta, no toda gratuidad es suficiente ni imposible. PAPER_V1_COST: acceso free0 donde publicado, paid sin aprobación; almacenamiento/operación/QA UNKNOWN. LIVE_COST: producto, escala y acuerdos UNKNOWN. FREE_ALTERNATIVE: otras rutas previas broker/públicas/OSS por admitir. PAID_INCREMENTAL_VALUE: historia/cobertura/continuidad **si verificadas**. ECONOMIC_JUSTIFICATION_REQUIRED=YES para gasto. Costes por provider publicados en wave03 son referencia fechada, no nueva cotización ni permiso; fijo/variable/mensual/escala/lock-in permanecen scorecard. Conservar alternativa gratuita y salida/retención antes de pagar. Ninguna ruta seleccionada.

Parser/SDK/dataset existentes WRAP/ADAPT antes de BUILD. Separar código importador libre, licencia del dato y privilegio de cuenta. [E7](probes/r020-path-semantics/README.md) prueba sólo la cota calendario; no QA del histórico. Reserva INTEGRITY_UNKNOWN, locktrue y targetdeferred.
