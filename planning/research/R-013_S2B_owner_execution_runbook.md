# S2B-ADM-01 — ejecución por el propietario y verificación sin elevación

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-06. Autorización recibida; **SETUP_PENDING / FS_NOT_EXECUTED**. [Scope aprobado](R-013_S2B_lab_ADM01.md), [autorización](probes/r013-s2b-lab-execution/authorization.json). Transacción `s2b-20261006-a6d74b2b`. El propietario es el único administrador; el agente no solicita elevación ni recibe secretos. PAPER Team sin autenticación Team en este laboratorio.

## 1. Primera acción manual: cuenta deshabilitada

1. Abrir **Administración de equipos** como administrador, aceptar UAC personalmente y entrar a **Usuarios y grupos locales → Usuarios → Usuario nuevo**. Alternativa de acceso: `Win+R`, `lusrmgr.msc`; si esa superficie necesita elevación, abrirla personalmente como administrador. No cambiar políticas ni instalar snap-ins si no está disponible.
2. Nombre exacto: `tos_probe_runner_b`. Descripción exacta: `TOS S2B-ADM-01 s2b-20261006-a6d74b2b`.
3. Introducir una contraseña nueva solo en los campos protegidos de Windows y confirmarla allí. No compartirla ni copiarla a archivos/comandos/chat. Desmarcar «El usuario debe cambiar la contraseña en el siguiente inicio de sesión» para este ensayo temporal; **marcar «Cuenta deshabilitada»**. No activar password-never-expires ni cambiar reglas host.
4. Crear únicamente esa cuenta. Verificar en **Propiedades → Miembro de** que es estándar y pertenece únicamente a **Users/Usuarios** (`S-1-5-32-545`). No agregar privilegios, otros grupos o cuentas Microsoft/Team. Si Windows requiere un cambio de política o si el nombre ya existe, detenerse.
5. Responder solo **«cuenta creada y deshabilitada»**. La verificación obtiene SID y estado sin contraseña. No enviar capturas del formulario con datos de credenciales.

La baseline readonly 18:25 UTC registró nombre/parent/root ausentes y proceso del agente no elevado. Revalidar ausencia del árbol antes de setup; no reutilizar recursos que aparezcan entre fases.

## 2. Helper administrativo de ACL: solamente el propietario

[Owner helper](probes/r013-s2b-lab-execution/owner_lab.ps1) aplica únicamente el plan declarado a recursos nuevos y registra ledger por SID/path/transacción. No crea usuarios, pide passwords, habilita billing, lanza procesos, cambia execution policy ni firewall/config global. Usa **PowerShell 7 de 64 bits existente**, adapter de APIs oficiales CreateDirectoryW/CreateFileW para aplicar descriptor inicial con create-new; no requiere instalación. Windows PowerShell 5.1 bloqueó el QA por policy: no Bypass, Unblock-File o cambios de policy para resolverlo. PowerShell 7.6.5 pasó AST/memoria/compilación sin llamadas nativas. No asumir disponibilidad global en PATH ni bajo Runner: el agente entregará el path/hash observado del ejecutable al owner antes de esta fase.

Antes de ejecutar: agente verifica cuenta estándar/deshabilitada y fuentes/versiones; el helper comprueba aprobación, source hashes, identidad operador distinta de Runner, elevación del propietario y ausencia de parent/root. `-Phase Plan` hace preview sin mutaciones; `-Phase Setup` crea parent + 14 recursos del catálogo, copias mínimas code/binding, fixtures sintéticos y ledger local protegido. DACL propietario BA, SY/BA/OPERATOR FullControl, grants mínimos BASE/job según policy; jamás ACL de ProgramData o paths anteriores.

Cuando la cuenta haya sido verificada, abrir personalmente **el ejecutable PowerShell 7 observado → Ejecutar como administrador**. Primero ejecutar Plan; el agente revisará el resultado antes de Setup en la misma identidad:

```powershell
& 'C:\Dev\Proyectos\Trading-agent\planning\research\probes\r013-s2b-lab-execution\owner_lab.ps1' -Phase Plan
```

Solo después de `PLAN_ONLY` correcto y revisión del agente (cuenta disabled/standard, 15 recursos, cero cambios), ejecutar en la misma identidad:

```powershell
& 'C:\Dev\Proyectos\Trading-agent\planning\research\probes\r013-s2b-lab-execution\owner_lab.ps1' -Phase Setup
```

