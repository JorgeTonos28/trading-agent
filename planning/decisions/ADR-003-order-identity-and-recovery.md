# ADR-003 — Identidad y recuperación de órdenes independientes del broker

- **Fecha:** 2026-10-01.
- **Estado:** `DECIDED` por Plan Architect para contrato abstracto D-013; decisión técnica dentro de D-002, ADR-001 y ADR-002, sin ampliar autoridad financiera.
- **Prioridad:** P0.
- **Contrato:** [TradeIntent y ciclo de orden RC1](../04_order_contract_RC1.md).

## Problema

El baseline exige `client_order_id`, estados e idempotencia, pero cada broker puede exponer identidades, callbacks y semánticas distintas. Un timeout después de enviar puede dejar una orden aceptada sin confirmación local. Reenviar a ciegas crea exposición duplicada; tratar `cancel requested` como `cancelled` puede ocultar un fill.

## Alternativas consideradas

| Alternativa | Ventaja | Problema |
|---|---|---|
| Usar `client_order_id` y estado broker como modelo interno universal | Menos traducción | No todos los brokers usan el mismo ID ni emiten los mismos eventos; el estado puede ser incompleto |
| Identidad/event ledger interno + adaptador broker | Contrato estable, replay y reconciliación explícita | Requiere mapeo y persistencia duradera |
| Reintentar tras timeout con ID nuevo y corregir luego | Puede recuperar liveness | Puede duplicar orden y riesgo; inadmisible |

## Evidencia y decisión

[Alpaca documenta búsqueda por ID cliente](https://docs.alpaca.markets/us/reference/getorderbyclientorderid), [órdenes con identificador de cliente y updates](https://docs.alpaca.markets/us/docs/orders-at-alpaca). [IBKR documenta `orderId` secuencial, callbacks duplicados y transiciones sin callback](https://interactivebrokers.github.io/tws-api/order_submission.html); su [referencia de ejecuciones](https://ibkrcampus.com/docs/tws-api/ref/execution) distingue `execId` por fill parcial. **Inferencia del proyecto:** un único campo broker no basta como identidad y fuente completa de estado para cualquier candidato.

Se adopta identidad interna `intent_id → order_key/command_id → broker IDs`, comando autorizado persistido antes de envío, eventos crudos + normalizados inmutables, deduplicación de ejecuciones y reconciliación de órdenes/fills/posición. Un timeout produce `UNKNOWN` y bloquea reenvío/nueva exposición hasta averiguar estado. La autorización de un alta/replace procede del Risk Engine sobre un `TradeIntent` concreto. La cancelación G2 usa `IncidentActionAuthorization` determinística del Risk Engine vinculada a una entrada pendiente identificada/verificada; no se convierte en permiso de orden ni en G3. La protección broker-side es entidad distinta y G2 la conserva.

## Límites y seguimiento

No se selecciona Alpaca, IBKR, SDK, base de datos, workflow ni tipo de orden. D-021 exige verificar identidad/consulta/eventos del broker candidato; D-030/031 prueba paper/recovery. D-012 define reservas y política de riesgo, D-014 clocks, D-026 persistencia. La implementación permanece bloqueada. Si un broker no puede satisfacer el contrato mediante adaptación y pruebas, se descarta o se propone cambio formal; no se debilita el contrato de manera implícita.
