# Política de riesgo PAPER V1 — contrato P0 RC0

**Estado:** `RESEARCHING` para D-012 y D-017. **Fecha:** 2026-10-01. **Autoridad:** borrador de Plan Architect, sin aprobación de política ni de umbrales. `implementation_locked=true`. Baseline: [hoja §7, §11–12, §32–33 y §54](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [ADR-001](decisions/ADR-001-paper-v1-authority.md).

## 1. Hechos, hipótesis y decisiones reservadas

El baseline exige `TradeIntent → Deterministic Risk Engine → Execution Engine → Broker`, long-only PAPER, sin aprobación humana por operación Champion aprobada. §11.3 propone 25% por posición, 0.50% riesgo estimado por posición, 2% agregado y límites de pérdida/drawdown **como parámetros iniciales de ingeniería**, no como política ya validada. §11.4 lista acciones de kill switch y advierte que `CLOSE_ALL` no debe ser reacción automática a todo fallo. El propietario aprobó A+ para el Portfolio Manager shadow, sin cambiar esos límites ni escoger umbrales.

**Hecho externo relevante:** un stop activado puede ejecutar lejos del precio stop en volatilidad; un stop-limit puede no ejecutar. No se debe presentar `distancia al stop × cantidad` como pérdida máxima garantizada. [FINRA, Stop Orders: Factors to Consider During Volatile Markets, 2025](https://www.finra.org/investors/insights/stop-orders-factors-consider-during-volatile-markets); [Investor.gov, Executing an Order](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/executing-order).

## 2. Reglas de diseño propuestas, aún sin política cuantitativa aprobada

1. **Precedencia:** integridad de cuenta/reconciliación y estado de suspensión; habilitación de Champion/instrumento; frescura/calidad PIT; límites de cuenta/cartera; límites de estrategia/posición; protección de ejecución. Un fallo o `UNKNOWN` en un control necesario deniega **nueva exposición**. Un intento de reducción de riesgo se evalúa por una ruta diferenciada con política propia; no se bloquea ciegamente por la misma regla de entrada.
2. **Estado que se cuenta:** posición reconciliada + órdenes vivas + reservas de intents aprobados y no finalizados. El presupuesto se reserva de forma atómica antes de emitir autorización; expiración, rechazo y fill parcial liberan o ajustan reserva solo después de evento/reconciliación verificable. Dos intents simultáneos no pueden consumir el mismo presupuesto.
3. **Autorización acotada:** `RiskDecision` incluye hash exacto del intent, política y estrategia versionadas, estado de cuenta usado, límite aprobado, validez temporal y checks con motivo. Cambiar snapshot, cantidad, posición o versión invalida la autorización. Execution revalida estado y no amplía el notional aprobado.
4. **Riesgo ex ante y realizado separados:** conservar cálculo de exposición, concentración, pérdida realizada/no realizada y estrés por gap; documentar precio de referencia, spread, liquidez y origen. El tamaño deseado se reduce o rechaza según política; nunca se aumenta para llenar presupuesto.
5. **Protección y fallos:** un stop broker-side, bracket u OCO es candidato sujeto a soporte y semántica del broker; no sustituye supervisión, reconciliación ni escenario de gap. La protección existente se conserva al bloquear nuevas entradas, salvo una instrucción de cancelación/reemplazo autorizada y verificable.
6. **Reanudación:** un sistema suspendido no vuelve a `NORMAL` por un heartbeat aislado. Requiere diagnóstico, reconciliación, fuentes frescas, ausencia de órdenes `UNKNOWN`, registro de causa y autorización de reanudación conforme a la política aprobada.

Estas reglas son recomendaciones de arquitectura para revisión. No fijan broker, tipo de orden ni umbrales.

## 3. Máquina de estados candidata

| Estado | Nuevas entradas | Órdenes ya vivas | Salida del estado |
|---|---|---|---|
| `NORMAL` | Pueden pasar por Risk Engine | Seguimiento/reconciliación | Incidente o límite |
| `ENTRY_BLOCKED` | Denegadas | Mantener/verificar protección; gestionar cancelación según incidente | Evidencia de recuperación y autorización de reanudación definida |
| `CANCEL_PENDING` | Denegadas | Cancelar solo órdenes elegibles y verificar acuse/fill concurrente | Reconciliación completa |
| `PAUSED_UNCERTAIN` | Denegadas | No asumir cancelación ni posición; consultar broker por IDs | Estado broker/cuenta cierto y runbook |
| `REDUCTION_ONLY` | Denegadas | Solo intents de reducción autorizados por política y Risk Engine | Reconciliación y gobierno |
| `RECOVERY_REVIEW` | Denegadas | Sin orden nueva | Checks de salud, reconciliación y autoridad de reanudación |

Una orden protectora activa y una orden de entrada pendiente no son equivalentes. El estado debe distinguir `entry`, `exit/protection`, `cancel`, `replace` y `reduce`, así como fills durante cancelación. Transiciones exactas, persistencia y recuperación quedan en D-013/D-017.

## 4. Matriz de incidentes para decisión humana D-017

| Incidente | Mínimo seguro propuesto mientras se conoce el estado | Acción más fuerte a decidir | Riesgo de acción excesiva |
|---|---|---|---|
| Feed stale/corrupto | Bloquear nuevas señales/entradas dependientes; alertar; conservar protección verificada | Cancelar entradas pendientes que dependían del feed | Cancelar un stop por clasificar mal la orden |
| Broker desconectado/timeout | Bloquear nuevas entradas, marcar órdenes inciertas, consultar IDs y reconciliar al volver | Cancelar entradas abiertas tras confirmar conectividad | Reenvío/duplicación o falsa cancelación |
| DB/audit no disponible | Bloquear nuevas entradas; no operar sin rastro duradero | Pausa de sistema hasta restore | Protección existente puede quedar sin supervisión |
| Posición, fill u orden interna ≠ broker | Bloquear nuevas entradas; estado `PAUSED_UNCERTAIN`; consulta/conciliación | Cancelar entradas y/o reducir exposición tras conocer posición real | Cerrar dos veces o sobrepasar posición |
| Límite soft de pérdida/drawdown | Bloquear o reducir nuevas entradas; alerta | Reducir exposición existente | Umbral mal calibrado por marcas o feed |
| Límite hard validado | Bloquear nuevas entradas; activar runbook y escalamiento | Cancelar pendientes, reducción gradual o `CLOSE_ALL` | Gap, liquidez, slippage y órdenes protectoras conflictivas |
| Intent duplicado o autorización caducada | Rechazar intento; bloquear nueva entrada hasta resolver duplicado | Pausar estrategia/cuenta | No debe eliminar una salida protectora válida |
| Prompt injection/shadow intenta cruzar autoridad | Denegar por frontera técnica, registrar, alertar | Suspender agente/componente afectado | Confundir intento textual con orden efectivamente enviada |

La tabla no autoriza aún `REDUCE_EXPOSURE` o `CLOSE_ALL`. Esos actos financieros exigen política y aprobación humana. La cancelación también necesita semántica de broker y clasificación de orden verificable.

## 5. Opciones de gobierno que requieren decisión

| Opción para incidentes tecnológicos o límite hard | Alcance | Ventaja | Riesgo |
|---|---|---|---|
| G1 — bloquear entradas y reconciliar | No incrementa exposición; preserva protección existente | Reduce acciones sobre estado incierto | Posición abierta sigue expuesta a mercado |
| G2 — G1 + cancelar entradas pendientes verificadas | Evita fills de exposición nueva | Limita crecimiento de riesgo | Carrera cancelación/fill; requiere conocer clase de orden |
| G3 — G2 + reducción/cierre según reglas determinísticas | Reduce exposición tras incidente validado | Puede limitar riesgo persistente | Venta en gap/spread alto, doble orden, protección conflictiva |

**Recomendación provisional:** usar G1 como respuesta inmediata universal a incertidumbre material; G2 únicamente para órdenes de entrada identificadas y con estado broker verificable. Reservar G3 para incidentes y condiciones específicamente aprobados, con posición reconciliada, límites de liquidez y runbook. No elegir `CLOSE_ALL` como fallback general. La decisión exacta D-017 debe fijar qué incidentes habilitan G2/G3, quién autoriza reanudación y cómo se maneja una posición sin protección verificable.

**Reanudación recomendada:** después de `PAUSED_UNCERTAIN`, discrepancia de posición/orden, límite hard o falla de protección, exigir autorización humana registrada tras reconciliación y revisión del incidente. La recuperación de un dato stale aislado puede habilitar una transición automática únicamente si una política posterior define pruebas de salud, ventana de estabilidad y ausencia de órdenes inciertas; hasta entonces se mantiene bloqueada. La decisión solicitada al propietario ahora es aprobar o modificar esta frontera de autoridad, no elegir valores numéricos de stops/pérdidas ni un broker.

## 6. Evidencia de cierre y pruebas exigidas

- D-012: tabla de precedencia, fórmula de riesgo y reservas, referencia de equity/clock, límites tras escenarios gap/partial fill y justificación/calibración de umbrales; aprobación del propietario.
- D-017: matriz incidente→acción aprobada, autoridad de suspensión/reanudación, tratamiento de salidas protectoras y simulaciones de carreras cancel/fill, outage y límite hard; aprobación del propietario.
- D-013/D-014: contratos de orden y dato completados antes de fijar semánticas de estado/frescura. Broker/orden concreta y umbrales PAPER calibrados siguen D-021/D-030/D-031.
- Build vs. Reuse: [Open Policy Agent](https://www.openpolicyagent.org/docs/policy-language) puede expresar reglas y [registrar decisiones](https://www.openpolicyagent.org/docs/management-decision-logs); bibliotecas de validación y controles broker son candidatos a comparar. Ninguno sustituye reserva atómica, reconciliación o autorización vinculada al estado. OPA queda `REFERENCE_ONLY / CANDIDATE`, no seleccionado; el evaluador financiero definitivo sigue D-020.
