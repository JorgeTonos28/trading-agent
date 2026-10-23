# R-020 — alternativas de reglas y demanda financiera — RC1

2026-10-13 · P0 D-008/D-010/D-011 RESEARCHING. **Strategy V1 Selection OPEN**, parámetros/configuración no aprobados, no backtest ni código operativo. Video primero; MATR benchmark. Estas alternativas son diseño propio: no atribuir al video entradas/reglas que no publicó. [Cards originales](R-020_video_candidate_rule_cards_RC0.md) y [demanda](R-020_candidate_data_workload_contract_RC1.md).

## 1. Separación de candidatos

| Variante de investigación | Entrada determinística propuesta | Fuente indispensable | Salida/posición a comparar | Admisión actual |
|---|---|---|---|---|
| VID-CONG-EOD | Nueva compra pública de actor en lista ex ante, activo elegible y documento único; una transición por evento, nunca por transaction_date | Congreso histórico con revisión/canal/disponibilidad y mapping de instrumento | Stop inicial y ratchet; salida temporal o evento público de venta del mismo actor, semántica a preregistrar | CONDITIONAL: clocks/rights/history sin demostrar; no elegir actor por ganancias |
| VID-F4-EOD | Compra no derivada admisible de insider; clasificador determinístico desde código/ownership/footnotes/plan y fecha utilizable; deduplicación por documento/transacción | Form4/4-A, issuer/security mapping y disponibilidad por canal | Módulo de posición compartido; exits por protección o plazo, no inferir venta de insider como orden automática | CONDITIONAL: P no demuestra por sí solo compra en exchange; no completar contexto con LLM |
| VID-13F-REBAL | Cambio observable de holdings entre informes comparables publicados, de gestor/lista ex ante; rebalance por nueva publicación | 13F histórico, versiones/completeness/confidential release y CUSIP as-of | Target exposure por regla explícita, horizonte más lento; no simular compra del gestor en quarter-end | CONDITIONAL: missing holding no equivale siempre a venta; coste/mapping/clock abiertos |
| VID-PRICE-ENTRY | Close(t) supera máximo de N cierres previos (sin t), universo/lista ex ante; señal solo después de barra disponible | Precios/corporate actions/calendario as-of; N y universo todavía OPEN | Ratchet separado de entry; comparar control sin ladder con ladder condicionado | NUEVO candidato del proyecto, no reconstrucción literal; sin selección ni resultado |
| MATR_V1 | SMA200/ROC126/ranking del baseline, semánticas M-01–11 | Precios diarios desde propuesta2005/warm-up, raw/ajustes as-of | ATR/eligibilidad/rebalance bajo ficha candidata | Candidato/benchmark, ninguna preferencia automática |

VID-ALERT conserva CONDITIONAL a acceso/historia/rights y reglas; wheel fuera PAPER actual. Form4, Congreso y 13F no son equivalentes ni necesariamente combinables. Options activity/blocks/revisions/flows conservan investigación por familia; no exigirlos a todas las variantes. La lista no añade estrategias al Champion sin decisión humana.

## 2. Contrato común propuesto del módulo de posición inspirado en video

Entrada `e` = fill reconciliado real; precio de referencia raw `p0`, cantidad reconciliada `q`, protección confirmada `s0`, calendario/snapshot/versiones. Sizing pasa exclusivamente por Risk/Execution. Cada parámetro es campo obligatorio de CandidateConfig; NULL/UNKNOWN impide admisión, no defaults elegidos por modelo.

**OPEN obligatorio antes de freeze:** unidad de episodio/lote vs posición agregada y reglas de actualización de p0/H/q/stop/contador ante parciales, top-ups y corporate actions. Split conocido as-of requiere rebase coherente de todos los precios y cantidad inversa antes de comparar; no unir raw pre/post-split ni disparar ratchet por discontinuidad contable. Un top-up no hereda implícitamente el high-water de una cantidad que aún no existía. Config debe resolver ownership/entry promedio/episode reset y mapeo broker de protección; cada alternativa cuenta como variante, no parámetro inferido por LLM.

- **Ratchet porcentual escalonado:** activación `H >= p0*(1+a)`; H es máximo de observaciones permitidas desde e, incluyendo solo datos ya disponibles. Para pasos relativos, `k=floor(log(H/[p0*(1+a)])/log(1+h))` y ancla `A_k=p0*(1+a)*(1+h)^k`; stop deseado `max(s_anterior,A_k*(1-b))`. a/h/b, precisión y frecuencia OPEN; h>0, 0<b<1. Variante continua distinta `max(s_anterior,H*(1-b))`; no mezclar resultados ni escoger retrospectivamente.
- **Ejecución:** stop deseado no es stop broker confirmado. Ratchet solo después de admitir dato y regla y confirmar reemplazo autorizado; un intento no baja protección ni cancela primero por defecto. Protección durante parciales/reemplazo/rechazo exige broker-specific contract y ruta PROTECT/replace normal autorizada por RiskDecision; cualquier excepción que cancele protección requiere regla específica documentada, probada y aprobada por owner. **G2 solo cancela entradas pendientes verificadas**, no autoriza reemplazar/cancelar protección. Sin mecanismo seguro demostrable, variante no admitida.
- **Escalones de compra en caída:** variante separada, con referencia anclada/contador/cap/reservas y gate de protección. Si stop se cruzó o salida/cancelación/posición UNKNOWN, no añadir. Tras salida confirmada, una nueva entrada necesita nueva señal, no reutilizar episodio. Aumentar exposición de un perdedor sigue propuesta pendiente; no tomar el -20% del video como permiso.
- **Precedencia propuesta:** incidente/reconciliación → protección/salida vigente → cancelación/reemplazo verificado → entrada/add permitido. No compensar salida pendiente con compra simultánea, ni contar cash esperado antes de fill/reconciliación.
- **Time exit:** H_hold en sesiones desde fill; versión/cutoff/holiday rule y siguiente oportunidad de ejecución explícitos. Venta de tercero, pérdida de señal, trailing y time exit son razones distintas; una sola transición reconciliada. Precios de gap/fill no se fuerzan al stop.

