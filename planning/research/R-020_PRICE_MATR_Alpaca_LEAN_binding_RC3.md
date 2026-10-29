# PRICE–MATR — bindings Alpaca/LEAN/Risk RC3

2026-10-28. RULES_SPECIFIED / FINANCIAL_BINDINGS_PARTIAL. Complementa EQ3 y RC2 sin modificar bytes de [config RC1](candidate_configs/PRICE_MATR_rules_RC1.json), doce declaraciones o cero trials. No selección de Strategy V1 ni implementación.

## Mapa por etapa y contrato

| Etapa | Binding determinable | Estado pendiente |
|---|---|---|
| Universo/indicadores | Seis ETF, IDs históricos, split-only as-of para precio/SMA/ROC/ATR; breakout excluye t; Wilder/empates/weekly eligibility RC2 | Source/calendar/actions admitidos. GLD warmup propio, sin proxy ni preinception fabricado |
| Clocks | Bar completo, exchange zone→UTC, known/receipt/cutoff y snapshot; DailyPreciseEndTime explícito en LEAN | Sesiones/DST/early close, reloj proveedor y lag real; fila daily fechada no es timestamp de disponibilidad |
| Signal/NAV/target | Señal determinística desde snapshot admitido; targetNAVsignal/3, whole qty/floor usando p_auth; no top-up ni cash redistribuido | Política de ejecución/cash y valores aprobados de freshness/cap/reservas |
| Entry propuesta OP-L1 | Marketable limit RTH/DAY con qty entera y cap explícito; p_auth igual al límite contractual, quote/as-of validado. Tick de compra conservador sin exceder presupuesto | Es **propuesta de realización**, no política aprobada ni nueva variante ejecutada. Parámetro de desviación/cap, expiry/cancel y quote source se fijan antes de F0. Market no hereda esa cota |
| Risk | Controles independientes RC3/R2, input UNKNOWN=no autorización; reservas de filled/remainder/no-sent exclusivas | Perfil D-031, modelos/cash/solver y transacción aceptados |
| Initial protection | Regla p0 de fills reconciliados−3ATR del snapshot, rebase de parcial y seal; desired≠confirmado | [B3 RC5](R-007_Alpaca_protection_reconciliation_RC5.md). Child pre-fill no prueba esta regla; sin ruta admisible no entrada |
| PRICE ratchet | Geometría10/5/5 y comparador decimal/racional; HWM post-seal, sin high de barra de fill | Actualización protectora efectiva/tick/replace sin ventana inventada; no trailing nativo equivalente por etiqueta |
| MATR | Elegibilidad diaria, ranking semanal top3; supervivientes sin repesar/ampliar; salida/stop según RC2 | Semántica de orden de salida que no debilite protector, cash elegible y reasignación tras fill/settlement |
| Contabilidad | Libro raw con splits, receivable/pago/costes; OHLC y volumen en unidades consistentes | Dividendos/paydates/actions/rates/fees; import y modelos LEAN adaptados |
| Evaluación | Mismos períodos/admisión/benchmarks/costes/métodos y cinco escalas; latencia/expiry modeladas | D-011, F0, M-11 y selección humana; ningún resultado histórico en esta fase |

OP-L1 concreta una forma ejecutable conservadora de p_auth, pero no se introduce como cambio aprobado de estrategia. El manifiesto F0 debe fijar exactamente qué configuración/alternativas se admiten; una alternativa que influya en selección entra en la familia/registro de pruebas, sin reparaciones postresultado.

## Event ordering y paridad

Actualizar acciones efectivas/unidades y estado broker antes de decidir desde un snapshot que las usa; conservar clocks de conocimiento. Los fills/ejecuciones y datos que llegan tras cutoff no alteran la decisión vieja. Una señal al cierre no compra retrospectivamente ese mismo cierre ni conoce el open siguiente para autorizar sizing.

Precedencia healthy: reconciliar estado y protecciones, salidas, después entradas con slots/cash elegibles. Incertidumbre material prevalece G1+G2; no es HOLD de un agente. La secuencia de eventos simultáneos necesita orden causal de fuente; un tie-break interno reproducible no prueba el orden real del mercado.

OHLC diario no identifica si high/ratchet ocurrió antes que low/stop. Si esa ambigüedad afecta fill/P&L, usar granularidad admisible o un protocolo de cotas/escenarios preregistrado; no seleccionar trayectoria favorable ni llamarla ejecución real. EOD puede bastar para señales y ser insuficiente para calificación de stops/gaps/parciales/espejo K2. El plan29.99 no demuestra por sí solo granularidad suficiente o quotes ejecutables.

Contrato de trace comparado: inputs/hash/cutoff y transform; señal/target; candidato intent/reservas/Risk verdict; command/parent/legs; ack/fill/replace/cancel/fees; posición/cash/receivable/mark; P&L y métricas. Explicar cada diferencia causal; tolerancias por unidad/tick/evento se fijan antes de resultados. No convertir defaults de LEAN o simulador Alpaca en oráculo universal.

## Estado de admisión y trabajo pendiente

No CONFIG_ADMITTED_FOR_RESEARCH ni F0. Las reglas indicadoras están especificadas; todavía faltan protección B3 y orden/cash/inputs/riesgo/método completos. No se ocultan como sólo R-030: el diseño de mapping se completa en Preparation, la evidencia de cuenta/host en target y la paridad integrada después de implementar. Form4 continúa investigación separada; no obliga All-in-One ni se agrega a estos dos candidatos.

## Binding posterior — 2026-10-29

[RiskRC5](R-027_parameter_and_binding_contract_RC5.md), [Q064](R-007_B3_route_and_policy_decision_RC0.md) y [lifecyclePG](R-011_bounded_lifecycle_and_PostgreSQL_contract_RC1.md) concretan redondeo/raw/ATR/as-of, cantidades alcanzables durante protección y dispatch durable. OP-L1/PF y números siguen propuestas. JSON/hash de las12hipótesis no se modifican para aparentar configuración admitida. No órdenes directas de LEAN/C/LLM, no bar high previo al seal ni cap market ficticio.
