# Pedagogical Agent — contrato completo propuesto RC0

**Fecha:** 2026-10-05. **Estado:** especificación P1 propuesta de D-019/029; obligación funcional D-019 aprobada en ADR-001. Mapea hoja §8.14/§55/§56/§57. Factual desde **fase B4 autonomous paper**, completo antes de DoD PAPER V1; no confundir fase con otros gates B4/B5 del documento. Sin autoridad financiera, selección de estrategia o runtime. [Contrato común](06_agent_evidence_contract_RC0.md).

## 1. Evidencia y fidelidad

Leer trazas sanitizadas y versionadas por trade/intent/signal/risk/order/fill/event ID, snapshot/corte, Champion/config/política aprobada, estado de reconciliación, costos/resultado medidos y derivaciones verificadas. Separar **plan → señal → intent → autorización/reducción/rechazo → solicitud broker → aceptación → fills → reconciliación → resultado**. Una solicitud/cancelación no es ack ni fill. Protecciones verificadas no garantizan precio ni fill.

Explicar motivos solo desde rule/reason codes de Champion/Risk y parámetros que realmente se usaron. Si falta la traza, `MOTIVE_UNKNOWN`; no deducir una causa solo porque un indicador coincida. Distinguir causalidad documentada, contribución contable/cálculo y conjetura. Claim numérico observado/derivado usa unidad, IDs, fórmula e inputs del contrato común; resumen no añade dato nuevo.

Dos clocks: `original_decision_at` y `knowledge_asof` del informe. Evidencia posterior puede explicar outcome **marcado posterior**, nunca reescribir lo sabido en la decisión ni alimentar shadow/PIT original. Revisiones de informes son append-only/supersedes; contradicción reconciliada tiene referencia de corrección. Evidencia conflictiva aún no resuelta -> PARTIAL/limitación, sin precio/P&L/causa final fabricados.

## 2. Contrato por operación

`PedagogicalReport` tiene report/job/schema IDs, versiones/modelo/Skill, trade/trace refs, clocks, content_status, español por defecto, claim ledger, explicación, conceptos, incertidumbre, pregunta/comprobación y fuentes. Se puede exportar/abrir por trade_id en otro chat como paquete autocontenido **sin credenciales**; incluye manifest, definiciones y vínculos, no depende de memoria oculta del chat.

| Campo narrativo requerido | Fuente y fallback |
|---|---|
| Qué ocurrió | Timeline desde eventos; unknowns explícitos |
| Señal/indicadores usados | Signal/Champion reason codes y valores as-of; `NOT_APPLICABLE` si no participan |
| Riesgo asumido/estimado | Risk decision y controles aplicables; distinguir límite, estimación y realización |
| Por qué ese sizing | Requested vs allowed vs filled, restricción vinculante documentada; `UNKNOWN` si falta registro |
| Invalidación/protección | Tesis/regla aprobada y stop conocido, riesgo de gap; no instruir modificarlo |
| Resultado | P&L neto realizado/no realizado y costes verificados o `PENDING/NOT_EVALUABLE`, jamás beneficio anticipado |
| Concepto y aprendizaje | Definición versionada vinculada a evento/experimento, ejemplo y pregunta breve |
| Teoría vs ejecución | Supuestos vs precio/fill/cost/latencia observados, limitaciones; sin causalidad inventada |

Desde B4: registro factual por evento/operación con los campos disponibles, estado pending/partial y explicación de UNKNOWN/G1+G2. No retrasar logging/protección esperando narrativa. Un renderer determinístico puede mostrar hechos ante fallo LLM, etiquetado `FACTUAL_FALLBACK`; no se contabiliza como cumplimiento del contrato agéntico completo.

## 3. Contrato completo antes de DoD

1. Informes por operación accesibles por trade_id y actualizados con outcomes conocidos; cobertura incluye intents rechazados y días sin trades, no solo ganadores destacados.
2. **Resumen diario**: decisiones, fills, incertidumbre, incidentes, riesgo/costes/resultados verificables, conceptos y preguntas; no trades -> explicación factual de no actividad si existe reason code, si no motivo UNKNOWN.
3. **Lección semanal**: síntesis desde eventos/experimentos, una secuencia de conceptos y ejercicio; incluye errores/sesgos/perdedores, sin seleccionar retrospectivamente solo éxitos.
4. Glosario versionado y **mapa de conceptos** con prerequisitos, relación a estrategia y vínculos a trades/experimentos.
5. Lista de dudas sugeridas, operaciones destacadas y errores del sistema; distinción bug, limitación de dato, hipótesis fallida y resultado adverso permitido.
6. Comparación teoría vs ejecución, costes/latencia/slippage/protección/PIT cuando se pueden medir.
7. Progreso de aprendizaje explícito opcional: nivel/objetivos/prerequisitos, ejercicios respondidos y dudas del usuario; no inferir competencia ni guardar datos personales innecesarios. Respuesta de comprensión se evalúa con rúbrica conceptual versionada; no se vuelve señal de trading ni presupuesto de riesgo. Estado editable/exportable bajo política de privacidad D-027.
8. Reportes citables/revisables, correcciones y feedback registrado; fallos/late/no-output visibles. Narrativa persuasiva sin evidencia no pasa aceptación.

