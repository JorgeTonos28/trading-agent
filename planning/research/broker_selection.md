# R-007 — Comparación de brokers PAPER y ruta futura LIVE (marco RC0)

**Baseline:** 2026-10-01. **Actualizado:** 2026-10-07. **Estado:** RESEARCHING; [wave documental 01](R-007_008_provider_evidence_wave01_2026-10-07.md) parcial, fichas restantes y probes pendientes. **Prioridad:** P1 para selección PAPER; pruebas de órdenes P2. **Decisión:** D-021, con aprobación humana antes de seleccionar. **Alpaca es referencia funcional del video, no broker elegido.** No abrir cuentas, conectar credenciales ni cursar órdenes durante preparación salvo probes desechables necesarios para cerrar decisiones del plan.

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

## Scorecard económico por fase — ADR-008

PAPER prioriza cuenta/API/datos paper sin gasto adicional **si cumplen calidad/semántica**. LIVE admite servicios pagos con valor y economía unitaria demostrados. No descartar broker futuro por precio PAPER ni inferir coste live desde simulación. Aplicar [ficha común](../economic_scorecard.md): fijo, variable, mensual y escala; comisiones/fees, datos, mínimos, API, custodia/funding/FX aplicables, slippage y mantenimiento/lock-in separados. Investigar no contrata; gastar requiere aprobación humana.

| Candidato | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Alpaca | UNKNOWN hasta elegibilidad/semántica | UNKNOWN | UNKNOWN | Otros brokers paper por validar | Calidad API/datos/órdenes/continuidad por probar | YES antes de gasto |
| IBKR | UNKNOWN | UNKNOWN | UNKNOWN | Otros brokers paper por validar | Cobertura/controles/coste total por probar | YES antes de gasto |
| Tradier | UNKNOWN | UNKNOWN | UNKNOWN | Otros brokers paper por validar | Paridad/órdenes/datos por probar | YES antes de gasto |
| tastytrade | UNKNOWN | UNKNOWN | UNKNOWN | Otros brokers paper por validar | API/streaming/cobertura por probar | YES antes de gasto |
| TradeStation | UNKNOWN | UNKNOWN | UNKNOWN | Otros brokers paper por validar | API/semántica/fiabilidad por probar | YES antes de gasto |

Estas filas conservan el inventario inicial 2026-10-02, no un precio vigente. Cada broker adicional tendrá los mismos seis campos antes de entrar al scorecard.

## Evidencia y scorecard vigente parcial — 2026-10-07

[Wave 01](R-007_008_provider_evidence_wave01_2026-10-07.md) actualiza los seis campos para Alpaca paper/data, IBKR y Tradier con fuentes oficiales. PAPER gratuito publicado no demuestra elegibilidad LIVE RD, permisos de cuenta ni paridad económica de fills. IBKR incluye RD en lista general, sin aprobación KYC; Tradier requiere distinguir streaming de mercado y eventos de cuenta. Todos SELECTED=NO; API adapters WRAP candidatos, nunca tools financieros de LLM.

Fichas tastytrade/TradeStation/otros y matriz concreta protection/order lifecycle/recovery siguen pendientes. Pruebas account/host-specific se ejecutarán solo en target autorizado; la comparación documental continúa Team/INFOTEP, sin cuenta, credenciales ni órdenes.

## Matriz de órdenes/protección — 2026-10-13

[RC1 cinco brokers](R-007_order_protection_matrix_RC1.md) distingue trial/simulator/api/paper-live y B1–5 NOT_TESTED. Bracket/OTO/trailing/parciales/session/replace necesitan mapping concreto; tastytrade fills artificiales y resets no validan P&L/recovery multiday. TradeStation instant SIM tampoco demuestra fill-realism. Broker OPEN a selección, sin cuenta ni acceso operativo desde AI.
