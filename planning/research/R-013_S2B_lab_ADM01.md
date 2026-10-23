# S2B-ADM-01 — laboratorio mínimo de filesystem, una cuenta base

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-06. **AUTHORIZED_OWNER_ADMIN_ONLY / SETUP_PENDING / FS_NOT_EXECUTED.** S2-B dirección candidata aprobada en [ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md); D-027/D-024 RESEARCHING. Gate nuevo, no reapertura de S2-ADM-01 (tres cuentas, DEFERRED).

## 1. Decisión exacta

Autorizar un administrador legítimo del host para crear **una cuenta Windows local estándar temporal `tos_probe_runner_b`** y **un árbol de canaries nuevo `C:\ProgramData\TradingOS-S2B-Probe\trial-01` con DACL explícitas**. Ejecutar pruebas breves de acceso a esos recursos bajo la cuenta y dos contextos restringidos; recoger evidencia y **revertir exclusivamente los recursos nuevos identificados por SID/path/marker**.

No se solicita login Team, creación de cuentas por rol, firewall/GPO/local security policy, servicio/task/daemon, red/IPC endpoints, AppContainer profile, broker/runtime financiero, modificación de cuentas/perfiles existentes, copia de auth ni gasto. Tampoco se solicita activar el elevated Windows sandbox de Codex: puede crear usuarios/ACL/firewall fuera de este scope. [Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox).

La arquitectura aprobada permite jobs automáticos; este laboratorio manual y temporal sirve investigación inicial, no selecciona una operativa que requiera intervención por job.

## 2. Cambios y configuración revisables

[Plan declarativo y ACL](probes/r013-s2b-lab-prep/lab-policy-plan.json), [renderer/validator PLAN_ONLY](probes/r013-s2b-lab-prep/policy_plan.py). No contienen password, provisioning ni comandos administrativos ejecutables. Los SID de ejemplo son sintéticos, nunca aplicar sus bindings como si fueran usuarios reales.

| Recurso nuevo | Cambio acotado |
|---|---|
| Cuenta `tos_probe_runner_b` | Crear inicialmente disabled, local estándar, membership únicamente Users `S-1-5-32-545`. Rechazar membership efectiva privilegiada o logon/rights que requieran cambiar política host. No Administrators/Backup/Remote Desktop ni privilegios especiales; no reset si nombre existe |
| Password y logon temporal | Propietario/admin elige contraseña única mediante entrada segura OS local, nunca chat/Git/argumento/log. Habilitar solo ventana del test; launcher/logon legítimo bajo esa cuenta, sin copiar credenciales. Ningún store Codex/broker ni cuenta ChatGPT nueva |
| Raíz nueva y padre nuevo exacto `C:\ProgramData\TradingOS-S2B-Probe` | Ambos new-only; parent es bootstrap fuera del catálogo FS14, no ProgramData. Owner Administrators, DACL protegida: SYSTEM/Administrators y operador confiable control total; Runner + restriction labels solo acceso declarado. Verificar padres ProgramData y ausencia de reparse; no modificar ACL de ProgramData ni de paths anteriores |
| `code/` | Herramienta/test code público pinado + fixture manifest readonly para Runner y ambos contextos. No cambiar permisos de PowerShell/Windows/DLLs/perfil de desarrollo para que cargue; si dependencias inaccesibles, registrar y parar |
| `financial-canary/` | Solo operador/SYSTEM/Administrators. Archivo sintético accesible a operador como positivo, inaccesible a Runner base y ambos contextos. Ninguna credencial real |
| `shadow/export/` y `pedagogy/export/` | BASE Runner read en ambas para positivo comparativo; restricting SID de cada contexto read solo a su export. DACL protegida sin Users/Everyone/Authenticated Users. Ped contiene marcador contemporáneo ficticio; Shadow no puede leerlo |
| `shadow/scratch/` y `pedagogy/scratch/` | BASE Runner + contexto propio Modify, sin WRITE_DAC/WRITE_OWNER en directorios protegidos. Parent/owner fuera del job; archivos nuevos requieren tests de DACL/default/inheritance y tránsito |
| `raw-results/` | Base harness escribe candidato no confiable; contexts no lo leen/escriben directamente. Operador recoge/sella copia fuera de cuenta Runner |
| `trusted-evidence/` | Solo operador/SYSTEM/Administrators, no Runner. Observaciones, source/policy hash, POS/NEG, actor/clock y rollback; Git solo resultado sanitizado |

