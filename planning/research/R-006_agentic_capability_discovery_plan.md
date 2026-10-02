# R-006 — Agentic Capability Discovery y Build-vs-Reuse

**Fecha:** 2026-10-01. **Estado:** `RESEARCHING`, P0. **Decisiones:** D-020 (investigación de capacidades) y D-024 (arquitectura agéntica/runtime, `OPEN`). **Alcance aprobado:** [ADR-007](../decisions/ADR-007-r006-openai-anthropic-plus-scope.md). **Límite:** `implementation_locked=true`; este plan solo autoriza documentación y probes desechables.

## 1. Pregunta de diseño

¿Cuál es la mejor arquitectura agéntica para Trading OS que podemos diseñar con **OpenAI/Codex en una cuenta ChatGPT Plus individual objetivo** y activos públicos gratuitos/reutilizables de Anthropic? Debe cubrir investigación cuantitativa y fundamental, propuestas shadow, explicación pedagógica, evaluación y auditoría sin dar autoridad financiera a un agente. La selección de runtime, topología, Skills, plugins, MCP, subagentes y estructura del Trading OS Plugin queda **abierta**. Codex sirve al Plan Architect en el entorno de investigación; eso no lo selecciona ni verifica su entitlement en el runtime Plus objetivo.

## 2. Alcance por responsabilidad

| Trabajo | Necesidad y límite | Candidatos iniciales a contrastar |
|---|---|---|
| Plan Architect/Guardian | investigación con fuentes, cambios trazables, revisión | Codex, Skills disponibles y plugins read-only de OpenAI |
| Quant/Strategy Research | hipótesis falsables, datos PIT, backtest reproducible, sesgos y OOS | Codex/Skills OpenAI, contenido público Anthropic; LEAN/NautilusTrader se evalúan aparte como motores quant |
| Equity/portfolio research | filings, earnings, valoración, tesis, escenarios y fuentes | Anthropic Financial Services y Skills; OpenAI herramientas de análisis/cookbooks; conectores financieros; APIs directas |
| Portfolio Manager shadow | propuesta estructurada, contexto pareado, aislamiento y comparación hipotética | Codex/Skills OpenAI y plantillas públicas Anthropic adaptables; **sin** TradeIntent operativo |
| Pedagogical Agent | explicación factual ligada a trazas, incertidumbre, currículo y verificación | Skills de documentos/visualización, templates de investigación, trazas/evals, generación de material didáctico |
| Conectores de datos | lectura autorizada, PIT, linaje, licencia, coste, frescura | MCP read-only, APIs oficiales, broker/market/alternative-data; R-007/008/021/025 alimentan R-006 |
| Riesgo/ejecución | evaluación determinística y gateway protegido | librerías de esquema/política y broker SDKs sujetos a ADR-006; **ningún** plugin/MCP/LLM recibe autoridad genérica de orden |

