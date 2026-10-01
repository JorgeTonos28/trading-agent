# Capability Landscape — plantilla de investigación inicial

Estado 2026-10-01: **investigación parcial**, sin selección. No interpretar una mención como confirmación de disponibilidad, compatibilidad, licencia o precio. Método completo en [R-006](research_backlog.md).

Actualización 2026-10-01: comenzó la verificación de fuentes primarias para OpenAI y Anthropic. `SELECTED=false` para todos los candidatos; acceso real a servicios de terceros, costes y licencia de cada componente siguen `UNKNOWN`. Las fichas iniciales están abajo.

| Familia | Candidatos a verificar (no seleccionados) | Caso de uso / evidencia requerida |
|---|---|---|
| OpenAI Skills | Skills del entorno, públicas y propias | Procedimientos de research, documentos, análisis; formato, portabilidad, licencia y evals |
| OpenAI Plugins/Apps | Plugins y apps accesibles a esta cuenta | Fuentes/acciones disponibles, permisos, costes, residencia de datos |
| Codex | Herramientas de repositorio, tareas, modelos, automatizaciones | Rol de Plan Architect/Guardian; límites de runtime y audit trail |
| MCP | Servidores de datos, research, broker y almacenamiento | Autenticación, lectura/escritura, permisos, mantenimiento y prompt injection |
| OpenAI Agents / finanzas | Agents SDK y capacidades financieras/de análisis existentes | Orquestación, tracing, guardrails, evaluaciones; confirmar ofertas actuales |
| Anthropic Financial Services | Skills, templates, connectors, agent workflows y reference agents | Licencia, dependencia de Claude, portabilidad de contenido/workflow y controles |
| Otros AI Labs | Soluciones publicadas pertinentes | Evidencia de disponibilidad, licencia, lock-in y valor incremental |
| Open source agent/workflow | LangGraph, Temporal y alternativas | Recovery, estado, evals, complejidad operativa |
| Quant frameworks | LEAN, NautilusTrader, vectorbt, Backtrader, librerías estadísticas | PIT, semántica de órdenes, coste, licencia, reproducibilidad |
| Broker APIs | Alpaca, IBKR, Tradier, tastytrade, TradeStation y otros | Elegibilidad RD, paper/live, orden/stream, reconciliación y límites |
| Market data | Broker-native, Databento, Massive, Nasdaq Data Link, Tiingo, Alpha Vantage y otros | Históricos, ajustes, timestamps, derechos, calidad y coste |
| Smart Money / alternative data | Congreso, SEC Form 4, 13F/hedge funds, unusual options, block/dark pool, analyst revisions, fund flows; Quiver, Unusual Whales, Capitol Trades, SEC/EDGAR y otros | API, historia, publicación PIT, licencia, latencia, calidad y utilidad por dataset; [R-025](research/smart_money_data_landscape.md) |

## Ficha obligatoria por candidato

`ID; capability; source/version/date; primary-source URL; EXISTS; AVAILABLE_TO_US; TECHNICALLY_COMPATIBLE; ECONOMICALLY_REASONABLE; SELECTED; license/portability; permissions; data sent; lifecycle/maintenance; alternatives; test; disposition; ADR`. Valores iniciales `UNKNOWN`, salvo existencia del candidato como mención en la hoja. La decisión de disposición se registra en un futuro `build_vs_reuse.md` con fundamento; inicialmente ninguna está clasificada.

## Fichas verificadas parcialmente — 2026-10-01

