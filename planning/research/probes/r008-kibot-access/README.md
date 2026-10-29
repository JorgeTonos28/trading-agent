# KD1 — acceso/forma de datos EOD gratuitos, protocolo previo

2026-10-23. El proveedor documenta guest público anónimo sin registro, no una credencial del propietario: https://www.kibot.com/api/api-access.html. Licencia pública permite uso interno/archivo y conservación, sin redistribución: https://www.kibot.com/license.html. Ninguna cuenta personal/trial/pago/contrato comercial enviado. API pública read-only, sin servicios ni cambios globales.

Scope preregistrado: seisETF SPY/QQQ/IWM/EFA/TLT/GLD, **2004-11-18 a2004-11-24** exclusivamente, requestdaily/unadjusted. No returns/señales/estrategia/calibración/ranking/backtest; no selección2019–22 o reserva2023–26. Expectativa: respuesta CSV OHLCV6columnas, fechas dentro del rango, valores finitos/positivos y high/low consistentes, sin duplicados; insuficiencia/cobertura faltante no se rellena. HTTP200 con error en body no es éxito. Login, hasta6history y logout, una conexión, timeout12s, sin retries. Si login falla, terminar requests financieras; si rango no respetado, no analizar precios ni persistir body fuera de scope.

Los datos brutos permitidos se almacenan **sólo en ignored.local** y no se imprimen, envían al modelo ni suben a Git. Captura Git limita estado técnico/fechas solicitadas/hashes y counts de controles sin precios/volúmenes/timestamps de trades. Usuario/password guest publicados por proveedor no son secretos ni cuenta privada; no capturar cookies/login response/query auth en logs/Git. Reproducibilidad de acceso no es inmovilidad/vintage del dataset.

PASS de acceso/formato sólo prueba esa respuesta pequeña; no derechos definitivos IA/non-display,6ETFhistoria completa, correcciones/PIT/paydates/calendar ni admisión. Guest no da ajustes según documentación: una fuente raw gratuita no completa por sí sola totalreturn/ATRasof/corporateactions. Costes y20celdas/fivecapitals preservados, no gasto.

## Resultado y diagnóstico

01: loginHTTP200/body200, seisERROR de parseo, logoutHTTP200; ningún raw persistido. [Diagnósticoacotado](diagnostic_protocol.md) observó en una requestSPY HTTP200/**body401**, una línea noCSV, sinbar/precio. No demuestra falta de cobertura histórica, rechazo de símbolos o causa de sesión. La documentación describe authporIP, no cookie/TCP; cookiecount0 no prueba defecto. **No nuevos retries ni bypass**. EstadoACCESS_NOT_ESTABLISHED_IN_RESEARCH_ENVIRONMENT; targetUNKNOWN; ningún datasetadmitido. Ocho requests01 y tresdiagnóstico, no operaciónbroker ni cuentaowner.
