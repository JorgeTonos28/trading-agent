# K2 — benchmark book reproducible RC0

2026-10-14. ADR-018 aprueba el paquete; este book especifica su realización candidata. No dataset admitido, parámetros de broker, capital o benchmark ejecutado. F0 permanece incompleto. Las políticas que dependan de fuentes/broker se cierran con su evidencia antes del freeze, nunca después de resultados.

## Identidad y fase

Manifest por ejecución: ID/versión/hash del book, source commit, security IDs históricos, universo, calendario/zona, ventana, warm-up, valores iniciales, política de cash/costes/dividendos/corporate actions, marks y relojes de disponibilidad. SPY/QQQ/IWM/EFA/TLT/GLD son la cohorte fija aprobada, no selección ex post de fondos supervivientes. No extender resultados a selección universal de acciones o fondos. Inception, mapeo y cobertura se admiten individualmente.

Comparación propuesta2019–2022 con cuatro subperíodos calendarios: mismo ledger continuo, sin restablecer pesos/cash/posiciones al inicio de cada año. Warm-up sólo para indicadores, sin P&L scored. Estado inicial fresh versus carry desde desarrollo debe estar fijado en CandidateConfig y matched a la fase; no elegir la convención favorable después. Confirmación tendrá manifest propio, mismo protocolo congelado y reserva sólo si M-11 acredita integridad.

## B-EW6-BH

1. Equity inicial simbólico K, misma base unitizada que los candidatos; no selección del capital real. Targets iniciales1/6 de exposición por ETF. Fricciones/rounding pueden producir pesos realizados distintos: registrar target, realizado y residual, sin llamarlos equal-weight exactos. Política candidata: reservar costes iniciales/cash, asignar iguales importes de inversión elegible y resolver quantity/price según regla de autorización; no seis presupuestos iguales incluyendo fees heterogéneos que ocultan pesos netos diferentes. Cantidades fraccionarias analíticas y redondeo factible del broker son escenarios distintos y versionados; no atribuir permiso de fractions a un broker aún no elegido.
2. Manifest de decisión conocido antes del evento inicial. Ejecución en primera oportunidad común permitida, con precios/fills/fricciones admisibles; próximo-open y MOO no se confunden. No ajustar cantidades usando un open futuro que no era conocido al enviar orden; presupuesto/notional fijo o regla de precio conservador y residual explícitos.
3. Después no vender/rebalancear por cambio de pesos, año, régimen o señal de candidata. Peso w_i(t)=qty_i*mark_i/NAV, deriva naturalmente. Cash/receivables son componentes separados; no normalizar pesos de activos a100% y ocultar cash.
4. Dividendos: derecho y receivable desde evento ex conforme a qty elegible/as-of; disponible sólo al pago/settlement confirmado. **Propuesta principal:** reinvertir únicamente en el fondo que pagó, en la siguiente oportunidad autorizada tras disponibilidad, con costes y rounding propios; no repartir entre seis ni restaurar pesos. Si fuente no informa pay-date fiable, estado NOT_ADMITTED para esa realización; total-return teórico/ex-date es sensibilidad explícita, no alias de cash realizable.
5. Splits/reverse splits cambian qty y precio coherentemente, sin crear P&L. Cash-in-lieu, spin-off, fusión, cierre o delisting se tratan por política previa y source event; no quitar instrumento/hueco retroactivamente ni reinvertir en ganador sustituto. Acción no resuelta => quarantine/modelo inválido, no precio0 ni retorno favorable imputado.
6. Raw prices + qty + dividend receivable/cash una sola vez para NAV. Precio ya total-return y pago extra es doble cómputo. Serie ajustada puede servir a indicadores sólo mediante transform as-of aceptado; no aporta fills o disponibilidad de dividendos.
7. Valoración común de fin de sesión y marks de eventos; registrar stale/missing/halts y uncertainty, no forward-fill indefinido oculto. Fricciones/spread/fees/rounding/impuestos incluidos o excluidos con scope idéntico y claro. Rentabilidad neta antes de impuestos personales desconocidos, no afirmar after-tax. Cash usa política real aplicable, nunca yield proxy regalado a la cuenta.

## B-CASH

