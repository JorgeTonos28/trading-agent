# B3-S1 — traces ficticios de protección y reconciliación

Protocolo previo 2026-10-28. Modelo finito de evidencia, no adaptador ni Financial Core. Sin SDK/API/cuenta, mercado o backtest. Escenarios propios, precios y cantidades ficticios. Contrastar expectativas predefinidas, no generar resultados de estrategias.

Casos obligatorios: parent parcial con child held; full parent con child aún sin confirmación; child activo y cantidad/stop válidos; PATCH aceptado mientras viejo se ejecuta y nuevo se rechaza; pending_cancel con fills concurrentes; cancel parent que afecta children; replay de fill; reemplazos con IDs distintos; estado terminal con corrección tardía; stop cruzado sin ejecución; expiry/corporate action; pérdida de stream y snapshot inconsistente. Ningún ack de submit/replace cuenta como protección. Reserva de remainder sólo se libera por extinción confirmada y reconciliada.

PASS significa que el oráculo detecta el contraejemplo o conserva la invariante especificada. No acredita el comportamiento del broker ni pasa B3. Un estado descubierto durante transición es evidencia de exposición/UNCERTAIN, no autorización para alcanzarlo. No fabricar un fallback de liquidación, emergency stop o cancel-and-new durante incidente. Se preservan G1+G2 y reanudación humana material.

Resultado01:21 expectativas PASS,19 calculadas y2 marcadores declarativos (corrección tardía y ausencia de ruta admitida); [scope](../../probe_scope_evaluation_2026-10-28.json). No broker, B3 ni reconciliación completa aceptados.
