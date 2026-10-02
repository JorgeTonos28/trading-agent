# R-008 — Market Data: marco de comparación y economía por fase

**Fecha:** 2026-10-02. **Estado:** `OPEN`, P1/D-022. Inicializa scorecard; no se investigaron precios ni se eligió proveedor en este hito. La selección debe satisfacer ADR-004 y las necesidades de candidatos Strategy V1, sin cambiar período/universo ni permitir look-ahead por conveniencia del plan gratuito.

Comparar cobertura histórica/activos/delistings/corporate actions, ajustes/revisiones as-of, timestamps/publicación, granularidad, streaming/backfill, latencia/availability, rate limits, licencia para automatización/backtest/almacenamiento, calidad cruzada y recuperación. Documentar diferencias entre feed paper y live; muestras oficiales cuando sea viable antes de selección.

## Scorecard económico inicial

PAPER: included/free/local-first con calidad suficiente. LIVE: valor económico, fiabilidad y latencia medidos frente a alternativas. Aplicar [ficha común ADR-008](../economic_scorecard.md): fijo/variable/mensual/escala, derechos exchange/non-display si aplican, backfill/add-ons y licencias, integración, lock-in, beneficio y condición para pagar. Investigar opciones pagas está autorizado; contratación/gasto requiere aprobación. Estos candidatos proceden del backlog; ninguna fila confirma oferta gratuita, producto o precio actual.

| Candidato | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Broker-native feeds | UNKNOWN broker/cuenta/feed | UNKNOWN | UNKNOWN | Feeds de otros brokers por probar | Paridad/reconciliación/cobertura/latencia a medir | YES si gasto |
| Databento | UNKNOWN | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Fidelidad/coverage/latencia a demostrar | YES si gasto |
| Massive | UNKNOWN | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Histórico/revisiones/streaming a demostrar | YES si gasto |
| Nasdaq Data Link | UNKNOWN dataset | UNKNOWN | UNKNOWN | Fuente pública del dataset si existe | Calidad/licencia/cobertura a demostrar | YES si gasto |
| Tiingo | UNKNOWN | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Ajustes/history/continuidad a demostrar | YES si gasto |
| Alpha Vantage | UNKNOWN límites/licencia | UNKNOWN | UNKNOWN | Feed incluido/público por universo | Límites/latencia/cobertura a demostrar | YES si gasto |

Todo candidato adicional completa estos campos y dimensiones funcionales antes de preselección. Precios/mensuales permanecen `UNKNOWN` hasta fuente/cotización fechada y escenario de carga; no inventar equivalencia de calidad entre planes gratis y pagos.
