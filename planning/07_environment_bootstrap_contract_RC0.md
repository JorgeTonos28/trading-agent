# Environment Bootstrap / Onboarding / Portability — RC0

**Vigencia ADR-011 — 2026-10-05:** propietario aprobó opción A y disposiciones RC2 como dirección de diseño PAPER: núcleo financiero local determinístico always-on + jobs Codex Team automáticos por evento/calendario, sin aprobación por job rutinario. D-020 DECIDED únicamente en dirección Build-vs-Reuse; versiones/permisos/runtime final siguen D-024 RESEARCHING. No implementación, gasto, capacidad sostenida ni autoridad financiera adicional. Plus permanece PRE-LIVE.


**Vigencia actual — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

2026-10-05. Requisito ADR-009 aprobado; mecanismo candidato D-037/R-028 P1. D-020 READY_FOR_DECISION/D-024 RESEARCHING. Fuente de verdad: repo, [ONBOARDING](../ONBOARDING.md), [manifest](../shared/bootstrap_manifest.json), perfiles y evidencia versionada. No implementar Trading OS.

## 1. Bootstrap Mode candidato

Recomendación: **modo lógico de Plan Architect/Guardian con procedimiento repo y Skill pequeña**, usando discovery/config/Skills nativos. No requiere proceso permanente ni una sesión por rol, ni nuevo instalador propio. Un Onboarding Agent programático futuro podría invocar el mismo paquete mediante el transporte elegido D-024. La Skill es un adaptador documental del contrato; no tiene capacidad de concederse permisos.

Entradas confiables: repo/commit, target declarado por dueño, scope de readiness, manifiesto de requisitos, permisos efectivos y aprobaciones existentes. Inventario y material externo son evidencia, no instrucciones para aumentar autoridad. Salidas: perfil observado sanitizado, diff de capacidades, plan de acciones, resultados por gate y reporte. Todo tiene `authority=NONE`.

## 2. Tres entornos

| ID | Propósito | Lo que NO demuestra |
|---|---|---|
| CURRENT_RESEARCH_ENVIRONMENT | Team declarado/observado históricamente; conducta, diseño y probes | Entitlements Plus o condiciones LIVE |
| PAPER_RUNTIME_ENVIRONMENT | Team actual: implementación tras DoR, backtests y PAPER | READY_FOR_IMPLEMENTATION, autorización inmediata PAPER/LIVE o entitlement API |
| FUTURE_LIVE_ENVIRONMENT | Plus individual candidato, migración PRE-LIVE R-029 | Aprobación de gasto, runtime, broker/capital o gates LIVE |

Perfilar **cada instancia**, no solo el tipo de plan. Registrar OS/superficie/versiones/capacidades/Skills/plugins/MCP/dependencias/límites/fallbacks/tests/estado. Plan observado puede ser UNKNOWN aunque el dueño haya declarado un target; documentar el error. `expected` es requisito; `observed` es evidencia. Nunca rellenar observado desde expected; no transferir resultados entre instancias/superficies ni hacia Plus.

## 3. Ruta ejecutable de preparación

| Paso | Acción | Evidencia / condición |
|---|---|---|
| Discover | Git root, rama/commit, etapa, manifests y dependencias | Clone completo; validar paths/hashes/refs; no ejecutar scripts de terceros al descubrirlos |
| Inspect | Versiones; fuentes de reglas; Skills; installed/enabled/callable plugins/apps/MCP; herramientas/permisos | Interfaces nativas readonly cuando existan; metadata no prueba acceso a fuente/dataset |
| Compare | Diff esperado↔observado y required/optional | UNKNOWN obligatorio bloquea su gate; explicar deltas del entorno |
| Plan | Acciones, prerequisitos, costes, approvals, rollback | No asumir permiso por figurar un paquete en manifiesto |
| Configure | Local assets ya llegan con clone; proponer settings/permisos concretos | Diff y alcance; cambios aprobados, idempotentes, backup sin secretos en repo; nunca sobrescribir settings globales |
| Accept | EB y TP según scope/entorno | TP1 antes de inferencia target, TP2–4 tras discovery; TP5–7 requieren operación y ventana temporal, no todo se completa en onboarding instantáneo |
| Prepare roles | Cadena global/local + rol/schema/tools/version confiables | Paquete documentado ≠ activación operativa. Plan Guardian solo tras freeze |
| Smoke/report | Fixtures sintéticas, resultados/fallos y readiness | Registro antes de resumir; reporte accionable, sin crear órdenes/posiciones ni gastar |

