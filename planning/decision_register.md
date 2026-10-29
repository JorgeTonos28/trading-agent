# Decision Register — inicialización

**Estado vigente 2026-10-29:** [checkpoint18](18_financial_hardening_checkpoint_RC0.md). Q063/A DECIDED dirección ADR024, D025/026RESEARCHING configuración/suficiencia; Q064 READY_FOR_DECISION política protectora. Lock/target/holdout intactos.

**Checkpoint anterior 2026-10-28 (Q063 sustituido por ADR024):** [bindings/readiness17](17_financial_bindings_and_readiness_RC0.md). Q-062 DECIDED ADR-023; Q-063 propuesta de dirección condicionada, no stack operacional aceptado. Datos NOT_ADMITTED, cero trials, lock/target/holdout preservados. Las notas anteriores son historia fechada.

**Vigencia 2026-10-28:** Q-062/A DECIDED como familias de diseño en ADR-023; no volver a solicitar Q-062. Twelve requiere aclaración; EODHD respondió según resumen del propietario, sin admisión. Ver nota actual al final. Las notas wave11/a249d77 se conservan como historia. Implementación bloqueada, aceptación target diferida y holdout UNKNOWN.

**Vigencia financiera wave11 — 2026-10-23:** [checkpoint16](16_financial_stack_checkpoint_RC0.md) y [MasterPlanRC0](../docs/master/MASTER_PLAN_v1.0_RC0.md), DRAFT/NOT_READY. Q061 DECIDED ADR022; investigación DD actual acotada, método no aceptado. Q062 READY_FOR_DECISION propone seleccionar Alpaca Paper Only + LEAN source como familias de diseño PAPER, sin aceptación de pin/protección/target ni autorización de cuenta/gasto. Datos4+6cards NOT_ADMITTED; vendors AWAITING_VENDOR_RESPONSE. Holdout INTEGRITY_UNKNOWN, implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED. Notas anteriores fechadas conservadas como historia.

**Checkpoint financiero vigente — 2026-10-23:** [readiness RC0](15_financial_design_readiness_RC0.md), [preregistro RC7](research/R-020_preregistration_readiness_RC7.md) y [evidencia ejecutada](research/R-020_financial_probe_findings_2026-10-23.md). Las notas fechadas anteriores se conservan como historia. D035-T1 semántica y D011-T1 grafo corregidos, no cierre de sus parents; D030/D031 diseño P1, pruebas operativas P2. Vendor inquiries AWAITING_VENDOR_RESPONSE por declaración owner, fecha exacta UNKNOWN; no respuestas/autorización. Q061 DECIDED en ADR022; continuar datos/broker/engine y diseño financiero, sin accesoPlus/admin/gasto. Holdout INTEGRITY_UNKNOWN, implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED.

**Vigencia aprobada — 2026-10-13, ADR-014 / propietario:** `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` en el alcance capacidades/roles/fronteras/integración B-RT1. `design_status=DESIGN_DECIDED`; `TARGET_ACCEPTANCE_DEFERRED`; `PAPER_RUNTIME_ACCEPTED=false`; `implementation_locked=true`. Un Runner, control confiable externo, core/secretos fuera AI, aislamiento/contexto mínimo por job, allowlists, identidad/lifecycle por attempt y admisión/audit externos son el contrato aprobado. Keyring, HOME readonly, token, desktop, IPC carrier y launch exactos son **mecanismos candidatos sustituibles**, no invariantes irreversibles; cambios preservan fronteras/autoridad con evidencia y gobierno correspondiente. R-030 acepta eficacia en Plus/PC personal. Investigación agéntica fundamental Team completada; no expandir R-006/010/013 por refinamiento indefinido. LIVE UNKNOWN; residuos H7 conservados sin evasión de policy.


> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Antecedente — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Fecha: 2026-10-01. Fuente base: [hoja de ruta v0.2](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md). `DECIDED` significa que la hoja fija el principio; no implica que su implementación esté especificada. Los candidatos nombrados por la hoja siguen abiertos. Estados: `OPEN`, `RESEARCHING`, `READY_FOR_DECISION`, `DECIDED`, `DEFERRED`, `SUPERSEDED`. P0/P1 bloquean el Plan v1.0.

