# Open Questions — inventario inicial

Fecha: 2026-10-01. Cada Q apunta a una decisión del [registro](decision_register.md). La prioridad expresa el gate más temprano que bloquea. El criterio de cierre es evidencia verificable, no una preferencia informal.

Estados: cada Q muestra su prioridad; Q-030–Q-037 incluyen estado explícito. Las Q anteriores conservan el estado inicial salvo que el registro de decisiones indique investigación en curso. Actualizar el estado al registrar su resolución.

| ID | Prioridad | Decisión | Pregunta y evidencia para cerrarla |
|---|---|---|---|
| Q-001 | P0 | D-008/010 | ¿Debe MATR_V1 ser Strategy V1 o un benchmark/candidato descartado tras comparación? El propietario confirmó que **no está seleccionada**; faltan reglas de candidato, evidencia y decisión humana final. |
| Q-002 | P0 | D-011 | El propietario confirma que **nunca se ejecutaron ni vieron backtests de MATR_V1**. ¿Qué política OOS preserva independencia al comparar varios candidatos y cómo se preregistra antes de consultar resultados? |
| Q-003 | P0 | D-011 | ¿Qué costes, spreads, slippage, parciales, dividendos e impuestos de transacción se modelan por escenario? Datos y test de sensibilidad. |
| Q-004 | P0 | D-012 | `DECIDED` en ADR-006: propietario aprobó opción B conceptual; controles independientes y límite más restrictivo. Fórmulas, escenarios y umbrales concretos continúan D-031/D-021/026/030; no existe aprobación para G3. |
| Q-005 | P0 | D-013 | `DECIDED` en contrato abstracto ADR-003: persistir antes de enviar, `UNKNOWN` sin reenvío, ledger de eventos y reconciliación de órdenes/fills/posición; mapeo y probes por broker D-021/030. |
| Q-006 | P0 | D-014 | `DECIDED` en ADR-004: clocks separados, evidencia por canal, `eligible_from`, revisiones as-of y snapshot inmutable; retrasos/muestras concretos D-018/022/033. |
| Q-007 | P0 | D-015 | `DECIDED`: el propietario aprobó A+ (ADR-001); Portfolio Manager Agent produce propuestas shadow auditables sin alterar intents operativos. |
| Q-008 | P0 | D-016 | `DECIDED`: un Champion operativo inicial puede combinar fuentes/señales; shadow y pedagogía factual desde B4; contrato completo pedagógico antes de DoD. Traceability detallada sigue en P1. |
| Q-009 | P0 | D-017 | `DECIDED`: propietario aprobó G1+G2, conservación de protección y reanudación humana tras pausa material en ADR-002; G3/liquidación automática no autorizados. Umbrales/clasificación detallada continúan D-031. |
| Q-010 | P0 | D-020 | ¿Qué capacidades existen, están disponibles a esta cuenta/región, son compatibles, asequibles y seleccionables? Evidencia de fuente primaria, licencia, coste, permisos, probes y clasificación; gate de D-024. |
| Q-011 | P1 | D-021 | ¿Qué broker PAPER admite el perfil real del dueño desde RD, los ETFs/órdenes necesarios, datos/stream y pruebas de recuperación? Verificación oficial y probes. |
| Q-012 | P1 | D-022 | ¿Qué proveedor cubre historia 2005–2026, ajustes, delistings/cambios, timestamps, uso automatizado y costes? Muestra comparada. |
| Q-013 | P1 | D-023 | ¿LEAN, NautilusTrader, vectorbt u otra solución reproduce las semánticas de los candidatos viables y sus fallos con coste razonable? Benchmark. |
| Q-014 | P1 | D-024 | `OPEN / GATED_BY_R-006`: ¿Qué Skills, plugins, MCP y frameworks sirven al Plan Architect y agentes operativos sin delegar autoridad de órdenes? La arquitectura/runtime no puede cerrarse antes de madurez R-006, pruebas de permiso/evals y aprobación material. |
| Q-015 | P1 | D-025 | ¿Temporal, otra solución o scheduler simple cumple recovery, replays e idempotencia a la escala V1? Prueba de fallos y coste operativo. |
| Q-016 | P1 | D-026 | ¿Qué repositorios de datos y eventos preservan decisiones, versiones, P&L y audit trail reconstruible? Esquemas y restore. |
| Q-017 | P1 | D-027 | ¿Qué aislamiento evita que prompt injection, plugin, dependencia o credencial paper alcancen ejecución/secretos live? Threat model. |
| Q-018 | P1 | D-028 | ¿Qué SLO/alertas/runbooks y backups exige PAPER V1 y cómo se ensayan? SLO medibles y tabletop. |
| Q-019 | P1 | D-029 | ¿Cómo se prueba que el sistema falla cerrado, no duplica órdenes y no promueve Challengers? Matriz de invariantes, integración y evals. |
| Q-020 | P2 | D-030 | ¿Qué tipo de orden de próxima sesión y protección broker-side muestran paridad suficiente entre replay y paper? Probes. |
| Q-021 | P2 | D-031 | ¿Son coherentes los valores PAPER 0.50/2/25% y las acciones soft/hard con gap risk y capital disponible? Calibración, stress y aprobación. |
| Q-022 | P2 | D-032 | ¿Qué periodo, cobertura de regímenes e incident budget se exige antes de paper autónomo? Gate medible. |
| Q-023 | P3 | D-040 | ¿Qué broker LIVE es elegible para el dueño en RD, y bajo qué entidad, jurisdicción y derechos de mercado? Confirmación documental. |
| Q-024 | P3 | D-041 | ¿Qué capital, impuestos, documentación y obligaciones aplican al perfil real? Validación profesional y decisión humana. |
| Q-025 | P3 | D-042 | ¿Qué evidencia separa paper/shadow/live mínimo y qué recuperación se exige para dinero real? Plan y aprobación. |
| Q-026 | P4 | D-050 | ¿Tienen Congreso/Form 4/noticias señal incremental tras latencia y costes? Estudios PIT separados. |
| Q-027 | P4 | D-051 | ¿Vale abrir derivados, shorts u otros activos? Investigación futura y nuevo gate humano. |

