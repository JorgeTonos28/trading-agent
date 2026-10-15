# S2-B — preparación de laboratorio, sin setup

2026-10-06. **No cuenta/ACL/firewall/credencial/config global creada o modificada.** [Gate concreto](../../R-013_S2B_lab_ADM01.md), [hallazgos](../../R-013_S2B_lab_preparation_2026-10-06.md). PAPER Team, Plus PRE-LIVE; implementación bloqueada.

## Common-SID y privilegios: probe realizado únicamente en memoria

`common_sid_probe.py` adapta source AccessCheck previo; `common-sid-attempt-01.json` preserva resultado y SHA256 ejecutado. Base Git b0d6818 (aprobación dirección), source/hashes locales en JSON. No impersonación efectiva, child process, filesystem ACL, Windows account/group/profile, red o auth. SID BUILTIN Users `S-1-5-32-545` se añade **a la lista restrictiva transitoria**, no a un grupo ni cuenta real. SID real TokenUser solo interno, no emitido.

12 observaciones de descriptor/token y dos verificaciones de privilegios:

| Descriptor | Tight Shadow (SID propio) | Shadow + common Users | Pedagogy + common Users |
|---|---|---|---|
| Export Shadow privado | ALLOW | ALLOW | DENY |
| Trace Ped privado | DENY | DENY | ALLOW |
| Read común runtime | DENY | ALLOW | ALLOW |
| Trace con grant común amplio | DENY | **ALLOW: counterexample de configuración** | ALLOW |

`DISABLE_MAX_PRIVILEGE` conservó SeChangeNotify habilitado. Crear un **handle transitorio** con Flags=0 y lista de todos los privilegios a borrar dejó cero privilegios. No se cambió el token del proceso corriente, grupos OS ni user rights globales. La documentación describe que SeChangeNotify omite comprobaciones de tránsito; **no** se probó un traversal real ni que eliminarlo sea compatible con Codex/DLL/filesystem. [CreateRestrictedToken](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken), [privilege constants](https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants).

Los diez checks originales son regresión del harness, no diez evidencias nuevas. El control original financial_canary sigue ungranted-object, sin positivo ni acceso financiero demostrado. Counterexample no declara toda S2-B fallida: prohíbe grants comunes en datos excluidos y exige tests de inheritance/owner/scratch/traversal. Todos SI/BL/RB/VP/LF efectivos NOT_TESTED.

## Plan, renderer y ejecución posterior

`lab-policy-plan.json` es un contrato declarativo de recursos nuevos. `policy_plan.py` funciona **solo PLAN_ONLY**, construye/valida SDDL en memoria y guarda/retorna un reporte sintético; no aplica ACL, crea cuentas, cambia usuarios o lanza jobs. Bindings ejemplo completamente sintéticos; futuro admin resolverá valores locales protegidos. No ejecutar SDDL de ejemplo como configuración real.

Reproducción del renderer: `python policy_plan.py --output <new-report.json>`. Rechaza overwrite; salida solo archivo explícito permitido, no target operacional. Prueba common-SID rechaza overwrite de evidencia; otro intento requiere copia+OUT distinto y nuevo hash/source. No reescribir el original.

Este paquete no contiene provisioning executor ni launcher operativo. Después de permiso específico se usa aplicación manual revisada y un harness desechable FS con operaciones/path limitadas al árbol, source/hash revisados; ningún resultado de thread-token filesystem equivaldrá a full SDK/process isolation. No ejecutar setup ni native windowsSandbox/setupStart al leer estos archivos.

## Artefactos y controles de ejecución

- `policy-plan-attempt-01.json` queda ligado a `policy_plan_attempt01_source.py` y `lab-policy-plan_attempt01_source.json` congelados. Attempt02 liga source/plan `*_attempt02_source.*` congelados, con SY/BA/OPERATOR OI/CI; 14 SDDL válidos solo sintaxis. Attempt03 liga source/plan activos y declara parent bootstrap nuevo exacto: 14 FS + 1 parent, 15 descriptores válidos **solo sintaxis**.
- `preflight_readonly.ps1` / `preflight-attempt-01.json`: ausencia de nombre/root/parent, metadata ProgramData y paths locales. Revalidar; no prueba autoridad, policies ni tool access del nuevo Runner.
- `filesystem_probe.py`: **NO EJECUTADO**, AST-only. Tras autorización, OPERATOR copia código revisado a `<lab-root>/code`, resuelve `local-binding.json` protegido con campos `gate`, `owner_approval_reference`, `root`, `source_sha256` y `bindings` BASE/OPERATOR/JOB_SHADOW/JOB_PEDAGOGY. No secrets; SID reales quedan solo en lab protegido. Un JSON autorreportado jamás autoriza setup.
- CLI futuro de harness: `python <lab-root>/code/filesystem_probe.py --actor OPERATOR --run <id-unico>` antes/después, BASE durante ventana. No ejecutar desde checkout de desarrollo; no impersonar otra cuenta aquí. Source/hash/actor/relative paths vienen de revisión externa.
- `NtCreateFile` relativo a root confiable + thread token sin privilegios: adapter **NOT_TESTED**, sin fallback absoluto/base ni permiso amplio. Base root handle no está aislado de código adversarial en el proceso; FS-A es harness de prueba confiable. Pin previo de ancestros/parents y lab quiescente necesarios; residual TOCTOU explícito, sin race/security sandbox claim.
- Mapping LF01–12 automático/manual y rollback exacto en gate: todos NOT_TESTED. Peer-child tiene grant READ al SID restrictivo peer y Users, con positivo descriptor-only y propio; validar DACL real antes de interpretar tránsito. Root/replace/rename y revocation no se dan por cubiertos por un open handle.

No cuentas/config creadas. No native Windows sandbox setup, login Team, red, instalación/runtime operacional ni gasto. Source hashes de capturas identifican bytes locales ejecutados; para fresh clone usar blob Git pinado y registrar diferencias EOL, no reescribir evidencia para que coincida.

[QA de preparación](preparation-QA-attempt-01.json): correspondencia de hashes originales/archivados, invariantes/paths, plan 14+1 y AST-only del harness; no ejecución nativa. [Revisión independiente](../../R-013_S2B_lab_independent_review_2026-10-06.md) permite presentar el gate para gobierno; no da aceptación efectiva ni permiso administrativo.
