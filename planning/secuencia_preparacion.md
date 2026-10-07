# Secuencia de Preparation Program — vigencia ADR-013

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Endpoint histórico 2026-10-06, tras autorización y preparación del handoff:** Q-052 / [S2B-ADM-01](research/R-013_S2B_lab_ADM01.md) DECIDED en permiso temporal / AUTHORIZED_OWNER_ADMIN_ONLY / SETUP_PENDING. [Guía de ejecución](research/R-013_S2B_owner_execution_runbook.md), una cuenta estándar temporal, nuevo árbol canary/ACL, pruebas FS acotadas y rollback. Preparación no privilegiada completada; siguiente paso requiere crear la cuenta mediante Windows por el propietario, no reaprobar el gate. FS NOT_TESTED. Q-051 dirección S2-B cerrada; viejo S2-ADM-01 tres cuentas withheld/DEFERRED. D-027/D-024 abiertos, Plus PRE-LIVE e implementación bloqueada. Secuencias administrativas anteriores son antecedentes, no autorizaciones activas.

2026-10-05. Team actual para preparación, futura implementación tras DoR, backtests y PAPER. Plus individual es candidato PRE-LIVE R-029 P3; no espera de acceso Plus. Implementation lock vigente.

1. **D-038 DECIDED:** registrar supersession ADR-010, perfiles/contratos/gates y source policy; commit/push.
2. **Paquete focal Team completado:** wave07 8/8, SDK bootstrap 14/14 y 16 checks consolidación; RC2/perfil PARTIAL. D-020 DECIDED en disposiciones ADR-011; D-024 RESEARCHING y no freeze.
3. **ADR-011 A DECIDED:** dirección core local + jobs Team automáticos por eventos/calendario y disposiciones RC2 aprobadas. No nueva aprobación por job rutinario, ni freeze/implementación.
4. **Paquete autónomo R-010–014 especificado/probado en alcance de preparación:** contratos de aislamiento/permisos, workflow/recovery, storage/audit, versiones/deploy y criterios/capacidad P1; revisión independiente. Comparar alternativas antes de pedir gobierno de arquitectura material D-027/D-024. Revisión crítica independiente requerida antes de freeze; no fingir reviewer independiente.
5. Después, siguiente P0 R-020/D-008 (preregistro/candidatos/Strategy V1), D-011, y R-007/008/009/025 datos/broker/quant/Smart Money; contratos D-021–029/033–035 y seguridad. No seleccionar broker/estrategia/umbrales ni gastar sin gobierno correspondiente.
6. Completar DoR: P0/P1 cerrados, contratos/protocolos/stack aprobados, bootstrap Team reproducible y review/freeze. Solo entonces implementar.
7. Validación P2: integración financiera/aislamiento/workflow, backtests y operación PAPER con workload definitivo, cuotas/ventanas reales, pedagogía y shadow; límites numéricos/promotion gates aprobados.
8. P3 tras PAPER validado: R-029 Team→Plus candidato, release/tag aprobado, diff/acceptance/migración y rollback; gates LIVE financieros/económicos aparte.

Source: plan-architect candidato; main baseline aprobado; deployment desde release/tag versionado aprobado. No merge/main/tag de deployment ahora.

## Secuencia histórica conservada — superseded en entorno/next-step por ADR-010

# Secuencia para cerrar el Preparation Program

