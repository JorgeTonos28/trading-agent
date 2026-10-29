# QL6 — diagnóstico de build y alcance de remediación

Protocolo previo, 2026-10-29. Un intento nuevo; QL5/01–02 no se modifican. Verificar hashes de los archivos transformados y targets contra QL5/01. Reutilizar únicamente su export de código público y cache local, sin Data, cuenta, secretos, Engine.Run, Algorithm o CLI/Cloud. Crear un host/smoke nuevos con directorios obj separados; es un cambio explícito de packaging de laboratorio, no repetición idéntica de QL5 ni prueba de que ese packaging causó sus timeouts.

Restore ≤45s, build ≤180s, metadata/fixtures ≤20s, logs a archivos propios; herramientas retornan sesión para poder continuar el análisis. No suprimir warnings ni debilitar expectativas. Capturar errores/tiempos, hashes de artefactos después del build y diagnósticos. La compilación no ejecuta Main del launcher.

Si compila, repetir las seis expectativas QL5. Añadir control de alcance de `UnzipToFolder(byte[], folder)`: inspección estática detectó otro `Path.Combine` sin containment. ZIP propio `../sibling-canary.txt` sólo puede alcanzar sibling de extract dentro del nuevo lab. Registrar si el path adicional sigue inseguro; observarlo NO equivale a seguridad PASS. No ataques absolutos/UNC/device, permisos OS o archivos ajenos. Separar build compatible de seguridad completa. Pin continúa no aceptado hasta cerrar extracción/import/dep/license/config/QP/target.
