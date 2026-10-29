# ADR-006 — Controles compuestos de riesgo para PAPER V1

- **Fecha:** 2026-10-01.
- **Estado:** `DECIDED`, aprobado explícitamente por el propietario para D-012 (arquitectura conceptual).
- **Prioridad:** P0. **Implementación:** bloqueada.
- **Antecedentes:** [paquete comparativo D-012 RC0](../research/D-012_risk_budget_architecture_decision_RC0.md), [política de riesgo RC1](../03_risk_policy_RC1.md), [ADR-002](ADR-002-paper-v1-incident-autonomy.md), [ADR-003](ADR-003-order-identity-and-recovery.md).

## Decisión

Se adopta la **opción B** del paquete D-012. Para una entrada PAPER V1, el Risk Engine determinístico aplicará controles independientes y limitará la cantidad autorizada al mínimo de todas las restricciones aplicables: exposición y cash/buying power; pérdida **estimada** hasta protección/stop; escenarios de gap y slippage; liquidez; y exposición ya comprometida por posiciones, órdenes vivas y reservas concurrentes. Una restricción obligatoria que no pueda evaluarse con datos y estado confiables bloquea nueva exposición. El motor puede reducir o rechazar un `TradeIntent`, nunca aumentar su cantidad. La reserva debe evitar que intents concurrentes consuman el mismo presupuesto.

La distancia al stop es una estimación condicionada, no una pérdida máxima garantizada. El estado de cuenta y las autorizaciones se vinculan por versiones y se reconcilian conforme a ADR-003. Ante incidentes rige exclusivamente G1+G2 de ADR-002.

## Alcance excluido

Esta aprobación **no** fija porcentajes, umbrales, escenarios numéricos, calibración, fórmula final de cada control, referencia exacta de equity, tecnología, broker, proveedor de datos ni Strategy V1. Tampoco autoriza construir el Risk Engine, G3, reducción/liquidación automática general o reanudación automática tras una pausa material. Los parámetros y pruebas PAPER permanecen en D-031/R-015; los detalles de datos, protección, órdenes y reservas se precisan con D-021/026/030 y la estrategia aprobada D-008. Cualquier ampliación de política o autonomía requiere gobierno humano.

## Consecuencias y evidencia pendiente

El diseño y los backtests deberán medir por separado stop-risk estimado y escenarios adversos, y registrar qué restricción fue vinculante en cada decisión. La arquitectura debe fallar cerrado ante dato stale, posición incierta, concurrencia o protección inválida. Antes de implementación se documentarán semánticas, fórmulas y pruebas de reservas/estado; antes de PAPER autónomo se aprobarán parámetros y escenarios calibrados. La evaluación Build-vs-Reuse de evaluadores de reglas, bibliotecas y broker APIs sigue abierta en R-006/D-020. `implementation_locked=true`.