| ID | Decisión y estado actual | Prioridad | Estado | Cierre / autoridad |
|---|---|---|---|---|
| D-001 | Preparation Program, DoR y bloqueo de implementación | P0 | DECIDED | Hoja §3, §56; dueño aprueba freeze |
| D-002 | Invariante TradeIntent → riesgo determinístico → ejecución → broker | P0 | DECIDED | Hoja §2, §7; cualquier cambio requiere aprobación humana |
| D-003 | Primera versión operativa PAPER; LIVE por gate separado | P0 | DECIDED | Hoja §0, §24–25; LIVE requiere aprobación |
| D-004 | Autonomía por operación dentro de estrategia y límites aprobados | P0 | DECIDED | Hoja §5; incidentes PAPER V1 delimitados en ADR-002/D-017 |
| D-005 | Research separado de Champion; promoción humana | P0 | DECIDED | Hoja §2, §26 |
| D-006 | MATR_V1 como primera estrategia/Champion experimental | P0 | SUPERSEDED | ADR-000: era una hipótesis del borrador; propietario reabrió selección el 2026-10-01 |
| D-007 | Capa Trading OS Plugin propia sujeta a Build vs. Reuse | P1 | DECIDED | Hoja §3.14, §9; formato y contenido abiertos en D-024 |
| D-008 | **Strategy V1 Selection**: variantes inspiradas en el video primero, MATR_V1 y otros candidatos justificados | P0 | OPEN | Comparación preregistrada, evidencia y aprobación humana; la primera descomposición no implica selección |
| D-009 | Extracción funcional del video: capacidades, mecanismos, estrategias y pedagogía | P0 | DECIDED | Plan Architect, cierre técnico 2026-10-07 tras revisión independiente: dossier/mapa/rule cards completos en ese scope. Claims NO VERIFICADOS; reglas/datos/selección siguen D-008/011/022/033; no estrategia aprobada |
| D-010 | MATR candidato/benchmark y configuración financiera | P0 | RESEARCHING | Reglas RC2 y binding Alpaca/LEAN RC3; OP-L1 propuesta, protección/order/cash/Risk/datos/método pendientes; no Strategy seleccionada |
| D-011 | Metodología de backtest: datos point-in-time, OOS, costes, benchmark, sesgos | P0 | RESEARCHING | Q-055/O-B y Q-056/B DECIDED conceptuales ADR-016/017. RC3/RC4 calificación conjunta; Q-057/K2 aprobado ADR018, Q-058/M1 aprobado ADR019; Q059/G-R1 aprobado ADR020 (método pendiente); métricas/márgenes/sample/costs/engine/datasets e integridad de reserva siguen abiertos. No estrategia seleccionada. |
| D-012 | Arquitectura conceptual de riesgo compuesto para PAPER V1 | P0 | DECIDED | Propietario aprobó opción B el 2026-10-01 en ADR-006: mínimo entre exposición/cash, stop estimado, gap/slippage, liquidez y reservas; fórmulas D-035, umbrales/escenarios D-031 y detalles D-021/026/030 abiertos |
| D-013 | Contrato abstracto de órdenes, `TradeIntent`, autorización, idempotencia y reconciliación | P0 | DECIDED | ADR-003 y `04_order_contract_RC1.md`: identidad interna, eventos, `UNKNOWN`, G2; mapeo broker D-021, pruebas D-030/031 |
| D-014 | Semántica abstracta de datos y linaje PIT: clocks, revisiones, ajustes as-of y snapshots | P0 | DECIDED | ADR-004 y `05_data_contract_RC1.md`; pruebas/delays por dataset/proveedor siguen R-021/D-022/D-033 |
| D-015 | Límites de componentes y autoridad; papel de Portfolio Manager, Signal y Execution | P0 | DECIDED | ADR-001 aprobado por el propietario 2026-10-01: A+; Champion/intent determinísticos, Portfolio Manager Agent SHADOW sin ruta operativa |
| D-016 | Alcance exacto PAPER V1 y gates de aceptación frente a fases B0–B7 | P0 | DECIDED | ADR-001 y contrato RC1: un Champion operativo puede combinar fuentes/señales; shadow y explicación factual desde B4, pedagogía completa antes de DoD |
| D-017 | Fronteras de autonomía PAPER V1 ante incidentes | P0 | DECIDED | Propietario aprobó G1+G2 y reanudación humana tras pausa material el 2026-10-01; ADR-002; G3/liquidación general no autorizados; umbrales D-031 abiertos |
| D-018 | Roles y gates abstractos de Smart Money/señales externas en Research/Strategy/Pedagogical | P0 | DECIDED | ADR-005 y `06_external_signal_admission_RC1.md`; ninguna familia/dataset admitido automáticamente, PIT/selección concreta D-008/022/033 |
| D-019 | Contrato del Pedagogical Agent y aprendizaje sin alterar Champion | P0 | DECIDED | ADR-001 aprobado: factual desde B4 y completo antes de DoD, sin autoridad financiera; contrato completo RC0 especificado, full reports/privacidad/evals P1/P2 pendientes |
| D-020 | Capacidades y Build-vs-Reuse: dirección de diseño RC2 | P0 | DECIDED | Propietario aprueba ADR-011 A y disposiciones RC2 el 2026-10-05. SELECTED_FOR_DESIGN=YES; selección final de runtime/versiones/permisos y suficiencia siguen D-024. Descubrimiento continuo ante necesidades nuevas; reservas no obligatorias. |
| D-021 | Familia broker PAPER: Alpaca Paper Only | P1 | DECIDED | ADR-023/Q062 propietario2026-10-28: DESIGN_SELECTION_ONLY; IBKR reserva. B1–B5/protección/parciales/recovery/target no aceptados; LIVE sigue separado |
| D-022 | Datos por rol y validador independiente | P1 | RESEARCHING | EODHD respuesta comercial reportada y precios3planes/5escalas; EOD19.99 prioridad condicionada. Twelve VENDOR_INFORMATION_REQUESTED. Cuatro+seis cards NOT_ADMITTED; derechos/PIT/calidad/pay-date/ejecución pendientes |
| D-023 | Familia motor: LEAN source local | P1 | DECIDED | ADR-023/Q062: DESIGN_SELECTION_ONLY; Nautilus reserva. Sin CLI/Cloud comerciales asumidos gratis. Pin/deps/modelos/QP1–QP10/paridad/target abiertos |
| D-024 | Runtime/topología/plugin agéntico PAPER | P1 | DECIDED | ADR-014 aprobado owner 2026-10-13 en scope B-RT1; diseño fundamental DESIGN_DECIDED. Target R-030 TARGET_ACCEPTANCE_DEFERRED, operacional NOT_IMPLEMENTED. Mecanismos/versiones finales requieren aceptación, sin diseño abierto por host-specific. |
| D-025 | Workflow durable, scheduler y recuperación | P1 | RESEARCHING | ADR-024/Q063 A aprobado como dirección condicionada; especificación/configuración/suficiencia pendientes. Historia: Q063 propone dirección condicionada APS3+ledger PostgreSQL frente Temporal+PostgreSQL; envelope/latencias/RPO/RTO/retención y full config/suficiencia P1 siguen abiertos; sin instalación o aceptación |
| D-026 | Storage, eventos y audit trail | P1 | RESEARCHING | ADR-024/Q063 A aprobado como dirección condicionada; seguridad/durabilidad/configuración/suficiencia pendientes. Historia: Q063 dirección PostgreSQL C/F separados; Parquet/DuckDB analíticos, no Redis obligatorio propuesto. H9 SQLite DELETE sólo instrumento; restore/lost receipts y target/pin/roles/constraints no aceptados |
| D-027 | Seguridad/permisos y secretos | P1 | DECIDED | Contrato de diseño B-RT1 DESIGN_DECIDED owner ADR-014; permisos efectivos SI/BL/RB/VP NOT_TESTED y target R-030 diferido. Mecanismos candidatos sustituibles con gobierno; lab diferido, no admin INFOTEP. |
| D-028 | Observabilidad, alertas, backups y deployment PAPER | P1 | RESEARCHING | R012RC2 separa audit durable/telemetría, actores/runbooks/RECOVERY_GAP; SLO/RPO/RTO/retención numéricos y restore motor final pendientes, sin main/tag automático |
| D-029 | Acceptance/evals trazables por contrato | P1 | RESEARCHING | Matrices broker/datos/engine/risk/ledger con fixtures y scopes; suite integrada/modelos/pin/criterios por completar. Ni suma de PASS ni marcadores declaran aceptación |
| D-034 | Esquema detallado, aislamiento y evaluación PIT de `ShadowPortfolioProposal` | P1 | RESEARCHING | ADR-001 fija obligación funcional; contratos RC0 común/shadow especifican caller confiable, snapshots ciegos pareados, target quantity y lineage, estados y comparación local vs trayectoria contrafactual. R-026 conserva gates de aislamiento real/engine/metrics; probes sintéticos no cierran evaluación |
| D-035 | Controles de riesgo compuestos verificables | P1 | RESEARCHING | R2/RC3+RC4+RC5; D035-T1 semántica y D035-T2 precondiciones de caps incrementales especificadas;900 celdas ficticias no calibración/solver real. Inputs/modelos/txns/parámetros D031/mapping pendientes |
| D-037 | Bootstrap, portability y agent packages | P1 | DECIDED | Ruta/contratos de diseño DESIGN_DECIDED ADR-009/014; fresh clone y aceptación Plus/PC personal R-030 diferidos antes de implementación. Sin dependencia de chat, cuentas/sesiones por rol no impuestas. |
| D-036 | Política económica por fase y adquisición de Skills/metodologías | P0 | DECIDED | Propietario, 2026-10-02, ADR-008: calidad/fiabilidad/capacidad al menor coste razonable; PAPER zero/low incremental cost first, LIVE economic value/unit economics; Skills/templates gratuitos/incluidos/propios; pagos investigables, aprobación explícita antes de contratar o gastar |
| D-033 | Proveedores Smart Money/alternative data y clasificación Build vs. Reuse por dataset | P1 | RESEARCHING | R-025; scorecards PIT, API, cobertura, calidad, latencia, licencia y coste; aprobación humana si gasto material |
| D-030 | Órdenes/protección y ejecución PAPER concreta | P1 | RESEARCHING | Q064 READY_FOR_DECISION de política PF versus cobertura nativa; ninguna ruta B3 admitida. Partial/OTO/PATCH/cancel/restore/cash explícitos; OP-L1 propuesta sin umbrales ni nueva tolerancia de desprotección. Integración/fill parity P2 después de diseño |
| D-031 | Perfil numérico inicial de riesgo y kill switches | P1 | OPEN | Límites/modelos/freshness/escenarios/acciones de diseño antes de DoR con aprobación humana; calibración/ensayos integrados operacionales P2. Sin umbrales aprobados |
| D-032 | Ventana y reglas de promoción desde replay a paper autónomo | P2 | OPEN | Métricas, incidentes y procedimiento explícito en DoR |
| D-038 | Entornos Team/PAPER y Plus PRE-LIVE de ADR-010 | P0 | SUPERSEDED | Supersession parcial ADR-013/D-043: Team/institucional research; Plus/personal PAPER; LIVE UNKNOWN. Deployment Source Policy permanece DECIDED y vigente. Evidencia histórica preservada. |
| D-039 | Premisa migración Team→Plus exclusivamente PRE-LIVE | P3 | SUPERSEDED | ADR-013 sustituye esa premisa por transición target PAPER R-030. Entorno LIVE sigue UNKNOWN; gates LIVE D-040/041/042 permanecen, sin selección implícita. |
| D-043 | Entornos AI/host y separación diseño/aceptación | P0 | DECIDED | ADR-013 aprobado por instrucción owner 2026-10-07: Team/INFOTEP research, Plus/PC personal PAPER, LIVE UNKNOWN. Lab diferido; diseño no implica aceptación ni implementación. |
| D-040 | Broker LIVE, elegibilidad/custodia/funding y permisos | P3 | DEFERRED | Gate LIVE, pruebas y aprobación humana |
| D-041 | Capital live, riesgo live, fiscalidad y obligaciones RD/EE.UU. | P3 | DEFERRED | Asesoramiento competente y aprobación humana antes de LIVE |
| D-042 | SLO, disaster recovery y criterios paper→shadow→live | P3 | DEFERRED | Evidencia operacional y aprobación humana |
| D-050 | Alpha incremental y nuevos Challengers sobre datos alternativos tras alcance V1 | P4 | DEFERRED | No sustituye D-018/D-033: taxonomía, PIT y selección de fuentes V1 son P0/P1 |
| D-051 | Opciones, shorts, leverage, futuros, cripto y regímenes avanzados | P4 | DEFERRED | Cambio de alcance y aprobación humana futura |

