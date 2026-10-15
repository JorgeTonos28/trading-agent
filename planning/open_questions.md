# Open Questions — inventario inicial

**Vigencia aprobada — 2026-10-13, ADR-014 / propietario:** `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` en el alcance capacidades/roles/fronteras/integración B-RT1. `design_status=DESIGN_DECIDED`; `TARGET_ACCEPTANCE_DEFERRED`; `PAPER_RUNTIME_ACCEPTED=false`; `implementation_locked=true`. Un Runner, control confiable externo, core/secretos fuera AI, aislamiento/contexto mínimo por job, allowlists, identidad/lifecycle por attempt y admisión/audit externos son el contrato aprobado. Keyring, HOME readonly, token, desktop, IPC carrier y launch exactos son **mecanismos candidatos sustituibles**, no invariantes irreversibles; cambios preservan fronteras/autoridad con evidencia y gobierno correspondiente. R-030 acepta eficacia en Plus/PC personal. Investigación agéntica fundamental Team completada; no expandir R-006/010/013 por refinamiento indefinido. LIVE UNKNOWN; residuos H7 conservados sin evasión de policy.


> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Antecedente ADR-011 — 2026-10-05:** propietario aprobó opción A y disposiciones RC2 como dirección de diseño PAPER: núcleo financiero local determinístico always-on + jobs Codex Team automáticos por evento/calendario, sin aprobación por job rutinario. D-020 DECIDED únicamente en dirección Build-vs-Reuse; versiones/permisos/runtime final siguen D-024 RESEARCHING. No implementación, gasto, capacidad sostenida ni autoridad financiera adicional. Plus permanece PRE-LIVE.


