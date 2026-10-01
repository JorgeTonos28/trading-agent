# Política de riesgo PAPER V1 — contrato P0 RC1

**Estado:** D-017 `DECIDED` en [ADR-002](decisions/ADR-002-paper-v1-incident-autonomy.md): G1+G2 para PAPER V1; D-012 `RESEARCHING` para reglas y umbrales. **Fecha:** 2026-10-01. `implementation_locked=true`. Baseline: [hoja §7, §11–12, §32–33 y §54](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [ADR-001](decisions/ADR-001-paper-v1-authority.md).

## 1. Hechos, hipótesis y decisiones reservadas

El baseline exige `TradeIntent → Deterministic Risk Engine → Execution Engine → Broker`, long-only PAPER, sin aprobación humana por operación Champion aprobada. §11.3 propone 25% por posición, 0.50% riesgo estimado por posición, 2% agregado y límites de pérdida/drawdown **como parámetros iniciales de ingeniería**, no como política ya validada. §11.4 lista acciones de kill switch y advierte que `CLOSE_ALL` no debe ser reacción automática a todo fallo. El propietario aprobó A+ para el Portfolio Manager shadow, sin cambiar esos límites ni escoger umbrales.

**Hecho externo relevante:** un stop activado puede ejecutar lejos del precio stop en volatilidad; un stop-limit puede no ejecutar. No se debe presentar `distancia al stop × cantidad` como pérdida máxima garantizada. [FINRA, Stop Orders: Factors to Consider During Volatile Markets, 2025](https://www.finra.org/investors/insights/stop-orders-factors-consider-during-volatile-markets); [Investor.gov, Executing an Order](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/executing-order).

## 2. Reglas de diseño propuestas, aún sin política cuantitativa aprobada

1. **Precedencia:** integridad de cuenta/reconciliación y estado de suspensión; habilitación de Champion/instrumento; frescura/calidad PIT; límites de cuenta/cartera; límites de estrategia/posición; protección de ejecución. Un fallo o `UNKNOWN` en un control necesario deniega **nueva exposición**. Una salida ordinaria de un Champion aprobado sigue su propio `TradeIntent → Risk → Execution`; esto no autoriza reducción automática general por incidente.
2. **Estado que se cuenta:** posición reconciliada + órdenes vivas + reservas de intents aprobados y no finalizados. El presupuesto se reserva de forma atómica antes de emitir autorización; expiración, rechazo y fill parcial liberan o ajustan reserva solo después de evento/reconciliación verificable. Dos intents simultáneos no pueden consumir el mismo presupuesto.
3. **Autorización acotada:** `RiskDecision` incluye hash exacto del intent, política y estrategia versionadas, estado de cuenta usado, límite aprobado, validez temporal y checks con motivo. Cambiar snapshot, cantidad, posición o versión invalida la autorización. Execution revalida estado y no amplía el notional aprobado.
4. **Riesgo ex ante y realizado separados:** conservar cálculo de exposición, concentración, pérdida realizada/no realizada y estrés por gap; documentar precio de referencia, spread, liquidez y origen. El tamaño deseado se reduce o rechaza según política; nunca se aumenta para llenar presupuesto.
5. **Protección y fallos:** un stop broker-side, bracket u OCO es candidato sujeto a soporte y semántica del broker; no sustituye supervisión, reconciliación ni escenario de gap. G2 conserva órdenes protectoras; su cancelación/reemplazo necesita regla específica documentada, probada y aprobada.
6. **Reanudación:** tras pausa material no se vuelve a `NORMAL` por heartbeat o reconexión aislados. Se requieren diagnóstico, reconciliación, fuentes frescas, ausencia de órdenes `UNKNOWN`, registro de causa y autorización humana registrada.

G1+G2 y reanudación humana tras pausa material están aprobados por ADR-002; las fórmulas, umbrales y demás reglas de D-012 continúan como diseño pendiente. No se fija broker ni tipo de orden.

## 3. Máquina de estados candidata

| Estado | Nuevas entradas | Órdenes ya vivas | Salida del estado |
|---|---|---|---|
| `NORMAL` | Pueden pasar por Risk Engine | Seguimiento/reconciliación | Incidente o límite |
| `ENTRY_BLOCKED` | Denegadas | Mantener/verificar protección; gestionar cancelación según incidente | Evidencia de recuperación y autorización de reanudación definida |
| `CANCEL_PENDING` | Denegadas | Cancelar solo órdenes elegibles y verificar acuse/fill concurrente | Reconciliación completa |
| `PAUSED_UNCERTAIN` | Denegadas | No asumir cancelación ni posición; consultar broker por IDs | Estado broker/cuenta cierto y runbook |
| `RECOVERY_REVIEW` | Denegadas | Sin orden nueva | Checks de salud, reconciliación y autoridad de reanudación |

Una orden protectora activa y una orden de entrada pendiente no son equivalentes. El estado debe distinguir `entry`, `exit/protection`, `cancel`, `replace` y `reduce`, así como fills durante cancelación. `CANCEL_PENDING` solo aplica a entradas identificadas y verificadas. Transiciones exactas, persistencia y recuperación quedan en D-013; no se infiere permiso G3 de un nombre de estado.

## 4. Matriz de incidentes bajo ADR-002

| Incidente | Acción autorizada G1/G2 | Acción no autorizada o aún pendiente | Riesgo de acción excesiva |
|---|---|---|---|
| Feed stale/corrupto | Bloquear nuevas señales/entradas dependientes; alertar; conservar protección; cancelar entradas solo tras verificar estado y propósito | Cancelar protección o reanudar con dato aún stale | Cancelar un stop por clasificar mal la orden |
| Broker desconectado/timeout | Bloquear entradas, marcar órdenes inciertas, consultar IDs y reconciliar; cancelar entrada solo tras verificar conectividad y estado | Reenviar entrada o presumir cancelación | Reenvío/duplicación o falsa cancelación |
| DB/audit no disponible | Bloquear entradas y pausar hasta recuperar rastro; conservar protección | Enviar cancelación u orden que no pueda auditarse | Protección existente puede quedar sin supervisión |
| Posición, fill u orden interna ≠ broker | Bloquear entradas, `PAUSED_UNCERTAIN`, reconciliar; cancelar solo entrada pendiente verificada | Reducir exposición automáticamente o reanudar sin humano | Cerrar dos veces o sobrepasar posición |
| Límite soft de pérdida/drawdown | Bloquear nuevas entradas si la futura política lo dispone; alerta | Reducir exposición existente automáticamente sin regla aprobada | Umbral mal calibrado por marcas o feed |
| Límite hard validado | Bloquear entradas; cancelar entradas verificadas; runbook y escalamiento; reanudación humana | Reducción gradual o `CLOSE_ALL` automáticos | Gap, liquidez, slippage y órdenes protectoras conflictivas |
| Intent duplicado o autorización caducada | Rechazar intento; bloquear nueva entrada hasta resolver duplicado | Reenviar con nuevo ID sin reconciliar | No debe eliminar una salida protectora válida |
| Prompt injection/shadow intenta cruzar autoridad | Denegar por frontera técnica, registrar, alertar y bloquear nuevas entradas si hay incertidumbre material | Permitir orden o reanudar pausa material sin humano | Confundir intento textual con orden efectivamente enviada |

La tabla autoriza G1+G2 dentro de sus condiciones; no autoriza `REDUCE_EXPOSURE` ni `CLOSE_ALL` generales. `cancel requested` no equivale a `cancel confirmed`: fill concurrente se reconcilia antes de actualizar posición/reserva. Fallo de protección se escala sin cancelar la protección por G2.

## 5. Opciones de gobierno y resultado

| Opción para incidentes tecnológicos o límite hard | Alcance | Ventaja | Riesgo |
|---|---|---|---|
| G1 — bloquear entradas y reconciliar | No incrementa exposición; preserva protección existente | Reduce acciones sobre estado incierto | Posición abierta sigue expuesta a mercado |
| G2 — G1 + cancelar entradas pendientes verificadas | Evita fills de exposición nueva | Limita crecimiento de riesgo | Carrera cancelación/fill; requiere conocer clase de orden |
| G3 — G2 + reducción/cierre según reglas determinísticas | Reduce exposición tras incidente validado | Puede limitar riesgo persistente | Venta en gap/spread alto, doble orden, protección conflictiva |

**Decisión aprobada:** G1 inmediato ante incertidumbre material y G2 solo para entradas pendientes identificadas y verificadas. G3 permanece **no autorizado**. Las órdenes protectoras se conservan; una excepción requiere regla específica, documentada, probada y aprobada. No se elige `CLOSE_ALL` como fallback general.

**Reanudación aprobada:** después de `PAUSED_UNCERTAIN`, discrepancia material de posición/orden, límite hard, falla de protección u otro incidente material, exigir autorización humana registrada tras reconciliación y revisión. Un dato stale transitorio solo podrá reanudarse automáticamente si una política posterior demuestra que es no material y define checks de salud, ventana de estabilidad y ausencia de órdenes inciertas; hasta entonces queda bloqueado. Esta decisión no elige valores numéricos de stops/pérdidas ni broker.

## 6. Evidencia de cierre y pruebas exigidas

- D-012: tabla de precedencia, fórmula de riesgo y reservas, referencia de equity/clock, límites tras escenarios gap/partial fill y justificación/calibración de umbrales; aprobación del propietario.
- D-017: frontera aprobada en ADR-002. Los runbooks y pruebas de carreras cancel/fill, outage, protección y límite hard deben demostrar conformidad antes de PAPER autónomo; no reabren autoridad sin nuevo ADR.
- D-013/D-014: contratos de orden y dato completados antes de fijar semánticas de estado/frescura. Broker/orden concreta y umbrales PAPER calibrados siguen D-021/D-030/D-031.
- Build vs. Reuse: [Open Policy Agent](https://www.openpolicyagent.org/docs/policy-language) puede expresar reglas y [registrar decisiones](https://www.openpolicyagent.org/docs/management-decision-logs); bibliotecas de validación y controles broker son candidatos a comparar. Ninguno sustituye reserva atómica, reconciliación o autorización vinculada al estado. OPA queda `REFERENCE_ONLY / CANDIDATE`, no seleccionado; el evaluador financiero definitivo sigue D-020.
