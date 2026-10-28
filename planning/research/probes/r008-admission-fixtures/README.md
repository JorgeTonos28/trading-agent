# DA-S2 — QA sintético de admisión por rol

Protocolo previo 2026-10-28. Sólo registros ficticios creados por nosotros, con IDs ficticios y fechas2030. **Ningún endpoint o dataset licenciado es consultado, descargado o enviado a IA.** No datos históricos, señales o backtests. El laboratorio no implementa ingestion productiva ni admite proveedores.

Expectativas independientes: raw OHLCV y calendario con grain/ID/unidades; hueco no equivale a holiday; doble row/key y timezone; split-only versus full-adjusted; dividendo histórico unadjustedValue versus value reexpresado; CSV sin paymentDate; pay-date ausente no crea cash temprano; declarationDate sin timestamp/vintage no prueba PIT; corrección tardía no cambia snapshot viejo; OHLC diario con stop y ratchet en una misma barra es ambiguo; quote IEX no es NBBO; petición de export raw a cloud se deniega; dataset con licencia favorable pero calidad incompleta sigue NOT_ADMITTED.

Cada caso tiene clasificación esperada antes de ejecutar. Los resultados validan los casos del contrato, no cobertura/calidad/PIT real de seis ETF. Los scripts/capturas conservan hashes y no se repiten para aumentar PASS.

## DA-S3 — unidades de volumen, protocolo adicional previo

La documentación EODHD distingue OHLC as-traded y volumen ajustado por splits. Nuevos casos propios: invertir un factor completo de reexpresión conserva volumen histórico/participación; factor incompleto produce UNKNOWN; volumen ajustado combinado con precio raw exagera liquidez; conversión split-only de indicadores usa sólo acciones efectivas al cutoff; validación aritmética no acredita vintage ni completitud. Se ejecuta un script/captura separado, sin modificar DA-S2.

DA-S2 result01:21/21 expectativas. DA-S3 volume-units01:6/6. Sólo fixtures propias y aritmética de unidades, no datos o derechos admitidos.

Precisión de revisión: el protocolo menciona timezone, pero DA-S2 no ejecuta parsing de zona/DST. NOT_TESTED; pendiente con calendario/clocks admitidos. No modificar captura ni añadir PASS por esa mención.
