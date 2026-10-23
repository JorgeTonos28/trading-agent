# QL0 — LEAN source/build feasibility, preregistered

2026-10-23. Public source commit f3d841e60dfd010ee5fc293ea893e56952484108 observed with git ls-remote. Candidate pin for investigation, not release approval. Sparse checkout only Common/Compression/Configuration/Logging and repository-root build/license files; no Data, Algorithms, tests or historical samples. Do not run launcher/strategy or activate CLI/Cloud/Docker/WSL/auth.

Allowed probe: inspect projects and build Common using already installed .NET10.0.302, dependencies from public NuGet only, temporary .local caches/home, telemetry/first-run notifications disabled, no build servers. No global install/config or credential sources; scoped NuGet config clears other feeds. If dependency/network/build fails, record ERROR/BLOCKED with evidence, not engine rejection or PAPER failure. Every attempt/capture immutable. A successful Common compile is not full LEAN build, runtime, fill/corporate-action paridad or target acceptance. Public source license does not license data or external packages automatically.

Expected gate: source/pin/license inspection plus Common compile compatibility or concrete missing requirements. Build latency/size only describes this host/process and cannot rank production performance. Files remain research dependencies under ignored .local; persist sanitized manifest/result/source hashes, not vendored engine or raw build logs containing local identifiers. No spending, broker or market-data network.


Intento01: restore ERROR por XML de harness: clear dentro de packageSourceCredentials se interpreta como credencial incompleta. No requiere usuario/password ni cuenta. Intento02 elimina ese bloque; conserva packageSources/clear con único feed público y env mínimo, sin credenciales. Fuente/result01 preservados.


Intento02: restore ERROR ConfigurationDefaults/path1 nulo con env excesivamente reducido. Intento03 conserva variables Windows de directorios comunes y redirige APPDATA/LOCALAPPDATA al home .local del laboratorio; mismo único feed público y sin auth/global installation. No ampliar permisos ni cambiar TLS para reparar red; si bloqueo externo persiste, documentar sin repetirlo.


Intento03: restore PASS (warnings NuGet NU1903/1904), Common build TIMEOUT55s, no build PASS. Intento04 reutiliza restore03/compilación parcial, sólo build incremental con paralelismo1, mismo límite55s y sin nuevo feed. Último intento acotado para resolver viabilidad de compilación; timeout futuro se mantiene como pendiente y no origina nuevas repeticiones. Advisory applicability se evalúa por plataforma/reachability, no se etiqueta todo warning como exploit en Windows.

## Resultados finales QL0 y extensión QL1

Common build04 PASS (7.134s, incremental). [QL1 preregistrado](QL1_protocol.md) amplió el grafo a diez proyectos fuente del mismo pin: se retiró **una referencia a Algorithm.CSharp** del proyecto Engine para no compilar ejemplos. [Manifest](engine-source-manifest.json) conserva hash original Git, hash modificado y referencia retirada; hashes Git LF y checkout Windows pueden diferir por EOL. No se alteró lógica financiera fuente.

`engine-result-01.json`: restore PASS (9.186s), build PASS (47.811s), Engine DLL presente con SHA256 capturado. Es **compilación de componentes Engine con referencia de ejemplos retirada**, no distribución stock/Launcher ejecutado, estrategia, benchmark de rendimiento, prueba de fills/dividendos ni aceptación target. `full_engine_built=false` en captura expresa ese alcance restringido; no niega la DLL construida. No se descargó Data ni se ejecutó algoritmo. Warnings de dependencias quedan abiertos; compilar no acepta seguridad/licencias.
