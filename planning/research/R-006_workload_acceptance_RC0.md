# R-006 — workload PAPER y matriz de aceptación RC0

**Fecha:** 2026-10-05. **Estado:** diseño de experimento propuesto; pasos 1–2 autónomos. No workload de Strategy V1 seleccionado, SLA aprobado, umbral financiero ni promesa de cuota Plus. Usa [contratos por rol](../06_agent_evidence_contract_RC0.md), [shadow](../06_shadow_portfolio_contract_RC0.md), [pedagogía](../06_pedagogical_contract_RC0.md), waves 04–06 y [Plus Gate](R-006_plus_runtime_gate_RC0.md).

## 1. Unidad de carga y demanda

Un **job** = una invocación lógica con snapshot/contrato inmutables y output final admitido; retries/intentos, tool reads y consultas interactivas cuentan aparte. Research/quant de background pueden diferirse dentro de ventana; shadow obligatorio se agenda en **cada evento de decisión de cartera** del perfil aprobado, no solo cuando el Champion abre una posición. Pedagogía factual se registra en cada evento material y produce informe por operación/día/semana. Batch de narrativa no elimina logging factual, shadow requerido ni informes completos. El LLM no genera señales/intents operativos ni participa permanentemente en controles financieros.

Supuestos de ingeniería **solo para probar capacidad**, revisables al seleccionar Strategy V1: ventana ejemplo 6.5 h, máximo 20 instrumentos, 2 fuentes por instrumento, 20 posiciones/eventos de trace por bundle, quotes/cash/reservas versionados, texto en español. No obliga a negociar US equities en esa sesión ni limita definitivamente universo/fuentes. Instrumentos SYN; no market data real ni broker.

| Perfil | Shadow pareado / día | Pedagogía por operación/evento + diario | Research | Quant | Total jobs base / día | Uso |
|---|---:|---:|---:|---:|---:|---|
| WL-L | 1 | 4 + 1 | 1 | 1 | 8 | Cadencia lenta/EOD ilustrativa; mínimo de integración, no demuestra WL-R |
| **WL-R representativo propuesto** | 26 (cada 15 min en ventana ejemplo) | 10 + 1 | 2 | 1 | **40** | Perfil de dimensionamiento para candidata; no estrategia intradía aprobada |
| WL-S estrés | 78 (cada 5 min) | 20 + 1 | 4 | 2 | 105 | Detectar frontera de cuota/backlog; no requisito para aceptar WL-R |

Además por semana: 1 lección, 1 actualización glossary/concept-map, 1 revisión de experimentos quant = **3 jobs** si no se agrupan justificadamente. Reserva de demanda interactiva del dueño: **10 jobs/día** en WL-R; demanda de prueba adicional de hasta **25%** de los 50 jobs base+interactivos, redondeada arriba, para retries/variación -> **63 jobs/día** en el escenario de aceptación. Estos son parámetros de prueba de carga, **no** márgenes financieros aprobados ni límites reales del plan. No repetir una decisión financiera por retry del agente.

Tamaños de payload UTF-8 sin secretos: pequeño ≤8 KiB, representativo ≤32 KiB, estrés ≤128 KiB. Medir también tokenizer del modelo/contexto y overhead de Skill/policy/tool/schema: bytes != tokens != consumo de cuota. Pedagogía semanal usa resumen verificable y refs a traces, no miles de eventos sin límite; rehidratar detalle de evidencia cuando sea necesario. El límite final de bundle se aprueba en D-024/026 con pruebas, no descartar fuentes para pasar artificialmente.

## 2. Plan de prueba y plazos propuestos

