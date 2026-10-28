# LEAN — admisión del pin y remediación candidata RC0

2026-10-28. Familia aprobada ADR-023; **PIN_NOT_ACCEPTED**. Este trabajo adicional cierra incertidumbres concretas de source/dependencies que podían investigarse ahora, sin reabrir arquitectura AI o ejecutar estrategia.

## Hallazgo reproducido, no advertencia hipotética

[QL4](probes/r009-archive-boundary/README.md): `Compression.Unzip(overwrite=true)` escribió una canary fuera de la subcarpeta extract al sibling de su laboratorio propio. **FAIL_BOUNDARY_DEMONSTRATED** del helper. El modo sin overwrite y el overload estándar .NET con overwrite rechazaron ese caso. Seis checks de observación PASS no significan seguridad PASS. Nada salió del nuevo árbol `.local` ni se probaron recursos financieros, permisos OS, S2 u otro proceso.

El helper usa BCL para este path; **no atribuirlo automáticamente al advisory de DotNetZip**. Sustituir sólo el paquete DotNetZip no repara ese bucle manual. Propuesta: reutilizar el overload estándar .NET y revisar todos los import/extract paths y límites, en vez de construir un parser ZIP general. No producción modificada ni upstream contactado.

## Dependencias, fuente y Build-vs-Reuse

[Auditoría resuelta QL3](probes/r009-archive-boundary/dependency-audit-01.json):41 libraries, incluidos proyectos;7 pares paquete/advisory asociados a5 advisories únicos. No SBOM completo. System.Drawing4.7.0 aparece en el [advisory Mac/Linux](https://github.com/advisories/GHSA-rxg9-xrhp-64gj); no afirmar esa vulnerabilidad concreta en Windows ni seguridad de otras plataformas por ello. WinHttp/ServiceModel tienen rangos/versiones patched documentados, sin afirmar reachability global desde la severidad de NuGet.

El [advisory DotNetZip](https://github.com/advisories/GHSA-xhg6-9j5j-w4vf) no identifica versión patched del paquete original y señala ProDotNetZip1.19.0 como alternativa corregida para ese CVE. [Fuente pública ProDotNetZip](https://github.com/mihula/ProDotNetZip) mantiene namespace Ionic.Zip, assembly distinto y licencia MS-PL con notices derivados. QL4 ejecutó roundtrip en memoria de texto propio; no compatibilidad binaria drop-in o auditoría global. ADAPT candidato antes de BUILD librería propia; no seleccionado para producción.

Referencias adicionales: [WinHttp](https://github.com/advisories/GHSA-6xh7-4v2w-36q6), [ServiceModel1](https://github.com/advisories/GHSA-jc8g-xhw5-6x46), [ServiceModel2](https://github.com/advisories/GHSA-p9wx-v264-q34p). Min-version patched conocida no equivale a versión moderna soportada final.

## Experimento aislado de remediación

[QL5](probes/r009-pin-remediation/README.md) exportó código del pin a un árbol nuevo, sin Data ni cambios al checkout original. Sustituyó PackageReference por ProDotNetZip1.19.0, el bucle unsafe por overload BCL y fijó Drawing4.7.2/WinHttp4.5.4/ServiceModel4.4.4 como experimento. Conservó la omisión de referencia de ejemplos QL1. Hashes/diffs y targets se capturan; no suppress warnings.

**01:** restorePASS12.584s; buildERROR/TIMEOUT60.396s, sin smoke. Filas0/0/0 no son PASS. Assets del host resolvieron los cinco candidatos y no registraron NU190; eso no demuestra seguridad o compatibilidad. **02:** una única continuación, presupuesto build120s sin cambiar código/expectativas ni nuevo restore. Resultado: `CONTINUATION_INCOMPLETE_OR_FAILED_NO_REMEDIATED_HOST_ACCEPTANCE`. La continuación02 no completa una demostración de build+smoke. Conservar el ERROR/FAIL exacto de sus pasos/filas; la resolución de paquetes y QL4 no prueban compatibilidad reconstruida o parche aceptado.

Todos los resultados originales permanecen; no reescribir el timeout como buildPASS. Duraciones por paso y diagnósticos reales en capturas. La intervención aquí es investigación de fuente, no upgrade, patch o configuración del Trading OS.

## Criterio P1 antes de admitir un pin

Fijar commit+parches+grafo/deps+SDK+licencias/notices, source review y regresión de data readers/import/compresión; validación de archives/paths/tamaño/links/encoding, modelos/contabilidad y QP aplicables; config/egress y reproducibilidad en target. Resolver el helper inseguro o demostrar exclusión efectiva del path bajo contrato, sin una waiver silenciosa. Paquetes actualizados o cero avisos no pasan este gate. No aceptar riesgo residual material sin gobierno.

ProDotNetZip/BCL: EXISTS=YES; AVAILABLE_IN_RESEARCH=YES para los componentes probados; TARGET_HOST=UNKNOWN; TECHNICALLY_COMPATIBLE=CONDITIONAL; SELECTED=NO. PAPER_V1_VIABLE_FREE=CONDITIONAL; licencia componente0 en las cinco escalas, costes de host/integración/operación totalesUNKNOWN. LIVE_COSTUNKNOWN; FREE_ALTERNATIVE=BCL/SharpZipLib según función; PAID_INCREMENTAL_VALUE=soporte si materialmente justificado; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. Nada contratado.
