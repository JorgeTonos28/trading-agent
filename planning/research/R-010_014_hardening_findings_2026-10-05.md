# R-010–014 — hardening PAPER: evidencia y checkpoint

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-05. Dirección ADR-011 A aprobada; D-020 DECIDED en disposiciones de diseño. **D-024 RESEARCHING**; no freeze, implementación, permisos finales, gasto, main ni deployment tag. PAPER Team; Plus candidato PRE-LIVE, no bloquea.

## 1. Entregables y alcance

- [Seguridad/permisos](../08_agent_security_contract_RC0.md): actores, amenazas, domains/holdout/paired blinding, S1/S2/S3, gate de viabilidad antes de freeze.
- [Workflow/recovery](../08_job_workflow_recovery_contract_RC0.md): invocación automática, trigger/outbox/identidad, axes/mapping, attempts/leases/fencing/epoch, bounded retry, no-output ≠ HOLD.
- [Audit/versiones/deploy](../08_audit_versions_deployment_contract_RC0.md): namespaces, evidence append, hashes/anchors, backup/restore/RPO gaps, versions y rollback/release.
- [Preregistro](R-010_014_hardening_protocol_RC0.md), [probes](probes/r010-hardening/), [review independiente](R-010_014_independent_review_2026-10-05.md), [ADR-012 propuesto](../decisions/ADR-012-agent-process-isolation-proposed.md).

Son especificación y experimentos desechables. Ningún worker/scheduler/control financiero del Trading OS construido. No credencial de broker solicitada; login Codex actual legítimo, sin copiar/exportar tokens ni activar API billing.

## 2. Evidencia práctica

| Probe | Resultado observado | Qué permite concluir / límites |
|---|---|---|
| H1/H2 SQLite temporal | **20/20** checks: subprocess sale abruptamente antes/después commit, rollback/confirmación, restore backup, receipts/dedup/late/hash/identity y conexión readonly | Semántica toy de commit/recepción; no PostgreSQL/Temporal, power loss, financial runtime o ACL OS |
| H2 suplemento review | **11/11**: dos threads concurrentes reciben mismo output, exactamente una selección y duplicate; expiry/current attempt/owner/generation/cancelled/exhausted/late | Transacción SQLite real, reloj/lease/identidad virtuales. No lease renewal/clock drift/cancel race ni motor final |
| Restore epoch | **3 comprobaciones lógicas + 1 asignación de política** registradas 4/4 | Mismo generation del backup puede coincidir con worker viejo; epoch externo evita admisión por diseño. No recuperación real de receipt perdido; UNKNOWN/exclusión explícitos |
| H3 carga virtual | 40 tareas perfil regular dentro de ventanas a multiplicador 1/2/4; reserva/burst revelan fallos | Simulación de servicio con latencias wave07, no 40/63 nuevas inferencias ni cuota sostenible. Datos/source/v1/v2 preservados |
| **H4 SDK/CLI publicados emparejados** | SDK0.160.0 / CLI0.160.0, resolver bundle por defecto; **2/2** research/shadow con Skill, read_evidence, structured output/admission; cleanup | Prueba concreta de compatibilidad en Team de pareja publicada; no permisos efectivos, todos los roles/requests o versión final seleccionada |
| H5 metadata local | Windows11 Enterprise 10.0.26300; hypervisor presente; python/node/git/codex en PATH; WSL declara no instalado; Docker/psql/Redis/DuckDB no hallados en PATH | No infraestructura/config lista por existencia binario o hypervisor. Ningún setup administrativo realizado |
| **H6 Temporal reusable** | CLI1.9.1 / Server1.32.0 / UI2.54.1; **10/10** evaluación: listeners loopback, duplicate workflow-ID rechazado, mismo run/history=2/status pendiente tras kill+restart, schedule dispara automáticamente 1 workflow y conserva run/count | Dev server local con SQLite persistido, sin worker. No Activity ejecutada, retries de SDK/modelo, Codex schedule integrado o stack production. Proceso parado y workspace limpiado |

### Versiones y artefactos