1. Fixture spine pequeña Team (wave 06) prueba correcciones concretas. **No** es una prueba de carga representativa ni entitlement.
2. Corpus representativo **especificado**: 20 instrumentos, 40 observaciones PIT con revisiones, 10 trades/intents incluidos rechazos/no-trade, 20 eventos trace/cash/reservas, discrepancia G1+G2, precio stale, missing cause/outcome, 1 texto inyectado, 1 revisión futura, fuente de disponibilidad UNKNOWN y derivación inválida. Construir datos sintéticos al medir la ruta finalista; aceptar solo hechos válidos, conservar exclusiones/IDs. No copiar datos comerciales sin licencia. No afirmar ejecutado un corpus por tener especificación.
3. Bajo Plus, **después del acceso y aprobación de candidata**, 1 smoke por procedimiento/ruta activa + regresión de diferencia material; luego sesión WL-R y observación de cuota compartida/ventanas. Propuesto: al menos 5 sesiones representativas repartidas en ≥7 días con uso interactivo registrado, incluyendo fin de ventana/reset cuando observable. No es autorización a automation/scheduled spending; ejecuciones futuras requieren entorno y política operativa concretos. Planifier puede adaptar calendario al reset real; un período no observado queda UNKNOWN.
4. WL-S se simula offline para colas y se prueba en Plus solo si el presupuesto/cuota existente lo permite; no agotar cuota ni comprar capacidad para completar estrés. Fallar WL-S no falla WL-R. Si WL-R no es suficiente, documentar breakpoint y opciones Tier 0/1, no bajar demanda shadow silenciosamente.

Plazos de experimento propuestos: shadow WL-R recibido ≤120 s después del snapshot; informe por operación/evento ≤10 min cuando llegan las trazas; daily antes de 09:00 hora America/Santo_Domingo del siguiente día de prueba; research/quant background dentro de 24 h; lección semanal dentro de 48 h de cierre semanal. **No** aprobación de cadencia/latencia final de trading. Si Strategy V1 requiere otro intervalo, rebaselinar antes de selección/operación y reusar conducta Team.

Criterio de capacidad WL-R propuesto: ≥95% de jobs requeridos con entrega funcional admisible on-time y **100% accounting** de faltantes/fail/late/quota; 100% de invariantes de autoridad/PIT/lineage en casos críticos; ningún fallo/información omitida presentado como éxito. `INSUFFICIENT_EVIDENCE/ABSTAIN` se admite y registra, pero **no** cuenta como entrega funcional exitosa cuando el fixture trae evidencia suficiente para la tarea. Abstención correcta ante datos insuficientes se puntúa en su clase de fallo/control, separada de carga válida; el denominador total requerido siempre se reporta. No pasar suficiencia solo generando placeholders. El 5% no concede excepción al DoD: incidentes/missing explicaciones deben quedar resueltos o con limitación explícita y gates funcionales cumplidos; fallo persistente shadow/pedagogía falla suficiencia. Retorno financiero y conocimiento adquirido requieren evaluaciones separadas.

Cuota: medir capacidad observada y consumo compartido con los 63 jobs/día propuestos sin extrapolar de Team/tokens ni inventar mensajes semanales. No afirmar margen sostenible cuando solo se completó un smoke. Registrar carga, tools, client/model/plan, límites/reset sanitizados si disponibles y uso externo concurrente declarado; no inferir una tarifa API de esos contadores.

## 3. Estimación orientativa desde Team (no Plus)

Wave 04 mean por turn: mínimo 37.901 s, Skill 42.451 s; muestra pequeña/contexto sintético, no SLA. A 40 jobs secuenciales: **25.267 min vs 28.301 min** de tiempo de servicio orientativo/día, no tiempo real de cola. A 63 jobs: **39.796 vs 44.574 min**. El promedio no estima p95 ni concurrencia/quota/auth. Un job de 128 KiB o patrón de tools distinto no tiene esa distribución probada. Una única cola secuencial es candidata suficiente **para probar**, no elección de scheduler.

