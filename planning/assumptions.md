# Assumptions Register — 2026-10-01

**Estado vigente posterior — wave07:** [RC2 Team](research/R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

**Vigencia actual — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Las hipótesis siguientes **no** son decisiones aprobadas. Su posible falsedad tiene que evaluarse antes del gate señalado. Estado inicial `UNVERIFIED`, salvo filas marcadas `REFUTADO`.

| ID | P | Supuesto / prueba de falsación | Impacto si es falso |
|---|---|---|---|
| A-001 | P0 | MATR_V1 puede especificarse sin optimización retrospectiva y ejecutarse a frecuencia diaria **si resulta seleccionada**; preregistro + replay. | Rediseñar el candidato o descartarlo en Strategy V1 Selection. |
| A-002 | P0 | La división 2005–2018 / 2019–2022 / 2023–2026 puede servir como protocolo OOS tras seleccionar entre candidatos; preregistrar comparación. El propietario confirma cero backtests de MATR_V1 consultados hasta 2026-10-01. | Nueva política OOS/forward si la comparación contamina el período. |
| A-003 | P0 | Close/SMA/ROC/ATR pueden calcularse con una única convención consistente de ajustes y disponibilidad; comparar data vendors. | Cambian señales/resultados. |
| A-004 | P0 | **REFUTADO:** un stop `3×ATR20` no garantiza pérdida ≤ budget 0.5%; gaps/overnight/fills pueden excederla. ADR-006 trata stop-risk como estimación y añade escenarios independientes. | D-035/031 aún deben definir fórmulas y escenarios; no presentar stop como límite real garantizado. |
| A-005 | P0 | Se puede proteger cada orden con autorización/versión verificable sin crear carrera entre risk y execution; prototipo de secuencia. | Rediseño de contratos. |
| A-006 | P1 | Un residente de RD con el perfil concreto del propietario puede obtener paper API y, después, live donde corresponda; confirmación oficial. | Candidato broker inviable. |
| A-007 | P1 | Históricos de ETFs 2005–2026 con timestamps, ajustes y derechos de uso son obtenibles dentro de presupuesto; muestras y cotización. | Cambia dataset/ventana/coste. |
| A-008 | P1 | Un motor reutilizable puede representar estrategia, órdenes y stops con fidelidad suficiente; benchmark. | BUILD/ADAPT más costoso. |
| A-009 | P0 | **SUPERSEDED por ADR-007:** que Agents SDK/Temporal y stack Python reduzcan complejidad no justifica su selección. Agents SDK/API son referencia Tier 2; Temporal pertenece a infraestructura R-011, no al comparativo agéntico R-006. | Evaluar rutas Codex/Skills y contenido Anthropic Tier 0/1 antes de D-024; el stack sigue abierto. |
| A-010 | P0 | Skills/plantillas de terceros pueden usarse legal y técnicamente en Codex; auditoría de licencia/formatos/permisos y probe real de portabilidad. | REFERENCE_ONLY o REJECT; formato similar no basta. Wave 04 probó activación de adaptaciones concretas en Team; no licencia/activación Plus de bundles propietarios. |
| A-011 | P1 | Dos fuentes permiten detectar errores materiales sin discrepancias irreconciliables; cross-check. | Más controles o cambio proveedor. |
| A-012 | P2 | Paper fills representan suficientemente la mecánica requerida para validar ejecución; shadow quotes y gap analysis. | Mayor fase shadow/limitaciones. |
| A-013 | P2 | Los límites PAPER 25%/0.5%/2% y soft/hard son coherentes con volatilidad y gaps; stress. | Recalibración humana. |
| A-014 | P3 | Resultados paper y shadow pueden transferirse parcialmente a capital live; análisis execution gap. | Live se aplaza. |
| A-015 | P4 | Alguna familia Smart Money/alternative data aporta señal post-publicación neta de costes; estudio incremental por candidato, después de factibilidad PIT. | Puede usarse solo para research/pedagogía o descartarse como señal. |
| A-016 | P0 | **REFUTADO por la transcripción primaria:** el video presenta varios componentes y estrategias distintas, sin una especificación única reproducible. | Tratar VID-TS, VID-CONG, VID-ALERT y VID-WHEEL por separado; no ensamblarlos implícitamente. |
| A-017 | P0 | El enfoque del video puede cumplir restricciones PAPER V1 sin opciones ni autoridad directa de LLM sobre broker; mapa de componentes y permisos. | Solo reutilizar workflow/metodología o exigir cambio de alcance humano. |
| A-018 | P0 | Una variante de copy trading congresual o de alertas puede reconstruirse con tiempo de publicación/recepción y universo histórico suficientes. R-021 debe intentar falsarlo antes de backtest. | Diferir la variante V1 aunque el tutorial muestre dashboards atractivos. |
| A-019 | P0 | Una interfaz común puede representar fuentes externas heterogéneas sin borrar su fecha real de disponibilidad, revisiones y nivel de confianza. R-023/004 prueban semántica. | Contratos por familia y adaptación del diseño de datos. |
| A-020 | P1 | Uno o varios proveedores especializados permitirán cubrir señales externas con derechos y coste razonables. R-025 compara contra fuentes oficiales. | Reducir alcance de fuentes V1 o construir normalización propia. |
| A-021 | P1 | PARTIAL solo fixtures: shadow con contexto versionado y canonización/derivación verificadas; no prueba cartera general/reproducibilidad generativa/aislamiento real. RC0 exige Champion oculto y distingue decisiones desde cartera real vs trayectoria contrafactual. | Parear solo hashes/contextos iguales; métricas/sealed outcomes y engine/seguridad R-026 antes DoD. |
| A-022 | P0 | **REFUTADO como inferencia válida:** la mera visibilidad de un plugin/MCP en documentación o catálogo no implica acceso a datos ni licencia para backtest. Verificar entitlement, costes y probe por dataset. | `AVAILABLE_IN_TARGET_PLUS` o `ECONOMICALLY_REASONABLE` queda NO/UNKNOWN hasta evidencia; buscar API/fuente alternativa. |
| A-023 | P3 | SUPERSEDED para PAPER por ADR-010: transferencia Team→Plus pasa a hipótesis PRE-LIVE P3, no disponibilidad PAPER. | Medir gates Team por etapa o R-029 PRE-LIVE; no gasto ni rebaja silenciosa de obligaciones. |
| A-024 | P1 | UNVERIFIED: native Codex en Team soporta demanda PAPER sostenida y recovery; identidad/acceso/probes no prueban cuotas/continuidad. | Medir gates Team por etapa o R-029 PRE-LIVE; no gasto ni rebaja silenciosa de obligaciones. |
| A-025 | P0 | **UNVERIFIED:** una ruta zero/low incremental cost puede cumplir los requisitos de calidad/fiabilidad PAPER V1. Probar capacidades, datos, límites y recovery; gratis no es evidencia de suficiencia. | Documentar brecha y opciones pagas revisables; no reducir silenciosamente gates ni comprar sin aprobación ADR-008. |
| A-026 | P0 | **PARTIAL:** wave 04 muestra valor cualitativo de procedimiento/pedagogía y más contexto; mínimo 10/10 checks vs Skill 9/10. No se demostró superioridad general ni fiabilidad. | Shortlist condicional; canonizar outputs/linaje y conservar baseline. Ver research/R-006_probe_wave_04_2026-10-05.md. |
| A-027 | P1 | **HYPOTHESIS:** el núcleo determinístico puede operar autónomamente con Codex intermitente. No equivale a continuidad probada ni runtime seleccionado. | Evaluar dependencias operativas, cadencia, estado/recovery y degradación en D-024/025; Team TP por etapa; Plus PRE-LIVE. |
| A-028 | P1 | UNVERIFIED: WL-R propuesto 40/63 jobs y deadlines son representativos/sostenibles en Team; benchmark acotado no sustituye multi-sesión/Strategy V1. | Medir gates Team por etapa o R-029 PRE-LIVE; no gasto ni rebaja silenciosa de obligaciones. |
| A-029 | P1 | **PARTIAL:** Codex SDK Python oficial puede reemplazar transporte propio; un smoke Team 7/7 y auth/schema compatibles, sin tool callbacks/full Skills/state/recovery probados. | SDK si cubre job contract; gap documentado justifica raw app-server/otra integración Tier 0/1, no construir por defecto. |

| A-030 | P1 | UNVERIFIED: abrir un paquete como cwd conserva automáticamente reglas raíz y Skills compartidas en todas las superficies/versiones. Documentación establece condiciones Git root/cwd/override y límite; R-028 lo prueba. | Verificar cadena/activación; entry point explicita raíz y contratos cuando discovery falla. No confundir instrucciones con ACL. |
| A-031 | P1 | UNVERIFIED: un clone y los assets públicos bastan para reproducir el entorno, aunque auth, dependencias, plugins, MCP y cuotas son externos. | Manifest/perfil/deltas y gates separados; fresh clone Team no transfiere auth ni prueba continuidad; Plus PRE-LIVE por separado. |
| A-032 | P1 | UNVERIFIED: el perfil acotado Team mantiene continuidad/cuota/auth y calidad en workload PAPER definitivo. Wave07 8/8 no prueba operación sostenida ni igualdad generativa. | P1 protocolo/política de versión; P2 carga/recovery/auth y regresión reales, sin gasto ni bajar obligaciones. |

## Hechos de baseline, no supuestos

La hoja declara el bloqueo de implementación, el invariante financiero, primera operación PAPER y autoridad humana sobre promoción/riesgo/live. Son reglas del proyecto hasta cambio documentado y aprobado; no afirmaciones sobre rendimiento de mercado.

El propietario declaró el 2026-10-01 que **nunca se ejecutaron ni consultaron resultados históricos de MATR_V1 o variantes cercanas**, para 2023–septiembre de 2026 ni para otro período. Esto es un hecho reportado sobre el proceso del proyecto, no evidencia de rendimiento ni garantía de que la futura comparación entre candidatos preserve un holdout.

**A-030 actualizado R-028:** PARTIAL — CLI Team probó root+rol y Skill en fixture, metadata y cinco respuestas; carpeta aislada no hereda. No generalizar a cada superficie/config/Plus; fresh clone real y target quedan pendientes. A-031 sigue parcial: assets versionados se transportan, auth/servicios externos no.

**A-030/031 tras fresh clone:** CLI app-server confirmó seis cadenas raíz+rol y Skill común; dos roles respondieron invariantes. Assets Git portables comprobados, con 31 cambios EOL del checkout; auth/localtools siguen prerequisitos externos. Desktop UI/SDK directo y Plus no demostrados. No tratar raw worktree hash como identidad portable.

## Supuestos adicionales P1 — hardening

| A-033 | P1 | UNVERIFIED: identidades/ACL/IPC/egress Windows por dominio pueden aislar todo SDK/app-server/handlers y mantener Team login legítimo sin filtrar Champion/holdout/secrets. | S2 propuesta ADR-012; aprobación y probe empírico antes de freeze. Native sandbox de comandos no demuestra proceso completo. |
| A-034 | P1 | PARTIAL: SDK/CLI0.160 publicado emparejado soporta roles/Skills/tools necesarios. | H4 2/2 research/shadow correctos, no todos los roles/requests/OS ni cuota sostenida; pin final abierto. |
| A-035 | P1 | UNVERIFIED: prioridad y una cola no preemptiva bastan para demanda PAPER. | H3 virtual muestra fallos de deadline en burst/carga amplificada; no seleccionar concurrencia por promedio ni falsificar capacidad nativa. |

| A-036 | P1 | UNVERIFIED: acceso gratuito a filings SEC permite reconstruir precisión PIT necesaria para una Strategy V1 aún no definida. | SEC documenta no timestamp first-available; DatasetCard R-020 exige canal/historia/método de disponibilidad y no confundir acceptance con receipt. No dataset descargado ni API probe. |
