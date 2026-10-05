# S2 — dominios, permisos y fronteras PAPER RC1

2026-10-05. **Especificación candidata** R-013/D-027 P1 bajo [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md). Dirección aprobada; configuración administrativa **NO autorizada**, aceptación efectiva **NOT_TESTED**. D-024 RESEARCHING, implementation_locked=true. No Trading OS implementado. Completa [seguridad RC0](08_agent_security_contract_RC0.md); no modifica A+, G1+G2 ni ADR-006.

## 1. Threat model y dos objetivos

**Security isolation:** tratar el job, SDK/app-server, handlers dentro de su proceso, fuentes y outputs como potencialmente comprometidos. Impedir que alcancen credenciales, estados financieros, Execution/broker, control confiable o permisos adicionales. Un handler local al job no puede ser la barrera que protege un recurso al cual ese mismo proceso tiene acceso.

**Experimental blinding:** aunque el proceso no tenga autoridad financiera, impedir que Shadow acceda a decisión/razones/output contemporáneos Champion, evaluación posterior, outcomes futuros, pedagogía o otros intentos excluidos del snapshot. Compartir contexto elegible no implica compartir la decisión. Seguridad puede pasar y blinding fallar: reportes/gates separados.

| Amenaza | Activo / frontera | Mitigación candidata y evidencia exigida |
|---|---|---|
| Inyección en Skill, filing, señal o output | Tools, export, admission | Schema/args/rol externos; tools por ID; rechazo de métodos desconocidos; tests con instrucciones hostiles |
| Proceso job comprometido, shell inesperada | Credenciales, core, stores | SID/token independiente sin privilegios; ACL/process handle/IPC/egress efectivos, no solo flags de comandos |
| Permisos heredados, grupo amplio, owner writable | ACL/config/binaries | DACL explícita administrada; no developer/admin SID en token; paquetes/config no writable; proceso no dueño de recurso protegido |
| Traversal, junction, symlink, hardlink, alternate stream, TOCTOU | Export/output/collect | Resolver por handles/identidad final; rechazar reparse/alias; receipt confiable de bytes sellados; tests de sustitución |
| Named pipe por defecto, loopback, servicio local | Core/control/DB | DACL/SID autenticado y operación concreta; deny red local no autorizada; endpoint no expuesto al job |
| IPC falsificado, handle/env heredado | Dispatcher/admission | Parent confiable de capacidades mínimas, herencia explícita de handles; principal derivado OS, no del JSON |
| Store/caché/chat compartido entre roles | Shadow/holdout | Dominios/exports/stores separados; sesiones nuevas; linaje predecisión; cuarentena de splits |
| Drift/config/plugin/scheduler comprometidos | Paquetes/control plane | Pins, fingerprint efectivo, trusted launcher fuera del job, no autoupdate ni permisos por output |
| Reintento/reboot/restore | Históricos/leases/snapshots | Epoch/envelope/fencing; preservar receipt; nunca nueva autoridad o duplicar efectos financieros |

Trusted Computing Base candidata: Windows/kernel, operador administrador, launcher mínimo, exportador, validator/admission, audit y core determinísticos. Un administrador host comprometido puede eludir ACL; S2 no promete aislar del administrador/kernel. Error en componentes confiables sigue siendo riesgo sujeto a review/tests. S3 en el mismo host tampoco elimina administrador comprometido.

## 2. Matriz concreta de identidades — propuesta, no cuentas creadas

Nombres ilustrativos para configuración reproducible; binder registra **SID efectivo** localmente, no nombres como autenticación. No reutilizar cuentas existentes ni asumir que todas las funciones deben ser sesiones Codex separadas. Dominios de seguridad ≠ número final de agentes de D-024.

