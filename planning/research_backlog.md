# Research Backlog v0 — 2026-10-01

**Vigencia aprobada — 2026-10-13, ADR-014 / propietario:** `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` en el alcance capacidades/roles/fronteras/integración B-RT1. `design_status=DESIGN_DECIDED`; `TARGET_ACCEPTANCE_DEFERRED`; `PAPER_RUNTIME_ACCEPTED=false`; `implementation_locked=true`. Un Runner, control confiable externo, core/secretos fuera AI, aislamiento/contexto mínimo por job, allowlists, identidad/lifecycle por attempt y admisión/audit externos son el contrato aprobado. Keyring, HOME readonly, token, desktop, IPC carrier y launch exactos son **mecanismos candidatos sustituibles**, no invariantes irreversibles; cambios preservan fronteras/autoridad con evidencia y gobierno correspondiente. R-030 acepta eficacia en Plus/PC personal. Investigación agéntica fundamental Team completada; no expandir R-006/010/013 por refinamiento indefinido. LIVE UNKNOWN; residuos H7 conservados sin evasión de policy.


> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Antecedente — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Prioridad: P0 arquitectura, P1 implementación, P2 paper autónomo, P3 live, P4 futuro. Cada investigación produce un dossier con fuentes fechadas, hechos frente a supuestos, alternativas, criterios, coste/licencia, pruebas cuando proceda, riesgo, recomendación y enlace a decisión/ADR. Ningún candidato citado en la hoja queda seleccionado por aparecer aquí.