**Frontera de investigación:** para la capa de IA/agentes solo OpenAI y Anthropic. Se inspeccionan OpenAI Skills, Plugins/Apps, Codex, MCP orientados a agentes y capacidades financieras incluidas; Agents SDK y API con **clave facturada** se estudian como `REFERENCE_ONLY` Tier 2. [Sign in with ChatGPT para uso del plan](https://developers.openai.com/siwc/token-sharing-open-source) se examina por separado como ruta Tier 0/1 condicional, sin presumir entitlement ni equivalencia con Agents SDK. Se inspeccionan Skills, prompts, templates, reference agents y workflows públicos de Anthropic para `PORT / ADAPT / REFERENCE_ONLY` sin Claude runtime. Google ADK, Microsoft Agent Framework, LangGraph, PydanticAI y otros labs/frameworks agénticos salen de R-006. R-007/008/009/021/025 mantienen separados brokers, datos, motores quant e infraestructura.

**Filtro económico [ADR-008](../decisions/ADR-008-economic-policy-by-phase.md):** PAPER V1 prioriza Tier 0/1 de la **cuenta Plus individual objetivo** o activos públicos/locales con calidad suficiente. Tier 2 puede estudiarse y registrarse como alternativa PAPER excepcional o futura LIVE, sin facturación; aprobar contratación/gasto explícitamente antes de cualquier probe facturable. LIVE considera valor material y economía unitaria, no solo precio. Skills/templates se adquieren gratis/incluidos/propios; sus dependencias se presupuestan aparte. Plus no incluye automáticamente consumo de OpenAI API.

**Dos entornos de evidencia:** `CURRENT_RESEARCH_ENVIRONMENT` = sesión actual de planificación con indicador observado `planType=team`; `TARGET_RUNTIME_ENVIRONMENT` = cuenta ChatGPT Plus **individual** de PAPER V1. Para capacidades dependientes del plan, reportar `AVAILABLE_IN_RESEARCH_ENVIRONMENT` y `AVAILABLE_IN_TARGET_PLUS` por separado. Un `YES` actual deja `AVAILABLE_IN_TARGET_PLUS=UNKNOWN` sin evidencia específica de Plus. Acceso a un archivo público y activación de una Skill en el runtime son hechos distintos.

## 3. Método y entregables

1. **Inventario verificable:** catálogo por capacidad y responsabilidad, versión/fecha, fuente primaria, licencia y dependencias. Separar lo visible en documentación, el código público, lo instalado, lo conectable y lo accesible con nuestra cuenta; un catálogo público no prueba acceso operativo.
2. **Fichas y scorecard:** registrar `EXISTS`, `AVAILABLE_IN_RESEARCH_ENVIRONMENT`, `AVAILABLE_IN_TARGET_PLUS`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE`, `SELECTED` con evidencia y Tier. `SELECTED=NO` hasta ADR. Distinguir contenido público de ejecución incluida en Plus y de API facturada. Una disposición final debe ser `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT`; mientras falte prueba, `PENDING`.
3. **Probes prioritarios antes de elegir:** conservar input, versión y resultado de cada prueba desechable. Registrar Skills/plugins visibles aquí como disponibilidad **solo de investigación**; contrastar documentación Plus y, cuando sea posible, la cuenta Plus objetivo. Importar/adaptar `SKILL.md` público en sandbox documental; MCP con datos sintéticos y permisos solo lectura; comparar rutas OpenAI/Codex Tier 0/1 sobre fixtures iguales; probar bloqueo de órdenes, prompt injection, trazabilidad y replay. No llamar API de pago.
4. **Comparativa económica y de operación:** entitlement **en Plus objetivo**, licencia y [seis campos económicos](../economic_scorecard.md), fijo/variable/mensual/escala, calidad, datos/infraestructura, integración, mantenimiento y lock-in por fase. Un SDK público ni prueba Team demuestran disponibilidad Plus; Tier 2 queda fuera de ejecución/selección paga PAPER sin aprobación, pero se estudia su valor futuro LIVE.
5. **Recomendación por capacidad:** matriz conservar/adaptar/portar/wrap/reference/build/reject con justificación y alternativas. Producir paquete D-020 y, después del gate, paquete D-024 con topología/runtime/plugin propuestos para gobierno humano. Actualizar `capability_landscape.md`, `build_vs_reuse.md`, `risk_register.md` y los contratos afectados.

## 4. Fixtures de comparación previstas

| Fixture desechable | Criterio medible |
|---|---|
| Filing y noticia con `event_at`, `published_at`, `ingested_at` distintos y texto que intenta dar órdenes | Citas verificables; disponibilidad PIT respetada; ninguna llamada a broker/TradeIntent |
| Hipótesis de estrategia con datos sintéticos y holdout marcado | Regla reproducible, separación research/OOS, detección de look-ahead y costes explícitos |
| Snapshot de cartera con dos señales y reserva concurrente simulada | `ShadowPortfolioProposal` con esquema, fuentes, versión y timestamp; aislamiento de ruta operativa; razones de divergencia reconstruibles |
| Traza de riesgo/orden con rechazo, parcial y cancelación incierta | Explicación pedagógica factual, incertidumbre explícita, sin causalidad inventada ni alteración de políticas |
| Caída o timeout de herramienta y reanudación | Replay/correlación de trazas, sin doble acción, coste y latencia registrados |

Comparar rutas viables **dentro de Tier 0/1**: Codex/Skills nativos, adaptación de contenido público Anthropic, MCP/plugin OpenAI limitado y ruta SIWC/Codex app-server **solo si supera entitlement/coste/operación**. Documentar Agents SDK/API con clave como referencia arquitectónica Tier 2, sin ejecución facturable. LEAN/NautilusTrader se comparan en R-009 como motores quant. No usar datos reales ni credenciales de broker en probes de arquitectura.

## 5. Agent Capability Gate para D-024

R-006 se considera **suficientemente maduro para preparar una decisión**, no necesariamente cerrado, solo cuando:

- el mapa de responsabilidades PAPER V1 tiene candidato reutilizable o explicación evidenciada de ausencia por cada capacidad mayor, incluido Pedagogical y Portfolio Manager shadow;
- los candidatos finalistas Tier 0/1 tienen fuente primaria actual, versión, licencia/portabilidad, disponibilidad específica del **TARGET_RUNTIME_ENVIRONMENT** y, cuando sea necesario, probe empírico allí, coste incremental y ruta de salida documentados; `UNKNOWN` crítico impide selección;
- se han ejecutado y registrado probes prácticos de finalistas cuando técnicamente posibles, y las imposibilidades (entitlement/red/coste) están documentadas;
- se ha probado o especificado un test negativo independiente para acceso a órdenes, secreto de broker, conversión shadow→intent y promoción no autorizada; la política escrita de una Skill no cuenta como barrera técnica;
- el scorecard compara al menos dos enfoques Tier 0/1 viables para orquestación y research, o justifica por qué solo uno supera el filtro; incluye alternativa mínima Codex/Skills y registra valor/coste LIVE de opciones pagas relevantes; ningún Tier 2 se ejecuta/selecciona para PAPER con gasto sin aprobación ADR-008;
- se han revisado duplicidades, lock-in, costes, fallos, prompt injection y dependencias con D-008/011/021/022/027/029/034;
- el paquete D-020 identifica disposiciones finales por capacidad y un reviewer crítico comprueba contradicciones. Solo entonces D-024 puede pasar a `READY_FOR_DECISION`; cerrarlo y congelar la arquitectura agéntica requiere decisión material y gobierno humano. Ningún gate desbloquea implementación por sí mismo.

## 6. Primera cola de investigación profunda

1. **OpenAI Plus/Codex:** inventario empírico de Skills/Apps/plugins/MCP y herramientas en **cuenta Plus objetivo**. Probar, sin pagos, workflow documental, salida estructurada, trazas y permisos. API con clave/Agents SDK son `REFERENCE_ONLY` Tier 2; SIWC/Codex app-server es candidato condicional distinto. El [alcance documentado de guardrails](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) sirve para diseñar límites, no para seleccionar runtime.
2. **Anthropic Financial Services:** inspeccionar `equity-research`, `market-researcher`, `earnings-reviewer`, plantillas/Skills y conectores. Probar portabilidad de una Skill de research y una de explicación a formato OpenAI/Codex; identificar instrucciones que sugieren acciones de cartera y retirarlas para PAPER V1. [Repositorio oficial](https://github.com/anthropics/financial-services).
3. **MCP orientado a agentes:** probar conectores disponibles en Codex y mocks read-only de fuente pública con datos sintéticos, timestamps y prompt injection. Conectores financieros premium son Tier 2 y se registran solo como referencia; su evaluación de dataset/precio corresponde a R-025.
4. **Comparación OpenAI/Codex:** Skill nativa, Skill Anthropic adaptada y workflow mínimo en Codex sobre fixtures idénticas; evaluar permisos, auditabilidad y operación sin instalar frameworks agénticos externos.
5. **Quant/Pedagogy/Shadow:** LEAN/NautilusTrader en R-009; en R-006, Skills de investigación, documentos/visualización, trazas y esquemas para Pedagogical y Shadow. Probes compartidos antes de recomendar `BUILD`.

**Evidencia acumulada:** inventario [R-006 inicial](R-006_initial_findings_2026-10-01.md), [wave 01](R-006_probe_wave_01_2026-10-01.md), [wave 02](R-006_probe_wave_02_2026-10-02.md) y [elegibilidad oficial Plus por superficie](R-006_plus_entitlement_evidence_2026-10-02.md). La segunda solo validó formato de Skill adaptada y fixture temporal; la documentación confirma Codex base, pero no el flujo específico de Skills/plugins en la cuenta Plus objetivo. Faltan conducta del modelo y probe allí. No se seleccionó runtime, framework, Skill, plugin, MCP ni proveedor.
