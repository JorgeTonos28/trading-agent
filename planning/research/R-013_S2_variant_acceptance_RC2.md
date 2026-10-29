# R-013 — acceptance por variante S2 RC2

**Vigencia aprobada — 2026-10-13, ADR-014 / propietario:** `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` en el alcance capacidades/roles/fronteras/integración B-RT1. `design_status=DESIGN_DECIDED`; `TARGET_ACCEPTANCE_DEFERRED`; `PAPER_RUNTIME_ACCEPTED=false`; `implementation_locked=true`. Un Runner, control confiable externo, core/secretos fuera AI, aislamiento/contexto mínimo por job, allowlists, identidad/lifecycle por attempt y admisión/audit externos son el contrato aprobado. Keyring, HOME readonly, token, desktop, IPC carrier y launch exactos son **mecanismos candidatos sustituibles**, no invariantes irreversibles; cambios preservan fronteras/autoridad con evidencia y gobierno correspondiente. R-030 acepta eficacia en Plus/PC personal. Investigación agéntica fundamental Team completada; no expandir R-006/010/013 por refinamiento indefinido. LIVE UNKNOWN; residuos H7 conservados sin evasión de policy.


> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-06. **SPECIFIED / NOT_TESTED**, dirección candidata S2-B aprobada por propietario; realización técnica aún no aceptada; permisos operativos pendientes. Excepción temporal S2B-ADM-01 aprobada únicamente para el owner. [Contrato RC2](../08_S2_agent_domain_contract_RC2.md), [comparativa](R-013_S2_variants_comparison_2026-10-06.md). No autoriza setup. S2-ADM-01 **DEFERRED / NOT_AUTHORIZED** por propietario.

## Continuidad de criterios

La [matriz RC1](R-013_S2_acceptance_matrix_RC1.md) conserva **SI-01..17, BL-01..09 y RB-01..05** como requisitos/historia. RC2 modifica su realización y el staging administrativo; ningún requisito financiero/blinding se debilita. Todos los tests efectivos de las tres variantes siguen NOT_TESTED. AccessCheck AC01..10 es evidencia semántica aparte.

| Criterios RC1 | Proyección S2-A | Proyección S2-B | Proyección S3 |
|---|---|---|---|
| SI-01 principal/herencia | Cuenta mínima por dominio; evaluar jobs del mismo SID | Runner distinto de F/developer + contexto restringido J; comparar token completo, no solo TokenUser | Guest separado F + contexto mínimo J |
| SI-02..04 secretos/namespaces/integridad | Grants entre cuentas y dentro de cada dominio | Grants efectivos por J, denegación a F y otros jobs; owner/parents/config protegidos | Guest/host + vistas J; mounts no reexponen F |
| SI-05..09 handles/IPC/tools/control | Caller completo y peer/control fuera del job | Control/supervisor fuera de procesos model/tools; binding externo por job/attempt además de SID | Supervisor/IPC guest y host bridges |
| SI-10..12 egress/children/runtime | Policy completa por proceso/dominio | Policy completa Runner y children/contextos; command sandbox no cubre todo | Egress guest/host bridge y descendants |
| SI-13..17 auth/audit/recovery/persistencia/errores | Login por dominio; estado entre jobs y registros externos | Native auth mínimo legítimo, sin peer history; supervisor/token/desktop/cache protegidos | Auth guest, estado J y audit protegido fuera del job |
| BL-01..09 snapshots/exports/linaje/cache/comparación | Cuentas no reparan snapshot erróneo | Contextos J, snapshot predecisión y DAG correcto; comparación tras seal | Una VM compartida no garantiza blinding |
| RB-01..05 clone/recovery/auth/carga/idempotencia | Medir múltiples bindings/logins | Medir wrapper/contextos/broker auth/cleanup/policy | Medir guest image/host bridge y job lifecycle |

El detalle semántico de cada ID permanece RC1. Sus referencias a SID/domain hermano se leen en B como **contexto efectivo**; no basta que ambos TokenUser difieran o coincidan. RB-03 login por dominio se adapta a ruta nativa mínima legítima bajo Runner, sin asumir credenciales exportables ni login por job. Su success requiere Codex funcional con permisos finales. Stages ADM01/02/03 antiguos son históricos; nueva propuesta concreta pendiente, no renumeración que reactive autorización.

## Casos adicionales VP: contexto común y supervisor

