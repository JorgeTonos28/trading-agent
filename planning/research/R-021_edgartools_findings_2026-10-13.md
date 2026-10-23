# R-021 E1 — EdgarTools5.62.0, evidencia offline y disposición

2026-10-13 · data normalizer research E-SEC-01. [Protocolo/fuente/result](probes/r021-edgartools-offline/README.md), [dependencies/hashes](probes/r021-edgartools-offline/dependencies-01.json). Package base público pinado5.62.0,44 distribuciones con hashes de artefactos en workspace privado ignorado, Python3.14 existente. Sin AI/cloud extras, instalación global, cuenta/APIkey/contacto SEC, datos históricos ni backtest.

## Observaciones capturadas, no gate de dataset

- Siete fixtures sintéticos de tabla: P exchange/P privado, F fiscal, M derivado, precio faltante, documento4/A y dos owners. **7/7 PASS_STRUCTURAL** para las expectativas del autor; precio faltante queda null y códigos/cantidad/ref footnote se conservan. El caller selecciona `DerivativeTable/NonDerivativeTable`: no se probó detección automática de clase documental ni separación end-to-end.
- `market_trades` incluye la compra **privada** códigoP del fixture. Coincide con source que filtra P/S; nombre de propiedad no prueba exchange/execution/conviction. No REUSE_AS_IS como señal financiera.
- `form` es suministrado por el caller al extractor de tabla: ese check no demuestra parseo end-to-end de amendment. Los dos owners son conteo raw del fixture, **no prueba** de enrichment, dedup histórico/joint reporting o identidad. Una fila económica no equivale a decisión de cartera correcta.
- Factory completo `Ownership.from_xml` no queda demostrado offline: termina `IdentityNotSetError`, consistente con enriquecimiento de entity en source. No se inventó contacto ni stub para lograr PASS. Se registró un `socket.connect` denegado por hook Python; timing/propósito no capturados, no atribuirlo con certeza a factory/import ni afirmar cero intentos de red. No demuestra egress/process isolation Windows.
- Metadata de plan/discretion/footnote content/source availability y PIT no queda validada por esta ejecución; ningún timestamp público ni dataset real. Latest docs no reemplazan pin5.62.0.

## Recomendación técnica

**ADAPT / WRAP**, manteniendo SELECTED=NO. Preferir extracción estructural sin enrichment implícito y con origen/missing preservados; adjudicar semántica/códigos/mapping/planes en reglas determinísticas versionadas y as-of, no label `market_trades` o summary narrative. Evaluar un adapter o port acotado MIT frente a full factory con enriquecimiento explícito temporalmente autorizado. No construir parser general por defecto ni instalar MCP/workflow/Skills del paquete.

EXISTS=YES, AVAILABLE_TO_US=public-package/structural probe YES, SEC access/history CONDITIONAL; TECHNICALLY_COMPATIBLE=PARTIAL, ECONOMICALLY_REASONABLE=UNKNOWN maintenance/mapping/quality; SELECTED=NO. PAPER_V1_VIABLE_FREE=PARTIAL software, no dataset admitted; PAPER_V1_COST=license0+hardware/operación UNKNOWN; LIVE_COST=0source+scale/ops UNKNOWN; FREE_ALTERNATIVE=otras bibliotecas/source SEC a comparar; PAID_INCREMENTAL_VALUE=normalización/historia/canal fiable si demostrado; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto.44dependencies/pandas/arrow/frontend overhead por medir, no contabilizar license0 como coste total0.

## Alcance restante

Próximo probe debe preservar footnotes completas/IDs, is_plan trivaluado vs heurístico, entity mapping as-of/amendments, missing values, ownership y source channel receipts. No repetir E1 para ocultar límites; fuente/captura conservadas. Tests negativos de dataset y leakage/revisiones no pasados. This research package no produce señal/intent operativo, no recibe broker secrets y no reabre investigación agéntica.

Fuentes primarias: [repositorio](https://github.com/dgunning/edgartools), [MIT](https://raw.githubusercontent.com/dgunning/edgartools/main/LICENSE.txt), [PyPI pin](https://pypi.org/project/edgartools/5.62.0/), [Form4 docs](https://edgartools.readthedocs.io/en/latest/insider-filings/). Package source local hashes en metadata, fuente externa puede cambiar sin afectar captura pinada.
