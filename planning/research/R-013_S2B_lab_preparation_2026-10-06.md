# R-013 — preparación de laboratorio S2-B

2026-10-06. Dirección candidata aprobada, **laboratorio listo para revisión / no autorizado / no ejecutado**. [ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md), [gate exacto S2B-ADM-01](R-013_S2B_lab_ADM01.md). D-027/D-024 RESEARCHING. No implementación ni cambios Windows. La aprobación publicada en b0d6818 no otorga permisos administrativos.

## Evidencia y alcance

| Evidencia persistida | Resultado observado | Lo que no demuestra |
|---|---|---|
| [Common-SID/token](probes/r013-s2b-lab-prep/common-sid-attempt-01.json) | 12 observaciones enfocadas coherentes; grant Users en lista restrictiva permite read común y puede exponer trace ajeno con ese grant | No recursos reales, cuenta Runner, runtime Codex, security/blinding efectivo |
| Mismo probe: privilegios | DISABLE_MAX_PRIVILEGE conserva SeChangeNotify habilitado; handle transitorio con borrado explícito queda con cero privilegios | No token del proceso corriente modificado, ningún user right global; compatibilidad/path traversal reales desconocidos |
| [Plan sintético attempt03](probes/r013-s2b-lab-prep/policy-plan-attempt-03.json) | 15/15 SDDL convierten en memoria (14 FS + 1 parent bootstrap); sin objetos creados | No permisos efectivos, aplicación/admin ni aceptación de seguridad |
| [Preflight readonly](probes/r013-s2b-lab-prep/preflight-attempt-01.json) | Cuenta/nombre y root/parent ausentes, ProgramData no reparse; PowerShell y Python detectados | No autoridad administrativa/host policy ni acceso del Runner nuevo. Revalidar antes de setup |
| [Harness filesystem](probes/r013-s2b-lab-prep/filesystem_probe.py) | Fuente preparada y AST parse correcto, **NOT_EXECUTED** | No API funcional nativa ni LF PASS; thread-token confiable no es proceso adversarial/Codex aislado |

Diez checks previos en common-SID son regresión, no nueva evidencia independiente. Counterexample esperado no es un acceso financiero real ni fallo de toda S2-B. Capturas originales conservadas; el financial-canary antiguo era objeto sin grant, no tenía positivo y no pasa SI secreto.

## Decisiones técnicas de preparación (no final runtime)

1. SID común de runtime exige separar estrictamente grants privados. No resolver compatibilidad concediendo Users/Everyone al perfil o exports. Probar herencia/default DACL/owner/parent DeleteChild.
2. SeChangeNotify omite comprobaciones de tránsito. Eliminarlo en token transitorio no equivale a cambiar política global y puede impedir acceso a C:/ProgramData o DLLs bajo un SID propio. No suponer que bastará un directorio privado.
3. El harness preparado usa `NtCreateFile` relativo al handle de root del lab para probar tránsito **dentro** del árbol; no amplía ACL Windows. API/ruta/positivos todavía desconocidos. Root handle permanece en harness confiable, no demuestra seguridad de proceso que pueda robarlo o revertir impersonación.
4. Pin/check de todos los ancestros precede cualquier create/report, lab quiescente sin writers concurrentes; post-create alone rechazado. Asunción TOCTOU residual explícita; races/reparse adversariales no se ensayan con este código.
5. LF09 incluye grant READ al peer SID del archivo y positivo de descriptor-only; solo con positivos reales propios y DACL confirmada puede una denegación peer informar de tránsito. No contar object-denial como barrera de directorio.
6. Owner/control SY/BA/OPERATOR se propagan a nuevos hijos code/runtime/observer; protected scratch broad-child conserva OPERATOR. Attempt01/source/plan originales congelados antes de corrección de herencia. Attempt02 corrige el plan, no reescribe resultado histórico.
7. Harness observa permisos de handles; rename/replace, revocation, grupos, ACL reales y rollback tienen procedimientos operadores explícitos. Output raw no es receipt sellado. No PASS agregado ni inferencia SI14.

