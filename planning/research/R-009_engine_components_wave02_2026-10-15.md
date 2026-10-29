# R009 — evidencia de componentes y brechas de paridad

2026-10-15. D023 RESEARCHING, **engine no seleccionado**. Ningún backtest/estrategia/market data consultado ni broker conectado. [QE0](probes/r009-nautilus-artifact/README.md) acota pruebas reales, errores, fuentes/pins y dependencias; no QP1–10 PASS.

## Nautilus: evidencia práctica y límites

[PyPI1.231.0](https://pypi.org/project/nautilus-trader/1.231.0/) y [release](https://github.com/nautechsystems/nautilus_trader/releases/tag/v1.231.0) fijan wheel Windows CPython3.14, publicado02-08-2026, fuente27a8e54e7ac3c57d6cbf8891f0283dfbaee97317. La versión no prerelease de1.x tiene release titulada **Beta**; no confundir con aceptación productiva. [Docs latest](https://nautilustrader.io/docs/latest/getting_started/installation/) son2.x y advierten incompatibilidad de APIs con1.x. No aplicar garantía high-precision/feature2.x a este wheel1.x.

| Intento real | PASS | FAIL | ERROR | Alcance |
|---|---:|---:|---:|---|
| QE0-01 |2|0|2|SHA/import core1.231; componentes y engineimport faltanpytz |
| QE0-02 |4|0|1|Equity ficticio tick.01/whole units y rechazo de.5; importengine faltapyarrow |
| QE0-03 |6|0|0|Añadidas dependencias concretas; import y constructor/dispose vacío, sin datos, estrategias, órdenes o run() |

Cada fuente/salida original tiene hash; no se sobrescribió intento para borrar errores. No sumar fases repetidas como12pruebas independientes ni extrapolar6/6 a paridad. Guard Python/env reducido **no** aislamiento de proceso/red nativo. Nueve wheels instalados sólo bajo `.local`, dependencias numéricas previas reutilizadas; ningún registro/config global/servicio/cuenta/secreto. click requerido por distribución no pudo descargarse: no entorno completo de dependencias aceptado por importar motor. Manifiesto conserva resets/fetcherrors y corrección del nombre de un wheel; wheelhash coincide con PyPI, sin afirmar verificación independiente Sigstore.

El modelo Equity probado rechaza cantidad fraccionaria. QE1-ROUND-01 añadió5checks específicos: el default make_qty puede1.6→2, mientras round_down→1 y .5 rechaza0; el futuro adapter debe floor/validlot para no exceder autorización Risk. No aceptaQP6 ni adapter por este componente. Esto restringe esa ruta1.x; **no** demuestra que el broker no soporte fractions. EQ3 propone whole units y benchmark contable debe distinguir ideal fraccionario de cartera factible. No reinterpretar lot/tick como precision abstracta de dinero ni forzar datos para pasar.

## LEAN: brechas concretas de accounting/as-of

[Normalization](https://www.quantconnect.com/docs/v2/writing-algorithms/securities/asset-classes/us-equity/requesting-data) distingueRaw, ajustes históricos globales yScaledRaw al tiempo del algoritmo. [Corporate actions](https://www.quantconnect.com/docs/v2/writing-algorithms/securities/asset-classes/us-equity/corporate-actions) documenta manejo de posiciones/órdenes y eventos; no prueba nuestro receivable/pay-date ni first-delivery/PIT. El [source engine](https://github.com/QuantConnect/Lean) continúa candidatoOSS separado deCLI/Cloud comercial.

No declarar todo ajuste global look-ahead por definición: algunas señales dimensionless son invariantes a escala común. Se necesita demostrar invariancia/unidades **para cada uso**; stops, raw sizing, ticks/cash/acciones/revisiones no heredan ese argumento. Preferencia candidata Raw + transformación as-of y ledger explícito. Si el engine acredita cash en fecha distinta al pay-date del book, requiere modelo/adaptación y prueba de doble crédito; una notificación de dividendo no acepta cash disponible.

Host research tiene dotnet10.0.302, pero no build/enginepin/deps/ejecuciónLEAN validados. No instalarCLI/Docker/WSL/servicios ni sustituir por build propio general. Una diferencia de feature es requisito de adaptación, no motivo para ampliar autoridad o cambiar benchmark silenciosamente.

## Matriz siguiente y economía

| Requisito común | LEAN raw | Nautilus1.231 | Gate |
|---|---|---|---|
| Build/import/componentes | DOCS_ONLY, buildNO | Captura QE0, parcial | Pin/build reproducible y full dependencies |
| Raw/actions/as-of/receivable/pay-date | Adaptación a probar | Modelo/adaptación a verificar, no native support asumido | QP2/7/8 |
| Stop/gap/OHLC/partial/linked cancel | Modelos/ruta a mapear | Sin simulación ejecutada en esta wave | QP1/3/4/5 + B3 |
| Cash/fees/whole/fraction/rounding | No probado | Sólo Equity qty/tick probado | QP6, benchmark book y parity |
| Audit/replay/Shadow exports | No probado | No probado | QP9 |
| Repeatability/carga target | No probado | No probado | QP10, target distinto de research |

Disposiciones siguen **REUSE_AS_IS engine + WRAP/ADAPT** de contratos candidatos; selecciónNO, compatibilidadCONDITIONAL, disponibilidad fuenteYES/build-hostparcial/targetUNKNOWN. PAPER_V1_VIABLE_FREE=CONDITIONAL engine+data+ops; PAPER_V1_COST engine0, coste local/deps/QA UNKNOWN. LIVE_COST operación/data/escala UNKNOWN. FREE_ALTERNATIVE el otro engineOSS por probar. PAID_INCREMENTAL_VALUE hosting/support/setup sólo si mejora medible. ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. Lock-in deeventos/catalog/models/ledger con salida por trazas versionadas. Ningún gasto nuevo ni motivo para BUILD simulator general demostrado.

QP sintéticos y comparación técnica aún pueden avanzar en Team; backtests de estrategias/carga/aceptación operacional pertenecen al target personal/Plus. No ocultar QP pendientes como exclusivos de entitlement; no repetir discovery agéntica.