**Hito histórico previo a aprobación ADR-011 — wave07:** [RC2 Team](research/R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

**Antecedente — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Fecha: 2026-10-01. Cada Q apunta a una decisión del [registro](decision_register.md). La prioridad expresa el gate más temprano que bloquea. El criterio de cierre es evidencia verificable, no una preferencia informal.

Estados: cada Q muestra su prioridad; Q-030–Q-037 incluyen estado explícito. Las Q anteriores conservan el estado inicial salvo que el registro de decisiones indique investigación en curso. Actualizar el estado al registrar su resolución.

| ID | Prioridad | Decisión | Pregunta y evidencia para cerrarla |
|---|---|---|---|
| Q-001 | P0 | D-008/010 | ¿Debe MATR_V1 ser Strategy V1 o un benchmark/candidato descartado tras comparación? El propietario confirmó que **no está seleccionada**; faltan reglas de candidato, evidencia y decisión humana final. |
| Q-002 | P0 | D-011 | El propietario confirma que **nunca se ejecutaron ni vieron backtests de MATR_V1**. ¿Qué política OOS preserva independencia al comparar varios candidatos y cómo se preregistra antes de consultar resultados? |
| Q-003 | P0 | D-011 | ¿Qué costes, spreads, slippage, parciales, dividendos e impuestos de transacción se modelan por escenario? Datos y test de sensibilidad. |
| Q-004 | P0 | D-012 | `DECIDED` en ADR-006: propietario aprobó opción B conceptual; controles independientes y límite más restrictivo. Fórmulas, escenarios y umbrales concretos continúan D-031/D-021/026/030; no existe aprobación para G3. |
| Q-005 | P0 | D-013 | `DECIDED` en contrato abstracto ADR-003: persistir antes de enviar, `UNKNOWN` sin reenvío, ledger de eventos y reconciliación de órdenes/fills/posición; mapeo y probes por broker D-021/030. |
| Q-006 | P0 | D-014 | `DECIDED` en ADR-004: clocks separados, evidencia por canal, `eligible_from`, revisiones as-of y snapshot inmutable; retrasos/muestras concretos D-018/022/033. |
| Q-007 | P0 | D-015 | `DECIDED`: el propietario aprobó A+ (ADR-001); Portfolio Manager Agent produce propuestas shadow auditables sin alterar intents operativos. |
| Q-008 | P0 | D-016 | `DECIDED`: un Champion operativo inicial puede combinar fuentes/señales; shadow y pedagogía factual desde B4; contrato completo pedagógico antes de DoD. Traceability detallada sigue en P1. |
| Q-009 | P0 | D-017 | `DECIDED`: propietario aprobó G1+G2, conservación de protección y reanudación humana tras pausa material en ADR-002; G3/liquidación automática no autorizados. Umbrales/clasificación detallada continúan D-031. |
| Q-010 | P0 | D-020 | ¿Qué capacidades nativas Team y activos Anthropic portables cubren PAPER con calidad, aislamiento y coste suficiente? Evidencia existente válida en su ruta; gaps focalizados TP y selección pendientes. Plus PRE-LIVE separado. |
| Q-011 | P1 | D-021 | ¿Qué broker PAPER admite el perfil real del dueño desde RD, los ETFs/órdenes necesarios, datos/stream y pruebas de recuperación? Verificación oficial y probes. |
| Q-012 | P1 | D-022 | ¿Qué proveedor cubre historia 2005–2026, ajustes, delistings/cambios, timestamps, uso automatizado y costes? Muestra comparada. |
| Q-013 | P1 | D-023 | ¿LEAN, NautilusTrader, vectorbt u otra solución reproduce las semánticas de los candidatos viables y sus fallos con coste razonable? Benchmark. |
| Q-014 | P1 | D-024 | OPEN / GATED_BY_R006: ¿núcleo determinístico local + jobs Codex Team intermitentes con roles/Skills y transporte oficial cubre obligaciones PAPER? Bootstrap, permisos, recovery y comparativa; decisión material owner. No gate Plus para PAPER. |
| Q-015 | P1 | D-025 | ¿Temporal, otra solución o scheduler simple cumple recovery, replays e idempotencia a la escala V1? Prueba de fallos y coste operativo. |
| Q-016 | P1 | D-026 | ¿Qué repositorios de datos y eventos preservan decisiones, versiones, P&L y audit trail reconstruible? Esquemas y restore. |
| Q-017 | P1 | D-027 | ¿Qué aislamiento evita que prompt injection, plugin, dependencia o credencial paper alcancen ejecución/secretos live? Threat model. |
| Q-018 | P1 | D-028 | ¿Qué SLO/alertas/runbooks y backups exige PAPER V1 y cómo se ensayan? SLO medibles y tabletop. |
| Q-019 | P1 | D-029 | ¿Cómo se prueba que el sistema falla cerrado, no duplica órdenes y no promueve Challengers? Matriz de invariantes, integración y evals. |
| Q-020 | P2 | D-030 | ¿Qué tipo de orden de próxima sesión y protección broker-side muestran paridad suficiente entre replay y paper? Probes. |
| Q-021 | P2 | D-031 | ¿Son coherentes los valores PAPER 0.50/2/25% y las acciones soft/hard con gap risk y capital disponible? Calibración, stress y aprobación. |
| Q-022 | P2 | D-032 | ¿Qué periodo, cobertura de regímenes e incident budget se exige antes de paper autónomo? Gate medible. |
| Q-023 | P3 | D-040 | ¿Qué broker LIVE es elegible para el dueño en RD, y bajo qué entidad, jurisdicción y derechos de mercado? Confirmación documental. |
| Q-024 | P3 | D-041 | ¿Qué capital, impuestos, documentación y obligaciones aplican al perfil real? Validación profesional y decisión humana. |
| Q-025 | P3 | D-042 | ¿Qué evidencia separa paper/shadow/live mínimo y qué recuperación se exige para dinero real? Plan y aprobación. |
| Q-026 | P4 | D-050 | ¿Tienen Congreso/Form 4/noticias señal incremental tras latencia y costes? Estudios PIT separados. |
| Q-027 | P4 | D-051 | ¿Vale abrir derivados, shorts u otros activos? Investigación futura y nuevo gate humano. |

## Preguntas de integridad documental

- Q-028 (P1, D-016, `DECIDED`): se corrigió `AGENTS.md` para señalar el roadmap existente indicado por el usuario.
- Q-029 (P1, D-016, `DECIDED`): se adoptó `planning/` como ubicación canónica de acuerdo con §3.5 de la hoja. Los nombres sin prefijo siguen §3.5 y conservan todo el contenido requerido por §3.23.

## Strategy V1 Selection

- Q-030 (P0, D-009, `DECIDED`, cierre técnico 2026-10-07): extracción funcional y tratamiento conservar/modificar/separar/descartar completos en dossier/mapa/rule cards, con revisión independiente documental. No estrategia seleccionada ni claims verificados; seguimiento de fuente solo por necesidad decisoria nuestra.
- Q-031 (P0, D-008, `OPEN`): ¿Qué criterios y pesos compararán Video-Inspired Strategy V1, MATR_V1 y otros candidatos sin seleccionar por rendimiento observado? Debe cerrarse antes de evaluar resultados y luego someter selección al propietario.
- Q-032 (P0, D-008/011 y detalle D-035, `RESEARCHING`): ¿qué reglas propias completas de entrada, stop, reentrada y sizing hacen admisible VID-TS? El video no las define coherentemente; rule cards registran ambigüedades y conflictos. Diseñar variantes ex ante y contrastar datos/órdenes/riesgo, sin atribuir reglas inventadas al creador ni mantener D-009 abierto por esto.
- Q-033 (P0, D-008/022/033, `OPEN`): ¿Puede VID-CONG o VID-ALERT obtener historia con disponibilidad PIT y derechos suficientes bajo ADR-004/005? Evaluación R-021; los dashboards del video no bastan.
- Q-034 (P0, D-018, `DECIDED`): ADR-005 fija roles graduados y gates de admisión para todas las familias Smart Money; ninguna familia queda seleccionada. Evidencia PIT y proveedor por dataset siguen D-022/033 y Strategy V1 D-008.
- Q-035 (P0, D-019, `DECIDED`): el propietario aprobó explicación factual desde B4 y reporte completo antes de DoD, derivados de traza real y sin autoridad de trading. Formato/evals detallados P1 después.
- Q-036 (P1, D-033, `RESEARCHING`): ¿Qué combinación de Quiver, Unusual Whales, Capitol Trades, SEC/EDGAR y otros proveedores entrega cada dataset con historia PIT, API, latencia, licencia, calidad y coste adecuados? Scorecard R-025.

- Q-040 (P3, D-040/042, `DEFERRED`): ¿Qué servicios pagos justifican su coste fijo/variable/mensual y por escala en LIVE frente a alternativas gratuitas, por calidad, continuidad, seguridad o beneficio neto esperado? Política D-036/ADR-008 `DECIDED`; presupuesto y selecciones concretas abiertos. No bloquea investigación PAPER, salvo que una insuficiencia material afecte el diseño V1.
- Q-037 (P1, D-021, `OPEN`): ¿Qué broker es elegible para RD y sirve a equities PAPER con API, streams y órdenes protectoras, manteniendo opciones futuras sin imponer derivados en V1? Comparación R-007; Alpaca no está seleccionado.
- Q-038 (P1, D-034, `OPEN`): ¿Qué esquema, aislamiento técnico, protocolo de evaluación PIT y métricas preregistradas permiten comparar Champion con `ShadowPortfolioProposal` sin que el shadow influya en operaciones ni obtenga datos futuros?
- Q-039 (P1, D-035, `OPEN`): ¿Cuáles son las fórmulas, unidades, redondeos, precedencia y casos de concurrencia verificables que concretan ADR-006 sin fijar aún los umbrales PAPER de D-031?

- Q-041 (P0, D-020, DECIDED en dirección): propietario aprueba ADR-011 A/disposiciones RC2. Versiones/permisos y freeze siguen D-024; operación sostenida sigue pendiente. No selección definitiva ni implementación.
- Q-042 (P1, D-024/025, RESEARCHING): ¿qué cadencia, recovery/degradación y contratos exige núcleo local + Codex Team intermitente? TP por etapa y demanda Strategy V1; operación sostenida P2, sin gate Plus.

- Q-043 (P1, D-034/029, `RESEARCHING`): ¿Cómo discriminar desde rol confiable ResearchHypothesis/ShadowPortfolioProposal/explicación y OBSERVED/DERIVED? Respuesta técnica RC0 en 06_agent_evidence_contract: caller externo/schema, enums, target qty, typed refs/lineage, tres ejes de estado y hashes pareados. Wave 06 prueba spine con fallos de checker conservados. Full schemas/aislamiento/integration siguen P1, no repetir muestra para ocultar errores.

- Q-044 (P1, D-037/020/024, RESEARCHING): ¿qué ruta reproducible bootstrap Team carga reglas/roles/Skills, restaura desde repo y prueba readiness sin chat? Fresh clone parcial probado; final permisos/runtime pendientes; Team→Plus solo PRE-LIVE.

**Q-044 avance R-028:** discovery nativo y herencia corroborados en fixture Team; contratos/perfiles/paquetes RC0 creados. Siguiente probe fresh clone; ruta target/gates y permisos siguen abiertos, no selección de sesiones.

**Q-044 estado posterior:** contrato y fresh-clone route documentados/probados en CLI Team (metadata 6, smoke 2). Quedan superficie/entitlement/operación target, full EB y permisos/runtime finales; evidencia parcial no cierra D-037.

- Q-045 (P3, D-039, DEFERRED): ¿qué deltas y suficiencia operacional requiere migrar el sistema validado Team a Plus candidato antes de LIVE? Activar R-029 cuando proceda, sin esperar ahora.

## P1 posterior ADR-011 — hardening

- Q-046 (P1, D-027, DECIDED solo dirección): propietario aprueba ADR-012 S2; S3 fallback formal, S1 solo research. La configuración efectiva, los gates separados de seguridad/blinding y el setup administrativo siguen pendientes; no permisos concedidos.
- Q-047 (P1, D-025/026, RESEARCHING): ¿qué motor/store, fencing/epoch y restore cumplen recepción at-most-once y conservación audit/PIT? Contratos 08 y probes toy reducen ambigüedad, motor final sigue pendiente.
- Q-042 avance: scheduler automático aprobado en ADR-011; cola/prioridad/concurrencia/plazos/cupo permanecen candidatos. Background largo puede bloquear shadow; workloads reales y retries con deadline original son gate, no 63 éxitos simulados.

- Q-048 (P1, D-010/033, RESEARCHING): ¿qué evidencia histórica acredita public availability/delivery de SEC por canal cuando la fuente no da timestamp first-available? DatasetCard R-020 distingue acceptance/filing/change/receipt y propone comparación de fuentes/canal conservador; no adoptar delay supuesto como PIT exacto.

- Q-049 (P1, D-027/D-024/D-037, DEFERRED): S2-ADM-01 **NOT_AUTHORIZED / OWNER_WITHHELD** el 2026-10-06. No crear las tres cuentas ni ACL; revisar variante antes de nueva propuesta administrativa. [Antecedente](research/R-013_S2_administrative_gate_ADM01.md).
- Q-050 (P1, D-027, RESEARCHING): ¿qué policy store/administrador y controles verificables aplican egress completo del SDK/children en este host con AllowLocalFirewallRules=False? Preflight y rule-source counts no establecen origen del setting. No cambiar merge/global defaults; gate red posterior concreto.

## Revisión vigente de variantes — 2026-10-06

- Q-051 (P1, D-027/D-024, DECIDED solo dirección): propietario confirma S2-B como candidata principal el 2026-10-06. Runner único/contextos efectivos; A si insuficiencia demostrada, S3 reserva. Sin aceptación ni permiso administrativo. [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md).
- Q-046 conserva aprobación histórica de frontera S2; no prescribe una cuenta por rol tras revisión. Q-050 sobre policy store/egress permanece RESEARCHING: mismo usuario o VM no sustituyen comprobación de red del harness completo.

## Próximo gobierno concreto — 2026-10-06

- Q-052 (P1, D-027/D-024/D-037, DECIDED en autorización de laboratorio): propietario autoriza **S2B-ADM-01**, una cuenta local estándar temporal `tos_probe_runner_b`, árbol canary nuevo/ACL exactas, pruebas FS acotadas y reversión por ledger SID/path. El administrador único será el propietario; los secretos se introducen mediante UI Windows, nunca chat/args/logs/Git. [Propuesta completa](research/R-013_S2B_lab_ADM01.md). AUTHORIZED_OWNER_ADMIN_ONLY, setup/login todavía pendientes; no Team login/red/ACL anteriores. No aceptación financiera/security/runtime ni cierre D-027/D-024.
- Q-051 cerrado solo dirección. Q-050 egress/policy store abierto; viejo Q-049 DEFERRED. No Plus ni nueva selección de S2-B solicitada.

## Entornos y gates vigentes — ADR-013

D-043 DECIDED; no pregunta de acceso Plus/admin institucional pendiente. Q-052 conserva la autorización histórica temporal, ejecución DEFERRED_TO_TARGET_PAPER_HOST. Preguntas de diseño ahora: workflow/store y fronteras nativas/versiones; después Strategy V1 (D-008 OPEN), brokers/data/engine/riesgo. D-024/027/037 target acceptance diferido R-030, no resultados FAIL ni runtime aceptado. LIVE UNKNOWN.

## Checkpoint de diseño material — 2026-10-07

- Q-053 (P1, D-024/D-027/D-037, DECIDED 2026-10-13 owner): ADR-014/B-RT1 aprobado como realización candidata en scope documentado; AGENTIC_ARCHITECTURE_DESIGN_COMPLETE, target aceptación diferida. Mecanismos específicos sustituibles, no permisos operacionales ni nueva acción owner requerida por este checkpoint.
- Q-042/Q-044/Q-045/Q-050 y sus notas anteriores conservan contexto histórico. Vigencia actual: Plus/personal es target PAPER; LIVE UNKNOWN; egress del host institucional no es gate PAPER. D-025/026/028/029 y Strategy workload siguen diseñables aquí; gates target no bloquean su investigación.
- Auth shared-home/keyring namespace, token/desktop/launch capability, C/J typed channels y instance/fingerprint están especificados en B-RT1/R-028; **compatibilidad/eficacia** target NOT_TESTED, no preguntas de acceso ahora.

## Próximo gobierno financiero — 2026-10-13

- Q-054 (P1, D-035, DECIDED 2026-10-13 owner): ADR-015 aprueba R2 principal, R1/controles independientes conservados y condiciones de señal/top-up/p_auth/incertidumbre/no doble conteo; sin fórmulas finales/params/pruebas ni selección de estrategia/broker.
- Strategy D-008 OPEN: config/universo/entry/exits/lote/as-of/sizing/protección/params y admisión de data deben completarse antes de freeze; no entrada inventada por LLM. No nuevas preguntas de arquitectura fundamental agéntica; target R-030 diferido.

## Aprobación vigente R2 — ADR-015, 2026-10-13

Owner aprueba R2 conceptual y acotado; R1/P&L/controles independientes conservados. Menor R2 no autoriza ampliar perdedoras: señal/regla Champion, nueva evaluación integral y reservas reconciliadas obligatorias. p_auth pending/new y protección condicional conservados. Missing/invalid/unconfirmed/crossed stop sin fill verificado => UNCERTAIN, nunca riesgo0. Costes/pérdidas/claims sin doble conteo ni exposición oculta; casos ganancias/pérdidas/partial/top-up/gap/rapid-move R-027 RC1. Q-054 DECIDED, **D-035 global RESEARCHING**, fórmulas/params/pruebas siguen abiertas. Sin selección Strategy/broker, implementación, gasto o target acceptance. [ADR-015](decisions/ADR-015-remaining-risk-reference-R2.md).

## Próxima decisión material — Q-055

- Q-055 (P0, D-008/D-011, DECIDED owner2026-10-14, ADR-016; formulación original conservada): ¿aprobar **O-B** como arquitectura conceptual de evaluación: desarrollo por candidato, selección comparable2019–2022 sólo con historia/PIT/rights admisibles y confirmación propuesta2023–2026-09-30 reservada para un candidato/config/selector congelado? Mantiene ventanas MATR; historia insuficiente => research/prospectivo, no scorecard confirmatorio ni rank por CAGR de ventanas distintas. Alternativas O-A uniformidad2005+ y O-C pasado exploratorio+forward futuro. [Problema/evidencia/trade-offs/recomendación](research/D-011_OOS_policy_decision_RC0.md). Reserva INTEGRITY_UNKNOWN hasta exposure ledger; si no se acredita integridad, reevaluación owner antes de abrir resultados. No números, Strategy/broker/data selection, implementación, acceso Plus/admin ni gasto aprobados. Métricas/sample/costs/protocolo final siguen D011 abiertos.

## Aprobación vigente O-B — 2026-10-14

[ADR-016](decisions/ADR-016-strategy-evaluation-O-B.md) registra Q055 DECIDED conceptual; D011 global RESEARCHING, Strategy OPEN. Reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11; alternativa prospectiva con gobierno si contaminada. Ensayos incluidos descartes, suficiencia/INSUFFICIENT_EVIDENCE, comparabilidad, walk-forward/sensibilidad/costes/retrasos y horizonte/latencia/caducidad quedan exigidos antes de resultados. Ningún modelo/umbral/estrategia/broker/data aprobado; lock y target deferral vigentes. Continúa paquete financiero sin solicitar Plus/admin ni investigación agéntica general.

## Q-056 — preferencia económica necesaria para preregistro

- Q-056 (P0, D008/D011, DECIDED owner/ADR-017; formulación original conservada): ¿qué mejora primaria buscamos frente al benchmark común: **A retorno incremental**, **B conservar retorno dentro de margen previo y reducir riesgo** (recomendación), o **C sólo demostrar operación sin claim económico**? B puede aceptar menor retorno dentro de margen; esa preferencia no pertenece al Architect. [Problema/evidencia/alternativas/trade-offs](research/D-011_economic_endpoint_decision_RC0.md). Sólo dirección conceptual, no margen/medida/p-value/power/Strategy/broker/params aún. Sin ello EvidenceRequirementCard/efecto/muestra no se pueden cerrar honestamente. O-B aprobado; no se repite Q055. Target/Plus/admin no son solicitud actual.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Q-057 — referencia económica concreta de PRICE–MATR

P0 / D008-D011 · DECIDED K2 por owner/ADR018; propuesta original conservada en [dossier K1/K2/K3](research/D-011_benchmark_qualification_decision_RC0.md). Recomendar K2: seis ETF a igual peso inicial buy-and-hold como primario, oportunidad cash y espejo EW6-BH-LAMBDA-REAL obligatorio, gates económicos AND. K1 SPY primario/espejo SPY; K3 ambos primarios y ambos espejos/gates. El alcance es sólo esta cohorte, no Form4; elegir referencia cambia la pérdida de oportunidad que medirán los futuros márgenes. No números/modelo/Strategy/broker/data ni implementación aprobados. Q056 DECIDED, no nueva elección abstracta de objetivo; selección de benchmark sí requiere gobierno económico conforme ADR017.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Q-058 — utilidad numérica de calificación

P0/D008-D011 · DECIDED M1 por owner/ADR019, [propuesta original M0/M1/M2](research/D-011_economic_margins_proposal_RC0.md). Recomendar M1: margenNI1pp CAGR/año, exceso mínimo cash1pp neto/año, reducciónES20% con cola95, sujeto a evidencia/precision y comparador defendibles. Números no aprobados, Q056/Q057 no se reabren. Trade-off de oportunidad, gastos/escala y muestra ficticia documentados, sin estimar parámetros del mercado. Aprobación eventual sólo presupuestos económicos/definición de cola, no calib/modelo/dataset/Strategy/capital/DoR.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.

## Q-059 — guardrails complementarios nuevos

P0/D011, DECIDED G-R1 por ADR-020 el 2026-10-15; alternativas históricas siguen abajo. [G-R1/G-R2](research/D-011_complementary_guardrails_proposal_RC0.md) definen cuánto deterioro DD/σ admitir además de ES20. Recomendar G-R1: no deterioro de DD frenteEW6-BH ni σ frenteespejo, con incertidumbre/método admisibles; recovery/pérdidas/stress reportados con censura/limitaciones y modelo válido. G-R2 tolera+1ppMDD/+5%σ, propuesta no autorizada. B/K2/M1 no se preguntan de nuevo; tampoco Risklimits/estrategia/capital/métodos oF0 por esta decisión.

## Vigencia G-R1 — ADR-020, 2026-10-15

[ADR-020](decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md): Q-059/G-R1 DECIDED en preferencia económica ex ante: no deterioro de DD frente a EW6-BH completo ni de volatilidad diaria frente al espejo K2 admisible. ES95/M1 primario y NI/cash/K2 conjuntos; recuperación/underwater/pérdidas/gaps/slippage/extremos obligatorios. DD exige estimando/horizonte/path/incertidumbre y aplicabilidad válidos; una trayectoria/bootstrap genérico no demuestra futuro. Volatilidad incluye upside/downside. Guardrails relativas no son límites absolutos Risk D-031. G-R2 no aprobado ni fallback. Estados separados y NO_STRATEGY_QUALIFIED; ningún método/dato/broker/Strategy/F0/implementación aceptado. Continuar P0/P1 financieros en checkpoints agrupados; holdout UNKNOWN/lock/targetdeferral.