No `ExecutionPolicy Bypass`, instalación ni cambio de políticas. Si ejecución se bloquea, reportar solo el error sin secretos y parar. Capturar exclusivamente resumen sanitizado de transacción, recursos creados y estado; SID/SDDL locales permanecen en ledger/binding protegido del lab. Journal sanitizado flushed antes de crear conserva evidencia incluso si aún no existe ledger. Un error parcial conserva cuenta deshabilitada y exige reconciliación/atribución owner antes de cualquier retry o cleanup; **no volver a Setup sobre recursos existentes**. Ver §7.

## 3. Verificación, ventana de pruebas y login seguro

1. El agente, en su sesión **no elevada**, verifica con `owner_lab.ps1 -Phase Inspect` source/hash, owner/DACL/target, ledger completo, binder y cuenta/SID/grupos, después positivos OPERATOR. OPERATOR es el SID real de Setup; si UAC usa otra cuenta y el agente no puede recoger evidencia, USER_ACTION_REQUIRED para collector legítimo, nunca ampliar ACL/suplantarlo. Prueba funcional positiva bajo operador no prueba BASE.
2. Propietario habilita únicamente la cuenta temporal para la ventana de test mediante sus Propiedades en Windows, después de validación del setup. Ninguna modificación de otra cuenta.
3. Propietario abre **Windows PowerShell como otro usuario** mediante la interfaz Windows (Shift/clic derecho → «Ejecutar como otro usuario», donde esté disponible). Windows Security recibe `.\tos_probe_runner_b` y su password directamente del propietario. No introducirlo en consola, `runas` con password/archivo, Get-Credential, Start-Process Credential, environment o chat. Si Windows requiere derechos de logon/política adicionales, detenerse sin concederlos. Los comandos interactivos públicos para lanzar Python no requieren ejecutar un script PowerShell o cambiar su policy.
4. En esa ventana no elevada y exclusivamente como Runner, comprobar `whoami` localmente y ejecutar el comando público del harness que se entregará tras validar el setup. Usar Python existente, código del lab y run ID único; no instalar runtime ni ampliar sus ACL para que arranque.
5. Cerrar la ventana Runner y deshabilitar la cuenta desde Windows al terminar, incluso ante error. Sin Team login, Codex job ni red. Un nuevo perfil creado por el login pertenece al SID temporal y se registra para la reversión descrita en el gate; no tocar un perfil existente.

El agente no puede iniciar esa sesión sin tu login seguro y no sustituirá la prueba ejecutándola como desarrollador. El script FS es harness confiable de threads, no proceso agéntico adversarial. Root handles/tokens pertenecen al harness; no se conceden a un modelo.

## 4. Evidencia y criterios

Ledger protegido en `trial-01\trusted-evidence\ledger-local.json`, binder readonly en `code\local-binding.json`. Solo fixtures/código públicamente revisados y metadatos de acceso; ningún secret. Raw BASE se recoge como candidato y se sella desde OPERATOR con hashes/version/run/clock; evidencia Git sanitizada excluye SID reales/nombres host/perfil.

LF01–12 mantienen su mapping automático/manual en el gate. Cada caso puede PASS_SCOPED/FAIL/ERROR/INVALID_POSITIVE/NOT_TESTED. Recursos negativos deben existir y tener positivo autorizado; missing path, sharing violation, malformed API o positivo fallido no equivalen DENY. File grants e inheritance/default DACL se inspeccionan antes de interpretar LF09. Abrir un handle no cubre rename/replace/revocation/OS audit. No agregar PASS de seguridad completo desde exit 0.

[Evaluador externo](probes/r013-s2b-lab-execution/evaluate_filesystem.py) es solo lectura; por defecto deja corroboración externa pendiente. Wrong identity/source/binding impiden PASS; grants no atribuibles son ERROR/señal que bloquea aceptación; grants prohibidos válidamente atribuidos son FAIL aun si otro positivo falló. DeleteChild se evalúa solo en directorios. Root/rename/replace, scratch normal peer/DACL real, revocation/survivor/relaunch, seal/rollback requieren procedimientos externos del mapping §7 del gate. Antes de cada procedimiento manual entregar comando/diff y revisar dentro del scope; no ejecutarlo sin preparación.

## 5. Reversión y residuos

