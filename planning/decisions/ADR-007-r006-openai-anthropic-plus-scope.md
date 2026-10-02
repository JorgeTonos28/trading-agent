# ADR-007 — Alcance y presupuesto de Agentic Capability Discovery

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
| 2 — excluido por defecto | OpenAI API con facturación separada, Anthropic API/Claude Managed Agents, suscripciones adicionales, herramientas empresariales, conectores financieros premium y gasto recurrente adicional. |

Un Tier 2 solo reabre consideración si no hay alternativa razonable Tier 0/1, la capacidad es material, se documentan coste y beneficio, y el propietario aprueba expresamente **considerar** el gasto. Esa aprobación no selecciona todavía producto ni autoriza implementación. ChatGPT Plus y OpenAI API tienen facturación separada; la existencia del Agents SDK/API no prueba disponibilidad económica bajo Plus. Su documentación puede servir de `REFERENCE_ONLY` sin llamar la API ni generar cargos. La prioridad de Anthropic es **contenido Apache-2.0 público** — Skills, prompts, templates, reference agents, workflows y metodologías — para `PORT`, `ADAPT` o `REFERENCE_ONLY` dentro de OpenAI/Codex, verificando dependencias y licencias de terceros. Claude/Anthropic runtime no se presupone.

**Aclaración investigativa, 2026-10-01:** la exclusión Tier 2 aplica a la ruta OpenAI API **con clave/facturación separada**. La documentación oficial describe una ruta distinta, [Sign in with ChatGPT para uso del plan](https://developers.openai.com/siwc/token-sharing-open-source), para ciertas aplicaciones open source/locales y solicitudes elegibles. R-006 la evaluará como hipótesis Tier 0/1 condicionada a entitlement Plus, límites y operación; ni su existencia ni la sesión actual prueban viabilidad para PAPER V1. Véase [probe wave 01](../research/R-006_probe_wave_01_2026-10-01.md).

**Aclaración de entornos, 2026-10-02, por instrucción del propietario:** `CURRENT_RESEARCH_ENVIRONMENT` es la sesión de planificación actual, cuyo indicador observado fue `planType=team`; sus capacidades pueden ser superiores y **solo sirven como evidencia de investigación**. `TARGET_RUNTIME_ENVIRONMENT` es una **cuenta ChatGPT Plus individual** y gobierna el diseño y presupuesto de PAPER V1. Cada ficha de capacidad dependiente del plan debe distinguir `AVAILABLE_IN_RESEARCH_ENVIRONMENT` de `AVAILABLE_IN_TARGET_PLUS`. Si un probe funciona aquí pero no existe evidencia específica para Plus, el segundo campo permanece `UNKNOWN`. Documentación sobre elegibilidad de Plus y acceso empírico en la cuenta objetivo son evidencias diferentes; la primera no prueba que la configuración exacta de Skills, plugins, herramientas o cuotas funcione allí. Pruebas de activos públicos independientes del plan pueden continuar.

## Límite de la decisión

La restricción de proveedores agénticos no elimina R-007 brokers, R-008 market data, R-025 Smart Money/alternative data, R-009 motores quant como LEAN/NautilusTrader, ni almacenamiento e infraestructura técnica. Esas líneas conservan sus propios gates. El filtro económico Tier 0/1 sí orienta todas las opciones PAPER V1; cualquier gasto recurrente Tier 2 sigue la excepción anterior.

D-024 permanece `OPEN` bajo el Agent Capability Gate de [R-006](../research/R-006_agentic_capability_discovery_plan.md). No se ha elegido runtime, topología, Skill final, plugin, MCP, broker, proveedor, Strategy V1 ni política numérica. `implementation_locked=true`.
