# R-020 — protocolo de evaluación completo en diseño RC5

2026-10-14. Especificación candidata, no método técnicamente aceptado ni D011 cerrado. B/K2/M1 permanecen aprobados. Reserva INTEGRITY_UNKNOWN, implementation_locked=true, TARGET_ACCEPTANCE_DEFERRED. Ninguna muestra PRICE/MATR/confirmatoria abierta.

## Orden y unidad de evidencia

Config/version y registro de toda búsqueda → DataCards/rights/PIT/acciones/cash → paridad de modelos/engine → MethodApplicability y validación/calibración → guardrails/escenarios/familia → F0 antes de resultados → desarrollo y selección cronológica → F1/config/selector congelados e integridad auditada → confirmación admisible. Target/DoR y operación conservan gates propios. Este contrato no permite saltar los pasos anteriores con fixtures.

Retornos diarios **de cartera** alineados con NAV financiero y equity económico, costos declarados y misma duración real. NI y cash usan net_after_incremental_ops de S frente a costes propios de benchmarks; ES/guardrails financieros net_trading. Warm-up no puntúa, folds no reinician posiciones favorablemente. Emitir por endpoint inputs, estimador, bounds, diagnósticos, subestado y motivo; agregado conserva todos, no score compensatorio.

## Endpoints M1

- C_NI=CAGR(S_econ)-CAGR(EW6-BH)+0.01, inferior bound debe ser≥0.
- C_CASH=CAGR(S_econ)-CAGR(B-CASH)-0.01, inferior bound debe ser≥0; el efecto mínimo es inclusivo. Sensibilidad con >0 no cambia criterio silenciosamente.
- C_ES=0.8*ES95(M)-ES95(S), inferior bound≥0; equivalente a H_R≤0, **no** ES(S-M). Pérdida=-return, masa fraccional5%, no clipping/tie-overcount.

Referencia ES positiva y estimable, espejo/cash/marks defendibles y composición/beta/factores documentados. Ratios no son calculables por defecto si denominador no positivo. NO_ESTIMABLE es diagnóstico, no éxito. ES95 no sustituye otros riesgos.

## Dependencia, familia e incertidumbre

Propuesta técnica: error de selección familiar≤5% para familia de variantes predefinida. Cada candidata necesita todos componentes AND; Bonferroni por variantes candidatas utilizadas protege familia **si tests válidos**. N incluye versiones/ablations escogidas a partir de resultados, no sólo dos finalistas; el ledger actual declara8 hipótesis anteriores y nuevas parametrizaciones separadas. N y reservas de error deben congelarse antes; nuevas búsquedas requieren versión/familia/confirmación nueva, no count retroactivo. Confirmación de una config congelada tiene familia propia. α/criterios técnicos finales no quedan aprobados por M1.

Bloques pareados de vectores S/B/M/cash con mismo índice; dependencias en diferencias/logretornos/loss/cuadrados y regímenes, no trades iid. Block selector/formula/sensibilidades previstos, no elegir tamaño con mejor PASS. Basic/percentile y otros métodos están sujetos a calibración; pin arch8, code/data hashes, seeds y réplicas. Vector de CI marginal no significa jointcoverage95%. Remuestreo de retornos no es backtest de ordenes sobre otra cronología.

## Gate MV — aceptación de métodos, obligatorio antes de PASS

