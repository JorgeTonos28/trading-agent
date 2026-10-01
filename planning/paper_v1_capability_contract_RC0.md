# PAPER V1 — contrato de capacidades y autoridad RC0

**Fecha:** 2026-10-01. **Estado:** `READY_FOR_DECISION` para alcance y autoridad material; **no aprobado ni congelado**. **Bloqueo:** `implementation_locked=true`. **Decisiones:** D-015/D-016/D-018/D-019, con dependencias D-008/D-012–014/D-017 y P1 de stack. **Fuentes:** [hoja de ruta §4–9, §55–57](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [mapa funcional](research/system_capability_map.md), [video descompuesto](research/video_inspired_strategy.md). Este documento especifica **qué debe poder hacer** PAPER V1 y quién tiene autoridad; ninguna tecnología, broker, proveedor o estrategia queda seleccionada.

## 1. Objetivo y límites de la versión

PAPER V1 debe operar **una estrategia Champion aprobada**, sobre instrumentos long-only del alcance que se defina al seleccionar Strategy V1, desde datos disponibles y versionados hasta órdenes paper reconciliadas. Debe poder investigar y ensayar Challengers sin darles autoridad operativa. Cada señal, decisión de riesgo, orden, fill, resultado y explicación pedagógica debe poder reconstruirse por identificador y versión. La autonomía por operación existe **solo dentro** de estrategia, capital, riesgo y estado aprobados; no requiere aprobación humana para cada orden válida. El propietario gobierna promoción, cambios centrales, ampliación de límites, broker, derivados y paso a LIVE.

**Propuesta de alcance mínimo:** un Champion a la vez; un broker PAPER; un universo acotado según Strategy V1; una fuente primaria de market data y validación suficiente; fuentes Smart Money opcionales como entradas de investigación hasta que una estrategia seleccionada las requiera. El contrato de datos admite familias heterogéneas desde el inicio. La cantidad de agentes, procesos o servicios no se fija aquí. Una funcionalidad puede ser un componente sin LLM.

**Fuera de PAPER V1:** dinero real, leverage, short selling, opciones/futuros/cripto, autopromoción de Challenger, autoedición de política de riesgo o de Champion, y LLM/MCP/plugin con credenciales de broker o herramienta genérica de órdenes. La preparación solo produce documentos y probes desechables.

## 2. Fronteras invariantes

```text
Research/Alternative Data ──> Strategy Lab/Challenger (sin órdenes)
Market/Data Snapshot ──> Champion Signal ──> Portfolio/Intent
                      ──> TradeIntent ──> Deterministic Risk Engine
                      ──> autorización vinculada al intento ──> Execution Engine
                      ──> Broker Adapter ──> PAPER Broker
Broker Events ──> Reconciliation ──> Audit/Performance
Audit/Performance ──> Monitoring + Pedagogical Agent + Research
```

1. El **único camino** de entrada, cambio o cancelación de posición es la ruta de intento, riesgo y ejecución autorizada. Ningún agente recibe `broker.buy/sell` ni secretos del broker.
2. El Risk Engine es autoridad financiera **determinística**. Puede rechazar o reducir dentro de política aprobada; nunca ampliar capital, riesgo o instrumentos por sugerencia de un modelo.
3. Execution valida que autorización, intent, versión de riesgo/estrategia, estado de cuenta y vencimiento sigan vigentes. Ante discrepancia o incertidumbre, no crea una nueva orden y reconcilia.
4. Research, backtest, pedagogy, monitoring generativo y Challengers pueden **proponer** o explicar; no cambian Champion ni parámetros activos. Promoción y cambios materiales requieren registro y aprobación humana.
5. Datos externos se consumen con licencia, origen y disponibilidad temporal explícitos. Un dato retrospectivamente enriquecido no se usa como si hubiera existido en tiempo real.

Estos puntos desarrollan D-002/D-005 ya `DECIDED`. Los detalles de política D-012/D-017 siguen abiertos y no se sustituyen por este contrato.

## 3. Matriz de responsabilidad y permiso propuesta

`R` lectura; `P` propuesta/artefacto sin efecto financiero; `I` crea intent; `A` autoriza/rechaza determinísticamente; `E` ejecuta solo autorización válida; `S` solicita suspensión; `H` aprueba gobierno. Un guion significa permiso ausente. Los permisos son **capacidades**, no acceso directo a tablas, claves o endpoints.

| Rol/componente | Datos/estado | Research/Challenger | Señal | TradeIntent | RiskDecision | Orden broker | Suspensión | Cambio Champion/política |
|---|---|---|---|---|---|---|---|---|
| Market/Quant/Backtest Agents | R según licencia | P | P en sandbox | — | — | — | — | — |
| Data Quality | R, marca calidad | P | — | — | — | — | S si dato crítico | — |
| Champion Signal Engine | R snapshot elegible | — | P versionada | — | — | — | — | — |
| Portfolio/Intent assembler | R estado reconciliado | — | R | **I** según Champion y presupuesto | — | — | — | — |
| Risk Agent explicativo | R | P | — | — | — | — | S | — |
| **Deterministic Risk Engine** | R estado y política | — | R | R | **A** | — | A/S según política | — |
| Execution Engine/Broker adapter | R mínimo | — | — | R autorizado | R | **E** | ejecuta cancelación/liquidación solo según política | — |
| Monitoring/Sentinel | R | P | — | — | — | — | **S**; acción final determinística | — |
| Performance/Attribution | R auditado | P | — | — | — | — | — | — |
| Champion/Challenger manager | R | P | P sandbox | — | — | — | — | solicita promoción |
| Pedagogical Agent | R auditado y filtrado | P educativa | — | — | — | — | — | — |
| Humano propietario | R | P | — | — | política aprobada | — en el flujo autónomo | H para reanudación material | **H** |

**Decisión material pendiente D-015:** confirmar si en V1 el Portfolio Manager Agent es solo asesor/observador y un ensamblador determinístico crea el `TradeIntent` (recomendación), o si el agente puede decidir prioridad/notional dentro de límites que el riesgo valida. Con un Champion, la asignación multi-estrategia no aporta valor inicial y aumenta la superficie de autoridad. Ninguna opción permite saltarse Risk Engine.

## 4. Contratos de información, todavía independientes del stack

| Artefacto | Campos/identidad mínimos | Productor → consumidor | Condición de aceptación |
|---|---|---|---|
| `DataObservation` / snapshot | fuente, dataset/versión, instrumento/entidad, `event_at`, `published_at`, `received_at`, `available_at` o desconocido, revisión, calidad, licencia, hash | Ingestión → research/signal | Si falta momento operable o calidad requerida, no habilita señal Champion |
| `ResearchHypothesis` / `ChallengerSpec` | hipótesis falsable, universo, entradas/salidas, sizing, costes, benchmark, datos PIT, autor/versión | Agents → Strategy Lab | Sin capacidad de orden ni promoción automática |
| `Signal` | Champion/version, instrumento, decisión, puntuación/razones medibles, snapshot ID, reloj de decisión, vigencia | Signal Engine → Portfolio/Intent | Replay con mismo snapshot y versión produce mismo resultado o divergencia explicada |
| `TradeIntent` | ID único, signal ID, estrategia/version, instrumento, lado, notional/cantidad deseada, razón, política de stop, expiración, cuenta/estado de referencia | Portfolio/Intent → Risk | No es orden; inválido sin snapshot, estrategia habilitada y estado fresco |
| `RiskDecision` | intent ID + hash, política/version, cuenta/posición/version, checks y motivos, notional autorizado, expiración, firma/verificador | Risk → Execution | No reusarse con intent o estado modificado; denegación registrada |
| `OrderCommand` / `BrokerEvent` | idempotency key/client ID, autorización, tipo/TIF, broker/account, aceptación, parcial, fill, cancel/reject y timestamps | Execution ↔ Broker | Duplicados y eventos fuera de orden no crean posiciones fantasma |
| `ReconciliationRecord` | estado interno vs broker, diferencias, acción y estado de bloqueo | Reconciliation → Risk/monitoring | Incertidumbre material bloquea nuevas entradas hasta resolver |
| `PedagogicalReport` | trade/intent/decision/order/fill IDs, explicación factual, conceptos §55, incertidumbre, links a fuente y versión | Pedagogical → propietario | No inventa causa, precio/fill ni rendimiento; distingue plan, autorización y resultado |

Los esquemas definitivos, clocks, corporate actions y modelo de estados se cierran en D-013/D-014. No se confunde `published_at` de una fuente con `event_at` del hecho económico; un campo desconocido permanece desconocido.

## 5. Capacidad por etapa y criterio observable

| Fase | Capacidad mínima | Evidencia de aceptación planificada |
|---|---|---|
| B0/B1 — research y validación | Datos versionados; Strategy V1 seleccionada; backtest reproducible, OOS, costes y benchmarks | Spec, datasets/snapshots, experiment IDs y replay documentados |
| B2 — core financiero | `TradeIntent`, política determinística, estados y autorización vinculante | Casos válidos e inválidos: rechazo, reducción, stale, gap y conflicto; sin broker directo |
| B3 — integración paper | Una orden de prueba autorizada, eventos, parciales, cancelación, reinicio y reconciliación | Replay sin orden duplicada; diferencias bloquean nueva entrada |
| B4 — paper autónomo controlado | Señal Champion, schedule/event trigger, riesgo, ejecución, monitor y cierre diario | Opera sin aprobación por trade, pero dentro de límites; kill switch probado; data/broker outage falla cerrado |
| B5 — agentes/capa de capacidades | Research/quant/monitor/attribution/pedagogy aprobados; plugin/Skills/MCP solo si scorecard los justifica | Reporte por operación trazable y útil; ninguna herramienta de investigación puede cursar orden |
| B6 — Champion/Challenger | Pipeline formal y comparación sin autoridad de promoción automática | Challenger produce evidencia/shadow, propietario aprueba promoción |
| B7+ — fuentes nuevas/LIVE | Fuentes externas adicionales, shadow/live según gates separados | No bloquean la primera operación PAPER salvo que Strategy V1 dependa de ellas |

**Conciliación de la hoja:** §8.6 pide Regime Detection en modo observación «desde el principio» y aclara que no es obligatorio para la primera operación. La propuesta incluye su contrato y trabajo observador temprano en B1/B2, permite estado `UNKNOWN` en la primera orden de B3 y exige observación activa antes de declarar terminada PAPER V1; nunca cambia parámetros Champion. §56 ubica agentes/plugin ricos en B5 después de B4, mientras §57 exige informe pedagógico para el **Definition of Done final** de PAPER V1. Se propone una explicación factual mínima desde B4 y el informe completo en B5 antes de declarar PAPER V1 terminada. §4 exige ensayar Challengers sin autoridad de capital: el aislamiento/pipeline B6 también es requisito del V1 funcional final, aunque no impida la primera operación B3/B4. Esto es interpretación para aprobación, no modificación silenciosa del roadmap.

## 6. Fallos y límites de autoridad que el plan debe probar

| Escenario | Resultado requerido, sujeto a política D-012/D-017 |
|---|---|
| Datos stale, timestamp PIT desconocido o calidad insuficiente | No nueva señal/entrada dependiente; alerta y rastro de rechazo |
| Dos señales o intents concurrentes consumen mismo presupuesto | Reserva/serialización determinística; nunca exposición superior al límite |
| Risk aprueba y cambian posición/precio/versión antes de enviar | Invalidar/revalidar; no usar aprobación vieja |
| Broker acepta pero respuesta/DB/stream falla | Consultar por client ID y reconciliar antes de reintentar; no duplicar |
| Fill parcial, cancelación o eventos reordenados | Estado monotónico/reconciliado; no asumir fill completo |
| Stop cruza gap o falla monitor | No prometer pérdida máxima igual al umbral; respuesta por política y prueba de escenario |
| Prompt injection en fuente, correo, Skill o MCP | Contenido de datos no adquiere permisos; aislamiento/validación y logging |
| Agente propone cambio de Champion, riesgo o broker | Solicitud de gobierno; no desplegar ni ejecutar hasta aprobación registrada |
| Reporte pedagógico sin causalidad verificable | Explicar solo hechos observados y marcar interpretación/incertidumbre |

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

## 8. Paquete de decisión material pendiente

| Opción | Alcance/autoridad | Ventaja | Coste/riesgo |
|---|---|---|---|
| A — **recomendada** | Un Champion; Signal e intent assembly determinísticos; Portfolio Manager Agent solo asesor; investigación/Smart Money opcional en read-only; reporte pedagógico factual mínimo en B4 y completo antes del DoD | Frontera financiera simple, reproducible y coherente con la hoja; conserva camino de expansión | Menos discreción agéntica inicial; cambios de estrategia pasan por gobierno |
| B | Portfolio Manager Agent prioriza y ajusta notional dentro de límites; Risk lo reduce/rechaza | Más flexibilidad con señales múltiples desde inicio | Mayor superficie de no determinismo y de pruebas, conflictos/versionado adicionales |
| C | Agente opera vía broker/CLI y guarda stops/monitor mediante automations, como en el video | Demostración rápida | **Inadmisible** bajo D-002, D-005 y AGENTS.md sin cambio explícito de invariante; no recomendada |

**Recomendación técnica:** A para PAPER V1. Decisión exacta requerida del propietario: aprobar o modificar **(i)** un Champion único inicial, **(ii)** autoridad de Signal/Portfolio/Intent determinística en operación, **(iii)** separación research/Smart Money sin orden directa y **(iv)** calendario de pedagogía B4/B5. La aprobación no selecciona Strategy V1, broker, proveedor, umbrales de riesgo ni runtime; esos expedientes conservan sus gates.

**Estado registrado:** D-015/D-016/D-019 están `READY_FOR_DECISION` con este paquete; formato/evals pedagógicos P1 pendientes. D-018 continúa `RESEARCHING` hasta contrato PIT por familia. Ningún cambio de autoridad se activa durante preparación.
