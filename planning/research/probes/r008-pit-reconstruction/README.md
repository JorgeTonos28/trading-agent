# CA-S1 — clocks/versions, probe previo con datos ficticios

2026-10-23. Subconjunto CA01–06/08 de wave05: conserva revisiones; cancels, rango exclusivo, recepción versus reconstrucción y dividendo receivable/pay-date. Registros propios2030, símbolo inexistente; stdlib, sin API/vendor/raw market data/backtest. No cliente de ingestión ni adaptador productivo. No acepta disponibilidad histórica por probar la lógica con clocks inventados.

Expectativas: cutoffdía2 eligev1 disponible día1, no correccióndía3; latest-only sin v1 produce INSUFFICIENT_EVIDENCE, no NO_EVENT. Evento antiguo sin disponibilidad demostrable es UNKNOWN. Descarga recibidadía6 puede reconstruirse al día2 con evidence+delay adecuados, pero no ser replay observado de ese día. Cancelación conocidadía4 no borra snapshotdía2. Rango[a,b) excluyeb; div10 se registra una vez como receivable y se mueve a cash al pago, sin doble crédito. Fechas UTC de fixture no prueban timezone/DST/calendario reales.

CA07 cuota/asignaciones/filas omitidas y CA09 independencia/upstream quedan NOT_EXECUTED_VENDOR. CA06 sólo contabilidad de fecha de pago, timezone/DST sigue NOT_TESTED. Los otros IDs reciben SYNTHETIC_COMPONENT_ONLY, no PASS vendor/dataset/paridad. Resultado create-exclusive y hash de fuente; no repetir sobre el mismo nombre. Licencia/coverage/quality/PIT reales permanecen no admitidos.


Intento01: ERROR_CAPTURE al serializar Decimal; captura parcial intacta result-01.partial.txt y manifest de error con hash. Intento02 cambia sólo serialización (antes de crear salida, default=str); mismos fixtures/expectativas, source01 intacto. No afirmar PASS de01 ni sobrescribir evidencia parcial.

## Resultado y límites tras revisión independiente

Intento02: 12 PASS de fixtures, 0 FAIL/ERROR. `CA08_PAY_MOVES_RECEIVABLE_TO_CASH` sólo comprueba una **identidad algebraica de NAV**. La transición de estado receivable→cash, el procesamiento de pago y su idempotencia están **NOT_TESTED**; la expectativa descrita arriba no se convierte en evidencia de ejecución. `NO_EVENT_PROVEN` en el fixture con retraso significa **ningún registro utilizable en esa vista/cutoff**, no inexistencia del evento corporativo. Un consumidor real debe distinguir esas situaciones y UNKNOWN; no reutilizar ese nombre como prueba de ausencia. CA07/09 siguen NOT_EXECUTED_VENDOR, calendarios/DST NOT_TESTED. No aceptación de dataset ni paridad desde estos fixtures.
