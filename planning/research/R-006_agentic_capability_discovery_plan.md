# R-006 — Agentic Capability Discovery y Build-vs-Reuse

**Fecha:** 2026-10-01. **Estado:** `RESEARCHING`, P0. **Decisiones:** D-020 (investigación de capacidades) y D-024 (arquitectura agéntica/runtime, `OPEN`). **Límite:** `implementation_locked=true`; este plan solo autoriza documentación y probes desechables. El propietario ordenó este foco después de aprobar D-012/ADR-006.

## 1. Pregunta de diseño

¿Qué capacidades existentes pueden cubrir con calidad verificable los trabajos de PAPER V1 — investigación cuantitativa y fundamental, fuentes externas, estrategia, propuestas de cartera shadow, explicación pedagógica, evaluación y auditoría — sin dar autoridad financiera a un agente? La selección de runtime, topología, Skills, plugins, MCP, subagentes y estructura del Trading OS Plugin queda **abierta**. Codex puede servir al Plan Architect hoy sin que eso lo seleccione como runtime operativo.

## 2. Alcance por responsabilidad

| Trabajo | Necesidad y límite | Candidatos iniciales a contrastar |
|---|---|---|
| Plan Architect/Guardian | investigación con fuentes, cambios trazables, revisión | Codex, Skills disponibles, plugins read-only, otros agentes de desarrollo |
| Quant/Strategy Research | hipótesis falsables, datos PIT, backtest reproducible, sesgos y OOS | Skills de research, Agents SDK/API, LangGraph, Google ADK, Microsoft Agent Framework, LEAN/NautilusTrader, bibliotecas estadísticas |
| Equity/portfolio research | filings, earnings, valoración, tesis, escenarios y fuentes | Anthropic Financial Services y Skills; OpenAI herramientas de análisis/cookbooks; conectores financieros; APIs directas |
| Portfolio Manager shadow | propuesta estructurada, contexto pareado, aislamiento y comparación hipotética | modelos + salida estructurada/evals de frameworks; plantillas de portfolio research como referencia; **sin** TradeIntent operativo |
| Pedagogical Agent | explicación factual ligada a trazas, incertidumbre, currículo y verificación | Skills de documentos/visualización, templates de investigación, trazas/evals, generación de material didáctico |
| Conectores de datos | lectura autorizada, PIT, linaje, licencia, coste, frescura | MCP read-only, APIs oficiales, broker/market/alternative-data; R-007/008/021/025 alimentan R-006 |
| Riesgo/ejecución | evaluación determinística y gateway protegido | librerías de esquema/política y broker SDKs sujetos a ADR-006; **ningún** plugin/MCP/LLM recibe autoridad genérica de orden |

La evaluación debe incluir OpenAI Skills, Plugins/Apps, Codex, Agents SDK/API/Responses, MCP y capacidades financieras; Anthropic Financial Services, Skills/templates/connectors/workflows y su portabilidad; otros AI Labs; open source; frameworks cuantitativos; broker APIs; market data y alternative data. El foco inicial es el diseño agéntico; R-007/008/021/025 profundizan brokers y datasets y vuelcan sus hallazgos en el catálogo.

## 3. Método y entregables

