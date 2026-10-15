# R-020 — inferencia, estimandos y evidencia RC4

2026-10-14. Investigación bajo ADR-016/017/018, propuesta técnica previa a resultados. No método validado ni márgenes aprobados, F0 incompleto, reserva INTEGRITY_UNKNOWN. Operación y alpha siguen separados. PRICE/MATR no ejecutados.

## Estimandos sin cambiar la pregunta

Competitividad: ΔR=CAGR(S)-CAGR(EW6-BH); cash: ΔC=CAGR(S)-CAGR(B-CASH), ambos sobre NAV neto/contabilidad unitizada del mismo calendario. Para fixtures252 sesiones/año es simplificación; evaluación usa365.25/duración real, no annualización por sesiones invertidas.

Streams explícitos: NI y cash usan **net_after_incremental_ops** de S frente a benchmarks con costes propios; reportar también **net_trading** para distinguir alpha de coste del sistema. ES primario/guardrails de riesgo financiero usan **net_trading** de S y espejo, misma contabilidad temporal de mercado; efecto de costes operativos sobre equity económico se reporta separado, no se omite del retorno. No imputar overhead de AI/datos/infra al benchmark pasivo para hacerlo artificialmente inferior. Distribución de F/uso/K y calendario de accrual se preregistran; costes/capital UNKNOWN => NOT_EVALUATED de calificación económica operacional, no costes0 asumidos. λ usa NAV financiero, no importe económico después de gasto externo; no modificar Risk Engine/contabilidad del broker desde esa atribución.

Riesgo candidato: ES_q de **loss=-retorno diario simple de cartera**, sin recortar ganancias a0. Para muestra n, m=n(1-q), pérdidas descendentes L_(i), k=floor(m): ES=(sum_{i≤k}L_(i)+(m-k)L_(k+1))/m. Fracción/ties definidos, no promediar todas las observaciones iguales al cuantil ampliando masa de cola. ES negativo/no positivo puede ocurrir; no convertirlo en0 para fabricar comparabilidad.

Contraste propuesto H_R=ES(S)-(1-ρ)*ES(M), M=EW6-BH-LAMBDA-REAL. Evita dividir entre un estimador inestable; **no resuelve** referencia no positiva/cola escasa. Evaluación exige riesgo de referencia positivo y suficientemente estimable con regla previa; faltante => INSUFFICIENT_EVIDENCE/NO_ESTIMABLE o INVALID según motivo. Ratio y H se reportan para interpretación cuando admisibles. ES(S)-ES(M) **no es** ES(S-M); pareado describe timestamps/remuestreo, no un cambio de estimando.

ES95 candidato frente a97.5/99: mismo n≈1008 ofrece masas nominales50.4/25.2/10.08, no clusters independientes. 95 conserva foco en pérdidas extremas con más información que99 en muestra limitada; no escoger q por el resultado ni declarar 50 observaciones suficientes. Sensibilidad de cola predefinida no modifica primario aprobado posteriormente.

## Intervalos y prueba conjunta

Datos válidos/criterios completos primero. Propuesta de límites unilaterales para ΔR/ΔC (inferiores) y H_R (superior); guardrails con contraste y regla propios. PASS económico sólo si todos gates y aplicabilidad/suficiencia pasan. Bound que no pasa por incertidumbre => INCONCLUSIVE o INSUFFICIENT, no evidencia automática contra candidata. Evidencia contraria requiere bound opuesto válido o guardrail determinístico predefinido.

AND/intersection-union no necesita tratar un vector de CI como cobertura simultánea: testear todos componentes a nivelα para una candidata controla rechazo de su null unión **si cada test es válido**. Familia entre candidatas/versiones requiere protección adicional. Propuesta conservadora Bonferroni sobre número previo de candidatas/variantes usadas para selección; no esconder búsqueda al contar sólo dos finalistas. Confirmación de una config congelada tiene familia propia previamente declarada, no corrige selección contaminada.