## Reglas de cierre

Una decisión abierta pasa a `RESEARCHING` al iniciarse una tarea R; a `READY_FOR_DECISION` cuando hay comparativa, evidencia, riesgos y recomendación; a `DECIDED` tras registrar resultado, aprobador y ADR cuando corresponda. El dueño aprobó D-012 **solo en arquitectura conceptual** y D-017 en frontera G1+G2; debe aprobar D-008 (selección y arquitectura final de estrategia), D-021, D-027, parámetros materiales de D-031 y cualquier gasto material o cambio de alcance. La priorización P1 de broker PAPER concilia el gate de diseño dependiente del broker de §3.8 con la lista P2 de §3.9: el **contrato abstracto** es P0 (D-013), la **selección concreta** es P1 porque el DoR exige stack y arquitectura completos; la prueba operativa pertenece a P2 (D-030).

**Aclaración de proceso 2026-10-05 (ADR-007):** propietario autoriza probes conductuales Team y shortlist sin acceso Plus; aceptación posterior específica para finalistas. Alternativa determinístico/local always-on + Codex intermitente explícitamente OPEN. D-020 `RESEARCHING`; D-024 `OPEN`; ninguna capability seleccionada.

**Hito R-006 2026-10-05:** [wave 04](research/R-006_probe_wave_04_2026-10-05.md), [wave 05](research/R-006_probe_wave_05_2026-10-05.md) y [shortlist RC0](research/R-006_shortlist_RC0.md) incorporan evidencia Team y recomendaciones Build-vs-Reuse. No cambia estado D-020/D-024, ni A+/G1+G2/riesgo conceptual, broker, Strategy V1 o umbrales. Plus gate reservado a finalistas.