Autologin/logout, copiar auth Team, revocar tokens, confiar proyecto/hooks, instalar conectores, activar API billing o ampliar tool scopes no son una consecuencia automática de clonar. Cuenta/consentimiento/credenciales requieren dueño mediante UI oficial. Config general de seguridad sigue D-027, no se congela en este contrato.

## 4. Clasificación de acciones

| Clasificación | Uso exacto |
|---|---|
| AUTOMATED | Acción permitida y comprobable con herramientas ya disponibles: lectura, hashes, validación, smoke sintético. Permiso y coste se comprueban primero |
| USER_ACTION_REQUIRED | Login/consentimiento/acceso/instalación manual o decisión material; indicar interfaz, resultado esperado y evidencia sanitizada, nunca pedir valor del secreto |
| UNAVAILABLE | Capacidad ausente/no compatible según evidencia; indicar requisito afectado, no convertir fallo temporal en NO definitivo |
| OPTIONAL | Mejora que no bloquea el scope actual; no instalarla por defecto |
| FALLBACK_AVAILABLE | Alternativa identificada con contrato/limitaciones/evidencia. Disponible no equivale a selected ni accepted |

Son etiquetas del plan de acción; availability, requisito required/optional, selected y estado de gate son ejes separados. Cada acción tiene ID, requisito, clasificación, estado, acción concreta, aprobación necesaria y evidencia. No esconder un login obligatorio bajo OPTIONAL. Fallback puede ser manual para preparación, sin demostrar suficiencia del shadow/operación autónoma.

## 5. Perfil y readiness

Schema RC0 compartido estrictamente versionado. Campos:

Las referencias locales evidence_refs publicadas se resuelven desde la raíz del repositorio, con verificación de paths/evidencia, no desde el cwd de un rol. Las referencias simbólicas SYNTHETIC de fixtures no cierran gates reales.

- environment_kind, expected_plan, observed_plan, surface, OS, repo_commit, manifest_sha256 y captured_at UTC;
- inventory con ID/kind, detected/enabled/callable por separado, version y evidence_refs (sin auth values);
- skills/plugins/MCP/localtools/dependencies mediante `kind`; cuotas/límites conocidos, UNKNOWN permitido;
- instruction_chain (paths relativos de repo; externos solo etiqueta/hash de archivo no secreto), paquetes verificados;
- action_plan, selected_fallbacks, acceptance_tests (environment/source/versión/resultado/evidencia), requirement_results;
- readiness_scope y estado/blocked_by, autoridad NONE, implementation_locked=true.

Estados: NOT_ASSESSED, PARTIAL, BLOCKED_USER_ACTION, BLOCKED_FAILED_GATE, READY_AGENT_ENVIRONMENT. Scope: PREPARATION_ONBOARDING o PAPER_AGENT_ENVIRONMENT. READY requiere todos los requisitos obligatorios del scope PASSED y sin acciones obligatorias abiertas. Para PAPER, además selección/gobierno aprobados, identidad Team y EB/TP del alcance correspondiente completos; aceptación sostenida operacional es P2. Un schema válido o autoinforme LLM no concede readiness: la comprobación externa valida evidencia y reglas.

No claim de readiness de sistema financiero. Aun con entorno listo, DoR/Strategy/broker/riesgo/gates PAPER independientes pueden seguir abiertos. LIVE nunca queda autorizado por este perfil.

## 6. Acceptance Gate de portabilidad

