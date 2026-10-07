# R-006 — shortlist RC2 y madurez PAPER Team

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-05. Vigente tras ADR-010; sustituye **recomendación/next-step** RC1 para PAPER, conserva RC1 y pruebas históricas. Cohorte candidata ya aprobada, selección final **NO**; D-020 DECIDED en disposiciones de diseño ADR-011; D-024 RESEARCHING (dirección A aprobada; freeze no listo). No implementación.

## 1. Disposiciones de diseño aprobadas

La tabla original conserva SELECTED=NO como **selección final de runtime**. ADR-011 aprueba estas disposiciones para especificación (`SELECTED_FOR_DESIGN=YES` para la cohorte activa); no activa reservas, paga servicios ni congela versiones/permisos. Jobs rutinarios serán automáticos por eventos/calendario, no manuales.

| Capacidad | EXISTS / AVAILABLE_IN_PAPER_TEAM | Compatibilidad / economía | Disposición propuesta; SELECTED=NO |
|---|---|---|---|
| C-010 base Codex | YES / YES ruta nativa | YES fixtures; cupo Team compartido, no costo API aprobado | **REUSE_AS_IS** capacidad base y control comparativo sin Skill |
| C-025a app-server + C-029 SDK | YES / YES Python inferencia/Skills/tools | YES contratos sintéticos; interfaz dynamic experimental, integración/aislamiento y versiones finales pendientes | **WRAP** familia oficial; SDK tipado preferido donde cubre contrato. No cliente RPC propio por defecto |
| C-017a research idea | YES / YES procedimiento | Método público Apache-2.0; 0 adquisición, runtime/datos aparte | **ADAPT / PORT** metodología PIT/tesis/falsifier, sin recomendación operativa directa |
| C-017b thesis/shadow | YES / YES procedimiento | OPEN toy/restart correctos; riesgo/fills/multiasset real sin validar | **ADAPT / PORT**, sin autoridad ni tesis ejecutable automática |
| C-024 pedagógico | YES / YES procedimiento factual | Causa/cancel UNKNOWN, trazas/preguntas; suite educativa completa P2 | **ADAPT** propio, contrato completo obligatorio aunque LLM no residente |
| C-028 quant review | YES / YES procedimiento | Train/OOS/cost/missing tests y no promoción; sin backtest validado | **ADAPT** propio; engine R-009 aparte |
| C-030 AGENTS/Skills nativos | YES / YES CLI y SDK fresh clone | Root+rol dentro Git completo; aislado pierde raíz, overrides deben verificarse | **REUSE_AS_IS**, sin confundir instrucciones y permisos |
| C-031 bootstrap/manifests/paquetes | YES / YES procedimiento y assets repo | Ruta Team reproducible parcial, auth/settings/deps externos explícitos | **ADAPT**, sin instalador propio ni knowledge del chat |
| C-027 MCP SDK | YES / mock YES, host completo UNKNOWN | MIT libre; integración real/datos innecesaria ahora | **WRAP reserva**, solo necesidad concreta con probe host |
| C-026 Data/plugins y C-002 plugin packaging | YES / por superficie UNKNOWN/PARTIAL | Propietario/entitlement distinto, portabilidad no demostrada | **REFERENCE_ONLY**; plugins autorizados futuros REUSE posible, no PORT propietario |
| C-032 custom agents nativos | YES / no topology probe seleccionado | Pueden transportar rol; no necesidad incremental probada | **REFERENCE_ONLY**, no sesión/proceso por paquete requerido |
| Anthropic otros métodos públicos | YES / archivos públicos, activación por tarea | Gratis metodología, dependencias premium no transferidas | **ADAPT / PORT reserva** o REFERENCE_ONLY si no función actual |
| Agents SDK/API/Claude Managed/premium financiero | YES / pago no ejecutado | Tier 2 separado de Team, sin autorización gasto | **REFERENCE_ONLY PAPER**, ficha económica LIVE futura |
| Otros labs/frameworks IA | Referencias existen, no evaluados | Fuera del alcance aprobado | **REJECT por alcance**, no juicio técnico |

No BUILD de framework de agentes, plugin completo o transporte propio demostrado necesario. Integraciones de caller/contratos son WRAP/ADAPT de proyecto, aún sin permiso de implementar. Prototipos de Skills no equivalen a Skills finales instaladas; métodos modulares ayudan a gobierno/portabilidad, sin superioridad universal de calidad/latencia frente al mínimo.