**Estado vigente posterior:** [shortlist RC1](research/R-006_shortlist_RC1.md) y [matriz de aceptación](research/R-006_workload_acceptance_RC0.md) completan el paquete autónomo solicitado (RC0 pasos 1–2). [Wave 06](research/R-006_probe_wave_06_2026-10-05.md) conserva 8/10 admission v1 y 10/10 v2 tras aclaración, no garantía general; [Codex SDK](research/R-006_codex_sdk_findings_2026-10-05.md) nativo 7/7 smoke. D-034 RESEARCHING, D-020 RESEARCHING/D-024 OPEN. Próximo input de paquete: orientación arquitectónica candidata y habilitar Plus; no cierre/freeze final ni gasto.

**Estado vigente posterior — ADR-009, 2026-10-05:** propietario aprobó shortlist RC1 como cohorte candidata para Plus Acceptance, no selección final ni aprobación total de su dirección arquitectónica. D-020 RESEARCHING/D-024 OPEN. Primero R-028/D-037 P1 formaliza/proba onboarding y portabilidad; el nuevo requisito está aprobado y bloquea D-024/DoR. No repetir solicitud de aprobación de cohorte. Acceso Plus sigue pendiente; trabajo independiente de entitlement continúa.

**D-037 avance técnico:** contratos bootstrap/packaging RC0, seis paquetes documentales/shared y Skill propia. Dossier R-028 conserva cinco smoke Team y 31 checks offline; un cleanup Windows falla después de resultados. Fresh clone continúa como próximo hito autónomo. Requisito aprobado, diseño no congelado; target Plus/seguridad/final runtime pendientes.

**Estado vigente R-028 posterior:** paquete diseño/probes fresh clone completado, dossier §9 y perfil PARTIAL. Seis cadenas root+rol, dos smoke reales desde clone, 31 checks offline y completion 9 checks sin repetir inferencia; hashes Git portable separan EOL. D-037 RESEARCHING, D-020 RESEARCHING/D-024 OPEN; next input acceso Plus para GP/EB target, no nueva aprobación de cohorte ni freeze.

**D-027/D-034/D-037 vigencia posterior S2:** dirección aprobada, no controles finales. [S2 RC1](08_S2_isolation_spec_RC1.md), [gates separados](research/R-013_S2_acceptance_matrix_RC1.md), [ADM-01 administrativo](research/R-013_S2_administrative_gate_ADM01.md). D-025/026/028 mantienen motor/store/observabilidad seleccionados pendientes; contratos enlazan launcher/control y audit fuera del job. D-024 permanece RESEARCHING, no freeze por documentación. Strategy V1 OPEN.