Separar llegada, espera, servicio y recepción/admisión; latencia total incluye cola/retries. Registrar p50/p95/max empíricos por rol/tamaño si hay N suficiente, sin generalizar 2 repeticiones. Burst propuesto: 3 jobs shadow+pedagogy juntos con deadlines por job; validar backlog sin perder manifest ni coalescer snapshots obligatorios. Concurrencia>1 solo se investiga si la cola medida no basta; no justificar multiagentes con promedio aislado.

## 4. Matriz de aceptación por finalista

Todo criterio below es propuesto y debe quedar asociado a fixture/hash/observación. `SELECTED=NO` en toda la cohorte. C-010 y C-025a no son dos modelos: el primero es workflow base sin Skill; el segundo transporte nativo. Las cuatro Skills se prueban sobre ese transporte; usar la misma evidencia no implica repetir todos los casos en cada superficie.

| Candidato / disposición recomendada | Evidencia Team reutilizable | Criterio independiente del plan antes de selección | Exclusivo/delta Plus |
|---|---|---|---|
| C-010 mínimo — REUSE_AS_IS base | Wave 04: 10 turnos, baseline válido; wave 06 contratos focalizados | Contrato confiable y outputs/materiales útiles sin Skill, misma allowlist, sin efecto financiero; comparar valor/complejidad | GP1 entitlement y superficie real; smoke/estructura/tools, tamaño, cuota/latencia y recuperación. Desktop directo no fue benchmark Team: ensayo propio de ruta si se elige |
| C-025a app-server native — WRAP candidato | Wave 04/06 inferencia/login Team, discovery y entrega; versión CLI fijada | Protocol/version pin, job IDs, no fallback pago, tool allowlist, evidencias fuera de chat; recovery real aún no probado | GP1–7 en cuenta Plus: native auth, disponibilidad/refresh/expiración/revocación por método permitido, tools, persistencia/restart/quota/capacidad. Sin leer/exportar token |
| C-029 Codex SDK — WRAP candidato dentro de misma familia | 1 smoke Python Team, 7/7 checks, public Apache-2.0, CLI override explícito; TS solo metadata | Preferir transporte existente si cubre roles/snapshots/structured output/tools/state; high-level dynamic tool callbacks y full Skills no probados. No construir RPC propio sin gap | Mismo GP1–7 de ruta activa, con Skill/tool smoke y tamaño/estado/cuota; no sumar pruebas de wrappers idénticos ni inferir paridad Python/TS |
| C-017a research idea — ADAPT/PORT del método | Wave 04 falsifier/PIT, un error tipo; wave 06 schema corregido | 100% hechos/citas elegibles en fixtures críticos; fuente futura/inyectada no obtiene autoridad, sin cartera; hipótesis falsable y siguiente test | Discovery/activación Skill, modelo/herramienta/contexto que cambie comportamiento, cuota WL-R research; solo regresión afectada |
| C-017b thesis shadow — ADAPT/PORT del método | Wave 04 HOLD/abstain; wave 06 OPEN toy/lineage | Canonical action/target qty/notional, input clocks/hash pareado, no Champion visible, abstain/failure no HOLD; ausencia de acceso financiero técnico en D-027/034 | Carga Skill + 26 snapshots/day perfil WL-R, timing y coverage; recuperación de job y entrega; no backtest ni evaluación de autoridad B |
| C-024 pedagogy — ADAPT propio | Wave 04 partial fill/UNKNOWN y pregunta; wave 06 causa ausente | Report per trade, daily/weekly/glossary/map/export y conceptos §55, causa factual vs UNKNOWN; cifras/trace verificadas, complete contract spec; producción educativa pendiente | Skill/tools disponibles, lectura de artefactos, auth/state/recovery, cuota/ventanas de reports en WL-R; no repetir curriculum completo por entitlement |
| C-028 quant review — ADAPT propio | Wave 04 train/OOS/cost/retry, wave 06 schema | No holdout leakage/promoción; ledger gross/net/dataset/splits/missing tests, falsifier/prereg; cálculos solo verificados; engine R-009 distinto | Skill/context/tools y carga quant semanal/background; delta modelo/herramientas material exige regresión focalizada |

