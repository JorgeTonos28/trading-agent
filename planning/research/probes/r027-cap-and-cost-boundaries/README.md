# R4 — caps de autorización y costes conjuntos

Protocolo previo 2026-10-28. Experimento desechable con Decimal y cantidades finitas; no Risk Engine productivo ni parámetros operativos aprobados. Sin datos, cuentas, órdenes, performance o backtest.

Comparar enumeración exhaustiva independiente con caps cerrados sólo en un modelo explícitamente monótono: límite de gasto con fee fijo/variable, target, exposición, reserva hasta stop y escenarios. Cantidad cero no paga fee. Riesgo de entradas usa p_auth cap de limit, no el mark favorable. Para órdenes market, p_auth no garantiza cap y el caso se rechaza como prueba de cota. Añadir costes no monótonos como negativo donde min-caps/búsqueda binaria no se justifican.

Verificar cantidades filled/remainder/no-sent disjuntas, cash debitado/no reflejado y fee conjunto; top-ups no permitidos por menor R2; split conserva q(m−s) sólo algebraicamente. Límites, shocks y fees ficticios sirven para probar fórmulas, nunca se promueven a D-031. PASS no valida solver general, transacciones, broker, p_auth o modelo de escenarios reales.

Resultado01:900 celdas monótonas sin discrepancia frente a enumeración;11 expectativas PASS,9 calculadas y2 marcadores declarativos. No perfiles/solver real/política/transactions aceptados.
