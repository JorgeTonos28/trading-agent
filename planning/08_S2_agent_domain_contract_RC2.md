# S2 RC2 — Agent Domain y contención por job

2026-10-06. **PROPOSED / READY_FOR_DECISION**, dirección S2-B recomendada, no permiso ni implementación. Sustituye como propuesta vigente el mapeo obligatorio rol→cuenta de [S2-A RC1](08_S2_isolation_spec_RC1.md). El objetivo S2 aprobado permanece: frontera financiera técnica. [Comparativa/evidencia](research/R-013_S2_variants_comparison_2026-10-06.md), [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md).

## 1. Dominios, procesos y confianza

| Dominio/contexto | Identidad candidata | Acceso máximo y autoridad |
|---|---|---|
| Financial Core F | Fuera de Agent Runner, identidad/servicio exactos pendientes | Risk/Execution/financial DB/broker secrets; único flujo financiero aprobado |
| Trusted Control C | Fuera de procesos model/tools; no tiene por ello broker credentials | Scheduler/export/admission/epoch/receipts/audit; configura vistas y valida outputs; no agente conversacional |
| Agent Runner A | Una cuenta Windows estándar/restringida dedicada; nombre `TradingOS Agent Runner` conceptual | Native Codex auth legítimo y launch según contrato mínimo; ningún acceso F ni core control; cuenta no creada |
| Trusted job supervisor | Proceso confiable, privilegios mínimos declarados, token/handles/config inaccesibles al job | Puede estar bajo A solo si protección efectiva está demostrada; C permanece externo. Si necesita más privilegio, documentar nuevo dominio y gate; jamás job/model privilegiado |
| Job J | Contexto restringido por instancia/attempt bajo A, mecanismo no seleccionado | Export mínimo readonly, scratch/output aislados, servicios estrictamente allowlisted; ninguna escritura sealed/audit/config ni acceso a otros jobs |
| Research / Quant / Shadow / Pedagogy | Roles lógicos de paquetes, vinculados a J por trusted manifest | Contratos propios, no usernames, SID declarado o prompts como autorización |

Los contextos J pueden usar restricted tokens/AppContainer/contención nativa equivalente probada. TokenUser común no implica token completo común. Un nombre de carpeta, Job Object de lifecycle, command sandbox aislado o `externalSandbox=true` no demuestra este contrato.

La frontera comprende SDK/caller/app-server/CLI, shell cuando autorizado, child processes, callbacks y herramientas. Handler externo con mayores permisos debe validar la operación concreta y no ofrecer ejecución arbitraria. Handler privilegiado dentro del proceso manipulable del job no es external admission. Native tool policy inicial deny-by-default; permisos finales D-024/D-027 todavía abiertos.

## 2. Matriz mínima de recursos

| Recurso | F/C/supervisor autorizado | Job J | Otro job K |
|---|---|---|---|
| Broker keys/core secrets/financial DB/Execution/control financiero | Solo dominio financiero competente | DENY lectura/write/IPC/red | DENY |
| Deployment/code/config/policy/registry/epoch/leases/admission | Lectura/write según dominio, code readonly operacional | Solo paquetes/referencias imprescindibles readonly; no policy/grants/code write | Igual contrato, sin state común modificable |
| Export J y metadatos firmados/sellados por control | Exporter crea, auditor recibe | READ autorizado a IDs/campos exactos | DENY salvo export propio aprobado |
| Scratch y candidate output J | Supervisor controla padres/lifecycle, admission lee bytes delimitados | RW limitado; ningún path traversal/link/owner grant que escape | DENY |
| Raw receipts/sealed/comparisons/audit | Control escribe append/admite; lectores autorizados | No alterar/borrar; vista acotada cuando corresponde | Sin lectura general de otros outputs |
| Profile/auth persistente | Login nativo legítimo y broker mínimo de auth por determinar | Solo lo imprescindible al native runtime; no perfil completo por conveniencia | Sin history/prompts/respuestas ajenos; entitlement compartido no es permiso de datos |
| Supervisor/peer process tokens, memory, handles, desktop | Control externo gestiona | DENY captura, impersonation, duplicación, injection/ventanas y comandos a supervisor | DENY |
| Network/IPC | Endpoint model/auth y operaciones export/submit explícitas | Deny financiero, peer y endpoints no allowlisted; full harness | Igual mínimo, sin canal común amplio |

