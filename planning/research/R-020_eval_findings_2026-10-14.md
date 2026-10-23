# R-020 E2 — resultados de primitives y contratos sintéticos

2026-10-14 · [protocolo previo](probes/r020-evaluation/README.md), [fuente](probes/r020-evaluation/probe_attempt01.py), [result01](probes/r020-evaluation/result-01.json), [dependencies/hashes](probes/r020-evaluation/dependencies-01.json). Source/result01 intactos; sin estrategias, histórico, datos financieros, cuentas, target acceptance ni permisos operativos.

## Observado

- statsmodels0.15.0/arch8.0.0 y15 distribuciones pinadas/hashes de wheel en `.local/r020-eval-deps`; Python3.14 existente, sólo binaries/base, sin build/global/admin. Licencias de principales consultadas; transitivas **NOT_COMPLETE** antes de seleccionar stack. Gasto incremental0, mantenimiento/target compatibilidad UNKNOWN.
- **19/19 PASS** según expectativas preregistradas:9comprobaciones primitives/admission y10escenarios de tiempo/evidencia. Holm conocido/permutado produce valores esperados; seed fijaStationaryBootstrap conserva120observaciones y pairing3× entre columnas.
- Vector con NaN **devuelve NaN sin rechazo automático**. Checks de admission externo detectan finitud/vacío; no prueba de un validador productivo. Alpha0.05, block5, seed1234 y muestra120 son **fixtures**, no criterios/parametrización aprobados para trading.
- No socket/DNS bloqueado observado en esta ejecución; Python audit no demuestra aislamiento de proceso/egress Windows. stdout acotado, stderr0líneas; launcher se ejecutó desde `.local`, copia archivada sólo evidencia.

## Lo que no demuestra

No intervalos, power, tasa de falsos positivos, block-length selection, DSR/PSR/PBO, dependencia/regímenes históricos, freshness semántica real, broker deadline/calendario, drift/feed/revisiones, Risk Engine o reproducibilidad operacional. Protocolos requieren MethodApplicabilityCard y pruebas adicionales antes de cierre. F0 NOT_FROZEN; dataset NOT_ADMITTED; estrategia NOT_SELECTED. Cero strategy trials en registry, no contar este probe como backtest.

Disposición recomendada **REUSE_AS_IS primitives + WRAP admission/version/paired lineage**, candidata no seleccionada. Usar librería contrastada evita proponer suite estadística general BUILD; paridad de dos funciones no selecciona modelo estadístico definitivo. Estado TECHNICALLY_COMPATIBLE=PARTIAL research, AVAILABLE_TARGET=UNKNOWN. Economía común en RC2; software0 no significa operación total0.

## Reproducción y siguiente gate

Archive launcher depende de ubicación `.local/run_eval_probe.py`; no ejecutarlo directamente desde probes. En fresh research clone, preservar original y preparar nuevo attempt/create-exclusive con intérprete/deps/seed/env propios documentados; hashes de fuente capturada y wheels permiten identificar intento. SHA256 aquí es **raw bytes capturados**; verificar Git blob del commit para portability/EOL, no reescribir captures si checkout transforma saltos. No repetir para mejorar score ni declarar target acceptance por reproducir aquí.

Gate siguiente de método: fallos/inputs no finitos, short/constant samples, serial/cross dependence y block-length sensitivity, prueba de intervals/power con distribuciones simuladas y errores conocidas; validación de p-values antes de ajuste. Target operacional/muestras reales/backtests en PC personal; investigación sintética autorizada en Team. Q056 dirección económica aporta requisito para especificar efecto/muestra, no selecciona primitives por sí sola.
