# R-006 — Agentic Capability Discovery y Build-vs-Reuse

**Vigencia aprobada — 2026-10-13, ADR-014 / propietario:** `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` en el alcance capacidades/roles/fronteras/integración B-RT1. `design_status=DESIGN_DECIDED`; `TARGET_ACCEPTANCE_DEFERRED`; `PAPER_RUNTIME_ACCEPTED=false`; `implementation_locked=true`. Un Runner, control confiable externo, core/secretos fuera AI, aislamiento/contexto mínimo por job, allowlists, identidad/lifecycle por attempt y admisión/audit externos son el contrato aprobado. Keyring, HOME readonly, token, desktop, IPC carrier y launch exactos son **mecanismos candidatos sustituibles**, no invariantes irreversibles; cambios preservan fronteras/autoridad con evidencia y gobierno correspondiente. R-030 acepta eficacia en Plus/PC personal. Investigación agéntica fundamental Team completada; no expandir R-006/010/013 por refinamiento indefinido. LIVE UNKNOWN; residuos H7 conservados sin evasión de policy.


> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Antecedente ADR-011 — 2026-10-05:** propietario aprobó opción A y disposiciones RC2 como dirección de diseño PAPER: núcleo financiero local determinístico always-on + jobs Codex Team automáticos por evento/calendario, sin aprobación por job rutinario. D-020 DECIDED únicamente en dirección Build-vs-Reuse; versiones/permisos/runtime final siguen D-024 RESEARCHING. No implementación, gasto, capacidad sostenida ni autoridad financiera adicional. Plus permanece PRE-LIVE.


