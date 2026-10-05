# Disposable R-006 probes

Estos archivos son experimentos de Preparation, no implementación de Trading OS. Ver [protocolo](../../R-006_behavioral_protocol_2026-10-05.md), [wave 04](../../R-006_probe_wave_04_2026-10-05.md) y [wave 05](../../R-006_probe_wave_05_2026-10-05.md).

## Reproducir evaluación sin consumir inferencia

Python con `jsonschema==4.26.0` (la versión efectivamente usada consta en `summary.json`; no instalar dependencias de producción). Desde raíz del repo:

```powershell
$env:PYTHONPATH = Join-Path $env:TEMP 'r006-pydeps'
python -B planning/research/probes/r006-behavioral-team/evaluate.py planning/research/probes/r006-behavioral-team/result-attempt-02.json "$env:TEMP/r006-evaluation-replay.json"
python -B planning/research/probes/r006-behavioral-team/role_admission_probe.py
```

El segundo comando reproduce el resultado local de schema en el directorio del probe; no llama modelo/broker. No reescribir outputs históricos de inferencia para lograr un resultado mejor. La rúbrica predefinida y el experimento posterior de admisión por rol son análisis diferentes.

## Dependencias temporales

Los probes usaron `pip --target` fuera del repo. No usar la API de OpenAI/Anthropic ni activar facturación como instalación/prueba. Para reinstalar las dependencias gratuitas locales necesarias:

```powershell
python -m pip install --target "$env:TEMP/r006-pydeps" jsonschema==4.26.0
python -m pip install --target "$env:TEMP/r006-mcpdeps" mcp==2.3.0
```

`mcp_mock_probe.py` activa las rutas pywin32 de ese destino para Windows. No requiere postinstall global; ejecuta SDK MCP oficial sin modelo ni red de datos. Dos procesos nuevos de fixture no prueban recovery del Trading OS o autenticación.

```powershell
python -B planning/research/probes/r006-behavioral-team/mcp_mock_probe.py --output "$env:TEMP/r006-mcp-replay.json"
```

## Nueva inferencia conductual

Requiere autorización para usar cupo de investigación y CLI/autenticación nativa ChatGPT Team; la autorización para esta ejecución consta en la instrucción del propietario. El script verifica account type/plan sanitizados, no refresca/exfiltra credenciales ni cae a una API key; máximo veinte turnos, contextos efímeros. No instalar Skills persistentes, conectar providers ni dar canales de órdenes. No correrlo bajo Plus como repetición de discovery; Plus Acceptance Gate tiene otro alcance.

```powershell
$env:PYTHONPATH = Join-Path $env:TEMP 'r006-pydeps'
python -B planning/research/probes/r006-behavioral-team/probe.py --output "$env:TEMP/r006-new-attempt.json" --limit 20
```

CLI/schema/modelo/versiones pueden cambiar; pin observaciones y conservar nuevos intentos aparte. El script usa protocolo experimental de tools dinámicas; discovery solo no prueba entrega. Marker confirma contenido del procedimiento, no autoridad ni calidad. Si falla runtime/marker, se detiene y conserva datos. En esta investigación el intento 01 es inválido como comparación; el intento 02 es la muestra de veinte.

Licencias: SDK MCP MIT; jsonschema MIT; metodología pública Anthropic Apache-2.0 (atribución/versiones en las adaptaciones); propios protocolos de research/pedagogía del proyecto. Skills del plugin OpenAI Data son Proprietary y **no** se incluyen aquí. Licencias de datos/servicios externos son independientes.
