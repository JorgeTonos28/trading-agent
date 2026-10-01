# R-007 — Comparación de brokers PAPER y ruta futura LIVE (marco RC0)

**Fecha:** 2026-10-01. **Estado:** OPEN (marco de comparación RC0; fichas y probes pendientes). **Prioridad:** P1 para selección PAPER; pruebas de órdenes P2. **Decisión:** D-021, con aprobación humana antes de seleccionar. **Alpaca es referencia funcional del video, no broker elegido.** No abrir cuentas, conectar credenciales ni cursar órdenes durante preparación salvo probes desechables necesarios para cerrar decisiones del plan.

## Candidatos iniciales, sin selección

Alpaca, Interactive Brokers (IBKR), Tradier, tastytrade, TradeStation y otros API brokers que cumplan el perfil del propietario. Incluir alternativas nuevas solo con fuente oficial y razón de elegibilidad. El broker PAPER y el futuro LIVE pueden diferir; el adapter debe evitar dependencia accidental del primero.

## Gates antes de score ponderado

1. **Elegibilidad real** para residente en República Dominicana y tipo de cuenta requerido; verificar entidades, KYC, disponibilidad de paper/API y restricciones mediante fuentes oficiales. No inferir live por ofrecer paper.
2. **Equities/ETFs PAPER** y automatización permitida bajo términos vigentes.
3. **Controles operativos mínimos**: consulta de órdenes/posiciones, cancelación, eventos/fills y recuperación tras caída, identificadores para reconciliación.
4. **Seguridad y segregación** de credenciales paper/live, scopes y permisos; agente sin acceso directo a orden genérica.

## Criterios comparativos

| Dimensión | Evidencia requerida |
|---|---|
| API y SDK | Documentación, autenticación, versionado, rate limits y soporte oficial |
| Paper/live | Diferencias de instrumentos, fills, precios, datos, saldos, horario y semántica de órdenes |
| Streaming y recuperación | Websocket/eventos, secuencias, reconexión, replay/polling, outage status |
| Órdenes | Market/limit, stop/stop-limit, bracket/OCO, trailing, parcial, GTC/TIF y horarios; validar compatibilidades concretas |
| Confiabilidad | Estado público, historial de incidentes, cambios API, soporte y pruebas de fallos propias |
| Disponibilidad RD | Confirmación oficial para el perfil concreto, no solo una lista general de países |
| Instrumentos futuros | Equities/ETF ahora; options como capacidad futura sin incluir derivados en PAPER V1 |
| Coste y datos | Comisiones, fees, market data, mínimos, financiación, spread implícito y coste de uso API |
| Seguridad | Secrets, scopes, IP restrictions si existen, segregación de cuentas, audit logs y revocación |

## Entregable y decisión

Ficha fechada por broker con `EXISTS / AVAILABLE_TO_US / TECHNICALLY_COMPATIBLE / ECONOMICALLY_REASONABLE / SELECTED`, fuente primaria, probes y `REUSE_AS_IS/WRAP/REJECT` cuando corresponda; scorecard con pesos fijados antes de pruebas y ADR aprobado por el propietario. Los probes B1–B5 verifican semántica paper después de preselección. El soporte futuro de opciones cuenta como criterio, pero no justifica comprometer V1 con derivados.