## Build vs. Reuse

Controles Windows/Win32/NtCreateFile: **WRAP candidato** para probes, referencias Microsoft; no construir sandbox de producción propio ni congelar mecanismo. DACL/Users/new-local-account: REUSE_AS_IS controles del OS con administración autorizada. Codex SDK/app-server oficial conserva WRAP cuando necesario, command-only Windows sandbox REFERENCE_ONLY para esta frontera: `externalSandbox` no crea contención y setup elevated modifica OS fuera del gate. AppContainer sigue REFERENCE_ONLY pendiente de necesidad/probe; sin profile instalado. Skills/metodologías RC2 intactas, ninguna API paga activada.

PAPER_V1_VIABLE_FREE=CONDITIONAL; PAPER_V1_COST=licencia/local sin gasto incremental esperado, tiempo setup/probe no medido; LIVE_COST=UNKNOWN; FREE_ALTERNATIVE=controles nativos/setup manual; PAID_INCREMENTAL_VALUE=no servicio nuevo propuesto; ECONOMIC_JUSTIFICATION_REQUIRED=antes de gasto. No afirmar B más barato o fiable solo por número de cuentas.

## Siguiente gate y pendientes

[QA persistido](probes/r013-s2b-lab-prep/preparation-QA-attempt-01.json) verifica hashes/archivos/invariantes y AST-only; [review independiente](R-013_S2B_lab_independent_review_2026-10-06.md) no identifica nuevos bloqueos P0/P1 para presentar el paquete al owner. No acredita seguridad ni concede permiso.

[S2B-ADM-01](R-013_S2B_lab_ADM01.md): una cuenta estándar temporal, nuevo árbol/ACL canary, pruebas acotadas sin red/login Team y reversión por ledger SID/path. Viejo gate de tres cuentas sigue withheld/DEFERRED. Se requiere autorización explícita por reserva del owner/AGENTS; no autorización administrativa inferida de S2-B.

Luego: viabilidad proceso completo/descendants/supervisor/token/desktop/IPC y egress; auth nativo Team mínimo, profile/cache/recovery y blinding real; reproducibilidad bootstrap, carga TP6 bajo permisos finales y review/freeze. Un PASS parcial FS no cierra D-027/D-024 ni TP4/EB/VP. Plus es PRE-LIVE y no bloquea PAPER; ningún fallback S1 ni escalamiento A/S3 automático.

## Fuentes primarias y tipo de inferencia

- [CreateRestrictedToken](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken): flags/delete list/tokens; contrastados con probe en memoria.
- [Privilege constants](https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants): SeChangeNotify/tránsito; la incompatibilidad de paths del runtime es **hipótesis** hasta test.
- [NtCreateFile user mode](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile): RootDirectory/nombres relativos/create-only/synchronous; wrapper preparado no probado.
- [Impersonation tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/impersonation-tokens): alcance thread distinto de process; no inferir contención de jobs.
- [Codex app-server](https://learn.chatgpt.com/docs/app-server) y [Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox): APIs oficiales como referencia; no setup disparado ni seguridad full-caller probada.

### Parent y versiones del plan después de review

Reviewer exige declarar el bootstrap parent nuevo exacto `C:\ProgramData\TradingOS-S2B-Probe`, owner BA/control SY/BA/OPERATOR y grants mínimos Traverse, separado de recursos trial-01. `lab-policy-plan.json` lo declara y `policy-plan-attempt-03.json` valida 14 FS + 1 parent, solo sintaxis. Attempt02/source/plan ahora también congelados (`*_attempt02_source.*`), además de attempt01; no se reescriben pruebas. Nunca modificar ProgramData; si parent ya existe, parar sin aplicar ni reutilizar. Rollback recursivo solo trial-01; parent transaction-created solo vacío/no-reparse y no recursivo.
