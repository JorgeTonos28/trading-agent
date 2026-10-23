# QE2 — matching nativo, protocolo previo a ejecución

2026-10-23. Nautilus1.231.0/wheel previamente fijado; cliente nativo instalado en .local, sin instalar nuevo SDK. **MICROPROBE_COMPONENT_ONLY**, no PRICE/MATR, histórico, backtest de estrategia, broker, API, credenciales, target o Trading OS. No usar BacktestEngine.run() ni clases Strategy. Sólo OrderMatchingEngine con Equity/quotes ficticios y un consumidor de eventos de laboratorio; no ledger operativo ni engine Risk.

Expectativas previas: stop-market sell95 cruzado por bid90 llena a90, no95; stop-limit95/94 no llena con bid90 y sí después de recuperar94; dos trayectorias con mismo OHLC100/102/90/92 pueden producir distinta ejecución stop-limit; consumo de liquidez debe contrastarse explícitamente, no suponerse por volumen de barra. Cuenta CASH y compras/posiciones ficticias previas permiten las ventas, sin short/leverage. Trace de fills/eventos y errores se conserva por intento; cada salida create-exclusive, sin ocultar FAIL/ERROR con reruns.

Se prueban cinco escenarios (gap-market, gap-limit con recuperación, path-high-low, path-low-high, liquidez compartida con/sin consumo). La variante path no implementa ratchet ni estrategia. Consumidor de eventos aplica Order/Position nativos en cache de memoria; no evalúa balances/settlement, fee realism o paridad broker. El resultado puede falsar una suposición de modelo; no pasa QP1–10 completos. Expectativas y datos no se ajustan para producir PASS; un defecto del harness exige nuevo intento con fuente/hash propio.

Python socket guard y env mínimo reducen conexiones accidentales; no constituyen aislamiento de proceso nativo. No se invoca adaptador/red. El código de laboratorio es propio, importa librería LGPL3 sin copiar su implementación. Pin/atribución en QE0/dependencies.json; target/versiones/licencias transitivas aún requieren gate. Repetibilidad comparará sólo trace económico/eventos, excluyendo UUID aleatorio y tiempo de captura, sin llamar a eso reproducción en Plus.


Intento01: 0PASS/0FAIL/5ERROR, todos INITIALIZED→FILLED por falta de OrderSubmitted en harness, no defecto demostrado del matcher. Fuente/result01 preservados. Intento02 agrega únicamente evento previo SUBMITTED y actualización cache; mismas expectativas/quotes. No repetir01.

## Resultado ejecutado

Intentos02/03: **7 PASS / 1 FAIL / 0 ERROR**, mismas trazas económicas; repetición no amplía cobertura. El FAIL de cap≤5 observó fills6 con consumo activo: `backtest/engine.pyx` del wheel1.231.0 continúa market orders sintéticamente un tick más profundo cuando agota L1. No demuestra que seis acciones reales fueran imposibles ni bug universal; refuta tratar el flag como hardcap de la quote. Ambos paths OHLC produjeron resultados distintos de stop-limit. No fills/cash/fees/settlement/paridad financiera aceptados fuera de este scope de matching. Capturas01–03 y ambas fuentes se conservan.
