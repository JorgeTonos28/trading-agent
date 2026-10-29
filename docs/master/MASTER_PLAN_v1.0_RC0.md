# Trading OS — MASTER_PLAN v1.0 RC0

**DRAFT_FOR_REVIEW / NOT_FROZEN / NOT_READY_FOR_IMPLEMENTATION.**

Actualización: 2026-10-28. Rama: `plan-architect`. Este documento integra el diseño disponible y sus dependencias. No sustituye silenciosamente la [hoja de ruta v0.2](hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md) ni aprueba las propuestas pendientes. El contrato final será `MASTER_PLAN_v1.0.md` después de revisión, aprobación y freeze.

Se mantienen `implementation_locked=true`, `TARGET_ACCEPTANCE_DEFERRED` y holdout `INTEGRITY_UNKNOWN`.

## 1. Mandato, alcance y autoridad

Trading OS investigará estrategias, producirá señales, controlará riesgo, ejecutará, monitoreará, comparará Champion/Challenger y explicará sus decisiones. PAPER inicial contempla equities/ETF long-only y una única configuración Champion aprobada, que puede combinar varias fuentes. Leverage, shorts, derivados y LIVE requieren gobierno separado. El video inspira candidatos sin selección automática; MATR permanece como candidato/benchmark y Form 4 como investigación externa.

`Señal/estrategia determinística → TradeIntent → Deterministic Risk Engine → Execution → Broker`.

Risk es la única autoridad financiera para aprobar, reducir o rechazar intents. Research, Quant, Shadow y Pedagogical no reciben credenciales del broker ni autoridad para ordenar, cambiar riesgo/Champion/asignaciones o reanudar una pausa material. No habrá aprobación humana por operación dentro de un Champion autorizado.

Ante incertidumbre material se bloquean nuevas entradas y se reconcilia. Sólo se cancelan automáticamente entradas pendientes identificadas y verificadas. Se conservan protecciones salvo regla específica documentada y probada. Los incidentes materiales requieren reanudación humana; G3 y liquidación general no están autorizados. Contratos: [A+](../../planning/decisions/ADR-001-paper-v1-authority.md), [G1+G2](../../planning/decisions/ADR-002-paper-v1-incident-autonomy.md), [órdenes](../../planning/04_order_contract_RC1.md) y [riesgo](../../planning/03_risk_policy_RC1.md).

## 2. Entornos y gates

| Fase | IA y host | Estado |
|---|---|---|
| Preparación | ChatGPT Team; workstation Windows institucional INFOTEP | Investigación/diseño y probes desechables. No es host PAPER ni se solicita administración |
| Implementación/PAPER | Plus individual; PC personal Windows administrada por el propietario | Aceptación R-030 pendiente antes de implementar; validación integrada/sostenida posterior P2 |
| LIVE | IA, host, broker y capital sin seleccionar | Decisión posterior a PAPER; no se presume continuidad del stack |

La evidencia Team no acredita entitlement Plus, seguridad o capacidad sostenida target. S2B-ADM-01 está diferido al target, no es FAIL ni acción pendiente en INFOTEP. Los ocho archivos sintéticos H7 permanecen como residuo documentado. Referencias: [ADR-013](../../planning/decisions/ADR-013-research-and-target-paper-environments.md), [R-030](../../planning/research/R-030_target_paper_environment_acceptance_RC0.md).

## 3. Arquitectura agéntica aprobada en diseño

Núcleo financiero local determinístico activo y supervisor/control confiable fuera del dominio AI. Un scheduler invoca automáticamente jobs Codex por eventos/calendario. El LLM no permanece necesariamente residente ni los jobs rutinarios requieren inicio manual.

Un Agent Runner utiliza aislamiento efectivo por job, contexto mínimo, allowlists, identidad por attempt, lifecycle, outputs estructurados y validación/admisión externa. Se registran snapshots, versiones e intentos. Timeout, cuota agotada, error, respuesta tardía o ausencia de output no conceden autoridad alternativa; ausencia no significa HOLD. Retry/recovery no deben duplicar efectos financieros.

Security isolation y experimental blinding son objetivos distintos. Keyring, token, HOME, IPC, desktop y launch son mecanismos candidatos reemplazables bajo gobierno. Prompts/AGENTS/authority=NONE no son barreras de seguridad. Diseño fundamental completo; no reabrir R-006/R-010/R-013 por refinamiento indefinido. [ADR-014](../../planning/decisions/ADR-014-agentic-design-checkpoint-proposed.md), [realización](../../planning/08_agentic_runtime_realization_RC1.md), [onboarding](../../ONBOARDING.md), [paquetes](../../planning/07_agent_packaging_contract_RC0.md).

