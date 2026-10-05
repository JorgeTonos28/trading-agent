# R-020 — CandidateRuleCards del enfoque inspirado en el video

2026-10-05. **Research candidate, no Strategy V1 seleccionada**. No backtest/implementación. Fuentes narrativas y timestamps están en [reconstrucción del video](video_inspired_strategy.md); no volver a auditar cifras promocionales.

## VID-TS: módulo de gestión, todavía no estrategia autónoma

| Campo | Evidencia / OPEN |
|---|---|
| Fuente y propósito | Demo Tesla a 14:17–20:41: entrada market exógena, stop inicial, trailing tras subida, compras en caídas |
| Entrada/universo | **OPEN**: petición discrecional al LLM no es señal determinística. No inventar un filtro de entrada para aprobar candidato |
| Protección | Narración ofrece 10%/20% iniciales y luego 10%; trailing tras +10%, piso 5% y escalones +5% ambiguos. **Son cifras del video, no riesgo aprobado del proyecto** |
| Sizing / entradas adicionales | OPEN; agente sugiere tamaño, comprar caída ≥20% si efectivo. Falta referencia de caída, reservas, número de escalones, máximo exposición y estado orden |
| Ejecución | Broker/order types y semántica real OPEN; polling cinco minutos del ejemplo no selecciona cadencia PAPER |
| Failure | Quote stale/unknown positions/protección no confirmada → régimen determinístico aprobado de datos/riesgo/G1+G2, no recomendación LLM alternativa |
| Admisión actual | INCOMPLETE como estrategia; utilizable como **REFERENCE_ONLY** de mecanismos/casos pedagógicos y futura especificación de salida |

### Escenarios que las alternativas deben resolver antes del backtest

Precios hipotéticos, sin costes/ejecución real, ilustran ambigüedad; no nuevos umbrales seleccionados.

| Escenario | Contradicción o requisito exacto |
|---|---|
| Compra100 →110: floor105 narrativo | 5% bajo110 =104.5; floor105 equivale a distancia absoluta5. Alternativas porcentual/absoluta no son iguales. Definir fórmula/unidades y evitar redondear para ocultar diferencia |
| Escalón +5% desde110 | Base relativa110 produce115.5; incremento absoluto5 produce115. High-water continuo vs escalonado son mecanismos distintos; no seleccionar según curva favorable |
| Compra100, stop90 y caída80 | La condición adicional -20% ocurre después de cruzar stop. Hace falta estado/fills/reentrada/prioridad; no emitir compra y salida contradictorias ni asumir protección limita gap |
| Subida y pullback entre polls | OHLC no determina orden de trayectorias intrabar. No forzar actualización/fill de stop a secuencia más favorable; granularidad/formulación depende de datos/engine/broker |
| Stop pendiente/rechazado o fill parcial | No usar posición objetivo como posición reconciliada. Protección real/UNKNOWN gobierna incidente material, no activar ladder por chat |

Resolver estas reglas como variantes preregistradas de salida; entry-rule y selección de Strategy V1 permanecen gobierno posterior. Un baseline con entrada sintética solo compara mecanismo en escenarios, no demuestra alpha.

## VID-EXT: señales externas separadas

| Campo | Estado |
|---|---|
| Familia video | VID-CONG disclosures; video también menciona volumen/opciones. Extender investigación a fuentes ADR-005 sin tratar Smart Money como Congreso |
| Fuente y disponibilidad | Quiver/Unusual Whales/Capitol Trades/SEC y especializadas R-025; ninguna seleccionada |
| Señal | **OPEN** actor/transaction type/threshold/windows/decay. Selección del “mejor actor” usando resultados del mismo período contaminaría selección; no copiar esa parte |
| Tradable universe / sizing / exits | OPEN; disclosure/report no define automáticamente activo elegible, cantidad, rebalance o venta |
| Normalización | Eventos con source ID/revision/availability channel; transform determinístico. Reported position ≠ executed purchase observable; filing amended no sustituye pasado |
| Dependencias | PIT/licencia/historia + market prices/corporate actions + broker + risk. Output narrativo de research/shadow no produce TradeIntent |
| Failure | Input obligatorio ausente/stale/revisado necesita regla explícita determinística de elegibilidad/pausa; promoción ADR-005 y aprobación Champion |
| Admisión | INCOMPLETE; prioridad investigar disponibilidad histórica/PIT antes de scorecard de resultados |

Form4/13F son candidatos de **fuente**, no estrategias aprobadas ni señal positiva por defecto. [DatasetCard SEC](R-020_SEC_dataset_admissibility_RC0.md) abre ruta gratuita y registra el gap real de public-availability timestamp.

## VID-ALERT / VID-WHEEL / MATR

VID-ALERT: metodología de ingesta/parsing/reference útil; historia autorizada, receipt timestamps y reglas completas UNKNOWN, no entrar a backtest con supuestos. VID-WHEEL: DEFERRED fuera del alcance derivado PAPER V1. MATR: [ficha existente](../02_MATR_V1_spec.md) sigue benchmark/candidato con M-01–11; no desplaza primera investigación del video ni se selecciona por sencillez. Ningún scorecard de rendimiento abierto.
