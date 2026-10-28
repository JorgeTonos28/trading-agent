# QL5 — factibilidad de remediación aislada, protocolo previo

2026-10-28. Sigue al hallazgo real QL4, no es implementación de Trading OS ni aceptación de pin. Sin Algorithm/Engine.Run, mercados, cuentas, servicios, credenciales o cambios administrativos. Exportar fuente pública del commit ya verificado a **árbol nuevo ignored**; no alterar checkout/DLL/capturas previas. Extraer sólo archivos regulares/directorios de paths de código explícitos, sin Data, enlaces ni traversal de archive.

Transformaciones de investigación: referencia DotNetZip→ProDotNetZip1.19.0; sustituir únicamente el cuerpo de extracción manual overwrite del helper por overload estándar .NET con overwrite; conservar la omisión previa del proyecto de ejemplos Algorithm.CSharp; fijar por targets de laboratorio Drawing4.7.2, WinHttp4.5.4 y ServiceModel4.4.4 como mínimos patched de los advisories consultados. Registrar hashes/diffs, sin suprimir warnings.

Un build del host mínimo nativo y smoke de metadata; dos casos de archivo dentro de un nuevo laboratorio: traversal a sibling propio debe rechazarse, archivo seguro debe extraerse; roundtrip Ionic.Zip confirma una API concreta. No paths absolutos/UNC/dispositivo ni filesystem fuera de `.local/ql5-pin-remediation`. No probar archivos de terceros, datos licenciados o todos los vectores ZIP.

Contrastar grafo assets y avisos observados. Cero avisos conocidos no demuestra seguridad; compatibilidad fullengine, licencias/SBOM, ZIP bomb/links/encryption, configuración/egress y target quedan por aceptar. Máximo un intento; si restore/build falla, conservar ERROR y no fingir reemplazo viable. El resultado sólo decide si merece seguir esta ruta de ADAPT/reuse antes de construir librería propia o abandonar la familia.

## Resultado01 y protocolo de continuación previo

01:restore PASS12.584s; build ERROR/TIMEOUT60.396s; no smoke ni regresión ejecutados.0/0/0 son counts de filas vacías, no éxito. Original preservado.

Se abre un experimento de continuación separado, una única vez, para resolver la incertidumbre concreta de compilación: mismos archivos/export/transformaciones/paquetes/expectativas, sin nuevo restore; validar hashes contra01 y aumentar sólo presupuesto de build a120s. Ejecución por proceso con tool yielding, no espera bloqueante de120s. Si compila, ejecutar el smoke previsto; cualquier fallo se conserva. Captura02 conserva referencia/hashes del01 y no reemplaza su resultado. Este cambio de presupuesto no convierte un timeout en fallo de compatibilidad o cambia un criterio financiero/seguridad.

Resultado02: CONTINUATION_INCOMPLETE_OR_FAILED_NO_REMEDIATED_HOST_ACCEPTANCE. La continuación02 no completa una demostración de build+smoke. Conservar el ERROR/FAIL exacto de sus pasos/filas; la resolución de paquetes y QL4 no prueban compatibilidad reconstruida o parche aceptado. Capturas01/02 y hashes preservados; pin/producción no aceptados.