## Preguntas de integridad documental

- Q-028 (P1, D-016, `DECIDED`): se corrigió `AGENTS.md` para señalar el roadmap existente indicado por el usuario.
- Q-029 (P1, D-016, `DECIDED`): se adoptó `planning/` como ubicación canónica de acuerdo con §3.5 de la hoja. Los nombres sin prefijo siguen §3.5 y conservan todo el contenido requerido por §3.23.

## Strategy V1 Selection

- Q-030 (P0, D-009, `RESEARCHING`): La transcripción separa infraestructura, trailing stop/ladder, señales congresuales, alertas, SIGNAL y opciones. ¿Qué mecanismos merece conservar, modificar, separar o descartar para **nuestro** Trading OS? Pantallas/prompts solo cuando aclaren el diseño; no auditar claims de rentabilidad.
- Q-031 (P0, D-008, `OPEN`): ¿Qué criterios y pesos compararán Video-Inspired Strategy V1, MATR_V1 y otros candidatos sin seleccionar por rendimiento observado? Debe cerrarse antes de evaluar resultados y luego someter selección al propietario.
- Q-032 (P0, D-009/012, `OPEN`): ¿Existe alguna regla coherente de stop, reentrada y tamaño para VID-TS, dado que el video alterna stop inicial 10/20%, compra tras caída ~20% y deja al agente elegir cantidad? Pantallas originales, especificación explícita y escenarios de conflicto.
- Q-033 (P0, D-008/022/033, `OPEN`): ¿Puede VID-CONG o VID-ALERT obtener historia con disponibilidad PIT y derechos suficientes bajo ADR-004/005? Evaluación R-021; los dashboards del video no bastan.
- Q-034 (P0, D-018, `DECIDED`): ADR-005 fija roles graduados y gates de admisión para todas las familias Smart Money; ninguna familia queda seleccionada. Evidencia PIT y proveedor por dataset siguen D-022/033 y Strategy V1 D-008.
- Q-035 (P0, D-019, `DECIDED`): el propietario aprobó explicación factual desde B4 y reporte completo antes de DoD, derivados de traza real y sin autoridad de trading. Formato/evals detallados P1 después.
- Q-036 (P1, D-033, `RESEARCHING`): ¿Qué combinación de Quiver, Unusual Whales, Capitol Trades, SEC/EDGAR y otros proveedores entrega cada dataset con historia PIT, API, latencia, licencia, calidad y coste adecuados? Scorecard R-025.
- Q-037 (P1, D-021, `OPEN`): ¿Qué broker es elegible para RD y sirve a equities PAPER con API, streams y órdenes protectoras, manteniendo opciones futuras sin imponer derivados en V1? Comparación R-007; Alpaca no está seleccionado.
- Q-038 (P1, D-034, `OPEN`): ¿Qué esquema, aislamiento técnico, protocolo de evaluación PIT y métricas preregistradas permiten comparar Champion con `ShadowPortfolioProposal` sin que el shadow influya en operaciones ni obtenga datos futuros?
- Q-039 (P1, D-035, `OPEN`): ¿Cuáles son las fórmulas, unidades, redondeos, precedencia y casos de concurrencia verificables que concretan ADR-006 sin fijar aún los umbrales PAPER de D-031?