Hurdle separado del cash contable. Elegir referencia monetaria y modelo con derechos/vintage/availability/calendario/basis/roll/costes; [R008](R-008_cash_benchmark_admission_RC0.md). DGS3MO yield no es retorno total y SOFR no es depósito del propietario. Modelled carry sólo claim modelado con gate explícito, no acceso probado a bills. No seleccionar proxy por cuál haga pasar la estrategia.

## B-EW6-BH-LAMBDA-REAL

Por cada intervalo, λ de exposición larga de S **conocida al inicio**, con qty/marks/NAV reconciliados; claims/reservas no se restan dos veces del NAV. Fuentes stale o λ fuera[0,1] producen input inválido, no clipping silencioso. Espejo asigna λ al basket de pesos naturales B-EW6-BH y resto a cash. Tiene ledger/fills/fees/turnover y delays propios, usando política de interés real con sus propios balances/elegibilidad; no trasladar interés idéntico si depende de umbral de cash.

Fill intraday requiere intervalos y marcas admisibles. Espejo reacciona después de conocer cambio, no antes del fill de S; exactitud ideal y reacción factible son escenarios separados. Con sólo barras/EOD, MATCHED_EXPOSURE_DIAGNOSTIC_LIMITED no prueba eficiencia confirmatoria. λ igual no significa mismos activos, beta, duration, volatilidad o tail risk. No compra/sizing real ni bypass de Risk/Execution.

## Composición, beta y factores

Reportar historia de pesos/NAV/cash y diferencias de composición frente al espejo. Factores diagnósticos predefinidos: equitiesUS/SPY, foreign equities/EFA, duration/TLT, gold/GLD; QQQ/IWM como tilts descriptivos. Son proxies ETF, no factores puros ni FF alpha. Una regresión con intercept y primas coherentes requiere cash/frequency definidos, rango/covarianza y colinealidad diagnosticados.

Diagnóstico ex post sirve a atribución de la evaluación y se etiqueta; ningún beta de toda la muestra dimensiona operaciones históricas. Si se usa estimación previa/rolling para comparador, ventana/lag/missing y modelo se congelan antes y usan sólo pasado. No añadir leverage/shorts o residuales negociables para «igualar» riesgo. No demostrar eficiencia activa sólo porque una mezcla defensiva venció al espejo: claim debe describir riesgo/composición observados. Comparación insuficiente/no defendible => LIMITATION / INSUFFICIENT_EVIDENCE, sin alpha ajustada inventada.

## Referencias secundarias y sensibilidad

- SPY buy-and-hold con mismas políticas contables. Mostrar ΔCAGR neta, terminal wealth, DD/tails y cash premium respecto de SPY, también si K2 pasa y SPY gana. No omitir período desfavorable.
- SPY/SMA200: regla exacta de precio/igualdad/warm-up/ejecución/cash definida en Config antes de resultados; no asumir que toda versión SMA200 sea idéntica a baseline.
- EW6 mensual: manifest independiente, regla de señal/evento/costes explícita, sensibilidad sin reemplazar BH ni escoger benchmark posterior. Si influye en selección, registra ensayo y familia, no «sólo gráfico».

Book no admite datos ni congela modelo estadístico. [E4](R-020_E4_findings_2026-10-14.md) demuestra sólo arithmetic/primitive; broker/engine parity, calendario, fuentes y granulares intraday permanecen gates.

## Coste incremental del sistema

Separar retorno net_trading (fees/spread/slippage/cash/dividendos del ledger financiero) de net_after_incremental_ops (más coste del sistema asignado a S por uso/escala, con calendario/accrual previo). Benchmarks pagan sus propios costes de ejecución/cash, no el mismo overhead de Codex/datos/infra para eliminar oportunidad pasiva. λ procede del NAV financiero reconciliado, no de un equity económico al que se restó gasto externo para inventar leverage. [RC4](R-020_statistical_method_contract_RC4.md) fija streams por gate; no cargos en broker/Risk reales por esta especificación.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](R-020_preregistration_readiness_RC6.md), [configEQ3](R-020_configuration_completion_RC1.md), [DataCards](R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](R-007_protection_dependency_contract_RC2.md), [RiskRC2](R-027_risk_formula_spec_RC2.md) y [engine/QE0](R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.