Mismo usuario base + ACL ordinaria concedida indiscriminadamente a ese usuario no distingue J/K. El mecanismo elegido debe aplicar derechos diferentes a ambos contextos. No grant FullControl/WRITE_DAC/WRITE_OWNER ni parent DeleteChild que permita sustituir exports/code; propietarios de recursos protegidos fuera del job. Probar recursos existentes, aliases/reparse/hardlinks/handles y controles positivos autorizados. No preservar autorizaciones de snapshot previo en token, handles o perfil.

**Propietario fuera del job significa principal y derechos efectivos, no otro PID.** Si supervisor y job mantienen el mismo TokenUser=A, un objeto cuyo owner sea A puede otorgar derechos implícitos de propietario. Declarar y probar owner/DACL/OWNER RIGHTS/integrity apropiados para proceso, token, IPC y filesystem protegidos; ausencia de ACE WRITE_DAC explícita no acredita denegación. VP-03/04 deben intentar READ_CONTROL, WRITE_DAC, WRITE_OWNER y sustitución de DACL, además de memory/token/handles. No exigir otro usuario por anticipado ni asumir que restricted token quita estas rutas automáticamente. [Owner of a new object](https://learn.microsoft.com/en-us/windows/win32/secauthz/owner-of-a-new-object), [OWNER RIGHTS SID](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers).

Focal semántico posterior observó denegación de estos derechos bajo ambos tokens restringidos aun con owner=usuario base en los descriptores sintéticos probados; token base sí obtuvo derechos implícitos. [Evidencia](research/probes/r013-s2-variants/README.md). No bypass observado en ese fixture, sin protección del supervisor real demostrada: mantener VP-03/04 y configuración owner explícita.

## 3. Auth, persistencia y red

Un login base legítimo podría reducir setup respecto de varias cuentas; es hipótesis hasta RB-03. No copiar tokens, usar broker secrets, compartir contraseñas o activar API paga. No autenticar manualmente por job rutinario. Refresh/expiry/revocation/cuota deben producir estados explícitos, nunca ampliar token del job ni volver a usuario developer.

DPAPI CurrentUser puede aportar protección entre el dominio financiero y el Runner si sus usuarios son distintos, con ACL y controles positivos correspondientes. No tratarlo como frontera entre roles bajo el mismo usuario base: el acceso al ciphertext/material necesario y a servicios que descifran debe estar restringido por contexto. Ninguna propuesta de auth/vault final queda seleccionada por este contrato.

Persistencia auth no autoriza persistencia de threads/history/prompts/exports de otro job. CODEx homes/profiles/stores/registry/cache/temp deben inventariarse por writes reales en laboratorio. El mismo AppContainer profile reutilizado también puede conservar datos. Un rol con permisos de scratch no puede plantar información recuperable por otro rol/attempt fuera de su contrato. Estado legítimo de tesis se entrega por export versionado de C, no acceso SQL/store común.

No resolver DLL/registry/cert/auth/refresh dando grants a Users/Everyone o al perfil completo. Toda ampliación se registra con razón, diff y regresión SI/BL. La egress policy cubre inferencia/auth/cliente/hijos, no solo comandos. Host actual reportó merge de reglas firewall locales deshabilitado y block logging false: política/red efectivas UNKNOWN hasta gate competente. No modificar firewall ni instalar proxy/driver en esta fase.

## 4. Blinding experimental independiente

1. C prepara snapshot pareado PIT antes del join contemporáneo Champion; mismos datos legítimos disponibles para decisión, incluidas posiciones previas cuando sean parte del contexto.
2. DAG/campos/versiones establecen qué señales/datos pueden entrar. No reintroducir decisión actual mediante annotations, cache, filenames, metadata o signal calculada desde esa decisión.
3. Shadow recibe solo export predecisión y rol/permisos vinculados externamente; Pedagogy puede recibir trace postdecisión en otro contexto.
4. C captura y sella receipt con job/attempt/epoch/snapshot/config/version/timestamps; solo después se construye comparación Champion vs Shadow. No importar output Shadow al flujo financiero.
5. Intentos de lectura de trace Pedagogy, holdout, outputs antiguos, estado cacheado y proceso supervisor se prueban separadamente de inaccesibilidad financiera.
6. Fallo BL invalida pares para evaluación; no concede autoridad. Timeout/late/no-output no se convierten en HOLD. Puede detener nuevos experimentos/launch según contrato de workflow; no liquidación, cambio Champion ni reanudación financiera.

Namespaces/workflow y snapshots correctos sirven al blinding; su eficacia depende de que job/model no pueda saltar esas interfaces. No necesitamos prejuzgar una cuenta por rol; sí evidencia de ausencia de rutas alternas a datos excluidos.

## 5. Lifecycle, admisión y bootstrap

Manifest externo liga role/job/attempt/epoch/export hash/policy fingerprint/launcher version/effective security context/allowed tools. Una cuenta común obliga a que admission/IPC no confíen solo en SID compartido ni JSON autorreportado. Mecanismo final de binding queda abierto; receipts/capabilities no reutilizables/replayables por peer.

Control verifica setup antes de launch; config drift, audit unavailable, permisos desconocidos o errores bloquean launch. Supervisor inicia contexto mínimo, no hereda environment/handles del developer; fin/crash/retry limpia procesos/vistas y preserva intento. Un retry crea contexto válido nuevo y verifica lease/epoch; como máximo una admisión vigente. No output produce acción financiera. No recovery con job elevado.

Bootstrap fresh clone reconstruye paquetes/contratos/perfiles y binding local sin chat ni auth en Git. Distingue AUTOMATED read-only, USER_ACTION_REQUIRED setup/login, UNAVAILABLE, OPTIONAL y FALLBACK_AVAILABLE. Config OS, creación de perfiles AppContainer/usuarios, ACL/IPC/firewall/login y launch operativo requieren propuesta autorizada. **S2-ADM-01 withheld/deferred; no setup automático.** Validación Team EB/TP/SI/BL/RB; Plus PRE-LIVE.

## 6. Acceptance y escalamiento

[Proyección RC2](research/R-013_S2_variant_acceptance_RC2.md) mantiene SI17/BL9/RB5, añadiendo verificaciones de contexto/supervisor compartido. Resultados semánticos AccessCheck no pasan tests efectivos. No sistema Trading OS implementado; interfaz y matriz son requisitos.

- B falla si job alcanza financiero, otro export excluido, token/handle del supervisor, persistencia ajena o canal no autorizado; registrar FAIL y bloquear candidato hasta remediación verificable.
- B UNKNOWN si falta autorización/login/policy/access/test: no escalar por ausencia de prueba.
- Si B exige perfil/grants inseguros o no diferencia jobs de forma reproducible, comparar **mínima** separación adicional S2-A por dominio de confianza/visibilidad, no por cada rol automáticamente. Mostrar bypass y coste operativo concreto al propietario.
- Si S2 no logra seguridad/IPC/egress/blinding/refresh/bootstrap verificables con controles permitidos, presentar S3; una VM común también debe pasar blinding. No migración ni downgrade silenciosos.

Security, blinding y operación son gates independientes; ninguna puntuación media compensa acceso prohibido. D-027/D-024 RESEARCHING; A+, G1+G2 y ADR-006 intactos. Dirección revisada pendiente de gobierno humano; final topology/permissions/freeze no aprobados.