| Gate | Evidencia requerida | Estado actual |
|---|---|---|
| MV01 input/estimando | Finite/escala/cash/costos/clocks, ES fraccional, cambios de unidades/corporate events y denominador | PARTIAL_SYNTHETIC |
| MV02 error | Nulidad por cada componente, **least-favourable null** con demás gates verdaderos, AND/familia y todos errores registrados | NOT_ACCEPTED; E5 sólo nulidad de todos a la vez |
| MV03 dependencia | IID, AR, volatility clustering/heavy tails, breaks/gaps y distintas correlaciones/overlap | PARTIAL_SCREEN; no generalización |
| MV04 precisión MC | Repeticiones/bounds MonteCarlo para comprobar error en α efectivo familiar, sin confundir draws con nuevos años | NOT_ACCEPTED |
| MV05 cobertura/power | CAGR/ES/guardrails de interés, alternativa material definida y precisión/suficiencia antes de resultados | NOT_ACCEPTED |
| MV06 estabilidad | Bloques/métodos preregistrados, mismas conclusions defendibles o insuficiencia explícita; no réplicas inválidas omitidas | NOT_ACCEPTED |
| MV07 patologías | InputsNaN/Inf/constantes, colas/dependencia insuficientes, ESref no positivo, returns≤-1, censura/marks/data gaps | PARTIAL_SYNTHETIC |
| MV08 revisión/paridad | Fuente/version/licencias/pins/independent review y repro en target cuando corresponda | DESIGN_REVIEW_PENDING; TARGET_DEFERRED |

Diseñar full-calibration por precisión: por ejemplo para p=.05, semiancho normal aproximado0.005 exige~7300replicas MC, aún más para error pequeño de familia; Wilson/binomial exacta y cases boundary determinan regla final. No usar M80/E4M160 como PASS. Bootstrap draws internos necesitan suficiente masa al cuantil efectivo y estabilidad independientes de MC. Esos presupuestos son cálculo de protocolo, no quota/duración target garantizadas ni permiso de gasto.

E5 realiza screening de CAGR/ES reales como **funcionales de DGP ficticia**, no suficiente gateMV completo. Si screening muestra defectos, no expandir calificación; elegir nueva investigación/método con registry y evidencia, nunca cambiar M1. No hay obligación de gastar CPU en full-calibration de un contrato guardrail aún no aprobado; el trabajo requerido sigue marcado para su versión final antes de F0/PASS.

## Suficiencia y decisión

Predefinir Effect/SampleCard: número de sesiones, masa extrema efectiva/clusters/dependencia, episodios/regímenes y incertidumbre admisible. Cantidad nominaln(1-q) no conteo independiente. Power/precisión se evaluarán bajo supuestos explícitos; no asegurar80% a partir de n≥1000 o trades≥30. Si condiciones de estimador o data faltan => NOT_EVALUATED/INVALID según motivo. Muestra declarada insuficiente=>INSUFFICIENT; muestra válida con bound que cruza criterio=>INCONCLUSIVE. FAIL económico exige evidencia válida contraria o violación determinística de guardrail previo; simple noPASS no equivale a inferioridad.

PASS_SCOPE_SELECTION/CONFIRMATION sólo todos endpoints y guardrails válidos/pasados, costo/escala definidos y método aceptado. Benchmark y estrategia no pierden sesiones malas ni pagan el mismo overhead ajeno. Ninguna PASS promociona Champion o LIVE. Todos no calificados=>NO_STRATEGY_QUALIFIED con razones, sin holdout para reparar.

Agregación guardrails conforme tabla Q059: DD/σ son gates cuantitativos propuestos; recovery/extremos requieren reportes completos/admisibles sin inventar duración de censura. Censura legítima bloquea claim exacto de duración, no todos los otros gates por sí sola. Modelo de stress inválido o reporte faltante sí bloquea evaluación global; límites Risk no aprobados bloquean operativo/DoR aparte. Inferencia sobre DD necesita estimando/path/horizonte validado; MDD histórico no demuestra expectedMDD futuro por remuestrear una trayectoria.

Guardrails nuevas propuestas en [Q059](D-011_complementary_guardrails_proposal_RC0.md), costes/escala en [SC0](R-020_cost_scale_scenarios_RC0.md), reglas en [configs](R-020_PRICE_MATR_rule_configurations_RC0.md) y fuentes en [DataCards](R-020_dataset_cards_RC0.md). F0 permanece incompleto hasta resolver sus obligaciones; no presentar diseño del protocolo como validación estadística final.
