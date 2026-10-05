# Reproducir probes de hardening (solo preparación)

Fixtures desechables; no módulos del Trading OS ni selección final. [Protocolo](../../R-010_014_hardening_protocol_RC0.md) y [dossier](../../R-010_014_hardening_findings_2026-10-05.md) gobiernan. Ejecutar desde raíz del clone en plan-architect. No API facturada, broker, OS setup ni credenciales en Git. Resultados originales permanecen; nuevas ejecuciones se guardan aparte antes de modificar cualquier resultado registrado.

## H1/H2/H3 y restore

Python stdlib 3.14.6 usado (versión SQLite guardada en result). Scripts contract_probe/lease_concurrency/queue/restore/evaluate no llaman modelos ni brokers; construyen DB temporal/relojes virtuales. Para repetir sin sobrescribir evidencia, usar copia en otro worktree/clone desechable y conservar resultados bajo nuevo ID/ruta; paths de wave07 deben mantenerse. H3 lee result-attempt-02 de wave07, no repite inferencia. queue_sensitivity_v1 corresponde a resultado histórico; v2 corrige labels, no convierte requests de reserva en retries reales.

## H4 bundle nativo

Dependencias observadas en [metadata](dependencies-observed.json), no lockfile final. Windows amd64. En directorios temporales **fuera del repo**:

1. Obtener paquete público openai-codex0.160.0 sin dependencias bajo `%TEMP%/r006-codexsdk-source` (pip `--target`, sin instalar global).
2. Obtener dependencias de metadata bajo `%TEMP%/r006-codexsdk-deps`; jsonschema4.26.0 y sus deps requeridas. El SDK necesita pydantic/packaging. Los otros temp paths opcionales usados previamente aportaban dependencias; no activos privados.
3. Descargar wheel `openai_codex_cli_bin-0.160.0-py3-none-win_amd64.whl` desde release PyPI de esa versión a `%TEMP%/r010_cli_0160`, verificar hash del dossier y extraer wheel a `source/` allí (incluye package y dist-info). No ejecutar un archivo sin hash verificado. H4 usa resolver default, no override a CLI instalada.
4. `PYTHONPATH` del **proceso**: `%TEMP%/r006-codexsdk-source;%TEMP%/r010_cli_0160/source;%TEMP%/r006-codexsdk-deps`, más directorios temporales de deps si realmente necesarios. No escribir cambios globales ni auth en repo.
5. Login Team previo por interfaz oficial/native, realizado por owner; script no copia/exporta token y aborta si cuenta/ruta/modelo no son los esperados. Plus no se necesita. Modelo explícito gpt-6.1-sol, sin fallback/billing.
6. Fijar `H4_ATTEMPT` nuevo; ejecutar stable_sdk_probe.py. No existe permiso para alterar política de seguridad para que pase. Dos jobs sintéticos research/shadow, clon Git y Skill local temporal; herramienta fija read_evidence. No heredarlo como perfil operacional.

Wheel SDK/hash/public source y schema fixtures están descritos en R-006 dossiers; propio probe importa helper wave07 y spine del mismo repo. Hay instrucción/root-rol verificadas; no requiere memoria del chat. Dependencias/logins/config efectivos siguen necesidades externas y el runtime final aún no se congela.

## H6 Temporal

Obtener release pública CLI1.9.1 Windows amd64 ZIP desde URL del dossier, verificar SHA256 y extraer a `%TEMP%/r010_temporal_191/source` (LICENSE y temporal.exe). Fijar `H6_ATTEMPT` nuevo y ejecutar temporal_probe.py. Script crea workspace temporal, proceso oculto headless/loopback, sin auth/config de usuario/workers/LLM; un workflow pendiente y schedule con una acción; mata/reinicia **solo PID propio** y limpia. Primer download urllib falló TLS y curl reintentó con TLS intacto; no desactivar validación ni instalar service/cloud.

evaluate_temporal.py evalúa resultado01 por nombre fijo; para nuevo intento ejecutar una copia con ruta de input/output nueva y dejar original. Prueba equality de run/status/**longitud** history, no el contenido íntegro de todos sus eventos. No aprobar producción con start-dev.

## Seguridad y hashes

Source_sha256 es hash raw del archivo ejecutado; reused_harness_sha256 de wave07 también raw y puede variar por EOL en Windows. Para identidad portable del repo usar Git blob del commit pinado conforme bootstrap. No modificar evidencia raw para igualar hash de checkout. Auth/account datos privados no aparecen en outputs; UUIDs H6 pertenecen a objetos sintéticos del servidor temporal, no cuentas reales. Scripts no garantizan frontera OS, quota sostenible, regla financiera, engine final o readiness PAPER.