`BASE`, `OPERATOR` y `JOB_SHADOW/JOB_PEDAGOGY` se resuelven por SID local y descriptor efectivo antes de aplicar. OPERATOR nunca BASE. Job labels son restricting SID numéricos de fixture, **no cuentas/grupos creados**. No cerrar mecanismo final o identidad por job operacional por estos nombres. Matriz usa Read/ReadExecute/Modify/FullControl y OWNER RIGHTS sin grants implícitos en recursos protegidos; masks/templates exactos en JSON. Toda DACL de recurso protegido bloquea herencia de permisos amplios; grants CI/OI solo en subárbol autorizado propio.

## 3. Secuencia y límites del primer laboratorio

1. Confirmar aprobación específica, administrador competente, name/root ausentes y parent/targets sin reparse; baseline de recursos/policy y source Git. Si name/root ya existe, no reutilizar ni alterar: parar.
2. Crear cuenta disabled y árbol protegido; binder verifica SID nuevo, grupos/owner/SDDL y marker de creación. Datos sintéticos, ningún secret movido. Resolver/renderizar diff final de SID/grants antes de ACL: **14 recursos FS + 1 bootstrap parent**, 15 descriptores en attempt03; source/plan anteriores preservados. Fallo parcial → rollback acotado, sin configurar políticas globales.
3. Operador demuestra positivos financieros/evidence y checks de integridad; logon de prueba bajo BASE. Identidad/token efectivo debe coincidir con SID creado, sin grupos/privilegios financieros/developer/admin. No ejecutar como developer y atribuirlo a BASE.
4. **FS-A:** harness de prueba confiable/pinado usa operaciones Win32 bajo thread tokens restringidos del mismo BASE para ensayar DACL de archivos reales. No modelo ni shell adversarial. Restriction labels privados; sin SID común concedido a datos privados. No inferir aislamiento de un proceso completo a partir de impersonación de thread: `CreateProcess` podría usar el token primario BASE. [Impersonation tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/impersonation-tokens).
5. **FS-B:** positivos/negativos/relaunch del catálogo siguiente; collector externo registra errores OS y hashes. Nunca usar paths ajenos al árbol. Sin red, servicios, RPC, inferencia ni API billing. Un runner no implementado/que falla = NOT_TESTED, no PASS.
6. Deshabilitar cuenta, cerrar logons/handles/procesos de prueba identificados, sellar evidencia y aplicar reversión del §5. No dejar cuenta habilitada al esperar otro gate.

No setup executor automático en este paquete; aplicación manual guiada/revisada con native Windows controls tras autorización. El plan declarativo y el protocolo hacen revisables los cambios. Antes de ejecutar un harness real se revisan su source/hash, operaciones/path allowlist y args contra este scope; un cambio de ámbito requiere otro gate. [Harness FS preparado](probes/r013-s2b-lab-prep/filesystem_probe.py), **AST revisado / NOT_EXECUTED**: adapta APIs Windows, no launcher/sandbox productivo. Usa `NtCreateFile` user-mode con `RootDirectory` del laboratorio abierto previamente por BASE/OPERATOR y nombres relativos fijos; evita suponer tránsito por C:/ProgramData bajo un token sin SeChangeNotify y no amplía ACL anteriores. Su viabilidad también es NOT_TESTED. No fallback a token BASE para una operación del contexto. Derechos pedidos añaden SYNCHRONIZE para I/O síncrono; conservar NTSTATUS y error OS. [NtCreateFile](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntcreatefile).

El harness confiable sella todos los ancestros y padres permitidos **antes de crear**, verificando handles/canonical path/no reparse y manteniéndolos abiertos sin write/delete sharing. Requiere lab quiescente, sin otros writers/job/model adversarial. Hay asunción residual TOCTOU en namespace; no probar contención adversarial ni considerar un check post-create suficiente. Si no se puede asegurar quietud o pin, parar sin crear; no probar race/reparse adversarial bajo este gate. Root handle, BASE token y código confiable permanecen en el mismo proceso: esto jamás demuestra aislamiento de un agente que pueda ejecutar código arbitrario.

