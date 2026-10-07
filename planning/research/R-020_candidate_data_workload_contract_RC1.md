# R-020 — Demanda de candidatos, datos y validación — RC1

2026-10-07 · P0 D-008/D-011 y dependencias P1. Protocolo de investigación, no estrategia/código/backtest. Target Plus/personal para ejecutables/operación; estas especificaciones se completan Team sin espera.

## Matriz ex ante

| Candidato/pieza | Input mínimo / clocks | Reglas todavía OPEN | Engine/broker/failure requerido |
|---|---|---|---|
| VID-TS salida/ladder | Precio raw, posición/cash/órdenes reconciliadas, acciones corporativas y quote/bar availability | Entry/asset/sizing/base/ratchet/reentrada, precedencia stop/caída | Datos que resuelvan intrabar o regla conservadora explícita; gap/stop/protection/cancel-partial. No constituye estrategia completa |
| VID-EXT Congreso | Documento/actor/transacción reportada/rango/revision y publicación/delivery/source history | Universo/actor ex ante, cómo transformar evento a target, expiración y exits | Eventos PIT + equity execution/prices; mandatory input ausente/stale requiere regla explícita, sin completar por LLM |
| VID-EXT Form4 / 13F | Documento/códigos/ownership/amendments y clocks; separar trade-event de quarter holdings | Filtros semánticos y patrón/hipótesis económica, horizon/transform/exit | Normalizador reusable validado y disponibilidad por canal; no operación en fecha de transacción/periodo si aún desconocida |
| VID-EXT options/blocks/revisions/flows | Source especializado/recepción/PIT histórico/precio y contexto, derechos | Señal direccional no inferida de volumen, threshold/decay/instrument mapping | Research primero; V1 equities puede consumir datos de opciones sin operar derivados, solo si evidencia/gobierno posterior |
| VID-ALERT | Mensaje autorizado con receipt/history/revisión/cancelación y parser reproducible | Fuente/licencia/reglas/sizing/expiration | Sin acceso/historia/permission no backtest admitido; no solicitar credenciales aquí |
| MATR benchmark/candidato | Daily raw/as-of adjustments/corporate actions, calendario/warm-up/history propuesta 2005+ | M-01–11, salida/ATR/calendario/órdenes/pre-registro | Replay diario no basta para stops intrabar/gaps; broker próximo open y cash/dividend accounting, no resultado visto ni selección |

Esta tabla es demanda a verificar, no selecciona una combinación. VID-WHEEL fuera V1; no leverage/short/options ejecutados. Un Champion puede usar varias familias; admitir una exige demostrar el contexto disponible y fallo de cada dependencia. Jobs research/shadow/pedagogía no producen intents; dependency financiera agéntica nueva requiere gobierno y failure contract.

## Data contract para toda comparación

Por dataset: fuente/ruta/rights/período/universo as-of/delistings, clocks separados, precisión/zone, revisions/backfill, acciones corporativas conocibles, feed/cobertura/data latency. No completar histórico 2005 con series recientes o cambiar fechas por conveniencia de proveedor gratis. [Wave broker/data](R-007_008_provider_evidence_wave01_2026-10-07.md) documenta historia anunciada Alpaca desde2016 y feed/fill discrepantes; es gap del candidato de fuente, no permiso para cambiar protocolo. [Smart Money wave](R-025_provider_evidence_wave01_2026-10-07.md) y SEC DatasetCard registran PIT no resuelto.

Si no hay prueba de disponibilidad histórica exacta: mantener UNKNOWN, evaluar **variante conservadora declarada** por canal/horizon, sensibilidad de retrasos y confirmación prospectiva; nunca convertir acceptance/transaction-date a available_at sin evidencia ni etiquetar supuesto como PIT exacto. No usar mejores actores/resultados ex post para definir la señal.

## Protocolo de evaluación pendiente D-011

1. Completar y versionar CandidateRuleCard sin campos operativos ambiguos; cada variante diferente cuenta como ensayo. Registrar exposición previa a datos/resultados y costes.
2. Admitir datos/reglas/scope/ejecución/failure antes de rendimiento. Criterios/weights/benchmarks y thresholds preregistrados antes de abrir las muestras correspondientes; cuantías/calendarios todavía no aprobados.
3. Design/train/selection-validation separados de confirmation intacta; muestras usadas para elegir no confirman esa selección. Conservar períodos del roadmap como propuestas condicionales, no inventar OOS sellado ni sustituirlos silenciosamente.
4. Benchmark económico/cash/dividendos y escenarios de coste/fills alineados, provenance común y validación secundaria. Conservative fill assumptions versionadas, sin convertir paper simulation a prueba de ejecución real.
5. Replay determinístico y paridad del engine con fixtures antes de backtests de candidatos. R-009: comparar LEAN/Nautilus/otras bibliotecas con límites/licencias/Windows/deployment; no BUILD backtester por defecto. Fuera restricción AI OpenAI/Anthropic.
6. Riesgo: fórmulas/unidades/rounding/concurrent reservations D-035 primero; valores/escenarios numéricos/promotion PAPER D-031/032 después con gobierno. No usar thresholds del video/MATR como aprobación.

## Próxima secuencia financiera concreta

Tras scope de diseño agéntico: **fuentes/PIT + completion de reglas video primero**, comparar MATR; fichas broker restantes y data/backtest engines; cerrar fórmulas riesgo y workflow/storage con demanda. No escoger estrategia ni broker todavía. Decisión humana futura D-008 debe tener alternativas completas/evidencia/recomendación; ausencia de entry rule es trabajo de diseño propio atribuido al proyecto, no motivo para pedir al dueño que invente todas las reglas ahora. Propietario revisa arquitectura de estrategia final y luego autoriza selección.

Este paquete no obtuvo datasets de precios ni resultados de backtests de estrategias, ni abrió holdout, ni ejecutó benchmark de rentabilidad, ni implementó Trading OS. Al comprobar inception/referencia IWM, páginas públicas de emisores incluyeron retornos del ETF/benchmark: exposición incidental registrada en el preregistro, sin uso para seleccionar o modificar reglas. No se certifica intacta una muestra por esa ausencia de backtests. Preserva componente pedagógico: cada escenario explica diferencia de clocks/órdenes/contabilidad con fuentes y estados, sin promesa de retorno.