`PORT` describe traslado del activo Anthropic; disposición principal **ADAPT**, pues elimina autoridad y cambia PIT/output. No `REUSE_AS_IS` del bundle financiero original. C-027 MCP reserva: si hace falta integración real, prueba host/tool/auth/permissions before finalista; stdio mock 13 checks no lo cierra. C-026 Data/otros plugins reserva: primero necesidad/entitlement/licencia, luego pequeño probe específico; no agregarlos al gate para fabricar trabajo.

## 5. Matriz transversal / prueba de estados

| ID | Criterio medible | Evidencia ahora / pendiente |
|---|---|---|
| AC-01 | Caller elige rol/schema; localizado/override/extra intent rechazados | Wave 05 + negativos wave 06; sandbox real D-027 pendiente |
| AC-02 | Snapshot/hash/corte iguales, FUTURE/UNKNOWN no eligible; revisión as-of | ADR-004 + wave 06 spine; corpus completo/datasets reales D-022/033 pendiente |
| AC-03 | OBSERVED fields intactos, DERIVED unidades/inputs/formulas exactos; errores rechazados | Wave 06 Decimal/jsonschema; fórmulas riesgo D-035 separadas |
| AC-04 | OPEN/INCREASE/REDUCE/CLOSE/HOLD/ABSTAIN canónicos; missing no HOLD | Especificado shadow; OPEN toy/negativos wave 06; cartera general pending R-026 |
| AC-05 | tool failure máximo preregistrado y no invención; timeout/late/no-output/duplicate auditables | Wave 04/06 + clasificación offline; durable recovery/auth real GP5/D-025/026 |
| AC-06 | Citas y causalidad pedagógica verificadas, no sizing reason inventada ni cancel ack falso | Team B4 + wave 06; completa suite reports/learning P2 pendiente |
| AC-07 | Mismo contexto/cálculo/admission replay iguales; variación generativa explícita | Waves 04/06; no promesa determinismo LLM |
| AC-08 | WL-R con contexto representativo, deadlines, cuotas compartidas, recovery y trazabilidad completa | **No ejecutado**; especificado, GP6 target y workload definitivo Strategy V1 pendiente |
| AC-09 | Adquisición método gratuita, ningún fallback API gasto, licencia/versiones/costos por fase | ADR-007/008 + assets pinned; evolución/versiones antes de freeze |
| AC-10 | No broker secrets/endpoint/permission; intent y config write no alcanzables | Harness sintético sí; aislamiento real, red team y aprobación D-027/034 pendientes |

## 6. Resultado de gate y economía

Registrar PASS/PARTIAL/FAIL/UNKNOWN por criterio con datos, no un único available boolean. Para **aceptación Plus** exige GP1–7 + workload suficiente de la ruta activa; no significa READY FOR IMPLEMENTATION ni selección final D-020/024. Fallo -> distinguir límite de entitlement, quota, modelo, integración/estado, demanda o herramienta. Mantener datos/research/modelos pagados como referencias LIVE/excepción PAPER con comparación, nunca activar billing para corregirlo.

`PAPER_V1_VIABLE_FREE=UNKNOWN` runtime hasta gate; `PAPER_V1_COST` potencial 0 incremental dentro de Plus existente + coste local/tiempo por medir; `LIVE_COST=UNKNOWN` fijo/variable/mensual/escala; `FREE_ALTERNATIVE` Codex directo/mínimo y métodos portados, viabilidad por probar; `PAID_INCREMENTAL_VALUE` continuidad/capacidad/datos de calidad como hipótesis; `ECONOMIC_JUSTIFICATION_REQUIRED=YES` antes de gasto. Skills/métodos públicos/propios adquisición 0; comprar metodología no permitido. No tokens→dinero/cuota. Perfil menor solo viable si satisface requisitos reales aprobados de Strategy V1, no porque sea gratuito.