AVAILABLE_IN_RESEARCH_ENVIRONMENT=YES en las rutas Team probadas. AVAILABLE_IN_PAPER_TEAM=YES **para la misma ruta/función probada**, no equivalencia de todo Team. AVAILABLE_IN_FUTURE_PLUS=UNKNOWN para runtime/activación. Archivos públicos disponibles independientemente del plan. ECONOMICALLY_REASONABLE=YES adquisición pública/propia; runtime **CONDITIONAL** a carga/cupo/operación suficiente, sin spend adicional aprobado.

## 2. Evidencia y madurez por gate

| Gate | Madurez arquitectura ahora | Trabajo realmente pendiente / etapa |
|---|---|---|
| TP1 acceso | Team nativo observado; modelo/cliente/ruta probados | Revalidar instancia/versiones en despliegue; no Plus para PAPER |
| TP2 Skills/roles/bootstrap | Cuatro procedimientos probados, root+roles y Bootstrap desde clone CLI/SDK | Assets finales/pins y package/version/distribución tras elección; Desktop solo si ruta final lo requiere |
| TP3 tools/outputs | SDK low-level callbacks + schema/lineage/PIT; 8/8 wave07, fallos conservados | Integración fuentes/engine/report completos; mantener regresión en upgrades experimental |
| TP4 autoridad | Cero endpoints financieros expuestos en harness; injection/toy admission y default handler detectado | **P1 D-027/034**: diseño/approval aislamiento de secretos/procesos/herramientas; **P2** enforcement/red team reales |
| TP5 recovery | Restart con mismo snapshot, contexto desde repo; dedup/late/no-output toy | **P1 D-025/026**: contrato workflow/storage; **P2** durable recovery/auth expiry/revocation. No reclamar native resume probado |
| TP6 carga | 7 funcionales + 1 failure, payload normal >32 KiB, servicio medio 30.93 s, burst máximo total 83.113 s | **P1** workload representativo/criterios y evidencia de suficiencia antes del cierre final runtime, PARTIAL; **P2** WL-R integrado/sostenido con cuotas/reset/uso compartido reales. ≥5 sesiones/≥7 días sigue propuesto, no aprobado ni eximido |
| TP7 economía/versiones | SDK libre/nativo documentado, sin API billing ni gasto; método público/propio | Versiones finales/operación legítima/upgrade policy; coste local y alternativas LIVE con ADR-008 |
| EB1–8 bootstrap | Fresh clone, rutas/hash Git, root/roles/Skill y perfil sanitizado; no chat requerido | Source release aprobado tras checkpoint; config effective/permissions/readiness full + integración final. Perfil PAPER **PARTIAL** |
| Capability Gate | Cobertura/reuse, licencia/coste, probes prioritarios, autoridad evaluada en harness, comparativa y limitaciones explícitas | **MATURE_FOR_SCOPED_ARCHITECTURE_DECISION**; selección/gobierno y review independiente antes de freeze |

Ni ocho jobs, ni clasificación offline, ni una cuota compartida antes/después prueban funcionamiento PAPER completo. Resultados originales wave06 8/10 evaluator v1 y 10/10 v2 siguen intactos; wave07 utiliza v2 preregistrado, no repara resultados tras observarlos. Shadow numéricamente coincide en el ejemplo; prosa distinta impide afirmar reproducibilidad generativa absoluta.

## 3. Arquitectura candidata y comparación

**Núcleo financiero local determinístico always-on + jobs Codex Team intermitentes.** El núcleo no necesita un LLM residente ni aprobación humana por operación Champion. Caller fijo prepara manifiesto/snapshot/rol/Skill/schema/tools; agente responde investigación/shadow/pedagogía; validator externo registra resultado/late/fail/duplicate sin convertirlo en TradeIntent. Roles de repo compartidos manual/programmatic, no topología de sesiones aprobada.

La [propuesta ADR-011](../decisions/ADR-011-paper-team-agentic-direction-proposed.md) compara jobs nativos, uso manual, LLM residente y API paga. Recomendación: familia nativa con wrappers mínimos y contratos externos. [Job boundary](R-006_native_job_boundary_RC0.md) expone amenazas/pendientes; aislamiento OS no lo prueba un prompt ni sandbox read-only.

## 4. Qué queda exclusivamente PRE-LIVE Plus

Disponibilidad/activación/config herramientas en cuenta Plus candidata, entitlement/cuota/continuidad para **demanda validada en Team**, auth legítima de nueva cuenta, perfiles/diffs/smoke de release, portabilidad/recovery y rollback de migración. [R-029](R-029_pre_live_environment_migration_gate_RC0.md). Reusar métodos/conducta Team y repetir solo deltas pertinentes. No repetir R-006 entera, ni pedir acceso Plus ahora, ni confundir este gate con aprobación financiera LIVE.

