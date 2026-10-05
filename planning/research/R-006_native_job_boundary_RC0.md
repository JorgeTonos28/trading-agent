# Contrato candidato — jobs Codex Team fuera del núcleo financiero

2026-10-05. Dirección ADR-011 A aprobada; detalles D-024 siguen candidatos, sin implementación. Detalla A+/G1+G2 sin ampliar autoridad. [Team acceptance](R-006_team_runtime_acceptance_RC0.md), contratos comunes/shadow/pedagogía y ADR-010 gobiernan.

## 1. Responsabilidades

Núcleo local determinístico: Champion aprobado, contexto de decisión versionado, señales/TradeIntent, riesgo, ejecución/reconciliación y estado financiero. Caller de jobs: seleccionar rol/procedimiento/versión/schema/tools, snapshot y plazo; registrar intentos y validar recepción/admission. Codex: generar investigación, revisión quant, propuestas shadow o explicación factual usando solo contexto y herramientas autorizados. Outputs nunca son autorizaciones financieras.

El caller es software determinístico; no un Portfolio Manager LLM con capacidad de dirigir herramientas del núcleo. Orquestación inicial candidata: roles lógicos en una cola acotada; sesiones efímeras por job, sin obligación de un proyecto/proceso independiente por rol ni delegación recursiva. Concurrencia se justifica con evidencia de carga si hace falta; no se elige aquí motor de workflow, storage o scheduler.

## 2. Manifest confiable por job

Campos mínimos propuestos: job_id lógico, attempt_id, trusted_role enum, repository release/commit, package/procedure/contract/schema/client/runtime versions y hashes, snapshot_id/hash, decision_at/knowledge_asof, family/parent_job_id cuando aplique, arrival_at/deadline, tool allowlist+límites, expected output class, admission version, environment fingerprint y authority=NONE. El caller fija estos valores; contenido externo ni output del LLM puede cambiarlos.

Conservar snapshot entregado y exclusiones PIT; shadow recibe el contexto pareado pertinente sin decisión Champion visible antes de sellar su propuesta. Ausencia de datos/confianza/calibración no se convierte en un hecho. El LLM no decide corte, rol, schema, permisos, retries ilimitados o fallback pago.

## 3. Transporte y herramientas

Preferir SDK Codex oficial cuando cubra contrato. Cliente tipado bajo nivel permite probar callbacks; high-level y protocolo raw son alternativas dentro de una familia, no runtimes obligatorios simultáneos. Dynamic tools son API experimental: pin y regression en upgrade; no prometer estabilidad de interfaz por ser oficial. No construir cliente RPC propio salvo gap concreto documentado.

Native login oficial Team; no exportar tokens ni usar endpoints privados. API de modelos facturada es alternativa diferente, Tier 2 no habilitado por defecto. Sin fallback automático a modelo/proveedor/billing. Para shadow/pedagogía, tools concretas read-only de snapshot/trace; para research/quant, permisos adicionales futuros requieren contrato/aislamiento y gobierno, no heredar shell libre del Plan Architect.

**SDK guard:** nunca usar default approval handler para estos jobs. Denegar comandos/file changes/escalación y cualquier método no reconocido; implementaciones finales deben responder con la denegación válida de cada método o cerrar el job fail-closed. Un objeto genérico inválido no es un contrato de denegación completo. Los probes actuales solo prueban tools sintéticas y rechazo offline, no todas las clases de server requests. Verificar permiso efectivo antes de inference.

## 4. Recuperación sin chat

Repo/release + manifest + snapshot + tool trace + output/admission son fuente de verdad. Rehidratación tras reiniciar un cliente reconstruye el contexto explícito en nueva sesión efímera; chat/model reasoning no son el estado durable del sistema. Native thread resume puede mejorar continuidad futura, pero no es requisito para reconstruir el estado financiero ni evidencia única.