| Gate | Antes de cierre | Prueba propuesta y vínculo |
|---|---|---|
| EB-1 clone/integridad | Reproducir entry point del commit/manifiesto correcto sin chat/caché de assets | Fresh local clone + refs/hashes; externos explícitos. Git privado exige acceso manual legítimo |
| EB-2 reglas/roles | Root+rol cargados, rol hermano ausente, override/truncación/conflicto detectados | Metadata + smoke observable en superficie seleccionada; no asumir ACL. TP2/4 |
| EB-3 capabilities/diff | Inventario expected/observed y entitlement específico | Skills/plugins/MCP/dependencies, desconocidos visibles; TP1–3, verificar instancia/superficie Team |
| EB-4 configuración/seguridad | Acciones permitidas/manuales, no secretos ni settings clobber | Diff autorizado, idempotencia/paths/rollback; permisos finales D-027. TP4/7 |
| EB-5 package portability | Manual/programmatic entry de ruta elegida carga mismo contrato/caller/outputs | Hashes/paths/lifecycle. No exigir dos rutas si una no se selecciona; no sesiones por rol impuestas |
| EB-6 smoke/recovery | Rol/Skill/schema/tools básicos y reporte recuperable | Snapshot del job/attempt y resultados, no duplicar configuración/admisión; TP3/5. Probe offline solo simula, no recovery durable real |
| EB-7 suficiencia target | Finalistas cumplen requisitos en Team, cuotas/auth/cadencia | TP1–7 + workload R-006; reutilizar comparación Team pertinente. TP6 necesita varias sesiones/días |
| EB-8 readiness audit | Estado derivado de evidencia por requisito, acciones exactas, revisión crítica | UNKNOWN/fail no pasan, opcional no bloquea, drift invalida gates afectados; D-029/037 |

**DoR/D-024:** antes de freeze, ruta final y paquetes/permiso seleccionados o descartados justificadamente, EB de preparación cerrado para Team, permisos aprobados y protocolo TP operacional definido; carga sostenida e integración financiera construida se ejecutan P2 antes de PAPER autónomo, responsable de mantenimiento/deployment y version pins. Protocolos financieros/PAPER/LIVE siguen separados. Discovery/probes válidos Team aplican a gates de arquitectura, sin probar operación sostenida ni todas las superficies. Véase matriz por etapa TP y ADR-010.

## 7. Reanudación y drift

Guardar checkpoints sanitizados por ejecución: commit/manifest/rules/Skill/schema/client version, inputs, IDs propios no asociados a cuenta y gates. Reiniciar compara fingerprint; se reutiliza evidencia solo si scope/inputs/ruta pertinentes coinciden. Cambios de plan/superficie/auth invalidan gates de entitlement; versión/config/instrucciones/Skill invalidan smoke/gates afectados, no toda investigación histórica. Carga/quota evidencia tiene ventana temporal declarada. Fallos y retries permanecen; máximo un resultado aceptado por job.

No descargar/cargar credenciales al recuperar un perfil. No ejecutar automáticamente postinstall/hook sugerido por una fuente. Un reporte histórico READY no es permiso vigente en máquina nueva. Recovery durable e identidad final de jobs se investigan en D-025/026; este documento no los implementa.

## 8. Build-vs-Reuse / coste

| Capacidad | Disposición propuesta | Motivo / gap |
|---|---|---|
| AGENTS + Skill discovery nativo | REUSE_AS_IS | Evitar cargador de roles propio; verificar cwd/root/overrides y activación |
| Bootstrap Mode/Skill + manifest propios | ADAPT | Procedimiento/documentos de contratos existentes; no nuevo runtime/installer |
| Native inventories SDK/app-server/config | WRAP | Caller/reporte sanitizado específico cuando transporte final lo requiera; APIs/version y target por probar |
| skill-installer público | REFERENCE_ONLY / ADAPT por necesidad | Para assets externos revisados/pinados; clone ya entrega locales, no instalar globalmente para cada rol |
| Custom native agents | REFERENCE_ONLY | Ruta opcional de invocación futura; no topología seleccionada |
| Portable plugin package/marketplace | REFERENCE_ONLY | Posible distribución posterior; instalación/trust/auth separadas |

Assets locales/Skill propia: PAPER licencia/adquisición 0, cómputo/cuota incluidos solo si TP demuestra; LIVE coste operacional UNKNOWN. Alternativa gratuita: procedimiento manual explícito y native discovery; no necesariamente equivalente al workload. Valor pago posible continuidad/gestión de entorno, no demostrado; requiere ficha ADR-008/aprobación antes de gastar. No comprar Skills ni asumir entitlement propietario.

## 9. Límites del paquete autónomo

Entregables: contratos/manifiesto/perfiles, paquetes documentales, Skill candidata, evidencia local y fresh-clone, deltas a Team Gate/shortlist y PRE-LIVE Plus. Endpoint cuando eso esté sincronizado y siguiente acción necesite gobierno material; el acceso Plus no bloquea este paquete Team. Auth bloqueada no detiene inventario local, diseño y negativos. D-037 queda RESEARCHING; mecanismos/permisos finales necesitan evidencia y gobierno correspondientes.

