# Wave10 — evidencia ejecutada y límites de los probes financieros

2026-10-23. Datos ficticios propios y código público pinado; sin precios históricos, Strategy.run, BacktestEngine.run, API broker, cuenta, credencial, gasto, configuración global o administración. Los conteos tienen scopes diferentes y **no se suman como validación estadística/operacional**. Doce hipótesis declaradas, cero trials de estrategia.

| ID | Ejecución conservada | Hallazgo / límite |
|---|---|---|
| [QE2 matcher](probes/r009-matching-components/README.md) |01:0PASS/0FAIL/5ERROR por lifecycle de harness;02:7PASS/1FAIL/0ERROR;03 repetición mismos resultados y trazas económicas | Nativo Nautilus1.231.0, fictitious CASH/posición/quotes. Gap market95→90, stop-limit95/94 no-fill en90, recuperación posterior; OHLC idéntico permite paths con fill/no-fill. ConsumoL1 activado llenó6 frente size5 por continuación sintética más profunda. Flag no es cap estricto; no bug universal ni liquidez real probada |
| [QL0 source](probes/r009-lean-source/README.md) |01XML ERROR;02env/path ERROR;03restore PASS/build TIMEOUT55s;04 Common build PASS incremental7.134s | No instalación global/CLI/Cloud/Docker. Errores no requieren credenciales. Código pinado y hashes; no ocultar intentos fallidos |
| [QL1 Engine](probes/r009-lean-source/QL1_protocol.md) | Restore PASS9.186s, build PASS47.811s, DLL/hash presentes | Diez proyectos fuente, una referencia a ejemplos Algorithm.CSharp retirada según manifest. Componentes compilados, no distribución stock/Launcher/run/fidelidad. .NET10.0.302 existente; fuente no contiene Data descargada |
| [R3 recursos](probes/r027-resource-semantics/README.md) |21PASS/0FAIL/0ERROR y66estados enumerados | Decimal, separaciónf/l/r y encumbrances, stale-cash/cancel/fees/gaps/split y contraejemplo solver no monótono. Algunos checks construyen estados; no prueban state validator, transacciones o solver productivo |
| [CA-S1 clocks](probes/r008-pit-reconstruction/README.md) |01 ERROR_CAPTURE/partial preservado;02 doce fixturesPASS | Revisión/as-of/replay observado versus reconstrucción/cancel/rango; pago sólo identidad NAV, transición/idempotenciaNOT_TESTED. Ningún vendor/dataset/PIT real aceptado; CA07/09 y DST pendientes |
| [E8 DD](probes/r020-dd-identification/README.md) |8checks marcadosPASS; siete verificaciones matemáticas y un sentinel declarativo | Misma esperanza−0.001, frecuencia de deterioro90% versus10%. Bound ilustrativo válido bajo sus supuestos IID/paths, no calibración, validación de independencia o aceptación DD-E |

## Hallazgos de código que afectan selección

LEAN `SecurityPortfolioManager.ApplyDividend` del pin capturado acredita cash en backtest Raw/SplitAdjusted sin modelo completo de pay-date. Requiere ADAPT para receivable/ex-date/pay-date y prueba de no doble crédito. `Raw` no resuelve ese gap por sí solo. [Recomendación de motor](R-009_engine_recommendation_RC1.md) es condicionada; QE2 y QL1 no son pruebas de igual alcance ni score competitivo.

NuGet emitió NU1903/NU1904: DotNetZip1.16 requiere remediación/análisis de extracción no confiable; System.Drawing.Common4.7 advisory específico afecta macOS/Linux, no demuestra exploit Windows. Compilación no acepta vulnerabilidades, licencias o seguridad del conjunto. [Manifest de dependencias](probes/r009-lean-source/dependency-provenance.json) conserva versiones/SHA512 y hashes de DLL; no es SBOM legal completo ni security audit. Archivos descargados/build/caches se mantienen sólo en ignored .local; sin datos/secretos.

## Reproducibilidad y cierre

Capturas y fuentes preservadas con .gitattributes raw; no cambiar expectativas para borrarFAIL. Corregir harness produce intento nuevo y motivo. Revisión independiente pidió reparar exclusividad de Risk y ciclo F0; [acta](R-020_financial_independent_review_2026-10-23.md). QA verifica conteos/hashes/trazas, invariantes/links y ausencia de promoción de datos/estrategia. No vuelve a ejecutar probes para aumentar conteos.

[QA del checkpoint](financial_checkpoint_QA_2026-10-23.json):50 comprobaciones de artefactos/hashes/invariantes/links PASS; no tests de runtime ni validación estadística. Preservados bytes de configuraciones RC1 y las12declaraciones,0trials,4+6cards no admitidas y main/originmain sin cambios.

No se ejecutó carga operacional Plus, seguridad target, broker actual o motor integrado. D011/D035 globales siguen RESEARCHING, F0 incompleto, holdoutUNKNOWN, implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED. Los ocho archivos H7 permanecen como residue documentado, sin intentos de limpieza.
