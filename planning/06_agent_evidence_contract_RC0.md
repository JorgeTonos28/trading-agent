# Contratos de evidencia y entrega por rol — RC0

**Fecha:** 2026-10-05. **Estado:** propuesta técnica revisable, no arquitectura seleccionada. Paquete autónomo R-006, paso 1; dependencias D-014/019/025/026/027/029/034. Preserva ADR-001 A+, ADR-002 G1+G2 y ADR-006. No implementa Trading OS ni cierra D-020/D-024. Los roles son responsabilidades lógicas, **no** cuatro procesos, subagentes o runtimes obligatorios.

## 1. Entregables y endpoint de este paquete

1. Contrato común, [shadow](06_shadow_portfolio_contract_RC0.md) y [pedagogía](06_pedagogical_contract_RC0.md), con estados y criterios comprobables.
2. [Workload y aceptación](research/R-006_workload_acceptance_RC0.md) para C-010/C-025a y cuatro procedimientos.
3. Regresión focalizada y negativos desechables con resultados conservados; [protocolo wave 06](research/R-006_probe_wave_06_protocol.md).
4. Shortlist revisada y paquete de decisión sobre **arquitectura candidata a aceptación**, sin selección/freeze.

Endpoint: los cuatro entregables completos, consistentes, commit/push; siguiente acción es gobierno de la candidata y acceso Plus. Otros trabajos del Preparation Program conservan su cola; no se declara bloqueado todo el proyecto. Plus no se prueba aquí y revisión independiente/seguridad/stack financiero no se dan por terminados.

## 2. Contrato del caller y autoridad

El caller confiable asigna `job_id`, `attempt_id`, `trusted_role`, `schema_id/version`, `snapshot_id/hash`, `decision_at`, `knowledge_asof`, `requested_at`, `deadline_at`, `comparison_group_id`, política de herramientas y versiones. Son metadatos fuera del contenido generado. Si el modelo los repite deben coincidir exactamente; nunca selecciona su propio validador, rol, deadline o permisos. Role enum: `RESEARCH_IDEA`, `QUANT_REVIEW`, `PORTFOLIO_SHADOW`, `PEDAGOGY`. Todo output de estos roles tiene `authority=NONE`.

| Rol confiable | Output admitido | Exclusiones obligatorias |
|---|---|---|
| RESEARCH_IDEA | Hipótesis, pantalla documentada, fuentes, falsifier, riesgos, siguiente experimento | No propuesta de cartera/TradeIntent, aprobación Champion ni rentabilidad fabricada |
| QUANT_REVIEW | Dictamen de suficiencia, registro train/OOS/costes, límites, protocolo de falsificación | No aprobación/promoción, no peeking holdout, no backtest inventado |
| PORTFOLIO_SHADOW | ShadowPortfolioProposal hipotética long-only dentro de universo del snapshot | No output operativo, endpoint Risk/Execution, escritura de configuración/posiciones/presupuesto |
| PEDAGOGY | Explicación factual, conceptos, pregunta y referencias a trazas | No causa inventada, instrucción de broker, reanudación, recomendación operativa personalizada |

`outputSchema` ayuda a formato; la admisión independiente valida schema por rol confiable, semántica, referencias y cálculos. Un JSON válido no es evidencia de permiso ni de fidelidad factual. Las instrucciones de Skill y anotaciones read-only de MCP no son ACL. Seguridad real y aislamiento de credenciales/canales necesitan D-027 y pruebas de integración antes de PAPER, con gobierno humano. No se selecciona su tecnología en este RC.

## 3. Snapshot y fuentes point-in-time

`EvidenceSnapshot` es inmutable y tiene manifest: IDs/hash, `decision_at`, `knowledge_asof`, versiones dataset/parser/disponibilidad, universo/instrument IDs PIT, calendario/sesión, vista de precio bruto/ajuste as-of, ledger reconciliado de posiciones/cash/reservas/protección, restricciones aprobadas y sus versiones, fuentes/revisiones/licencia/calidad. Una limitación se conserva; no se sustituye un UNKNOWN por cero. El hash se calcula sobre una representación canónica versionada; **no** se asume que serializaciones distintas son iguales. En el probe se usa JSON sort_keys/separadores/UTF-8 sin floats; la convención de producción pertenece a D-026.