## Revisión de granularidad S2 — 2026-10-06

El propietario mantiene seguridad técnica y separa blinding de topology OS. [ADR-012 revisado](decisions/ADR-012-agent-process-isolation-proposed.md), [comparativa](research/R-013_S2_variants_comparison_2026-10-06.md), [RC2](08_S2_agent_domain_contract_RC2.md). **Propuesta S2-B READY_FOR_DECISION; no finalizada.** D-027/D-024 RESEARCHING; D-020 disposiciones aprobadas intactas. Q-049 administrativo DEFERRED por negativa expresa; Q-051 es la próxima decisión material de dirección, sin permiso de setup. Los bloques anteriores de ADM-01 son antecedentes sustituidos. No cambio A+, G1+G2, riesgo/Strategy V1, Team PAPER/Plus PRE-LIVE, implementation lock o main.

## Confirmación S2-B — 2026-10-06, posterior a comparativa

Q-051 **DECIDED solo dirección candidata** por propietario: S2-B principal; S2-A condicionada a insuficiencia por job demostrada, S3 reserva si S2 no cumple seguridad. [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md). Actualizar contratos/perfiles y preparar laboratorio mínimo; siguiente gobierno es configuración administrativa concreta, no volver a pedir dirección. D-027/D-024 RESEARCHING, permisos/implementación/gasto/freeze no autorizados; ADM-01 continúa DEFERRED.

## Gate concreto preparado S2-B — 2026-10-06

Q-052 READY_FOR_DECISION, **no autorización aún**: [S2B-ADM-01](research/R-013_S2B_lab_ADM01.md), una cuenta temporal + nuevos recursos/policy canary + tests y rollback revisables. [Dossier](research/R-013_S2B_lab_preparation_2026-10-06.md) conserva 12 observaciones comunes y 2 privilegios, 14 SDDL sintácticos y preflight readonly; fuente FS solo preparada, no acceptance. Q-051 no reabierto; Q-049/ADM01 de tres cuentas DEFERRED. D-027/D-024 RESEARCHING, financieras/gasto/implementation/main intactos.

## Autorización S2B-ADM-01 — owner, 2026-10-06

Q-052 **DECIDED solo autorización exacta del laboratorio**, propietario administrador único. [Autorización](research/probes/r013-s2b-lab-execution/authorization.json), [runbook](research/R-013_S2B_owner_execution_runbook.md). Agent no eleva ni solicita secretos; prepara, verifica y ejecuta operaciones no privilegiadas. Ningún setup/FS PASS por la aprobación. D-027/D-024 abiertos, old ADM-01 withheld, no scope expansion, implementación o gasto.

## Checkpoint agéntico — 2026-10-07

[ADR-014](decisions/ADR-014-agentic-design-checkpoint-proposed.md) / [checkpoint](14_agentic_architecture_design_checkpoint_RC0.md) READY_FOR_DECISION de diseño material B-RT1, **no aprobado**. D-020 no se reabre; roles/capabilities maduros, D-024/D-027 requieren owner para aceptar realización candidata. D-037 diseño contractual propuesto junto con instancia/fingerprint, target acceptance sigue diferido. D-025/026/028/029/034/035 transversales siguen abiertos en Team; no ocultarlos como exclusivos target. PAPER_RUNTIME_ACCEPTED=false. Siguiente foco independiente Strategy V1/broker/data/engine/riesgo.

## Aprobación vigente R2 — ADR-015, 2026-10-13

Owner aprueba R2 conceptual y acotado; R1/P&L/controles independientes conservados. Menor R2 no autoriza ampliar perdedoras: señal/regla Champion, nueva evaluación integral y reservas reconciliadas obligatorias. p_auth pending/new y protección condicional conservados. Missing/invalid/unconfirmed/crossed stop sin fill verificado => UNCERTAIN, nunca riesgo0. Costes/pérdidas/claims sin doble conteo ni exposición oculta; casos ganancias/pérdidas/partial/top-up/gap/rapid-move R-027 RC1. Q-054 DECIDED, **D-035 global RESEARCHING**, fórmulas/params/pruebas siguen abiertas. Sin selección Strategy/broker, implementación, gasto o target acceptance. [ADR-015](decisions/ADR-015-remaining-risk-reference-R2.md).

## Gobierno siguiente — Q-055, 2026-10-13

[OOS O-B propuesto](research/D-011_OOS_policy_decision_RC0.md), alternativas O-A/O-C y [review](research/D-011_R-021_independent_review_2026-10-13.md) preparados. Q055 READY_FOR_DECISION scope conceptual; D011 permanece RESEARCHING hasta protocolo completo verificable. No aprobación por silencio ni por review. MATR conserva ventanas baseline; reserva confirmatoria INTEGRITY_UNKNOWN, no certify por aprobar O-B. Tiingo Starter REJECT sólo rol durable según investigación/licencia, no broker/data/engine/Strategy elegido. ADR015/R2 aprobación owner intacta.

## Aprobación vigente O-B — 2026-10-14

[ADR-016](decisions/ADR-016-strategy-evaluation-O-B.md) registra Q055 DECIDED conceptual; D011 global RESEARCHING, Strategy OPEN. Reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11; alternativa prospectiva con gobierno si contaminada. Ensayos incluidos descartes, suficiencia/INSUFFICIENT_EVIDENCE, comparabilidad, walk-forward/sensibilidad/costes/retrasos y horizonte/latencia/caducidad quedan exigidos antes de resultados. Ningún modelo/umbral/estrategia/broker/data aprobado; lock y target deferral vigentes. Continúa paquete financiero sin solicitar Plus/admin ni investigación agéntica general.