## 4. Stack financiero propuesto

| Capa | Propuesta o alternativas | Dependencia de cierre |
|---|---|---|
| Broker PAPER | ADR-023 selecciona **Alpaca Paper Only** en diseño; IBKR TWS reserva | B1–B5, incluidos protección, feeds y target |
| Backtesting | ADR-023 selecciona **LEAN source** local en diseño; Nautilus reserva/comparador acotado | Pin/dependencias, distribución, modelos y paridad |
| Históricos/actions/cash/quotes | D-022 abierto por producto y rol | Derechos, retención, cobertura, PIT, calidad, pay-date y feed operacional |
| Workflow/scheduler | ADR-024 aprueba APScheduler3.x acotado; Temporal reserva | Dirección condicionada DECIDED; ledger/ownership, envelope y suficiencia D1 P1 |
| Ledger/storage/audit | ADR-024 aprueba dirección PostgreSQL C/F separados; Parquet/DuckDB analíticos; Redis reserva | Pin/config/atomicidad/roles/restore/retención P1; SQLite sólo instrumento de laboratorio |
| Observabilidad/evals | Contratos existentes; productos abiertos | D-028/D-029: SLO, RPO/RTO, suites y recuperación |

Nada se selecciona por aparecer en tabla. No construir un simulador general si una capacidad reutilizable satisface el contrato. No contratar CLI/Cloud/APIs pagas sin aprobación. Evidencia: [Q-062](../../planning/research/D-021_023_PAPER_stack_decision_RC0.md), [broker RC4](../../planning/research/R-007_PAPER_broker_selection_packet_RC4.md), [motor RC2](../../planning/research/R-009_engine_selection_packet_RC2.md), [demanda D1](../../planning/research/R-010_financial_workload_binding_RC0.md).

## 5. Reglas de estrategia y bindings

Las [configuraciones EQ3 RC1](../../planning/research/candidate_configs/PRICE_MATR_rules_RC1.json) y el [contrato RC2](../../planning/research/R-020_rule_binding_completion_RC2.md) son hipótesis, no un Champion. Doce declaraciones; cero ejecuciones históricas de estrategia. El detalle del JSON prevalece sobre este resumen:

- PRICE: breakout de las 126 sesiones previas, ATR20, ratchet propio 10/5/5 propuesto.
- MATR: SMA200, ROC126, top 3, elegibilidad diaria, ranking semanal y protección inicial de 3 ATR propuesta.
- Misma cohorte SPY/QQQ/IWM/EFA/TLT/GLD; target NAV de señal/3, enteros floor con p_auth; sin adds, top-ups ni redistribución automática del cash libre.

Calendario, clocks as-of, identificadores, tratamiento de precios y warmup individual deben quedar fijados sin proxies anteriores a inception. GLD no dispone de 200 sesiones propias previas a enero de 2005. La señal caduca según contrato; ventas/settlement aún no disponibles no habilitan entradas. No usar el open futuro para autorizar retrospectivamente ni sustituir un stop desde el fill por signal-close sin registrar variante/gobierno. HWM, fills parciales y protección son bindings explícitos.

El [binding RC3](../../planning/research/R-020_PRICE_MATR_Alpaca_LEAN_binding_RC3.md) conecta etapas con LEAN/Alpaca/Risk. OP-L1 marketable limit RTH/DAY es propuesta, no política aprobada. Faltan datos/calendario/PIT, orden/TIF/cap, p_auth/freshness, protección parcial/reemplazo, costes/settlement y perfil Risk. D-008 continúa abierto: selección y arquitectura final de Strategy V1 requieren al propietario; no hay ganador obligatorio.

## 6. Datos, derechos y clocks

Las [cuatro DataCards](../../planning/research/datacards/financial_dataset_cards_RC0.json) y [seis tarjetas por instrumento](../../planning/research/datacards/ETF_instrument_admission_RC1.json) siguen **NOT_ADMITTED**. Precio raw, acciones corporativas, disponibilidad/recepción/revisión, calendario/identidad y efectivo cumplen roles distintos. Reconstrucción as-of y replay observado se distinguen; latest-version/last-updated no prueban vintage. [Contrato PIT](../../planning/05_data_contract_RC1.md).