1. **A0–A1, ahora:** baseline, Plan Architect, diagnóstico, registros, dependencias y DoR desglosado. Confirmar identidad del dueño/aprobador. Salida de esta ejecución: `planning/` inicializado; aún no se declara `PLAN_UNDERSTOOD=TRUE` formal porque quedan ambigüedades P0.
2. **Mapa del Trading OS P0:** R-022 cierra funciones, ownership, fronteras y fases: investigar → datos → estrategias/backtest → señales → TradeIntent → riesgo → ejecución/reconciliación → monitoreo/desempeño → Champion/Challenger → pedagogía. R-019 suministra inspiración funcional del video y clasifica conservar/modificar/separar/descartar; sin auditoría de claims promocionales.
3. **Contratos financieros y de datos P0:** R-002/003/004/005 fijan riesgo, autoridad, órdenes, PIT y PAPER V1. R-023/021 definen taxonomía y disponibilidad temporal de señales externas; R-024 especifica Pedagogical Agent con trazas verificables y sin autoridad financiera. Revisar consistencia conjunta D-012–019.
4. **Build vs. Reuse P0, foco inmediato:** R-006/D-020 examina IA/agentes **solo OpenAI y Anthropic** bajo ADR-007: Skills/Plugins/Codex/MCP verificables en **Plus individual objetivo** y activos públicos Anthropic, Tier 0/1 primero. ADR-008 permite estudiar pagos futuros/excepcionales, sin contratar ni gastar antes de aprobación. PAPER zero/low incremental y LIVE valor/economía unitaria son criterios distintos; metodologías gratuitas. El Agent Capability Gate impide cerrar D-024 hasta madurez y gate Plus. R-025 compara Smart Money por dataset; R-007 brokers y R-009 quant conservan investigación.
5. **Strategy V1 P0 sobre contratos comunes:** R-020 fija criterios antes de consultar resultados y compara variantes video primero, MATR_V1 y nuevos candidatos; R-001 caracteriza MATR. La selección/arquitectura final exige aprobación humana. No se fuerza una única estrategia a partir de piezas heterogéneas.
6. **Stack y operación P1:** R-008–R-014 validan market data, backtest, runtime, workflow, storage, seguridad, observabilidad, evals y pedagogía contra los contratos P0; scorecards/probes y ADRs. Decisiones de broker y datos materialmente costosos van al dueño.
7. **P2 con procedimiento:** definir en el Plan v1.0 cómo se calibrarán tipo de orden, stops y límites con paper/probes R-015; todo P2 debe estar resuelto o tener gate, responsable y evidencia explícitos antes del DoR. No se permite paper autónomo hasta cumplimiento.
8. **P3/P4 y freeze:** LIVE y búsqueda incremental de alpha quedan en R-016–018, con gates separados. Critic/Red Team de P0/P1, consistency y traceability checks, `MASTER_PLAN_RC1.md`, revisión del dueño, `MASTER_PLAN_v1.0.md` congelado y solo entonces `implementation_locked=false`.

**Regla de orden:** cerrar primero fronteras y contratos; investigar candidatos de proveedor en paralelo sin seleccionarlos antes del scorecard. Ningún resultado de plataforma modifica un invariante sin change record y aprobación correspondiente.

## Cola inmediata de decisiones P0/P1

| Orden | Decisión | Evidencia de cierre | Intervención humana |
|---|---|---|---|
| 1 — P0 | D-015/016/019 DECIDED con A+; D-018 DECIDED como roles/gates abstractos | ADR-001/005 y contratos RC1; PIT por dataset sigue R-021/025 | Dueño aprobó alcance A+; ninguna fuente específica aprobada |
| 2 — P0 | D-012/013/014/017: riesgo, TradeIntent/órdenes, datos PIT y autonomía ante fallos | R-002/003/004/021: estados, secuencias de fallo, timestamps, controles y pruebas especificadas | Aprobación del dueño para política de riesgo y límites de autonomía |
| 3 — P0 inmediato + P1 dependiente | D-020/R-006 Capability Discovery; D-024 queda abierto hasta gate. D-033/021 proveedores/broker continúan en paralelo | Inventario y scorecards con disponibilidad, permisos, licencias, coste y probes; después paquete D-024. R-025/007 validan datos y broker | Arquitectura agéntica material, broker y gasto material requieren gobierno humano; ningún candidato preseleccionado |
| 4 — P0 | D-008/010/011: Strategy V1 y validación | R-019/020/001: variantes video separadas, MATR y otros candidatos, reglas falsables, protocolo OOS antes de resultados | Selección/arquitectura final aprobada por dueño |
| 5 — P1 | D-022–029: datos de mercado, backtest, runtime, workflow, storage, seguridad, pruebas y operación | R-008–014: benchmarks/probes, coste, threat model y criterios verificables | Seguridad material y datos costosos al dueño; resto por ADR técnico |

**Hito A+ alcanzado 2026-10-01:** el propietario aprobó [ADR-001](decisions/ADR-001-paper-v1-authority.md) y [contrato PAPER V1 RC1](paper_v1_capability_contract_RC1.md), cerrando D-015/016/019. El bloque posterior cerró D-017/013/014/018 mediante ADR-002–005 en su alcance abstracto; sus pruebas dependientes de broker/dataset permanecen P1/P2. R-026 detalla y evalúa el canal shadow como P1. R-025 y R-007 siguen abiertos sin selección ni gasto prematuro.

