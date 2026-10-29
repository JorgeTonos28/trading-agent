# R-013 — revisión independiente del handoff autorizado S2-B

2026-10-06. Reviewer `/root/independent_hardening_review`, revisión crítica requerida por Preparation Program. **Lectura únicamente** de autorización, helper, runbook, evaluador y QA. No ejecutó script/probe, administración o secretos; no constituye acceptance de seguridad.

## Hallazgos y cierre documental

| ID | Prioridad | Hallazgo | Reparación verificada por lectura |
|---|---|---|---|
| ER-01 | P1 | Error antes de trusted-evidence deja recursos sin ledger durable | Journal sanitizado flushed INTENT antes de crear, VERIFIED después; trusted-evidence temprano; fallo visible. Partial rollback bloquea hasta atribución owner; journal no es autoridad de borrado |
| ER-02 | P1 | Receipt con booleans no prueba copia fuera del lab | Receipt control-only verificado, copia externa/path canonical/hash/length y reporte público/hash comprobados antes de borrar |
| ER-03 | P1 | GetOwnerSid nonzero ignorado podía simular ausencia de procesos | UNKNOWN bloquea todos los deletes; owner verifica PIDs/creation times concretos, sin kill global/policy extra |
| ER-04 | P1 | Journal editable podía transformar ledger parcial en setup completo | Ledger protegido debe tener status complete, source/policy/helper exactos y manifest18; corroboración VERIFIED/ACL; partial sigue bloqueado |
| ER-05 | P2 | UAC con otra cuenta puede dejar agente sin permiso collector | OPERATOR es SID de Setup, no nombre de desarrollador; acción owner collector legítimo, no ampliar ACL o suplantar |
| ER-06 | P2 | DeleteChild aplicado también a files | Evaluador solo considera 0x40 en directorios; pares file quedan no aplicables, no ERROR/PASS engañoso |
| ER-07 | P2 | Grant con metadatos inválidos podía afirmar fallo del diseño | ERROR/unattributed señal bloqueante; FAIL atribuible se conserva aun con positivo ajeno fallido |
| ER-08 | P2 | QA intermedio sin conservar todas las versiones de source | Marcar snapshots anteriores con provenance limitada; QA05/source actual y QA02/evaluator actual son únicos resultados activos; no reproducibilidad retrospectiva inventada |

## Resultado de la revisión

Sin P0/P1 pendientes que impidan entregar el handoff dentro del **laboratorio confiable/quiescente autorizado**. Helper SHA256 `7f6ac7b77b14d420b482d241888f43adfd7f282842573d46de5c437b427499cd` coincide [QA05](probes/r013-s2b-lab-execution/offline-source-qa-05.json). Evaluador y source de QA Python coinciden [QA02](probes/r013-s2b-lab-execution/offline-evaluator-qa-02.json). PowerShell 7 existente, create-new con SD inicial y procedimientos de bloqueo/export coherentes con [runbook](R-013_S2B_owner_execution_runbook.md).

QA Python son **15 checks offline: 3 source + 12 evaluador sintético**, no 15 pruebas reales filesystem ni mocks de flujo Setup/Rollback. QA PowerShell: AST, 15 descriptores en memoria y compilación del adapter sin llamadas nativas. Estado OS observado readonly; account/setup/login/FS/rollback no ejecutados. [Estado actual](probes/r013-s2b-lab-execution/execution-state.json).

R-013/D-027/D-024 siguen abiertos; S2-B candidata sin aceptación técnica. Security/blinding de proceso completo, native Team auth/egress/IPC y workload siguen fuera. Owner administra/login seguro, agente solo no privilegiado. No Windows policy/config/billing changes por la revisión.