Desde2026-10-28 Twelve Data está VENDOR_INFORMATION_REQUESTED; EODHD, VENDOR_RESPONSE_RECEIVED/PLAN_SCOPE_CLARIFICATION_PENDING/TECHNICAL_ADMISSION_PENDING según resumen del propietario. Fechas reales de recepción UNKNOWN; no correo original inspeccionado ni dataset admitido. Priorizar plan EOD19.99 si cumple, sin imponer All-in-One99.99. Ver [evidencia/contratos](../../planning/research/R-008_vendor_evidence_and_plan_scope_RC1.md). [Kibot/FirstRate](../../planning/research/R-008_perpetual_retention_sources_RC0.md) añaden rutas publicadas de retención permanente. KD1 no recibió barras: diagnóstico body 401 pese al login guest 200. No prueba cobertura ni rechazo global. Norgate conserva la restricción de archivo tras expiración documentada previamente. Ninguna fuente seleccionada. El [protocolo de seis ETF/roles](../../planning/research/R-008_six_ETF_admission_plan_RC2.md) separa histórico, acciones, ejecución, eventos externos, feed PAPER y efectivo/costes; OHLC raw no se mezcla con volumen split-adjusted, ni dividendo reexpresado con qty histórica.

Procesamiento local y envío a IA requieren admisiones separadas. DENY externo por defecto sin derechos demostrados, también para derivados, snapshots o resúmenes licenciados/reempaquetados/reconstruibles; autorización por campo, uso y destino. El núcleo no exige enviar todo el raw al LLM; cada rol recibe sólo campos permitidos. Si falta un campo necesario, se declara la limitación. Llamar snapshot/resultado/backup a un contenido no cambia sus derechos.

## 7. Órdenes, protección y reconciliación

IDs internos de intent/command y mappings con IDs permanentes/de sesión/cliente. Ack, accepted, fill, replace y cancel-confirmed son eventos distintos; timeout implica UNKNOWN sin reenvío ciego. Filled, remainder y reservas se reconcilian, incluidos fills durante cancelación/restart. Protección deseada no equivale a confirmada; incertidumbre activa G1+G2 y los incidentes materiales requieren reanudación humana.

No agregar take-profit artificial para suplir OTO/replace. Sin protección B3 admisible no hay entrada; una nueva tolerancia a quedar sin protección o cambio de regla requiere gobierno. El ledger operativo usa cantidades/cash del broker verificados. La contabilidad económica/referencia se reporta aparte: dividendos modelados no crean buying power. Sin comparabilidad, el P&L paper no acredita paridad ni calificación económica. [Binding/protección RC5](../../planning/research/R-007_Alpaca_protection_reconciliation_RC5.md): ninguna ruta B3 admitida, parcial/OTO/PATCH/cash/restore explícitos; no permiso de desprotección o emergencia.

## 8. Riesgo compuesto

Se aplica la restricción más exigente entre exposición/cash, riesgo hasta protección, gap/slippage, liquidez y reservas concurrentes. R2 mide desde la marca actual a protección válida/confirmada; R1, P&L, pérdidas, drawdown y demás controles son independientes. Protección ausente/inválida/no confirmada o cruzada sin ejecución verificada implica incertidumbre, nunca cero. Menor R2 no autoriza ampliar perdedoras. Entradas nuevas/pendientes conservan p_auth y protección condicional.

Filled, remainder y autorización no enviada son cantidades disjuntas; lifecycle y encumbrance separados. No doble resta de cash/costes/reservas ni omisión de exposición. Solver con monotonicidad demostrada o método adecuado; compare-and-commit, epoch, durabilidad y mappings requieren aceptación. Presupuestos/umbrales D-031 no aprobados. [ADR-006](../../planning/decisions/ADR-006-composite-risk-architecture.md), [ADR-015](../../planning/decisions/ADR-015-remaining-risk-reference-R2.md), [fórmulas RC3](../../planning/research/R-027_risk_formula_spec_RC3.md) y [caps/inputs RC4](../../planning/research/R-027_risk_inputs_and_caps_RC4.md). Min-caps sólo bajo monotonía/separabilidad y baseline/presupuesto restante conocidos; no solver general validado.

## 9. Evaluación económica y estadística

O-B/B/K2/M1/G-R1/ADR-021 y [ADR-022](../../planning/decisions/ADR-022-conditional-expected-drawdown-claim.md) vigentes. EW6-BH con pesos iniciales iguales/deriva natural es primario. Cash y espejo K2 obligatorios; SPY BH/SMA200 secundarios explícitos; mensual sólo sensibilidad predefinida. Exposición equivalente no demuestra equivalencia de riesgo/beta/factores.