## 3. Campos que realmente faltan antes de selección/freeze

Cada config exige: universo as-of, entrada/filtros/tie-break, actor/lista y exclusiones, cutoffs/clocks/missing, cadence/calendario, expiración/señal/reentrada, N/a/h/b/H_hold/ATR si aplica, policy sizing D-035/031, lotes/redondeo, orden/protección/cancel-partial, costes/dividendos/cash, benchmarks y protocolo OOS. Ningún candidato está listo para ejecutar mientras faltan estos valores o datos admitidos. Estas reglas reducen ambigüedad y permiten comparar demandas; no convierten una ficha paramétrica en una estrategia congelada.

**Recomendación de investigación autónoma:** comprobar primero Form4 y Congreso como señales del enfoque video; contrastar VID-PRICE-ENTRY como entrada propia separada y MATR benchmark. Priorizar clocks/normalización/rights antes de abrir rendimiento, no aprobar Smart Money por amplitud del proveedor ni declarar alpha de un patrón por intuitivo.

## 4. Workload hacia contratos transversales

EOD evento/publicación, datos por sesión y protección siempre supervisada localmente; no hay dependencia LLM financiera por estas propuestas. Jobs agénticos research/quant/shadow/ped tienen snapshots/roles ADR-014, cadencias por confirmar tras estrategia. Count events/positions/orders/revisions y bursts antes de D-025/026/028. Shadow compara oportunidad y trayectoria bajo clocks/costes comunes; ni propuesta atrasada ni blinding contaminado entra como contemporánea. Pedagogía explica hechos y alternativas, no recomendación ejecutable.

## Fuentes y límites

Video aporta módulo/narrativa; nuevas entradas/ratchet son propuestas nuestras. [SEC códigos Form4](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69) distingue P/A/F/M/G; [13F FAQ](https://www.sec.gov/rules-regulations/staff-guidance/frequently-asked-questions-about-form-13f) trata holdings, clases y confidential treatment. [Admisión de datos RC1](R-021_external_dataset_admission_RC1.md) y [órdenes](R-007_order_protection_matrix_RC1.md) documentan limits. No conclusiones de retorno, ningún dataset histórico ni holdout consultados.

## Aprobación vigente R2 — ADR-015, 2026-10-13

Owner aprueba R2 conceptual y acotado; R1/P&L/controles independientes conservados. Menor R2 no autoriza ampliar perdedoras: señal/regla Champion, nueva evaluación integral y reservas reconciliadas obligatorias. p_auth pending/new y protección condicional conservados. Missing/invalid/unconfirmed/crossed stop sin fill verificado => UNCERTAIN, nunca riesgo0. Costes/pérdidas/claims sin doble conteo ni exposición oculta; casos ganancias/pérdidas/partial/top-up/gap/rapid-move R-027 RC1. Q-054 DECIDED, **D-035 global RESEARCHING**, fórmulas/params/pruebas siguen abiertas. Sin selección Strategy/broker, implementación, gasto o target acceptance. [ADR-015](../decisions/ADR-015-remaining-risk-reference-R2.md).

## Aprobación vigente O-B — 2026-10-14

[ADR-016](../decisions/ADR-016-strategy-evaluation-O-B.md) registra Q055 DECIDED conceptual; D011 global RESEARCHING, Strategy OPEN. Reserva PROPOSED_RESERVE/INTEGRITY_UNKNOWN hasta exposure ledger/M11; alternativa prospectiva con gobierno si contaminada. Ensayos incluidos descartes, suficiencia/INSUFFICIENT_EVIDENCE, comparabilidad, walk-forward/sensibilidad/costes/retrasos y horizonte/latencia/caducidad quedan exigidos antes de resultados. Ningún modelo/umbral/estrategia/broker/data aprobado; lock y target deferral vigentes. Continúa paquete financiero sin solicitar Plus/admin ni investigación agéntica general.

## Evaluación comparable wave04 — 2026-10-14

[ScorecardRC2](R-020_comparable_candidate_scorecard_RC2.md), [evalRC2](R-020_evaluation_protocol_RC2.md) y [horizon](R-020_decision_horizon_latency_RC0.md) añaden fichas/precondiciones/registry/freshness; no Configs aprobados ni preregistro sellado. [Exposureledger](exposure_ledger.md) parcial conserva integridad UNKNOWN, sin apertura de reserva. [Q056](D-011_economic_endpoint_decision_RC0.md) requiere preferencia económica antes de completar efecto/muestra;19/19sintéticos no evidencia de rentabilidad/operación.
