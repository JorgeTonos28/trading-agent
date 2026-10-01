# PAPER V1 — contrato de capacidades y autoridad RC1 (A+)

**Fecha:** 2026-10-01. **Estado:** alcance/autoridad funcional **aprobados como A+** en [ADR-001](decisions/ADR-001-paper-v1-authority.md), frontera G1+G2 en [ADR-002](decisions/ADR-002-paper-v1-incident-autonomy.md), orden abstracta en [ADR-003](decisions/ADR-003-order-identity-and-recovery.md), datos PIT en [ADR-004](decisions/ADR-004-point-in-time-data-lineage.md) y roles de señales externas en [ADR-005](decisions/ADR-005-external-signal-admission.md); D-012 y DoR aún abiertos. **Bloqueo:** `implementation_locked=true`. **Decisiones:** D-013/D-014/D-015/D-016/D-017/D-018/D-019 `DECIDED`; D-008 y P1 de stack abiertos. **Fuentes:** [hoja de ruta §4–9, §55–57](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [mapa funcional](research/system_capability_map.md), [video descompuesto](research/video_inspired_strategy.md). Este documento especifica **qué debe poder hacer** PAPER V1 y quién tiene autoridad; ninguna tecnología, broker, proveedor o estrategia queda seleccionada.

## 1. Objetivo y límites de la versión

PAPER V1 debe operar **una configuración/estrategia Champion aprobada inicialmente**, sobre instrumentos long-only del alcance que se defina al seleccionar Strategy V1, desde datos disponibles y versionados hasta órdenes paper reconciliadas. Un Champion puede consumir **varias fuentes o familias de señales**. Debe poder investigar y ensayar Challengers y mantener Portfolio Manager Agent en shadow sin darles autoridad operativa. Cada señal, decisión de riesgo, orden, fill, resultado, propuesta shadow y explicación pedagógica debe poder reconstruirse por identificador y versión. La autonomía por operación existe **solo dentro** de estrategia, capital, riesgo y estado aprobados; no requiere aprobación humana para cada orden válida. El propietario gobierna promoción, cambios centrales, ampliación de límites, broker, derivados y paso a LIVE.

**Alcance mínimo aprobado:** un Champion operativo a la vez; un Portfolio Manager Agent en shadow; un broker PAPER aún por seleccionar; universo acotado según Strategy V1; market data y validación suficientes. Fuentes Smart Money pueden alimentar research o la estrategia seleccionada si pasan sus gates; no se exige ni se excluye una fuente específica. El contrato de datos admite familias heterogéneas. La cantidad de procesos o servicios no se fija aquí. Una funcionalidad puede ser un componente sin LLM.

**Fuera de PAPER V1:** dinero real, leverage, short selling, opciones/futuros/cripto, autopromoción de Challenger, autoedición de política de riesgo o de Champion, conversión de propuestas shadow en intents operativos, y LLM/MCP/plugin con credenciales de broker o herramienta genérica de órdenes. La preparación solo produce documentos y probes desechables.

## 2. Fronteras invariantes

```text
Research/Alternative Data ──> Strategy Lab/Challenger (sin órdenes)
Market/Data Snapshot ──> Champion Signal ──> Portfolio/Intent
                      ──> TradeIntent ──> Deterministic Risk Engine
                      ──> autorización vinculada al intento ──> Execution Engine
                      ──> Broker Adapter ──> PAPER Broker
Contexto elegible ──> Portfolio Manager Agent SHADOW
                  ──> ShadowPortfolioProposal ──> Audit/Evaluation ONLY
Broker Events ──> Reconciliation ──> Audit/Performance
Audit/Performance ──> Monitoring + Pedagogical Agent + Research
```

1. El **único camino** de entrada, cambio o cancelación de posición es la ruta de intento, riesgo y ejecución autorizada. Ningún agente recibe `broker.buy/sell` ni secretos del broker.
2. El Risk Engine es autoridad financiera **determinística**. Puede rechazar o reducir dentro de política aprobada; nunca ampliar capital, riesgo o instrumentos por sugerencia de un modelo.
3. Execution valida que autorización, intent, versión de riesgo/estrategia, estado de cuenta y vencimiento sigan vigentes. Ante discrepancia o incertidumbre, no crea una nueva orden y reconcilia.
4. Research, backtest, pedagogy, monitoring generativo y Challengers pueden **proponer** o explicar; no cambian Champion ni parámetros activos. Promoción y cambios materiales requieren registro y aprobación humana.
5. Datos externos se consumen con licencia, origen y disponibilidad temporal explícitos. Un dato retrospectivamente enriquecido no se usa como si hubiera existido en tiempo real.
6. `ShadowPortfolioProposal` usa el **mismo contexto elegible** al tiempo de decisión que el camino Champion, cuando corresponde, pero vive en un canal separado: no se convierte en `TradeIntent`, no llega a Risk/Execution/Broker y no modifica posiciones, Champion, riesgo ni asignaciones. Su captura y evaluación son auditables.

Estos puntos desarrollan D-002/D-005 ya `DECIDED`. D-017 fija G1+G2 y reanudación humana tras pausa material; las reglas cuantitativas D-012 siguen abiertas.

## 3. Matriz de responsabilidad y permiso aprobada en alcance

`R` lectura; `P` propuesta/artefacto sin efecto financiero; `I` crea intent; `A` autoriza/rechaza determinísticamente; `E` ejecuta solo autorización válida; `S` solicita suspensión; `H` aprueba gobierno. Un guion significa permiso ausente. Los permisos son **capacidades**, no acceso directo a tablas, claves o endpoints. El canal shadow no posee ruta técnica a `TradeIntent`.

| Rol/componente | Datos/estado | Research/Challenger | Señal | TradeIntent | RiskDecision | Orden broker | Suspensión | Cambio Champion/política |
|---|---|---|---|---|---|---|---|---|
| Market/Quant/Backtest Agents | R según licencia | P | P en sandbox | — | — | — | — | — |
| Data Quality | R, marca calidad | P | — | — | — | — | S si dato crítico | — |
| Champion Signal Engine | R snapshot elegible | — | P versionada | — | — | — | — | — |
| Portfolio/Intent assembler | R estado reconciliado | — | R | **I** según Champion y presupuesto | — | — | — | — |
| Portfolio Manager Agent **SHADOW** | R contexto elegible sin secretos | P `ShadowPortfolioProposal` | R, puede proponer señal shadow | **—** | — | **—** | — | — |
| Risk Agent explicativo | R | P | — | — | — | — | S | — |
| **Deterministic Risk Engine** | R estado y política | — | R | R | **A** | — | A/S según política | — |
| Execution Engine/Broker adapter | R mínimo | — | — | R autorizado | R | **E** | G2: cancela solo entradas pendientes verificadas; sin liquidación automática general | — |
| Monitoring/Sentinel | R | P | — | — | — | — | **S**; acción final determinística | — |
| Performance/Attribution | R auditado | P | — | — | — | — | — | — |
| Champion/Challenger manager | R | P | P sandbox | — | — | — | — | solicita promoción |
| Pedagogical Agent | R auditado y filtrado | P educativa | — | — | — | — | — | — |
| Humano propietario | R | P | — | — | política aprobada | — en el flujo autónomo | H para reanudación material | **H** |

**D-015 aprobado:** un ensamblador determinístico crea el `TradeIntent` operativo; Portfolio Manager Agent produce propuestas estructuradas **shadow**. Puede expresar prioridad y notional hipotéticos, pero no modifica cantidad/prioridad del Champion ni el presupuesto real. La futura autoridad limitada tipo opción B necesita evidencia y un nuevo ADR aprobado. Ninguna modalidad permite saltarse Risk Engine.

## 4. Contratos de información, todavía independientes del stack

| Artefacto | Campos/identidad mínimos | Productor → consumidor | Condición de aceptación |
|---|---|---|---|
| `DataObservation` / snapshot | fuente/canal, dataset/versión, instrumento/entidad, clocks distintos, `availability_evidence`, `eligible_from`, revisión/supersedes, calidad, licencia, hash | Ingestión → research/signal | Sin evidencia de disponibilidad operable al corte, no habilita señal Champion; ADR-004 |
| `ResearchHypothesis` / `ChallengerSpec` | hipótesis falsable, universo, entradas/salidas, sizing, costes, benchmark, datos PIT, autor/versión | Agents → Strategy Lab | Sin capacidad de orden ni promoción automática |
| `Signal` | Champion/version, instrumento, decisión, puntuación/razones medibles, snapshot ID, reloj de decisión, vigencia | Signal Engine → Portfolio/Intent | Replay con mismo snapshot y versión produce mismo resultado o divergencia explicada |
| `ShadowPortfolioProposal` | ID, versión del agente/modelo/prompt/política shadow, `decision_time`, context/snapshot IDs y data cut-off, posiciones hipotéticas a abrir/cerrar/mantener, prioridad, notional/sizing, señales, razones estructuradas, confianza calibrada o `NOT_APPLICABLE`, fuentes, supuestos y limitaciones | Portfolio Manager Agent → **Shadow Audit/Evaluation solamente** | Nunca se acepta como `Signal`/`TradeIntent` operativo; no comparte credenciales ni endpoint de Execution; rechazo automático de cualquier intento de cruzar frontera |
| `TradeIntent` | ID único, signal ID, estrategia/version, instrumento, lado, notional/cantidad deseada, razón, política de stop, expiración, cuenta/estado de referencia | Portfolio/Intent → Risk | No es orden; inválido sin snapshot, estrategia habilitada y estado fresco |
| `RiskDecision` | intent ID + hash, política/version, cuenta/posición/version, checks y motivos, notional autorizado, expiración, firma/verificador | Risk → Execution | No reusarse con intent o estado modificado; denegación registrada |
| `OrderCommand` / `BrokerEvent` | `order_key` interno; IDs broker según API; autorización vinculada, tipo/TIF, broker/account, aceptación, parcial, fill, cancel/reject y timestamps | Execution ↔ Broker | Duplicados y eventos fuera de orden no crean posiciones fantasma; G2 `CancelCommand` solo con autorización determinística ADR-002/003 |
| `ReconciliationRecord` | estado interno vs broker, diferencias, acción y estado de bloqueo | Reconciliation → Risk/monitoring | Incertidumbre material bloquea nuevas entradas hasta resolver |
| `PedagogicalReport` | trade/intent/decision/order/fill IDs, explicación factual, conceptos §55, incertidumbre, links a fuente y versión | Pedagogical → propietario | No inventa causa, precio/fill ni rendimiento; distingue plan, autorización y resultado |

El modelo abstracto de identidad/estados se fija en D-013/ADR-003 y los clocks/revisiones/ajustes as-of en D-014/ADR-004. Esquemas por broker y dataset siguen D-021/D-030/D-018/D-022/D-033. No se confunde `published_at` con `event_at`; un campo desconocido permanece desconocido. El snapshot shadow debe corresponder al mismo instante de decisión y datos disponibles del Champion para que la comparación sea justa; puede registrar diferencias explícitas de contexto.

## 5. Capacidad por etapa y criterio observable

| Fase | Capacidad mínima | Evidencia de aceptación planificada |
|---|---|---|
| B0/B1 — research y validación | Datos versionados; Strategy V1 seleccionada; backtest reproducible, OOS, costes y benchmarks | Spec, datasets/snapshots, experiment IDs y replay documentados |
| B2 — core financiero | `TradeIntent`, política determinística, estados y autorización vinculante | Casos válidos e inválidos: rechazo, reducción, stale, gap y conflicto; sin broker directo |
| B3 — integración paper | Una orden de prueba autorizada, eventos, parciales, cancelación, reinicio y reconciliación | Replay sin orden duplicada; diferencias bloquean nueva entrada |
| B4 — paper autónomo controlado | Señal Champion, schedule/event trigger, riesgo, ejecución, monitor y cierre diario; **Portfolio Manager shadow produce propuestas auditadas** y Pedagogical Agent explica hechos | Opera sin aprobación por trade dentro de límites; shadow aislado; kill switch probado; data/broker outage falla cerrado |
| B5 — agentes/capa de capacidades | Research/quant/monitor/attribution/pedagogy aprobados; plugin/Skills/MCP solo si scorecard los justifica | Reporte pedagógico completo, comparación Champion vs shadow; ninguna herramienta de investigación puede cursar orden |
| B6 — Champion/Challenger | Pipeline formal y comparación sin autoridad de promoción automática | Challenger produce evidencia/shadow, propietario aprueba promoción |
| B7+ — fuentes nuevas/LIVE | Fuentes externas adicionales, shadow/live según gates separados | No bloquean la primera operación PAPER salvo que Strategy V1 dependa de ellas |

**Conciliación aprobada de la hoja:** §8.6 pide Regime Detection en modo observación «desde el principio» y aclara que no es obligatorio para la primera operación. Su contrato y trabajo observador se ubican temprano en B1/B2; puede estar `UNKNOWN` en la primera orden B3 y debe observar antes del DoD. §56 ubica agentes/plugin ricos en B5 después de B4, mientras §57 exige informe pedagógico para el **Definition of Done final**. La explicación factual empieza en B4 y el informe completo llega en B5 antes de declarar PAPER V1 terminada. §4 exige ensayar Challengers sin autoridad de capital: el aislamiento/pipeline B6 también es requisito del V1 funcional final, aunque no impida la primera operación B3/B4. El Portfolio Manager Agent opera en shadow desde B4. Estos hitos no autorizan una tecnología concreta.

## 6. Fallos y límites de autoridad que el plan debe probar

| Escenario | Resultado requerido conforme a D-013/D-017; detalle cuantitativo D-012 y broker D-021/030 pendiente |
|---|---|
| Datos stale, timestamp PIT desconocido o calidad insuficiente | No nueva señal/entrada dependiente; alerta y rastro de rechazo |
| Dos señales o intents concurrentes consumen mismo presupuesto | Reserva/serialización determinística; nunca exposición superior al límite |
| Risk aprueba y cambian posición/precio/versión antes de enviar | Invalidar/revalidar; no usar aprobación vieja |
| Broker acepta pero respuesta/DB/stream falla | Consultar por client ID y reconciliar antes de reintentar; no duplicar |
| Fill parcial, cancelación o eventos reordenados | Estado monotónico/reconciliado; no asumir fill completo |
| Incertidumbre material o hard limit | G1 bloquea entradas y reconcilia; G2 solo cancela entrada pendiente identificada y verificada; conserva protección; G3 no autorizado |
| Pausa por discrepancia material, hard limit o protección fallida | Reanudación con autorización humana registrada, nunca solo por heartbeat/reconexión |
| Stop cruza gap o falla monitor | No prometer pérdida máxima igual al umbral; respuesta por política y prueba de escenario |
| Prompt injection en fuente, correo, Skill o MCP | Contenido de datos no adquiere permisos; aislamiento/validación y logging |
| Agente propone cambio de Champion, riesgo o broker | Solicitud de gobierno; no desplegar ni ejecutar hasta aprobación registrada |
| Reporte pedagógico sin causalidad verificable | Explicar solo hechos observados y marcar interpretación/incertidumbre |
| Shadow intenta emitir un intent/usar broker o cambiar asignaciones | Frontera técnica deniega, registra intento y alerta; no basta una instrucción de prompt |
| Shadow usa datos posteriores o evalúa con fill perfecto | Invalidar comparación; replay PIT y modelo de costes/fills hipotéticos versionados |

## 7. Build vs. Reuse como puerta de diseño permanente

| Capacidad | Alternativas ya identificadas; ninguna seleccionada | Evaluación antes de construir |
|---|---|---|
| Flujos de investigación/pedagogía | OpenAI Skills/Plugins; plantillas/Skills Anthropic; procedimientos propios | `ADAPT/PORT/REFERENCE_ONLY` según licencia, formato y calidad; Skills no conceden permisos por sí mismas. [OpenAI Skills](https://developers.openai.com/plugins/concepts/skills) |
| Agentes/orquestación | OpenAI Agents SDK, Codex, frameworks open source y llamadas directas | Evaluar handoffs, estado, tracing, permisos, coste y portabilidad. El SDK ejecuta loop y herramientas, pero nuestra app conserva deployment, storage y decisiones de aprobación. [Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) |
| Acceso a datos/herramientas | APIs directas, MCP de proveedores y plugins | `WRAP` detrás de adaptadores de solo lectura cuando aplique; licencias, schemas, PIT, prompt injection y fiabilidad por herramienta. [Arquitectura de plugins](https://developers.openai.com/plugins/concepts/plugins) |
| Backtest y market data | LEAN, NautilusTrader, vectorbt, proveedores market/alternative data | Probes de semántica de órdenes/PIT/costes; no construir motor por inercia |
| Broker adapter y stops | APIs oficiales de candidatos, tipos de orden y streams | Scorecard R-007; no seleccionar Alpaca por el video |
| Risk gateway | Bibliotecas de reglas/validación más núcleo determinístico bajo control del proyecto | No seleccionar `BUILD` hasta comparar componentes reutilizables; guardrails de agente no reemplazan chequeo financiero por llamada. [Guardrails oficiales](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) |
| Pedagogical Agent | Skills y flujos de explicación, trazas/evals reutilizables | Medir fidelidad factual y trazabilidad; no depender de texto libre sin evidencia |

Cada capacidad mayor recibe ficha R-006 con `EXISTS`, `AVAILABLE_TO_US`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE`, `SELECTED` y una disposición `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT` antes de ADR técnico. La documentación oficial de OpenAI confirma la separación Skill (workflow) / MCP (acciones) y que los guardrails del SDK tienen alcance específico por entrada/salida/herramienta; la inferencia arquitectónica del proyecto es exigir autorización financiera **fuera** del agente, en el gateway determinístico.

## 8. Decisión A+ y futura evaluación de autoridad

| Opción | Alcance/autoridad | Ventaja | Coste/riesgo |
|---|---|---|---|
| A — propuesta inicial | Un Champion; Signal e intent assembly determinísticos; Portfolio Manager Agent asesor conceptual | Frontera financiera simple | No genera evidencia estructurada del valor del agente |
| **A+ — aprobada** | A más Portfolio Manager Agent en shadow con propuesta versionada y evaluación PIT, sin ruta a intent/órdenes | Evidencia para futura decisión con frontera financiera intacta | Requiere aislamiento y medición reproducible |
| B | Portfolio Manager Agent prioriza y ajusta notional dentro de límites; Risk lo reduce/rechaza | Más flexibilidad con señales múltiples desde inicio | Mayor superficie de no determinismo y de pruebas, conflictos/versionado adicionales |
| C | Agente opera vía broker/CLI y guarda stops/monitor mediante automations, como en el video | Demostración rápida | **Inadmisible** bajo D-002, D-005 y AGENTS.md sin cambio explícito de invariante; no recomendada |

**Decisión registrada:** A+ fue aprobada explícitamente por el propietario. Evaluar coincidencias/divergencias con Champion determinístico, riesgo propuesto, rendimiento hipotético neto de costes, estabilidad, reproducibilidad, errores y utilidad incremental. Las métricas y ventanas se preregistrarán antes de mirar resultados; ninguna métrica promueve autoridad automáticamente. Esta aprobación no selecciona Strategy V1, broker, proveedor, umbrales de riesgo ni runtime.

**Estado registrado:** D-015/D-016/D-019 están `DECIDED` en el alcance funcional A+; D-013/D-014/D-017/D-018 también están `DECIDED` en sus contratos abstractos. Riesgo cuantitativo, admisión PIT por dataset, formato/evals, broker y tecnología continúan en sus decisiones propias. `implementation_locked=true` durante preparación.
