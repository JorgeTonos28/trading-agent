# R-013 S2 — revisión crítica independiente

2026-10-05. Reviewer `/root/independent_hardening_review`, agente distinto del autor, tarea read-only en continuidad de la revisión independiente solicitada por el propietario. Revisó contratos, matrices, gate ADM-01, fuentes/resultados NA y manifest/profile/onboarding. No ejecutó probes, cambios administrativos ni accedió a secretos. No es auditoría humana, aprobación de seguridad ni aceptación del runtime.

| Hallazgo | Prioridad | Reparación verificada / evidencia pendiente |
|---|---|---|
| IR-S2-01 | P1 | Persistencia en perfil/cache/TEMP/auth-adjacent bajo mismo SID sobrevive al export. S2 RC1 + SI-16/BL-06 exigen enumerar writable states, canary→relaunch, survivors explícitos y frontera efectiva. Reparación **contractual** verificada; enforcement NOT_TESTED |
| IR-S2-02 | P2 probe / P1 operacional | Fuente attempt-01 copió env completa y NA-01 heredó por default; no valores reales reportados, no leak credential observado. Attempt-02 corrigió env task parcialmente pero dejó herencia en NA-01/Git. Fuentes/JSON originales preservados; attempt-03 usa OS/task allowlist en **todos** los subprocesses. Reviewer confirmó fuente/digests de 02/03. Reparación activa verificada; no garantía sobre env histórica |
| IR-S2-03 | P1 criterio | Negativos requieren positivo autorizado al mismo target y error/telemetría distinguible; ausencia/timeout no PASS. SI/BL protocol lo exige |
| IR-S2-04 | P1 red | Native command proxy no cubre cliente/modelo/auth/otras superficies. Policy merge/source y block precedence importan; nunca 'block-all + allow excepción' supuesto. S2 §6/ADM-02 conserva full-process tests y policy origin UNKNOWN |

Verificación final: Security isolation, Shadow blinding y reproducibilidad separados; 7/7 NA incluyen counterexamples, no S2 controles PASS. ADM-01 solo tres cuentas estándar + árbol canary/ACL/procesos/tests/deshabilitar; egress/IPC/Team login/capacidad quedan abiertos. Manifest/profile no autorizan admin/operational permissions; D-027/D-024 RESEARCHING. UNKNOWN/gobierno pendiente no S2 FAIL, S3 no automático y S1 no operativo.

Documentación final aclara que attempt-03 completa la reparación env; 01/02 raw y fuentes se conservan. Review permite entregar propuesta revisable, no cerrar decisiones. [Contrato](../08_S2_isolation_spec_RC1.md), [acceptance](R-013_S2_acceptance_matrix_RC1.md), [gate humano](R-013_S2_administrative_gate_ADM01.md), [hallazgos](R-013_S2_findings_2026-10-05.md).