| ID | Capacidad | EXISTS | AVAILABLE_TO_US | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED | Hallazgo y siguiente prueba |
|---|---|---|---|---|---|---|---|
| C-001 | OpenAI Agents SDK | Sí | SDK público; acceso API de esta cuenta no comprobado | Pendiente | Pendiente | No | [Documentación oficial](https://developers.openai.com/api/docs/guides/agents/sdk): orquestación en app propia con tools, MCP, handoffs, tracing; el servidor conserva deployment, storage y aprobaciones. Probar límites de guardrails y coste contra llamadas directas. |
| C-002 | OpenAI Skills/Plugins/MCP | Sí | Skills del entorno presentes; publicación/conexión de plugin propio no comprobada | Pendiente | Pendiente | No | [Skills](https://developers.openai.com/plugins/build/skills) codifican workflow; [plugin packaging](https://developers.openai.com/plugins/build/plugins) agrupa skills/MCP. Evaluar formato portátil, permisos y si basta Skill sin MCP. |
| C-003 | OpenAI Agent guardrails/human review | Sí | API de esta cuenta no comprobada | Parcial: no sustituye risk gateway | Pendiente | No | [Guía oficial](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals): guardrails de agente no cubren automáticamente todo tool call; validar el efecto en el límite de cada tool. Risk Engine permanece determinístico. |
| C-004 | Anthropic financial-services reference agents | Sí | Repositorio público; servicio Claude/Managed Agents no comprobado | Pendiente de portabilidad | Pendiente | No | [Repositorio oficial](https://github.com/anthropics/financial-services): agentes, Skills, conectores y wrappers; declara que son para borradores con revisión humana y no ejecutan transacciones. Revisar licencia por componente, dependencia de Cowork/Managed Agents y utilidad para research/pedagogía. |
| C-005 | Anthropic Agent Skills públicas | Sí | Repositorio público; runtime de nuestra cuenta no comprobado | Pendiente de portabilidad | Pendiente | No | [Repositorio oficial](https://github.com/anthropics/skills): estructura `SKILL.md` y ejemplos. Auditar licencia y scripts individuales antes de portar. |
| C-006 | OpenAI multi-agent portfolio cookbook | Sí | Página pública; ejecución/API no comprobada | Parcial: workflow de research solamente | Pendiente | No | [Cookbook oficial](https://developers.openai.com/cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration) marcado **archivado y posiblemente obsoleto**. Ejemplo de colaboración macro/fundamental/quant y herramientas, útil como referencia metodológica; no prueba alpha, seguridad de ejecución ni adecuación de modelos/APIs actuales. |
| C-007 | OpenAI Skills como workflow | Sí | Documentación pública; Skill local posible | Parcial: investigación/pedagogía, no autoridad financiera | Pendiente | No | [Documentación oficial](https://developers.openai.com/plugins/concepts/skills): Skill empaqueta instrucciones/recursos; MCP aporta datos y acciones. Evaluar ADAPT para procedimientos, sin equiparar instrucciones a control de broker. |
| C-008 | OpenAI Agents SDK como runtime | Sí | SDK público; acceso/coste de cuenta no comprobados | Parcial: loop, tools, handoffs y tracing; gateway externo requerido | Pendiente | No | [Documentación oficial](https://developers.openai.com/api/docs/guides/agents/sdk): la aplicación controla deployment, estado, tools y aprobaciones. Candidato a WRAP/ADAPT tras comparación R-010. |
| C-009 | Guardrails/approvals de Agents SDK | Sí | Documentación pública; disponibilidad de ejecución no comprobada | Parcial: alcance por entrada, salida o herramienta | Pendiente | No | [Documentación oficial](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals): los guardrails no cubren automáticamente todas las llamadas en cadenas; la autorización financiera debe verificarse en el límite de ejecución. |

**Inferencia inicial:** los workflows de equity research de Anthropic pueden aportar métodos de investigación; su propio alcance publicado no cubre estrategia cuantitativa operativa, risk gateway ni ejecución. Los plugins de OpenAI separan instrucciones de Skills y acceso controlado de MCP, compatible conceptualmente con el invariante del proyecto, pero falta probar la frontera real de permisos. Ningún hallazgo justifica incorporar o instalar un componente todavía.

R-025 abrió fichas preliminares para [Quiver](https://api.quiverquant.com/), [Unusual Whales](https://unusualwhales.com/developers), [Capitol Trades](https://www.capitoltrades.com/about-us) y [SEC/EDGAR](https://www.sec.gov/about/developer-resources), además de candidatos por descubrir. Las ofertas declaradas por proveedor solo prueban existencia aparente; no confirman disponibilidad para esta cuenta, historia PIT, derechos o selección.
