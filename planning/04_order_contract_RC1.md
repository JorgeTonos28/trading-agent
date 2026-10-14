# `TradeIntent` y ciclo de orden — contrato P0 RC1

**Estado:** contrato abstracto D-013 `DECIDED` en [ADR-003](decisions/ADR-003-order-identity-and-recovery.md), 2026-10-01. No implementa órdenes ni selecciona broker/tipo de orden. Baseline: [hoja §7, §32–33](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [PAPER V1 RC1](paper_v1_capability_contract_RC1.md) y [ADR-002](decisions/ADR-002-paper-v1-incident-autonomy.md). El canal `ShadowPortfolioProposal` queda fuera de este ciclo por ADR-001.

## 1. Identidades y propiedad

| Artefacto | Productor único | Campos mínimos y relación | Efecto |
|---|---|---|---|
| `Signal` | Champion Signal Engine determinístico | `signal_id`, Champion/version, instrumento, snapshot/cutoff, tiempo/vigencia, razones verificables | No es orden |
| `TradeIntent` | Intent assembler determinístico | `intent_id`, `signal_id`, account, estrategia/version, instrumento, lado, desired qty/notional, stop/exit policy ID, decision clock, snapshot ID, expiración, motivo, hash canónico | Solicitud al Risk Engine; no autoriza broker |
| `RiskDecision` | Deterministic Risk Engine | `risk_decision_id`, `intent_id` + hash, política/version, snapshot de cuenta/reservas, checks y razones, qty/notional máximo, vencimiento, `APPROVE/REDUCE/REJECT` | Única autorización financiera, si válida |
| `OrderCommand` | Execution Engine | `command_id`, `order_key` interno persistente, `risk_decision_id`, broker/account, tipo/TIF/protección aprobados, qty ≤ autorizada | Única solicitud de alta/replace al broker |
| `IncidentActionAuthorization` | Risk Engine determinístico | incidente/versión, tipo `CANCEL_VERIFIED_PENDING_ENTRY`, orden destino, evidencia de identidad/estado, vencimiento, política ADR-002 | Única autorización para G2; nunca `REDUCE_EXPOSURE`/`CLOSE_ALL` |
| `CancelCommand` | Execution Engine | `command_id`, autorización G2, `order_key` y referencia broker verificadas, motivo, instante | Solicitud de cancelación; no demuestra cancelación final |
| `BrokerEvent` | Broker adapter | IDs de broker/cliente/ejecución si existen, estado, fill qty/price, timestamp broker y recepción, secuencia si existe, raw hash | Evidencia normalizada y original preservado |
| `ReconciliationRecord` | Reconciliation Engine | posición, cash, órdenes y fills internos vs broker; diferencias; snapshot/version y resolución | Habilita o bloquea nuevas entradas |

El `RiskDecision` no puede reutilizarse si cambia intent, cuenta, posición, reserva, Champion/política, data cutoff o expiración. La representación exacta de firma/HMAC se decide en D-027; el contrato requiere vínculo verificable, no una tecnología concreta. `REJECT` y reducción de **cantidad solicitada del mismo intent** dejan traza; esto no es G3. `REDUCE` puede generar un `OrderCommand` solo con cantidad aprobada; no se vuelve a interpretar libremente la señal. Un `IncidentActionAuthorization` no puede usarse como permiso de colocación o de reducción de posición.

## 2. Idempotencia, estados y recovery

La identidad **interna** de intención usa account + Champion/version + señal/instante + instrumento + lado + propósito (`ENTRY`, `EXIT`, `PROTECT`, `REDUCE`) y un `intent_id` persistido. Cada comando tiene `order_key` interno inmutable. El identificador aceptado por el broker puede ser client-assigned, secuencial, asignado por broker o una combinación; **no se presupone `client_order_id` universal**. El adaptador conserva mapa `order_key ↔ broker_client_id/broker_order_id/permanent_id`, según API. Un timeout **no** crea otra orden lógica ni permite reenviar hasta determinar estado. Si la API ofrece idempotencia por ID cliente, debe probarse; si no, la recuperación usa consulta de órdenes, ejecuciones y posición antes de decidir. Un nuevo intento tras rechazo terminal necesita nuevo comando y autorización vigente.

El ledger persiste el comando autorizado **antes** de transmitirlo. Si no puede persistirse o auditarse, no se inicia una nueva orden. Estado interno mínimo: `CREATED → RISK_APPROVED → SEND_PENDING → SUBMITTING → SUBMITTED/UNKNOWN → ACCEPTED → PARTIALLY_FILLED/FILLED`, con ramas `CANCEL_REQUESTED → CANCEL_PENDING → CANCELLED`, `REJECTED`, `EXPIRED` y `RECONCILIATION_REQUIRED`. Este grafo es conceptual: los eventos broker pueden faltar, repetirse o llegar fuera de orden; se preserva secuencia de hechos y se deriva estado de cuenta desde broker + ejecuciones reconciliadas. `UNKNOWN` no significa `REJECTED` ni habilita reenvío. `CANCEL_REQUESTED/PENDING` no significa `CANCELLED`. `CANCELLED` puede coexistir con cantidad ya llenada. Una corrección/bust de ejecución abre reconciliación y corrige ledger sin borrar el evento original.

Si falla el proceso después de enviar y antes de guardar respuesta, el recoverer consulta broker por **todos los identificadores disponibles**, lista de órdenes abiertas/cerradas, ejecuciones y posición; reconcilia cuenta antes de autorizar nueva entrada. Si no puede determinar si la orden fue aceptada, mantiene `UNKNOWN`, bloquea exposición nueva y escala. [Alpaca documenta ID cliente consultable](https://docs.alpaca.markets/us/reference/getorderbyclientorderid) y [stream de actualizaciones](https://docs.alpaca.markets/us/docs/websocket-streaming); [IBKR documenta IDs de orden propios, callbacks duplicados y posibles transiciones sin callback](https://interactivebrokers.github.io/tws-api/order_submission.html), así como [ID separado por ejecución parcial](https://ibkrcampus.com/docs/tws-api/ref/execution). Estos son **ejemplos de diferencias**, no selección de broker. El adaptador debe demostrar búsqueda y reconciliación suficientes con el candidato real.

**Incidente G1+G2 (ADR-002):** un controlador determinístico bloquea nuevas entradas y solicita reconciliación. Execution solo puede emitir cancelación automática si la orden es una **entrada pendiente** con identidad, propósito y estado broker verificados. `CANCEL_PENDING` y acuse de solicitud no liberan reserva ni demuestran cancelación final; un fill concurrente se registra y reconcilia. No se cancelan órdenes protectoras por esta ruta. Ningún timeout habilita reducción/liquidación automática o reanudación de una pausa material.

## 3. Invariantes y transiciones exigidas

| Invariante | Criterio observable |
|---|---|
| Solo órdenes autorizadas | Cada comando de alta/replace enlaza un `RiskDecision` válido para intent, cuenta, versión y estado; cada G2 cancel enlaza `IncidentActionAuthorization` verificable |
| Cantidad acotada | Suma de órdenes/fills/reservas de exposición nueva no supera la cantidad o riesgo aprobado; fill parcial no libera presupuesto prematuramente |
| No duplicación tras incertidumbre | Ante timeout/reinicio no hay segundo envío mientras el primer intento sea `UNKNOWN`; búsqueda y reconciliación preceden una nueva decisión |
| Eventos tolerantes a repetición | Mismo `execution_id`/evento no suma dos veces; corrección o bust se registra como hecho nuevo vinculado, no sobrescritura silenciosa |
| Protección separada | Orden de entrada, salida, stop y legs se identifican por propósito y relación padre/hijo; G2 no cancela stop/protección |
| Estado confirmado | `CANCELLED` exige confirmación broker o evidencia de ausencia y reconciliación suficiente; solicitud de cancelación no basta |
| Recuperación auditada | Se conserva comando, autorización, intento de envío, respuestas, eventos crudos, normalización y reconciliación con clocks/versiones |
| Shadow aislado | `ShadowPortfolioProposal` no satisface tipos/autorizaciones de `TradeIntent`, `RiskDecision` ni `IncidentActionAuthorization` |

La reserva de presupuesto se libera solo al conciliar fill/cancel/reject terminal y cantidad pendiente. ADR-006 fija el control compuesto; los detalles de fórmula/simultaneidad son D-035 y las garantías de almacenamiento/durabilidad son D-026. La interfaz del broker no se declara idempotente sin probe.

## 4. Escenarios de aceptación del contrato

1. Dos señales simultáneas compiten por el mismo cash/risk budget: solo se autoriza exposición conjunta dentro de límite.
2. Autorización expira o cambia la posición entre Risk y Execution: no se envía orden con permiso viejo.
3. Broker acepta orden, stream se cae y DB no confirma: consulta por ID y conciliación; ninguna orden duplicada.
4. Fill parcial y cancelación concurrentes: cantidad final y reserva se ajustan al fill real.
5. Broker rechaza entrada o protección: estado explícito, alerta y respuesta conforme a política aprobada, nunca fingir protección.
6. `ShadowPortfolioProposal` se presenta en cualquier interfaz operacional: rechazo y evento de seguridad, ninguna conversión a `TradeIntent`.
7. Cancelación G2 de entrada con fill concurrente: el fill se contabiliza una vez, el resto queda cancelado solo tras confirmación, y la protección permanece.
8. Corrección o bust posterior de un fill: ledger conserva ambos hechos y reabre reconciliación de posición/cash/riesgo.
9. Reincorporación tras reinicio con orden `UNKNOWN`: nuevas entradas bloqueadas hasta consultas de órdenes, ejecuciones y posición; ninguna reanudación automática tras pausa material.

## 5. Build vs. Reuse y gates dependientes

Las APIs/SDKs oficiales de brokers son candidatos a `WRAP`, no gateways de riesgo. [Alpaca Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca) muestra ID cliente y stream; [IBKR TWS API](https://interactivebrokers.github.io/tws-api/order_submission.html) usa `orderId` y eventos distintos. Ambas quedan `REFERENCE_ONLY` para este contrato hasta D-021; no se elige broker por facilidad de documentación. Frameworks de workflow, esquema/validación y ledger se comparan en D-020/025/026 antes de `BUILD`. Ninguna Skill, plugin, MCP ni LLM recibe endpoint genérico de orden.

**D-013 queda cerrado solo como contrato abstracto.** La selección de broker y mapeo de IDs/estados/tipos de orden se resuelve en D-021 (P1); arquitectura de reservas en D-012/ADR-006 y semántica de fórmulas en D-035 (P1); clocks en D-014 (P0); persistencia en D-026 (P1); probes de cancel/replace/stop, paper fills y failure recovery en D-030/031 (P2). Una dependencia que no cumpla estas garantías reabre D-013 por change record, no se omite silenciosamente.

## Gates temporales broker — wave04

[Timing sources](research/R-007_008_timing_evidence_2026-10-14.md) añaden auctiondeadline/OPGpermissions, GTCexpiry, gatewayauth/restart y presetversion. Misseddeadline no fillOpen ficticio; pendingcancel puede ejecutar/reservas conservadas. Expiry de señal no cancela protección ni concede G3. Pruebas target permanecen B1–5NOT_TESTED.

## Demanda PRICE–MATR wave05

[Pairing](research/R-020_PRICE_MATR_pairing_spec_RC0.md) propone sello de entry antes de ratchet agregado, con protección inmediata de parciales y p0/fills/qty/HWM reconciliados. Es mecanismo candidato a contrastar, no protección broker aceptada ni regla Champion aprobada; lote/seal y coste de retraso permanecen en Config/gates broker/engine. Stop deseado no confirmado, crossed/missing no riesgo cero; ADR015/G1+G2 intactos.

## Demanda de presets wave07

[Rules](research/R-020_PRICE_MATR_rule_configurations_RC0.md) explicita ATR_signal frozen/rawrebase/p0partialexfees/desiredmonotone, materialpauseantesdehealthyexit/replace/entry, expiryentrada separado deprotección, slots/cashreconciliado ytargetStrategyOPEN. Broker mapping yprotección efectiva requieren pruebas, no pasan porsemánticaJSON; G1G2/noG3/autoridadRoot intactos.
