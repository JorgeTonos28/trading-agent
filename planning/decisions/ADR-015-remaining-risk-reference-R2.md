# ADR-015 — referencia principal R2 para riesgo restante

**Fecha:** 2026-10-13. **Estado:** DECIDED / CONCEPTUAL_SCOPED_APPROVAL. **Aprobador:** propietario por instrucción directa. **Afecta:** Q-054 DECIDED, subdecisión de referencia D-035; D-035 global continúa RESEARCHING. Complementa ADR-006 opción B; no sustituye A+, G1+G2 ni ADR-014. `implementation_locked=true`.

## Decisión y condiciones del propietario

R2 es la referencia principal del riesgo restante desde el valor actual de la posición hasta **protección confirmada válida**. La aprobación conceptual no congela fórmula final, inputs, porcentajes, umbrales, escenarios, Strategy V1, broker/engine ni implementación.

1. Conservar R1 desde precio de entrada para atribución/análisis, junto con contabilidad de P&L realizado/no realizado y pérdidas acumuladas. Entry-to-stop es una estimación distinta, no reemplaza la pérdida efectivamente observada.
2. Mantener controles independientes de pérdidas, drawdown, exposición, liquidez, cash y gap/slippage; rige el mínimo restrictivo de ADR-006. R2 no garantiza pérdida máxima ni ejecución en stop.
3. Una reducción de R2 **no autoriza top-up ni promedio a la baja automático**. Toda ampliación exige señal válida, regla explícita Champion aprobada, nuevo TradeIntent/evaluación integral y reservas reconciliadas. La fórmula de capacidad no genera una señal ni orden.
4. Entradas nuevas/remainders siguen `p_auth` conservador de autorización y estimación de protección **condicional** documentada/probada; no usar marca favorable para reducir riesgo inicial ni etiquetar stop proyectado como confirmado.
5. Protección ausente/inválida/no confirmada o precio que cruzó stop sin ejecución verificada => incertidumbre y controles fail-closed; riesgo no evaluable nunca0. Posiciones/órdenes/fills/coverage se reconcilian; G2 sólo entradas pendientes verificadas, protección conservada y reanudación humana tras incidente material. No autorizar G3.
6. Costes/pérdidas/reservas no se duplican; preservar toda exposición real. Own-claim projection/replacement atómico no libera reserva globalmente ni compensa con venta pendiente; broker holds y ledger claims deben mapearse de forma verificable.
7. Evaluar ganancias/pérdidas, parciales, top-ups, gaps y movimientos adversos rápidos; protocolos/casos [R-027 RC1](../research/R-027_R2_scenarios_RC1.md), sin declarar pruebas operacionales pasadas.

## Aplicación al contrato de medición

Para cantidad reconciliada positiva, validar primero marca/protección/qty/timestamps/raw units/session. Solo después aplicar fórmula final R2 aprobada en futura Risk Policy. El caso clamp `max(mark-stop,0)` del dossier **no permite asignar0 a protección incierta o stop cruzado**. Usar estado `UNCERTAIN/NOT_EVALUABLE` y valor null, o bound conservador separado explícito, sin convertirlo en medida confirmada. Una posición flat reconciliada puede tener riesgo de posición0; remainders/reservas se contabilizan por separado, no desaparecen por estar flat.

## Dependencias y estado restante

Q-054 cerrado en referencia R2 y condiciones. D-035 mantiene fórmulas/unidades/precios/fees/rounding/scenarios/concurrent reservations, mapping broker y pruebas pendientes. D-031 números/calibración y D-030 protección/fills permanecen abiertos. CandidateConfig D-008 exige regla de ampliación propia, no hereda averaging-down del video. D-022 datos/marks/PIT, D-021 broker, D-023 engine y D-025/026 storage/workflow completan evidencia, sin aprobación automática.

[Dossier comparativo original](../research/D-035_risk_measurement_decision_RC0.md), [revisión independiente](../research/R-020_027_independent_review_2026-10-13.md) y algebra8/8 ficticio se preservan. La aprobación no convierte el probe en prueba de Risk Engine ni en permiso financiero. La capa agéntica fundamental continúa completa en scope ADR-014; target acceptance R-030 diferido, LIVE UNKNOWN. No gasto, administración/Plus, merge main ni release.
