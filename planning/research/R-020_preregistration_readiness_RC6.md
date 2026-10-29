# Preregistro RC6 — cumplimiento conjunto, readiness y pendientes reales

2026-10-15. Consolidación deRC5 con ADR020, configuracionesEQ3, subcards, broker/risk y probes. **F0_NOT_FROZEN / METHOD_NOT_ACCEPTED**. DoR no alcanzado; Strategy V1 OPEN. No cambia B/K2/M1/G-R1 ni abre datos/holdout.

## Endpoints y error

NI/cash usan retorno económico de S después de costes incrementales correspondientes y benchmarks con costes propios; ES/DD/σ usan net_trading financiero. Mantener contrastesC_NI≥0, C_cash≥0 y C_ES≥0 segúnRC5. DD observado y claim inferencial de [DD applicability](R-020_drawdown_method_applicability_RC0.md) no se confunden; realización inferencial requiere checkpoint explícito. Volatilidad diaria=desviación estándar del retorno de la población/modelo/horizonte definido, no automáticamente estimador válido por usar ddof1. No annualizar por√252 para decidir guardrail diario ni sustituirlo por downside deviation.

Para una candidata calificada por **AND de cinco endpoints**, un componente nulo válido basta para acotar falsa calificación por el nivel de su test; IUT no exige independencia entre endpoints. No es cobertura simultánea de5intervalos. Entre variantes, presupuesto familiar y selección adaptativa siguen control propio. α_F=.05 continúa propuesta técnica, no validación ni aprobación de probabilidad de pérdida; α_i se fija según familia/selector antes de resultados. Bonferroni entre candidatas sólo protege si tests válidos; no ocultar error marginal bajo baja potencia de otros gates.

Registro actual12hipótesis/parametrizaciones,0trials; no asumir N=2 porque dos son propuestas prioritarias. Declarar qué resultados/searches influyen en selección y familia completa; controles exploratorios nunca se convierten en confirmatorios por renombrar muestra. Ningún reinicio gratuito del presupuesto al cambiar familia/etapa. Bootstrap draws y MonteCarlo replications son presupuestos distintos, no años adicionales.

## Validación antes de calificar

| Bloque | Protocolo necesario | Estado actual |
|---|---|---|
| MV01 | Inputs/estimandos/unidades/cash/PIT/ES fraccional y DDpath | Componentes ficticios parciales; no admisión real |
| MV02/04 | Error de cada nulidad al borde con otros gates verdaderos, AND y familia; precisión binomial por α efectivo | E5/E6 screening, no validado |
| MV03 | IID; ARpositivo/negativo; clusters/tail con momentos suficientes; breaks/gaps como misspecification; correlación y costos/estado | Sólo screens parciales |
| MV05 | Cobertura/potencia/precision de CAGR/ES/σ y DD claim elegido; efectos previos, no sólo tests de media anual | NOT_ACCEPTED |
| MV06 | Bloques/métodos y presupuestos previos, estabilidad y sensibilidad; no elegir método que da mejor tasa | NOT_ACCEPTED |
| MV07 | Constantes, returns≤−1/NAV≤0, NaN/Inf, ESref no positivo, cola efectiva, censura/gaps, invalidez de modelo | E7 yprevios parciales, no gate global |
| MV08 | Review independiente, fuente/pin/paridad técnica y aplicación al dataset/modelo del claim | Review diseño parcial, engine/datos no aceptados |

Los casos con varianza/momentos/dependencia incompatibles con el método deben mostrar inadmisibilidad, no `FAIL estrategia`. Preregistrar los cuantiles/bloques/calibración y la precisión MC antes de cada campaña. Evaluar bloques5/20/60 como sensibilidad propuesta; no seleccionar por retorno ni por qué daPASS. Niveles efectivos pequeños requieren muchos draws/replications; estimar coste local antes de campaña completa. No fijar un número mágico de trades/días/tailpoints para prometer potencia.

## F0 readiness explícito

