# E3 — endpoints, exposición y tamaño de muestra: protocolo previo

2026-10-14 · experimento desechable con fixtures ficticios, sin datos reales/retornos de PRICE/MATR ni backtest de estrategia. Reutilizar arch8/statsmodels0.15 de E2 sólo para primitive probes; sin nuevas instalaciones/cuentas/OS/admin. No implementar suite productiva.

Expectativas preregistradas: misma λ y cash que benchmark debe producir misma serie; cash-only no satisface cashpremium>0; retirarcashcarry o imputarlo dos veces debe diferir de ledger correcto; inferiority bound no pasa a partir de pointestimate, ratiosrisk inválidos no son0; matriz intervals marginales no se etiqueta conjunta; todos insuficientes=>NO_STRATEGY_QUALIFIED con razones, no FAIL automático. Direction tests son contrato ficticio, no margin aprobado.

Reutilizar `StationaryBootstrap.conf_int` en vectores sintéticos pareados, one-sided bounds repetibles, incluidas nonfinite/constant inputs admitidas/rechazadas externamente. Registrar limitaciones/errores sin alterar fixtures para PASS. Examinar tabla analítica de power para margen0.5/1/2pp con σdifference1/5/10% anual y α0.025/power0.8 **sólo supuestos ilustrativos**, nunca valores aprobados ni garantía sobre candidatos. Fórmula normal iid anual con igualdadverdadera; validar al menos un caso frente a solve_power e informar discrepancia/limitación, no trasladar resultado a bootstrapCAGR/regímenes.

Captura create-exclusive source/results/pins/hash/seed; proceso research sin secrets/envallowlist/redguardPython. Dependencias15 de E2, no fullprocesssecurity. F0/target/Strategy NOT_ACCEPTED, margennumérico no aprobado. Potencia/coverage conjunta empírica/censura/tails completa requiere protocolo adicional; no afirmar por estos fixtures que19/19previo o nuevoschecks equivalen a alpha.

## Captura ejecutada y alcance

[Source](probe_attempt01.py), [result](result-01.json), [launcher archivado](executed_launcher_archive.py) y [dependencias reutilizadas](dependencies-01.json) preservan la ejecución única. El launcher es un archivo histórico del helper privado, no un comando listo para ejecutar desde esta carpeta. Para reproducir en otro entorno, reconstruir rutas/env del protocolo y dependencias pinadas; emitir nueva attempt/captura, nunca sobrescribir esta evidencia ni usar disponibilidad Team como aceptación target. No se reinstalaron dependencias.

Los hashes de probes son de bytes capturados. Las declaraciones del registry conservan por separado bytes/EOL de captura y hash del blob Git normalizado cuando difieren; un fresh clone con otro EOL no modifica la historia. Verificar contra el commit fuente, no contra documentos que han recibido adendas posteriores.

E3 captura **19/19 fixtures**, pero muestras constantes/no finitas de conf_int previstas no fueron ejecutadas: NOT_TESTED. Ratio NaN no sustituye esa prueba; ninguna cobertura estadística/alpha/candidato queda demostrada.