Cada observación usa los clocks y `eligible_from` del ADR-004: event, published, source/provider availability cuando aplican, received, validated, effective, precisión/zona y evidencia del canal. Operación capturada: elegibilidad >= recepción/validación/embargo. Replay: evidencia PIT y retraso preregistrado, sin inventar recepción propia histórica. Un dato con disponibilidad UNKNOWN no es señal operable. Las Skills **consumen** el manifest y no recalculan una fecha más favorable.

Un prefilter confiable crea la vista elegible al corte. Para evaluar inyección puede incluir textos no confiables etiquetados; estos no conceden rol/permisos. Observaciones excluidas conservan ID/hash/razón en manifiesto, no se entregan como valores disponibles. Una corrección es nueva revisión con `supersedes`; un backfill no sobrescribe la versión vista antes. Contradicción no resuelta produce incertidumbre/quarantine, no selección silenciosa de la cifra deseada.

### Snapshot pareado

Champion y shadow se comparan solamente si comparten manifest/hash, universo, estado de cartera, corte informativo y restricciones comparables. Instrucciones de rol son distintas y versionadas. La decisión Champion se **oculta al generador shadow** para evitar anclaje; el comparador la une después con el proposal sellado. Un flujo explicativo que muestre Champion no se usa como prueba ciega de utilidad incremental. Si un agente añade fuentes propias no presentes en el contexto Champion, el resultado se etiqueta `UNPAIRED`; puede investigarse separado, no mezcla denominadores.

`decision_at` es el corte de la decisión financiera. `knowledge_asof` es el corte del material entregado: igual a decision_at para shadow/research histórico; para pedagogía posterior puede ser mayor y debe distinguir qué se sabía entonces y qué se supo después. `generated_at/received_at` no adelantan elegibilidad. Un proposal tardío con contexto original aún sirve para análisis PIT retrospectivo, etiquetado `LATE_RETROSPECTIVE_ONLY`; no prueba capacidad de reaccionar a tiempo.

## 4. Evidencia, claims y linaje de cálculo

Cada claim tiene `claim_id`, tipo `OBSERVED / DERIVED / HYPOTHESIS / GENERAL_CONCEPT`, texto, referencias y limitación. Los valores numéricos son decimal string, unidad (`USD`, `SHARE`, `PERCENT_POINT`, `RATIO`, etc.) y moneda cuando aplica. Porcentajes especifican escala; cantidad != notional != exposición != pérdida al stop. OBSERVED referencia campo/ID/revisión del snapshot sin modificación. HYPOTHESIS no se presenta como hecho; GENERAL_CONCEPT cita definición versionada, no se atribuye a una operación sin traza.

DERIVED incluye `derivation_id`, fórmula/versión, input claim IDs, valores/unidades, resultado, regla de redondeo/precisión y verificador. Cálculo preferentemente emitido por software determinístico y explicado por el agente; derivación sugerida por LLM queda no verificada hasta comprobarla. Errores, división por cero, unidad incompatible, input futuro, fórmula desconocida o lineage cíclico invalidan el claim y sus dependientes. No ocultar una derivación dentro de un fact observado.

Ejemplo **sintético, no política**: cash 10000 USD, reservas 400 USD -> disponible 9600 USD por `cash_minus_reservations@toy-1`; 4 shares × 100 USD/share -> 400 USD por `quantity_times_price@toy-1`. No demuestra buying power broker, sizing, límites o riesgo general. Fórmulas de riesgo/concurrencia reales siguen D-035/D-031 y selección de datos/broker.

### Referencias sin ambigüedad

En el contrato final, usar referencias tipadas `{source_id, revision, field_path}`; no una cadena que mezcle nombres de instrumentos, facts o documentos. En el spine desechable RC0 se admiten ID de fuente exacto (`R1`) o referencia `source.field` (`R1.growth`) **solo si ambos existen en el manifest**. No quitar sufijos silenciosamente ni aceptar un prefijo de fuente conocida con campo inventado. Wave 06 reveló que el primer checker asumía source ID puro aunque la tarea solicitaba `R1.growth`; su resultado v1 se conserva como limitación del evaluador, no invención del modelo.

## 5. Tres estados separados

