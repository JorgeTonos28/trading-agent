# Build vs. Reuse — marco de decisión inicial

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Antecedente ADR-011 — 2026-10-05:** propietario aprobó opción A y disposiciones RC2 como dirección de diseño PAPER: núcleo financiero local determinístico always-on + jobs Codex Team automáticos por evento/calendario, sin aprobación por job rutinario. D-020 DECIDED únicamente en dirección Build-vs-Reuse; versiones/permisos/runtime final siguen D-024 RESEARCHING. No implementación, gasto, capacidad sostenida ni autoridad financiera adicional. Plus permanece PRE-LIVE.


**Hito histórico previo a aprobación ADR-011 — wave07:** [RC2 Team](research/R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

**Antecedente — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Estado 2026-10-01: **R-006 es P0 y foco inmediato**; D-024 queda abierto hasta el Agent Capability Gate. [ADR-007](decisions/ADR-007-r006-openai-anthropic-plus-scope.md) limita IA/agentes a OpenAI y Anthropic y prioriza Tier 0/1. El inventario está en [capability_landscape.md](capability_landscape.md) y [fichas/probes R-006](research/R-006_initial_findings_2026-10-01.md). La mayoría de disposiciones siguen `PENDING`; [cookbook multiagente de portfolio](https://developers.openai.com/cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration) es `REFERENCE_ONLY` porque está archivado y no satisface A+/shadow como contrato operativo.

## Disposiciones permitidas

| Disposición | Significado operativo |
|---|---|
| REUSE_AS_IS | Usar sin modificación funcional tras licencia, permisos y pruebas |
| ADAPT | Modificar una pieza reutilizable para nuestros contratos |
| PORT | Trasladar procedimiento/código a otro runtime respetando licencia |
| WRAP | Integrar una API/componente tras interfaz propia y límites de permiso |
| REFERENCE_ONLY | Aprender del diseño; no incorporar artefacto ni dependencia |
| BUILD | Construir porque alternativas fallan requisitos medibles |
| REJECT | Excluir por seguridad, licencia, fiabilidad, coste o desajuste |

## Criterios de comparación

1. Seguridad y autoridad financiera: un componente generativo no puede aprobar riesgo ni enviar orden irrestricta.
2. Fidelidad al contrato funcional, PIT, reproducibilidad y auditabilidad.
3. Disponibilidad real para cuenta, región, producto y entorno PAPER.
4. Licencia, portabilidad, datos enviados, privacidad y mantenimiento.
5. Coste total: licencia, datos, integración, operaciones y salida.
6. Reversibilidad y capacidad de prueba independiente.

Una capacidad puede existir y ser técnicamente compatible, pero no estar disponible en el **Team actual objetivo PAPER** o no ser económicamente razonable. La disponibilidad en la sesión Team de investigación no demuestra entitlement en Plus. `SELECTED` exige evidencia y decisión registrada. Un `BUILD` para componente mayor requiere comparación con alternativas y justificación explícita; el Risk Engine determinístico es una **intención arquitectónica de control propio**, pero incluso ahí se investigarán librerías de apoyo sin delegar autoridad.

## Primera cola de clasificación

R-006: OpenAI Skills/Plugins/Codex/MCP y análisis cuya inclusión en **Team actual objetivo PAPER** debe verificarse; ruta SIWC/Codex app-server como hipótesis de uso del plan; Anthropic Financial Services y Skills/templates/workflows públicos portables. OpenAI Agents SDK/API con **clave facturada** y Anthropic runtime son Tier 2 y quedan `REFERENCE_ONLY` por defecto. Fuera de R-006 continúan motores quant, broker APIs, market/alternative data, almacenamiento, seguridad y observabilidad. Las fichas separan `EXISTS`, `AVAILABLE_IN_RESEARCH_ENVIRONMENT`, `AVAILABLE_IN_TARGET_PLUS`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE` y `SELECTED`. `PENDING` no equivale a clasificación final; cada disposición final tendrá evidencia y ADR cuando proceda.

La [wave 02 de R-006](research/R-006_probe_wave_02_2026-10-02.md) deja C-017 como **`ADAPT` candidata**: se validó formato y fixture temporal de una adaptación desechable, pero no activación Plus ni comportamiento del modelo. `SELECTED=NO`; ninguna Skill entra aún al diseño final.

## Economía por fase y por capa

[ADR-008](decisions/ADR-008-economic-policy-by-phase.md) exige calidad suficiente antes de preferir gratis: PAPER cero/bajo coste incremental, LIVE valor económico y economía unitaria. Estudiar un servicio pago está autorizado; gastar/contratar no. Las referencias Tier 2 anteriores son **disposiciones PAPER provisionales por presupuesto**, no `REJECT` permanente ni prohibición de evaluar LIVE. Skills/metodologías se adquieren gratis/incluidas/propias; modelos/datos/runtime/infraestructura se comparan aparte. Cada candidato usa los [seis campos y detalle de coste](economic_scorecard.md); una futura disposición puede diferir entre PAPER y LIVE con evidencia y aprobación.

## Recomendaciones tras waves 04/05 — 2026-10-05

[Shortlist RC0](research/R-006_shortlist_RC0.md): mínimo Codex `REUSE_AS_IS` como capacidad/benchmark; integración nativa app-server `WRAP` candidata; idea-generation y thesis-tracker `ADAPT`; procedimientos propios breves de Quant Review/pedagogía adaptan métodos/contratos tras discovery, sin motor ni subagentes seleccionados. MCP SDK oficial `WRAP` de lectura opcional, probado localmente; Data propietario `REFERENCE_ONLY` hoy, reuse dentro de entitlement verificable después. Assets Earnings/Audit/Calendar son reservas adaptables por necesidad. No comprar Skills/templates ni asumir premium access.

Mínimo 10/10 y Skill 9/10 checks: no se demostró superioridad general. Skill aporta detalle metodológico/pedagógico; estructura/seguridad pertenecen también a harness y contratos. Role/schema/lineage requieren endurecimiento; no seleccionar bundles o construir componentes mayores por inercia. Todos `SELECTED=NO`; no cerrar D-020/D-024.

## Recomendación actual RC1 — paquete autónomo completado

[Shortlist RC1](research/R-006_shortlist_RC1.md) incorpora [wave 06](research/R-006_probe_wave_06_2026-10-05.md), contratos por rol/shadow/pedagogía, workload/matriz y [Codex SDK nativo C-029](research/R-006_codex_sdk_findings_2026-10-05.md), distinto de Agents SDK API. Recomendaciones (ninguna SELECTED):

- C-010 capacidad base **REUSE_AS_IS**, conservar benchmark mínimo.
- C-025a/C-029 **WRAP** de transporte oficial mínimo; preferir SDK cuando cubra job contract, app-server por gap concreto (tools/callbacks/lifecycle). No construir RPC framework nuevo por defecto ni imponer Python/TS.
- C-017a/b **ADAPT**, **PORT** del método público Anthropic (Apache), eliminando autoridad y cambiando PIT/output; no portar runtime/conector premium por copiar prompt.
- C-024/C-028 **ADAPT** de métodos/contratos propios tras revisar activos: pedagogía factual/curriculum y Quant Review; no motor quant propio seleccionado.
- MCP oficial **WRAP** reserva por interoperabilidad necesaria; Data/plugin propietario **REFERENCE_ONLY** hoy, REUSE_AS_IS solo con entitlement/licencia/uso demostrado.
- Métodos financieros públicos Earnings/Audit/Calendar/Model/Market **ADAPT/PORT** reserva por tarea; APIs/modelos pagos **REFERENCE_ONLY** PAPER con LIVE económica abierta.
- Otros labs/frameworks agénticos **REJECT** por alcance aprobado, no fallo técnico; brokers/datos/quant/infra conservan investigación separada.

No BUILD de capacidad mayor autorizado/seleccionado. Integración propia específica de contratos se propone después de comparar workflow/storage/engine R-009/011/012; no implementación durante preparación. Wave 06 corrige tipos en corpus pequeño, con checker v2 enmendado y v1 conservado; no superioridad/general fiabilidad. [Plus Gate](research/R-006_plus_runtime_gate_RC0.md) sigue abierto; paquetes finales D-020/D-024 requieren aceptación target, review independiente y gobierno. Orientación candidata local determinística always-on + jobs Codex intermitentes se presenta al propietario, sin freeze.

## Bootstrap/Agent Packaging — candidato R-028

REUSE_AS_IS discovery/instrucciones/Skills nativos (C-030); ADAPT modo de onboarding/Skill propia/perfiles/paquetes de contratos actuales (C-031); WRAP inventarios/transporte oficial cuando D-024 elija una ruta. Skill-installer público REFERENCE_ONLY/ADAPT si hace falta adquirir assets externos, no para copiar nuestros assets a home. Roles nativos custom agents C-032 y plugin packaging C-002 REFERENCE_ONLY ahora. No construir instalador/discovery engine/orquestador nuevo por defecto. SELECTED=NO, Team no prueba Plus. [Dossier](research/R-028_bootstrap_findings_2026-10-05.md).

**R-028 paquete concluido:** fresh clone metadata de seis roles + dos smoke, profile PARTIAL y hash de Git blob portable. No installer operativo construido; bootstrap es método/instrucciones y contratos candidatos. Coste por fase y free/paid alternativas en dossier R-028. Plus access/gates y final gobierno siguen pendientes.

## P1 posterior ADR-011 — reuse y fronteras

[Paquete R-010–014](research/R-010_014_hardening_findings_2026-10-05.md): official SDK/CLI0.160 bundle default probado; wrapper no propio RPC. Seguridad candidata reutiliza controles Windows por dominio (S2), VM reserva; permisos no aprobados. Temporal baseline vs APScheduler/OS investigados como **workflow determinístico**, fuera del límite de frameworks IA; SQLite solo probe, no selección storage. No BUILD motor/audit framework antes de necesidad demostrada. D-024 abierto; R-006 método suficiente para dirección aprobada, capacidad/operación pendiente.

**Vigencia ADR-012 — 2026-10-05:** el propietario aprueba S2 como dirección candidata de aislamiento PAPER por dominios Windows. S3 es fallback formal sujeto a nueva decisión si S2 falla; S1 solo probes sin secretos. Las propuestas históricas S2 vs S3 quedan resueltas únicamente en dirección. Security isolation y Shadow experimental blinding requieren acceptance separado; configuración administrativa, permisos efectivos y D-027/D-024 siguen abiertos. Ningún usuario/ACL/firewall/credencial se modifica por esta aprobación. Véase [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md).

**R-013 S2:** reutilizar identidades/DACL/IPC/process/network Windows y native Codex, envolver interfaces mínimas después del gate; no construir sandbox/driver de red desde cero. C-033 REUSE_AS_IS/WRAP condicionado, C-034 Job Objects REFERENCE_ONLY→WRAP sujeto a probe. [S2 RC1](08_S2_isolation_spec_RC1.md) documenta coste y límites. S3 permanece reserva, sin VM aprovisionada ni gasto. Slots/env/caches aislados se prueban, no se resuelven con un prompt.

## Revisión de controles de aislamiento — 2026-10-06

Reutilizar controles Windows antes de construir contención: restricted tokens candidatos WRAP (AccessCheck semántico 10/10, compatibilidad Codex UNKNOWN), AppContainer REFERENCE_ONLY hasta prueba autorizada, usuarios/DACL/IPC/egress REUSE_AS_IS/WRAP, Job Objects lifecycle sin garantía de sandbox. [Comparativa](research/R-013_S2_variants_comparison_2026-10-06.md). S2-B recomendado, no launcher custom seleccionado ni cuenta por rol necesaria; S2-A solo si necesidad demostrada, S3 reserva. Sin perfiles/ACL/users/firewall ni gasto; ADM-01 withheld. Codex/SDK/Skills disposiciones ADR-011 intactas.

## Diseño candidato vigente — 2026-10-07

[B-RT1](08_agentic_runtime_realization_RC1.md) y [checkpoint](14_agentic_architecture_design_checkpoint_RC0.md) concretan ownership/launch/auth/tools/state y binding; ADR-014 READY_FOR_DECISION, no aprobado. R-006 maduro para esta decisión; D-020 disposiciones aprobadas conservadas. Plus/PC personal R-030 aceptación diferida, LIVE UNKNOWN. No freeze ni permiso operacional; workspaces/AGENTS son packaging, no barrera. Costo incremental/autenticación/gates futuros no autorizados por este texto.

## Vigencia técnica wave10 — 2026-10-23

Wave10: LEAN source principal condicionado de investigación, Nautilus alternativa; Common/Enginecomponent build y matching no aceptan fidelidad/seguridad. Ver research/R-009_engine_recommendation_RC1.md y matrix15; motores seleccionadosNO.

## Actualización wave11 — 2026-10-23

[EngineRC2](research/R-009_engine_selection_packet_RC2.md), [brokerRC4](research/R-007_PAPER_broker_selection_packet_RC4.md) y Q062 preparan selección de familias: LEANreuse/adapt, SDK/APIswrap; reservasNautilus/IBKR, sin motor propio general/contratos pagados. Source/build/behavior no selección por anticipado.