El binder protegido en `code/local-binding.json` registra gate, referencia externa de aprobación, root, SHA256 de la copia revisada y SID BASE/OPERATOR/job labels. El JSON no concede permiso; comprobarlo contra autorización humana y transaction ledger fuera de BASE. Grupos y privilegios BASE estándar se verifican por operador antes del launch; el harness verifica TokenUser, y sus thread contexts eliminan todos los privilegios y usan SID restrictivo propio. Fallo de identidad/contexto o restore bloquea pruebas; no developer/BASE fallback ni permiso nuevo. Metadatos/SID no son passwords; ninguno se publica como credencial.

Antes de BASE, y después, ejecutar observaciones OPERATOR con IDs diferentes; confirmar existencia/hash y DACL efectiva de cada target negativo (incluido scratch creado después). BASE escribe raw-results no confiable; recoger/sellar desde OPERATOR. Reporte no devuelve PASS agregado. No usar OS_ERROR, missing-path, sharing violation, positivo fallido o API defectuosa como DENY válido.

### Catálogo predefinido

| ID | Control / prueba | Resultado esperado |
|---|---|---|
| LF-01 | Operador lee financial-canary/evidence y modifica fixture controlada | POS funcional y target existente, hash/clock antes/después |
| LF-02 | BASE lee ambos exports/code y escribe raw-results | POS para diferencia efectiva por contexto; BASE no es job operacional |
| LF-03 | BASE lee/escribe financial-canary/trusted-evidence | Access denied distinguible, positivo LF01; no lectura de recursos financieros reales |
| LF-04 | Contexto SHADOW lee export propio y escribe scratch propio | POS, IDs/binding confiables |
| LF-05 | Contexto PED lee export propio y escribe scratch propio | POS, IDs/binding confiables |
| LF-06 | SHADOW↔PED lee export/scratch ajeno y financial-canary | DENY, mismo usuario BASE y contexto distinto; positivos LF01/04/05 |
| LF-07 | Ambos solicitan write/delete/replace/WRITE_DAC/WRITE_OWNER a code/export/root/evidence | DENY; probar permisos efectivos y parent DeleteChild, no mutar ACL si un handle inesperado concede derecho: registrar FAIL |
| LF-08 | Variar grant Users/Everyone en descriptor **solo en memoria** | Counterexample coherente con probe common-SID; ningún grant amplio aplicado a exports reales |
| LF-09 | Crear scratch con READ explícito al SID restrictivo del peer y Users, además de grants propios; positivo propio y AccessCheck peer del mismo descriptor, luego lectura real peer | DENY real necesario después de ambos positivos. No confundir denegación por DACL del archivo con barrera de tránsito. Inspeccionar default DACL/inheritance del archivo normal separado; condición de tránsito/owner verificada. No asumir que directorio privado lo protege. Si preparación exige privilegio adicional, parar sin ampliarlo |
| LF-10 | Revocar vista solo dentro de árbol de prueba, cerrar contexto/relaunch y probar cache/survivor de fixture | No acceso excluido recuperable; cobertura limitada al árbol, profile/registry/temp completo pendientes. No output faltante = HOLD |
| LF-11 | Escribir/reemplazar raw output, collector sella copia con manifest/version/epoch | Receipt externo íntegro, candidato no controla el seal. No audit OS garantizado |
| LF-12 | Reconstrucción instrucciones/política con nuevos bindings y reversión | Diff controlado, exclusión de existentes; sin auth/chat/developer rights |

Todos LF **NOT_TESTED**. ERROR5/denegación real vs missing-path/DNS/timeout distintos. LF-09 fallo invalida esa configuración B, no toda familia B automáticamente; no admitir experimentos contaminados. FS-A prueba recurso real bajo contexto de thread, no SI01/full app-server/SDK. El observer recoge el harness de prueba confiable, sin alegar SI14 contra un proceso adversarial comprometido o auditoría OS activa.

## 4. Lo que queda fuera, explícitamente pendiente

Proceso completo + descendants/supervisor/handles/token/desktop/IPC, full egress, auth nativo Team/expiry/refresh, DLL/registry/profile/cache, carga TP6/recovery sostenido, snapshots PIT/DAG/Champion real, broker/core integrado. VP-01..08 y SI/BL/RB siguen sin acceptance final. **No proceso restringido en default desktop ni pruebas de UI/supervisor** bajo este gate; un future launch gate debe definir private desktop/Job Objects/process ACL e IPC concreto. No elevar job ni ampliar carpetas existentes para resolver compatibilidad. [CreateRestrictedToken](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken).

