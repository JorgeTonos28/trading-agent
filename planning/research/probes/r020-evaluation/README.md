# E2 — evaluación estadística y tiempo: protocolo sintético

2026-10-14 · preregistrado antes del probe. Datos ficticios/semillas fijas, sin precios reales ni backtest. Investigar primitives reutilizables: statsmodels0.15.0 `multipletests(method='holm')`, arch8.0.0 `StationaryBootstrap`; metadata PyPI confirma wheelscp314. Instalar base sólo en workspace `.local/r020-eval-deps`, sin build/source/global/config/admin/API/accounts. Licencias revisadas en R020RC2, software no seleccionado.

Expectativas previas:

- Holm con p-values ficticios0.01/0.04/0.20 produce ajuste0.03/0.08/0.20; label alpha0.05 sólo caso de prueba, no criterio aprobado para estrategias. Permutar orden mantiene IDs y resultados; NaN y vector vacío deben rechazarse en admission externo, no tomarlos como tests aprobados. La librería puede devolver valores sin error: capturar sin corregir source ni ocultar.
- Stationary bootstrap: dos columnas ficticias pareadas de120observaciones, cada una3×la otra; seed repetida produce mismos índices, longitud120 conservada y columnas siguen relación. No test estadístico de estrategia ni estimación de intervalo/power/optimal block length. Probar sensibilidad iid vs dependencia sólo queda NOT_TESTED en esta wave.
- Fixture de tiempo: disponible después de cutoff=>NOT_AVAILABLE; expirado=>EXPIRED; pasado brokerdeadline=>MISSED_DEADLINE; UNKNOWNcoverage=>UNCERTAIN; contrato sin campos=>NOT_EVALUATED; muestra declarada insuficiente=>INSUFFICIENT_EVIDENCE. Casos PASS prueban expectativas del autor, no semántica broker/OS/clock ni Risk Engine.

Fuente/result create-exclusive, cada fallo preservado; no cambiar fixtures para obtener PASS ni ejecutar suite Trading OS. Source/deps hashes, stdout acotado, env del proceso hijo con allowlist y HOME privado; Python socket audit antes de imports, no aislamiento Windows. No reabre R006 ni toca H7. Registry de trials de estrategias sigue executed0; E2 se registra como probe sintético distinto.

## Captura posterior

Attempt01:19/19PASS, NaN library returnedNaN, import sin error; [result](result-01.json)/[fuente](probe_attempt01.py)/[deps15](dependencies-01.json)/[launcher archivado](executed_launcher_archive.py). [Dossier de alcance](../../R-020_eval_findings_2026-10-14.md) separa comportamiento parcial de criterio final. Launcher original ubicación `.local/run_eval_probe.py`; no ejecutar archive directamente ni sobreescribir result01. Source/model fixture no se cambia tras observación para ocultar fallos.
