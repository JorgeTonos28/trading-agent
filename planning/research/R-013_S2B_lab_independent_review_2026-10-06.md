# R-013 — revisión independiente del laboratorio S2-B

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-06. Reviewer `/root/independent_hardening_review`, solicitado como revisión crítica del Preparation Program. **Lectura únicamente**; no ejecución de probes/harness, setup administrativo, secretos o código Trading OS. Revisión del paquete de preparación, no auditoría humana ni aceptación de seguridad/runtime.

## Hallazgos y resolución

| ID | Prioridad | Hallazgo | Reparación comprobada en lectura final |
|---|---|---|---|
| LR-01 | P1 | Archivo amplio sin grant al peer podía denegar por DACL del objeto y simular barrera del parent | READ explícito peer SID; positivo AccessCheck del mismo descriptor, positivo propio real y peer posterior; DACL real/positivos pendientes. No claim de tránsito antes del lab |
| LR-02 | P1 | Validación canonical post-create podía llegar tarde ante reparse de un parent | Checks/pin de ancestros y parent antes de crear, handles retenidos, lab quiescente sin writers; TOCTOU residual declarado, no sandbox adversarial. Ruta relativa al root confiable |
| LR-03 | P1 | Control OPERATOR/SY/BA no llegaba a hijos nuevos con grants no heredables; broad SD omitía OPERATOR | OI/CI en directorios, grants sin herencia en archivos; OPERATOR explícito en broad child protegido. Attempt01 preservado, attempt02 corrige herencia |
| LR-04 | P1 | Token sin SeChangeNotify podía fallar tránsito C:/ProgramData antes de alcanzar el lab | Adapter user-mode NtCreateFile RootDirectory relativo, sin ampliar ACL Windows ni fallback a BASE; fuente preparada, API/positivos reales NOT_TESTED. No garantiza full Codex |
| LR-05 | P2 | Harness parcial podía confundirse con cobertura de todo LF/replace/root/revocation/collector | Mapping automático/manual/pendiente §7; máscaras negativas mínimas añadidas. Root/rename/replace/revocation/seal/rollback no aprobados por exit 0 ni thread filesystem |
| LR-06 | P2 | Rollback permitía borrar padres fuera del árbol y a la vez exigía todos los targets dentro | Único target recursivo trial-01; padre nuevo exacto separado, vacío/no-reparse/no recursivo, nunca ProgramData/preexistentes |
| LR-07 | P2 | Parent nuevo faltaba en declarativo de permisos y dependía de default inheritance | `bootstrap_parents` declara path exacto/owner/grants; attempt03 valida 14 FS + 1 parent, todos solo sintaxis; source/plan02 archivados |

Fuente filesystem final leída: SHA256 local `ce2a39ad0bfc7ad7cb86fd8e2a78d570bdafc6bd9c5117f37569ca45cf24fb93`. Wrong principal aborta sin escribir reporte; pin y root handle permanecen en harness confiable, nunca evidencia de un proceso adversarial seguro. Reviewer verificó correspondencia SHA source/plan de renderer01/02 archivados y 03 activo, common-SID01 y preflight01.

## Conclusión de la revisión

No se identificaron hallazgos P0/P1 adicionales que impidan **presentar el paquete de preparación para decisión humana en su alcance**. [S2B-ADM-01](R-013_S2B_lab_ADM01.md) sigue READY_FOR_DECISION / NOT_AUTHORIZED / NOT_EXECUTED.

La viabilidad nativa de la API/ruta, todos los positivos y negativos filesystem reales, proceso completo/handles/token/desktop/IPC/red, auth/cache/recovery/carga TP6 y blinding experimental siguen pendientes. D-027/D-024 RESEARCHING, implementación bloqueada. No equivalencia entre lectura, sintaxis, observaciones en memoria y aceptación efectiva. [Dossier](R-013_S2B_lab_preparation_2026-10-06.md).
