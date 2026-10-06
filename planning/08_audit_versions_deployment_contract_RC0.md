# 08 — storage, audit, versiones y deployment RC0

2026-10-05. D-026/D-028/R-012/014 **RESEARCHING**; R-010/D-024 abierto. Contratos candidatos, no schemas/runtime productivos.

## 1. Stores y límites

Conservar cuatro clases vinculadas por IDs: (a) estado/eventos/commands financieros reconciliables ADR-003; (b) raw observations/revisiones y snapshots PIT ADR-004; (c) job/attempts/leases/tool traces/raw outputs/veredictos; (d) derivados analíticos/educativos. Core es única fuente financiera; proposals/explicaciones no escriben eventos de órdenes. Jobs no reciben credenciales SQL/DB, access paths financieros ni locks compartidos del execution engine.

Storage baseline a investigar: PostgreSQL transaccional, Parquet lake, DuckDB análisis, Redis cache/locks. No sustituirlo silenciosamente por SQLite del probe. Para writes de commands/recepción/leases exigir commit durable; un Redis cache/lock no es ledger autoritativo ni fencing sin validación en store. PostgreSQL synchronous commit conserva confirmación hasta WAL durable; ajustes async cambian garantía. [PostgreSQL WAL](https://www.postgresql.org/docs/current/wal-async-commit.html). Redis tiene modos con trade-offs de pérdida: [persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/).

Parquet/DuckDB son vistas de investigación, no verdad de posición/orden; licencias, versión, PIT y conteos de export trazables. Redis no entra como obligatorio antes de demostrar necesidad; eliminarlo del baseline requeriría change record. SQL/artefactos y sus permissions deben ser probados con motor final antes de cerrar D-026; actualmente no hay PostgreSQL/Redis ejecutable detectado en PATH (no concluye que ningún servicio exista).

## 2. Evidencia durable

Cada registro conserva job/attempt/event/parent IDs; trusted role y authority NONE; release/commit/package/procedure/schema/admission/runtime/client/model IDs; snapshot/cutoff/hash/exclusiones; trigger/deadline/arrival/start/receive/admission clocks; lease-generation; tool nombre/args validados/hash del resultado; raw output/hash y estado/errores sanitizados; identidad del componente confiable. No almacenar reasoning privado ni tokens. Auth/quota metadata solo sanitizada, sin cuenta IDs/credential material.

Hash Git blob del commit para identidad portable; raw-worktree/EOL hash observación separada. Snapshot hash cubre bytes/canonicalization-version, referencias de blobs y metadatos; objetos immutable write-once bajo servicio confiable. Hash no demuestra fuente verdadera ni protege frente a escritor que puede sustituir registro **y** hashes. Anclar digests de lotes fuera del namespace escribible por worker y verificar chain/head/backup; threat model de administrador host comprometido exige controles adicionales LIVE, no prometer WORM porque archivo sea JSON.

Audit trail solo append desde actor autorizado; corrección mediante evento superseding con original preservado. At-most-one admitted-output constraint conserva todos los intentos, rejected/late/duplicate incluidos. Revalidación con nuevo admission crea nuevo veredicto, no reescribe histórico. Retención/borrado/licencia/PII y acceso a backups se fijan con proveedores/datasets; no inventar periodo legal universal. Datos operacionales/secretos reales nunca se suben a Git público; Git contiene documentos, procedimientos, schemas, fixtures sintéticas y referencias sanitizadas.

## 3. Backup, restore y observabilidad

Separar RPO/RTO de store financiero, job store y evidencia raw; valores finales pendientes de workload y gobierno. Backup no es PASS sin restore: nueva ubicación/identidad permitida, verificación integridad, reconstrucción de índices/recepción/leases, datos PIT y snapshot presentes. Export JSON no sustituye transacción/backup de DB. SQLite H1 es demo, no aceptación del motor final/power loss.

Métricas de caller: required/queued/started/attempted/on-time-valid/late/rejected/no-output/quota/failed; denominador job vs attempts separado; tiempos queue/service/total por rol/tamaño; backlog/deadline slack/age; leases stale; drift config/schema/hash; auth availability; footprint de storage; errores pedagógicos pendientes. Alertas factuales con severidad/owner/runbook: ninguna alerta LLM cancela/liquida/reanuda posiciones. Stopped-agent supervisor no reinicia core en pausa material.

Runbooks mínimos antes de DoR: cliente/job crash, late/duplicate, datos corruptos/missing, login revocado, quota, upgrade drift, filesystem/DB lleno, reloj retrocede, backup fallido/restore y reboot. Integración y RPO/RTO se verifican P2; no omitir diseño/criterios P1 para evitar circularidad implementation-before-ready.

## 4. Versiones y despliegue

Release/tag aprobado → commit + manifest/assets/dependencies/artifact hashes + gates + config effective fingerprint → deployment. `plan-architect` para preparación/candidato, `main` baseline estable; ninguna promoción automática ahora. El manifest declara versiones exactas SDK/CLI/OS/protocolo, Python/deps/Skill/schema/admission/calendar/dataset/tools, modelo solicitado y efectivo. Modelo alias/servicio remoto no garantiza pesos congelados: conservar outputs y rerun regresión afectada ante drift, no prometer bitwise replay del LLM.

Published Python SDK incluye CLI pinado. Wave07 SDK0.160.0 con override CLI0.159-alpha fue prueba válida de esa **pareja**, no del bundle por defecto. H4 investiga pareja publicada compatible sin global install/upgrade. [SDK oficial](https://learn.chatgpt.com/docs/codex-sdk). Cambios de permissions/client/Skill/schema/tools requieren tests afectados y nueva versión; failure → no iniciar jobs con configuración inesperada. Autoupdate no puede alterar runtime/privilegios aprobado sin gate; sin pin/control efectivo no freeze.

Rollback restaura release/config/evidence compatibles; migraciones DB forward/backward y fencing de workers viejos especificados. No borrar eventos/outputs ni reusar command IDs para simular reversión financiera. Arranque tras reboot no autoriza resume de incidente material. Bootstrap debe detectar deps/auth/settings externos y guiar manualmente, nunca Git secrets ni asumir chat previo.

**Restore/incarnation:** antes de aceptar trabajo tras restore/redeploy, parar o aislar workers y emitir un nuevo `environment_incarnation_id` desde control confiable, separado del backup restaurado. Manifest/lease/output llevan ese epoch y se verifica junto a generación/current attempt/expiry: el backup no puede revivir un lease antiguo. Si se perdió receipt previamente confirmado (RPO>0), reconciliar con evidencia immutable/anchors fuera del backup; si no se reconstruye, registrar `RECOVERY_GAP/UNKNOWN` y excluir comparabilidad afectada. No recontar output como nuevo ni backfill on-time silencioso. El lost-job gap no altera posición financiera ni autoriza orden/resume. Probe toy de epoch/lost receipt antes del cierre de diseño, integración real después de implementación.

El epoch actual pertenece al **envelope del intento**, no al job_id lógico ni a una mutación del manifest original. Conservar creation epoch y outputs admitidos históricos. Nuevas recepciones exigen epoch vigente; restore no marca retroactivamente outputs históricos como inválidos ni inventa identidades nuevas para eventos viejos.

## 5. Economía por candidato externo

PostgreSQL/Parquet/DuckDB/Redis/Temporal locales: PAPER_V1_VIABLE_FREE=CONDITIONAL al motor/instalación/licencia/recursos; PAPER_V1_COST=0 licencia esperada para opciones libres, tiempo/hardware por medir; LIVE_COST=UNKNOWN fijo/variable/mensual/escala. FREE_ALTERNATIVE=local/self-host según candidato. PAID_INCREMENTAL_VALUE=hipótesis de continuidad/managed operations/backups/seguridad; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de contratar. SQLite stdlib: gratuito para probe, no sustitución aprobada. Pin y verificar licencia del artefacto final (Redis depende de distribución/versión). No facturación/servicio cloud iniciado.

## S2 — raw/output versus sealed evidence y audit de permisos

Aplicar [S2 RC1](08_S2_isolation_spec_RC1.md): jobs solo export permitido y scratch/output propios; C recoge bytes a store sellado fuera de job, H realiza join posterior. Ningún writer del job puede modificar snapshot/receipt/digest anchor, backup core, configuration o package. Trusted SID/policy/version fingerprint de lanzamiento y cada negativo forman audit sanitizado; raw OS SID/SDDL local protegido. No claim de logging OS completo por handler log: SI-14 exige correlación de acceso rechazado con controles positivos y observer apropiado; habilitar SACL/audit/firewall logging necesita gate administrativo.

Bootstrap/deploy liga SIDs de instancia nueva, config/policy y versión exacta sin copiar autenticación ni ACL con SID viejo silenciosamente. Reboot/restore revalida denies antes de iniciar/admitir jobs; permisos unknown bloquean, no fallback S1. Postseal mutation conserva original en receipt. Directories de canary ADM-01 son laboratorio, no layout productivo implementado ni nuevo store seleccionado.

## Stores y versiones con Agent Runner — 2026-10-06

[RC2](08_S2_agent_domain_contract_RC2.md): namespace por job y contexto efectivo, no cuenta obligatoria por rol. Raw/sealed/comparisons/registry/audit y code/config protegidos por control externo; job no tiene credenciales SQL/store ni write a receipts/grants. Supervisor/context token/policy binding se versionan además del rol; receipt tras copy/seal precede join Champion/Shadow. Auth persistente se separa de history/prompt/peer output; survivors explícitos. Probe AccessCheck no genera audit OS ni verifica permisos reales. Release/tag aprobado, main estable y manifest/source policy intactos; ADM-01 withheld, nuevo gate posterior a variante.
