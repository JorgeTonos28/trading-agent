# ADR-004 — Disponibilidad point-in-time y revisiones de datos

- **Fecha:** 2026-10-01.
- **Estado:** `DECIDED` por Plan Architect para contrato abstracto D-014; decisión técnica que desarrolla la hoja §2.5/§38 sin elegir proveedor ni estrategia.
- **Prioridad:** P0.
- **Contrato:** [datos PIT y linaje RC1](../05_data_contract_RC1.md).

## Problema

`event_at`, aceptación/publicación, disponibilidad en API y recepción por nuestro sistema son momentos diferentes. Un filing puede referirse a una transacción anterior; una serie de precio ajustada hoy puede incluir splits/dividendos todavía desconocidos en el instante histórico. Si se usan fechas económicas o revisiones actuales como disponibilidad histórica, el backtest incorpora información futura.

## Alternativas

| Alternativa | Ventaja | Problema |
|---|---|---|
| Usar `event_at`/`filed_date` como único reloj | Simple | Adelanta disclosure y pierde latencia del canal |
| Usar solo `received_at` propio | Fiel al sistema desde que opera | No existe para historia anterior; no permite comparar datasets históricos |
| Identificar clocks por canal/revisión y derivar `eligible_from` verificable | Separación PIT y replay reproducible | Exige evidencia, versiones y exclusión de datos incompletos |

## Evidencia y decisión

La [SEC explica que aceptación, fecha de filing y cambio son campos distintos](https://www.sec.gov/about/webmaster-frequently-asked-questions) y que no proporciona un timestamp del primer instante en que el contenido está disponible en sec.gov. Sus [APIs de submissions/XBRL se actualizan durante el día](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), pero ello no prueba cuándo lo recibió un proveedor concreto. [LEAN distingue modos de normalización que usan toda la historia futura frente a historia conocida hasta el tiempo del algoritmo](https://www.quantconnect.com/docs/v2/writing-algorithms/securities/asset-classes/us-equity/requesting-data). Son hechos de fuente primaria; la regla siguiente es inferencia de diseño del proyecto.

Se adopta un registro inmutable de observaciones/revisiones con fuente, canal, clocks, calidad, licencia y hash. `eligible_from` se deriva de evidencia de disponibilidad del **canal realmente usado**, validación y retraso conservador preregistrado. Un campo desconocido no se imputa con `event_at`. Replay temporal selecciona solo revisiones elegibles al `decision_at`; correcciones futuras no reescriben snapshots anteriores. Precio transable bruto y vista de indicadores ajustada as-of son conceptos separados. Champion y shadow se comparan sobre snapshots pareados; si no, la comparación se invalida.

## Consecuencias y seguimiento

D-014 queda `DECIDED` solo en el contrato abstracto. D-018/D-022/D-033 deben verificar disponibilidad PIT, calidad, licencia y frescura por familia/proveedor; D-023 verifica semántica del motor; D-026 define almacenamiento. Una fuente sin evidencia suficiente queda restringida a research/pedagogía o a un replay de menor resolución justificado; no se fuerza como señal operativa. Ningún proveedor, framework, MCP, ajuste específico o umbral de frescura fue seleccionado. `implementation_locked=true`.
