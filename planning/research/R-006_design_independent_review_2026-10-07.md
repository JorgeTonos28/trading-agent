# R-006/R-010/R-013 — revisión de diseño tras ADR-013

2026-10-07. Reviewer existente `independent_hardening_review`, lectura documental/fuentes; no ejecutó probes/admin ni editó. Requerida por roadmap §3.16 y trabajo crítico P0/P1. Revisión de agente distinta al autor principal, no auditoría humana ni autorización.

## Hallazgos y disposición

| Hallazgo | Prioridad | Reparación / límite |
|---|---|---|
| C/A/J/auth/state/binding abstractos | P1 | B-RT1 concreta ownership, token por attempt, native auth/config y transacción ledger C; revisión confirma aptitud para presentar candidato |
| Onboarding vigente mezclado con instrucciones Team PAPER anteriores | P1 | ONBOARDING inicia ADR-013/route actual; cuerpo previo identificado histórico. Contract deltas actuales antes de scopes anteriores |
| Evidencia sin instance/config binding | P1 | R-028 RC1 + schema v0.3 y test fields; B1 sintético posterior a primera revisión, no store real protegido |
| TokenPolicy, desktop, launch capability y callbacks ambiguos | P1 | B-RT1-T1, desktop separado, CreateProcessAsUserW/acquisition/lifecycle fail-closed; stubs J y READ_TOOL/SUBMIT_RESULT separados |
| HOME por job no preserva namespace keyring estable | P1 | Código Codex pinado confirma HOME-derived key; propuesta corrige HOME mínimo fijo readonly + sqlite/log/TEMP privado, compatibilidad NOT_TESTED |
| WinCred compartido puede transportar contenido entre attempts | P1 aceptación | BL-AUTH canary arbitrary metadata y restart, fail/reopen si native refresh permite carrier excluido. No bypass observado, no aislamiento por keyring supuesto |
| Schema v0.3 conservaba $id v0.2 | P2 | Corregido solo branch v0.3; branch v0.2/capturas originales conservados |
| R-028 decía probes ejecutados sin fuente/resultados | P2 | B1 preregistrado/ejecutado 16 casos PASS, fuente/resultados enlazados; no claims de autenticidad/readiness |
| Fingerprint canonicalization unspecified | P2 | canonical-json-v1 propuesto; vector/interoperabilidad verifier final pendientes, no claim de prueba |

## Conclusión registrada

Reviewer confirmó las reparaciones en B-RT1 guardado y no identificó otro P0/P1 **documental** resoluble Team que impida presentar propuesta material condicional al owner. Auth keyring/refresh, writes residuales, cross-user launch efectivo, ACL/IPC/red, seguridad/blinding/capacidad Plus son incógnitas target. Servicios/derechos nuevos o cambios de trust obligan a revisar diseño, no son un parámetro automático.

No aprueba B-RT1/D-024/D-027/freeze/Plus/PAPER. Primera entrega no revisó H7; segunda revisión de fuentes y límites B1/H7 se registrará como adenda, no fingirla ya realizada. [Checkpoint](../14_agentic_architecture_design_checkpoint_RC0.md).

## Segunda revisión de evidencia

Reviewer contrastó fuente/schema/hashes B1 y sus 16 casos con resultados: coinciden, scope FAKE explícito. Contrastó hashes H7 y attempts1/2; no exactly-once ni Activity-timeout observado directamente. Cleanup parcial/residuo correcto. No ejecutó scripts. H8 no revisado independientemente.

**P2 identificado:** helper pwsh de H7 que consulta listeners no pasa env allowlist y hereda entorno completo, contrario al protocolo. No observó secretos leídos/expuestos; no repetir H7 para esconderlo. Fuente/resultados originales intactos, caveat en dossier y versión `h7_controller_next.py` corregida para eventual repetición (NOT_EXECUTED). H8 explícitamente limita env de sus hijos. No nuevo P0/P1 de diseño por este hallazgo.