## Aclaración del perfil RC0 — Git identity

`repo_commit` identifica snapshot ensayado. `manifest_sha256` es SHA256 del Git blob `shared/bootstrap_manifest.json` de ese commit, sin autorreferencia; asset hashes portables usan la misma regla. Raw worktree hash es evidencia local distinta. Un perfil posterior puede reutilizar solo gates cuyos inputs/rules/Skill/schema/cliente/condiciones relevantes sigan iguales; cambios de contenido no EOL se consideran drift. Evidence_kind simulado nunca se usa para cerrar target gates. Fresh clone local no implica máquina limpia, nueva autenticación o surface Plus.

## Hardening posterior ADR-011

Bootstrap debe verificar contratos 08, configuración efectiva/identity domain/namespace y versión de admission, tool allowlists, dataset/holdout exports, trusted incarnation por intento y ausencia de broker paths/credenciales. S2 propuesto requiere gobierno/config concreta; no crear usuarios/firewall/VM por onboarding automático. WSL binario presente pero subsistema no instalado se reporta UNAVAILABLE/USER_ACTION_REQUIRED, no disponible. H4 bundle native default0.160 probado en Team es evidencia focal de candidato, no nueva readiness completa del entorno ni permiso final. Auth del dominio se configura legítimamente por owner; no copiar tokens. Perfil histórico observado no se actualiza como PASS porque cambió documentación.

**Vigencia ADR-012 — 2026-10-05:** el propietario aprueba S2 como dirección candidata de aislamiento PAPER por dominios Windows. S3 es fallback formal sujeto a nueva decisión si S2 falla; S1 solo probes sin secretos. Las propuestas históricas S2 vs S3 quedan resueltas únicamente en dirección. Security isolation y Shadow experimental blinding requieren acceptance separado; configuración administrativa, permisos efectivos y D-027/D-024 siguen abiertos. Ningún usuario/ACL/firewall/credencial se modifica por esta aprobación. Véase [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md).

## S2 reproducible — vigencia posterior ADR-012

[S2 RC1](08_S2_isolation_spec_RC1.md) declara dominios independientes de roles, paths mínimos y política versionada. Bootstrap identifica token/group/policy efectiva y bindings SID de esta instancia; no copia SIDs/auth del Team histórico. Exports/caches/sessions/workspaces separados preservan blinding Shadow. [SI/BL/RB](research/R-013_S2_acceptance_matrix_RC1.md) se registran como NOT_TESTED hasta acceso efectivo, no convertir preflight/smoke en READY. [ADM-01](research/R-013_S2_administrative_gate_ADM01.md) es USER_ACTION_REQUIRED pendiente de aprobación. No script auto-user/ACL/firewall, instalación/credencial/privilegio tácito ni número final de sesiones por carpeta. Source policy release/tag aprobado permanece.

## Bootstrap y packaging con S2-B propuesto — 2026-10-06

[RC2](08_S2_agent_domain_contract_RC2.md) sustituye como propuesta activa la realización por cuentas RC1; [acceptance RC2](research/R-013_S2_variant_acceptance_RC2.md). Un paquete/rol no implica cuenta Windows, sesión o proyecto Codex independiente. Bootstrap registra usuario base y contexto efectivo por job, grants, auth mínimo, persistencia, IPC/red, policy/version y SI/BL/RB/VP observados; no importa auth/SID del chat previo. S2-ADM-01 es DEFERRED/NOT_AUTHORIZED por owner, no próxima instalación. Acción humana vigente Q-051 dirección revisada; futuro setup exige diff/gate concreto. Mantener UNKNOWN/NOT_TESTED y PARTIAL, no READY por probe semántico. PAPER Team/Plus PRE-LIVE y deployment source policy intactos.

## Confirmación de dirección S2-B — 2026-10-06

Propietario aprueba S2-B como candidata principal, Q-051 cerrado en dirección. Un Runner base con aislamiento efectivo por job; A/S3 reservas condicionadas. Assets y controles continúan candidatos, no permisos/runtime aceptados. Siguiente gate es laboratorio mínimo concreto y reversible; no administración autorizada. [ADR-012](decisions/ADR-012-agent-process-isolation-proposed.md).