**Avance P0 posterior:** [riesgo RC1](03_risk_policy_RC1.md), [orden RC1](04_order_contract_RC1.md) y [datos RC1](05_data_contract_RC1.md) documentan el bloque. El propietario aprobó G1+G2 y reanudación humana tras pausa material en [ADR-002](decisions/ADR-002-paper-v1-incident-autonomy.md); D-017 está `DECIDED` y G3 no autorizado. ADR-003 cierra contrato abstracto D-013 sin elegir broker; ADR-004 cierra semántica PIT D-014 sin admitir datasets; [ADR-005](decisions/ADR-005-external-signal-admission.md) cierra roles/admisión D-018 sin seleccionar fuente. El propietario aprobó la opción B de riesgo conceptual D-012 en [ADR-006](decisions/ADR-006-composite-risk-architecture.md); escenarios, umbrales y pruebas siguen abiertos. El siguiente trabajo prioritario es R-006/D-020/D-024 Capability Discovery antes de congelar diseño agéntico; R-020/D-008 continúa después de esta investigación inicial y antes de consultar resultados.

**Secuencia R-006 actualizada 2026-10-05:** conducta comparativa Team → shortlist condicional → Plus Acceptance Gate de finalistas → paquetes D-020/D-024 y gobierno. La ausencia de cuenta Plus no bloquea discovery. Preservar alternativa de núcleo determinístico/local always-on con Codex intermitente; no congelar topología.

**Estado vigente R-006 2026-10-05:** [shortlist RC1](research/R-006_shortlist_RC1.md) tras completar pasos autónomos 1–2 de RC0: contratos por rol/shadow/pedagogía, workload y matriz; wave 06 y transporte Codex SDK nativo probados. No parar tras resumen dentro de un paquete abierto: aplicar Autonomous Continuation Rule, persistir/commit/push y avanzar. Endpoint de este paquete R-006 alcanzado; siguiente acción es dirección candidata material y acceso Plus, sin final selección/freeze de D-020/024. Gate target limitado a finalistas; no repetir discovery completo.

**Después de intervención:** confirmar dirección candidata y sesión Plus, escoger wrapper oficial adecuado al contrato/tools, ejecutar GP1–7 y demanda representativa; review independiente/seguridad y paquete final D-020/D-024. Strategy V1 demanda puede rebaselinar workload antes de freeze. R-020/D-008 continúa como siguiente P0 de preparación (preregistro/candidatos, sin backtests no aprobados), con R-025/R-007/R-008/009 y contratos de integración en su orden. Contratos financieros y futuras investigaciones independientes no quedan cancelados por acceso Plus pendiente; cada paquete tendrá endpoint explícito. Trading OS sigue sin implementar.

## Secuencia vigente — requisito de portabilidad 2026-10-05

1. Cohorte RC1 aprobada para aceptación; no volver a pedir esta aprobación ni cerrar D-020/D-024.
2. **Ahora R-028/D-037 P1**, dependiente del gate arquitectónico: fuente oficial, contrato de onboarding/perfiles/paquetes, probes Team/fresh clone y diferencias/readiness offline. Requisito ADR-009 aprobado.
3. Persistir/sincronizar evidencias y deltas de R-006/GP; continuar todo trabajo de este paquete que no dependa de entitlement/gobierno.
4. Plus Acceptance GP1–7 más gate de portabilidad usando entorno objetivo y assets del clone. Acceso requiere acción del dueño; no transferir auth Team. Reutilizar evidencia conductual, repetir solo diferencias relevantes.
5. Review/seguridad y gobierno final D-020/D-024/037; runtime/topología aún abiertos. La ruta bootstrap es condición DoR explícita. R-020/D-008 y demás trabajo independiente siguen válidos; no implementar Trading OS.

**Endpoint R-028 alcanzado:** diseño/paquetes/probes nativos y fresh clone/reporte PARTIAL completados y persistidos; próximo gate requiere cuenta Plus real para GP/EB target. Cohorte ya aprobada; no final runtime. Scope del paquete independiente de entitlement agotado; solicitar acceso conforme Autonomous Continuation Rule. No implica pausa global de Preparation ni cierre de R-020/otras investigaciones.

## Checkpoint material posterior ADR-011

Contratos/probes/review P1 documentados en dossier R-010_014. Endpoint siguiente: ADR-012 dirección material S2 vs S3; no aprobación por job ni Plus. Antes del checkpoint se avanzó preregistro independiente R-020; Strategy V1 sigue OPEN. Tras dirección: config/permisos concretos, probe aislamiento real, motor/store final, carga representativa y revisión del paquete antes de D-024; no freeze por smoke.

