# S2B-ADM-01 — autorización y preparación de ejecución

2026-10-06. **AUTHORIZED_OWNER_ADMIN_ONLY / OWNER_ACTION_REQUIRED / NOT_EXECUTED**. [Estado actual](execution-state.json). Administrador único: propietario; agent no elevado. Transacción `s2b-20261006-a6d74b2b`. [Runbook completo](../../R-013_S2B_owner_execution_runbook.md), [scope](../../R-013_S2B_lab_ADM01.md), [autorización](authorization.json). Cuenta/lab temporales; ninguna configuración PAPER instalada.

## Estado observado

| Elemento | Resultado actual | Lo que acredita |
|---|---|---|
| Baseline + readonly-preflight-03 | cuenta/parent/root ausentes a 19:03 UTC; operador no elevado | Disponibilidad en ese instante, no setup ni autoridad admin |
| Owner helper parser / memory descriptors | PASS, 15 descriptores sintéticos | Sintaxis y representación del plan, no ACL efectivas |
| Adapter Win32 compilation | PASS, definiciones compiladas; cero llamadas nativas | Compila bajo PowerShell 7.6.5 actual, no creación/rollback |
| Offline QA02 | 15 PASS / 0 FAIL: 3 source + 12 evaluador sintético | Detecta invalid metadata/positives, errors, missing/duplicate observations y grants sintéticos |
| QA memory attempt01 | ERROR lector parent-kind, fuente/error preservados | Defecto del propio QA corregido; no fallo de S2-B |
| Windows PowerShell 5.1 QA03 | ERROR policy blocked antes del script | No equivalencia de superficies; ninguna policy se cambia/bypassea |
| LF01–12 filesystem real | NOT_TESTED | Ninguna evidencia de denegación/compatibilidad nativa |
| Whole process / native Codex Team / IPC / egress / auth / recovery | NOT_TESTED | Gates independientes pendientes |
| Rollback | NOT_STARTED | No recursos OS creados por agente; comprobar de nuevo tras cada acción owner |

El lab aún no puede ejecutarse sin crear la cuenta y aplicar ACL con acciones owner. Primera acción §1 del runbook: crear únicamente `tos_probe_runner_b`, descripción de transacción, estándar/Users y disabled, contraseña introducida solo Windows. No carpetas todavía. R-013/D-027/D-024 abiertos. S2-B sigue candidata viable para validación, no técnicamente aceptada.

## Fuentes/evidencia

- `owner_lab.ps1`: owner ejecuta Plan/Setup/Rollback; agent solo lectura/Inspect no elevado. Scope fixed y source hashes, create-new descriptor inicial, journal previo, partial bloqueado, manifest protegido, export real, owner UNKNOWN bloquea delete. Sin creación de usuarios, captura de password, login o process-launch; eliminación de la cuenta nueva solo por SID en rollback owner.
- `readonly_preflight.ps1` / `readonly-preflight-03.json`: metadata readonly sin SID/secretos publicados.
- `preparation_checks.ps1`, `offline-source-qa-05.json`: AST/memoria/compile, sin ejecutar helper. QA02/04 conservan snapshots intermedios; QA01 error con fuente archivada; QA03 bloqueo de 5.1.
- `preparation_checks.py`, `offline-evaluator-qa-02.json`: 3 checks source + 12 de evaluador con fixtures sintéticos, no recursos lab. QA01 conserva comparación anterior; hashes refieren a sus versiones de captura.
- `evaluate_filesystem.py`: assessment readonly posterior; no aggregate security PASS y corroboración externa pendiente por defecto.
- `authorization.json` y `owner-setup-baseline-01.json`: snapshots iniciales, no sustituyen estado actual/procedencia humana.

Los snapshots de preparación anteriores NOT_AUTHORIZED permanecen intactos como historia. La aprobación humana posterior permite únicamente este scope. Nunca registrar SID reales, password/PIN/token/auth/financial creds en Git. Metadatos privados del ledger sin secretos se retienen fuera de Git para comprobar export; no usar `.local` como almacén de secretos operacionales.

**Provenance limitada de intermedios:** QA-source02 y evaluator-QA01 no conservan todos los bytes de las versiones previas del helper/evaluator; son historial, no resultados actuales reproducibles. QA05 y evaluator-QA02 corresponden a sources actuales y hashes verificados. [Revisión independiente de lectura](../../R-013_S2B_execution_handoff_review_2026-10-06.md) sin P0/P1 de handoff pendientes; no execution/acceptance.

## Endpoint y gate posterior

**HUMAN_ACTION_REQUIRED:** acción Windows de cuenta disabled del owner; ningún nuevo consentimiento del gate. Tras verificación: preview/setup owner, OPERATOR positivos, login BASE seguro, FS, seal, procedimientos manuales restantes y rollback. Owner deberá actuar nuevamente en pasos privilegiados/login conforme runbook.

Reportar PASS_SCOPED/FAIL/ERROR/INVALID_POSITIVE/NOT_TESTED por caso, alcance/limitaciones, viabilidad, rollback/residuos. Filesystem PASS nunca acepta S2-B. Después de FS, proponer **S2B-PROC-01** para proceso/supervisor/token/handles/descendants/private desktop/IPC; no ejecutarlo por este gate. Egress y auth Team separados, sin dinero/API/global changes.
