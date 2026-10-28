# LEAN — realización local desde fuente RC3

2026-10-28. ADR-023 selecciona familia. **LOCAL_SOURCE_HOST_BUILD_DEMONSTRATED; pin/modelos/paridad/target NOT_ACCEPTED.** No implementación de Trading OS, backtest, cuenta, CLI, Cloud o gasto.

## Evidencia ejecutada y límite

[QL3](probes/r009-lean-local-source/README.md) verificó antes de compilar el commit f3d841e60dfd010ee5fc293ea893e56952484108. Compiló el `Launcher/Program.cs` original mediante un proyecto mínimo de laboratorio que referencia Engine/Messaging/Queues. Se conserva la modificación previa QL1: una referencia de ejemplos Algorithm.CSharp retirada del proyecto Engine. El launcher stock incluye otros proyectos de ejemplos, toolbox, downloader, research y optimizador; **no se declara compilación de toda la solución stock intacta**.

Restore15.121s, build39.962s y smoke de metadata0.561s:6 checks PASS de entrypoint/tipos/dependencias. No se invocó Main, Initializer, Engine.Run ni Algorithm. Los [hashes posteriores](probes/r009-lean-local-source/build-observation-after-run.json) distinguen observación de artefactos de la verificación previa de fuente. No es atestación del loader.

El resultado demuestra una ruta de compilación local sin dependencia del CLI/login comercial, no ejecución completa ni inexistencia universal de red. QL0/QL1/QL2 siguen siendo evidencia complementaria con su scope original. Fuente pública: [repositorio](https://github.com/QuantConnect/Lean), [arquitectura modular oficial](https://www.quantconnect.com/docs/v2/lean-engine/getting-started). Servicios, datos, CLI/Cloud y soporte tienen licencias/economía separadas; no se asumen gratuitos.

## Ruta de ejecución a aceptar después

1. Fresh clone del release autorizado, source/dependency manifest y pin revisado. Build reproducible del subconjunto necesario, con diferencias explícitas frente al upstream y SBOM/licencias.
2. Config de research local cerrada: backtesting=true por contrato, algoritmo propio admitido, directorios locales de datos/resultados, providers de disco y mapping/factor files admitidos. Rechazar archivo de config ausente, opciones desconocidas o una selección live/cloud; no aceptar fallback a defaults por un error de path.
3. `dotnet <host-compilado>.dll --config <config-verificada>` es forma candidata de launch, **no comando ejecutado en este laboratorio**. El config de upstream ofrece providers locales, pero el wrapper deberá comprobar la configuración efectiva tras overlays/argumentos. Las propiedades de disco no son una barrera de egress de todo el proceso.
4. Smoke sin estrategia y fixtures integradas antes de datos reales; después gates de import/contabilidad/fills/paridad. Nunca ejecutar el template upstream con sus datasets para demostrar rendimiento.
5. LEAN opera como motor de investigación/contabilidad simulada. Sus Risk/Portfolio/Brokerage nativos no sustituyen el Risk Engine del proyecto ni conceden autoridad de órdenes PAPER. Integración futura sólo por contratos autorizados.

Inspección estática pinada: Program usa Config/Initializer y obtiene handlers por configuración; DefaultDataProvider abre archivos; el config base nombra JobQueue/Messaging/local object/map/factor providers. `DailyPreciseEndTime` es true en AlgorithmSettings de este pin; fijarlo explícitamente y probar calendario/EndTime/cutoff. No transferir UTC/AlwaysOpen de QL2 a mercado real. Ninguna de esas lecturas prueba que todos los plugins sean offline o estén admitidos.

## Remediación y gates P1/P2

QL3 preserva advertencias DotNetZip, System.Drawing.Common, WinHttpHandler y ServiceModel. No declarar todo explotable en Windows ni todo inocuo por ser transitive: inventariar versión/advisory, plataforma, reachability y remediación/exclusión demostrada antes de aceptar un pin. No ignorar warnings para congelar el plan. QP1–QP10/modelos, librerías/clientes, packaging target y datos siguen abiertos; ejecución integrada de implementación sólo después de DoR.

Build-vs-Reuse: motor REUSE_AS_IS; host/config/import/modelos WRAP/ADAPT. PAPER_V1_VIABLE_FREE=CONDITIONAL, licencia motor0; integración/host/datos/operación totalUNKNOWN. LIVE_COSTUNKNOWN; FREE_ALTERNATIVE=Nautilus reserva; PAID_INCREMENTAL_VALUE=soporte/servicios sólo si material y medido; ECONOMIC_JUSTIFICATION_REQUIRED=YES. Cinco escalas obligatorias; no compra ni instalación global.

## Evidencia adicional antes de admisión del pin

[QL4/QL5 y remediación](R-009_current_pin_remediation_RC0.md): helper de extracción overwrite falla containment dentro del laboratorio propio. Requiere reparación/exclusión probada antes de pin; no rechazo automático de familia. Timeout01 preservado, continuación02 con código igual: CONTINUATION_INCOMPLETE_OR_FAILED_NO_REMEDIATED_HOST_ACCEPTANCE. No waiver ni aceptación global por actualizar paquetes.
