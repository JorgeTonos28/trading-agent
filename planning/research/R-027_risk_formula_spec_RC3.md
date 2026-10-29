# D-035 — dominios, recursos y fórmulas RC3

2026-10-23. Corrige RC2 tras crítica independiente. **FORMULA_CONTRACT_SPECIFIED / NOT_IMPLEMENTED**, sin aprobar umbrales, parámetros, broker o Strategy. ADR006/015, A+ y G1+G2 gobiernan; sin G3. D-035 global sigue RESEARCHING por mappings/modelos/solver/durabilidad/aceptación. Números de pruebas son ficticios.

## Tres dimensiones separadas

Por tramo económico a: f_a=posición abierta; l_a=remainder de orden viva; r_a=autorización no representada aún por orden. Estas cantidades son disjuntas **dentro de una agregación económica**, con ID/versión/epoch y mapping de ejecución. El lifecycle (submitted, partial, pending-cancel, terminal) es otra dimensión. El vector de encumbrances cash/exposure/R2/gaps/liquidity enlaza esas cantidades y **puede coexistir con órdenes pendientes**.

Exposición conservadora: E=Σ f_a·m_a + Σ l_a·v_live,a + Σ r_a·p_auth,a. No añadir otra cantidad por su claim. v_live es una valoración conservadora válida para orden viva, no modificación de su autorización ni límite de fill garantizado. p_auth de una market order tampoco es un cap contractual de ejecución.

Cash libre: C_free=C_base−Σ obligaciones_exclusivas_no_representadas_en_C_base−buffer. C_base requiere mapping documentado de débitos, retenciones y settlement: un fill no reflejado conserva obligación hasta estar representado. Dividend receivable, venta no confirmada y settlement no elegible no son cash libre. No descontar dos veces una retención que el campo broker ya restó. Fees pueden limitar controles independientes sin cobrarse dos veces en el mismo book/proyección.

Ejemplo de reconciliación: orden10 a100, cash1000; fill4 deja cash600 y reserva600 para remainder6, free0. La exposición a mark110 es440+600=1040, no1640. Pending-cancel conserva reserva; cancelación confirmada de6 conserva posición4 y libera sólo la obligación extinguida. Si C_base aún1000, mantener400 de débito no reflejado y600 de reserva. Un terminal de orden no borra fills/busts/correcciones.

## R2, pendiente y escenarios

Para cada tramo efectivamente protegido: q≥0, mark fresco m>0, protección confirmada de esa cantidad con 0<s<m, unidades raw/moneda y clocks consistentes.

- R2_filled=Σ q_k·(m_k−s_k)+C_exit_joint_futuro. R1/P&L desde entrada y pérdidas realizadas/no realizadas siguen registros y límites independientes; no restarlos otra vez de R2.
- Cobertura parcial: publicar cantidad cubierta/descubierta y riesgo conocido parcial. Si falta protección confirmada de una cantidad abierta, el agregado dependiente de protección es UNCERTAIN, no sólo suma de la parte cubierta. Stop cruzado, expirado, inválido o no confirmado tampoco representa0.
- Pending/new: R_cond=Σ u_k·(p_auth,k−s_cond,k)+C_entry_exit_futuro_no_pagado, con u≥0 y 0<s_cond<p_auth, regla y mapping admisibles. Es reserva condicional, nunca cobertura actual. Si floor/semántica de protección eventual no son defendibles, control UNKNOWN; no inventar stop conocido antes del fill.
- C_exit_joint es función del futuro plan de órdenes. Particionar lote4+6 no duplica un fee fijo conjunto; cualquier asignación por tramo suma exactamente su coste. Órdenes de salida distintas pueden legítimamente generar costes distintos.
- Para escenario ω: L_ω=NAV_actual−NAV_ω, con cash/fills/posiciones/costes bajo el mismo escenario. Si contiene pérdida íntegra mark→gap, no sumar de nuevo mark→stop. Escenarios correlacionados se evalúan conjuntamente; no diversificación asumida por tener seis ETF.

Exposición, cash, R2, pérdida acumulada/drawdown, liquidez y escenarios mantienen controles independientes. No usar menor R2 como señal de top-up; hipótesis EQ3 no permite adds. Una proyección de escenario no es cota garantizada de pérdida.

## Cantidad autorizable y solver

q* = max {q en lotes válidos: 0≤q≤q_target y cada control aplicable g_j(q,snapshot)≤B_j}. Target lo fija Strategy, no capacidad libre. B o input obligatorio UNKNOWN => UNCERTAIN/no autorización positiva. q=0 no paga fee de orden inexistente ni significa aprobación de input inválido. Conjunto vacío => REJECT con razones.

Sólo usar min de caps o búsqueda binaria cuando se pruebe la estructura/monotonicidad de cada g_j, incluyendo fees, lotes y efectos de mercado. Enumeración finita sirve de oráculo de laboratorio para contrastar un futuro solver, no selección de algoritmo productivo ni promesa de rendimiento. Una función no monótona puede admitir {0,1,3} y binary search devolver1: prueba numérica no generalización a costes reales.

Nueva versión de autorización **no despachada**, mutuamente excluyente de la vieja: conservar encumbrance anterior hasta compare-and-commit; ajustar diferencia exactamente una vez. Dos órdenes simultáneamente vivas no comparten reserva por presumir reemplazo atómico. Cancel/replace usa grafo, fills y qty confirmados. IDs repetidos/epoch viejo/ack perdido requieren consulta/reconciliación, no resend con ID nuevo o liberar por timeout. Durabilidad/concurrencia real D026 sigue pendiente.

## Corporate actions y relojes

Split verificado a=acciones_nuevas/antiguas: q'=a·q; m', s', p_auth' y ATR'=valor/a. Conserva algebraicamente q(m−s). Precio/tick/qty efectiva, fractions/cash-in-lieu, fees y órdenes del broker requieren reconciliación; álgebra no confirma modificación de protección. No comparar stop raw pre-split con mark post-split. Dividendo cash no crea ajuste retroactivo del stop ni cash antes del pago.

## Evidencia y pendientes

[R3 probe](probes/r027-resource-semantics/README.md):21checks aritméticos PASS y66estados finitos de fill/cancel/remainder. No transacción, broker, solver general, Risk Engine, umbral o paridad aceptados. Corrige dos errores conceptuales reales sin política de riesgo nueva; independiente confirma ámbito antes del hito.

Pendientes antes de admisión/configuración: esquema de campos broker/cash, quotes/modelos/freshness y p_auth, floor/ventana de protección, funciones de costes/gaps/liquidez, límites absolutos D031 y perfil de investigación declarado, solver y compare-and-commit especificados/probados; después aceptación target e integración. Lo que afecta diseño no se oculta en P2. Build-vs-Reuse: Decimal, engines, SDK/ledger/storage existentes antes de código propio; Risk del engine no sustituye autoridad financiera aprobada.
