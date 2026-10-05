# R-028 / R-006 — probes desechables de portabilidad

No instalador ni implementación Trading OS. Ver [protocolo](../../R-028_bootstrap_probe_protocol.md) y [resultados](../../R-028_bootstrap_findings_2026-10-05.md).

- `native_probe_attempt01.py` y `native_probe_attempt02.py`: snapshots originales del harness, errores preservados.
- `native_probe.py`: parser de fuentes corregido; fixture TEMP, discovery nativo y smoke Team. No configuración global ni extraRoots. Target Plus UNKNOWN. Intento 04 completa cinco turnos pero falla cleanup Windows después; no repetir para ocultarlo.
- `offline_probe.py`: manifiesto/schema y clasificación de perfiles sintéticos, 31 checks. `fixtures-readiness.json` son simulaciones, no perfil observado Plus.
- `result-native-attempt-*.json`: resultados incrementales originales sin secretos, IDs de cuenta/threads, stderr ni chain-of-thought.

Dependencias reutilizadas: Python 3.14 local, Git, CLI Codex pin registrado, jsonschema disponible en TEMP de investigación. Reproducción en otra máquina debe declarar/instalar legítimamente sus herramientas; paths TEMP actuales no son parte del contrato. Para prueba nativa `--output` debe ser nuevo; `--metadata-only` no ejecuta inferencia ni cambia cuenta. No usar fixtures completas de Plus como readiness real.
