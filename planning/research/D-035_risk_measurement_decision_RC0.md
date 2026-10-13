# D-035 / Q-054 — referencia de riesgo y capacidad reservada — propuesta RC0

2026-10-13 · Propuesta original conservada; **Q-054/R2 referencia conceptual DECIDED por owner en ADR-015**, D-035 global RESEARCHING. Números D-031 abiertos; sin implementación ni ampliación G1+G2. [Candidatos](R-020_candidate_rules_RC1.md) necesitan definición común de sizing/riesgo antes de freeze. [Revisión independiente](R-020_027_independent_review_2026-10-13.md) permitió presentar el scope, no cierra D-035 completo. Alternativas/comparación siguientes son antecedente; condiciones vigentes al final y en ADR-015.

## 1. Decisión concreta

¿Usar como presupuesto de **riesgo restante hasta protección** la pérdida desde marcas actuales verificadas de equity (opción R2), conservando entry-to-stop como análisis de capital/atribución, o usar R1/R3?

| Opción | Medida para posiciones long existentes | Ventaja | Trade-off |
|---|---|---|---|
| R1 entry-to-stop | `q*max(entry-stop,0)` | Riesgo del capital original interpretable | Stop por encima de entrada produce0 aunque se puedan perder ganancias actuales. No mide drawdown futuro desde equity actual |
| **R2 current-equity-to-protection, recomendado** | `q*max(mark-stop_confirmed,0)` con marcas frescas y protección válida | Consistente con presupuesto aplicado a equity actual; conserva riesgo restante de ganancias y evita doble contar pérdida ya reflejada | Requiere marca/feed/FX/session y protección verificables; cantidad admisible puede variar con mark sin modificar stop. No garantiza pérdida máxima |
| R3 ambos presupuestos independientes | Control R1 y R2 con presupuestos separados y límite más restrictivo | Permite gobernar capital inicial y equity restante | Dos presupuestos/parametrización, mayor complejidad; valores no aprobados, no asumir que siempre equivale a R2 |

Ejemplo **ficticio**, no riesgo aprobado: entry100, mark120, stop110, q10. R1=0; R2=100 USD de pérdida estimada desde equity actual al stop. Con entry100/mark90/stop80/q10: R1=200, R2=100; la pérdida actual ya está en equity. R2 puede ser **menos restrictivo que R1 en posiciones perdedoras**, por eso exige decisión humana y no se llama simple aclaración documental. Stop execution puede perder más por gaps/slippage; escenarios independientes siguen obligatorios.

## 2. Especificación técnica propuesta bajo R2

Scope inicial USD, equities/ETF long-only cash, sin offsets de shorts/leverage/derivados ni crédito por correlación/hedges. Divisas/monedas distintas no se presumen USD; valor/FX UNKNOWN en control obligatorio deniega nueva exposición. Ejecución fraccionaria/lote todavía D-021/030, nunca round-up para alcanzar orden mínima.

`S` = snapshot financiero reconciliado/versionado; `E` equity marcado coherente. `C_base` = cash confirmado elegible para gasto bajo settlement/cash-account policy, antes de claims de entradas no llenas. `C_free=C_base-sum(cash_claims_exclusivos)-buffer_aprobado`, sin volver a descontar cantidades ya debitadas por fills. Buying power/free cash broker es control adicional coherente, no se suma como dinero extra ni se descontará una segunda vez la misma retención. Campos broker→base/debit/hold deben reconciliarse D-021/026/030; mapping UNKNOWN deniega. Estado incoherente o E<=0 => nuevas entradas bloqueadas y acción G1/G2/runbook aplicable, no liquidación general.

Ownership económico exclusivo por lote/intento: posiciones llenas + remainder de entradas vivas + reserva de autorización todavía no representada por entrada; no sumar una misma cantidad bajo dos objetos. Cambio reservation→order→partial fill transfiere cobertura atómicamente/reconciliable. Una salida/cancelación pendiente no reduce posición ni libera presupuesto/cash hasta evento cierto. Cancel requested ≠ cancel confirmed; no reemplazar IDs para ocultar riesgo.

**Revalidación con reserva propia:** para autorización aún no despachada, el control calcula la proyección excluyendo **solo su claim exclusivo** del conjunto de encumbrances, evalúa el candidato una vez y compara/reemplaza ese claim atómicamente con estado/generación/snapshot actuales. No se libera globalmente el claim durante el cálculo ni se ofrece a otro intent. Cash/stop/gap/exposure siguen la misma exclusividad. Si tiene orden broker viva ya representada, no se excluye como autorización nueva ni se vuelve a enviar; cambios pasan lifecycle/reconciliación D-013. Revalidación fallida no borra claim incierto; rechazo/liberación exige estado comprobado. Fixture aritmético: C_base100, otros claims60, claim propio20 => free20, capacidad de prueba excluyendo propio40. Candidate cost32 permite replacement20→32, totalclaims92/free8; comparar32 con free20 sin devolver solo propio lo cargaría dos veces. No prueba de transacción/concurrencia.