## Paquete financiero wave04 — 2026-10-14

D011 RESEARCHING: ADR016/Q055 DECIDED sólo O-B. [RC2](research/R-020_evaluation_protocol_RC2.md) concreta F0/F1/method/sample/registry y [horizonte](research/R-020_decision_horizon_latency_RC0.md); F0 NOT_FROZEN, reserve UNKNOWN. [Scorecard](research/R-020_comparable_candidate_scorecard_RC2.md) compara diseño/demanda de cinco candidatos, ninguno admitido/seleccionado. [Q056 objetivo económico](research/D-011_economic_endpoint_decision_RC0.md) READY_FOR_DECISION conceptual tras review, antes de definir efecto/muestra: A más retorno, B eficiencia retorno/riesgo recomendada, C demostrador operacional. No criterio numérico/modelo ganador fijado.

D021/022 siguen RESEARCHING con [wave timing](research/R-007_008_timing_evidence_2026-10-14.md): delayedSIP/feeds/deadlines/GTC/auth/presets y gates target. D023/025/026/028/029/033/034/035 mantienen pruebas/stack/retención/demanda restantes; libraries primitives no cierran esos scopes.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Wave05 — contrato económico y admisión externa, 2026-10-14

Q056 no se reabre. [RC3](research/R-020_economic_qualification_contract_RC3.md) propone NI, exceso cash y mejora de riesgo/guardrails AND, con inferencia/sample/multiple-testing pendientes; [Q-057](research/D-011_benchmark_qualification_decision_RC0.md) READY_FOR_DECISION de gobierno material de benchmark primario y espejos para la cohorte PRICE–MATR. D008 OPEN y D011 RESEARCHING, ninguna referencia/parametrización final aprobada. [Pairing](research/R-020_PRICE_MATR_pairing_spec_RC0.md) distingue comparación integral de ablations, ledgers divergentes y MODULE_ONLY.

R008 [cash admission](research/R-008_cash_benchmark_admission_RC0.md) separa yield/carry modelado/interés real. R021 [Form4RC2](research/R-021_Form4_semantic_admission_RC2.md) mantiene UNKNOWN de planes históricos y semántica por fila. Probes E3 19/19 y F2 13/13 son sintéticos/componentes; no alpha, datasets o target. Registry8 declaraciones/trials0 conserva hashes/EOL históricos, F0 incompleto. [Revisión](research/R-020_021_economic_independent_review_2026-10-14.md).

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Wave06 — benchmark book, estadística y fuentes

Q056/Q057 DECIDED en sus scopes. [Book K2](research/R-020_K2_benchmark_book_RC0.md) propone políticas reproducibles, targets/realizados, deriva/reinversión, clock/cash y beta/factores; [RC4](research/R-020_statistical_method_contract_RC4.md) fija estimandos/admission y streams económicos explícitos. NI/cash con coste operativo incremental de S; ES financiero net_trading; benchmarks no absorben overhead de agentes. Modelo/calibración/guardrails siguen pendientes; propuesta [Q058](research/D-011_economic_margins_proposal_RC0.md) presenta márgenes/efecto nuevos, no selección ni cierre D011.

[SEC RC3](research/R-021_SEC_availability_admission_RC3.md) y [fuentes wave03](research/R-008_sources_evidence_wave03_2026-10-14.md) actualizan derechos/history/availability sin admitir datasets o elegir vendor. [E4](research/R-020_E4_findings_2026-10-14.md)14/14 cálculos/componentes+piloto MC, no alpha; [M11 parcial](research/R-020_M11_repository_audit_RC0.md) no acredita integridad. Holdout UNKNOWN, implementación bloqueada/target diferido.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.

## Wave07 — protocolo, admisión y configuraciones propuestas

[RC5](research/R-020_evaluation_contract_RC5.md) especifica diseño de evaluación y MVgates, métodoNOT_ACCEPTED; B/K2/M1 no se reabren. [DataCards](research/R-020_dataset_cards_RC0.md)4cards y6ETFobligaciones, allNOT_ADMITTED. [Configs](research/R-020_PRICE_MATR_rule_configurations_RC0.md)2presets nuevos conIDs propios, stop/cutoff/expiry/slots/pause explícitos; target/risknums/broker/source OPEN, no Strategy aprobada. [Costscale](research/R-020_cost_scale_scenarios_RC0.md)20celdas hipotéticas, ningúnK seleccionado.

E5/E6 screeningCAGR/ES y nulidades8/8 y11/11, ninguna aceptación estadística; [findings](research/R-020_E5_findings_2026-10-14.md) y [review](research/R-020_wave07_independent_review_2026-10-14.md) persistidos. Registry10decl/0trials, historialraw+repairrevision conservados. [Q059](research/D-011_complementary_guardrails_proposal_RC0.md) READY_FOR_DECISION para nuevos controles DD/σ/reportes, no límitesRisk/modelo/datasets. D011RESEARCHING/F0incompleto, holdoutUNKNOWN/lock/targetdeferral.

## Vigencia G-R1 — ADR-020, 2026-10-15