Q-050 sobre política de red permanece RESEARCHING. Un test offline sin endpoints no demuestra deny broker/loopback. Team login será acción legítima separada; no cuentas por rol ni Plus requerido. Si B no mantiene permisos compatibles: evidencia y remediación acotada primero; alternativa mínima A o S3 mediante gobierno, sin fallback S1 PAPER.

## 5. Reversión exacta, incluida en propuesta

Antes de crear registrar transacción con `created_account_sid`, `created_resource_paths`, marker/hash, hashes código/policy y baseline ausencia; capturar cambios paso a paso. No restaurar objetos que ya existían porque no deben tocarse.

1. Terminar solo procesos/logons de prueba con PID+creation time+imagen/hash/SID de esta transacción; nunca kill por nombre global. Deshabilitar cuenta identificada por SID aunque una prueba falle; error → ROLLBACK_INCOMPLETE y acción de administrador.
2. Guardar copia sanitizada de evidencia en repositorio y copia local confiable; no borrar eventos normales Windows de creación/logon/ACL. Esos logs permanecen como historia de auditoría.
3. Si se creó perfil de usuario, administrador verifica SID exacto nuevo, profile no special/no loaded y ruta asignada a ese SID. Eliminar únicamente ese perfil nuevo con interfaz Windows de perfiles; no borrar `C:\Users` por nombre ni otros perfiles. Si propiedad/path/estado ambiguos, parar y reportar rollback incompleto. Logon de prueba debe evitar carga de perfil cuando sea viable; no asumir que no deja uno.
4. Eliminar la cuenta **solo por SID de creación registrado** después de comprobar que nombre/SID/marker coinciden y no fue reutilizada. No reset de cuentas ajenas; la cuenta temporal no se conserva como cuenta operativa.
5. Eliminar recursivamente únicamente el árbol nuevo resuelto exactamente a `C:\ProgramData\TradingOS-S2B-Probe\trial-01`. Verificar que todos los objetivos recursivos permanecen dentro de ese árbol y sin reparse; si existen enlaces, detener limpieza recursiva y solicitar tratamiento acotado del link, sin seguirlo. PowerShell nativo end-to-end/LiteralPath, sin cmd ni patterns. ACL nuevas desaparecen con esos objetos, ninguna ACL anterior se restaura o amplía. El padre nuevo `C:\ProgramData\TradingOS-S2B-Probe` queda fuera de trial-01: solo eliminar **no recursivamente**, si la transacción demuestra que se creó aquí, sigue vacío y no es reparse. Nunca eliminar ProgramData ni un padre preexistente.
6. Comparar baseline/final: cuenta/SID deshabilitada y eliminada, perfil nuevo eliminado o pendiente explícito, árbol eliminado, código/evidencia protegidos copiados, cero servicio/task/firewall/policy/auth cambios. Solo si todo completado **REVERTED**; nunca reportar reversión completa si quedan residuos. No continuar PAPER con lab pendiente.

Eliminar los recursos nuevos descritos está autorizado exclusivamente mediante la reversión por SID/path/ledger y los pasos administrativos del propietario. Todavía no se ha ejecutado. Si se prefiere conservar evidencia local/árbol, será READINESS=LAB_RETAINED por decisión explícita, no rollback completo.

## 6. Economía y gobierno

PAPER_V1_VIABLE_FREE=CONDITIONAL; PAPER_V1_COST=sin suscripción/API nueva, cuenta local/controles host sin precio incremental esperado, tiempo admin y prueba no medidos; LIVE_COST=UNKNOWN; FREE_ALTERNATIVE=aplicar setup manualmente y native controls; PAID_INCREMENTAL_VALUE=no servicio pago propuesto; ECONOMIC_JUSTIFICATION_REQUIRED=antes de gasto. No instalar framework ni drivers. S3 licencia/recursos por evaluar solo si se justifica después.

**Gobierno resuelto:** propietario autoriza S2B-ADM-01 dentro de este alcance exacto y será el único administrador. Agent prepara/guía/verifica/ejecuta partes no privilegiadas; owner introduce secretos solo mediante UI segura Windows. [Autorización trazable](probes/r013-s2b-lab-execution/authorization.json). No pedir otra aprobación del gate. **USER_ACTION_REQUIRED** corresponde a las acciones administrativas/login concretas. HUMAN_ACTION_REQUIRED antes de ampliar scope; no red, auth Team, policy global, gasto o aceptación final.

## 7. Mapping de cobertura: ningún LF ejecutado