1. Propietario cierra la sesión/pruebas Runner y deshabilita la cuenta por SID validado; no kill global ni cambios a sesiones ajenas.
2. Agente recoge/sella datos sintéticos y publica resultados sanitizados. Guardar copia del ledger de metadatos en `.local/s2b-execution-private/s2b-20261006-a6d74b2b/ledger-copy.json`, ignorada por Git, antes de borrar el árbol. Esa carpeta no es un secret store financiero. Reporte público en `probes/r013-s2b-lab-execution/filesystem-evaluation.json`; ningún SID real/host/profile. Preparar nuevo receipt control-only `trusted-evidence/export-verified.json`: transaction/gate, path/hash/length de ledger/copia y path/hash del reporte. El helper verifica ACL del receipt y existencia/hash/length reales: booleans solos no pasan.
3. Si Windows creó perfil del nuevo SID: propietario, en **Propiedades avanzadas del sistema → Perfiles de usuario**, verifica que sea únicamente el perfil temporal, no especial ni cargado, y lo elimina. No eliminar `C:\Users` por patrón. Ambigüedad o perfil cargado = rollback pendiente.
4. Helper `-Phase Rollback` requiere cuenta deshabilitada, sin perfil/sesión/proceso atribuible pendiente, ledger protegido completo (status/manifest18/source/policy/helper), journal corroborado y export válido; propietario ejecuta con elevación. Elimina root exacto sin reparse, padre nuevo vacío no recursivamente y cuenta por SID/marker revalidado al final, conservando identidad hasta terminar el árbol. Cualquier GetOwnerSid distinto de cero/query error con proceso existente es UNKNOWN y bloquea **todo delete**; owner inspecciona PIDs/creation times concretos en Windows/Task Manager y registra atribución/ausencia para reconciliación. No matar procesos del sistema ni ampliar policy para pasar. No borra eventos Windows normales, perfiles ajenos o padres anteriores.
5. Agente verifica cuenta/SID, parent/root, perfil y residuos. Estado REVERTED solo con todos los controles cumplidos; en otro caso ROLLBACK_INCOMPLETE y acción exacta del owner.

## 6. Entrega final y siguiente gate

Reporte persistido: PASS/FAIL/ERROR/NOT_TESTED por caso; alcance demostrado/no demostrado, viabilidad condicional S2-B, rollback y residuos. Una falla de fixture/API produce ERROR/INVALID y no condena automáticamente S2-B; un acceso efectivo prohibido es FAIL y bloquea esa realización hasta reparación/gobierno.

Ni FS PASS acepta S2-B ni cierra D-027/D-024. El siguiente gate propuesto **S2B-PROC-01** abordará proceso completo, supervisor/tokens/handles/descendants/private desktop e IPC con artefactos y scope propios; egress/policy store y native Team auth quedan posteriores y requieren autorización específica. No usar esta autorización para red/auth/VM ni aceptar arquitectura financiera implementada.

## 7. Journal y recuperación parcial

`owner-transaction-local.jsonl` es un artefacto sanitizado del repositorio, no configuración OS: INTENT durable antes de cada creación, VERIFIED después, SID fingerprints/descriptor hash/paths fijos, nunca SID real/secreto. No se alteran ACL fuera del lab. Ledger/binder locales están protegidos; la primera creación puede preceder su existencia. Journal editable no es autoridad de borrado ni prueba de autenticidad adversarial.

Setup parcial **siempre bloquea Rollback del helper** y prohíbe launch/retry. El agente recoge journal/baseline y coteja marker/SID, paths/ACL/creation metadata reales y eventos. El propietario confirma atribución real; solo entonces se preparan pasos exactos de reversión de recursos atribuibles dentro de SID/path originales. INTENT sin VERIFIED, journal truncado/alterado, ACL inesperada, child ajeno u objeto reutilizado requieren revisión; no reescribir eventos para inventar procedencia. Cualquier expansión exige HUMAN_ACTION_REQUIRED. Mantener quiescencia durante check/delete; no alegar resistencia a race hostil.

## Fuentes primarias del helper

- [CreateDirectoryW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createdirectoryw): descriptor inicial, error si existe.
- [CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew): CREATE_NEW y descriptor inicial, sin open idempotente.
- [GetOwnerSid](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/getownersid-method-in-class-win32-process): cero éxito; otro retorno error.