Bootstrap por bloques de vectores alineados S/B/M/cash/factores; mismos índices en todos. Remuestreo inferencial de retornos ya contabilizados **no es** un nuevo backtest ejecutable ni prueba de comportamiento de órdenes bajo otra cronología. [arch8 docs](https://bashtage.github.io/arch/bootstrap/confidence-intervals.html) distingue métodos y dependencia; [block length](https://bashtage.github.io/arch/bootstrap/generated/arch.bootstrap.optimal_block_length.html) opera por columna. Elección previa debe incluir diferencias, pérdidas/cuadrados y dependencia relevante, no sólo media de S. No elegir bloque/método que genere menor p-value.

Basic/percentile son candidatos, ninguno seleccionado por el piloto. Cobertura requiere calibración de estimandos reales (CAGR/ES/DD), colas/dependencia/volatility/regímenes, degeneración y precisión Monte Carlo. Un bloque20 tampoco repara cualquier no-estacionariedad. Resampling de paths cambia drawdown/recuperación: incertidumbre requiere estudio separado/censura, no trasladar mean-CI a máximo drawdown.

## Admission externa y suficiencia

- Finite todos inputs, retornos simples>-1 salvo default definido, monotonicidad/clocks/calendar, escala/unidades y costes coherentes antes de librería. E4 observó Inf que devolvió límite finito0: un output finito no demuestra input válido.
- Constantes/cola degenerada/ESref no positivo, pocas masas o bloques efectivos: no precisión infinita económica. No quitar réplicas inválidas ni cambiar métrica por conveniencia.
- Efectos/margen, alpha/familia, power o precisión, bloques/regímenes/coverage y reglas de stops/fees/delays se preregistran. Muestra posterior sólo se evalúa contra la regla, no se ajusta la regla a esa muestra.
- Piloto E4 de media anual ficticia informa limitaciones, no power ni alpha para PRICE/MATR. M=160 da incertidumbre amplia: no reclamar calibración aprobada.
- Propuesta de evidencia: precisión del bound más estrecha que una fracción predefinida del efecto mínimo, potencia nominal≥80% bajo alternativa material especificada y control de error con incertidumbre Monte Carlo. Cantidad de repeticiones se diseña para esa precisión; no tratar80% en un fixture como regla ya aprobada.
- Reportar cola nominal, clusters/overlap/episodios, años/regímenes, concentración, sensibilidad a bloque/costes/delay. Ningún conteo universal de30/100 trades da permiso.

Todos insuficientes => NO_STRATEGY_QUALIFIED con razones; no cambiar margen ni usar holdout como research. Configs/métodos no aprobados => NOT_EVALUATED. Guardrails financieros del Risk Engine y económico-estadísticos no son la misma política.

## Reutilización

arch8 primitives y statsmodels0.15/Wilson/Holm/Bonferroni: REUSE_AS_IS funciones + WRAP validación externa, candidato no selección. E4 sin instalación nueva; licencias transitivas/versiones/target siguen pendientes, no BUILD suite general. [ES, fuente de autores](https://arxiv.org/abs/cond-mat/0105191) sustenta la distinción de definición en distribuciones discretas; no valida nuestro tamaño de muestra ni porcentajes.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](../decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.

## Avance técnico posterior — wave07

[R-020_evaluation_contract_RC5.md](R-020_evaluation_contract_RC5.md) especifica propuestas/gates, no método/dataset/Strategy admitidos. M1 aprobado/ADR019; Q059 guardrails distintas propuestas. E5/E6screens no statisticalacceptance, costos/scale/fuente/financialtarget pendientes. Versiones anteriores conservadas; no benchmark/margen cambiados por resultados.

## Vigencia G-R1 — ADR-020, 2026-10-15

[ADR-020](../decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md): Q-059/G-R1 DECIDED en preferencia económica ex ante: no deterioro de DD frente a EW6-BH completo ni de volatilidad diaria frente al espejo K2 admisible. ES95/M1 primario y NI/cash/K2 conjuntos; recuperación/underwater/pérdidas/gaps/slippage/extremos obligatorios. DD exige estimando/horizonte/path/incertidumbre y aplicabilidad válidos; una trayectoria/bootstrap genérico no demuestra futuro. Volatilidad incluye upside/downside. Guardrails relativas no son límites absolutos Risk D-031. G-R2 no aprobado ni fallback. Estados separados y NO_STRATEGY_QUALIFIED; ningún método/dato/broker/Strategy/F0/implementación aceptado. Continuar P0/P1 financieros en checkpoints agrupados; holdout UNKNOWN/lock/targetdeferral.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](R-020_preregistration_readiness_RC6.md), [configEQ3](R-020_configuration_completion_RC1.md), [DataCards](R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](R-007_protection_dependency_contract_RC2.md), [RiskRC2](R-027_risk_formula_spec_RC2.md) y [engine/QE0](R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.
