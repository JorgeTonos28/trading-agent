# R-022 — Mapa funcional del Trading OS (RC0)

**Fecha:** 2026-10-01. **Estado:** mapa completado; [contrato PAPER V1 RC1](../paper_v1_capability_contract_RC1.md) y ADR-001 aprueban A+ para D-015/016/019; ADR-005 cierra roles/admisión abstracta D-018. **Prioridad:** P0. **Decisiones:** D-015, D-016, D-018, D-019. Este mapa convierte la inspiración del video y la [hoja v0.2](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md) en requisitos de **nuestro** sistema. No fija stack, broker ni Strategy V1; no autoriza implementación.

## Capacidades y fronteras

| Capacidad | Entrada → salida verificable | Frontera/decisión aún abierta |
|---|---|---|
| Descubrimiento e investigación | Fuentes/hipótesis → dossier con origen, timestamps, limitaciones y experimento | Research Agents solo lectura; no promueven Champion ni alteran riesgo |
| Ingestión y normalización | Market/alternative data → snapshots versionados con clocks separados, `availability_evidence`, `eligible_from` y revisiones as-of | Semántica D-014/ADR-004; proveedor/admisión D-018/D-022/D-033, calidad y licencias |
| Strategy Lab y backtest | Hipótesis versionada → reglas falsables, replay, OOS y comparadores | Selección D-008; motor D-023; acceso al holdout |
| Signal Engine | Datos elegibles + reglas Champion → señal operativa determinística rastreable | D-015/ADR-001 A+ DECIDED; reglas Strategy V1 D-008 abiertas. Ningún output LLM completa una regla operativa |
| Portfolio/intent | Señal + cartera reconciliada → `TradeIntent` operativo versionado, ensamblado determinísticamente | Contratos abstractos D-012/013 aprobados; fórmulas D-035, parámetros D-031 y prioridad Strategy D-008 abiertos; un Champion puede combinar señales |
| Portfolio Manager shadow | Mismo contexto elegible cuando corresponda → `ShadowPortfolioProposal` auditada | Sin ruta a `TradeIntent`/Execution; detalle y evaluación PIT D-034 |
| Risk Engine | Intent + estado + presupuesto → aprobar/reducir/rechazar con motivo | **Determinístico**; controles independientes y mínimo restrictivo D-012/ADR-006 DECIDED, fórmulas D-035/umbrales D-031 abiertos; incidente G1+G2 D-017/ADR-002 |
| Execution/Broker adapter | Autorización válida → órdenes, eventos, fills, reconciliación | Broker D-021; idempotencia/recuperación D-013; sin acceso directo del LLM |
| Monitorización | Datos, posiciones, órdenes, salud y desempeño → alerta/solicitud de suspensión | G1+G2 y reanudación humana tras pausa material aprobados; SLO/runbooks D-028 |
| Champion/Challenger | Evidencia de experimentos → comparación y solicitud de promoción | Solo humano aprueba promoción/cambios centrales; D-005/D-016 |
| Pedagogical Agent | Hechos auditados sobre señal, riesgo, orden, fill y resultado → explicación con fuente y nivel de aprendizaje | No inventa razones, altera operaciones ni divulga secretos; contrato D-019 |
| Gobierno y auditoría | Decisión, versión, autorización y resultado → rastro reproducible | Retención, seguridad y revisión D-026/D-027 |

## Qué aporta el video

| Elemento del video | Tratamiento de diseño provisional | Motivo |
|---|---|---|
| Investigación conversacional y dashboards | **Conservar y modificar** | Útiles para investigación y enseñanza, con trazabilidad y datos versionados |
| Conectar agente a fuentes externas | **Conservar y modificar** | Adaptadores de solo lectura, timestamps PIT, controles de calidad y licencia |
| Codex/CLI con acceso directo al broker | **Descartar como frontera de órdenes** | Contradice el invariante `TradeIntent → Risk → Execution → Broker` |
| Automatización, control móvil y alertas | **Conservar y modificar** | Workflow durable, permisos, estados y acciones auditadas; no inferir disponibilidad continua de un cron |
| Trailing stop y compras escalonadas | **Separar** | Son gestión de posición y variante candidata, sujetos a política de riesgo y reglas explícitas |
| Congreso, alertas de terceros, opciones | **Separar** | Fuentes/estrategias distintas; opciones fuera de alcance V1 sin aprobación |
| SIGNAL | **Usar como referencia conceptual** | La hoja requiere controles más concretos de datos, validación, gobierno y aprendizaje |

## Contratos abstractos establecidos y detalle restante — 2026-10-07

1. Responsabilidad/autoridad D-015/ADR-001 A+ establecida; permisos técnicos D-027/B-RT1 propuestos y aceptación target R-030 diferida.
2. Semántica de datos D-014/ADR-004 y admisión abstracta D-018/ADR-005 establecidas; DatasetCards/PIT/licencia/proveedores D-022/033 pendientes por fuente.
3. Interfaz `Signal → TradeIntent → RiskDecision → OrderIntent → BrokerEvent → Reconciliation` D-013/ADR-003 establecida; mapeo concreto broker/órdenes D-021/030 y pruebas pendientes.
4. Separación Research/Champion D-005 establecida; ningún ciclo automático modifica producción sin aprobación.
5. Pedagogía factual desde B4 y contrato completo antes de DoD D-019/ADR-001 establecidos; contratos/evidencia R-006 especificados, evals e integración D-029 pendientes.
6. Alcance A+ D-016 establecido: Champion determinístico, Shadow sin ruta operativa; no exige todas las fuentes en V1. Strategy D-008, fórmulas riesgo D-035 y parámetros D-031 siguen abiertos.

**Gate de R-022:** mapa de responsabilidades, permisos y contratos aceptado; consistencia con D-002, D-005 y DoR; candidatos tecnológicos todavía abiertos.

**D-009/R-019:** extracción funcional completada 2026-10-07; este mapa no declara estrategia, tecnología ni seguridad efectiva seleccionadas. [Dossier](video_inspired_strategy.md).
