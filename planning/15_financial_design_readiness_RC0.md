# Checkpoint financiero y readiness de Plan v1.0 — RC0

**Estado actual 2026-10-28:** ver [readiness17](17_financial_bindings_and_readiness_RC0.md); este checkpoint conserva historia. Q062 aprobado sólo familias; datos y B3 no admitidos; Q063 propuesta condicionada, sin aceptación o implementación.

2026-10-23. Plan Architect, rama plan-architect. **Diseño financiero aún incompleto; no READY_FOR_IMPLEMENTATION.** Agentic architecture design scoped complete ADR014; no expansión de R006/010/013. implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED, reserva INTEGRITY_UNKNOWN. No dataset admitido/estrategia seleccionada/backtest histórico ejecutado.

## Cierres técnicos de este paquete

| Subitem | Cierre acotado y evidencia | No significa |
|---|---|---|
| D035-T1 | Semántica de cantidades/lifecycle/encumbrances reparada, revisión independiente, [RiskRC3](research/R-027_risk_formula_spec_RC3.md), R3:21checks/66estados finitos | Risk Engine, solver/txn, parámetros o D035 aceptados |
| D011-T1 | F0 research no exige Champion; diseño aprobado/DoR/implementación/promoción operacional separados, [RC7](research/R-020_preregistration_readiness_RC7.md) | F0 congelado, candidato seleccionado o evidencia económica/operativa aprobada |
| Reglas EQ3 | SMA/ROC/ATR/ranking/slots/target/expiry/settlement/ratchet/HWM explícitos, [RC2](research/R-020_rule_binding_completion_RC2.md) | Configuración financiera completa: orden/datos/p_auth/Risk/costes aún pendientes |
| R007 comparación | Inventario concreto de activación/protección/replace/binding/recovery y finalistas de ingeniería [RC3](research/R-007_broker_execution_evidence_RC3.md) | Broker elegido, RD/KYC concedido o paridad paper/live |
| R009 viabilidad | Nautilus matcher nativo y LEAN Common/Engine componentes compilados; [recomendación condicionada](research/R-009_engine_recommendation_RC1.md) | Engine seleccionado, fidelidad integrada o seguridad aceptada |
| R008 admisión | [Wave06](research/R-008_sources_admission_wave06_2026-10-23.md), CA-S1, separación SFP/SEP y retención/IA/costes | Derechos de uso, calidad o PIT real admitidos |

No cerrar un parent P0/P1 por concluir un subitem. Capturas, errores, FAIL y limitaciones están en [índice de probes](research/R-020_financial_probe_findings_2026-10-23.md). Revisión independiente en [acta](research/R-020_financial_independent_review_2026-10-23.md).

## Matriz P0/P1 vigente: dependencias reales

