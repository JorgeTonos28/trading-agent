# Checkpoint financiero — bindings y stack RC0

**Supersession 2026-10-29:** Q063/A aprobado en ADR024. Este checkpoint conserva evidencia wave12; sus solicitudes Q063 son históricas. Dirección APS3/PostgreSQL decidida; configuración/suficiencia no aceptadas.

2026-10-28. Fuente de estado actual después de a249d77 y ADR-023. **NOT_READY_FOR_IMPLEMENTATION**; implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED, holdout INTEGRITY_UNKNOWN. No cuentas, gasto, datos licenciados, históricos de estrategias o implementación.

## Cierres y evidencia real

| Resultado | Qué queda resuelto | Qué no queda aceptado |
|---|---|---|
| Q-062/A, ADR-023 | Alpaca Paper Only + LEAN source, familias de diseño; reservas IBKR/Nautilus | B1–B5/QP1–QP10/pin/modelos/seguridad/target/LIVE |
| Proveedores | Registro de respuestas reportadas, fechas reales UNKNOWN y derechos por plan/uso/destino | No DATASET_ADMITTED; Twelve requiere aclaración y EODHD alcance de plan barato/contrato/calidad/PIT |
| Costes | Tres precios públicos EODHD añadidos a cinco escalas; escenarios previos conservados | No elección retrospectiva de escala, compra o coste operacional total conocido |
| LEAN local QL3 | Source preflight, build de host mínimo con Program.cs público, seis checks de tipos/entrypoint sin invocarlo | No build de toda solución stock ni Engine.Run/Algorithm; warnings/pin/ejecución completa pendientes |
| Reglas/bindings | Mapa PRICE–MATR→inputs/LEAN/order/Risk/cash/paridad y OP-L1 propuesta explícita | No configuración financiera completa, protección B3 o Strategy V1 seleccionada |
| Calidad de datos | Matriz por seis ETF y rol; fixtures de PIT/pay-date/units/egress | No cobertura/historia/licencia/QA real de ningún ETF |
| D035-T2 | Precondiciones y álgebra de caps incrementales monótonos;900 celdas contra oráculo exhaustivo | No riesgo numérico, solver general, precios/gaps/fees reales o transacción aceptados |
| Ledger/restore | H9 job/outbox/receipts/backup y complemento de copia restaurada; RECOVERY_GAP explícito | No PostgreSQL/FSYNC/power-loss/race de receipts/carga PAPER/seguridad |
| Workflow/storage | [Q-063](research/D-025_026_PAPER_workflow_storage_decision_RC0.md) listo para dirección de familias condicionada | Aún propuesta; no full stack freeze ni suficiencia, no instalación/WSL/VM |

[Scope de probes](research/probe_scope_evaluation_2026-10-28.json) distingue checks calculados, marcadores declarativos y límites. No sumar PASS como validación estadística/financiera. Doce hipótesis, cero trials; cuatro DataCards+seis subcards NOT_ADMITTED. DD-E y B/K2/M1/G-R1 permanecen aprobados sin otra ronda conceptual.

## P0/P1 que aún separan el proyecto de Plan v1.0

| Bloque | Prioridad/estado | Dependencia para cerrar |
|---|---|---|
| Strategy D-008/010 | P0 OPEN/RESEARCHING | Configuración financiera completa y comparación preregistrada; selección/diseño humano, no ganador obligatorio |
| Evaluación D-011 | P0 RESEARCHING | Datos/modelos/método admisibles, familia/selector/uncertainty/suficiencia, M-11; no más DD conceptual sin defecto material |
| Datos D-022 | P1 RESEARCHING | Plan/licencia/retención/egress por rol y seis ETF; muestras autorizadas, calidad/cobertura/PIT/pay-date/cash/ejecución verificables |
| Broker/motor D-021/023 | Familias DECIDED; obligaciones técnicas P1/P2 abiertas | Protección y cash mapping, pin/dependencias/import/modelos/trace/paridad; gates de diseño no se renombran host-specific |
| Órdenes/Risk D-030/031/035 | P1 RESEARCHING/OPEN | B3/ruta, p_auth/order policy/cash; parámetros absolutos/modelos y acciones de protección aprobados; solver/transacciones |
| Workflow/storage D-025/026 | P1; Q-063 dirección READY_FOR_DECISION | Familia/huella; envelope numérico, RPO/RTO/retención y diseño/pin/constraints/pruebas/suficiencia antes de freeze |
| Observabilidad/evals D-028/029 | P1 RESEARCHING | Criterios numéricos/actores/alertas/restore y suite trazable de motor/broker/datos/riesgo; no cierre por fixtures |
| Externas/Shadow D-033/034 | P1 por demanda y scope | Form4 sigue research separado; ninguna señal externa obligatoria en ETF; contrafactual depende Strategy/datos/motor/costes |
| R-030; aceptación D-024/027/037 | P1 TARGET_ACCEPTANCE_DEFERRED | Fresh clone y aceptación Plus/PC personal antes de implementar; operativo integrado/sostenido P2. Diseño agéntico permanece completo |

## Ruta de cierre

1. Resolver Q-063 de dirección de stack y concretar sus gates sin instalar nada ahora.
2. Completar diseño de protección/cash/órdenes/riesgo y admisión de datos por roles; no esperar comercial para lo independiente, ni autorizar compra mientras alcance/valor falten.
3. Congelar configuraciones research/metodología sólo tras sus inputs/gates, comparar candidatos y presentar selección fundamentada al propietario; no consultar reserva de integridad desconocida.
4. Revisar el master integrado, cerrar P0/P1 de diseño y realizar transición target gobernada. DoR/target/freeze/aprobación preceden implementación; main no se modifica automáticamente.

**Siguiente HUMAN_ACTION_REQUIRED preparado:** Q-063, dirección APScheduler3.x acotado+PostgreSQL frente a Temporal+PostgreSQL. Requiere gobierno porque cambia la huella y responsabilidad de workflow respecto al candidato del roadmap. No solicita credenciales, administración, cuentas, gasto o implementación. Protección, datos, parámetros y target siguen pendientes visibles.

[Revisión crítica independiente](research/R-020_financial_bindings_review_2026-10-28.md) realizada: P1 de alcance D1/Q063 reparado, sin otros P0/P1 que bloqueen presentar dirección condicionada. No equivale a aprobación del propietario o aceptación técnica.

[QA final](research/financial_phase_final_QA_2026-10-28.json):65 controles de coherencia PASS; preserva explícitamente los fallos/inconclusos de componentes, sin aceptación financiera o estadística. Todos los cambios materiales deben sincronizarse antes de reportar este hito completado.

## Hallazgo adicional concreto de pin

[Auditoría/remediación LEAN](research/R-009_current_pin_remediation_RC0.md): QL4 securityhelperFAIL dentro del laboratorio propio. Alternativa BCL/fork estudiados; QL5 timeout01 preservado y continuación02=CONTINUATION_INCOMPLETE_OR_FAILED_NO_REMEDIATED_HOST_ACCEPTANCE. Obligación P1 de pin/parches/dependencias/regresión; no sólo test host-specific, no seguridad aceptada ni familia rechazada. Q063 permanece decisión de dirección condicionada, sin modificar esta obligación.