Estados de transporte/admission: QUEUED, RUNNING, COMPLETED, FAILED_TOOL, FAILED_RUNTIME, TIMEOUT, NO_OUTPUT, REJECTED, ACCEPTED_ON_TIME, LATE_RETROSPECTIVE_ONLY, DUPLICATE. `content_status` COMPLETE/PARTIAL/ABSTAIN/INSUFFICIENT_EVIDENCE es eje distinto. Guardar cada intento; máximo una recepción admisible por job lógico, con política determinística de elección/retry definida D-025/026. El replay de admisión es determinístico; output generativo puede variar y no debe llamarse reproducible en sentido numérico fuerte sin evidencia.

Los nombres anteriores de transporte no sustituyen estados canónicos de evidence: aplicar mapping/version [delivery-contract-v2](../08_job_workflow_recovery_contract_RC0.md). Dispatch/envelope del intento/lease/tool receipts/admission incluyen `environment_incarnation_id` confiable distinto de config fingerprint, preservando manifest y job_id lógico originales. Tras restore nuevo epoch invalida nuevas recepciones de workers antiguos, no outputs históricos ya admitidos. Elegir output requiere current attempt/owner/generation/expiry/lifecycle y epoch vigentes en la misma transacción externa.

Una propuesta shadow tardía sirve para análisis retrospectivo identificado y sin contaminación de comparación on-time. Silencio/fallo no es HOLD. Pedagogía no inventa causas/outcomes; pending/missing reports quedan contabilizados. El agente que termina no reanuda una pausa financiera material; G1+G2 requiere autorización humana conforme ADR-002.

## 5. Degradación y separación de autoridad

Agente ausente/cuota/fallo: núcleo financiero sigue sus reglas determinísticas aprobadas y políticas de salud de inputs/riesgo; no depende de aprobación LLM operación por operación. Si datos/protección/estado financiero tienen incertidumbre material, A+/G1+G2 gobierna la pausa/reconciliación. No convertir una falla educativa en señal de salida ni usar riesgo financiero para ocultar incumplimiento de shadow/pedagogía. Fallos persistentes impiden aceptación funcional PAPER hasta corregirlos.

Outputs research/quant/shadow/pedagogy van a namespaces sin interfaz de TradeIntent operativo ni configuración Champion/riesgo. No basta `authority=NONE` en JSON: la implementación debe impedir acceso técnico y validar desde caller externo. No exposición de broker credentials, broker SDK endpoints, control sockets, storage writes financieros ni permisos de promotion.

## 6. Gaps de seguridad y operación antes de cierre final

- Definir/testear identidad del proceso, filesystem/network isolation y almacén de secretos D-027. Sandbox read-only no demuestra por sí solo ausencia de lectura de secretos fuera del cwd ni frontera entre procesos bajo el mismo usuario Windows.
- Revisar config efectiva, hooks/trust, plugins/MCP/apps heredados y version drift; una allowlist declarada no demuestra todos los caminos del host.
- Denegación tipada de toda solicitud/escalación y aislamiento/red team en integración real, incluido intento de escribir/controlar núcleo financiero.
- Workflow/storage durable, interrupción/retry/quota/expiry/recovery y backup/restoration D-025/026/028, con pruebas P1 de diseño y P2 operacionales.
- Demanda definitiva Strategy V1 y carga sostenida; ventana real de cuotas y uso compartido Team. No validar con extrapolación de tokens ni burst único.
- Revisión crítica independiente y gobierno antes de freeze. Este análisis es del Plan Architect; no presenta auto-review como independiente.

Las metodologías/contratos existen y son reutilizables; estas integraciones son ajustes locales candidatos WRAP/ADAPT cuya construcción permanece bloqueada hasta DoR. Ninguna nueva autoridad, gasto, broker o estrategia seleccionados.

## 7. Automatización aprobada ADR-011

Triggers de eventos/calendario son reglas versionadas del caller determinístico. Jobs rutinarios aprobados no requieren intervención por invocación. Fallo agéntico no genera decisión financiera por defecto. Contrato de cada dependencia estratégica obligatoria debe identificar datos faltantes/timeout/late y decisión determinística admisible de fallo; aún no hay Strategy V1 seleccionada.