| Eje | Enum / semántica | Responsable |
|---|---|---|
| Ejecución del job | `QUEUED`, `RUNNING`, `SUCCEEDED`, `TOOL_FAILED`, `AUTH_BLOCKED`, `QUOTA_BLOCKED`, `TIMED_OUT`, `NO_OUTPUT`, `CANCELLED` | Caller/runtime observado; modelo no lo decide |
| Contenido | `COMPLETE`, `PARTIAL`, `INSUFFICIENT_EVIDENCE`, `ABSTAIN` | Modelo propone; admisión comprueba consistencia |
| Admisión/entrega | `ACCEPTED_ON_TIME`, `LATE_RETROSPECTIVE_ONLY`, `REJECTED_SCHEMA`, `REJECTED_ROLE`, `REJECTED_PIT`, `REJECTED_LINEAGE`, `REJECTED_AUTHORITY`, `UNPAIRED`, `DUPLICATE` | Verificador independiente |

El estado financiero (`NORMAL`, pausa material, reconciliación, etc.) viene del ledger aprobado ADR-002/003, en namespace separado; `SUCCEEDED` no significa incidente resuelto. TOOL_FAILED puede tener salida válida INSUFFICIENT_EVIDENCE; NO_OUTPUT significa ningún JSON final aceptable, nunca HOLD ni abstención voluntaria. Timeout con respuesta tardía se conserva como observación tardía, sin volver el job on-time. Proposal completo != autorización financiera.

## 6. Persistencia, idempotencia y recovery propuestos

Persistir manifest/solicitud antes de invocar, conservar output bruto **solo** sintético/sanitizado o con política de privacidad aprobada, tool receipts, admisión/errores, modelo/cliente/Skill/prompt/schema/contrato/config hashes y tiempos/latencia. No conservar chain-of-thought ni tokens/secretos. Audit facts explican decisiones; no son razonamiento interno privado del modelo.

`job_id` identifica la tarea lógica; `attempt_id` cada intento. Propuesta/claim IDs son locales al job y nunca order IDs. Admitir a lo sumo un resultado final por job según regla determinística versionada (primer resultado válido recibido; revisión explícita es nuevo job superseding). Intentos adicionales se auditan como duplicados/conflictos. Un content hash compartido entre jobs no autoriza deduplicar eventos económicos distintos.

Recovery rehidrata **el mismo** manifest/contrato, conserva histórico de entregas y etiqueta el intento; no refresca datos silenciosamente. Retry máximo preregistrado por clase/fallo; en wave 06 son hasta dos lecturas sintéticas, no una política de producción. Nunca reenvía orden ni modifica el Champion. Auth/quota inaccesible: registrar causa sanitizada, no cambiar a API paga/otra cuenta, no loops ilimitados. Retención, durable workflow, backup/restore y cuota siguen D-025/026 y Plus Gate; esta especificación no prueba recuperación real.

## 7. Fallos y obligación funcional

- Fallo agéntico aislado: guardar evidencia, estado, backlog y cobertura perdida; explicación factual determinística puede conservar hechos pero no sustituye el Pedagogical Agent completo ni producción shadow. Reintento/recuperación bajo política acotada.
- Faltante financiero obligatorio, inconsistencia material/hard limit/protección: G1+G2 y autorización humana para reanudar; nunca degradar el control por falta de LLM.
- Shadow/pedagogía persistentemente incompletos: capacidad PAPER degradada, incumple su gate/DoD. La duración tolerable, escalamiento y efecto operacional se deben aprobar con Strategy V1/workload/runbooks; no aprobar aquí una excepción permanente.

## 8. Verificación y límites de este RC

Schemas y pruebas bajo [probe de contratos](research/probes/r006-contracts/) son **experimentos de planificación**: demuestran discriminación en fixtures, no motor financiero, aislamiento OS ni ruta broker. Reutilizan `jsonschema` y `decimal`, sin construir framework/validator propios de producción. Negativos: rol del contenido, enums localizados, intent inesperado, override de modo, input futuro, derivación equivocada, unidad errónea, qty ambigua, contexto distinto, tardío/no-output/duplicado. La wave 06 prueba regresión focalizada de los procedimientos con contratos explícitos. R-006 madura para una propuesta condicionada; D-020/D-024 permanecen abiertos.