| Dominio / identidad candidata | Procesos / permisos mínimos | Filesystem y secreto propio | IPC/red admisible |
|---|---|---|---|
| F / `tos_core` | Core, Risk, Execution futuros; usuario servicio no admin | Estado financiero RW, broker secret propio; sin auth Codex | Broker/market-data seleccionados y control financiero autenticado; nunca aceptar job agent |
| C / `tos_control` | Launcher/workflow/export/admission; no LLM | Jobs/audit RW, releases/config R; sin broker secret; vista de snapshot exportable R por interfaz | Iniciar procesos con credencial de lanzamiento protegida; interfaz export aprobada, no órdenes; transport propio sin broker |
| R / `tos_research` | Research/Quant jobs y SDK/app-server del dominio | Export research permitido R; workspace propio temporal; auth Team propia | Solo transporte native Codex aprobado; tool lectura IDs; sin core/control endpoint |
| S / `tos_shadow` | Shadow jobs y SDK/app-server | Snapshot pareado R; workspace/output propio; auth Team propia | Solo transporte native Codex; no R/P/H namespaces; no Champion/control |
| P / `tos_pedagogy` | Pedagogical jobs y SDK/app-server | Trace factual posdecisión R; workspace/output propio; auth Team propia | Solo transporte native Codex; no escritura/control core ni namespace Shadow |
| H / `tos_evaluator` | Evaluación determinística offline de pares/holdout | Outputs sellados + join Champion R; evaluación derivada RW | Sin broker/orden; no publicar outcomes al job; acceso holdout solo fase aprobada |
| O / operador humano | Aprobar setup/config/reset material; instalar release aprobado | ACL/config protegidas administradas; backup protegido | Acceso administrativo exclusivamente fuera de procesos modelo |

Plan Architect/desarrollo permanece en entorno actual sin secretos, separado de despliegue. Onboarding inspecciona/reporta; no adquiere por ese rol SID administrador. Plan Guardian permanece inactivo hasta freeze. Dividir R en research y quant si vistas/holdouts/permisos divergen; no cerrarlo antes de D-024. Cada dominio requiere login Team legítimo si usa Codex: **no copiar auth.json/tokens**. Accounts launch/rights/control privilege exactos quedan gate administrativo separado; no dar SeTcb/SeDebug/admin al modelo ni convertir launcher amplio en broker.

## 3. Contrato filesystem — rutas candidatas fuera del checkout de desarrollo