H4 wheel `openai_codex_cli_bin-0.160.0-py3-none-win_amd64.whl`, 149416482 bytes, SHA256 `a1245cc0c7d390d22af4920d512ceae8519dee2cf51d8eec56f3899861a8160a`; SDK público Apache-2.0. Bundle extraído temporalmente, sin global install ni cambiar Codex desktop. Clonó commit `8982c73` para role/AGENTS; raw hashes de fuentes/probes guardados. La evidencia de wave07 SDK/CLI distinto permanece, no se reinterpreta como bundle estable. [SDK oficial](https://learn.chatgpt.com/docs/codex-sdk).

H6 release CLI1.9.1, ZIP 46408338 bytes, SHA256 `babb65844835045c91fb98930fe10b81de28db80c8c609180473d2c0b18c7589`; [licencia MIT de CLI](https://raw.githubusercontent.com/temporalio/cli/v1.9.1/LICENSE), [release](https://github.com/temporalio/cli/releases/tag/v1.9.1). Primer fetch urllib falló TLS reset; curl primera conexión timeout, retry exitoso con verificación TLS. No disable TLS; fallos registrados en resultado. [CLI start-dev](https://docs.temporal.io/cli/command-reference/server) documenta persistencia `db-filename` y advierte uso exclusivamente desarrollo. No seleccionar start-dev como deployment PAPER sostenido.

## 3. Capacidad: resultado que cambia el diseño de prueba

H3 toma **máximo observado por rol en wave07**, multiplicadores hipotéticos y llegadas virtuales. Perfil regular 40 tareas: 40/40 contabilizadas dentro de ventanas ilustrativas; no demuestra suficiencia native. Reserva v2 representa **50 jobs lógicos + 13 cargas abstractas = 63 service requests**, no 63 jobs funcionales ni retries del mismo parent. A x4, 3 solicitudes exceden su ventana ilustrativa. Tasa funcional debe usar jobs requeridos incluyendo fallidos/no-output, no attempts.

Burst con Quant iniciado justo antes de 2 shadow + 1 pedagogy: a x1, 4/4 solicitudes dentro de ventana; a x2/x4, ambos shadow exceden 120s propuestos (2/4 solicitudes dentro). Prioridad entre jobs ready **no preempta** el job background en ejecución. No seleccionar automáticamente más procesos: comparar budget/ventanas/background interruptible o colas/concurrencia aisladas contra carga real. Deadline/cadencia/cola final dependen de Strategy V1 y gate D-024. No bajar obligación Shadow ni llamar HOLD al timeout.

Falta evidencia native de WL-R representativo definitivo, reserve/reties con parent/deadline original, auth/quota compartida y observación sostenida P2. Antes de freeze P1 justificar factibilidad concreta de carga/ruta elegida; estos resultados no dispensan TP6.

## 4. Build-vs-Reuse y economía

| Capacidad | Disposición / estado | Economía y gate |
|---|---|---|
| Codex/Skills + SDK/app-server | Dirección aprobada REUSE_AS_IS / WRAP | Incremental API billing 0 en probes nativos Team; quota/sostenibilidad y pin final abiertos |
| Identidad/ACL/IPC/red Windows + sandbox nativo | **REUSE/WRAP candidato S2**, no seleccionado/aprobado aún | Software existente, licencia extra esperada0; costo setup/tiempo por medir. Necesita gobierno D-027 y prueba efectiva, no configuración automática |
| VM local | REFERENCE_ONLY reserva S3 | Recursos/guest/license/operación desconocidos; no gasto autorizado |
| Temporal | **WRAP candidato baseline**, probe de dev viable | EXISTS=YES; local probe AVAILABLE=YES; compatibility PARTIAL por motor sin worker; económicamente CONDITIONAL self-host; SELECTED=NO. License CLI verificada, server/deps/deploy final pendientes |
| APScheduler/OS scheduler | REFERENCE_ONLY/ADAPT alternativas de comparación | Free local, no equivalencia durable por calendar solamente; pruebas no realizadas |
| PostgreSQL/Parquet/DuckDB/Redis | Baseline de investigación, no elección final | Free viability/licencia/distribución/costos operativos por fijar; no nuevas instalaciones ni servicios |
| SQLite stdlib | REUSE_AS_IS **instrumento de probe** | Costo licencia/API0; no convierte toy en stack operacional |

PAPER_V1_VIABLE_FREE=CONDITIONAL donde falta integración; PAPER_V1_COST=0 de adquisición/API/servicio adicional en estos probes, uso de suscripción y tiempo local no nulos. LIVE_COST=UNKNOWN fijo/variable/mensual/escala; FREE_ALTERNATIVE=local/existing native; PAID_INCREMENTAL_VALUE continuidad/managed operations como hipótesis; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. No runtime IA fuera de OpenAI/Anthropic: Temporal/APScheduler son workflow determinístico, no framework agéntico alternativo.

## 5. Madurez y endpoint

R-006 suficiente para **dirección y disposiciones aprobadas**, discovery sigue activo ante necesidades. P1 contratos y probes acotados avanzados; revisión independiente por agente con reparaciones explícitas. D-024 **NO listo para freeze**: frontera material/permisos efectivos, workflow/store final/pins y carga/suficiencia requieren cierre. P2 integra/valida el sistema después de DoR. Plus es exclusivamente PRE-LIVE.

Antes de detener este paquete se avanzó independientemente [R-020 admisión Strategy V1](R-020_strategy_admission_preregistration_RC1.md); no selección de candidato. Siguiente gobierno concreto **ADR-012 dirección S2 vs S3**. AGENTS exige aprobación de arquitectura material de seguridad. Recomendación S2 por reutilización/menor cambio de entorno, condicionado a viabilidad; si falla, S3 y nueva revisión, nunca fallback S1 operativo. Aprobar dirección no configura OS ni cierra D-027/D-024.

**Vigencia ADR-012 — 2026-10-05:** el propietario aprueba S2 como dirección candidata de aislamiento PAPER por dominios Windows. S3 es fallback formal sujeto a nueva decisión si S2 falla; S1 solo probes sin secretos. Las propuestas históricas S2 vs S3 quedan resueltas únicamente en dirección. Security isolation y Shadow experimental blinding requieren acceptance separado; configuración administrativa, permisos efectivos y D-027/D-024 siguen abiertos. Ningún usuario/ACL/firewall/credencial se modifica por esta aprobación. Véase [ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md).
