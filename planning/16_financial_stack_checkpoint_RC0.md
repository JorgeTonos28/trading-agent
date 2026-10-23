# Checkpoint de stack y datos — wave11 RC0

2026-10-23. **NOT_READY_FOR_IMPLEMENTATION**. El [Master Plan RC0](../docs/master/MASTER_PLAN_v1.0_RC0.md) integra el diseño como DRAFT_FOR_REVIEW, sin freeze. Se mantienen implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED y holdout INTEGRITY_UNKNOWN. Sin implementación, backtests de estrategias, cuentas, depósitos ni gasto.

## Avances efectivamente completados

| Frente | Resultado | Límite o cierre |
|---|---|---|
| Q-061 | DD-E condicionado aprobado y registrado en ADR-022 con sus siete condiciones | Claim DECIDED; contrato de reporte especificado. Método/modelo/aplicabilidad no aceptados; [handoff acotado](research/R-020_DD_specification_handoff_RC0.md), sin campaña DD indefinida |
| LEAN | QL2 restore/build/run de componentes PASS; nueve checks nativos de gap, stop-limit, timing, split y defaults de fills/dividendos | No Algorithm/backtest ni paridad aceptada. Algunos PASS confirman defaults que requieren adaptación. [Motor RC2](research/R-009_engine_selection_packet_RC2.md) listo en alcance de familia |
| Datos | Kibot/FirstRate aportan rutas publicadas de retención permanente; derechos locales e IA separados | [Investigación](research/R-008_perpetual_retention_sources_RC0.md). KD1: login 200; seis errores y diagnóstico body 401. Cero barras/admisiones; causa desconocida, sin bypass ni rechazo global |
| Broker | Ruta global Alpaca Paper Only frente a requisitos Pro/funding de TWS; schemas 2026 y límites del simulador comprobados documentalmente | [Broker RC4](research/R-007_PAPER_broker_selection_packet_RC4.md). Cambia prioridad recomendada para PAPER; no selecciona broker ni acredita LIVE |
| Plan | Contratos aprobados/propuestas/dependencias integrados en master RC0; revisión crítica y QA | No se cierran decisiones por redactarlas. [Revisión independiente](research/R-020_financial_stack_independent_review_2026-10-23.md), [QA](research/financial_stack_QA_2026-10-23.json) |

Doce hipótesis, cero trials de estrategia; cuatro DataCards y seis subcards NOT_ADMITTED. Se conservan nominal USD10k, costes en las cinco escalas y veinte celdas hipotéticas previas. Twelve/EODHD AWAITING_VENDOR_RESPONSE por declaración del propietario, sin respuesta, fecha exacta o autorización inferida.

## P0/P1 restantes y dependencias reales

| Bloque | Estado | Evidencia o decisión necesaria |
|---|---|---|
| D-008/010 P0 | Strategy V1 OPEN; reglas PRICE/MATR especificadas, bindings abiertos | Conectar datos, order policy, p_auth, parciales, Risk, costes y evaluación; selección/diseño final del propietario |
| D-011 P0 | Claim DD aprobado y reporte especificado; método/evaluación aún abiertos | Inputs/modelos admisibles, calibración/aplicabilidad/suficiencia, familia/selector y M-11. No reclasificar métodos como simples tests de host |
| D-021/023 P1 | **READY_FOR_DECISION de familias**, no seleccionadas | Q-062 A: Alpaca Paper Only + LEAN source. Después: pins, B1–B5/QP1–QP10 y mappings; aprobación no implica aceptación |
| D-022 P1 | Derechos/cobertura/PIT/calidad/cash abiertos; cuatro+seis tarjetas NOT_ADMITTED | Muestra autorizada y licencia, campos, delays y QA verificables. Consultas comerciales separadas; acceso guest no establecido aquí; sin usar holdout |
| D-030/031/035 P1 de diseño | Cantidades/lifecycle/encumbrances y contrato R2 especificados; fórmulas finales/bindings/parámetros pendientes | Paquete conjunto de órdenes/protección/cash/Risk, solver y transacciones; perfiles numéricos al propietario cuando fundamentados. Pruebas operacionales P2 separadas |
| D-025/026/028/029 P1 | Demanda D1 y contratos disponibles; stack/SLO/durabilidad/restore/evals abiertos | Versiones, modelos, backup y evidencia de durabilidad según demanda; no reabrir arquitectura agéntica general |
| D-033/034 P1 | Form 4 en research; Shadow sin autoridad operativa | Fuente externa sólo si admitida/seleccionada. Evaluación contrafactual depende de Strategy/datos/motor/costes; no se impone fuente externa a la cohorte ETF |
| R-030; aceptación D-024/027/037 P1 | Diseño agéntico completo; target diferido | Bootstrap/auth/aislamiento/cuotas/smoke en PC personal/Plus antes de implementar. Integración/carga sostenida P2 antes de PAPER autónomo. Sin acciones institucionales |

## Ruta restante al master final

1. Q-062 permite fijar las familias de diseño si el propietario aprueba; no habilita setup, gasto ni operación.
2. Cerrar configuración financiera, fuentes/modelos y sus contratos de aceptación, más stack transversal. Licencias y cuentas pendientes no borran diseño abierto; pruebas futuras no certifican hoy.
3. Revisar el master integrado, resolver P0/P1 de diseño y decisiones materiales con revisión crítica cruzada.
4. Ejecutar la transición R-030 en el target cuando corresponda. DoR exige cero P0/P1 abiertos y aceptación aplicable; freeze y baseline/release requieren gobierno. No modificar main automáticamente.

**Siguiente HUMAN_ACTION_REQUIRED:** [Q-062](research/D-021_023_PAPER_stack_decision_RC0.md), selección de familias broker/backtesting con alternativas, evidencia y riesgos. No repetir DD/capital ni solicitar credenciales, funding o gasto ahora.