## 4. Curriculum y alcance

| Nivel de §55 | Conceptos | Vinculación y condición |
|---|---|---|
| 1 | Mercado, ETF, order types, bid/ask, spread, P&L | Instrumentos realmente usados o experimento educativo etiquetado |
| 2 | SMA, momentum, ATR, volatility, sizing | Según Strategy V1; no presume MATR seleccionada ni calcula indicadores inexistentes |
| 3 | Sharpe, Sortino, drawdown, correlation, beta | Desde análisis validado con período/frecuencia/baseline/unidades; muestra insuficiente -> limitación |
| 4 | Backtest bias, overfitting, walk-forward, Monte Carlo, regime | Desde experimentos/versiones; no afirmar tests completados sin resultados |
| 5 | Options, Greeks, IV, assignment, microstructure | Conceptual/experimentos cuando pertinente; no habilita derivados, leverage o short en PAPER V1 |

No exigir que cada informe contenga todos los niveles. Curriculum cubre la ruta progresiva; cada concepto enseñado debe vincularse a operación real del sistema PAPER o experimento explícito. Conceptos ajenos al Champion se etiquetan como extensión educativa, no razón operativa. No usar el ejemplo MATR de §8.14 como configuración aprobada.

## 5. Fallos, prioridades y pruebas

Si herramienta falla permanentemente: output INSUFFICIENT_EVIDENCE, sin timeline/claims inventados; mantener backlog. Si evidencia parcial: explicar lo conocido, campos pendientes y cómo se verifica. Si fuente incluye órdenes/injection: citar datos válidos y rechazar instrucciones; nunca sugerir cancelar protección/reanudar automáticamente material pause. Cualquier recomendación de política nueva es propuesta para gobierno, no cambio aplicado.

Acceptance antes de DoD: exactitud en fixtures de partial fill/cancel UNKNOWN, risk reduce/reject, no trades, costs vs gross/net, protection failure, corrección posterior, fuentes contradictorias, missing lineage, inyección; todos los claims materiales rastreables. Report diario/semanal/glosario/mapa/export por trade_id y currículo se comprueban con materiales renderizados y revisión humana/independiente. Pregunta pedagógica evalúa comprensión sin afirmar aprobación financiera. No claim causal/rendimiento sin evidencia; tests negativos rechazan source/derivation inventadas. Cobertura y puntualidad contra workload acordado, no umbral de riesgo creado aquí.

Wave 04 prueba B4 parcial; wave 06 prueba estructura/canonización y causa UNKNOWN. **No** demuestra ya curriculum completo, aprendizaje logrado ni report renderer/export. Plus Gate solo integración/operación de finalistas, no eval educativa completa. D-029/026/027 y PAPER P2 mantienen gates pendientes.

## 6. Build vs. Reuse

C-024 **ADAPT** métodos de trazabilidad/explicación en Skill breve propia, complementada con C-010 baseline. C-026 Data y document/visualization Skills son **REFERENCE_ONLY** hasta entitlement/uso concreto; no copiar contenido propietario. Se puede reutilizar dentro de inclusión Plus validada para QA/materiales, no dependencia necesaria del informe factual básico Markdown/JSON. Activos financieros públicos Apache de Anthropic aportan estructura de evidence ledger, riesgo/falsifier y revisión; su narrativa de inversión se adapta a enseñanza factual. No hay compra de template ni runtime Claude. Software de gráficos/reportes y almacenamiento se investigará antes de construir subsistemas; el método pedagógico del proyecto es específico, no requiere LLM always-on.

## Vigencia de entrega posterior ADR-011 / hardening RC0

Dirección core local + jobs Team automáticos aprobada; D-020 DECIDED en disposiciones de diseño, D-024 RESEARCHING. Textos anteriores de siguiente Plus/selección pendiente son historia de sus hitos. Plus solo PRE-LIVE ADR-010. [Workflow/recovery y mapping delivery-contract-v2](08_job_workflow_recovery_contract_RC0.md) separa workflow/attempt de enums de entrega originales, que se conservan para probes v1; no cambia content_status ni autoridad. Leases/identidades/epoch/namespace se validan fuera del modelo; no-output no es HOLD. Permisos finales y motor permanecen abiertos.