## 5. Aprobación y siguiente paquete

Propietario aprobó ADR-011 A y disposiciones RC2; la anterior solicitud queda resuelta. Continuar P1 R-010–014 y preregistro Strategy V1 independiente. D-024 no puede cerrarse por esta aprobación ni por smokes. Gates Team permanecen; Plus solo PRE-LIVE.

## Hardening posterior ADR-011

[Contratos/probes/review R-010–014](R-010_014_hardening_findings_2026-10-05.md) especifican automatización, seguridad por dominios, recovery/epoch, audit/versiones y carga. SDK/CLI0.160 emparejado H4 pasa 2/2 focales; no final pin ni cuota. D-020 DECIDED en disposiciones de diseño; D-024 sigue RESEARCHING hasta gates. Próximo gobierno ADR-012 frontera material de seguridad, no Plus.

**Vigencia ADR-012 — 2026-10-05:** el propietario aprueba S2 como dirección candidata de aislamiento PAPER por dominios Windows. S3 es fallback formal sujeto a nueva decisión si S2 falla; S1 solo probes sin secretos. Las propuestas históricas S2 vs S3 quedan resueltas únicamente en dirección. Security isolation y Shadow experimental blinding requieren acceptance separado; configuración administrativa, permisos efectivos y D-027/D-024 siguen abiertos. Ningún usuario/ACL/firewall/credencial se modifica por esta aprobación. Véase [ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md).

**Estado S2 posterior:** [RC1 concreto](../08_S2_isolation_spec_RC1.md), 17 SI + 9 BL + 5 RB especificados. S2 acceptance NOT_TESTED; tres cuentas/ACL canary requieren [ADM-01](R-013_S2_administrative_gate_ADM01.md). R-006 reduce incertidumbre de contratos, no acredita permisos/cuota finales ni congela D-024. Native OS controls se REUSE/WRAP; runtime Team mantiene arquitectura ADR-011 automática. Ningún acceso Plus solicitado.

## Gate S2 revisado — 2026-10-06

[Comparativa A/B/S3](R-013_S2_variants_comparison_2026-10-06.md) y [RC2](../08_S2_agent_domain_contract_RC2.md) proponen **Agent Runner común con contextos efectivos por job**, sin cuenta obligatoria por rol. No cambiar disposiciones D-020/ADR-011 ni congelar D-024. **ADM-01 DEFERRED/NOT_AUTHORIZED**, no próximo gate: Q-051 dirección candidata revisada antes de laboratorio nuevo. AC10/10 es semántica, no TP4/EB/SI/BL/RB efectivo ni TP6 capacidad bajo permisos. Plus PRE-LIVE, PAPER Team, futuros native auth/egress/cache/recovery/workload pendientes.

## Endpoint S2-B y evidencia adicional — 2026-10-06

Dirección S2-B aprobada; Q-051 DECIDED en ese alcance. [Laboratorio mínimo S2B-ADM-01](R-013_S2B_lab_ADM01.md), Q-052 DECIDED únicamente en autorización temporal **AUTHORIZED_OWNER_ADMIN_ONLY**. [Runbook por fases](R-013_S2B_owner_execution_runbook.md). Setup/login pendientes de acciones manuales del propietario; no permisos PAPER finales. [Dossier](R-013_S2B_lab_preparation_2026-10-06.md) y fuentes distinguen memoria12+privilegios2, sintaxis14 y preflight readonly de **FS/thread/native NOT_TESTED**. Grant común/tránsito/default DACL se incluyen en VP04/LF09, con positivos adecuados. Setup aún no ejecutado; no retry bajo BASE para operaciones de job. Full process/IPC/egress/auth/cache/recovery/TP6 y SI17/BL9/RB5/VP8 pendientes; ningún gate efectivo se pasa por estos contadores. R-006 madura diseño, D-020 conserva aprobación, D-027/D-024 siguen RESEARCHING. ADM-01 tres cuentas DEFERRED; PAPER Team y Plus PRE-LIVE.

## Checkpoint posterior ADR-013 — vigencia 2026-10-07

[Checkpoint](../14_agentic_architecture_design_checkpoint_RC0.md) / B-RT1 READY_FOR_DECISION, no aprobado. Scope R-006 diseño maduro; disponer capabilities no acepta target Plus/PC personal. R-030 difiere target-specific, LIVE UNKNOWN; las notas Team PAPER/Plus PRE-LIVE previas son historia. Preguntas concretas ownership/auth/persistencia/launch/tooladmission/binding especificadas con review; compatibilidad host/plan sigue NOT_TESTED. R-011/012/014 transversales y P0 Strategy/data permanecen investigables ahora.
