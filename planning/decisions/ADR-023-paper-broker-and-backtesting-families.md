# ADR-023 — Alpaca Paper Only + LEAN source para diseño PAPER

- Fecha de aprobación y registro: 2026-10-28.
- Estado: **DECIDED — DESIGN_FAMILIES_ONLY**.
- Decisión: Q-062/A; selección de diseño D-021/D-023. No aceptación operacional ni cierre de todos sus gates.
- Fuente: instrucción explícita del propietario en esta sesión. Antecedente: checkpoint a249d77 y propuesta Q-062.

## Dirección aprobada

Alpaca Paper Only es la familia principal de broker PAPER V1; LEAN source, la familia principal de backtesting. IBKR TWS y Nautilus permanecen como reservas. Reutilizar el motor y envolver/adaptar APIs, modelos e interfaces necesarias antes de proponer capacidades generales propias.

LEAN source se investigará como ejecución local desde código fuente. Apache 2.0 del motor no demuestra gratuidad de LEAN CLI, QuantConnect Cloud, datos o servicios comerciales; no se activan ni contratan por esta decisión.

## Condiciones vinculantes

1. Mantener B1–B5 y QP1–QP10: protección efectiva, parciales, cancel/replace, reconexión, reconciliación y paridad.
2. Representar explícitamente diferencias del simulador Alpaca en dividendos, liquidez, slippage, costes y ejecución. El libro económico no crea buying power operativo del broker.
3. Si B3 no demuestra protección admisible, no habilitar nuevas entradas. Bracket/OTO o un precio de stop deseado no acreditan protección de cantidad ejecutada. No se añade una tolerancia de desprotección ni G3.
4. La disponibilidad global de Paper Only no acredita elegibilidad LIVE en República Dominicana. Broker LIVE sigue abierto.
5. La elección de familia no acepta el pin LEAN actual, SDK, modelos, datos, Strategy V1, límites de riesgo, host, runtime ni capacidad sostenida.

## Autorización y seguimiento

No autoriza cuenta, credenciales, suscripción, contratación, depósito, gasto, implementación, operación ni LIVE. `implementation_locked=true`, `TARGET_ACCEPTANCE_DEFERRED`, holdout `INTEGRITY_UNKNOWN`.

D-021/D-023 registran selección de diseño; mappings/pin/seguridad/modelos/aceptación se conservan como obligaciones P1/P2 según su fase. DoR no se alcanza por esta aprobación. Cualquier incompatibilidad material requiere evidencia y gobierno antes de sustituir familia o debilitar contratos.
