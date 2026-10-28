# Riesgo — caps, inputs y parámetros RC4

2026-10-28. Extiende [RC3](R-027_risk_formula_spec_RC3.md), ADR-006/015; **sin cambio de política o umbral aprobado**. D-035 parent RESEARCHING. Cierre técnico D035-T2 limitado a precondiciones del solver/caps, no Risk Engine ni solver real aceptado.

## Modelo afín en que min-caps es defendible

Éste es un modelo de gasto **incremental** de un nuevo tramo respecto de cartera/obligaciones base Y0 fijas. El control total H_j(Y0,q)=H_j(Y0,0)+g_j(q), y B_j es presupuesto restante: límite aprobado menos H_j(Y0,0), no el límite íntegro ignorando exposición previa. Costes conjuntos y obligaciones existentes deben estar correctamente particionados antes de esa resta.

Para una cantidad entera q, cada restricción incremental j es g_j(0)=0 y g_j(q)=a_j q+b_j para q>0, con a_j>0, b_j≥0 y presupuesto fijo B_j≥0 en el snapshot. Entonces cap_j=max(0,floor((B_j−b_j)/a_j)), limitado al lote/target; q*=min(target,caps). Es consecuencia de monotonía/separabilidad bajo esas hipótesis, no un algoritmo general para costes/gaps/mercados. Cantidad cero no valida un input inválido ni paga fee de orden inexistente.

Requisitos: todos los controles aplicables y unidades conocidos, target de Strategy, grid/lotes factibles, presupuestos/denominador NAV definidos, reserva y coste conjunto reconciliados. B negativo, a desconocido, protección no admisible o snapshot inválido significan no autorización positiva/UNCERTAIN, no cap0 «aprobado». Restricción con a=0 necesita su tratamiento lógico separado. Con costes discontinuos/no monótonos, ratios NAV dependientes de q, diversificación/escenarios conjuntos o interacciones de órdenes, probar propiedades o evaluar conjunto factible con un solver adecuado. No aplicar búsqueda binaria por conveniencia.

[R4](probes/r027-cap-and-cost-boundaries/README.md) contrastó900 celdas monótonas frente a enumeración exhaustiva, sin discrepancias;11 expectativas de las cuales9 calculadas y2 marcadores declarativos. Contraejemplo no monótono preservado. No calibra riesgo, fills, precios, modelo de escenarios, solver general o transacciones. R3 conserva su evidencia de cantidades/claims; no se repite.

## Binding de inputs

| Input | Requisito determinable | Sin evidencia |
|---|---|---|
| p_auth | Cota contractual si limit, misma moneda/unidades, quote/conservadurismo/freshness versionados | Market no obtiene fill cap porque se haya calculado p_auth; OP-L1 sigue propuesta |
| m/s/q | Mark fresco y protector válido/confirmado de qty en unidades raw | Cobertura parcial/crossed/unknown→R2 agregado UNCERTAIN, no cero |
| Cash | Saldo base, débitos reflejados/en tránsito, holds, settlement, fees y reservas exclusivas | No margin buying_power ni dividendo de modelo como cash real |
| Costes | Entrada/plan de salida conjunta, fijos/variables/redondeo y costes ya pagados distintos | No fee fijo por cada partición ni coste pagado otra vez |
| Gaps/liquidez | Scenarios de cartera correlacionados y disponibilidad/volumen en unidades históricas | No sumar mark→stop otra vez a pérdida íntegra mark→gap; no asumir independencia de ETF |
| Commit | Snapshot/version/epoch vigentes y compare-and-commit durable antes de dispatch | Race/ack/timeout no libera reserva; dos órdenes vivas no comparten una reserva por presunto replace atómico |

## Registro de parámetros que aún requieren cierre

| Familia | Parámetros pendientes | Gobierno y evidencia |
|---|---|---|
| D-031 riesgo absoluto | Pérdidas/drawdown, exposición, riesgo restante y reservas, concentración | Preferencia del propietario + evidencia/escenarios. M1/G-R1 relativos no los sustituyen |
| Protección | Ventana/alerta/acciones autorizadas, qty/minimum effective coverage, renovación/expiry | Política material específica y B3; no emergencia implícita ni G3 |
| Calidad de input | Freshness/skew/staleness, quote spread/cap y señal expiry | Contrato de fuente/ruta, horizonte y sensibilidad económica antes de F0 |
| Escenarios | Gap/slippage/impacto, liquidez/participación, correlación y costes | Datos/escenarios defendibles; números ficticios de probes no son calibración |
| Operación | Retry/deadline/backpressure/RPO/RTO | Núcleo y ledger reales, broker/target; fallo de agente no acción financiera alternativa |

No restaurar0.5%/25% del borrador como valores aprobados. Sin fuentes/ruta protectora/perfil defendible no hay propuesta numérica madura de D-031; conservar campos pendientes en vez de inventar precisión. Reducir R2 no permite top-up; EQ3 no lo contempla. Ganadora/perdedora/partial/top-up rechazado/gap/rápido adverso siguen casos obligatorios de aceptación.