Cumplimiento conjunto sin score compensatorio: inferioridad máxima 1 pp CAGR anual; exceso neto mínimo 1 pp anual sobre cash; ES95 diario reducido 20% frente al espejo admisible; DD-E sin deterioro esperado frente a EW6-BH completo con límite superior válido ≤0; volatilidad diaria sin deterioro frente al espejo.

DD-E declara modelo P, horizonte H y estado inicial I0. No garantiza mejora en la mayoría de las trayectorias ni menores pérdidas futuras. Distribución/probabilidad/magnitud/cuantiles se reportan cuando fiables; de lo contrario, falta de estimabilidad explícita. Mejoras extremas raras con mayoría de trayectorias peores son limitación material. DD-P no es un gate aprobado.

Familia/selector/multiplicidad/walk-forward/sensibilidad/latencia, método/calibración/aplicabilidad/suficiencia siguen sujetos a [RC7](../../planning/research/R-020_preregistration_readiness_RC7.md). El [handoff DD](../../planning/research/R-020_DD_specification_handoff_RC0.md) especifica claim/reporte y acota investigación genérica; no valida modelos. E4–E8 no son validación estadística completa. NOT_EVALUATED, INVALID_DATA_OR_METHOD, INSUFFICIENT_EVIDENCE, INCONCLUSIVE, FAIL y PASS son distintos. NO_STRATEGY_QUALIFIED es legítimo.

## 10. Ventanas e integridad

MATR: investigación 2005–2018, selección 2019–2022, confirmación propuesta 2023–2026-09-30. [Exposure ledger](../../planning/research/exposure_ledger.md)/M-11 parcial: **PROPOSED_RESERVE / INTEGRITY_UNKNOWN**. No abrir reserva para seleccionar/reparar ni cambiar ventana por un free tier. Confirmación independiente; contaminación exige alternativa prospectiva revisada por el propietario antes de usarla. Horizonte/estado inicial/warmup se fijan antes de F0, sin elegirlos según resultados.

## 11. Economía y escala

PAPER: Zero/Low Incremental Cost First. LIVE: Economic Value First. Servicios pagos siguen como candidatos futuros; Skills/templates públicos, gratuitos, incluidos o propios. Gasto/contratación requieren aprobación. USD10,000 es referencia nominal, no depósito.

Todos los modelos de costes se evalúan en USD2k/5k/10k/25k/50k; veinte celdas hipotéticas previas conservadas. No elegir escala favorable después de resultados. UNKNOWN no es cero. Separar costes fijos/variables/asumidos/incrementales, impuestos/FX, host/datos/runtime y lock-in. Precios públicos y escenarios no autorizan compras.

## 12. Shadow, pedagogía y aprendizaje

[Shadow](../../planning/06_shadow_portfolio_contract_RC0.md) recibe snapshots pareados/ciegos y propone acciones, prioridad, sizing, fuentes, razonamiento, confianza cuando corresponda y versiones. Nunca genera TradeIntent operativo ni alcanza Execution. Comparación local y rendimiento contrafactual son análisis distintos; D-034 depende de Strategy/datos/motor/costes.

[Pedagogical](../../planning/06_pedagogical_contract_RC0.md) explica hechos desde B4 y cumple contrato completo antes del DoD PAPER: fuentes, cálculos, incertidumbre y límites sin datos inventados. Champion/Challenger conserva registro/evaluación/promoción humana; no aprendizaje que modifique órdenes/riesgo por sí mismo.

## 13. Workflow, storage, observabilidad y seguridad

Los contratos de [workflow/recovery](../../planning/08_job_workflow_recovery_contract_RC0.md), [audit/versiones/deployment](../../planning/08_audit_versions_deployment_contract_RC0.md) y demanda D1 gobiernan ownership, outbox, leases/epoch/attempt, deadlines y un único output admitido por identidad lógica. Workflow at-least-once no demuestra efecto financiero exactly-once.

Restore cambia incarnation, exige reconciliación y no reenvía ciegamente. Agentes sin SQL operativo/cash/broker; análisis sin autoridad de escritura crítica. El [paquete Q-063](../../planning/research/D-025_026_PAPER_workflow_storage_decision_RC0.md) propone dirección de familias condicionada; no cierra stack/SLO/RPO/RTO/retención/durabilidad. Su envelope numérico y evidencia de suficiencia siguen P1 antes de freeze. [Audit/observabilidad RC2](../../planning/research/R-012_PAPER_audit_observability_acceptance_RC2.md) separa audit durable y telemetría local: restore con historia perdida requiere RECOVERY_GAP, no nuevo intento que oculte el receipt perdido. H7/H8/SQLite toy no prueban operación integrada. Backups/audit protegidos y compatibles con licencias. La protección del núcleo es independiente de disponibilidad del agente.

