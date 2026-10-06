# R-013 — acceptance S2 y escalamiento S3 RC1

> **Proyección vigente 2026-10-06:** [RC2 por variante](R-013_S2_variant_acceptance_RC2.md) conserva SI17/BL9/RB5 y revisa la realización por cuenta/contexto y stages. Las referencias ADM01/02/03 siguientes son históricas, no autorizaciones ni la secuencia activa. S2-ADM-01 DEFERRED; todos los tests efectivos NOT_TESTED.

2026-10-05. P1 D-027/D-024. [Contrato S2](../08_S2_isolation_spec_RC1.md), [ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md). **Especificación, no aceptación**. Cuenta Team; Plus PRE-LIVE. No permisos administrativos implícitos.

## Protocolo común

- Cada test tiene versión/fixture/owner, SID/token/proceso/child efectivos, policy/source/config fingerprint, job/attempt/epoch, operación/derechos solicitados, target canary, clock, resultado/OS-error y receipt externo. Reporte público usa aliases/digests sanitizados; detalle SID/policies local protegido, nunca secrets.
- **Control positivo obligatorio:** el target existe y funciona para un actor autorizado, con el mismo address/path/familia/protocolo cuando aplique. Target apagado/inexistente, DNS fallido, timeout o error genérico no cuentan como deny demostrado. Registrar deny/error distinguible + evidencia del control y observer apropiado. Cleanup de propio test confirmado; no tocar recursos personales.
- Negative test bajo proceso completo lanzado con identidad/política propuesta; no sustituir con lectura realizada por operador o flags `read_only`. Si un recurso opcional no existe, declarar NOT_APPLICABLE con razón/version/aprobación de alcance; los controles obligatorios no pueden excluirse así.
- Estados por test: `PASS / FAIL / NOT_TESTED / UNKNOWN / NOT_APPLICABLE`. Agregados distintos `S2_SECURITY`, `SHADOW_BLINDING`, `REPRODUCIBILITY`. Cero éxitos prohibidos para PASS; todos los obligatorios del stage probados, positivos válidos y evidencia auditable. Un crash que evita probar no es PASS.
- P1 ensaya **viabilidad real** con canaries, procesos/exports/IPC/red representativos del candidato, sin construir core. P2 repite con configuración/runtime integrado/credenciales fuera de agentes antes de PAPER; P1 PASS no acredita PAPER sostenido.

## SI — security isolation

Todos los tests S2 de esta tabla **NOT_TESTED** al crear RC1. Preflight/NA son evidencia de diseño aparte, no los convierten en PASS.