| LF | Fuente preparada / comprobación necesaria |
|---|---|
| 01 | OPERATOR harness financial/export + escritura de reporte; inspección manual de hashes/DACL y positivos sobre scratch antes/después del intento peer. Crear fixture/control existe desde setup |
| 02 | BASE harness code/exports, raw-report positivo; escritura de scratch bajo cada contexto. No sustituye comprobar grupos/permisos base |
| 03 | BASE harness financial read y máscaras write/DeleteChild/delete/WRITE_DAC/WRITE_OWNER financial-file/dir/evidence-dir; lectura evidence/control y permisos del collector se comprueban por operador. No todos los objetos de evidence ensayados automáticamente |
| 04–05 | Harness propio read/write, cero privilegios y TokenUser; si positivo falla, NO ACCEPTANCE |
| 06 | Harness exports/financial/peer broad-scratch después de crear; scratch normal peer y SDDL de archivos creados requieren control del operador |
| 07 | Harness máscaras sobre code/config/export/file/financial/evidence/raw y DeleteChild dirs; root y sustitución/rename/replace efectivo son procedimientos manuales **pendientes**, no cubiertos por abrir un handle. No alterar objeto protegido si un derecho se concede: FAIL |
| 08 | Probe ejecutado solo en memoria, evidencia ya disponible; no gate efectivo por ello |
| 09 | Harness peer child-object positive + propio real + peer real, con privilegios declarados; operador verifica DACL aplicada al archivo y positivos persistentes. Ruta relativa/pin son NOT_TESTED; fallo API/setup invalida caso |
| 10 | Procedimiento operador: revocar grant propio solo a un fixture/export de este árbol, cerrar contexto y reabrir; registrar handles supervivientes. Sin profile/cache/registry global; puede revelar gap, no full revocation PASS |
| 11 | Operador captura raw, hash/context/epoch y copia readonly a trusted-evidence; intento BASE de alterar seal se verifica allí. No SI14 contra proceso comprometido |
| 12 | Operador vuelve a renderizar bindings, compara setup y ejecuta rollback con ledger; nuevo run después de reversión requiere recursos nuevos autorizados y otra referencia de transacción |

Ledger externo mantiene estado de cada caso: NOT_TESTED/PASS_SCOPED/FAIL/ERROR/INVALID_POSITIVE, evidencia y exclusiones. Un proceso con exit 0 no pasa LF01–12. Todos los gates completos SI/BL/RB/VP permanecen NOT_TESTED.

## Autorización posterior — propietario, 2026-10-06

Los estados NOT_AUTHORIZED de fuentes/capturas de preparación describen su fecha original, no se reescriben. El owner aprueba únicamente cuenta estándar temporal/parent-tree/ACL declaradas/tests sintéticos/evidencia/reversión. Conserva cada exclusión original. Sole admin owner, secret input Windows UI only. [Guía de ejecución por fases](R-013_S2B_owner_execution_runbook.md) registra transacción, acciones manuales y evidencia; aún no cuenta/setup FS ejecutado por el agente. D-027/D-024 RESEARCHING.

## Handoff concreto dentro de scope — 2026-10-06

[Helper owner-only](probes/r013-s2b-lab-execution/owner_lab.ps1) y [runbook](R-013_S2B_owner_execution_runbook.md) automatizan exclusivamente nuevas creaciones/ACL declaradas cuando **el propietario** lo ejecuta con elevación. No provisioning del agente ni permiso operacional. Usa PowerShell 7 ya existente; 5.1 policy blocked se registra y no se modifica. APIs oficiales con create-new/descriptor inicial, mismas grants y 15 targets; trusted-evidence se crea antes de fixtures. Journal sanitizado es artefacto del repositorio, no configuración del host. Binder/ledger SID locales solo dentro de lab; copia local de metadatos de ledger, sin secretos, se retiene ignorada en `.local/` para comprobar export antes de rollback.

Orden seguro de reversión del helper: cuenta deshabilitada + ausencia de procesos/perfil verificada → evidencia exportada → tree exacto → parent nuevo vacío → cuenta por SID revalidado. Mantiene identidad para verificar los paths hasta terminar, evita perder atribución por eliminar la cuenta antes del árbol; mismos recursos aprobados, sin restore de ACL anteriores. Un error parcial o UNKNOWN bloquea automatización y exige revisión owner y reversión de recursos atribuidos, no limpieza por patrón. No ejecución administrativa todavía.
