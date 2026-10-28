# QL3 — ruta local LEAN source, protocolo previo

2026-10-28. ADR-023 elige familia, no pin. Laboratorio de compilación del entrypoint público y carga de sus tipos, **sin invocar Launcher.Main, Initializer.Start, Engine.Run, Algorithm, broker o backtest**. No datos, cuentas, APIs privadas, CLI/Cloud comerciales, Docker, servicios o instalación global.

Fuente esperada: f3d841e60dfd010ee5fc293ea893e56952484108 en `.local/lean-source`. Verificar pin antes del trabajo; inventariar cambios previos (Engine.csproj sin referencia a ejemplos Algorithm.CSharp de QL1). Ampliar sparse checkout únicamente con Launcher/Messaging/Queues, nunca Data. El launcher stock referencia ejemplos, optimizador, research, downloader y toolbox. Para contrastar el camino mínimo se compila el mismo Program.cs con un proyecto de laboratorio que referencia Engine, Messaging y Queues; no se afirma build de la solución stock intacta.

Expectativas: restore/build con .NET10 y NuGet público scoped existentes; producción de un host local desde fuente sin login/CLI. Un smoke separado carga por reflexión los tipos de Program/Engine/JobQueue/Messaging sin llamar al entrypoint. Las rutas de configuración local y providers se inspeccionan estáticamente y se reportan aparte. Compilar/cargar tipos no demuestra ejecución de un algoritmo, seguridad, ausencia universal de red, suficiencia o paridad.

Máximo dos intentos por error de harness, con capturas separadas y límites por proceso. El driver no sobrescribe resultados. Env allowlist, caches de investigación existentes, logs completos ignored y evidencia sanitizada en Git. Warnings de dependencias se preservan; no pin operacional aceptado por compilar.

Resultado01: restore/build/metadata smoke PASS,6 checks. Main/Engine.Run no invocados. Proyecto mínimo distinto de solución stock, parche previo QL1 conservado. Nuevos warnings preservados y hashes de artefactos observados después; no pin/target aceptados.
