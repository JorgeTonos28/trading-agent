# QL4 — superficie de archivos y alternativa reutilizable

Protocolo previo 2026-10-28, después de QL3. Sin Algorithm, Engine.Run, mercados, cuentas, credenciales, admin o configuración global. .NET/NuGet público scoped existente. No modificar fuente/DLL/capturas previas.

La revisión estática detectó `Compression.Unzip(overwrite=true)` que combina destino con nombre de entry sin containment explícito. Probar con un zip propio de una sola entrada `../sibling-canary.txt`, **únicamente bajo un árbol nuevo `.local/ql4-archive-boundary/lab`**. El sibling sólo puede caer en ese laboratorio: ningún path absoluto, UNC, dispositivo o target de usuario. Verificar paths resueltos antes de escribir. No datos sensibles ni filesystem policy/ACL. No probar payloads contra otro proceso/namespace. Conservar fixtures, sin eliminación recursiva.

Expectativas: observar si el helper nativo con overwrite escapa de la subcarpeta extract hacia su sibling ficticio; tal observación es un **FAIL de seguridad del helper**, aunque el check de comportamiento coincida. Contrastar el modo sin overwrite y el overload BCL moderno con overwrite contra el mismo caso, ambos dentro de su subárbol nuevo. No probar bombas de descompresión, links o todas las plataformas.

Build-vs-Reuse: investigar ProDotNetZip1.19.0, fork público MS-PL señalado como patched para GHSA-xhg6-9j5j-w4vf. Probar su API Ionic.Zip con roundtrip en memoria de texto propio; identidad de assembly distinta. Esto no acepta binario como drop-in ni reconstruye LEAN completo con reemplazo. Se conserva DotNetZip viejo transitivo para llamar al componente nativo; no se afirma limpieza del grafo por restaurar el fork.

Un intento con capturas/source hashes, timeout acotado; error preservado, no repetir para esconder discrepancia. Archivo inseguro sólo canary de laboratorio. Pin de LEAN y seguridad target siguen NOT_ACCEPTED. El experimento fundamenta remediación/adaptación, no despliegue o aceptación de riesgo residual.

Resultado01:6 observaciones esperadas, pero **helper nativo overwrite seguridadFAIL**. Canary sólo sibling del laboratorio. BCL y sin-overwrite rechazaron ese caso; API del fork en memoria funcionó. No S2/finanzas/seguridad global probadas. Auditoría41libraries/7pares/5advisories, no SBOM completo.
