# R-007 — comparación de rutas de órdenes y recovery RC3

2026-10-23. D021 RESEARCHING. Fuentes oficiales, sin cuenta/SDK/login/API/broker/órdenes reales. No elegir broker por etiqueta bracket ni precio0. Completa [dependencias RC2](R-007_protection_dependency_contract_RC2.md); B1–5 siguen sin aceptación target.

## Hallazgos que cambian la especificación

| Ruta | Evidencia oficial vigente | Consecuencia para PRICE–MATR |
|---|---|---|
| Alpaca REST | [Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca): bracket activa hijos después de fill completo; cancelar miembro cancela resto; DNR/DNC, sin extended-hours; PATCH de precios documentado para bracket/OCO. OTO aparece con reemplazo aún no soportado, en contradicción textual con otra referencia de bracket. pending_replace rechaza cancel | No admitir protección parcial por defecto ni asumir que OTO permite ratchet. No agregar take-profit artificial a PRICE/MATR para obtener un bracket reemplazable: cambiaría estrategia. B3 debe resolver ruta exacta y conflicto de documentación |
| IBKR TWS | [Modificación](https://www.interactivebrokers.com/docs/tws-api/doc/orders/modifying-orders): mismo username/clientID/orderID; permID identifica orden entre bindings; reqAllOpenOrders no hace bind. Binding puede cancelar/reenviar y cambiar prioridad | Recovery no debe «re-adoptar» una orden a ciegas mediante una consulta con efectos. Persistir session/client/IDs y reconciliar open/completed/executions antes de nueva acción; preservar protectores. No transferir garantías FIX a TWS |
| IBKR TWS preset | [Child/presets](https://www.interactivebrokers.com/docs/tws-api/doc/orders/place-order/adding-a-profit-taker-and-stop-loss): parámetros de bracket pueden venir de presets externos | Preferir children explícitos/versionados para investigación; presets sin export/hash no config reproducible. No afirma que una API determinada active protección proporcional a parciales |
| IBKR continuidad | [Reauth](https://www.interactivebrokers.com/docs/tws-api/doc/tws-settings/daily-weekly-reauthentication) y [socket](https://www.interactivebrokers.com/docs/tws-api/doc/connectivity/broken-api-socket-connection): sesión/gateway/reautenticación tienen lifecycle propio | D025/028 requieren maintenance/reconnect/snapshot/reconcile; reauth manual periódica no equivale a aprobación de cada operación. No almacenar/bypassear2FA ni crear tareas/servicios ahora |
| Tradier | [Trading](https://docs.tradier.com/docs/trading), [advanced](https://docs.tradier.com/reference/advanced-orders): REST/sandbox, equity whole shares, clases OTO/OCO/OTOCO; tag es etiqueta opcional | tag no demuestra deduplicación/idempotencia; activation/cancel-replace/partial/protección siguen por probar. Sandbox delayed no garantiza paridad ni fills reales. No inferir elegibilidad RD de API pública |

Fuentes legacy TWS full-fill y FIX partial mantienen alcance histórico/API separado. No hay nueva evidencia de que ninguna ruta cumpla aún el contrato de protección parcial exacto. Tradier/tastytrade/TradeStation conservan sus fichas y gaps; falta de evidencia no es rechazo global.

## Recomendación técnica de shortlist y protocolo

Mantener **IBKR TWS y Alpaca REST** como finalistas de ingeniería, sin seleccionar broker: IBKR por cobertura/capacidades documentadas y RD en lista pública previa, con complejidad de sesiones/recovery; Alpaca por integración REST/streaming/paper, condicionado a elegibilidad real/datos/licencia y protección/ratchet. Tradier reserva activa por OTOCO/whole-equity pero menos evidencia de estas semánticas. No puntuar return ni prometer apertura/KYC.

Binding por ruta: entry type/TIF/cap/expiry, parent-child dependencies, qty/price de cada parcial, condición de activación, cancel/remainder, OCO/overfill, modificación/rechazo/timeout, GTClifecycle/actions, exec/bust/commission/cash/settlement clocks, ownership y recuperación. No default market, GTC perpetuo ni priceatstop. Las mismas obligaciones alimentan QP y el perfil Risk.

Negativos previos a selección/aceptación: fill parcial con child held; cancel de entrada que derriba stop; replace en vuelo que recibe fill; doble cierre por OCO; restart con IDs equivocados; snapshot incompleto; cash no reflejado; split sin ajuste confirmado. Resultado permitido: UNCERTAIN/G1+G2 y reanudación humana si incidente material, nunca liquidación general o orden compensatoria implícita.

**Hito cerrado de diseño:** inventario de semánticas/recovery y evidencia que exige B3. **No cerrado:** broker, mapeo probado, ventana/umbrales de protección y capacidad target. No hace falta esperar emails de históricos para completar esta comparación, pero no sustituye pruebas de cuenta.

## Economía por fase y reuse

SDKs/APIs oficiales: WRAP/ADAPT candidatos; no herramienta/MCP con credenciales de broker en AI. PAPER_V1_VIABLE_FREE=CONDITIONAL por broker/cuenta/datos; PAPER_V1_COST acceso paper0 donde documentado, fees/data/operación y fijo/variable/mensual efectivos UNKNOWN; LIVE_COST UNKNOWN por cuenta/mercado/volumen. FREE_ALTERNATIVE los otros finalistas por admitir. PAID_INCREMENTAL_VALUE mejores datos/ejecución/soporte sólo si medidos. ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. Lock-in de sesiones/IDs/órdenes/market entitlements y salida/recovery deben medirse.

Un investigador/seisETF/órdenes de baja frecuencia no define aún volumen/turnover; no inventar mensualización. Costes de todas rutas admitidas/estrés en2k/5k/10k/25k/50k, nominal10k y20celdas previas conservados. Elegibilidad, trading permissions, terms y pricing por producto no admitidos por esta nota.
