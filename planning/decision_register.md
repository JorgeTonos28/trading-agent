# Decision Register — inicialización

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
| D-010 | Especificación de MATR_V1 como candidato/benchmark | P0 | RESEARCHING | RC0 en `02_MATR_V1_spec.md`; no es contrato de implementación salvo selección D-008 |
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
| D-021 | Broker PAPER y elegibilidad real para residente de RD | P1 | RESEARCHING | Wave documental 2026-10-07 Alpaca/IBKR/Tradier; alternativas restantes, gates B1–B5 y aprobación humana pendientes. No cuenta/API operativa ni selección |
| D-022 | Proveedor de históricos y datos para candidatos Strategy V1; validador secundario | P1 | RESEARCHING | Wave 2026-10-07 feed/clock/fill/historia; cobertura/PIT/ajustes/licencia/coste y muestras cruzadas pendientes. No dataset admitido |
| D-023 | Motor(es) de investigación/backtest event-driven | P1 | RESEARCHING | R-009 RC0: LEAN engine source vs CLI comercial, Nautilus stable vs docsRC y QP1–10. Ningún engine seleccionado/instalado; coste/pin/benchmark pendientes. |
| D-024 | Runtime/topología/plugin agéntico PAPER | P1 | DECIDED | ADR-014 aprobado owner 2026-10-13 en scope B-RT1; diseño fundamental DESIGN_DECIDED. Target R-030 TARGET_ACCEPTANCE_DEFERRED, operacional NOT_IMPLEMENTED. Mecanismos/versiones finales requieren aceptación, sin diseño abierto por host-specific. |
| D-025 | Workflow durable, scheduler y política de recuperación | P1 | RESEARCHING | Contrato 08: automatic triggers/outbox, attempts/leases/epoch, máximo una recepción, fail-closed/retries acotados. Temporal candidato baseline vs APScheduler/OS; probes de semántica y motor, no selección final. |
| D-026 | Almacenamiento, eventos, identidad/versionado y audit trail | P1 | RESEARCHING | Contrato 08 audit; PostgreSQL/Parquet/DuckDB/Redis baseline por verificar. SQLite toy no selecciona store. Restore/incarnation y receipts perdidos explícitos; motor final/retención/license pendientes. |
| D-027 | Seguridad/permisos y secretos | P1 | DECIDED | Contrato de diseño B-RT1 DESIGN_DECIDED owner ADR-014; permisos efectivos SI/BL/RB/VP NOT_TESTED y target R-030 diferido. Mecanismos candidatos sustituibles con gobierno; lab diferido, no admin INFOTEP. |
| D-028 | Observabilidad, alertas, runbooks, backups y despliegue PAPER | P1 | RESEARCHING | Contrato 08 audit/versiones: métricas/denominadores, runbooks, release/rollback/epoch; SLO/RPO/RTO finales y restore del motor seleccionado pendientes. Sin main/tag automático. |
| D-029 | Estrategia de tests y evals de agentes con criterios de aceptación | P1 | OPEN | R-006 workload/matriz y wave 06 especifican/proban spine por rol; suite general financiera/agentic/integration y revisión independiente aún pendientes, no cierre por 10 fixtures |
| D-034 | Esquema detallado, aislamiento y evaluación PIT de `ShadowPortfolioProposal` | P1 | RESEARCHING | ADR-001 fija obligación funcional; contratos RC0 común/shadow especifican caller confiable, snapshots ciegos pareados, target quantity y lineage, estados y comparación local vs trayectoria contrafactual. R-026 conserva gates de aislamiento real/engine/metrics; probes sintéticos no cierran evaluación |
| D-035 | Especificación técnica verificable de controles de riesgo compuestos | P1 | RESEARCHING | ADR-015 owner aprueba referencia R2 y condiciones; Q054 DECIDED. Fórmulas finales/units/inputs/params/fees/claims/escenarios y pruebas pendientes; no D-035 completo cerrado ni auto-topup de perdedoras. |
| D-037 | Bootstrap, portability y agent packages | P1 | DECIDED | Ruta/contratos de diseño DESIGN_DECIDED ADR-009/014; fresh clone y aceptación Plus/PC personal R-030 diferidos antes de implementación. Sin dependencia de chat, cuentas/sesiones por rol no impuestas. |
| D-036 | Política económica por fase y adquisición de Skills/metodologías | P0 | DECIDED | Propietario, 2026-10-02, ADR-008: calidad/fiabilidad/capacidad al menor coste razonable; PAPER zero/low incremental cost first, LIVE economic value/unit economics; Skills/templates gratuitos/incluidos/propios; pagos investigables, aprobación explícita antes de contratar o gastar |
| D-033 | Proveedores Smart Money/alternative data y clasificación Build vs. Reuse por dataset | P1 | RESEARCHING | R-025; scorecards PIT, API, cobertura, calidad, latencia, licencia y coste; aprobación humana si gasto material |
| D-030 | Ejecución PAPER concreta: tipo de orden, stops, slippage y fill parity | P2 | OPEN | Protocolo antes de paper autónomo; decisión puede afectar D-010/011 |
| D-031 | Umbrales PAPER calibrados y kill switches ensayados | P2 | OPEN | Evidencia backtest/paper y aprobación humana de política |
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