| ID | P | Cierra | Investigación / prueba y entregable |
|---|---|---|---|
| R-019 | P0 | D-009 | DECIDED / extracción funcional completada 2026-10-07: dossier, mapa conservar/modificar/separar/descartar y rule cards revisados independientemente. Claims NO VERIFICADOS. Reglas propias/datos/validación siguen R-020/021/025; Strategy V1 OPEN. Seguimiento de fuente solo si resuelve una decisión nuestra. |
| R-020 | P0 | D-008/011 | RESEARCHING: CandidateRules RC1 VID-CONG/F4/13F/PRICE propios + MATR benchmark; episodio/lotes/partial/split/params y datos todavía OPEN. Sin backtest/selección. |
| R-021 | P0 | D-014/018/008 | RESEARCHING: E1 EdgarTools5.62.0 offline7/7table-only, factoryerror y ADAPT/WRAP candidato; sin dataset admitido. Factibilidad PIT para **familias de señales externas** que puedan alimentar V1: timestamps de evento/publicación/recepción, cobertura histórica, derechos y primera operación posible. Congreso y alertas de terceros son casos, no el conjunto completo; coordinar con R-023/025. |
| R-022 | P0 | D-015/016/018/019 | DECIDED: contrato PAPER V1 RC1 y ADR-001 cierran A+ D-015/016/019; ADR-005 cierra roles/admisión abstracta D-018, mientras R-021/025 prueba datasets. |
| R-023 | P0 | D-018/014 | DECIDED en contrato abstracto ADR-005/`06_external_signal_admission_RC1.md`: familias separadas, roles graduados y gates PIT/licencia/OOS; R-021 y R-025 siguen pruebas por dataset/proveedor. |
| R-024 | P0 | D-019/015/016 | DECIDED en alcance funcional: contrato RC1 y 06_pedagogical_contract_RC0 detallan informes/curriculum §55 y fidelity/causas/estados; formato propuesto sin implementación. Privacidad, reports/export/learning/complete educational evals P1/P2 pendientes. |
| R-001 | P0 | D-010/011 | RESEARCHING: MATR_V1 RC0 es ficha candidata, no Strategy V1 seleccionada; faltan convenciones, datos, timing y protocolo OOS comparativo. |
| R-002 | P0 | D-012/017 | DECIDED en alcance conceptual: D-017/ADR-002 G1+G2 y reanudación humana; D-012/ADR-006 opción B compuesta. Umbrales, escenarios, fórmulas concretas y pruebas siguen D-031/D-021/026/030. |
| R-003 | P0 | D-013/015 | DECIDED en contrato abstracto: `04_order_contract_RC1.md` y ADR-003 fijan identidades, eventos, autorización, `UNKNOWN` y G2; semántica/probes del broker candidato siguen D-021/030/031. |
| R-004 | P0 | D-014 | DECIDED en contrato abstracto: `05_data_contract_RC1.md` y ADR-004 fijan clocks por canal, `eligible_from`, revisiones y ajustes as-of; muestras/delays/proveedor siguen R-021/025/008. |
| R-005 | P0 | D-016 | DECIDED en alcance: contrato RC1 §5 mapea B0–B7 y §57; traceability requisito→test y umbrales detallados permanecen P1/P2 antes del DoR. |
| R-006 | P0 | D-020/024 | FUNDAMENTAL DESIGN COMPLETE owner ADR-014 2026-10-13; approved RC2 dispositions. Continuous reuse checks only for new needs/material evidence, no indefinite wave expansion. Target Plus/personal acceptance R-030 deferred. |
| R-007 | P1 | D-021 | RESEARCHING: [wave 01](research/R-007_008_provider_evidence_wave01_2026-10-07.md) verifica docs Alpaca/IBKR/Tradier, feed/fills y rutas RD sin cuenta/KYC. Todos candidatos abiertos incl. tastytrade/TradeStation/otros; order/protection/stream/recovery/licence scorecards y ADR humano pendientes. |
| R-008 | P1 | D-022 | RESEARCHING: [wave05 acciones/PIT](research/R-008_alternative_actions_PIT_wave05_2026-10-23.md), matriz CA01–09 NOT_EXECUTED y rutas por ventana; [consultas finales](research/R-008_vendor_clarification_requests_RC0.md) READY_FOR_OWNER_SEND, envío automático prohibido. Licencia/cobertura/quality/PIT/precio reales pendientes; no dataset admitido ni espera global de respuestas. |
| R-009 | P1 | D-023 | RESEARCHING: R-009_backtesting_reuse_RC0.md LEAN raw vs CLI pago, Nautilus stable vs2.x docs; QP1–10 synthetic paridad protocolo NOT_TESTED, ningún engine seleccionado. |
| R-010 | P1 | D-024 | DESIGN_DECIDED ADR-014 in agentic integration scope. Native mechanism/auth/runtime/host/quota/recovery acceptance R-030 deferred; no new fundamental Team design research. |
| R-011 | P1 | D-025 | Workflow/recovery 08: eventos/calendario automático, outbox, estados/versiones, leases/expiry/concurrencia, epoch. Temporal baseline investigado, APScheduler/OS alternativos. Probes toy/motor no seleccionan tecnología; integración final pendiente. |
| R-012 | P1 | D-026 | Storage/audit 08: baseline PostgreSQL/Parquet/DuckDB/Redis, commit durable y immutable evidence, hashes no autenticación, restore/lost receipts. SQLite crash/backup/race solo probe. Motor final/cost/retención por cerrar. |
| R-013 | P1 | D-027 | DESIGN_DECIDED security contract S2-B/B-RT1; concrete mechanisms candidates. SI/BL/RB/VP and lab DEFERRED_TO_TARGET_PAPER_HOST; no admin INFOTEP or security PASS. |
| R-014 | P1 | D-028/029 | Métricas/runbooks/deploy 08 y revisión independiente IR-01–07, remediación documental/probes. H3 cola virtual revela bloqueo no preemptivo, no cuota/capacidad real. Protocolos/operación integrada y full evals pendientes. |
| R-015 | P2 | D-030/031/032 | Probes y calibración PAPER: orden siguiente sesión, brackets/stops, fills parciales, incidentes y gate de autonomía. |
| R-016 | P3 | D-040/041/042 | Broker live, jurisdicción, costos, impuestos/documentación, capital, disaster recovery y gates paper→shadow→live. |
| R-017 | P4 | D-050 | Investigación **incremental futura** de alpha/Challengers para familias externas que no entren en alcance V1; factibilidad arquitectónica y selección de fuentes V1 se adelantan a R-021/023/025. |
| R-025 | P1 | D-033/020/022 | RESEARCHING: [wave 01](research/R-025_provider_evidence_wave01_2026-10-07.md) y probe metadata público Quiver sin auth. SEC/Quiver/UW/Capitol/especialistas abiertos; clocks existentes no prueban PIT, rights/historia/coste/utilidad por dataset pendientes. |
| R-026 | P1 | D-034 | RESEARCHING: contratos RC0 común/shadow especifican schema spine, contexto ciego pareado, targets/linaje, comparador local vs trayectoria acumulativa y métricas. Wave 06 focalizada preregistrada; aislamiento real, simulator/fills/costs/datasets y pre-registro con Strategy V1 siguen abiertos. Reutilizar jsonschema/Decimal en probes y evaluar engine R-009 antes de BUILD. |
| R-028 | P1 | D-037/020/024/027/029 | DESIGN_DECIDED bootstrap/portability/packages ADR-014; captured Team/fresh-clone research preserved. Target EB/TE acceptance R-030 deferred before implementation. |
| R-027 | P1 | D-035 | RESEARCHING: ADR-015 R2 referencia conceptual DECIDED; escenarios RC1 explicitan ganancias/pérdidas/partial/top-ups/gap/rapid moves y UNCERTAIN jamás0. Fórmulas/fees/cash/mappings/concurrencia/pruebas/params pendientes, no cierre entero. |
| R-018 | P4 | D-051 | Opciones/short/leverage/cripto/futuros/regímenes avanzados: investigar solo tras alcance PAPER. |
| R-029 | P3 | D-039/024/037/040/042 | SUPERSEDED en premisa Team→Plus exclusivamente PRE-LIVE por ADR-013. Ficha/evidencia histórica preservadas. Plus es target PAPER R-030; LIVE UNKNOWN. |
| R-030 | P1 | D-043/024/027/037 | TARGET_ACCEPTANCE_DEFERRED: contratos diseñados ahora, ejecución personal Windows/Plus antes de implementación, integración/carga P2 antes de PAPER. `research/R-030_target_paper_environment_acceptance_RC0.md`. |

