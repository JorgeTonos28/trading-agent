# QE0 — Nautilus 1.231.0: artefacto y componentes

Preregistro 2026-10-15. R-009 antes de una selección D-023; no backtest de PRICE/MATR ni ejecución financiera. Instalar/descomprimir exclusivamente wheel público en `.local/r009-nautilus-deps`, sin extras de brokers/visualización, servicios, Docker o cambios globales. Pin1.231.0 (línea1.x, release titulada Beta); docs2.x no aplican automáticamente. CPython3.14 Windows x64, wheelSHA295b67b127f67429ebb9d937bd11448f930bee697fca6a8e0ec1de343ad3c68c.

Intento1: hash del wheel; import core/version; construir Equity `FIXTURE.SIM` whole units con tick.01; comprobar que el modelo Equity rechaza qty.5; importar BacktestEngine sin ejecutarlo. Cada fase captura PASS/FAIL/ERROR por separado; dependencia ausente es ERROR de ese intento, no rechazo funcional del engine. Reutilizar numpy/pandas/deps del entorno localE2 donde compatibles. No resolver/instalar dependencias nuevas automáticamente tras un error; un próximo intento tendrá otro source/ID y alcance preregistrado.

El launcher usa HOME nuevo/env allowlist; guard socket Python impide conexiones Python, **no es seguridad OS ni barrera contra egress nativo**. No adapters/auth/endpoints ni acceso a precios; todo dato propio ficticio. Fuentes públicas y metadata SHA con licencia en manifest; no vendorear wheel/source en Git. Resultado no pasa QP1–10, corporate actions, calendario, fills, paridad live, target-host ni carga. Instalar un engine reutilizable de research no implementa Trading OS.

## Enmienda previa al intento2

QE0-01 capturó2PASS/2ERROR por pytz ausente. Instalación local adicional sólo pytz2026.5 y msgspec0.22.0, wheels PyPI/SHA verificados en descarga. El batch de otras dependencias se detuvo por ConnectionReset en metadata; ninguna de ellas instalada. QE0-02 repite fases para resolver ese error concreto, preservando source/result01. Guard socket.connect/connect_ex en lugar de reemplazar la clase evita romper imports estándar SSL; sigue sin aislamiento OS/egress nativo. No se convierte import/Equity en paridad del motor ni se añade un backtest.

## Enmienda previa al intento3

QE0-02:4PASS/1ERROR por pyarrow ausente; Equity rechazó.5. Antes de QE0-03 se añaden sólo wheels locales SHA verificados pyarrow25.0.0,portion2.6.3,sortedcontainers2.4.0,tqdm4.70.1,colorama0.4.6,fsspec2026.2.0. Solicitudes de metadata/fetch de click fallaron; no instalado ni requisito completo declarado. Un comando de instalación falló por filename de portion incorrecto y no instaló; corrección posterior conservada en manifest. QE0-03 incluye además constructor/dispose de BacktestEngine con loggingbypass, sin datos/estrategias/órdenes ni run(), para comprobar sólo inicialización. No QP ni paper. No seguir imports iterativamente tras este scope; si falta otra dependencia se conserva ERROR y obligación.

## QE1-ROUND-01 preregistro específico, antes de ejecutar

Hallazgo del reviewer: make_qty1.x usa redondeo bancario por defecto. Probe separado de QE0, sin repetir engineconstructor: valores1.6→default2/floor1,1.5→2/1,2.5→2/2,12.999→13/12; round_down(.5) debe rechazar cantidad0. Comprueba sólo Quantity/Equity y riesgo de redondear hacia arriba, no adapter/Risk/Execution ni QP6 global. Mismo wheel/deps/envlauncher, fuente/salida nuevas con hash; no nuevos installs ni red.
