# `TradeIntent` y ciclo de orden — contrato P0 RC0

**Estado:** D-013 `RESEARCHING`, 2026-10-01. Documento de diseño, sin implementación ni broker seleccionado. Baseline: [hoja §7, §32–33](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [PAPER V1 RC1](paper_v1_capability_contract_RC1.md). El canal `ShadowPortfolioProposal` queda fuera de este ciclo por ADR-001.

## 1. Identidades y propiedad

| Artefacto | Productor único | Campos mínimos y relación | Efecto |
|---|---|---|---|
| `Signal` | Champion Signal Engine determinístico | `signal_id`, Champion/version, instrumento, snapshot/cutoff, tiempo/vigencia, razones verificables | No es orden |
| `TradeIntent` | Intent assembler determinístico | `intent_id`, `signal_id`, account, estrategia/version, instrumento, lado, desired qty/notional, stop/exit policy ID, decision clock, snapshot ID, expiración, motivo, hash canónico | Solicitud al Risk Engine; no autoriza broker |
| `RiskDecision` | Deterministic Risk Engine | `risk_decision_id`, `intent_id` + hash, política/version, snapshot de cuenta/reservas, checks y razones, qty/notional máximo, vencimiento, `APPROVE/REDUCE/REJECT` | Única autorización financiera, si válida |
| `OrderCommand` | Execution Engine | `command_id`, `client_order_id` determinístico, `risk_decision_id`, broker/account, tipo/TIF/protección aprobados, qty ≤ autorizada | Única solicitud al broker |
| `BrokerEvent` | Broker adapter | IDs de broker/cliente, estado, fill qty/price, timestamp broker y recepción, secuencia si existe, raw hash | Evidencia, no fuente única de verdad |
| `ReconciliationRecord` | Reconciliation Engine | posición, cash, órdenes y fills internos vs broker; diferencias; snapshot/version y resolución | Habilita o bloquea nuevas entradas |

El `RiskDecision` no puede reutilizarse si cambia intent, cuenta, posición, reserva, Champion/política, data cutoff o expiración. La representación exacta de firma/hmac se decide en D-027; el contrato requiere vínculo verificable, no una tecnología concreta. `REJECT` y `REDUCE` dejan traza. `REDUCE` puede generar un `OrderCommand` solo con cantidad aprobada; no se vuelve a interpretar libremente la señal.

## 2. Idempotencia, estados y recovery

Clave de intención = account + Champion/version + señal/instante + instrumento + lado + propósito (`ENTRY`, `EXIT`, `PROTECT`, `REDUCE`), con identidad persistente y política para reintento. La clave concreta requiere prueba contra semántica del broker. `client_order_id` se asigna antes de enviar y persiste con el comando; un timeout **no** genera una clave nueva para la misma orden lógica.

Estados mínimos: `CREATED → RISK_APPROVED → SUBMITTING → SUBMITTED/UNKNOWN → ACCEPTED → PARTIALLY_FILLED/FILLED`, con ramas de `CANCEL_PENDING → CANCELLED`, `REJECTED`, `EXPIRED`. `UNKNOWN` obliga consulta de estado, no reenvío automático. Un evento duplicado no suma fill dos veces; eventos tardíos no revierten una transición terminal sin evidencia broker y reconciliación. Fills pueden ocurrir durante cancelación. Las posiciones se calculan por ejecuciones reconciliadas, no por simple estado `ACCEPTED`.

Si falla el proceso después de enviar y antes de guardar respuesta, el recoverer consulta broker por `client_order_id` y lista de órdenes/fills; reconcilia cuenta antes de autorizar nueva entrada. Si el broker no ofrece búsqueda/idempotencia suficiente, el candidato no cumple el gate sin un procedimiento alternativo probado. [IBKR documenta callbacks duplicados y que puede faltar un `orderStatus` para ejecuciones inmediatas](https://interactivebrokers.github.io/tws-api/order_submission.html); esto justifica integrar fills y reconciliación, sin seleccionar IBKR. La semántica se comprobará en cada broker candidato.

**Incidente G1+G2 (ADR-002):** un controlador determinístico bloquea nuevas entradas y solicita reconciliación. Execution solo puede emitir cancelación automática si la orden es una **entrada pendiente** con identidad, propósito y estado broker verificados. `CANCEL_PENDING` y acuse de solicitud no liberan reserva ni demuestran cancelación final; un fill concurrente se registra y reconcilia. No se cancelan órdenes protectoras por esta ruta. Ningún timeout habilita reducción/liquidación automática o reanudación de una pausa material.

## 3. Escenarios de aceptación a especificar

1. Dos señales simultáneas compiten por el mismo cash/risk budget: solo se autoriza exposición conjunta dentro de límite.
2. Autorización expira o cambia la posición entre Risk y Execution: no se envía orden con permiso viejo.
3. Broker acepta orden, stream se cae y DB no confirma: consulta por ID y conciliación; ninguna orden duplicada.
4. Fill parcial y cancelación concurrentes: cantidad final y reserva se ajustan al fill real.
5. Broker rechaza entrada o protección: estado explícito, alerta y respuesta conforme a política aprobada, nunca fingir protección.
6. `ShadowPortfolioProposal` se presenta en cualquier interfaz operacional: rechazo y evento de seguridad, ninguna conversión a `TradeIntent`.

**Pendientes para cierre D-013:** modelo formal de transiciones/eventos, política de reserva y expiración con D-012, semántica de cancel/replace/protective order por broker, clocks D-014, replay de fallos, consistencia y prueba de no duplicación. Build vs. Reuse evalúa SDKs/APIs oficiales de brokers, bibliotecas de validación y motores de workflow; ningún SDK de broker recibe autoridad propia de aprobar operaciones.