| ID | Prueba futura con fixtures/canaries reales autorizados | PASS requerido |
|---|---|---|
| VP-01 | Comparar TokenUser base, restrict SIDs/capabilities, groups/privileges/integrity J/K y children | Diferencias de permisos J/K verificadas bajo misma cuenta; nada de token supervisor/developer accesible |
| VP-02 | Abrir export propio, otro export y financiero bajo cada contexto, con recursos existentes | Positivo propio funciona; accesos ajenos denegados por mecanismo efectivo con razón/audit externo |
| VP-03 | Intentar abrir/duplicar token/handle, leer memoria, inyectar/controlar supervisor/peer, READ_CONTROL/WRITE_DAC/WRITE_OWNER y sustituir DACL de procesos/tokens/IPC | Denegación de derechos no permitidos según policy explícita; owner/OWNER RIGHTS/integrity verificadas y positivos; sin handles amplios ni IPC/window desktop de escape |
| VP-04 | Scratch/links/owner/parent DeleteChild/READ_CONTROL/WRITE_DAC/WRITE_OWNER/config tampering y sustitución de DACL | Sin alteración de permisos, exports, binarios, policy, audit o sealed store; owner definido por principal efectivo, no PID; positivos autorizados |
| VP-05 | Plantar canary en profile/cache/TEMP/registry/Codex history/paths auth-adjacent; relaunch/cambio rol | Job siguiente no recupera datos excluidos; persistencia legítima auth/tesis separada y explicitada |
| VP-06 | Login/refresh/expiry/revocation + DLL/cert/config y tools failclosed bajo contexto final | Native Team funcional sin ampliar a perfil entero/grants amplios ni API billing; errores explícitos |
| VP-07 | Replays, false role/job/epoch, swapped exports, concurrent job y callback fuera de allowlist | Binding externo al modelo y mismo SID; sin cross-job admission/canales privilegiados |
| VP-08 | Full harness inference/auth/client/children TCP/UDP/IPv4/IPv6/loopback/proxy + desktop | Egress/IPC/desktop mínima verificable; solo comandos confinados no pasa |

Todos VP NOT_TESTED. No launch bajo token restringido, AppContainer profiles, filesystem/process DACL reales, usuarios o policy cambios se realizan por este documento. Futuro gate administrativo debe detallar mecanismo mínimo, diff, fixture, positivos/negativos, auditoría y rollback antes de pedir permiso. No usar recursos personales/secretos reales para buscar bypass.

## Estados, escalamiento y evidencia

PASS exige acceso propio funcional y deny efectivo al excluido, sin timeout/missing-resource que simule denegación; logs/source/config/epoch/token-summary/version reproducibles. ERROR/UNKNOWN/NOT_TESTED no equivalen PASS ni FAIL de la arquitectura. Fallo por mecanismo bypass preservado, remediación autorizada y regresión afectada. BL FAIL invalida pares, no autoriza finanzas.

Primero evaluar reparación o mínima separación S2-A por necesidad concreta si B falla. S3 solo por insuficiencia documentada S2 y decisión humana, con SI/BL/RB propios. No S1 PAPER. TP4/EB4/EB6/EB8 reutilizan evidencia aplicable; TP6 bajo permisos finales y TP7 sostenido todavía pendientes. D-027/D-024 no cerrados por especificación ni probe semántico.

## Endpoint S2-B y evidencia adicional — 2026-10-06

Dirección S2-B aprobada; Q-051 DECIDED en ese alcance. [Laboratorio mínimo S2B-ADM-01](R-013_S2B_lab_ADM01.md), Q-052 DECIDED únicamente en autorización temporal **AUTHORIZED_OWNER_ADMIN_ONLY**. [Runbook por fases](R-013_S2B_owner_execution_runbook.md). Setup/login pendientes de acciones manuales del propietario; no permisos PAPER finales. [Dossier](R-013_S2B_lab_preparation_2026-10-06.md) y fuentes distinguen memoria12+privilegios2, sintaxis14 y preflight readonly de **FS/thread/native NOT_TESTED**. Grant común/tránsito/default DACL se incluyen en VP04/LF09, con positivos adecuados. Setup aún no ejecutado; no retry bajo BASE para operaciones de job. Full process/IPC/egress/auth/cache/recovery/TP6 y SI17/BL9/RB5/VP8 pendientes; ningún gate efectivo se pasa por estos contadores. R-006 madura diseño, D-020 conserva aprobación, D-027/D-024 siguen RESEARCHING. ADM-01 tres cuentas DEFERRED; PAPER Team y Plus PRE-LIVE.
