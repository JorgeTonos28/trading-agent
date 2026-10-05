# ADR-007 — Alcance y presupuesto de Agentic Capability Discovery

**Vigencia actual — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](../research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

- **Fecha:** 2026-10-01.
- **Estado:** `DECIDED` por instrucción explícita del propietario; acota R-006/D-020 y condiciona D-024.
- **Prioridad:** P0. **Implementación:** bloqueada.

## Decisión

R-006 investigará **solo OpenAI y Anthropic** para Skills, plantillas/agentes de referencia, workflows, plugins, MCP orientados a agentes y runtimes de IA. Su pregunta rectora es: «¿Cuál es la mejor arquitectura agéntica para Trading OS con OpenAI/Codex bajo ChatGPT Plus y activos gratuitos/reutilizables de Anthropic?». Quedan fuera del comparativo agéntico PAPER V1 Google ADK, Microsoft Agent Framework, LangGraph, PydanticAI y otros AI Labs/frameworks de agentes. Las menciones anteriores son historial de candidatos, no investigación activa.

La preferencia económica PAPER V1 es:

| Tier | Regla |
|---|---|
| 0 — preferido | Capacidad incluida en **la cuenta ChatGPT Plus individual objetivo** o contenido público/open source que se pueda usar, portar o adaptar sin pago incremental. |
| 1 — evaluable | Servicio gratuito con límites, cuenta gratuita o componente open source ejecutable localmente sin coste relevante. |
| 2 — ejecución paga sin autorización | OpenAI API con facturación separada, Anthropic API/Claude Managed Agents, suscripciones adicionales, enterprise, conectores premium y gasto adicional; investigación documental permitida, sin contratación ni consumo facturable. |

**Aclaración económica 2026-10-02 — [ADR-008](ADR-008-economic-policy-by-phase.md):** se pueden estudiar y registrar alternativas Tier 2 sin permiso adicional. Contratar, activar facturación o generar gasto incremental exige aprobación explícita. PAPER prioriza cero/bajo coste; LIVE compara valor y economía unitaria. Una brecha material de calidad/fiabilidad puede justificar estudiar pago aun si existe una opción gratuita; no se descarta tecnología futura solo por precio. ChatGPT Plus y OpenAI API tienen facturación separada; Agents SDK/API públicos no prueban entitlement Plus. `REFERENCE_ONLY` por presupuesto PAPER no es disposición definitiva LIVE. Anthropic prioriza contenido público Apache-2.0 para `PORT/ADAPT/REFERENCE_ONLY`, verificando licencias/dependencias. Skills/templates no se compran; sus runtimes/datos pueden justificar coste aparte en fases posteriores.

**Aclaración investigativa, 2026-10-01:** la exclusión Tier 2 aplica a la ruta OpenAI API **con clave/facturación separada**. La documentación oficial describe una ruta distinta, [Sign in with ChatGPT para uso del plan](https://developers.openai.com/siwc/token-sharing-open-source), para ciertas aplicaciones open source/locales y solicitudes elegibles. R-006 la evaluará como hipótesis Tier 0/1 condicionada a entitlement Plus, límites y operación; ni su existencia ni la sesión actual prueban viabilidad para PAPER V1. Véase [probe wave 01](../research/R-006_probe_wave_01_2026-10-01.md).

**Aclaración de entornos, 2026-10-02, por instrucción del propietario:** `CURRENT_RESEARCH_ENVIRONMENT` es la sesión de planificación actual, cuyo indicador observado fue `planType=team`; sus capacidades pueden ser superiores y **solo sirven como evidencia de investigación**. `TARGET_RUNTIME_ENVIRONMENT` es una **cuenta ChatGPT Plus individual** y gobierna el diseño y presupuesto de PAPER V1. Cada ficha de capacidad dependiente del plan debe distinguir `AVAILABLE_IN_RESEARCH_ENVIRONMENT` de `AVAILABLE_IN_TARGET_PLUS`. Si un probe funciona aquí pero no existe evidencia específica para Plus, el segundo campo permanece `UNKNOWN`. Documentación sobre elegibilidad de Plus y acceso empírico en la cuenta objetivo son evidencias diferentes; la primera no prueba que la configuración exacta de Skills, plugins, herramientas o cuotas funcione allí. Pruebas de activos públicos independientes del plan pueden continuar.

## Límite de la decisión

**Aclaración 2026-10-05, instrucción del propietario:** se autorizan pruebas conductuales/comparativas bajo Team independientes del entitlement (PIT, calidad, inyección, trazabilidad, estructura, shadow, pedagogía, aislamiento, repetibilidad y fallos). No disponer de la cuenta Plus objetivo no bloquea R-006 ni una shortlist condicional. Team demuestra comportamiento/diseño en la configuración ensayada, nunca disponibilidad Plus. Los finalistas pasan después un Plus Acceptance Gate de acceso, activación, cuotas, herramientas, autenticación, persistencia/recovery y suficiencia operacional. Se reutilizan los resultados conductuales; solo diferencias concretas de entorno justifican regresiones focalizadas. `AVAILABLE_IN_TARGET_PLUS=UNKNOWN` cuando corresponda. D-020 sigue `RESEARCHING` y D-024 `OPEN`.

Se conserva explícitamente como alternativa **abierta** el núcleo local/determinístico siempre activo y Codex/Plus como capa agéntica intermitente de research, shadow, análisis y pedagogía. La autonomía de un Champion aprobado no requiere por definición un LLM permanente. No se selecciona aquí topología, runtime ni stack y no cambia A+, G1+G2 o el gateway financiero.

La restricción de proveedores agénticos no elimina R-007 brokers, R-008 market data, R-025 Smart Money/alternative data, R-009 motores quant como LEAN/NautilusTrader, ni almacenamiento e infraestructura técnica. Esas líneas conservan sus gates y aplican ADR-008: Tier 0/1 primero en PAPER, valor económico en LIVE y autorización antes de gastar.

D-024 permanece `OPEN` bajo el Agent Capability Gate de [R-006](../research/R-006_agentic_capability_discovery_plan.md). No se ha elegido runtime, topología, Skill final, plugin, MCP, broker, proveedor, Strategy V1 ni política numérica. `implementation_locked=true`.

**Evidencia posterior 2026-10-05:** [shortlist RC1](../research/R-006_shortlist_RC1.md) completa paquete autónomo de contratos/workload y regresión Team, con [Codex SDK C-029](../research/R-006_codex_sdk_findings_2026-10-05.md) como candidato nativo gratuito de transporte. No es Agents SDK/API facturada; disponibilidad del archivo no acredita inferencia Plus. D-020/D-024 siguen abiertos; no se cambia el alcance aprobado ni se ejecuta Plus Gate sin cuenta objetivo. La Autonomous Continuation Rule de AGENTS exige continuar hitos hasta endpoint real o input humano, con commit/push; no modifica autoridad financiera.
