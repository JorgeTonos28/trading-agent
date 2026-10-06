# Capability Landscape — plantilla de investigación inicial

**Vigencia ADR-011 — 2026-10-05:** propietario aprobó opción A y disposiciones RC2 como dirección de diseño PAPER: núcleo financiero local determinístico always-on + jobs Codex Team automáticos por evento/calendario, sin aprobación por job rutinario. D-020 DECIDED únicamente en dirección Build-vs-Reuse; versiones/permisos/runtime final siguen D-024 RESEARCHING. No implementación, gasto, capacidad sostenida ni autoridad financiera adicional. Plus permanece PRE-LIVE.


**Hito histórico previo a aprobación ADR-011 — wave07:** [RC2 Team](research/R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

## Matriz vigente PAPER Team — ADR-010

EXISTS=YES en todos los candidatos siguientes; SELECTED=NO. Los resultados específicos Team ahora son aplicables al target PAPER, sin convertirlos en seguridad/cuota sostenida probada. AVAILABLE_IN_FUTURE_PLUS=UNKNOWN para activación/runtime dependientes del plan; acceso a código público no equivale a runtime disponible.

| Capacidad | AVAILABLE_IN_PAPER_TEAM | Compatibilidad / economía PAPER | Disposición recomendada / siguiente evidencia |
|---|---|---|---|
| C-010 Codex base | YES ruta CLI nativa probada | YES fixtures; consumo de cupo existente, continuidad UNKNOWN | REUSE_AS_IS; TP carga/recovery |
| C-025a app-server / C-029 Python SDK | YES inferencia/Skills/callbacks SDK low-level wave07; contexto restart, no durable recovery | YES integración sintética, PARTIAL producción; código libre y login nativo, sin API billing | WRAP transporte oficial; no runtime propio por defecto |
| C-017a research idea | YES procedimiento probado | ADAPT método Apache-2.0; adquisición 0 | ADAPT / PORT metodología, outputs PIT |
| C-017b shadow thesis | YES procedimiento probado | ADAPT método; aislamiento financiero real pendiente | ADAPT / PORT, shadow sin autoridad |
| C-024 pedagogía / C-028 quant | YES procedimientos probados | Métodos propios 0; informes completos/integración pendientes | ADAPT; no garantía de superioridad sobre mínimo |
| C-030 discovery / C-031 bootstrap | YES CLI fixture/fresh clone | PARTIAL por superficie/recovery; assets locales 0 | REUSE_AS_IS / ADAPT, Team EB/TP |
| C-027 MCP / C-026 Data plugin | MCP mock YES, host real UNKNOWN; Data entitlement ambiguo por superficie | No necesarios por defecto; licencia/Data proprietary | WRAP reserva / REFERENCE_ONLY; no PORT propietario |
| Agents SDK, APIs y Managed Agents | Código público/servicio existe; no ejecución paga aprobada | Tier 2 separado de Team | REFERENCE_ONLY PAPER; economía LIVE ADR-008 |

## Inventario y resultados históricos conservados

Las tablas fechadas siguientes conservan los ejes Plus originales; no son la disponibilidad PAPER vigente ni sus próximos pasos. La matriz anterior y ADR-010 prevalecen.

**Vigencia actual — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

**Referencia vigente 2026-10-05:** [shortlist RC1](research/R-006_shortlist_RC1.md), [contratos por rol](06_agent_evidence_contract_RC0.md) y [workload/aceptación](research/R-006_workload_acceptance_RC0.md). Paquete autónomo RC0 pasos 1–2 completado; madurez suficiente para propuesta de cohorte/dirección, no final selección. Tablas/notes anteriores conservan evidencia por ola, no reemplazan estado actualizado. D-020 RESEARCHING/D-024 OPEN; todos SELECTED=NO y target Plus operativo UNKNOWN.

Estado 2026-10-05: **shortlist condicional, investigación parcial para selección**, sin selección. R-006/D-020 es P0 y gate de D-024. [ADR-007](decisions/ADR-007-r006-openai-anthropic-plus-scope.md) limita IA/agentes a OpenAI/Anthropic; [ADR-008](decisions/ADR-008-economic-policy-by-phase.md) prioriza Tier 0/1 PAPER y valor económico LIVE, sin descartar pagos del futuro. Estudiar pagos está autorizado; contratar/gastar requiere aprobación. No interpretar una mención como confirmación de acceso, compatibilidad, licencia o precio. Método en [plan R-006](research/R-006_agentic_capability_discovery_plan.md); [inventario/probes](research/R-006_initial_findings_2026-10-01.md).

Actualización 2026-10-02: [ADR-007](decisions/ADR-007-r006-openai-anthropic-plus-scope.md) distingue `CURRENT_RESEARCH_ENVIRONMENT` (esta sesión, `planType=team`, solo investigación) de `TARGET_RUNTIME_ENVIRONMENT` (**ChatGPT Plus individual**, diseño y presupuesto PAPER V1). [Wave 01](research/R-006_probe_wave_01_2026-10-01.md) observó herramientas aquí; [wave 02](research/R-006_probe_wave_02_2026-10-02.md) validó solo formato de Skill adaptada y fixture PIT. La [evidencia documental Plus por superficie](research/R-006_plus_entitlement_evidence_2026-10-02.md) confirma elegibilidad general de Codex y visibilidad del directorio, pero no activación de Skills/plugins concretos. SIWC C-025 sigue condicional. `SELECTED=NO` para todos los candidatos Trading OS.

| Familia | Candidatos a verificar (no seleccionados) | Caso de uso / evidencia requerida |
|---|---|---|
| OpenAI Skills | Skills del entorno, públicas y propias | Procedimientos de research, documentos, análisis; formato, portabilidad, licencia y evals |
| OpenAI Plugins/Apps | Plugins y apps de la cuenta Plus objetivo | Fuentes/acciones disponibles, permisos, costes, residencia de datos; catálogo Team solo evidencia de investigación |
| Codex | Herramientas de repositorio, tareas, modelos, automatizaciones | Rol de Plan Architect/Guardian; límites de runtime y audit trail |
| MCP | Servidores de datos, research, broker y almacenamiento | Autenticación, lectura/escritura, permisos, mantenimiento y prompt injection |
| OpenAI Agents / finanzas | Agents SDK/API con clave como `REFERENCE_ONLY` Tier 2; Codex y SIWC plan usage como rutas Tier 0/1 **por verificar** | Patrones de orquestación, tracing, guardrails, evaluaciones; separar documentación, entitlement, preview y facturación |
| Anthropic Financial Services | Skills, templates, prompts, agent workflows y reference agents públicos | Licencia por archivo, dependencia de Claude y portabilidad `PORT / ADAPT / REFERENCE_ONLY` hacia OpenAI/Codex sin Anthropic runtime |
| Workflow técnico no agéntico | Opciones de persistencia y jobs, fuera de R-006 | Estado y recovery se investigan en infraestructura R-011; no seleccionar runtime agéntico externo |
| Quant frameworks | LEAN, NautilusTrader, vectorbt, Backtrader, librerías estadísticas | PIT, semántica de órdenes, coste, licencia, reproducibilidad |
| Broker APIs | Alpaca, IBKR, Tradier, tastytrade, TradeStation y otros | Elegibilidad RD, paper/live, orden/stream, reconciliación y límites |
| Market data | Broker-native, Databento, Massive, Nasdaq Data Link, Tiingo, Alpha Vantage y otros | Históricos, ajustes, timestamps, derechos, calidad y coste |
| Smart Money / alternative data | Congreso, SEC Form 4, 13F/hedge funds, unusual options, block/dark pool, analyst revisions, fund flows; Quiver, Unusual Whales, Capitol Trades, SEC/EDGAR y otros | API, historia, publicación PIT, licencia, latencia, calidad y utilidad por dataset; [R-025](research/smart_money_data_landscape.md) |

## Ficha obligatoria por candidato

`ID; capability; source/version/date; primary-source URL; cost_tier; EXISTS; AVAILABLE_IN_RESEARCH_ENVIRONMENT; AVAILABLE_IN_TARGET_PLUS; TECHNICALLY_COMPATIBLE; ECONOMICALLY_REASONABLE; SELECTED; license/portability; permissions; data sent; lifecycle/maintenance; alternatives; test; disposition_by_phase; ADR; PAPER_V1_VIABLE_FREE; PAPER_V1_COST; LIVE_COST; FREE_ALTERNATIVE; PAID_INCREMENTAL_VALUE; ECONOMIC_JUSTIFICATION_REQUIRED`. Valores iniciales `UNKNOWN` salvo evidencia. Un `YES` en investigación no se copia a Plus. Para activos públicos distinguir acceso al archivo de activación del runtime. ADR-008 permite estudiar Tier 2, pero ejecución paga PAPER exige aprobación; LIVE se evalúa por valor. La disposición se registra en `build_vs_reuse.md`; ninguna queda seleccionada.

## Fichas verificadas parcialmente — 2026-10-01

| ID | Capacidad | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_TARGET_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED | Evidencia / siguiente prueba |
|---|---|---|---|---|---|---|---|---|
| C-001 | OpenAI Agents SDK | YES | YES: código público | YES: código público; inferencia con API key fuera de Plus | PARTIAL: gateway externo obligatorio | NO para PAPER V1 con API key: Tier 2 | NO | [SDK](https://developers.openai.com/api/docs/guides/agents/sdk) `REFERENCE_ONLY`; no probe facturable. |
| C-002 | OpenAI Skills/Plugins/MCP | YES | YES: Skills visibles aquí | UNKNOWN para configuración y acceso concretos en Plus | PARTIAL: formato documentado | UNKNOWN para Plus | NO | [Evidencia por superficie](research/R-006_plus_entitlement_evidence_2026-10-02.md): directorio visible entre planes; Skill/plugin concreto y MCP pendientes de probe Plus. |
| C-003 | OpenAI Agent guardrails/human review | YES | YES: documentación pública; runtime sin probe | YES: documentación pública; uso API con clave Tier 2 | PARTIAL: no sustituye risk gateway | NO para ejecución API facturada PAPER V1 | NO | [Guía](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) `REFERENCE_ONLY`. |
| C-004 | Anthropic financial-services reference agents | YES | YES: repositorio público | YES: repositorio público; activación Codex UNKNOWN | PARTIAL: portabilidad por probar | PARTIAL: activo Tier 0, dependencias por auditar | NO | [Repositorio](https://github.com/anthropics/financial-services); Earnings Reviewer usa FactSet/Daloopa; método adaptable, wrapper/conector no asumidos disponibles ([wave 02](research/R-006_probe_wave_02_2026-10-02.md)). |
| C-005 | Anthropic Agent Skills públicas | YES | YES: archivos públicos | YES: archivos públicos; activación Codex UNKNOWN | PARTIAL: portabilidad por probar | PARTIAL: activo Tier 0, licencias por archivo | NO | [Repositorio](https://github.com/anthropics/skills); revisar scripts y dependencias. |
| C-006 | OpenAI multi-agent portfolio cookbook | YES | YES: página pública | YES: página pública; ejecución API Tier 2 | PARTIAL: referencia de research | YES como referencia gratuita | NO | [Cookbook archivado](https://developers.openai.com/cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration), `REFERENCE_ONLY`. |
| C-007 | OpenAI Skills como workflow | YES | YES: documentación pública | YES: documentación pública; activación específica UNKNOWN | PARTIAL: research/pedagogía, sin autoridad | UNKNOWN hasta probe Plus | NO | [Concepto](https://developers.openai.com/plugins/concepts/skills); ChatGPT Personal Skills y Codex Skills tienen [elegibilidad separada](research/R-006_plus_entitlement_evidence_2026-10-02.md); procedimiento ≠ control financiero. |
| C-008 | OpenAI Agents SDK como runtime | YES | YES: código público; no ejecutado | YES: código público; inferencia con API key fuera de Plus | PARTIAL: loop/tools/tracing, gateway externo | NO con API key: Tier 2 | NO | [SDK](https://developers.openai.com/api/docs/guides/agents/sdk), `REFERENCE_ONLY`. |
| C-009 | Guardrails/approvals del SDK | YES | YES: documentación pública | YES: documentación pública; ejecución API Tier 2 | PARTIAL: alcance por tool | NO con API key: Tier 2 | NO | [Guía](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals), `REFERENCE_ONLY`. |
| C-025 | App-server nativo (a) / SIWC plan usage (b) | YES | YES inferencia nativa Team (a); UNKNOWN OAuth (b) | UNKNOWN: entitlement y operación Plus individual | YES fixtures nativas (a); PARTIAL preview (b) | CONDITIONAL: Tier 0/1 por ruta | NO | [Overview](https://developers.openai.com/siwc/token-sharing-open-source), [app-server](https://developers.openai.com/siwc/token-sharing-open-source/codex-app-server), [límites](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations). |

**Inferencia inicial:** los workflows de equity research de Anthropic pueden aportar métodos de investigación; su propio alcance publicado no cubre estrategia cuantitativa operativa, risk gateway ni ejecución. Los plugins de OpenAI separan instrucciones de Skills y acceso controlado de MCP, compatible conceptualmente con el invariante del proyecto, pero falta probar la frontera real de permisos. Ningún hallazgo justifica incorporar o instalar un componente todavía.

R-025 abrió fichas preliminares para [Quiver](https://api.quiverquant.com/), [Unusual Whales](https://unusualwhales.com/developers), [Capitol Trades](https://www.capitoltrades.com/about-us) y [SEC/EDGAR](https://www.sec.gov/about/developer-resources), además de candidatos por descubrir. Las ofertas declaradas por proveedor solo prueban existencia aparente; no confirman acceso del proyecto, historia PIT, derechos o selección. Su acceso API/dataset se verifica separado de cualquier entitlement de plugin/Plus.

## Ficha económica por candidato — PAPER vs LIVE

Aplicar [ADR-008 y scorecard](economic_scorecard.md). Esta tabla inicia campos, **no valida precios ni beneficios**; el detalle fijo/variable/mensual/escala se completa con cotización y workload antes de recomendar pago. `0 contenido` se refiere solo a lectura/adquisición del activo público; no declara gratis runtime, datos ni operación. Las disposiciones `REFERENCE_ONLY` anteriores por presupuesto son PAPER, reevaluables para LIVE. Skills/templates mantienen adquisición gratuita como regla.

| ID/capacidad | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| C-001 SDK público | UNKNOWN para workflow | 0 código; inferencia UNKNOWN | UNKNOWN por uso | C-010/C-025, sin validar | Hipótesis: control del harness; probar frente a Plus | YES si ejecución paga |
| C-002 Skills/Plugins/MCP | UNKNOWN por componente | UNKNOWN; entitlements separados | UNKNOWN | Skill/local read-only candidata | Dependiente de app/datos/runtime, sin demostrar | YES si dependencia paga |
| C-003 guardrails/review API | NO para ruta facturada | 0 docs; API UNKNOWN | UNKNOWN | Aislamiento/gateway determinístico y permisos Codex por evaluar | Controles/evals adicionales a probar; no autoridad financiera | YES si ejecución paga |
| C-004 Anthropic reference agents | PARTIAL: solo activos | 0 método; conectores/runtime UNKNOWN | UNKNOWN dependencias | Fuentes públicas + adaptación candidata | Valorar datos/runtime aparte; no comprar metodología | YES si dependencia paga |
| C-005 Anthropic Skills públicas | PARTIAL: solo activos | 0 adquisición; integración UNKNOWN | UNKNOWN dependencias | ADAPT/PORT gratuito | Valorar datos/runtime aparte | YES si dependencia paga |
| C-006 cookbook portfolio | YES como referencia | 0 lectura; ejecución fuera del probe | UNKNOWN si se ejecutara | Método propio/C-017 | No demostrado; referencia archivada | YES si ejecución paga |
| C-007 workflow Skills OpenAI | UNKNOWN activación Plus | UNKNOWN; docs públicas 0 | UNKNOWN runtime/datos | Procedimiento propio con fixtures | Valor runtime/datos separado del prompt | YES si dependencia paga |
| C-008 SDK como runtime | NO ruta API facturada | UNKNOWN API; fuera de ejecución paga autorizada | UNKNOWN por carga | C-010/C-025, sin validar | Hipótesis: continuidad/control vs cupo Plus; probar | YES |
| C-009 guardrails del SDK | NO ruta API facturada | UNKNOWN inferencia | UNKNOWN | Frontera técnica/gateway + permisos por evaluar | Hipótesis de mejor evaluación/controles, sin demostrar | YES |
| C-010 Codex + Skills | UNKNOWN configuración Plus | Potencial 0 incremental; capacidad/cupo UNKNOWN | UNKNOWN escala | Workflow mínimo Codex candidato | Comparar API/servicio por continuidad y calidad | YES para alternativa paga |
| C-011 OpenAI Developers plugin | UNKNOWN instalación Plus | UNKNOWN; no activar billing API | UNKNOWN | openai-docs/documentación pública | Sin mejora financiera demostrada | YES si ruta paga |
| C-012 SDK público/API | NO ruta API facturada | 0 código; API UNKNOWN | UNKNOWN por uso | C-010/C-025 candidatos | Harness/continuidad como hipótesis | YES |
| C-013 Agents/Responses API key | NO como entitlement Plus | UNKNOWN API | UNKNOWN por uso | C-010/C-025 candidatos | Evaluar control/continuidad y límites, no presumir superioridad | YES |
| C-014 Docs MCP | UNKNOWN integración completa | Endpoint público; cliente UNKNOWN | UNKNOWN mantenimiento | Documentación web oficial | No valor pago demostrado | YES si dependencia paga |
| C-015 cookbook portfolio | YES referencia | 0 lectura | UNKNOWN si se ejecutara | Procedimiento propio/C-017 | No demostrado; no comprar template | YES si ejecución paga |
| C-016 reference templates | PARTIAL: activos públicos | 0 método; datos/runtime UNKNOWN | UNKNOWN | Adaptar fuente pública | Dependencias premium solo si mejoran evidencia/cobertura | YES si dependencia paga |
| C-017 equity research Skills | YES método; activación Plus UNKNOWN, conducta Team probada | 0 adquisición; runtime/datos UNKNOWN | UNKNOWN | Workflow mínimo propio | Mejor datos/runtime a demostrar; template gratuito | YES si dependencia paga |
| C-018 financial MCP | UNKNOWN por proveedor | UNKNOWN; sin suscripción aprobada | UNKNOWN por dataset/uso | SEC/EDGAR y fuentes públicas candidatas | PIT/cobertura/latencia a medir en R-025 | YES |
| C-022 LEAN/NautilusTrader | UNKNOWN workflow/datos | Código público; operación/datos UNKNOWN | UNKNOWN | Motores locales candidatos R-009 | Comparar datos/hosting por fidelidad y continuidad | YES si dependencia paga |
| C-023 broker/data APIs | UNKNOWN por proveedor | UNKNOWN | UNKNOWN | R-007/008/025 | Cobertura/latencia/reconciliación, pendientes de evidencia | YES |
| C-024 Skills pedagógicas | UNKNOWN composición Plus | UNKNOWN; metodología sin compra | UNKNOWN datos/runtime | Markdown/trazas y procedimiento propio | Calidad factual/claridad y continuidad a evaluar | YES si dependencia paga |
| C-025 SIWC/app-server | UNKNOWN gate Plus | Potencial 0 incremental; cupo/operación UNKNOWN | UNKNOWN escala | Codex directo/workflow mínimo candidato | API paga: control/capacidad como hipótesis si Plus insuficiente | YES si alternativa paga |

C-019–021 siguen fuera del alcance agéntico ADR-007; la política económica no reabre su evaluación. Brokers/datos tienen fichas económicas propias y storage/infra/observabilidad adoptan el scorecard común antes de preselección.

**Wave 03 / gate Plus:** [app-server local read-only](research/R-006_probe_wave_03_2026-10-02.md) descubrió C-017 habilitada en raíz temporal con autenticación CLI `team`, sin inferencia ni instalación persistente. Discovery disponible en investigación; activación/comportamiento/Plus siguen `UNKNOWN`. C-010/017 ganan esta subcapacidad probada; C-025 SIWC no recibió OAuth ni inferencia. El [gate Plus RC0](research/R-006_plus_runtime_gate_RC0.md) especifica las evidencias pendientes; `SELECTED=NO` y D-024 OPEN.

## Evidencia conductual y aceptación — 2026-10-05

Team puede probar calidad, PIT, linaje, inyección, estructura, shadow, pedagogía, repetibilidad y fallos para una shortlist condicional. No demuestra entitlement Plus. El [Plus Acceptance Gate RC1](research/R-006_plus_runtime_gate_RC0.md) se reserva a finalistas y diferencias de entorno. Mantener `AVAILABLE_IN_TARGET_PLUS=UNKNOWN` cuando corresponda. Núcleo determinístico local always-on + Codex intermitente sigue alternativa OPEN, sin selección D-024.

## Cohorte actual con evidencia Team — 2026-10-05

[Wave 04](research/R-006_probe_wave_04_2026-10-05.md), [wave 05](research/R-006_probe_wave_05_2026-10-05.md) y [shortlist RC0](research/R-006_shortlist_RC0.md) prevalecen sobre pendientes conductuales de notas históricas. Veinte turnos Team; no extrapolar entitlement/modelo/cuota Plus. `SELECTED=NO` en todos; D-020 RESEARCHING, D-024 OPEN. Compatibilidad es del probe, no producción.

| ID | Capacidad | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_TARGET_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED | Disposición recomendada/evidencia |
|---|---|---|---|---|---|---|---|---|
| C-010 | Codex mínimo/Skills explícitas | YES | YES 20 turnos nativos Team | UNKNOWN configuración/carga | YES fixtures; estado pendiente | CONDITIONAL cupo Plus | NO | REUSE_AS_IS base como benchmark; Skill aporta procedimiento, no garantía; wave 04. |
| C-017a/b | Idea generation / thesis tracker adaptados | YES | YES activación/marker/output Team | YES archivos públicos; UNKNOWN activación | YES limitada; mezcla de output en research | YES método; runtime condicional | NO | ADAPT research/shadow; contexto/PIT/linaje y roles por endurecer. |
| C-024 | Skill factual pedagógica propia de prueba | YES | YES traza/pregunta Team | YES archivo propio; UNKNOWN activación | YES probe B4, DoD completo pendiente | YES método; runtime condicional | NO | ADAPT de métodos/contratos; no currículo completo ni herramientas finales seleccionadas. |
| C-026 | Data analyze-data-quality/validate-data 1.0.11 | YES | YES contenido; UNKNOWN activación por conflicto de superficies | UNKNOWN | PARTIAL método/entitlement | CONDITIONAL inclusión/licencia | NO | REFERENCE_ONLY hoy; licencia Proprietary, no PORT; posible reuse dentro de entitlement después. |
| C-027 | SDK MCP oficial 2.3.0 MIT | YES | YES mock stdio 13 checks | YES código público; UNKNOWN integración host | YES local; host/connector pendientes | YES SDK; datos aparte | NO | WRAP opcional de lectura; no protocolo propio, annotations no ACL. |
| C-028 | Prototipo propio Quant/Strategy Review | YES | YES train/OOS/costes/fallo Team | YES archivo propio; UNKNOWN activación | YES checklist, no backtest | YES método; runtime condicional | NO | ADAPT de protocolo research/PIT, engine en R-009. |

C-025a nativo existente está probado para estas fixtures Team; C-025b SIWC OAuth no se probó. C-011 Developers sigue no instalado; Data catálogo instalado contradice inspector ChatGPT not_installed. No resolver conflictos por suposición. Fuentes/métodos Anthropic Earnings/Audit/Calendar son reservas ADAPT, wrappers/conectores premium REFERENCE_ONLY PAPER; disponibles como archivos, no como servicios por descargarlos.

| Nueva capacidad | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| C-026 Data | UNKNOWN inclusión/licencia Plus | 0 solo si incluido; no comprar Skill | UNKNOWN plan/servicio | Checklists propios y métodos públicos | Tools extra/calidad por probar | YES si dependencia paga |
| C-027 SDK MCP | YES código; UNKNOWN workflow host | 0 licencia; local/operación no cuantificados | Software 0, hosting/datos/ops UNKNOWN | Tool dinámica/API directa | Posible connector operativo/fiable, sin probar | YES si servicio incremental |
| C-028 Quant Review | YES método; UNKNOWN runtime Plus | Método 0; inferencia/datos/local aparte | Método 0; runtime/datos UNKNOWN | Workflow mínimo con contrato común | Datos/runtime mejores, no compra de Skill | YES si dependencia paga |

Fichas económicas y lock-in/salidas/carga por cohorte en [shortlist §3](research/R-006_shortlist_RC0.md). La adquisición gratuita de un método no prueba coste cero del sistema ni fiabilidad; no hubo billing API/contratación aprobado.

## Contratos/workload y transporte reutilizable — estado vigente posterior

[Wave 06](research/R-006_probe_wave_06_2026-10-05.md): 10 turnos con schema por trusted role y quantity/lineage/causa ausente; admission v1 8/10 y v2 10/10 tras interpretación de citation calificada registrada. 39/39 checks locales v2. No superioridad general ni seguridad/performance/Plus demostrados. Especificaciones RC0 común, shadow y pedagógica completas como contrato propuesto; workload WL-R solo perfil de prueba, no cuota ni estrategia seleccionada.

| ID | Capacidad | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_TARGET_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED | Disposición recomendada |
|---|---|---|---|---|---|---|---|---|
| C-029 | Codex SDK Python 0.160.0 / TypeScript metadata 0.160.0 | YES público Apache-2.0 | YES Python Team 1 smoke 7/7; TS solo metadata | YES archivo; UNKNOWN inferencia/tools/Skill/state/cuota target | YES Python smoke CLI pin explícito; high-level dynamic tool callbacks no probados, TS NOT_TESTED | YES software; CONDITIONAL runtime/local/quota | NO | WRAP transporte oficial si cubre contrato, antes de transporte propio; distinto de Agents SDK/API facturada |

| Candidato | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| C-029 Codex SDK | UNKNOWN workflow Plus; YES software | 0 licencia; potencial quota incluida/local por medir | UNKNOWN fijo/variable/mensual/escala | C-025a/C-010 con gates | Continuidad/capacidad/control como hipótesis futura, no probado | YES antes de gasto |

[Ficha SDK y fallos preservados](research/R-006_codex_sdk_findings_2026-10-05.md): primer intento enum del harness mal nombrado, antes de inferencia; segundo smoke pasa. No actualizar CLI/config/auth del propietario para probarlo. Cohorte final propuesta C-010, C-025a/C-029 como **familia alternativa de transporte**, C-017a/b, C-024 y C-028; MCP/Data reservados por necesidad. C-017a/b son ADAPT y traslado metodológico PORT; full wrappers/premium reference, no entitlement importado. [Plus Gate RC2](research/R-006_plus_runtime_gate_RC0.md) verifica finalistas con workload; seguridad/engine/Strategy V1/DoD/review son otros gates.

## Gate vigente de portabilidad — 2026-10-05

Cohorte RC1 aprobada solo para aceptación; SELECTED=NO. ADR-009 añade D-037/R-028 P1, onboarding/perfiles/paquetes y gate previo D-024/DoR. Entitlement Plus no se deduce de Team ni de un clone. Mecanismos nativos de AGENTS/Skills/inventory/config se investigan antes de proponer instalador propio.

## Candidatos de portabilidad — R-028

| ID | Capacidad | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_TARGET_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED | Disposición propuesta |
|---|---|---|---|---|---|---|---|---|
| C-030 | Codex native AGENTS/cwd + repo Skill discovery | YES | YES 5 smoke Team, metadata y Skill local | UNKNOWN activación/superficie target | YES en CLI/fixture probada, no todas superficies | YES assets/nativo; cupo target condicional | NO | REUSE_AS_IS |
| C-031 | Bootstrap Mode, Skill repo propia, perfiles y paquetes RC0 | YES documentos/assets creados | YES formato/31 checks locales; fresh clone pendiente en este hito | YES archivos; UNKNOWN comportamiento/gates target | PARTIAL diseño y fixtures, sin instalador/runtime | YES adquisición 0, runtime condicional GP | NO | ADAPT de contratos/método |
| C-032 | Custom agents/config roles nativos Codex | YES documentación oficial | UNKNOWN activación; no probe específico | UNKNOWN | UNKNOWN integración/version/superficie | CONDITIONAL nativo/cupo/local | NO | REFERENCE_ONLY, sin topología elegida |

[Resultados R-028](research/R-028_bootstrap_findings_2026-10-05.md). Instalar no es habilitar/invocar. Carpetas package y shared son estructuras de planificación, no freeze ni autoridad. Cleanup WinError 32 tras cinco turnos conservado; lifecycle GP5/EB6 pendiente.

**C-030/C-031 actualización posterior:** fresh clone del commit 9e0dbed descubrió Skill bootstrap en seis roles y cargó root+local; dos smoke confirmaron current Plan Architect/authority NONE/lock y Guardian inactive. C-031 compatibilidad PARTIAL: workflow completo no probado ni target; availability archivos YES, entitlement/activación target UNKNOWN. Perfil PARTIAL y hashing portable de Git blobs; no selección. [Dossier §9](research/R-028_bootstrap_findings_2026-10-05.md).

## Alcance de selección ADR-011

**Vigencia ADR-011 — 2026-10-05:** propietario aprobó opción A y disposiciones RC2 como dirección de diseño PAPER: núcleo financiero local determinístico always-on + jobs Codex Team automáticos por evento/calendario, sin aprobación por job rutinario. D-020 DECIDED únicamente en dirección Build-vs-Reuse; versiones/permisos/runtime final siguen D-024 RESEARCHING. No implementación, gasto, capacidad sostenida ni autoridad financiera adicional. Plus permanece PRE-LIVE.

Se conserva A+, G1+G2 y ADR-006. Las futuras dependencias obligatorias de Strategy V1 tendrán fallo explícito. No modificación de main ni release de despliegue.

## P1 posterior ADR-011 — reuse y fronteras

[Paquete R-010–014](research/R-010_014_hardening_findings_2026-10-05.md): official SDK/CLI0.160 bundle default probado; wrapper no propio RPC. Seguridad candidata reutiliza controles Windows por dominio (S2), VM reserva; permisos no aprobados. Temporal baseline vs APScheduler/OS investigados como **workflow determinístico**, fuera del límite de frameworks IA; SQLite solo probe, no selección storage. No BUILD motor/audit framework antes de necesidad demostrada. D-024 abierto; R-006 método suficiente para dirección aprobada, capacidad/operación pendiente.

**Vigencia ADR-012 — 2026-10-05:** el propietario aprueba S2 como dirección candidata de aislamiento PAPER por dominios Windows. S3 es fallback formal sujeto a nueva decisión si S2 falla; S1 solo probes sin secretos. Las propuestas históricas S2 vs S3 quedan resueltas únicamente en dirección. Security isolation y Shadow experimental blinding requieren acceptance separado; configuración administrativa, permisos efectivos y D-027/D-024 siguen abiertos. Ningún usuario/ACL/firewall/credencial se modifica por esta aprobación. Véase [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md).

## Capabilities técnicas S2 — complemento no agéntico, 2026-10-05

| ID / candidato | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_PAPER_TEAM | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED / disposición |
|---|---|---|---|---|---|---|
| C-033 Windows users/DACL/process/IPC/firewall-WFP | YES documentación y cmdlets host | YES metadata readonly; UNKNOWN effective isolated runtime | UNKNOWN gates SI/BL/RB; no cuentas creadas | CONDITIONAL al policy store/launch/auth/negativos | CONDITIONAL local/licencia actual; sin gasto activado | S2 dirección aprobada, controles no aceptados; REUSE_AS_IS/WRAP |
| C-034 Windows Job Objects lifecycle/descendientes | YES fuente Microsoft | UNKNOWN probe runtime; documental | UNKNOWN breakaway/nesting/child rights | CONDITIONAL wrapper/control domain | CONDITIONAL local/software nativo; tiempo por medir | NO; REFERENCE_ONLY hasta probe, WRAP si demuestra necesidad/viabilidad |

No amplían capa IA fuera OpenAI/Anthropic. Economics seis campos/coste/alternativa en [S2 §9](08_S2_isolation_spec_RC1.md). Availability de controles SO no prueba entitlement/auth Plus/Team; entornos futuros UNKNOWN. [Hallazgos](research/R-013_S2_findings_2026-10-05.md) distinguen 7 observaciones esperadas de todos los gates S2 NOT_TESTED. Policy merge impide inferir firewall efectivo por una regla declarada; no framework/sandbox propio construido.

## Revisión vigente R-013 — 2026-10-06

[Comparativa S2-A/B/S3](research/R-013_S2_variants_comparison_2026-10-06.md), [RC2](08_S2_agent_domain_contract_RC2.md) y [probe](research/probes/r013-s2-variants/README.md). C-033 conserva controles Windows pero **no selecciona una cuenta por rol**; C-034 Job Objects no es barrera por sí mismo. S2-ADM-01 withheld; S2-B dirección recomendada pendiente de gobierno y gates. Skills/runtime financiero no construidos.

| Capability | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_PAPER_TEAM | AVAILABLE_IN_FUTURE_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED / disposición candidata |
|---|---|---|---|---|---|---|---|
| C-035 Windows restricted tokens / AccessCheck | YES Microsoft | YES semántica 10/10 con token/descriptor en memoria; no launch | UNKNOWN runtime Codex y OS policy efectivos | UNKNOWN entorno/política; mecanismo OS no depende del entitlement | PARTIAL semántica, UNKNOWN native auth/launch/egress | CONDITIONAL controles locales nativos, sin gasto; integración/operación por medir | NO; WRAP candidato de API existente, no sandbox propio |
| C-036 AppContainer Win32 unpackaged | YES Microsoft | DOCUMENTED_ONLY; ningún profile/process creado | UNKNOWN native Codex/auth/persistencia/IPC/red | UNKNOWN instalación/runtime destino | UNKNOWN; soporte Win32 genérico no acredita Codex | CONDITIONAL host/licencia/recursos/setup, sin compra | NO; REFERENCE_ONLY hasta probe autorizado |

Economía C-035/036: PAPER_V1_VIABLE_FREE=CONDITIONAL; PAPER_V1_COST=sin facturación activada, licencia incremental esperada 0, ingeniería/recursos UNKNOWN; LIVE_COST=UNKNOWN con migración y operación; FREE_ALTERNATIVE=S2-A mínimo o mecanismo nativo equivalente condicionado; PAID_INCREMENTAL_VALUE=no servicio pago propuesto; ECONOMIC_JUSTIFICATION_REQUIRED=antes de gasto/material coste operativo. Entitlement Team/Plus separado de disponibilidad OS. Ningún gate efectivo pasa por AC.

## Confirmación de dirección S2-B — 2026-10-06

Propietario aprueba S2-B como candidata principal, Q-051 cerrado en dirección. Un Runner base con aislamiento efectivo por job; A/S3 reservas condicionadas. Assets y controles continúan candidatos, no permisos/runtime aceptados. Siguiente gate es laboratorio mínimo concreto y reversible; no administración autorizada. [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md).
