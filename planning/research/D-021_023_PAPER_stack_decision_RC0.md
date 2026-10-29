# Q-062 — selección de diseño del stack broker/backtesting PAPER

2026-10-23. P1 / **READY_FOR_DECISION** del propietario. Propuesta basada en revisión de acceso, semánticas, builds y llamadas nativas de componentes. No está aprobada por anticipado ni acepta pin, distribución, modelos, configuración financiera, Strategy V1 o método estadístico.

## Recomendación: paquete A

**Alpaca Paper Only como broker PAPER y LEAN source como familia principal de backtesting.**

Reutilizar el motor y adaptar los modelos/contratos necesarios; envolver APIs/SDK oficiales cuando corresponda. IBKR TWS queda como reserva de broker y Nautilus como reserva de motor. No se requieren dos motores productivos. Datos históricos, referencia monetaria y LIVE siguen abiertos.

Alpaca documenta una ruta paper global sin funding. La documentación actual de TWS exige cuenta IBKR Pro abierta/fondeada y añade dependencias de sesión. LEAN Common/Engine compilan desde fuente y QL2 ejecutó componentes de fills y acciones corporativas; las diferencias de parciales y pay-date están identificadas. La recomendación no depende de resultados de estrategias ni de comparar conteos de PASS. Evidencia: [broker RC4](R-007_PAPER_broker_selection_packet_RC4.md), [motor RC2](R-009_engine_selection_packet_RC2.md).

## Alternativas y trade-offs

| Paquete | Ventajas | Riesgos y dependencias |
|---|---|---|
| **A: Alpaca PAPER + LEAN source** | Acceso paper global documentado; REST/streaming; componentes equity/actions compilados y ejecutados | El simulador broker omite dividendos y otros costes/efectos; IEX no equivale a NBBO. Parciales/OTO/replace pendientes. Ingeniería .NET y adaptación de modelos; pin/dependencias por aceptar |
| B: IBKR TWS + LEAN source | API, cobertura y órdenes amplias; RD en lista pública; mismo motor | Pro/funding/entitlements y mantenimiento de sesiones. Paper no garantiza paridad. Seleccionarlo no autoriza depósito, cuenta ni gasto |
| C: Alpaca PAPER + Nautilus | Superficie Python/wheel y matcher nativo ya ejecutado | Mayor incertidumbre en acciones corporativas/receivables/adaptadores. El flag L1 probado no impuso el hard cap supuesto. LGPL3, dependencias y paridad por revisar |

Ninguna opción resuelve por sí sola licencia/PIT, protección, cash, datos o calificación. No se presupone un broker de fills perfectos ni se propone construir un simulador general como atajo.

## Alcance exacto de aprobar A

Selecciona **familias de diseño PAPER** para concretar especificación e integración. D-021/D-023 pueden registrar esa selección; mantienen abiertos y explícitos sus gates P1/P2 aplicables de pin, protección, modelos, paridad y target. No se alcanza DoR por esta aprobación.

No autoriza crear cuentas, solicitar credenciales, modificar host/ACL/firewall, depositar/fondear, contratar datos/CLI/API, aprobar Strategy/riesgo ni implementar Trading OS. Preparación continúa en Team; las acciones target serán gobernadas en PC personal/Plus. LIVE permanece sin selección.

**B3 no se relaja por elegir broker.** Sin un mapping admisible de protección no hay entradas. No fabricar cobertura desde un precio deseado ni agregar un take-profit artificial. Nuevas tolerancias de desprotección, reglas o G3 requieren gobierno. Un fallo material de la familia elegida se registra antes de proponer sustitución o ampliación de permisos.

## Decisión solicitada

¿Aprueba el propietario **A — Alpaca Paper Only + LEAN source** como selección de diseño PAPER, manteniendo esos gates e IBKR/Nautilus como reservas? Es una decisión de dependencias tecnológicas y operativas, no permiso para investigar ni solicitud de acceso ahora.

## Resultado — 2026-10-28

**Q-062/A DECIDED por el propietario**, [ADR-023](../decisions/ADR-023-paper-broker-and-backtesting-families.md). Alpaca Paper Only + LEAN source seleccionados como familias de diseño; IBKR/Nautilus reservas. La pregunta anterior queda histórica. Se mantienen B1–B5/QP1–QP10 y todas las exclusiones. Investigar ejecución local de fuente, sin asumir gratuidad CLI/Cloud; B3 no admisible bloquea entradas. No aceptación operacional ni elegibilidad LIVE.
