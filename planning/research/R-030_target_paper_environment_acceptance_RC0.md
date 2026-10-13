# R-030 — Target PAPER Environment Transition & Acceptance — RC0

**Vigencia aprobada — 2026-10-13, ADR-014 / propietario:** `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` en el alcance capacidades/roles/fronteras/integración B-RT1. `design_status=DESIGN_DECIDED`; `TARGET_ACCEPTANCE_DEFERRED`; `PAPER_RUNTIME_ACCEPTED=false`; `implementation_locked=true`. Un Runner, control confiable externo, core/secretos fuera AI, aislamiento/contexto mínimo por job, allowlists, identidad/lifecycle por attempt y admisión/audit externos son el contrato aprobado. Keyring, HOME readonly, token, desktop, IPC carrier y launch exactos son **mecanismos candidatos sustituibles**, no invariantes irreversibles; cambios preservan fronteras/autoridad con evidencia y gobierno correspondiente. R-030 acepta eficacia en Plus/PC personal. Investigación agéntica fundamental Team completada; no expandir R-006/010/013 por refinamiento indefinido. LIVE UNKNOWN; residuos H7 conservados sin evasión de policy.


2026-10-07 · **P1 · TARGET_ACCEPTANCE_DEFERRED** · ADR-013/D-043; D-024/D-027/D-037. No ejecución ahora ni solicitud de acceso Plus/admin institucional.

## Matriz por fase

| Gate | Contrato de diseño durante Preparation | Aceptación específica del target, antes de implementar | Validación del sistema construido, antes de PAPER |
|---|---|---|---|
| TE-1 plan/acceso | Ruta Codex nativa, coste separado API, inventario/requisitos/fallback | Plus individual observado, cliente/transporte/modelos habilitados, login legítimo del dueño, entitlement/cuotas observables | Suficiencia cuota/cadencia compartida y reset bajo workload Strategy V1 |
| TE-2 bootstrap/packages | EB1–8, contratos globales/por rol, hashes Git y manifest, dependencia/config diff | Fresh clone en PC personal sin chat; activos finales, cwd y reglas por rol, activación Skill/procedimiento, inventario de herramientas/policies | Restore desde snapshot aprobado y regression después de cambios |
| TE-3 outputs/tools | Cuatro procedimientos RC2, PIT, linaje, enums confiables, validators externos y tool allowlists | Smokes nativos en ruta/config final; rechazar schema/tool/request fuera de allowlist; no billing fallback | Fuentes/engine/report reales, fallos/injection y calidad de outputs |
| TE-4 security | S2-B, SI17/BL9/RB5/VP8, mínimos FS/IPC/red/secrets, S2-A/S3 condicionados; contratos job/security separados de blinding | Gates administrativos revisables owner-only, FS sintético seguido por full-process/auth/network/IPC/supervisor/peer/relaunch; no secretos financieros reales necesarios | Red team e integración del deployment final, drift, blinding y permisos efectivos |
| TE-5 recovery | At-least-once attempts, máximo un receipt, fencing/epoch, bounded retries, no-output ≠ HOLD, no chat durabilidad | Recovery de fixture no financiero, auth/logout/refresh tratados sin secretos/export; state/writer separados | Crash/backup/restore, late replies, desconexiones y reconciliación financiera |
| TE-6 capacidad | Workload parametrizable, cola acotada, admisión/expiración, no asumir preemption o concurrencia segura | Benchmark acotado de acceso/suficiencia para smoke; límites desconocidos explícitos | WL-R Strategy V1 y varias sesiones/días; ≥5 sesiones/7 días es propuesta pendiente, no permiso ni umbral aprobado |
| TE-7 operación | Pins, licencias, update policy, release fuente, runbooks/protocolos, economía ADR-008 | Versiones exactas/bundled CLI, configuración final y evidence fingerprint en PC personal; rollback de setup | SLO/RPO/RTO seleccionados, pruebas restore, observabilidad y reports continuos |

No todos los tests operacionales se exigen antes de construir: la columna target utiliza **fixtures desechables**. Se requiere un resultado verificable por fila aplicable; FAIL/UNKNOWN/NOT_TESTED no se promueven a PASS. Si el target revela una incompatibilidad que cambia seguridad/runtime/autoridad, registrar evidencia y volver a gobierno, sin downgrade ni fallback pago automático.

## Reutilización de evidencia

Conservar TP1–7 Team y gates Plus anteriores como evidencia histórica, con IDs/source/versión. Reutilizar resultados conductuales, PIT, schema/lineage, método adaptado vs mínimo y fixtures de failure. Repetir únicamente diferencias de plan/instancia/host/superficie/config, y smokes finales afectados por esas diferencias; no repetir toda R-006 bajo Plus. Team no demuestra `AVAILABLE_IN_TARGET_PAPER_PLUS` ni `AVAILABLE_ON_TARGET_PAPER_HOST`.

## S2B-ADM-01 portable

Estado `DEFERRED_TO_TARGET_PAPER_HOST`; LF01–12 siguen NOT_TESTED. La transacción histórica no debe ejecutarse en nueva instancia. Preparar un nuevo binding target con bytes/policy/source/commit, nueva transacción y gate del administrador propietario. No crear automáticamente cuentas/firewall/ACL por abrir el repo o invocar Bootstrap. Helper de preparación bloquea Setup/Rollback mientras está diferido. Rollback de laboratorio acotado por SID/path/ledger; no tiene alcance operacional global.

## Entregable

Environment profile sanitizado con AI-plan/host separados; diff expected/observed; acciones AUTOMATED/USER_ACTION_REQUIRED/UNAVAILABLE/OPTIONAL/FALLBACK_AVAILABLE; resultados con fase, refs, source/versión; readiness calculado externamente. `READY_AGENT_ENVIRONMENT` no implica READY_FOR_IMPLEMENTATION global, PAPER ni LIVE.

Esta ficha especifica pruebas futuras; no registra ejecuciones que no ocurrieron. LIVE target UNKNOWN, R-029 histórico no selecciona un entorno futuro.

## Deltas candidatos B-RT1 / instancia

Contrato [B-RT1](../08_agentic_runtime_realization_RC1.md) aprobado 2026-10-13; TE-4 verifica supervisor C protegido, aislamiento/identidad/lifecycle efectivos, tools mínimos y admisión externa. TokenPolicy B-RT1-T1, desktop, AcquireRunnerLaunchCapability y carrier IPC son mecanismos candidatos, no requisito irreversible de una API concreta. TE-1/4 prueban auth/refresh y persistencia permitida; keyring/HOME readonly/redirects y **BL-AUTH WinCred canary→relaunch** aplican si se conserva ese mecanismo. Un reemplazo debe cubrir amenazas equivalentes y registrar evidencia/gobierno antes de aceptación, nunca eliminar un test por conveniencia. Si exige mover supervisor a A, nuevo servicio privilegiado, grants amplios, contenido compartido excluido o login por job, volver a owner por cambio material, no ampliar permisos automáticamente.

TE-2/7 exige [instance/fingerprint](R-028_instance_binding_RC1.md) por resultado y scope fijado externamente. B1 sintético comprueba lógica de bindings, no la autenticidad del registro ni target PASS. No usuarios, login, privilegios, desktops/policies/config nuevos realizados por esta adenda.