Raíz operacional candidata `C:\ProgramData\TradingOS\<deployment-id>\`; **no creada**. Release readonly desde tag/commit aprobado futuro; `plan-architect` solo probes. Nada de usar checkout completo más stores reales como workspace modelo. Administrador/SYSTEM gestionan propietarios y DACL; grants explícitos por SID, broad groups no reciben grants operativos. No grant `FullControl/WRITE_DAC/WRITE_OWNER` al job en recursos protegidos. Una ausencia de grant individual no prueba deny si un grupo suyo permite.

| Recurso | F | C | R | S | P | H |
|---|---|---|---|---|---|---|
| `release/` paquete específico + shared permitido | R/X | R/X | R/X subset | R/X subset | R/X subset | R/X |
| `config/trusted/`, job registry, leases, receipts, audit | — | RW | — | — | — | R audit autorizado |
| `financial/state/`, core logs y broker material | RW | —; export API mínima | — | — | — | —; export específico |
| `exports/research/<job>/<attempt>/` | — | crear/sellar | R activo | — | — | R autorizado |
| `exports/shadow/<job>/<attempt>/` | — | crear/sellar | — | R activo | — | R después de seal |
| `exports/pedagogy/<job>/<attempt>/` | — | crear/sellar | — | — | R activo | R autorizado |
| `work/<domain>/<job>/<attempt>/scratch-output/` | — | recoger bytes | RW suyo | RW suyo | RW suyo | — |
| `sealed-evidence/`, `pair-join/`, `champion-contemporary/` | origen export | RW | — | — | —; trace export separada | R autorizado |
| `holdout/confirmatory/` | — | export según fase | — antes de apertura | — | — | R solo autorización |
| Auth native Codex y caches de otro dominio | — | — | — ajeno | — ajeno | — ajeno | — |

`—` significa acceso denegado requerido, no comprobado. R/X distingue paquetes ejecutables del contenido/snapshot solo R. C no monta DB financiera: interfaz de export determinística entrega campos autorizados y no acepta orders. El mínimo privilegio de esa interfaz tendrá revisión con Strategy/data/core; ningún job puede conectarla directamente.

Eliminar herencia amplia en el **árbol nuevo autorizado**, no modificar repo/perfil personal/sistema por defecto. Administrador/SYSTEM propietarios de export/code/config/sealed stores; permisos efectivos de cada token y grupos registrados. Job puede escribir scratch/output, nunca snapshot/sellos/audit/receipts. Evitar permisos DeleteChild en padre que permitan reemplazar hijos protegidos. Rechazar enlaces y resolver volumen/file-id/reparse final antes de collect; validar tamaño/schema/digest de los bytes **copiados al store confiable**, no confiar en una ruta mutable del job. Output posterior a receipt no sustituye original.

Cada lanzamiento nuevo recibe solo export/paths activos; revocar vista previa y destruir proceso anterior/handles antes de reutilizar identidad. Identidad por dominio no aísla jobs simultáneos del mismo SID: prohibir concurrencia allí salvo frontera por job demostrada; los jobs no necesitan ver históricos/caches de su dominio. Si mantener ese aislamiento exige cuentas por job, containers/VM o amplia reconfiguración, documentar coste y volver a D-024; no asumir aislamiento por nombre de carpeta. Tests intentan lectura/reemplazo desde mismo dominio y dominios hermanos, durante/después de reuso.

[Microsoft icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls) documenta DACL, herencia y derechos. `/verify` comprueba estructura, no acceso efectivo: el gate lanza accesos reales bajo cada SID. Privilegios/protección de handles tienen [controles de proceso](https://learn.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights); probar lectura de memoria/token/handle canary sin SeDebug ni handle heredado. No inspeccionar memoria de procesos personales reales.

## 4. Secretos, entorno y autenticación

1. Broker/data/DB financieros solo F o servicio mínimo autorizado; no variables de entorno, repositorio, argumentos, mounts, logs, backups agénticos o herramientas con valores reales. **Todos los primeros tests usan canaries sintéticas.** Probar lectura y escritura de archivo canary + acceso al proceso canary, no credenciales reales.
2. Native Team auth reside en perfil protegido del dominio correspondiente y se establece mediante login oficial del propietario. Identidad Codex legítima no demuestra por sí sola permiso de unattended launch en Windows; fase posterior valida login/refresh/logout/quota sin API fallback. No export/copiar token entre cuentas ni usar un profile compartido con R/S/P.
3. Carga del child env desde allowlist versionada: variables OS mínimas, job-local TEMP/TMP, paths binarios pinados; no heredar env de desarrollo, proxy, APIKEY, broker/data vars, startup hooks, PYTHONPATH o stores ajenos. No registrar valores. Auth/env requeridos por cliente se habilitan por necesidad documentada; never drift auto-allow.
4. Handle inheritance explícita solo stdio del job; no handles core/store/token. Launcher mantiene sus credentials y privilegios fuera del modelo. Recovery no eleva job; login revocado → AUTH_BLOCKED/owner, nunca API pagada o import de auth ajena.
5. Evaluar DPAPI **CurrentUser + ACL** para secretos locales F/launcher; no decisión de vault final. La protección de máquina por sí sola no separa usuarios: [CryptProtectData](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) permite descifrar a otros usuarios si usa LOCAL_MACHINE. Probar cripto con canary y dos SIDs tras gate; backups/rotation/manual recovery no se diseñan alrededor de export de token ni contraseña en Git.

## 5. IPC/control

Primera interfaz job↔caller: stdio de su **propio** SDK/app-server sin listeners amplios, parent mínimo. C entrega manifest/export; job retorna bytes no confiables. No dar credencial SQL/Temporal/core ni socket control a los agentes; Activity determinística confiable invoca wrapper fuera del dominio financiero y obtiene receipt, no callback del modelo con órdenes.

Si IPC adicional es necesario: canal específico por dominio/job, DACL explícita por SID/logon-session; autenticar principal efectivo OS y asociar job/attempt/epoch fuera del JSON. Allowlist mínima `read_export(export_id, record_ids)` y `submit_candidate(output_bytes)` como operaciones conceptuales; no paths/SQL/URLs, `execute`, `create_intent`, `resume`, `change_risk`, acceso general al core. Validar tamaño/IDs/clock/lease; ausencia/unknown → rechazo registrado. No por ello seleccionar protocolo final ni crear servicio productivo.

Named pipe no acepta descriptor NULL, Everyone/Anonymous/NETWORK ni generic client rights que permitan crear instancia servidor. [Microsoft pipe security](https://learn.microsoft.com/en-us/windows/win32/ipc/named-pipe-security-and-access-rights) documenta default demasiado amplio y el solapamiento FILE_GENERIC_WRITE/FILE_CREATE_PIPE_INSTANCE. Tests: principal hermano/remoto rechazado; namespace squatting; cliente que declara SID/rol falso; connection cancel/replay; handles heredados; output flood. Protecciones server ownership/remote rejection/impersonation limitada deben declararse antes de configurar pipe. Loopback por sí solo no identifica al usuario.

## 6. Network/egress — decisión técnica no congelada

| Origen | Permitido propuesto | Denegado requerido |
|---|---|---|
| R/S/P proceso completo | Transporte native modelo/auth de OpenAI necesario y observado en fase específica | Broker/data endpoints directos, red LAN/loopback no aprobada, SMB/WinRM/control/DB; destino arbitrario |
| Tools locales | Lectura export por ID, sin sockets | Red externa/local y tool que introduce credenciales/URL/SQL |
| C | Launch/collect y stores propios; canal export core autorizado | Broker/órdenes, listener general accesible a job |
| F | Broker/data seleccionados bajo contrato financiero | Inferencia/outputs job como autoridad alternativa |

No lista inventada de dominios OpenAI ni wildcard `*.openai.com` aceptada como mínima. En fase auth/transport se observa metadata **sin tokens/headers/cuerpo**, fija destinos necesarios/versionados y valida permit/deny sin ampliar automáticamente. TLS verification permanece activa, sin MITM improvisado. Auth inicial interactiva puede tener permisos temporalmente diferentes, explícitos y revocados antes del gate operacional.

El [proxy Codex](https://learn.chatgpt.com/docs/agent-approvals-security) filtra comandos, no todo tráfico de cliente/modelo/auth, MCP/apps/browser. App-server [`process/*`](https://learn.chatgpt.com/docs/app-server) puede ejecutar fuera del sandbox; no se expone en allowlist. Deshabilitar esas herramientas reduce superficie pero **no sustituye egress del proceso completo**. Controles Windows nativos se reutilizan ([sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox)); su setup administrativo es otro gate, no se ejecuta desde onboarding automáticamente.

Candidato: Windows Firewall/WFP con scope efectivo por SID/imagen y salida autorizada verificable; sin construir driver/filter propio en preparación. WFP [ALE](https://learn.microsoft.com/en-us/windows/win32/fwp/application-layer-enforcement--ale-) soporta identidad app/usuario; eso no demuestra que cualquier regla PowerShell discrimine cada proceso/usuario/loopback. [New-NetFirewallRule](https://learn.microsoft.com/en-us/powershell/module/netsecurity/new-netfirewallrule?view=windowsserver2025-ps) define filtros; verificar ActiveStore, prioridad, aplicación y tests para TCP/UDP/IPv4/IPv6/loopback/IP directo/redirect/proxy/hijos antes de PASS. Un allow por binario compartido podría dar permiso al dominio equivocado; bloquear exe principal dejando Python/PowerShell libre tampoco cumple.

**Hallazgo host:** preflight sin mutaciones observa outbound default Allow, `AllowLocalFirewallRules=False` y LogBlocked=False en los tres perfiles. Esto **no prueba** acceso a todo endpoint ni fracaso de S2; sí impide asumir que crear una regla local la hace efectiva. [Microsoft rules](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules) distingue policy merge/Group Policy. Determinar store competente/administrador antes del gate red; no cambiar merge, defaults globales o política empresarial silenciosamente. Imposibilidad de enforcement completo y reproducible tras evaluación → reevaluación S3, no fallback S1.

## 7. Tools, snapshots y blinding

Native policy/Skill/AGENTS config pinada y readonly; allowlist inicial solo lectura de evidencia por ID definido + structured output. Request approvals command/file → typed decline; permission subset vacío; elicitation decline; desconocido → stop/reject. No app/browser/Computer Use/MCP/plugins/hooks/shell/subagent spawn o process/* heredados. Ampliación por necesidad concreta pasa contrato/version/tests y gobierno material correspondiente. Denegar custom handlers capaces de ejecutar aunque tool label diga read-only.

Export Shadow deriva **antes de unir decisión Champion**, desde contexto financiero elegible común. Incluir as-of holdings/cash/reservas/quotes/señales/risk constraints permitidos: holdings de la cartera real provenientes de decisiones anteriores son contexto legítimo, no exigir que Shadow ignore toda historia financiera. Excluir contemporaneous decision/reasons/sizing/TradeIntent/orden nueva, logs/evaluación/outcomes posteriores y pedagogía relacionada. Champion futuro nunca consultado para llenar campos faltantes.

Contratos de evidencia por export: `job_id/attempt_id/role`, snapshot-id/digest/canonicalization-version, cutoff, fuentes/revisiones/available-at, dataset/split/version, `visibility_policy_version`, `dependency_lineage`, lista de campos/tipos/minimización y limitaciones. Pair ID identifica el contexto predecisión; join Champion/Shadow reside H/C fuera de S. No incluir hash de una decisión secreta de baja entropía que permita adivinarla por enumeración.

Output Shadow se copia/sella por C **antes** de permitir join/evaluación H; si Champion termina antes, su namespace sigue cerrado. Timeout/late/no-output/UNPAIRED nunca desaparecen del denominador. Reintento rehidrata contexto elegible; no devuelve outputs Champion/pedagogía/otros intentos para mejorar resultado. Sesiones/caches/histories/storage de los dominios separados; tests de reuso y canales laterales visibles (nombres de jobs, fechas, tamaños, ranking, errores). Clasificar límites: no prometer eliminar todo timing side-channel del OS; demostrar que los campos/servicios expuestos no codifican decisión excluida.

Una allowlist de campos **no basta** si `signal.value` o narrativa aprobada fue generada usando Champion contemporáneo. Exigir DAG/linaje causal elegible y test de invariancia: mismos inputs predecisión, distintas decisiones Champion → mismos bytes de export y metadata visible a S. Sources text no confiable no puede establecer etiquetas propias `PRE_DECISION`. Admission externo verifica lineage declarado contra registry confiable; detalles de exporters/proveedores concretos se prueban antes de PAPER. No asumir que un scanner literal elimina contaminación semántica.

## 8. Auditoría, recovery y bootstrap

Cada test/intento guarda run/version/source_commit/policy-fingerprint, SID/domain alias e integrity/group/privilege classes efectivos, operación/recurso sintético, permitido/denegado/error exacto, clocks y resultado. Rechazo visible al job ≠ evidencia única: caller/audit fuera del job + fuente OS cuando aplique (security audit/SACL/firewall) correlacionan intento/resultado sin valores secretos. Política audit no activa por este documento; gate administrativo separado. Probar que job no borra/forja evidencia, que auditoría indisponible bloquea nuevo lanzamiento y que crash no convierte UNKNOWN en PASS.

Bootstrap declara `AUTOMATED` (lecturas/checks permitidos), `USER_ACTION_REQUIRED` (SID/ACL/política/login/admin), `UNAVAILABLE`, `OPTIONAL`, `FALLBACK_AVAILABLE`. Rebuild desde repo + perfil sanitizado + política local autorizada, no passwords/SID portable/auth copiados. Tras restore/reboot revalidar derechos/red/IPC/source/config/epoch antes de admitir; si drift detiene jobs, nunca reanuda pausa core. Ver [workflow](08_job_workflow_recovery_contract_RC0.md) y [audit/deploy](08_audit_versions_deployment_contract_RC0.md).

## 9. Build-vs-Reuse y coste

Windows identidades/DACL/process protection/IPC/WFP: **REUSE_AS_IS / WRAP** controles del SO, no construir sandbox nuevo. Native Codex approvals/permissions/Team login: **REUSE_AS_IS / WRAP** con callback fail-closed y control del proceso completo. Procedures export/lineage/negative evals: **ADAPT** contratos propios/stdlib, no producción. VM S3: **REFERENCE_ONLY** fallback investigable, selección requiere evidencia/gobierno.

PAPER_V1_VIABLE_FREE=CONDITIONAL: host/licencia actuales y policy/auth viables; PAPER_V1_COST=0 gasto activado, tiempo/admin/recursos por medir. LIVE_COST=UNKNOWN; FREE_ALTERNATIVE=S2 local o S3 local si recursos/licencia suficientes; PAID_INCREMENTAL_VALUE=posible separación/operación administrada, no seleccionada; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de gasto. No API/servicio pago, compra Skill o cambios de políticas realizados.

## 10. Evidence/gates

[Matriz SI/BL/RB y criterios S2→S3](research/R-013_S2_acceptance_matrix_RC1.md). [Propuesta administrativa acotada](research/R-013_S2_administrative_gate_ADM01.md). [Hallazgos/probes](research/R-013_S2_findings_2026-10-05.md). Elegir S2 no cierra D-027/D-024; mandatory NOT_TESTED/UNKNOWN impide PASS. No exigir construir core financiero para probe de viabilidad P1: canaries/processes/controllers sintéticos bastan para ensayar frontera; el gate P2 exige repetir con integración seleccionada, nunca secretos publicados.

## Revisión independiente — persistencia y lifecycle

Un job bajo un SID persistente puede copiar inputs/outputs en su perfil, cache, TEMP, scratch, threads o auth-adjacent state y recuperarlos tras cerrar el export. Serializar jobs/terminar procesos por sí solos **no** eliminan esa persistencia. SI-16/BL-06/RB-02 deben plantar una canary en cada ubicación writable del SID, terminar/revocar/relaunch y verificar qué puede volver a leerse.

Estado sobreviviente permitido requiere contrato versionado: transporte/auth nativo estrictamente necesario; tesis/artefactos research solo cuando reexportados por control confiable y declarados en manifest/corte/linaje; no libre perfil/cache/history de Champion/otros jobs para Shadow. Declarar cada path/store writable efectivo, incluido auth cache: no asumir que auth es incapaz de almacenar canary. OS ACL/ephemeral isolation debe impedir persistencia fuera del scratch permitido o la configuración no demuestra aislamiento por job. Login/session legítimos y refresh necesitan probe aparte: no solución seleccionada ni copia de tokens. Si no hay frontera reproducible dentro S2, volver a D-024/gobierno/S3 conforme criterios, no aceptar prompt o cleanup incompleto como barrera.

Lifecycle candidato reutiliza [Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects): supervisión/kill-on-close a evaluar, sin flags breakaway, detectando también rutas de creación que evaden asociación. No sustituye permisos por proceso ni prueba cleanup por falta de notificación. Si [impersonación IPC](https://learn.microsoft.com/en-us/windows/win32/api/namedpipeapi/nf-namedpipeapi-impersonatenamedpipeclient) falla, rechazar operación, nunca ejecutar como servicio privilegiado.