| Requisito | Evidencia persistente | Pendiente |
|---|---|---|
| Utilidad/benchmarks/guardrails | ADR016–020 | B/K2/M1/G-R1 aprobados; no reabrir sin evidencia material |
| Reglas/target/estado/calendario | [RC1](R-020_configuration_completion_RC1.md),2nuevasEQ3 conparents | Mapping orden, Risknumeric/costs/scale y ownerStrategy final |
| Fuentes/rights/PIT/QA |4DataCards +6subcards [wave04](R-008_dataset_admission_wave04_2026-10-15.md) | TodasNOT_ADMITTED, metadata GLD no historia |
| Ejecución/paridad | [BrokerRC2](R-007_protection_dependency_contract_RC2.md), [enginewave02](R-009_engine_components_wave02_2026-10-15.md) | B1–5/QP1–10 pendientes, sin broker/engine seleccionados |
| Risk/claims | [RC2](R-027_risk_formula_spec_RC2.md) | Parámetros/solver/txn y D031 absolutos no aprobados |
| Costes/capital |20celdasSC0 hipotéticas | Nominal10k aprobadoADR021, costes obligatorios en5escalas y todos modelos; fuentes/costes reales UNKNOWN, no elegir K favorable |
| Estadística/selector/familia | RC5/RC6/DDapplicability | ClaimDD y métodos/calibración/suficiencia antes dePASS |
| Integridad/confirmación | Exposure ledger/M11 parcial | PROPOSED_RESERVE/INTEGRITY_UNKNOWN; alternativa prospectiva gobernada si necesaria |

No confundir aprobación de una hipótesis para investigar con Strategy seleccionada, método admitido, F0sellado o operación autorizada. Los parámetros necesarios para implementación no desaparecen enP2 por etiquetarlos calibración; aceptación target R030 sigueP1 separada. No solicitar Plus/admin INFOTEP.

## Evidence states

NOT_EVALUATED: falta requisito/ejecución. INVALID_DATA_OR_METHOD: input/modelo no admisible. INSUFFICIENT_EVIDENCE: muestra/cobertura/precisión previamente insuficiente. INCONCLUSIVE: evidencia válida no resuelve lado del criterio. FAIL: evidencia válida adversa/violación determinística del criterio preregistrado; no mera falta de significancia. PASS_SCOPE_SELECTION/CONFIRMATION sólo si todos endpoints y gates/reportes admisibles pasan en ese scope. Reporte de recuperación censurada puede estar completo sin duración exacta; no inventarPASSestadístico. Todos no calificados=>NO_STRATEGY_QUALIFIED con razones, sin reparación en holdout.

[ADR021](../decisions/ADR-021-PAPER-economic-reference-capital.md) fija nominal10k y evaluación de costes en todas5escalas; actual costsUNKNOWN no se convierten en0. Se preservan20celdas hipotéticas, no son cotizaciones.

## Fuente alternativa/PIT — 2026-10-23

[Wave05](R-008_alternative_actions_PIT_wave05_2026-10-23.md) examina acciones corporativas Databento como alternativa complementaria: revisión/alta/disponibilidad/recepción y replay observado versus reconstrucción se distinguen. Matriz CA01–09 especificada, NOT_EXECUTED; ninguna API/muestra/cuenta. WRAP condicionado/REFERENCE_ONLY actual; no source selected ni admisión. Derechos de retención/IA, cobertura/calidad, costes y paridad siguen pendientes. No esperar respuestas Twelve/EODHD para continuar P0/P1; envío automático prohibido. Las notas anteriores de autorización de comunicación son históricas, sustituidas por entrega personal del propietario.

F0_NOT_FROZEN/METHOD_NOT_ACCEPTED; 12declaraciones, 0trials. Conservados B/K2/M1/G-R1, referencia10k y costes en todas5escalas,20celdas y UNKNOWN explícito; reserva INTEGRITY_UNKNOWN, locktrue/targetdeferred.

## Vigencia técnica wave10 — 2026-10-23

Readiness vigente RC7 corrige dependencia de Champion antes de F0; RC6 queda histórico, no exige promoción operacional antes de implementar.