| Prioridad/ID | Qué falta para cerrar diseño | Dependencia real / quién |
|---|---|---|
| P0 D008 | Selección/diseño Strategy V1, sin ganador obligatorio | Reglas/config y D011/datos/costes; propietario para decisión final |
| P0 D010 | Especificación MATR candidata completamente vinculada | Reglas ya precisadas; fuente/calendario, order/protection/p_auth, Risk/costes y engine. PRICE mismas dependencias; no privilegiar MATR |
| P0 D011 | ClaimDD DECIDED ADR022; métodos aplicables/validados, familia/selector/muestra, protocolo completo y confirmación | Q061 aprobado; falta admisión técnica de método/datos, sin mover márgenes. IntegridadM11/ledger, no abrir reserva por conveniencia |
| P1 D021 | Broker/cuenta/eligibilidad y mapping seleccionado | IBKR/Alpaca finalistas, Tradier reserva; B1–5 evidencia por API/ruta y decisión humana. Parte práctica requiere cuenta target, no correo de históricos |
| P1 D022 | Datos primarios, cash y validación secundaria admitidos |4cards+6subcards, rights/retention/IA/coverage/PIT/calidad; respuestas Twelve/EODHD sólo una ruta. Muestras autorizadas y pruebas técnicas pendientes |
| P1 D023 | Motor/pin/packaging/modelos y paridad de diseño aceptables | LEAN principal de investigación, Nautilus alternativa; QP integrado, dependencias y modelo dividendos/liquidez, sin elegir por retorno |
| P1 D030 diseño | Entry/TIF/cap/p_auth/stop/protección parcial/cancel-replace/fill/settlement | D021/022/023/035 y requisitos de Strategy; pruebas integradas operativas P2 separadas |
| P1 D031 diseño | Perfil inicial numérico, hard/soft/freshness/gaps/liquidez y acciones compatibles G1+G2 | Propuesta fundamentada tras inputs/modelos; aprobación humana de política. Calibración/kill-switch operacional P2, no trasladar todo el diseño a P2 |
| P1 D035 | Fórmulas/input/modelos/solver/compare-and-commit completos | RC3 elimina errores; D021/022/026/030/031 para mappings/atomicidad y presupuesto. Nada se autoriza con UNKNOWN |
| P1 D025/026 | Workflow/store/versiones/durabilidad/ownership y restore seleccionados | Demanda financiera [D1](research/R-010_financial_workload_binding_RC0.md), incidencias/fees/events y recursos. Temporal/APS/Postgres/SQLite candidatos; más evidencia de configuración/operación, no cierre por nombre |
| P1 D028/029 | SLO/RPO/RTO/reportes/runbooks y suite conjunta/preregistro | Demanda/stack, fuente/broker/engine y fallos obligatorios. Criterios diseñables en Team; ejecución operacional después de implementación |
| P1 D033 | Alcance de fuentes externas V1 y admisión por rol/dataset | Form4 investigación; fuente pública no señal operativa admitida. No forzar SmartMoney dentro de ETF ni detener reglas ETF por falta de históricos Form4. Datos externos operativos sólo si seleccionados y admitidos |
| P1 D034 | Comparador Shadow y trayectoria contrafactual con costes/latencia/modelos | Contratos ya existen; D008/011/022/023/030 para evaluación y métricas. Aislamiento target R030, sin nueva autoridad |
| P1 R030; D024/027/037 aceptación | Plus/PC personal, fresh-clone, auth, aislamiento efectivo, cuotas/recovery/smoke | **TARGET_ACCEPTANCE_DEFERRED**; diseño agente cerrado. Requiere transición al target antes de implementación; no solicitud de acceso/admin institucional ahora |

D030/D031 se descomponen ahora trazablemente: sus decisiones de diseño/configuración son **P1**; validación integrada/ajuste autorizado previo a PAPER permanece P2. Corrige una dependencia oculta de DoR, sin aprobar política, implementación o nuevos alcances. D032 transición a PAPER continúa P2. No calcular avance sumando documentos o checks.

## Qué nos separa de Plan v1.0

1. **Contrato financiero determinable:** unir reglas con datos/órdenes/protección/Risk/costes, resolver conflictos de parciales y stop basado en fill, elegir broker/engine y fuente con evidencia suficiente. No reconstruir precios históricos para llenar huecos jurídicos.
2. **Contrato de evaluación admisible:** decidir significado DD, validar métodos/aplicabilidad/suficiencia, cerrar familia/selector y tratamiento de integridad/confirmación. Mantener NO_STRATEGY_QUALIFIED como salida real.
3. **Stack y operación especificados:** workflow/storage/audit/observabilidad/evals ligados a demanda; sin prototipos de producción. Review crítica y reconciliación de roadmap/ADRs/contratos en un MASTER_PLAN candidato único.
4. **Gobierno/freeze y target:** revisión de Plan v1.0; aceptación R030 personalPlus antes de DoR/implementación y promoción de baseline/release sólo con aprobación. Un documento revisable puede enumerar obligaciones target pendientes, pero no afirmar que es el contrato final READY con P0/P1 abiertos.

No se necesita esperar ambos correos para los puntos independientes. Tampoco se puede declarar diseño financiero cerrado mientras un mapping o método crítico esté sin resolver. No se necesita otra ronda general de arquitectura agéntica.

## Secuencia ejecutable posterior y siguiente gobierno

El paquete autónomo actual cubrió reglas, recursos, matching, compilación fuente, alternativas/PIT/costes y revisión. Q061 quedó aprobado en ADR022; la siguiente tarea autónoma es resolver datos/broker/engine y bindings financieros. No volver a pedir aprobación de su significado o tolerancia. En paralelo posterior: B3/protection bindings y evidencia admisible de datos; QP/adaptaciones de engine; propuesta conjunta Risk/órdenes y stack D1. Las respuestas externas se evalúan cuando existan, sin autorizar usos por respuesta genérica.

## Actualización wave11 — 2026-10-23

[Checkpoint16](16_financial_stack_checkpoint_RC0.md) es readiness vigente. Q061DECIDED; Q062familiastecnológicas READY_FOR_DECISION, no stack/pin/broker/target admitidos.
