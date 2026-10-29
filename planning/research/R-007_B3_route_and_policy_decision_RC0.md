# Q-064 — protección inicial y fills parciales PAPER

2026-10-29. **READY_FOR_DECISION de dirección financiera**, D-030/D-031/D-035; Alpaca sigue familia aprobada ADR-023. No aceptación B3, implementación o permiso de órdenes. La aprobación de una familia y la protección admisible son decisiones distintas.

## Hecho que obliga a decidir

[Documentación de órdenes Alpaca](https://docs.alpaca.markets/us/docs/orders-at-alpaca), revisada hoy: los exits bracket se activan después de completar el parent; OTO hereda requisitos y su texto no confirma replacement. No prueba protección de un fill parcial. Un stop fijo enviado antes tampoco reproduce automáticamente `p0_running−3ATR_signal` que depende de fills futuros. No se añade TP artificial ni se sustituye ratchet PRICE por trailing nativo.

La alternativa entry independiente → fill verificado → stop independiente requiere dos efectos externos. Si t_fill < t_observación ≤ t_envío_stop ≤ t_protección_efectiva, hay exposición entre fill y protección. Latencia/timeout/outage impiden garantizar un máximo absoluto por software cliente. Un watchdog sólo detecta incumplimiento; no limita pérdida ni asegura que la posición deje de estar descubierta. FOK/qty1/retry no hacen atómica esa secuencia; no suponer ausencia de parciales por tamaño pequeño.

En PAPER, [el simulador](https://docs.alpaca.markets/us/docs/paper-trading) puede producir parciales aleatorios y no limita tamaño por liquidez disponible; eso sirve para probar lifecycle, no ejecución real. Un feed IEX visible no reproduce necesariamente la información NBBO empleada por el simulador. B3 y book económico/ejecución permanecen separados.

## Alternativas y recomendación

| Dirección | Beneficio | Coste/riesgo y evidencia faltante |
|---|---|---|
| P0 — exigir cobertura nativa efectiva desde primer fill | Minimiza dependencia del cliente para protección inicial | Ninguna ruta Alpaca documentada admite hoy esa exigencia con nuestras reglas; no nuevas entradas. Mantener broker candidato hasta B3 target/documentación específica; si no cumple, reevaluar reserva, sin selección automática |
| **PF — desarrollar contrato post-fill acotado (recomendado condicionalmente)** | Conserva regla de stop dependiente del fill, sin TP o trailing sustitutos; permite especificar parciales reales | Acepta estudiar una ventana expuesta y fallo posiblemente persistente. Necesita presupuesto/tiempo/gap/cobertura y acciones aprobados, pruebas API target y protección/recovery. No admite ventana por redactar contrato |
| Cambiar semántica de estrategia/protección | Podría habilitar otro mecanismo nativo | Nueva variante/reglas, no equivalencia automática ni bypass de parciales; comparar antes de seleccionar Strategy. No recomendado como reparación silenciosa |

Se recomienda **PF como dirección de política sometida a condiciones, no operación** si el propietario acepta que PAPER pueda llegar a admitir ese riesgo explícito bajo un perfil posterior aprobado y probado. Investigar contratos ya está autorizado: la nueva decisión es la tolerancia conceptual a una ventana expuesta, no permiso para seguir estudiando. Si exige P0, preservar esa preferencia: no rebajar cobertura para avanzar ni dar por fallida la familia sin pruebas pertinentes. No se propone cambiar broker en este checkpoint ni aprobar ventana numérica arbitraria sin target.

## Contrato PF propuesto, todavía no aprobado

1. Entrada RTH, entero, límite ejecutable/cap contractual, DAY, extended_hours=false, sin adds/top-ups. OP-L1 sigue propuesta: el precio límite se fija con quote/freshness/tick y costes admitidos; nunca open futuro, ningún retry con ID nuevo por ack perdido. Strategy target congelado precede Risk.
2. Antes de enviar, persistir autorización, cantidades/reservas y un plan de protección determinístico versionado. El presupuesto descubierto/gap y qty por tramo cubren la **máxima cantidad alcanzable de fills**, incluido todo remainder vivo que pueda llenar durante instalación/cancel-race, no sólo el shortfall observado. Bloquear nuevas decisiones no detiene una orden ya viva. Cancel request no libera reserva; cap/tramos/FOK exigen semántica admitida. Reserva condicional no se presenta como R2 de posición protegida. Unknown de input/core/broker/audit bloquea envío.
3. Cada fill reconciliado agrega una cantidad económica única. Registrar cobertura/descubierto desde el instante económico del fill y desde recepción; no esconder retraso de feed. Recalcular desired inicial como max del anterior y p0_running−3ATR congelado, mismas unidades; no aflojar por fill favorable.
4. Proponer stop sólo para shortfall verificado sin otro command protector incierto o capaz de cubrir/vender esa cantidad. Mantener protectores existentes. Duplicados/pending_replace/held/ACK no se suman como protecciones distintas. No emitir sell por qty desconocida, ni cobertura mayor que posición por reenviar tras timeout.
5. Un futuro perfil PF aprobado podría distinguir PROTECTION_PENDING, transición esperada conocida y medida, de brecha/unknown/incidente material. Antes de ese perfil rige el fail-closed actual; redactar PF no crea excepción. En pending bloquear nuevas decisiones/dispatch de entradas; el remainder vivo todavía puede llenar, según§2. Ese estado no certifica protección. El perfil deberá incluir tabla de commands permitidos/inhibidos, datos/limites que deben seguir conocidos, qué instalación ya autorizada puede continuar y cuándo se convierte en incidente material. Ningún permiso general de operar durante pausa.
6. Confirmar efectividad por qty/precio/estado/orden/clocks reconciliados; verificar también parcial, expiración/corporate action/replace y stop cruzado. Ratchet posterior conserva old protector hasta confirmar replacement; no cancel-and-new que abra hueco por conveniencia.
7. Fuera de una futura transición PF expresamente admitida, brecha de protección; o en cualquier estado stop inválido/cruzado o incertidumbre material → G1+G2, evidencia y humano para resume. Sin G3, emergency sell ni autoflatten. No asumir que pausar elimina la exposición; reportar la cantidad aún descubierta, el remainder que todavía puede llenar y lo que no se puede reparar automáticamente. Un nuevo protector durante incidente sólo sería admisible mediante regla específica aprobada y probada, no por PF genérico.

### Parámetros y aceptación que PF NO aprueba

Tiempo desde fill y recepción, máxima edad de estado, presupuesto descubierto/gap, cantidad por tramo, stop grid/floor/efectividad, backoff/retries de commands y criterios de incidente requieren propuesta numérica + gobierno antes de CONFIG_ADMITTED/DoR. Ninguno se deduce del target100ms de SQL. Un máximo de watchdog no es garantía de cobertura en ese tiempo.

B3-PF cases: parcial→stop→otro parcial; fill durante cancel; fill después de timeout; stop rejected/unknown/crossed; viejo protector ejecuta durante replace; reinicio entre fill y persistencia/POST/ack; doble delivery; split y qty residual; pérdida de red/proceso/DB. Esperados preregistrados antes de ejecutar en target, con fail-closed y sin nuevos permisos. Si no puede cumplirse la política aprobada, no entradas y presentar reserva; no waiver por aprobar Q064.

## Decisión exacta

**¿Aprobar PF como dirección de política que permita llegar a admitir una ventana post-fill expuesta en PAPER, únicamente bajo un perfil numérico y técnico posterior aprobado y probado, o exigir P0/cobertura nativa desde el primer fill?** Recomendación PF condicionada. No se aprueba aún ventana operativa, duración, riesgo numérico, acciones de emergencia, cuenta, target, Strategy, gasto o implementación. Sin respuesta continúa P0/no nuevas entradas, no aprobación por silencio.

El paquete de [riesgo](R-027_parameter_and_binding_contract_RC5.md) y [D2](R-010_workload_and_durability_envelope_RC1.json) avanza de forma independiente. El punto de decisión no se convierte en bloqueo de proveedores o target de toda Preparation.
