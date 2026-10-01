# Assumptions Register — 2026-10-01

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
| A-010 | P0 | Skills/plantillas de terceros pueden usarse legal y técnicamente en Codex; auditoría de licencia/formatos/permisos y probe real de portabilidad. | REFERENCE_ONLY o REJECT; formato similar no basta. |
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
| A-021 | P1 | El Portfolio Manager Agent shadow podrá recibir un contexto elegible comparable al del Champion y producir propuestas reproducibles sin información futura ni efecto operativo. R-026 debe probarlo. | Limitar la comparación a contextos pareados disponibles; corregir aislamiento/evaluación antes del DoD. |
| A-022 | P0 | **REFUTADO como inferencia válida:** la mera visibilidad de un plugin/MCP en documentación o catálogo no implica acceso a datos ni licencia para backtest. Verificar entitlement, costes y probe por dataset. | `AVAILABLE_TO_US` o `ECONOMICALLY_REASONABLE` queda NO/UNKNOWN hasta evidencia; buscar API/fuente alternativa. |
| A-023 | P0 | **UNVERIFIED:** las capacidades de Codex observadas en este chat estarán disponibles para el runtime PAPER V1 con la suscripción Plus del propietario, sin factura adicional ni límite operativo incompatible. Verificar cuenta, límites y modo de ejecución; no inferirlo por visibilidad local. | Rediseñar la arquitectura Tier 0/1 o llevar excepción Tier 2 al propietario con coste/beneficio. |
| A-024 | P0 | **UNVERIFIED:** Sign in with ChatGPT plan usage y Codex app-server pueden operar la carga PAPER V1 dentro del cupo Plus y sus términos. La sesión sondeada informa `planType=team`; documentación/CLI no prueban entitlement Plus ni continuidad desatendida. | Tratar C-025 como `REFERENCE_ONLY` o buscar otra ruta Tier 0/1; no activar API con clave sin excepción ADR-007. |

## Hechos de baseline, no supuestos

La hoja declara el bloqueo de implementación, el invariante financiero, primera operación PAPER y autoridad humana sobre promoción/riesgo/live. Son reglas del proyecto hasta cambio documentado y aprobado; no afirmaciones sobre rendimiento de mercado.

El propietario declaró el 2026-10-01 que **nunca se ejecutaron ni consultaron resultados históricos de MATR_V1 o variantes cercanas**, para 2023–septiembre de 2026 ni para otro período. Esto es un hecho reportado sobre el proceso del proyecto, no evidencia de rendimiento ni garantía de que la futura comparación entre candidatos preserve un holdout.