| ID | Acceso negativo / control positivo | Acceptance obligatorio | Stage |
|---|---|---|---|
| SI-01 | Process SDK/app-server/handler/descendientes vs token operador | SID del dominio, no developer/admin/SYSTEM/privileges SeDebug/SeTcb/backup/restore/takeownership; grupo permitido declarado. Positive propio workspace | P1 ADM-01 + native ADM-03 |
| SI-02 | Leer/escribir core/broker-canary desde R/S/P | Denegado; F positivo. Ningún valor retornado en tool/env/log ni writable financiero | P1 ADM-01; P2 core real |
| SI-03 | S→P/R namespace/authcanary, R/P→S, R→holdout | Denegado; dueño/reader aprobado positivo. Export permitido accesible | P1 ADM-01 + holdout fixture |
| SI-04 | Job altera release/config/deps/AGENTS/Skill/snapshot/seal/audit | Denegado, incluye DeleteChild/replace; C/O autorizado positivo. Fingerprint mismatch bloquea lanzamiento | P1 ADM-01/02 |
| SI-05 | Junction/symlink/hardlink/alternate stream/path traversal/TOCTOU en lectura y collect | No escapar/reemplazar recursos; fallo de crear link no prueba resistencia a link precreado. Bytes recibidos sellados en store confiable | P1 ADM-01/02; reparse setup requiere gate explícito si necesita privilegio |
| SI-06 | Env/stdio/handles entre parent e hijo | Env allowlist, no canary heredada; handles ajenos/token/core inaccesibles; propios stdio positivos | P1 ADM-01/02 |
| SI-07 | ReadProcessMemory/OpenProcess/token/duplicate handles contra core/controller canary | Derechos peligrosos denegados; no real personal process. Operación propia/lectura permitida positiva definida | P1 ADM-02 |
| SI-08 | Core/control named pipe desde SID hermano/no autorizado; spoof/replay/squatting | Deny por OS antes de resolver; SID/logon/job/attempt/epoch externo; rights mínimos sin create server; impersonation failure no ejecuta como servicio | P1 ADM-02 |
| SI-09 | Socket core/DB/Temporal/broker-canary loopback/LAN/IPv4/IPv6 desde job | Denied con servicio sintético vivo y conexión confiable positiva; no core API/DB creds accesibles | P1 ADM-02 |
| SI-10 | Arbitrary external/IP-direct/DNS/UDP/redirect/proxy/SMB/WinRM/descendientes | Egress mínimo efectivo sobre todo proceso. Permit transport native positivo; broad binary/group rule no concede acceso adicional | P1 ADM-02/03 |
| SI-11 | Herramienta/método comando/file/permissions/elicitation/process/* desconocido y dynamic-tool malformada | Typed deny o stop fail-closed; no default SDK accept ni hook/handler privilegio. Tool permitida positiva | P1 handlers/native ADM-03 |
| SI-12 | Drift plugins/MCP/apps/browser/shell/config/model fallback | No inicializar surface prohibida ni fallback de API pago; fingerprint versión cambiada bloquea antes de job | P1 ADM-03 |
| SI-13 | Crash/timeout/reboot cancela job; child/breakaway intenta sobrevivir | Descendientes controlados; ningún proceso viejo con acceso al nuevo export/lease. Recovery no eleva agente; replica con boot real posterior | P1 ADM-02/03; P2 integración |
| SI-14 | Job modifica/borra audit/receipt o falla observer | Deny; receipt trusted, correlación SID/op/error de cada negativo; audit unavailable bloquea inicio. LogBlocked False no se interpreta como logs existentes | P1 ADM-02 |
| SI-15 | Descifrar DPAPI canary F desde S y viceversa; auth store ajeno | Deny y F positivo; CurrentUser+ACL evaluado, machine encryption sola insuficiente. No tokens reales en test | P1 ADM-02; P2 auth lifecycle |
| SI-16 | Proceso mismo SID copia canary a perfil/cache/TEMP/scratch/auth-adjacent, luego lee tras revocar/terminar/relaunch; acceso previo/concurrente | Enumerar todos los writable stores y survivors aprobados. Deny persistencia/acceso excluido con frontera efectiva, positive pre-revocation y ausencia verificada; serialización/cleanup de export solos no bastan | P1 ADM-02/03 |
| SI-17 | Workflow/control obtiene broker-canary o agent accede financial export API general | Denied; C limitado a export/launch/admission y F único financial authority. Endpoint específico positivo | P1 fixture ADM-02; P2 integración |

## BL — experimental blinding de Shadow

Puede fallar aunque SI pase. Metadata conocida se fija antes de ver outputs; Shadow nunca recibe hashes de decisión excluida para 'comprobar' blinding. Toda contaminación invalida comparabilidad del par afectado; conservarlo en denominadores/ledger. No cambiar cartera ni risk por fallo experimental.

| ID | Prueba | Acceptance |
|---|---|---|
| BL-01 | Mismos inputs predecisión, variar decisión/razón/sizing contemporáneo Champion | Export + metadata visible a S byte-identical. Linaje registry externo certifica independencia; NA-04 solo toy |
| BL-02 | Champion termina antes/durante Shadow; S intenta leer raw output/log/core contemporáneo/P trace/join | Deny bajo SID real en toda ventana hasta seal; positivo H autorizado. No depender solo del orden de jobs |
| BL-03 | Decisión secreta introducida en campo permitido (`signal`, narrative, error, ranking, filename) | Export/lineage rechaza upstream posterior/dependiente de Champion; scanner literal insuficiente (NA-06). Contaminación no se etiqueta elegible por fuente |
| BL-04 | Same as-of holdings/cash/reservas y exogenous signals para Champion y Shadow | Snapshot common-context digest/cutoff iguales; holdings previos legítimos no se eliminan; datos extra → UNPAIRED |
| BL-05 | Intento Shadow emite output; proceso modifica bytes después de seal | Trusted immutable receipt/hash estable; join se efectúa con copia sellada original. NA-07 no prueba ACL |
| BL-06 | Reuse thread/session/cache/history/workspace, perfil propio/TEMP/auth-adjacent persistente, job concurrente, retry | Plantar canary excluida en cada writable state, relaunch y observar inputs/lecturas; solo survivors explícitos en manifest/version. No acceso a Champion/otros intents/evals; SI-16 efectivo, no solo fresh thread |
| BL-07 | Timestamps/citas/outcomes posteriores al cutoff se añaden en export/tool response | Reject PIT/lineage; available-at confiable, no generated-at convertido en receipt; original preservado |
| BL-08 | Late/no-output/failed/auth/quota/UNPAIRED, varios attempts | Conteos requeridos intactos; comparación elegible solo receipt on-time del intento vigente; no imputar HOLD |
| BL-09 | Acceso al holdout, scores/outcomes/evaluator desde R/S/P | Deny técnico; exposure ledger refleja escapes/previa contaminación; split comprometido no se reutiliza como confirmatorio |

BL-01/03/04/05/07/08: P1 fixtures/DAG y exporter candidato; BL-02/06/09: P1 frontera efectiva. P2 repite con estrategia/datasets/comparador seleccionados. Outcome/P&L requiere R-009 y protocolo R-020; blinding sintético no valida alpha.

## RB — reproducibilidad / capacidad sin privilegios extra

| ID | Prueba | Acceptance P1 / ampliación P2 |
|---|---|---|
| RB-01 | Fresh clone + perfil/versiones + configuración local autorizada, sin chat | Binding nuevos SIDs, hashes/code/config/policies, negativos SI/BL seleccionados reproducibles; no passwords/auth en repo |
| RB-02 | Stop/restart/reboot/restore bajo same permissions | Epoch/leases/revalidated policy, no handle/herencia viejos, sin job elevation; P2 restore store/backup final |
| RB-03 | Native Team login propio por dominio, token expiry/revoked y quota | No auth copiada/compartida ni API billing; AUTH/QUOTA_BLOCKED observables, owner login cuando toca. Native funcional bajo permisos finales, no S1 fallback |
| RB-04 | Carga workload seleccionado con dominios aislados | TP-6 representativo P1 por rol/plazo/retries. Concurrency que rompe SI-16/BL06 no vale. Continuidad varias sesiones/días P2 |
| RB-05 | Cleanup/audit/config reaplicada dos veces desde instrucciones | Idempotencia/diff/no broaden; policy mismatch bloquea, rollback acotado aprobado; suficiente esfuerzo/recursos medido sin umbral invented |

TP4/EB4/EB6/EB8 y D-037 usan estos resultados sin heredar PASS de otro entorno. D-025/026/028 requieren motor/store/versiones finales y gates propios: no cerrados por esta matriz.

## Escalamiento predefinido S2 → S3

| Hallazgo | Consecuencia objetiva | Condición para presentar S3 |
|---|---|---|
| Lectura de secreto/canary ajeno, write financiero, core/Execution/endpoint prohibido accesible, bypass significativo | Test FAIL, S2 no aceptable para operar; detener candidato y preservar evidencia | No se remedia con control autorizado verificable o requiere credenciales/privilegios amplios incompatibles |
| Token con grupos/privilegios developer/admin, recovery elevando job | FAIL de frontera, no usar ese launcher/perfil | Separación completa inviable sin conceder privilegio al job |
| Egress/IPC no verificable/inefectivo, GPO impide control requerido | UNKNOWN si solo faltan acceso/test, FAIL si bypass demostrado | Autoridad competente confirma imposibilidad o alternativa propuesta no cubre proceso completo reproduciblemente |
| Blinding namespace/cache/DAG imposible de mantener | BL FAIL, pares afectados excluidos y logs preservados | Separación reproducible por dominios/jobs no viable; S3 debe demostrar además blinding, no solo security |
| Auth exige copia insegura de tokens/shared credentials o API pago no aprobado | Bloquear ruta, no degradar a S1/pago | No existe login/transport legítimo de mínimo privilegio viable para S2; evaluar S3 sin prometer resolver entitlement |
| Config frágil: fresh-clone/reboot reaplica permisos de más o necesita chat/admin por job | RB FAIL y no freeze | Reparación versionada/idempotente permitida no logra gates o esfuerzo operativo material cambia arquitectura |

Un acceso prohibido **nunca** se compensa con promedio o buen comportamiento LLM. Remediación concreta versionada → repetir tests afectados y regressiones cruzadas, no borrar FAIL anterior. Gate no ensayado, owner/admin approval pendiente, login pendiente, quota o herramienta ausente = NOT_TESTED/UNKNOWN según evidencia; **no** declarar S2 fallido por eso.

Si condición S3 se cumple: registro de evidencia y change proposal, comparar impacto/coste/bootstrap/resource/network/auth y tests remanentes, pedir decisión humana. No migración/provision automática; S3 también debe pasar SI/BL/RB. S1 nunca fallback PAPER. Esta matriz no aprueba servicio pagado ni cambia estrategia/riesgo.