[ADR-020](decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md): Q-059/G-R1 DECIDED en preferencia económica ex ante: no deterioro de DD frente a EW6-BH completo ni de volatilidad diaria frente al espejo K2 admisible. ES95/M1 primario y NI/cash/K2 conjuntos; recuperación/underwater/pérdidas/gaps/slippage/extremos obligatorios. DD exige estimando/horizonte/path/incertidumbre y aplicabilidad válidos; una trayectoria/bootstrap genérico no demuestra futuro. Volatilidad incluye upside/downside. Guardrails relativas no son límites absolutos Risk D-031. G-R2 no aprobado ni fallback. Estados separados y NO_STRATEGY_QUALIFIED; ningún método/dato/broker/Strategy/F0/implementación aceptado. Continuar P0/P1 financieros en checkpoints agrupados; holdout UNKNOWN/lock/targetdeferral.

| D-044 | Referencia económica nominal PAPER y sensibilidad de costes | P1 | DECIDED | ADR-021: USD10k principal, costes obligatorios en5escalas; sin funding/LIVE/riesgo/gasto aprobado |

## Referencia PAPER y cobertura de costes — ADR-021, 2026-10-15

[ADR-021](decisions/ADR-021-PAPER-economic-reference-capital.md): propietario fija nominalUSD10,000 antes de resultados y exige costes evaluados/reportados en las cinco escalasUSD2k/5k/10k/25k/50k, conservando20celdas hipotéticas previas. Todas las fuentes/modelos de coste admitidos se aplican a cada escala; UNKNOWN explícito, no0/omisión ni capital favorable elegido después. Principal10k no prometePASSuniversal ni exigePASSen5como nuevo gate implícito. Sin depósito/funding/capitalLIVE/gasto/risknumbers; costes reales/método/data/Strategy no aceptados. HoldoutUNKNOWN/lock/targetdeferral.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](research/R-020_preregistration_readiness_RC6.md), [configEQ3](research/R-020_configuration_completion_RC1.md), [DataCards](research/R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](research/R-007_protection_dependency_contract_RC2.md), [RiskRC2](research/R-027_risk_formula_spec_RC2.md) y [engine/QE0](research/R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](research/R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.

## 2026-10-23 — consultas externas: preparación aprobada, entrega por propietario

El propietario aprobó preparar [ambos correos definitivos](research/R-008_vendor_clarification_requests_RC0.md) y los enviará personalmente desde correo personal. Envío automático desde cualquier cuenta NO autorizado; el antiguo gate de autorización/remitente deja de ser la próxima aprobación requerida. [Ledger](research/vendor_inquiries/status.json): READY_FOR_OWNER_SEND/NOT_SENT, 0envíos; EXTERNAL_CLARIFICATION_PENDING sólo al confirmar envío real de cada consulta. Respuesta genérica no admite datos: licencia aplicable, cobertura, calidad y evidencia técnica/PIT verificable siguen independientes. Continuar los P0/P1 financieros sin esperar respuesta; no nuevo gasto/cuenta/trial/credenciales/selección. implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED e INTEGRITY_UNKNOWN.

## 2026-10-23 — envío personal confirmado por declaración del propietario

Twelve Data y EODHD: **AWAITING_VENDOR_RESPONSE**, equivalente a EXTERNAL_CLARIFICATION_PENDING; 2envíos declarados, no verificación de buzón. [Ledger](research/vendor_inquiries/status.json) separa fecha de declaración2026-10-23 de fecha exacta de envío UNKNOWN/no indicada. Sin respuesta ni derechos de uso/dataset admitido; no envío automático autorizado. No esperar respuestas para continuar preparación financiera P0/P1.

## Wave10 — cierres técnicos acotados y siguientes decisiones

D035-T1 DECIDED (Plan Architect, revisión crítica): cantidades/lifecycle/encumbrances separados en RiskRC3. D011-T1 DECIDED sólo grafo F0 research versus aprobación de diseño/DoR y promoción operacional; no Champion previo a implementación. Parents D011/D035 RESEARCHING. Reglas EQ3 completadas en capa de hipótesis, no binding financiero ni selección.

Q061 READY_FOR_DECISION/P0: claim final DD-E condicionado frente a DD-P/claim pendiente, con evidencia matemática E8. No otra autorización para investigar ni reapertura de G-R1. D030/D031 se descomponen trazablemente: diseño P1, aceptación/calibración integrada P2; no nueva política de riesgo aprobada. D023 recomendación LEAN condicionada, no seleccionado desde compilación. [Matriz completa](15_financial_design_readiness_RC0.md).

## Q-061 aprobado — ADR-022, 2026-10-23

Propietario aprueba **DD-E condicionado** como interpretación inferencial G-R1: diferencia esperada de máximos DD frente a EW6-BH completo bajo P/H/I0 y supuestos explícitos, tolerancia0/upperbound válido≤0. Reportar DD observado/distribución/probabilidad/magnitud de deterioro/cuantiles cuando fiables; mejoras extremas infrecuentes con mayoría peor son limitación material visible, no «menor riesgo» sin contexto. DD-P no aprobado, sin umbral implícito. Separar incertidumbre datos/parámetros/modelo/MC; no bootstrap genérico o simulación abundante sin validación. Otros endpoints/Risk/gobierno independientes; no promoción automática. [ADR022](decisions/ADR-022-conditional-expected-drawdown-claim.md).

Q061 DECIDED; D011 RESEARCHING/método no admitido. No otra pregunta DD conceptual; completar pruebas viables acotadas y priorizar datos/broker/engine/reglas/Planv1. Holdout INTEGRITY_UNKNOWN, implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED.

## Wave11 — selección de familias lista para propietario

[Q062](research/D-021_023_PAPER_stack_decision_RC0.md) READY_FOR_DECISION P1: paqueteA Alpaca Paper Only + LEAN source, B IBKR+LEAN, C Alpaca+Nautilus. No selección/aprobación por anticipado. Source/SDK/modelos nativos son reuse/adapt; críticas y aceptación de pin/datos/mapping/seguridad/target separadas.

QL2nativo9checksPASS acredita comportamiento default, no paridad. KD1 loginPASS/6ERROR y diagnóstico401 conservados, sin raw ni cobertura aceptada. Claim/report DD especificado ADR022, método/modelo/suficiencia abiertos; no más campaña DD general sin motivo material. MasterRC0 integra aprobaciones/propuestas y readiness16 identifica dependencias, no cierra DoR. D030/031 diseñoP1 y validaciónP2, RiskRC3 intacto.

## 2026-10-28 — Q-062 aprobado y proveedores actualizados

El propietario aprueba Alpaca Paper Only + LEAN source como **familias de diseño PAPER**, IBKR/Nautilus reservas: [ADR-023](decisions/ADR-023-paper-broker-and-backtesting-families.md). B1–B5/QP1–QP10, pin/modelos/protección efectiva/target siguen pendientes; sin cuentas, gasto, implementación o LIVE. B3 no admisible implica no entradas.

[Evidencia comercial](research/R-008_vendor_evidence_and_plan_scope_RC1.md) disponible desde 2026-10-28, fecha real de recepción UNKNOWN y correos originales no inspeccionados. Twelve=VENDOR_INFORMATION_REQUESTED, aclaración del propietario pendiente de envío. EODHD=VENDOR_RESPONSE_RECEIVED / PLAN_SCOPE_CLARIFICATION_PENDING / TECHNICAL_ADMISSION_PENDING; todos los datasets NOT_ADMITTED, raw a IA externa DENY_UNCONFIRMED. Tres precios públicos19.99/29.99/99.99 incorporados a las cinco escalas; se prioriza EOD económico si cumple. No se espera respuesta para avanzar research.

## Cierre técnico acotado D035-T2 y siguiente gobierno — 2026-10-28

D035-T2 DECIDED sólo contrato matemático: caps/min/búsqueda binaria requieren monotonía/separabilidad y baseline/presupuesto restante conocidos; un oráculo finito no valida solver general. R4/RC4 especifican el alcance sin cambiar política. Parent D035 sigue RESEARCHING.

[Q-063](research/D-025_026_PAPER_workflow_storage_decision_RC0.md) READY_FOR_DECISION de dirección condicionada de familias/huella, no cierre de stack/suficiencia. APS3 acotado+PostgreSQL recomendado; Temporal+Postgres reserva alternativa. D1 aclara trazablemente que envelope/latencias/RPO/RTO/retención y evidencia siguen P1 antes de freeze. B-RT1/trust/autoridad no cambian, sin administración o implementación.

## D-023 — pin no admitido tras auditoría concreta

Familia ADR023 sigue DECIDED. QL4 demuestra fallo de helper overwrite; requisito P1 de remediación/exclusión probada, no waiver por build. QL5 captura01TIMEOUT y02=CONTINUATION_INCOMPLETE_OR_FAILED_NO_REMEDIATED_HOST_ACCEPTANCE. Source graph/rebuild/fixtures no admiten engine integrado o pin; no se acepta riesgo residual automáticamente. Q063 no cambia este gate.

## 2026-10-29 — Q-063/A aprobado

[ADR-024](decisions/ADR-024-bounded-scheduling-and-durable-stores.md): dirección condicionada APScheduler3.x acotado + PostgreSQL, Temporal self-hosted reserva. Q063 DECIDED; D025/026 RESEARCHING para especificación/configuración/suficiencia. Scheduler sólo wakeups; ledger durable, permisos efectivos C/F, fallos/recovery/fencing y WAL/fsync/backup/RPO/RTO requieren evidencia. No exactly-once broker por outbox ni aceptación PostgreSQL desde SQLite. Lifecycle finito; escalamiento de complejidad obliga recomparar Temporal. No cuenta/gasto/configuración/implementación. Continúan pin LEAN, B3, bindings/riesgo/datos y readiness, sin esperar proveedores ni target.

## Estado financiero vigente — 2026-10-29

[Checkpoint18](18_financial_hardening_checkpoint_RC0.md): Q063/A DECIDED ADR024; APS3 sólowakeups/PostgreSQL durable, Temporal reserva. Configuración/suficiencia P1 pendientes. LEAN source y reparación de extracción contrastadas con capturas/errores preservados; pin no aceptado. B3 no admitido; Q064 READY_FOR_DECISION de política PF versus cobertura nativa. RiskRC5/lifecyclePG/D2 especificados con pruebas acotadas, no implementación/SQL/Postgres/target. Datos4+6NOT_ADMITTED,12hipótesis/0trials, capital10k/costes5escalas, método noaceptado y holdoutUNKNOWN. R006/010/013 fundamentales no reabiertos.
