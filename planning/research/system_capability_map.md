# R-022 — Mapa funcional del Trading OS (RC0)

**Fecha:** 2026-10-01. **Estado:** mapa completado; [contrato PAPER V1 RC1](../paper_v1_capability_contract_RC1.md) y ADR-001 aprueban A+ para D-015/016/019; D-018 sigue en investigación. **Prioridad:** P0. **Decisiones:** D-015, D-016, D-018, D-019. Este mapa convierte la inspiración del video y la [hoja v0.2](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md) en requisitos de **nuestro** sistema. No fija stack, broker ni Strategy V1; no autoriza implementación.

## Capacidades y fronteras

| Capacidad | Entrada → salida verificable | Frontera/decisión aún abierta |
|---|---|---|
| Descubrimiento e investigación | Fuentes/hipótesis → dossier con origen, timestamps, limitaciones y experimento | Research Agents solo lectura; no promueven Champion ni alteran riesgo |
| Ingestión y normalización | Market/alternative data → snapshots versionados con `event_at`, `published_at`, `received_at`, `available_at` cuando apliquen | Proveedor y contrato PIT D-014/D-033; calidad y licencias |
| Strategy Lab y backtest | Hipótesis versionada → reglas falsables, replay, OOS y comparadores | Selección D-008; motor D-023; acceso al holdout |
| Signal Engine | Datos elegibles + reglas Champion → señal rastreable | Agente vs lógica determinística; autoridad D-015 |
| Portfolio/intent | Señal + cartera reconciliada → `TradeIntent` operativo versionado, ensamblado determinísticamente | Reglas exactas de sizing/prioridad D-012/013; un Champion puede combinar señales |
| Portfolio Manager shadow | Mismo contexto elegible cuando corresponda → `ShadowPortfolioProposal` auditada | Sin ruta a `TradeIntent`/Execution; detalle y evaluación PIT D-034 |
| Risk Engine | Intent + estado + presupuesto → aprobar/reducir/rechazar con motivo | **Determinístico**; precedencia y kill switch D-012/D-017 |
| Execution/Broker adapter | Autorización válida → órdenes, eventos, fills, reconciliación | Broker D-021; idempotencia/recuperación D-013; sin acceso directo del LLM |
| Monitorización | Datos, posiciones, órdenes, salud y desempeño → alerta/acción definida | SLO, runbooks y autoridad de suspensión D-017/D-028 |
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

## Contratos P0 a definir antes de elegir stack

1. Diagrama de responsabilidad y permisos por agente/componente; quién propone, quién decide y quién ejecuta.
2. Contrato de evento/dato PIT compartido para mercado, SEC, Congreso, opciones, flujos, revisiones de analistas y alertas.
3. Interfaz `Signal → TradeIntent → RiskDecision → OrderIntent → BrokerEvent → Reconciliation`, con errores y estados.
4. Separación entre aprendizaje de **investigación** y cambio de **Champion**: ningún ciclo automático modifica producción sin aprobación.
5. Contrato pedagógico: explicación basada en rastro real, incertidumbre explícita, fuentes/timestamps y material progresivo vinculado a operaciones o experimentos (§55).
6. Alcance PAPER V1 mínimo frente a capacidades futuras. La plataforma debe poder investigar nuevas fuentes sin exigir que todas alimenten la primera estrategia.

**Gate de R-022:** mapa de responsabilidades, permisos y contratos aceptado; consistencia con D-002, D-005 y DoR; candidatos tecnológicos todavía abiertos.