**Avance independiente R-020:** cards de reglas video y admisibilidad SEC creadas con fuentes primarias; no resultados históricos consultados. Tras checkpoint seguridad, continuar datos/PIT y variantes admisibles/protocolo OOS; broker/engine/risk numérico mantienen decisiones separadas.

## Checkpoint vigente — aprobación S2 y próximo gate administrativo

ADR-012 S2 dirección candidata aprobada. Ejecutar R-013 autónomo: contratos concretos por dominio, threat model, secretos, negative tests, blinding separado, acceptance/escalamiento y probes sintéticos no administrativos. Persistir/revisar/commit/push. Solo después presentar el cambio administrativo concreto necesario para probar identidades/ACL/IPC/egress efectivos. D-027/D-024 RESEARCHING; no esperar Plus, no repetir elección S2, no Trading OS. Continuar P1 independientes antes de detenerse; Strategy V1 permanece OPEN.

## Endpoint histórico del paquete S2 — ADM-01 (suspendido 2026-10-06)

Threat model/identity-FS-network-IPC-secrets, SI17/BL9/RB5 y escalamiento predefinidos; preflight readonly + 7 observaciones/counterexamples, revisión y persistencia. Ningún S2 PASS. Trabajo P1 independiente de configuración actualizado: launch/recovery, raw/sealed/audit/deploy y bootstrap. Siguiente prueba efectiva requiere cuentas/ACL reservadas a gobierno: Q-049 / [ADM-01](research/R-013_S2_administrative_gate_ADM01.md). Solicitar solo ese laboratorio, no repetir elección S2. ADM-02 red/IPC/audit y ADM-03 login Team requieren sus propuestas concretas posteriores. D-024/D-027 abiertos; Strategy V1/datos/motor mantienen secuencia propia, sin backtests/holdout/aprobación tácita.

## Endpoint vigente tras aprobación S2-B — 2026-10-06

Q-051 cerrado en dirección candidata. Continuar R-013: especificar laboratorio mínimo S2-B, reutilizar controles existentes, comprobar artefactos/contratos sin cambios administrativos y revisión independiente. La configuración real que necesite users/ACL/firewall/credentials debe presentarse con reversión y HUMAN_ACTION_REQUIRED; no repetir elección de dirección. ADM-01 histórico permanece DEFERRED. D-027/D-024 abiertos.

## Endpoint S2-B y evidencia adicional — 2026-10-06

Dirección S2-B aprobada; Q-051 DECIDED en ese alcance. [Laboratorio mínimo S2B-ADM-01](research/R-013_S2B_lab_ADM01.md), Q-052 READY_FOR_DECISION/NOT_AUTHORIZED. [Dossier](research/R-013_S2B_lab_preparation_2026-10-06.md) y fuentes distinguen memoria12+privilegios2, sintaxis14 y preflight readonly de **FS/thread/native NOT_TESTED**. Grant común/tránsito/default DACL se incluyen en VP04/LF09, con positivos adecuados. No setup ni retry bajo BASE para operaciones de job. Full process/IPC/egress/auth/cache/recovery/TP6 y SI17/BL9/RB5/VP8 pendientes; ningún gate efectivo se pasa por estos contadores. R-006 madura diseño, D-020 conserva aprobación, D-027/D-024 siguen RESEARCHING. ADM-01 tres cuentas DEFERRED; PAPER Team y Plus PRE-LIVE.

## Secuencia vigente — ADR-013, 2026-10-07

1. Registrar research Team/INFOTEP y target PAPER Plus/personal; defer lab, mantener historia y lock.
2. R-006/R-010/R-013: completar preguntas arquitectónicas resolubles en Team, contratos/review y checkpoint de diseño acotado; separar R-030 target acceptance P1.
3. R-020/001/019/021: cerrar definición de candidatos Strategy V1 y metodología OOS preregistrada, sin resultados consultados ni selección implícita MATR.
4. R-007/008/025/009: brokers/RD, precios/historia y señales externas, engine y paridad; reunir evidencia para decisiones humanas materiales.
5. R-027/011/012/014: fórmulas riesgo, workflow/storage/operación y protocolos restantes; Plan v1.0 diseño revisado/freeze con gobierno.
6. Transición autorizada a PC personal/Plus: fresh clone/R-030/seguridad; DoR y permiso de implementación solo tras gates requeridos. Sistema integrado/backtests/load/recovery/PAPER después; LIVE se decidirá posteriormente.

No acceso Plus ni administración INFOTEP solicitados. No esperar esas pruebas para investigar diseño o P0/P1 financieros.
