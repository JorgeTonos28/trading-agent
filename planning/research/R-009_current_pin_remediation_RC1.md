# LEAN — reparación de source y gates del pin RC1

2026-10-29. Sustituye el estado de factibilidad inconclusa de [RC0](R-009_current_pin_remediation_RC0.md), conservando todos sus timeouts y fallos. **TWO_PATH_REPAIR_FEASIBILITY_DEMONSTRATED / PIN_NOT_ACCEPTED**. No implementación de Trading OS, estrategia, backtest o aceptación target.

## Resultado real y correcciones

| Experimento | Observación | Interpretación limitada |
|---|---|---|
| QL5/01–02 anteriores | Dos buildTIMEOUT, sin smoke | Preservados; no prueba de incompatibilidad |
| [QL6](probes/r009-remediation-diagnostics/README.md) | Nuevo host con obj separados, restore7.573s/build133.473s/run1.311s;8checks | Compila source con fork/min-patches, sin ejecutar Main. No prueba que packaging causó timeout. Segundo helper UnzipToFolder todavía FAIL_BOUNDARY_DEMONSTRATED |
| [QL7](probes/r009-extraction-repair/README.md) |01restoreERROR;02componente8PASS/1FAIL;03mismo parche9PASS después de corregir fixture de slash esperado | Error del harness por perfil mínimo y falso negativo lexical conservados. BCL rechaza traversal en3rutas; prueba absoluta no cubría shape relativo |
| [QL8](probes/r009-contract-preserving-host/README.md) |01buildERROR por omitir código Common/Data;02 repone1171.cs, build110.57s/run1.178s,14PASS | Integración en host mínimo de ambos fixes + fork y retorno relativo legacy. No stocksolution completa, Engine.Run, Algorithm, broker o datos |

El primer fallo era Unzip overwrite con bucle BCL manual; no confundirlo con CVE DotNetZip. El segundo UnzipToFolder repetía Path.Combine sin containment y era llamado desde Api.Download. Ambos se contrastaron con canaries fuera de extract pero siempre dentro del nuevo laboratorio propio. No recursos OS/financieros ni archivos ajenos. La causa de QL8/01 fue filtro demasiado amplio del harness, no el código de mercado: Data raíz de datasets y namespace Common/Data no son equivalentes.

## Reparación reutilizable candidata y contrato

Unzip usa overload BCL ExtractToDirectory con flag overwrite. UnzipToFolder usa ZipArchive.ExtractToDirectory y sólo tras éxito arma la lista legacy Path.Combine(outFolder,entry.FullName); conserva paths relativos cuando input lo era. QL7 devolvía absolutos y se **descarta ese detalle del parche** a favor de QL8. No parser propio, no producción parcheada. SharpZipLib/fork todavía se usan para otras APIs: BCL no sustituye mágicamente todo su surface.

Candidato hereda export de commit f3d841e60dfd010ee5fc293ea893e56952484108, omisión explícita de proyecto de ejemplos Algorithm.CSharp y mínimos patched de experimento ProDotNetZip1.19/Drawing4.7.2/WinHttp4.5.4/ServiceModel4.4.4. No se asumen versiones modernas soportadas definitivas ni seguridad por assets sin avisos. Sigue warningNETSDK1206/win7 y warnings de API/documentación, no ocultados. [Manifest candidato](LEAN_source_repair_candidate_manifest_RC0.json) enlaza source/patches/dep/capturas y hashes; no release de despliegue.

QL8 cuenta nueve casos ZIP, dos shape/content relativos, dos metadata launcher/engine y un roundtrip del fork.14PASS no son14gates de seguridad ni QP. Corregir fixture no borra FAIL02. Retornar error no hace extracción transaccional: un ZIP mixto podría dejar archivos previos al fallo; staging completo queda no admitido. El consumidor sólo usa artefactos sellados tras validación íntegra.

## Gates acotados que faltan antes de admitir pin

1. Aplicar exactamente patches revisados sobre fuente verificada; no volver a usar upstream original para extraer archivos arbitrarios. Code/dependency/license/SBOM review y decisiones de plataforma/reachability, no waiver por cero avisos. Auditoría resuelta no es auditoría completa del proceso.
2. Contrato de import: formatos permitidos, límites de tamaño/entradas/ratio, nombres/encoding/duplicados, destino staging nuevo, no links/reparse/paths compartidos, identidad del escritor y posterior seal. BCL traversal no demuestra defensa ante ZIPbomb, links o mutación concurrente. No afirmar barrera OS por validar path.
3. Revisar todos los callers utilizados y semántica de retorno; APIs/tar/downloader no necesarios quedan excluidos por config/allowlist verificable, no por comentario. Paridad/modelos/readers/actions/dividendos/costes/fills QP1–QP10 antes de uso correspondiente.
4. Pin final SDK/deps/config/host/versiones y build reproducible; target personal/Plus valida source/auth/aislamiento/config/runtime. Los aspectos host-specific no reabren diseño ni pasan por evidencia Team.

Este paquete cierra factibilidad técnica de la reparación candidata y shape ensayado; no declara PIN_ACCEPTED. No seguir extendiendo una campaña genérica de compresión: ejecutar después sólo los casos de import/deps/callers exigidos por el pipeline seleccionado. Nautilus sigue reserva, no cambio de familia ni petición de gasto.

Disposición ADAPT/WRAP del host/import y REUSE del motor; ProDotNetZip/BCL ADAPT candidato. EXISTS=YES; investigación=YES para probado; target=UNKNOWN; TECHNICALLY_COMPATIBLE=CONDITIONAL_SCOPE_DEMONSTRATED; SELECTED_FOR_PRODUCTION=NO. AdquisiciónOSS0; integración/hardware/backup/operación/mensual totalUNKNOWN, cinco capitales, LIVE reevalúa valor, FREE_ALTERNATIVE=BCL/SharpZipLib según función o Nautilusfamiliareserva; PAID_INCREMENTAL_VALUE=soporte si beneficio material; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto.