## Protocolo de Capability Discovery (R-006)

Por cada capacidad se registrará `EXISTS`, `AVAILABLE_IN_RESEARCH_ENVIRONMENT`, `AVAILABLE_IN_PAPER_TEAM`, `AVAILABLE_IN_FUTURE_PLUS`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE`, `SELECTED` por separado; Tier, versión/fecha, fuente primaria, licencia/portabilidad, permisos, datos transmitidos, pruebas y disposición `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT` por fase. Vigencia ADR-013: Team/INFOTEP research; Plus/PC personal target PAPER; LIVE UNKNOWN. Campos actuales y aplicabilidad en `13_environment_evidence_applicability.md`; Team no prueba Plus. R-030 difiere aceptación target antes de implementación sin bloquear investigación. `SELECTED=false` hasta ADR; `unknown` no se interpreta como `false`. IA/agentes solo OpenAI y Anthropic bajo ADR-007. ADR-008 autoriza estudiar pagos y exige aprobación antes de contratar/gastar; el presupuesto PAPER no veta LIVE. Ninguna Skill/plugin/MCP recibe autoridad de broker por instalarse.

## Política económica transversal R-007–014/025/026 y capabilities futuras

Aplicar [ADR-008](decisions/ADR-008-economic-policy-by-phase.md) y [scorecard común](economic_scorecard.md) en cada ficha: `PAPER_V1_VIABLE_FREE`, `PAPER_V1_COST`, `LIVE_COST`, `FREE_ALTERNATIVE`, `PAID_INCREMENTAL_VALUE`, `ECONOMIC_JUSTIFICATION_REQUIRED`, fijo/variable/mensual/escala, lock-in, beneficio y condición para pagar. PAPER prioriza suficiente calidad a bajo coste incremental; LIVE economía unitaria y valor operativo/retorno esperado con incertidumbre. Templates/Skills no se compran; dependencias se evalúan aparte. Brokers, [market data](research/market_data_selection.md) y Smart Money tienen tablas iniciales; storage/infra/observabilidad y nuevos candidatos incorporan el esquema antes de preselección.

Orden vigente 2026-10-07: contratos financieros abstractos D-012–019 establecidos; D-020 disposiciones aprobadas, R-006 MATURE_FOR_DESIGN_DECISION y Q-053/ADR-014 checkpoint de diseño material pendiente, target R-030 diferido. **Foco principal pasa a R-020/021/001, R-007/008/025/009 y R-027:** Strategy V1, datos/PIT, brokers, backtest y fórmulas riesgo. D-009 extracción completada no selecciona estrategia. R-010–014 transversales siguen motores/storage/ops/evals con demanda financiera; no ocultar trabajo diseñable como aceptación exclusiva Plus. R-015 precede PAPER autónomo; LIVE separado.

**Avance 2026-10-02:** [wave 03](research/R-006_probe_wave_03_2026-10-02.md) probó protocolo/discovery efímero en Team sin inferencia; el [gate Plus RC0](research/R-006_plus_runtime_gate_RC0.md) detalla lo pendiente. Actualización 2026-10-05: ejecutar ahora comparación conductual y shortlist en Team; no esperar Plus. El Plus Acceptance Gate verifica después únicamente diferencias de acceso/operación de finalistas, reutilizando evidencia Team. D-020/D-024 no se cierran.

**Hito actual 2026-10-05:** [shortlist RC1](research/R-006_shortlist_RC1.md) tras contratos/workload y wave 06: 10 turnos focalizados, 8/10 checker original vs 10/10 tras aclaración de cita, 39 checks locales y SDK nativo 7/7 smoke. Pasos 1–2 especificados/probados en su alcance sintético, workload target **no ejecutado**. Siguiente acción de paquete: orientación candidata y acceso Plus. Mantener R-020/007–014/025 y validación financiera/educativa/review/seguridad en cola; no etiquetarlos como exclusivos Plus ni inferir cierre de R-006 final.

**R-028 endpoint autónomo completado:** contratos RC0, six role packages/shared/Skill, 31 checks offline, five native fixture smoke y fresh clone commit 9e0dbed: metadata 6 + smoke 2; completion 9 checks tras KeyError sin inferencia repetida. Readiness research PARTIAL. R-028 RESEARCHING hasta ruta target/gates e integración final; D-037 no cerrado. Siguiente acción requiere acceso Plus; investigación independiente de Preparation permanece en cola.

## S2-B dirección confirmada — 2026-10-06

R-013 continúa autónomo en especificación/preparación no administrativa bajo S2-B aprobado. Proponer laboratorio mínimo de una identidad base, recursos canary y contextos por job; detallar positivos, negativos, límites, coste y reversión. No S2-ADM-01 ni users/ACL/firewall/credentials hasta gate concreto. D-027/D-024 abiertos; no Plus ni implementación.

## R-013: paquete autónomo de preparación completado — 2026-10-06

[Laboratorio/gate S2B-ADM-01](research/R-013_S2B_lab_ADM01.md) y [dossier](research/R-013_S2B_lab_preparation_2026-10-06.md): una cuenta y canaries, LF01–12 con mapping/manual/positivos, source/plan pinados y rollback. Memoria/common-SID/privilegios + sintaxis14 y readonly ejecutados; FS/native/admin NO. Q-052 DECIDED solo permiso temporal recibido. Continuación efectiva requiere acción owner Windows UI/admin dentro del scope; D-027/D-024 abiertos y R-013 no cerrado. A/S3 condicionales, no setup/elevación por source ni autoridad financiera nueva.

## Cierre del paquete de diseño independiente — 2026-10-07

R-006 MATURE_FOR_DESIGN_DECISION, D-020 direction preservada; R-010/R-013 scope de arquitectura candidato listo para owner con [B-RT1/checkpoint](14_agentic_architecture_design_checkpoint_RC0.md), no PAPER_RUNTIME_ACCEPTED. B1 16 casos; H7 Temporal redelivery y cleanup parcial/env-helper caveat; H8 calendario persistente 6 criterios. [Comparación engines/stores](research/R-010_workflow_storage_comparison_RC1.md). R-028 binding/bootstrap contractual completo para revisión, target gates R-030 diferidos.

R-011/R-012/R-014/026/027 siguen P1 transversales: workload Strategy V1, elección engine/store, datos/retención/SLO y protocolos/fórmulas. No requieren Plus para diseño. Revisión independiente incorpora repairs de propiedad/launch/auth/WinCred/instance; aprobación B-RT1 es Q-053. No cerrar R-006 discovery permanente: necesidades nuevas requieren reuse check.

Wave02 actual: referencias y endpoint financiero en secuencia_preparacion.md y R-020_027_independent_review_2026-10-13.md. R-006/010/013 diseño fundamental completo, target R-030 diferido. Q-054 próximo gobierno, no Plus/admin institucional.

## Aprobación vigente R2 — ADR-015, 2026-10-13

Owner aprueba R2 conceptual y acotado; R1/P&L/controles independientes conservados. Menor R2 no autoriza ampliar perdedoras: señal/regla Champion, nueva evaluación integral y reservas reconciliadas obligatorias. p_auth pending/new y protección condicional conservados. Missing/invalid/unconfirmed/crossed stop sin fill verificado => UNCERTAIN, nunca riesgo0. Costes/pérdidas/claims sin doble conteo ni exposición oculta; casos ganancias/pérdidas/partial/top-up/gap/rapid-move R-027 RC1. Q-054 DECIDED, **D-035 global RESEARCHING**, fórmulas/params/pruebas siguen abiertas. Sin selección Strategy/broker, implementación, gasto o target acceptance. [ADR-015](decisions/ADR-015-remaining-risk-reference-R2.md).

## Paquete financiero wave03 y endpoint — 2026-10-13

R020 semánticas comunes RC1, R021 E1 ejecutado y R008retención RC1 completados en scope; [review](research/D-011_R-021_independent_review_2026-10-13.md) y [Q055O-B](research/D-011_OOS_policy_decision_RC0.md) con repairs P1/P2 documentados. R008 Starter durable REJECT, alternativas restantes sin suficiencia certificada. R020/R021/D011 siguen investigación global; siguiente gobierno material Q055 arquitectura de evaluación, no Plus/admin ni nueva ronda agéntica. Tras decisión: CandidateConfigs, criterios/costs/cobertura antes de resultados, fichas fuente/broker restantes, engine/QP, risk formulas/storage/ops por demanda. No esperar target para investigar; backtests/aceptación operativa se realizan en PC personal.

## Aprobación vigente O-B — 2026-10-14

[ADR-016](decisions/ADR-016-strategy-evaluation-O-B.md) registra Q055 DECIDED conceptual; D011 global RESEARCHING, Strategy OPEN. Reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11; alternativa prospectiva con gobierno si contaminada. Ensayos incluidos descartes, suficiencia/INSUFFICIENT_EVIDENCE, comparabilidad, walk-forward/sensibilidad/costes/retrasos y horizonte/latencia/caducidad quedan exigidos antes de resultados. Ningún modelo/umbral/estrategia/broker/data aprobado; lock y target deferral vigentes. Continúa paquete financiero sin solicitar Plus/admin ni investigación agéntica general.

## Wave04 autónoma — endpoint económico, 2026-10-14

R020: [RC2](research/R-020_evaluation_protocol_RC2.md), cinco fichas comparables en diseño/demanda, registry/exposure ledger/EvidenceCard y horizon/latency/freshness. EvidenceCard NULL conserva pendientes, no preregistro sellado. ProbeE2 statsmodels/arch19/19 sólo sintético, dataset/alpha/target NOT_TESTED. R007/008 timing fuentes primarias y economía/rights desconocidos documentados. [Review](research/R-020_evaluation_independent_review_2026-10-14.md) incorpora cuatro P1 y dos P2 reparados.

Q056 READY es el siguiente gobierno material antes de efecto/muestra/endpoint; D008/011 siguen abiertos. Después: objetivo→EvidenceCard numérica/método validado→Configs/data rights/PIT/costs/latency→F0→comparación/selección de diseño→F1/confirmación y target/DoR en scopes propios. No API paga/Plus/admin requerida para el trabajo de diseño independiente; ejecutables/backtests de estrategias y carga real target PC personal.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Wave05 — paquete autónomo y dependencia económica

R020 RC3/PAIR-01/02, R008 cash y R021 semántica Form4 completados en scope documental con E3/F2 y [review](research/R-020_021_economic_independent_review_2026-10-14.md). No investigación global cerrada: fuentes/PIT/rights/returnmodels, métodos/precision y StrategyConfig aún abiertos. Próximo gobierno material [Q057](research/D-011_benchmark_qualification_decision_RC0.md), no Q056 repetido.

Después de esa referencia: fijar métricas candidatas/MethodApplicabilityCard, márgenes y mínimos justificados antes de resultados; completar fuente cash+ETF y Form4/amendments/firstdelivery/rights, broker/order matrix y engineparidad; fórmulas/operación por demanda. Target R030 sigue diferido, no Plus/admin aquí. El estudio plan-agnostic no ejecutado es alternativa registrada, no admisión ni sustitución de filtro S-F4-01.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Wave06 y dependencia siguiente

R020 bookK2/RC4/márgenes, M11 repositorio parcial y E4 completados en scope de diseño/probes; R008 nuevas alternativas y R021 canalSEC con PAC/índices/readiness. [Review](research/R-020_wave06_independent_review_2026-10-14.md) incorpora reparaciones de overhead/streams/targets. No cierre estadístico ni fuente; M11UNKNOWN. Siguiente gobierno numérico Q058, no preferencias abstractas.

Tras margen/efecto: guardrails económicos, MethodApplicability/calibración CAGR/ES/DD/familia/precision previa, CandidateConfig, price+actions+cash/datasetrights/as-of y broker/engine parity; formulas/reservas/workflow por demanda. No capital/source UNKNOWN=0 ni calibración por pilot. R030/Plus/PC personal diferido antes de implementación, no solicitud actual.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.

## Wave07 y frontera de gobierno

R020protocolRC5, DataCards/precios/cash/mirror/F4, rulepresets propuestos, costscale y E5/E6 completados en scope design/screen. Validacióninferencial MV01–08 aún abierta: ningún método se selecciona por tasa favorable. Fuente/rights/PIT/protección/targetnumeric siguen gates antes de F0. [Q059](research/D-011_complementary_guardrails_proposal_RC0.md) siguiente gobierno material; después calibración de guardrails/estimandos definitivos con precisión y familia previas, costos/escala/source y Configs financieras.

No backtests/marketdata/reserva ni cap/risknumeric aprobados. R009paridadengine y R007broker siguen por demanda, targetR030 separado antes de implementación. No solicitar Plus/admin institucional o nuevas preferencias B/K2/M1.

## Vigencia G-R1 — ADR-020, 2026-10-15

[ADR-020](decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md): Q-059/G-R1 DECIDED en preferencia económica ex ante: no deterioro de DD frente a EW6-BH completo ni de volatilidad diaria frente al espejo K2 admisible. ES95/M1 primario y NI/cash/K2 conjuntos; recuperación/underwater/pérdidas/gaps/slippage/extremos obligatorios. DD exige estimando/horizonte/path/incertidumbre y aplicabilidad válidos; una trayectoria/bootstrap genérico no demuestra futuro. Volatilidad incluye upside/downside. Guardrails relativas no son límites absolutos Risk D-031. G-R2 no aprobado ni fallback. Estados separados y NO_STRATEGY_QUALIFIED; ningún método/dato/broker/Strategy/F0/implementación aceptado. Continuar P0/P1 financieros en checkpoints agrupados; holdout UNKNOWN/lock/targetdeferral.

## Referencia PAPER y cobertura de costes — ADR-021, 2026-10-15

[ADR-021](decisions/ADR-021-PAPER-economic-reference-capital.md): propietario fija nominalUSD10,000 antes de resultados y exige costes evaluados/reportados en las cinco escalasUSD2k/5k/10k/25k/50k, conservando20celdas hipotéticas previas. Todas las fuentes/modelos de coste admitidos se aplican a cada escala; UNKNOWN explícito, no0/omisión ni capital favorable elegido después. Principal10k no prometePASSuniversal ni exigePASSen5como nuevo gate implícito. Sin depósito/funding/capitalLIVE/gasto/risknumbers; costes reales/método/data/Strategy no aceptados. HoldoutUNKNOWN/lock/targetdeferral.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](research/R-020_preregistration_readiness_RC6.md), [configEQ3](research/R-020_configuration_completion_RC1.md), [DataCards](research/R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](research/R-007_protection_dependency_contract_RC2.md), [RiskRC2](research/R-027_risk_formula_spec_RC2.md) y [engine/QE0](research/R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](research/R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.

## 2026-10-23 — consultas externas: preparación aprobada, entrega por propietario

El propietario aprobó preparar [ambos correos definitivos](research/R-008_vendor_clarification_requests_RC0.md) y los enviará personalmente desde correo personal. Envío automático desde cualquier cuenta NO autorizado; el antiguo gate de autorización/remitente deja de ser la próxima aprobación requerida. [Ledger](research/vendor_inquiries/status.json): READY_FOR_OWNER_SEND/NOT_SENT, 0envíos; EXTERNAL_CLARIFICATION_PENDING sólo al confirmar envío real de cada consulta. Respuesta genérica no admite datos: licencia aplicable, cobertura, calidad y evidencia técnica/PIT verificable siguen independientes. Continuar los P0/P1 financieros sin esperar respuesta; no nuevo gasto/cuenta/trial/credenciales/selección. implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED e INTEGRITY_UNKNOWN.