**Hito histórico previo a aprobación ADR-011 — wave07:** [RC2 Team](R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

**Antecedente — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Siguiente paquete activo:** hardening P1 de dirección ADR-011, frontera material de seguridad ADR-012 y gates de runtime pendientes. SDK/Skills/recovery/carga acotada y propuesta comparativa anteriores ya tienen evidencia; no repetir discovery entera. Las secciones fechadas de waves y endpoints anteriores son históricas y no exigen acceso Plus.

**Fecha:** 2026-10-01. **Estado:** `RESEARCHING`, P0. **Decisiones:** D-020 (investigación de capacidades) y D-024 (arquitectura agéntica/runtime, `OPEN`). **Alcance aprobado:** [ADR-007](../decisions/ADR-007-r006-openai-anthropic-plus-scope.md). **Límite:** `implementation_locked=true`; este plan solo autoriza documentación y probes desechables.

## 1. Pregunta y alcance vigentes

¿Qué arquitectura agéntica PAPER podemos diseñar con OpenAI/Codex en Team actual y métodos públicos/propios de Anthropic, sin autoridad financiera LLM? Solo OpenAI/Anthropic en IA/agentes. Brokers/datos/quant/infra se investigan aparte. Tier 0/1 preferido; API facturada no incluida por suscripción y sin gasto autorizado. LIVE sigue economía ADR-008.

## 2. Método vigente

Inventario por rol, EXISTS / AVAILABLE_IN_RESEARCH_ENVIRONMENT / AVAILABLE_IN_PAPER_TEAM / AVAILABLE_IN_FUTURE_PLUS / TECHNICALLY_COMPATIBLE / ECONOMICALLY_REASONABLE / SELECTED. Exigir versiones/licencias/permisos/inputs/outputs y probes relevantes antes de selección. Disposiciones REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT, por fase. SELECTED=NO hasta gobierno.

Reutilizar waves 04–06, MCP mock, activos Anthropic pinados, smoke SDK y R-028 bootstrap. Team evidencia ahora aplica al target PAPER en rutas probadas. No repetir comparación completa ni exigir Plus. Investigar gaps oficiales SDK/Skills/tools; recovery rehidratado desde repo/snapshot; corpus y carga acotada Team; documentar fallos, aislamiento observado y amenazas no resueltas.

## 3. Entregables y endpoint

- Gate [Team TP](R-006_team_runtime_acceptance_RC0.md) y EB por etapa; protocolos/resultados; matriz de madurez y propuesta arquitectura/capacidades.
- Contratos confiables por rol, shadow/pedagogía y caller determinístico externo; núcleo local always-on + jobs Codex Team intermitentes permanece candidato.
- Comparativa económica, coste incremental/no billing y fallbacks con limitaciones.
- Paquete material revisable D-020/D-024; detenerse cuando siguiente paso requiera gobierno de arquitectura/permisos, no por resumen informativo. Revisión independiente crítica antes de freeze, no simularla con auto-review.
- DoR exige arquitectura/contratos/seguridad/bootstrap de preparación seleccionados y protocolos. Operación sostenida/integración financiera implementada P2 antes de PAPER; Plus gate P3 R-029 tras PAPER validado.

## Historia conservada — método y protocolo anteriores

## 1. Pregunta de diseño

¿Cuál es la mejor arquitectura agéntica para Trading OS que podemos diseñar con **OpenAI/Codex en Team actual para PAPER (ADR-010)** y activos públicos gratuitos/reutilizables de Anthropic? Debe cubrir investigación cuantitativa y fundamental, propuestas shadow, explicación pedagógica, evaluación y auditoría sin dar autoridad financiera a un agente. La selección de runtime, topología, Skills, plugins, MCP, subagentes y estructura del Trading OS Plugin queda **abierta**. Codex sirve al Plan Architect en el entorno de investigación; eso no lo selecciona ni verifica su entitlement en el runtime Plus objetivo.

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

**Filtro económico [ADR-008](../decisions/ADR-008-economic-policy-by-phase.md):** PAPER V1 prioriza Tier 0/1 de la **cuenta Team actual objetivo PAPER** o activos públicos/locales con calidad suficiente. Tier 2 puede estudiarse y registrarse como alternativa PAPER excepcional o futura LIVE, sin facturación; aprobar contratación/gasto explícitamente antes de cualquier probe facturable. LIVE considera valor material y economía unitaria, no solo precio. Skills/templates se adquieren gratis/incluidos/propios; sus dependencias se presupuestan aparte. Plus no incluye automáticamente consumo de OpenAI API.

**Dos entornos de evidencia:** `CURRENT_RESEARCH_ENVIRONMENT` = sesión actual de planificación con indicador observado `planType=team`; `PAPER_RUNTIME_ENVIRONMENT` = Team actual de PAPER V1; Plus individual es candidato PRE-LIVE. Para capacidades dependientes del plan, reportar `AVAILABLE_IN_RESEARCH_ENVIRONMENT` y `AVAILABLE_IN_TARGET_PLUS` por separado. Un `YES` actual deja `AVAILABLE_IN_TARGET_PLUS=UNKNOWN` sin evidencia específica de Plus. Acceso a un archivo público y activación de una Skill en el runtime son hechos distintos.

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
- los candidatos tienen fuente primaria actual, versión, licencia/portabilidad, coste incremental, dependencias y ruta de salida documentados; una shortlist condicional admite `AVAILABLE_IN_TARGET_PLUS=UNKNOWN`. La selección final requiere el Plus Acceptance Gate, sin repetir la investigación conductual Team;
- se han ejecutado y registrado probes prácticos de finalistas cuando técnicamente posibles, y las imposibilidades (entitlement/red/coste) están documentadas;
- se ha probado o especificado un test negativo independiente para acceso a órdenes, secreto de broker, conversión shadow→intent y promoción no autorizada; la política escrita de una Skill no cuenta como barrera técnica;
- el scorecard compara al menos dos enfoques Tier 0/1 viables para orquestación y research, o justifica por qué solo uno supera el filtro; incluye alternativa mínima Codex/Skills y registra valor/coste LIVE de opciones pagas relevantes; ningún Tier 2 se ejecuta/selecciona para PAPER con gasto sin aprobación ADR-008;
- se han revisado duplicidades, lock-in, costes, fallos, prompt injection y dependencias con D-008/011/021/022/027/029/034;
- el paquete D-020 identifica disposiciones finales por capacidad y un reviewer crítico comprueba contradicciones. Solo entonces D-024 puede pasar a `READY_FOR_DECISION`; cerrarlo y congelar la arquitectura agéntica requiere decisión material y gobierno humano. Ningún gate desbloquea implementación por sí mismo.

## 6. Primera cola de investigación profunda

1. **OpenAI/Codex:** inventario y comparación conductual en Team ahora; aceptación de Skills/Apps/plugins/MCP y herramientas en **cuenta Plus objetivo** solo para finalistas después. Probar, sin pagos, workflow documental, salida estructurada, trazas y permisos. API con clave/Agents SDK son `REFERENCE_ONLY` Tier 2; SIWC/Codex app-server es candidato condicional distinto. El [alcance documentado de guardrails](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) sirve para diseñar límites, no para seleccionar runtime.
2. **Anthropic Financial Services:** inspeccionar `equity-research`, `market-researcher`, `earnings-reviewer`, plantillas/Skills y conectores. Probar portabilidad de una Skill de research y una de explicación a formato OpenAI/Codex; identificar instrucciones que sugieren acciones de cartera y retirarlas para PAPER V1. [Repositorio oficial](https://github.com/anthropics/financial-services).
3. **MCP orientado a agentes:** probar conectores disponibles en Codex y mocks read-only de fuente pública con datos sintéticos, timestamps y prompt injection. Conectores financieros premium son Tier 2 y se registran solo como referencia; su evaluación de dataset/precio corresponde a R-025.
4. **Comparación OpenAI/Codex:** Skill nativa, Skill Anthropic adaptada y workflow mínimo en Codex sobre fixtures idénticas; evaluar permisos, auditabilidad y operación sin instalar frameworks agénticos externos.
5. **Quant/Pedagogy/Shadow:** LEAN/NautilusTrader en R-009; en R-006, Skills de investigación, documentos/visualización, trazas y esquemas para Pedagogical y Shadow. Probes compartidos antes de recomendar `BUILD`.

**Evidencia acumulada:** inventario [R-006 inicial](R-006_initial_findings_2026-10-01.md), [wave 01](R-006_probe_wave_01_2026-10-01.md), [wave 02](R-006_probe_wave_02_2026-10-02.md) y [elegibilidad oficial Plus por superficie](R-006_plus_entitlement_evidence_2026-10-02.md). La segunda solo validó formato de Skill adaptada y fixture temporal; la documentación confirma Codex base, pero no el flujo específico de Skills/plugins en la cuenta Plus objetivo. La conducta Team se completa en waves 04/05 (§8); falta aceptación del entorno Plus solo para finalistas. No se seleccionó runtime, framework, Skill, plugin, MCP ni proveedor.

**Wave 03 y gate:** [protocolo read-only](R-006_probe_wave_03_2026-10-02.md) valida discovery efímero en Team, no activación del modelo/Plus. Usar [gate Plus RC0](R-006_plus_runtime_gate_RC0.md) para la siguiente evidencia del entorno objetivo; la falta de esa cuenta no bloquea pruebas conductuales Team ni shortlist. El gate se aplica después a finalistas y reutiliza la evidencia de comportamiento. Una alternativa paga se estudia con ADR-008, sin gastar ni sustituir evidencia Plus.

## 7. Protocolo aprobado de avance — 2026-10-05

La evidencia se divide en **conducta/diseño (Team)** y **aceptación del entorno (Plus individual)**. Se ejecutan comparaciones Skill vs workflow mínimo con el mismo modelo, tareas, contratos, fixtures, tools y schema; la Skill es la diferencia experimental. PIT, linaje, estructura, inyección, fallos, calidad, shadow, pedagogía y repetibilidad se investigan ahora. Registrar barreras del harness separadas de obediencia del modelo, resultados fallidos incluidos, métricas predefinidas y revisión cualitativa con limitaciones. No gastar en APIs ni instalar Skills de producción.

La primera shortlist es una recomendación condicional, no cierre D-020/D-024 ni selección. Plus verifica únicamente disponibilidad, activación, entitlement, cuotas, herramientas, autenticación, persistencia/recovery y suficiencia operacional. Un cambio material de modelo/herramienta puede requerir regresión focalizada, no repetir toda R-006.

Se compara también la alternativa abierta **núcleo local/determinístico always-on + capa Codex/Plus intermitente**. Champion, señales operativas, Risk Engine y ejecución mantienen A+/G1+G2; research, shadow y pedagogía no se convierten en requisito LLM permanente por defecto. Una ausencia de agente puede degradar esas capacidades; no autoriza una orden, reanudación material o promoción. El contrato completo de pedagogía sigue requerido antes del DoD PAPER V1.

## 8. Hito de evidencia — 2026-10-05

[Wave 04](R-006_probe_wave_04_2026-10-05.md): veinte turnos Team, mínimo vs cuatro procedimientos explícitos, PIT/inyección/quant/shadow/pedagogía/fallos/repetibilidad; calibración fallida preservada. [Wave 05](R-006_probe_wave_05_2026-10-05.md): MCP SDK local, metadata/permiso/licencia plugins, activos Earnings/Audit/Calendar y schema por trusted role. [Shortlist RC0](R-006_shortlist_RC0.md) alcanza evidencia suficiente para cohorte condicional, no madurez final/selección. D-020 RESEARCHING, D-024 OPEN. Lo pendiente de Plus solo aplica a finalistas; contratos/snapshots/workload pueden continuar en Team.

## 9. Paquete autónomo RC0 pasos 1–2 — completado 2026-10-05

La [shortlist RC1](R-006_shortlist_RC1.md) es recomendación actual. [Contratos](../06_agent_evidence_contract_RC0.md) por rol, PM shadow y pedagogía completa propuestos; [workload/matriz](R-006_workload_acceptance_RC0.md) WL-L/R/S y GP1–7 especificados. [Wave 06](R-006_probe_wave_06_2026-10-05.md) prueba role/lineage/qty/cause/failure focalizados y conserva enmienda del checker (8/10 v1, 10/10 v2); no superioridad universal de Skills. [Codex SDK](R-006_codex_sdk_findings_2026-10-05.md) nativo prueba transporte público 7/7 checks, diferente de Agents SDK/API; no tool callbacks/recovery/Plus probados.

Madurez: suficiente para propuesta de dirección/cohorte de aceptación, **no** para cerrar D-020/D-024. Endpoint del paquete solicitado alcanzado después de persistir/commit/push. Siguiente intervención: dirección arquitectónica candidata material y acceso Plus para aceptación limitada. No marcar todo Preparation bloqueado: Strategy V1/plataformas/datos, threat model/revisión independiente e integración financiera/pedagógica siguen su backlog; un gate Plus no los sustituye. No ampliar frameworks, gastar, implementar o congelar.

## Adenda vigente — Environment Bootstrap / Portability

ADR-009 registra aprobación de cohorte candidata RC1, no selección final. Antes de Plus, R-028/D-037 P1 añade inventario/perfiles/paquetes y ruta reproducible fresh clone sin memoria Team. D-024/DoR no cierran sin contrato y evidencia de bootstrap. Procedimientos manuales/programáticos comparten assets; no una sesión por rol obligatoria. [Protocolo R-028](R-028_bootstrap_probe_protocol.md).

## P1 posterior ADR-011 — reuse y fronteras

[Paquete R-010–014](R-010_014_hardening_findings_2026-10-05.md): official SDK/CLI0.160 bundle default probado; wrapper no propio RPC. Seguridad candidata reutiliza controles Windows por dominio (S2), VM reserva; permisos no aprobados. Temporal baseline vs APScheduler/OS investigados como **workflow determinístico**, fuera del límite de frameworks IA; SQLite solo probe, no selección storage. No BUILD motor/audit framework antes de necesidad demostrada. D-024 abierto; R-006 método suficiente para dirección aprobada, capacidad/operación pendiente.

## S2 approval y paquete de cierre P1

ADR-012 dirección S2 aprobada. [S2 RC1](../08_S2_isolation_spec_RC1.md)/[SI-BL-RB](R-013_S2_acceptance_matrix_RC1.md) separan security/blinding/runtime reproducibility. Capability Discovery conserva dispositions ADR-011; native OS controls REUSE/WRAP, no sandbox propio. Preflight/7 observaciones son diseño, no effective acceptance. Próximo gobierno [ADM-01](R-013_S2_administrative_gate_ADM01.md) cuentas/ACL sintéticas; egress/IPC/auth pending, D-024 RESEARCHING; Plus PRE-LIVE.

## Gate S2 revisado — 2026-10-06

[Comparativa A/B/S3](R-013_S2_variants_comparison_2026-10-06.md) y [RC2](../08_S2_agent_domain_contract_RC2.md) proponen **Agent Runner común con contextos efectivos por job**, sin cuenta obligatoria por rol. No cambiar disposiciones D-020/ADR-011 ni congelar D-024. **ADM-01 DEFERRED/NOT_AUTHORIZED**, no próximo gate: Q-051 dirección candidata revisada antes de laboratorio nuevo. AC10/10 es semántica, no TP4/EB/SI/BL/RB efectivo ni TP6 capacidad bajo permisos. Plus PRE-LIVE, PAPER Team, futuros native auth/egress/cache/recovery/workload pendientes.

## Endpoint S2-B y evidencia adicional — 2026-10-06

Dirección S2-B aprobada; Q-051 DECIDED en ese alcance. [Laboratorio mínimo S2B-ADM-01](R-013_S2B_lab_ADM01.md), Q-052 DECIDED únicamente en autorización temporal **AUTHORIZED_OWNER_ADMIN_ONLY**. [Runbook por fases](R-013_S2B_owner_execution_runbook.md). Setup/login pendientes de acciones manuales del propietario; no permisos PAPER finales. [Dossier](R-013_S2B_lab_preparation_2026-10-06.md) y fuentes distinguen memoria12+privilegios2, sintaxis14 y preflight readonly de **FS/thread/native NOT_TESTED**. Grant común/tránsito/default DACL se incluyen en VP04/LF09, con positivos adecuados. Setup aún no ejecutado; no retry bajo BASE para operaciones de job. Full process/IPC/egress/auth/cache/recovery/TP6 y SI17/BL9/RB5/VP8 pendientes; ningún gate efectivo se pasa por estos contadores. R-006 madura diseño, D-020 conserva aprobación, D-027/D-024 siguen RESEARCHING. ADM-01 tres cuentas DEFERRED; PAPER Team y Plus PRE-LIVE.
