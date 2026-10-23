# Preregistro RC7 — grafo de decisión, inferencia y admisión

2026-10-23. Complementa y sustituye las filas vigentes de readiness RC6; preserva historia. **F0_NOT_FROZEN / METHOD_NOT_ACCEPTED**, D-011 RESEARCHING. B/K2/M1/G-R1 y ADR021 intactos. No estrategia, dato, broker o engine aceptado; holdout INTEGRITY_UNKNOWN.

## Corrección de dependencia D011-T1

F0 admite **candidatos de investigación**, no requiere Champion operativo ni ganador previo. `RULES_SPECIFIED → CONFIG_ADMITTED_FOR_RESEARCH → F0 research → evaluación de selección/F1 → confirmación aplicable` expresa gates de investigación, sin autorizar su ejecución antes de admisión. El diseño de Strategy V1 seleccionado/aprobado y congelado pertenece a DoR; después de DoR/aceptación target viene implementación, validación operacional y promoción PAPER. La evidencia operacional no puede exigirse como condición circular para empezar a implementar. Las fases pueden conservar NO_STRATEGY_QUALIFIED; no promover sólo para cumplir calendario.

La revisión independiente detectó y reparó el ciclo en RC6 y la lectura circular posterior; [reglas RC2](R-020_rule_binding_completion_RC2.md) es el contrato vigente. D011-T1 cierra **sólo semántica de admisión y fases**, no selección, F0 ni método. Los requisitos de evidencia económica antes de selección/promoción siguen los scopes del plan; sus condiciones incumplidas no desaparecen por esta corrección.

## Evaluación conjunta, sin sustituciones

Mantener cinco endpoints AND: NI1ppCAGR frente EW6 completo; exceso cash+1pp neto; ES95 diario reducción20% frente espejo K2 admisible; DD no deterioro frente EW6 completo; volatilidad diaria no deterioro frente espejo. Renta neta operacional incorpora overhead incremental correspondiente y todas cinco escalas; riesgo financiero net_trading según RC4/RC6. Espejo no demuestra equivalencia de beta/factores. Reportar oportunidad frente SPY, recuperación/censura/underwater/acumuladas/gaps/extremos.

IUT para una candidata no implica intervalos simultáneos ni corrige búsqueda entre12hipótesis. Familia/selector/error por variante/fase, descartes y revisión adaptativa deben congelarse antes de resultados. α_F=.05 es propuesta de error estadístico, **no probabilidad de pérdida financiera**. Bounds/MC dependientes de método no se eligen por qué produce PASS. Sin método aplicable no existe PASS económico; falta de precisión no implica FAIL.

## Pregunta material ya fundamentada: significado del DD

[E8](probes/r020-dd-identification/README.md) demuestra exactamente, con leyes ficticias, que el mismo DD esperado diferencial−0.001 puede coexistir con90% o10% de trayectorias con DD peor. No es dato de mercado ni prueba de que suceda en PRICE/MATR. DD-E, DD-P y pathwise son claims distintos: se propone [Q-061](D-011_DD_claim_decision_RC1.md) antes de congelar el claim final, sin pedir otra tolerancia G-R1.

Conservar H por calendario/fase y fresh/flat/priorwarmup pre-F0, sin elegir carry después de selección. El bound ilustrativo de E8 exige paths H independientes observados bajo supuestos; no convertir draws de un modelo ajustado o ventanas solapadas en años independientes. Sus ocho checks incluyen un sentinel declarativo de independencia; no validación estadística. θ_D debe declarar P/modelo/I0/reglas y separar incertidumbre de datos, ajuste, misspecification y MonteCarlo.

## Condiciones necesarias antes de PASS, no promesas de potencia

MV01–08 de RC6 permanecen: calibración marginal al borde con otros gates verdaderos; AND/familia/selector; dependencia AR±/clusters/colas/regímenes/gaps; cobertura/potencia y precisión; bloques y sensibilidad prefijados; degeneración/censura; revisión independiente y aplicabilidad al dataset. Los E4–E8 son componentes/screens. No hay método universal validado ni prueba de imposibilidad global de G-R1. Bootstrap genérico de retornos de cartera no equivale a replay causal del mercado/políticas; un número grande de replications no resuelve misspecification.

Preregistro final debe incluir: versiones/pins/código de cálculo; fuentes y universo IDs; clocks/ajustes/actions/cash; configuraciones y variantes; calendarios, ventanas y warm-up; order policy/parciales/p_auth/latencias/expiry; modelos de ejecución/costes; perfil Risk; endpoints/estimandos/H/I0; familia/selector y gasto de error; gates de muestra/cola efectiva/regímenes; fallos/estados; protocolo de confirmación y exposición; outputs de paridad y review. Cada UNKNOWN conserva bloqueo en su scope.

## Readiness actualizado

| Bloque | Completado ahora | Falta real |
|---|---|---|
| PRICE/MATR | Reglas de indicadores, ranking, target, expiry/settlement y protección RC2 | Binding fuente/calendario/órdenes/Risk/costes; aprobación de candidata de implementación/selección |
| Datos | Wave06, clocks CA-S1, derechos Norgate, SFP versus SEP |4DataCards+6subcards NOT_ADMITTED; licencia/cobertura/calidad/vintages reales, cash realizable |
| Broker/engine | RC3 brokers, QE2 nativo, QL0/QL1 compilados, recomendación LEAN condicionada | Broker elegido/eligibilidad, parciales/stop/replace/recovery; engine/pin/deps y QP integrado admitidos |
| Riesgo | RC3 cantidades/lifecycle/claims separados; R3 aritmético | Parámetros absolutos D031, fuentes, modelos de escenarios, solver/atomicidad/txn y pruebas |
| Estadística | Endpoints económicos ya aprobados; semántica de claims y límites de E8 explícitos | Q061; MV aplicado/validado, suficiencia sin relajar márgenes |
| Confirmación | Exposure ledger y M11 parcial | Reserva no acreditada; alternativa prospectiva gobernada si necesaria |
| Entorno | Diseño agente aprobado | R030 personalPlus P1 antes de implementar; integrado/sostenido P2 antes de PAPER autónomo |

Estados siguen NOT_EVALUATED, INVALID_DATA_OR_METHOD, INSUFFICIENT_EVIDENCE, INCONCLUSIVE, FAIL y PASS en scope definido. D-011 global no cierra; no backtests prematuros. Plus/admin institucional no solicitados.
