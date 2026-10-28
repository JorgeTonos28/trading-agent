# Alpaca PAPER — protección, parciales y reconciliación RC5

2026-10-28. Familia seleccionada ADR-023; **B1–B5 NOT_ACCEPTED**, B3 no admitido bloquea entradas. Diseño/contratos avanzan sin cuenta. No ampliar A+, G1+G2, G3 o permisos durante incidentes.

## Rutas y hechos verificables

| Ruta | Evidencia documental actual | Resultado de diseño |
|---|---|---|
| Bracket/OTO | [Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca): children bracket tras full fill; OTO hereda requisitos y mantiene texto de replacement no soportado, contradictorio con bracket | No cobertura parcial demostrada; no mapear p0−3ATR de fill futuro a un child fijo previo sin equivalencia. No TP artificial para forzar bracket |
| Buy standalone + stop tras fill | Stop de salida sólo para posición existente; exige otro envío/confirmación | Ventana no protegida y carreras de quantity. No aprobada por este documento; requiere regla específica de protección/tiempo/acciones permitidas y B3 |
| FOK/IOC | Documentados pero TIF marcado con asterisco/contacto para whole qty; advanced orders restringen TIF | No presumir disponibilidad, compatibilidad OTO o eliminación de toda ventana. IOC permite parciales; FOK no hace atómico el stop posterior |
| Trailing standalone | HWM/trail nativos, RTH, sin leg bracket/OCO; corporate actions pueden modificar/cancelar | No equivale al ratchet PRICE10/5/5 ni arregla activación inicial. No sustituir reglas |
| PATCH | [Referencia](https://docs.alpaca.markets/us/reference/patchorderbyorderid-1): HTTP exitoso no garantiza replace; fill viejo puede rechazar nuevo; ciertos estados no admiten PATCH | Mantener grafo viejo/nuevo y cantidad efectiva; confirmación por estado/evento reconciliado, nunca por HTTP200 |

No hay ruta B3 declarada admisible. Es una pregunta real de mapping/política financiera, no sólo un checkbox de acceso. Los tests target podrán aportar comportamiento; no repararán por sí solos una regla de protección sin definir. No seleccionar otra familia o tolerancia silenciosamente.

## Contrato concreto de estados y evidencia

Por posición: economic_lot_id, security_id/raw units, broker_order_id/client_order_id, parent/leg/replaces/replaced_by, exec/activity IDs, cantidad filled, remainder, cantidades protegidas/descubiertas, precio/tipo/TIF/expiry del protector y clocks de recepción/efectividad. Stop deseado, held, submitted, pending_replace o ACK no cuentan como protección confirmada. Stop cruzado sin fill verificado implica UNCERTAIN, no R2=0.

Por orden: ingesta raw sellada, normalización versionada, dedupe por identidad de ejecución y preservación de busts/correcciones. `filled` terminal no significa que una corrección posterior pueda descartarse. No sumar simultáneamente cum_qty y fills individuales. Desconexión/timeout/paginación incompleta retienen incertidumbre y reservas; REST posterior requiere reconciliar órdenes, legs, actividades y posiciones, no presumir un snapshot global atómico.

G2: cancelar únicamente entrada verificada cuyo grafo/effect no debilite protección. Cancel parent/remainder no es elegible si sus efectos sobre children son desconocidos. Fills durante cancel siguen siendo posición; la petición no libera cash. Una orden protectora existente puede ejecutarse durante pausa; no se concede emergency sell, nuevo stop o cancel-and-new por conveniencia sin la regla específica aprobada.

Al reiniciar: no reenviar POST por timeout con un ID nuevo. Buscar por IDs conocidos, consultar posiciones/órdenes/actividades con solape y paginación hasta cobertura verificable; contradicción material pausa/reconciliación/humano. El modelo puede explicar el incidente, no resolverlo con herramientas financieras.

## Libro operativo versus económico

Saldo cash/holdings del broker y book de evaluación son distintos. No usar margin buying_power como presupuesto propio ni inferir settled cash de un campo no documentado. El mapping de efectivo necesita semántica de débitos, retenciones, settlement, fees y actividades; si no puede demostrarse cash elegible, no autorización positiva. [Actividades](https://docs.alpaca.markets/us/docs/account-activities) proporcionan IDs/cum_qty/leaves_qty/fills y actividades no trade, no una prueba automática de settlement elegible.

Dividendo ausente del simulador paper nunca crea cash operativo desde el modelo. El book económico registra entitlement/receivable/pago verificados y costes incrementales por separado. No compensar divergencias depositando cash ficticio, resetear cuenta para borrar pérdidas o llamar paridad al P&L broker. Al evaluar utilidad: modelo económico admitido y broker paper operacional son gates distintos.

## Acceptance B1–B5 y paridad

B1 endpoint/cuenta exclusivamente PAPER y no LIVE; B2 feeds/quotes/clocks/cash/entitlements; B3 secuencias completas parciales/protección/replace/cancel/expiry/actions; B4 costes/dividendos/liquidez y divergencias; B5 stream/disconnect/restart/recovery/carga. Probar positivos y negativos, ninguna corrección manual oculta. Source/config/versiones y trace esperado antes de cada caso; precio stop no garantiza fill.

[B3-S1](probes/r007-alpaca-contract-traces/README.md):21 expectativas PASS de fixtures;19 calculadas y2 marcadores declarativos identificados en la evaluación de scope. No son21 pruebas de broker, ni full reconciliation o B3 PASS. Los contraejemplos precisan el contrato; no autorizan alcanzarlos en operación.