Para cantidad adicional `q_new`, cada control evalúa el **estado posterior propuesto** incluyendo reservas/remainders; top-ups cuentan la posición existente, no solo el nuevo lote. Controles separados:

1. Exposición: notional posterior por activo/estrategia/portfolio con precio conservador de autorización; pesos/caps abiertos.
2. Cash: `q_new*p_auth + fees_fixed + costs_variable(q_new) <= C_free`; venta pendiente no financia compra. Unknown costos requeridos no cero.
3. Protección estimada: para **posición llena existente**, `q_filled*max(mark_actual-stop_confirmed,0)` más coste de salida contado una sola vez; validación de quote/protection/session/qty precede cálculo. Para **remainder de entrada y nueva autorización**, la referencia única es `p_auth` conservador versionado (precio superior de valoración de entrada según quote/orden/escenario), nunca precio histórico de insider/entry del primer lote ni la marca actual favorable. `q_remaining*max(p_auth-stop_planned,0)` más costes de ese lote, únicamente si el mapeo de protección condicional/partial/activation ha sido documentado y probado en broker. Se registra CONDITIONAL_PROTECTION_ESTIMATE, nunca CONFIRMED. Sin ese contrato no se admite nueva entrada. Tras fill se migra a mark/protección reales; fallo va G1+G2 y runbook, sin liquidación automática. `p_auth` no garantiza el precio de mercado: gap/slippage independientes y revalidación siguen obligatorios. Stop futuro en intent no confirma protección existente; protección no válida/crossed/quantity mismatch => control no evaluable, riesgo UNKNOWN/unprotected, jamás0. Costes no duplicados entre distancia/slip/precio y término separado.
4. Gap/slippage: escenarios versionados sobre toda la cartera/reservas, mark-to-scenario + coste liquidez/ejecución coherente. No asumir independencia favorable ni que stop acota gap; evitar doble sumar el mismo slip en precio y coste. Presupuestos/escenarios numéricos pendientes D-031.
5. Liquidez: participación/spread/quote/tradability y feed/cobertura requeridos. Volumen IEX no prueba volumen consolidado; bounds/cadence/costos no seleccionados. Capacity UNKNOWN bloquea nuevas entradas dependientes.

Para controles monotónicos se calculan `q_j_max` admisibles; `q_authorized=floor_to_lot(min(q_requested,q_exposure,q_cash,q_protection,q_gap,q_liquidity))`. Revalidar **todos** los predicados después de redondeo, costes fijos/cambios de estado y antes de reservar/emisión. Controles no monotónicos necesitan enumeración/búsqueda limitada justificada y feasible intersection, no dividir presupuesto por distancia usando un algoritmo no demostrado. Sin solución/certificado coherente => rechazar; no resolver mediante LLM ni aumentar cantidad.

Idempotencia/reservas/estado/audit transaccionales siguen ADR-003 y D-026: modelo no opera ledger ni reevalúa aprobación. Bloqueo material/resume humano/G3 no autorizado conservados. Fórmula no promete financieros exactamente-once; recovery/reconciliation explícitos.

## 3. Evidencia y alcance

[Probe algebraico](probes/r027-risk-algebra/README.md) utiliza Decimal y números ficticios para contrastar referencias, reservas y constraints; no simula mercados/backtest/engine/broker ni valida Risk Engine. Paridad implementación futura, concurrencia/crash/powerloss/corporateactions/feeds reales permanecen tests financieros, no R-006. [Risk baseline](../03_risk_policy_RC1.md), [ADR-006](../decisions/ADR-006-composite-risk-architecture.md) y [broker matrix](R-007_order_protection_matrix_RC1.md).

## 4. Alcance de una eventual aprobación

Solo referencia R2 para riesgo remanente y contrato algebraico/reservas; ninguna cifra/gap/percent/límite, broker, engine, Strategy V1, código, PAPER o LIVE aprobado. Entry analytics se conservan, loss/drawdown caps se definen aparte y se evita contarlos dos veces. D-035 no se declara DECIDED sin owner y revisión; parámetros/pruebas siguen abiertos por scope. Cambiar estrategia/risk sin esta decisión alteraría sizing, por lo que éste es el próximo gobierno material; demás investigación independiente se completa antes de presentar.

## Aprobación vigente R2 — ADR-015, 2026-10-13

Owner aprueba R2 conceptual y acotado; R1/P&L/controles independientes conservados. Menor R2 no autoriza ampliar perdedoras: señal/regla Champion, nueva evaluación integral y reservas reconciliadas obligatorias. p_auth pending/new y protección condicional conservados. Missing/invalid/unconfirmed/crossed stop sin fill verificado => UNCERTAIN, nunca riesgo0. Costes/pérdidas/claims sin doble conteo ni exposición oculta; casos ganancias/pérdidas/partial/top-up/gap/rapid-move R-027 RC1. Q-054 DECIDED, **D-035 global RESEARCHING**, fórmulas/params/pruebas siguen abiertas. Sin selección Strategy/broker, implementación, gasto o target acceptance. [ADR-015](../decisions/ADR-015-remaining-risk-reference-R2.md).
