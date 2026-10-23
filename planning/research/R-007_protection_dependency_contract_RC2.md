# Broker/protección — dependencias de cancelación y admisión RC2

2026-10-15. Extensión técnica conservadora de ADR-002/003/006/015; G1+G2, no G3. D021/030 siguen abiertos, ningún broker seleccionado/cuenta/orden probados. **No se añade permiso de cierre/stop de emergencia durante incidente**.

## Grafo de órdenes antes de G2

Clasificar una orden como entrada no es suficiente. Snapshot verificable de parent/children/OCO/OTO, fills/qty/protection state, TIF, active/held y efectos documentados por **API/ruta/version**. Una cancelación sólo es elegible G2 cuando se verifica estado/propósito **y** que no cancela/debilita protección de una posición. Grupo desconocido/efecto sobre children desconocido => no enviar cancelación automática, bloquear entradas/reconciliar/escalar. No inferir que cancelar remainder equivale a cancelar parent sin consecuencias.

Si hay fills concurrentes, la solicitud no libera cash/reserva. Sólo eventos reconciliados ajustan cantidades exclusivas filled/pending/cancelled, con protección efectiva confirmada. Broker puede ejecutar protección ya vigente durante pausa; nuevas ventas/cancel-and-new/replace no se autorizan por este contrato. Excepción de protección requiere su regla específica documentada, probada y aprobada.

## Evidencia primaria por ruta

- [Alpaca Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca): bracket activa salidas tras full fill; cancelar una orden puede cancelar el resto del grupo. Parcial previo no se presume protegido. Trailing standalone no equivale al ratchet propuesto. Cancelación y OCO no son atomicidad universal. B3 continúa NOT_TESTED.
- [IBKR TWS](https://www.interactivebrokers.com/docs/tws-api/doc/orders/place-order/adding-a-profit-taker-and-stop-loss) distingue children explícitos de PRESET; configuración externa requiere export/version. [Lección TWS](https://www.interactivebrokers.com/campus/trading-lessons/python-complex-orders/) contiene respuesta oficial histórica full-fill; [FIX p31](https://www.interactivebrokers.com/campus/wp-content/uploads/sites/2/2023/07/IBKR-FIX-Specification.pdf) describe otra semántica parcial. No transferir garantías FIX a TWS/cuenta vigente. Transmit coordinado no prueba protección parcial o atomicidad financiera.
- Tradier/tastytrade/TradeStation conservan [RC1](R-007_order_protection_matrix_RC1.md); sandbox artificial o API desktop no acepta lifecycle/API ejecutora ni economía. Verificar cada combinación, sin rechazo global por falta de evidencia.

## Matriz obligatoria B3 ampliada

| Caso | Evidencia positiva y negativa | Sin evidencia |
|---|---|---|
| Fill parcial antes de children activos | qty filled cubierta, ack/estado/trigger/TIF correcto y ventana de exposición medida | NOT_ADMITTED para esa ruta/variante; no asumir protección |
| Cancel parent/remainder | Efectos sobre children conocidos; carreras fill/cancel y continuidad de protectores | No G2 automático si puede debilitar protección |
| Rechazo/timeout/restart entre parent e hijos | Receipt/IDs/query y reserva/posición reconciliadas, protección efectiva | UNCERTAIN, entradas bloqueadas y humano si material |
| Cancel/replace concurrente con fill | No doble stop, sobreventa, short accidental o cash libre ficticio | Inadmisibilidad/incidente, no compensación financiera implícita |
| GTC/expiry/corporate action | Precio/qty/raw rebasados, renovación y estado confirmado antes de vencimiento | Protección no permanente por etiquetaGTC; contrato fail-closed |
| Gap/stop-limit sin fill | Trigger≠fill, precio/qty/mercado actual verificados | R2 no cero ni salida ficticia al stop |

Separa **protection policy** (diseño), **broker mapping** (docs + cuenta/API) y **acceptance** (target con B1–B5). `p_auth`/stop condicional no confirman cobertura posterior; latest mark favorable tampoco. El contrato debe fijar ventana máxima/alerta de exposición no protegida y acciones permitidas con gobierno de Risk/D031; hoy no se inventa cero latencia ni una tolerancia numérica. No seleccionar órdenes FOK/IOC o emergency close como parche sin evaluar soporte, costes y cambio de reglas.

## Paridad y economía

R009 debe representar activación children/parciales/grupos/cancel/fees de la ruta real; un fill simulado instantáneo no prueba protección. SDKs oficiales WRAP candidatos, no endpoints a LLM. APIs abiertas no incluyen permisos de mercado/KYC: [IBKR países](https://www.interactivebrokers.com/en/accounts/open-account-country-list.php) lista República Dominicana, no prueba apertura/entitlements del propietario. Cuotas/fees/data/funding/operación siguen scorecard por fase; no gasto ni nuevas credenciales aquí.