1. **Inventario verificable:** catálogo por capacidad y responsabilidad, versión/fecha, fuente primaria, licencia y dependencias. Separar lo visible en documentación, el código público, lo instalado, lo conectable y lo accesible con nuestra cuenta; un catálogo público no prueba acceso operativo.
2. **Fichas y scorecard:** para cada candidato relevante registrar exactamente `EXISTS`, `AVAILABLE_TO_US`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE`, `SELECTED` como `YES/NO/PARTIAL/UNKNOWN` con evidencia. `SELECTED=NO` hasta ADR. Evaluar permisos, datos enviados, portabilidad, mantenimiento, coste total y salida. Una disposición final debe ser `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT`; mientras falte prueba, escribir `PENDING`, no inventar selección.
3. **Probes prioritarios antes de elegir:** conservar input, versión y resultado de cada prueba desechable. Probar instalación/importación y esquema de salida sin secretos; `SKILL.md` financiero portado solo en sandbox documental; MCP con datos sintéticos y permisos solo lectura; agentes/frameworks con la misma fixture; bloqueo de llamadas a orden, prompt injection, trazabilidad y replay. Un SDK instalado o un ejemplo que corre no demuestra adecuación financiera.
4. **Comparativa económica y de operación:** coste de modelo/API, datos/licencias, infraestructura, integración, mantenimiento y migración; disponibilidad para esta cuenta/región. Donde no haya cotización o entitlement, `UNKNOWN` y solicitud específica antes de seleccionar.
5. **Recomendación por capacidad:** matriz conservar/adaptar/portar/wrap/reference/build/reject con justificación y alternativas. Producir paquete D-020 y, después del gate, paquete D-024 con topología/runtime/plugin propuestos para gobierno humano. Actualizar `capability_landscape.md`, `build_vs_reuse.md`, `risk_register.md` y los contratos afectados.

## 4. Fixtures de comparación previstas

| Fixture desechable | Criterio medible |
|---|---|
| Filing y noticia con `event_at`, `published_at`, `ingested_at` distintos y texto que intenta dar órdenes | Citas verificables; disponibilidad PIT respetada; ninguna llamada a broker/TradeIntent |
| Hipótesis de estrategia con datos sintéticos y holdout marcado | Regla reproducible, separación research/OOS, detección de look-ahead y costes explícitos |
| Snapshot de cartera con dos señales y reserva concurrente simulada | `ShadowPortfolioProposal` con esquema, fuentes, versión y timestamp; aislamiento de ruta operativa; razones de divergencia reconstruibles |
| Traza de riesgo/orden con rechazo, parcial y cancelación incierta | Explicación pedagógica factual, incertidumbre explícita, sin causalidad inventada ni alteración de políticas |
| Caída o timeout de herramienta y reanudación | Replay/correlación de trazas, sin doble acción, coste y latencia registrados |

Comparar primero una solución mínima sin framework, OpenAI Agents SDK/API, LangGraph y una opción de otro AI Lab en los **mismos** casos si acceso y licencia lo permiten. LEAN/NautilusTrader se comparan como motores quant, no se confunden con autoridad de agente. No usar datos reales ni credenciales de broker en probes de arquitectura.

## 5. Agent Capability Gate para D-024

R-006 se considera **suficientemente maduro para preparar una decisión**, no necesariamente cerrado, solo cuando:

- el mapa de responsabilidades PAPER V1 tiene candidato reutilizable o explicación evidenciada de ausencia por cada capacidad mayor, incluido Pedagogical y Portfolio Manager shadow;
- los candidatos finalistas tienen fuente primaria actual, versión, licencia/portabilidad, disponibilidad de cuenta, coste razonable estimado y ruta de salida documentados; `UNKNOWN` crítico impide selección;
- se han ejecutado y registrado probes prácticos de finalistas cuando técnicamente posibles, y las imposibilidades (entitlement/red/coste) están documentadas;
- se ha probado o especificado un test negativo independiente para acceso a órdenes, secreto de broker, conversión shadow→intent y promoción no autorizada; la política escrita de una Skill no cuenta como barrera técnica;
- el scorecard compara al menos dos enfoques viables para runtime/orquestación y para research, o justifica por qué solo uno supera el filtro; incluye alternativa mínima;
- se han revisado duplicidades, lock-in, costes, fallos, prompt injection y dependencias con D-008/011/021/022/027/029/034;
- el paquete D-020 identifica disposiciones finales por capacidad y un reviewer crítico comprueba contradicciones. Solo entonces D-024 puede pasar a `READY_FOR_DECISION`; cerrarlo y congelar la arquitectura agéntica requiere decisión material y gobierno humano. Ningún gate desbloquea implementación por sí mismo.

## 6. Primera cola de investigación profunda

1. **OpenAI local/SDK/API:** inventario real de Skills/Apps/Codex/MCP; comparar Agents SDK frente a Agents API/Responses y opción mínima. Probar tool boundaries, salida estructurada, trazas/evals, costes y permisos. El [alcance documentado de guardrails](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) exige validación al lado de cualquier efecto.
2. **Anthropic Financial Services:** inspeccionar `equity-research`, `market-researcher`, `earnings-reviewer`, plantillas/Skills y conectores. Probar portabilidad de una Skill de research y una de explicación a formato OpenAI/Codex; identificar instrucciones que sugieren acciones de cartera y retirarlas para PAPER V1. [Repositorio oficial](https://github.com/anthropics/financial-services).
3. **MCP de datos financieros:** comparar conectores de Anthropic/LSEG/S&P/FactSet y APIs directas con R-025; hacer probe solo lectura con datos públicos/sintéticos primero, verificar entitlements, PIT, licencia y scope antes de acceso real.
4. **Frameworks competidores:** LangGraph, Google ADK, Microsoft Agent Framework, PydanticAI y enfoque mínimo; evaluación de estado, recuperación, tool permissions, auditabilidad y operación. No elegir por popularidad.
5. **Quant/Pedagogy/Shadow:** LEAN/NautilusTrader y bibliotecas de análisis para Quant; herramientas de documentos/visualización y trazas para pedagogía; esquemas/evals para Shadow. Probes compartidos antes de recomendar BUILD.

**Resultado de esta apertura:** inventario y probes preliminares en [R-006 inicial](R-006_initial_findings_2026-10-01.md). No se seleccionó runtime, framework, Skill, plugin, MCP ni proveedor.