## 14. Pruebas y aceptación

QL0/QL1 build, QL2 nueve checks de componente, QE2 7 PASS/1 FAIL, Risk R3 21 checks/66 estados y fixtures de clocks son evidencia acotada, no paridad integrada ni admisión de motor/broker/target. [QL3](../../planning/research/R-009_local_source_execution_RC3.md) compiló un host local mínimo con entrypoint público y cargó metadata sin ejecutar Main/Engine.Run o backtest; no CLI/Cloud/login. H9 usa SQLite DELETE para transacciones/backup ficticios, no PostgreSQL o poder de recuperación operacional. No sumatoria de PASS. QP1–QP10/B3, actions/pay-date, quotes, parciales, cancel/replace, fees, clocks/calendario, restore y métodos requieren aceptación en su alcance antes del uso correspondiente.

R-030 debe comprobar en Plus/PC personal: fresh clone, fuente/dependencias, autenticación, Skills/herramientas, aislamiento filesystem/procesos/red/IPC, blinding, cuotas, recovery y smoke tests. Acciones del propietario con interfaces seguras/rollback. No Plus/admin en INFOTEP. Aceptación integrada/sostenida P2 antes de PAPER autónomo.

## 15. Fases y Definition of Ready

Preparación mantiene registros/invariantes/revisión independiente. F0 de candidatos de investigación no exige Champion previo. Selección/diseño Strategy V1 y freeze de especificación requieren gobierno antes de DoR; promoción operacional después de implementación/validación según gates.

DoR exige cero P0/P1 abiertos, contratos determinables, evidencias, revisión, aprobaciones y aceptación target aplicable. [Checkpoint vigente](../../planning/17_financial_bindings_and_readiness_RC0.md) enumera pendientes; este RC0 no los cierra. B0–B7 después de DoR y master final congelado, respetando milestones/DoD. Ningún plazo reduce rigor ni obliga estrategia ganadora.

## 16. Fuente de despliegue y gobierno

plan-architect: trabajo candidato. main: baseline estable aprobado. Release/tag aprobado: snapshot reproducible con commit/manifest/evidencia. No merge/tag/promoción automáticos. Cada cambio material actualiza registros, pasa coherencia y se sincroniza con commit/push. Secretos/raw privado fuera de Git; bootstrap sin depender del chat. Freeze aprobado transforma Plan Architect en Plan Guardian; este RC0 no activa esa transición.

**Q-062/A aprobado en [ADR-023](../../planning/decisions/ADR-023-paper-broker-and-backtesting-families.md):** familias broker PAPER/motor seleccionadas en diseño. No CLI/Cloud comerciales asumidos gratis; sin B3 admisible no entradas. Fuentes/derechos, protección/cash/Risk, métodos/configuración, stack transversal y target siguen abiertos. No reclasificar diseño pendiente como test futuro para forzar cierre.

## Checkpoint histórico de propuesta — 2026-10-28; resuelto ADR024

[Q-063](../../planning/research/D-025_026_PAPER_workflow_storage_decision_RC0.md) presenta APScheduler acotado+PostgreSQL frente a Temporal+PostgreSQL; propuesta de huella/familias, no selección automática o suficiencia. No reabre B-RT1. El master sigue DRAFT/NOT_FROZEN/NOT_READY: datos, B3, Risk/parámetros, configuración/validación/selección Strategy, stack final y target permanecen obligaciones reales.

## Admisión del pin LEAN — evidencia actual

[Auditoría de fuente/paquetes](../../planning/research/R-009_current_pin_remediation_RC0.md) demostró helper overwrite inseguro en laboratorio propio. Candidatos BCL/fork reutilizables y experimento aislado aportan evidencia, con timeout01 preservado y continuación02=CONTINUATION_INCOMPLETE_OR_FAILED_NO_REMEDIATED_HOST_ACCEPTANCE. El pin exige remediación/exclusión y regresiones/seguridad/licencias/target antes de aceptación; selección de familia o cero avisos NuGet no lo admiten.

## Q-063 aprobado — 2026-10-29

[ADR-024](../../planning/decisions/ADR-024-bounded-scheduling-and-durable-stores.md) sustituye el estado pendiente de dirección anterior: APScheduler3.x limitado a scheduling/wakeups + PostgreSQL durable, separación C/F y sin SQL agéntico; Temporal reserva. La configuración/suficiencia numérica y durabilidad/seguridad efectiva permanecen P1, no aceptadas por fixtures SQLite. No implementación/target/gasto autorizado.
