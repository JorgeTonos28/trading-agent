# 08 — seguridad y permisos de jobs PAPER RC0

**Vigencia 2026-10-06:** [S2-B RC2](08_S2_agent_domain_contract_RC2.md) propuesto; [comparativa](research/R-013_S2_variants_comparison_2026-10-06.md). Cuenta por rol no es requisito demostrado. Frontera financiera y blinding separados; S2-ADM-01 withheld/DEFERRED. Dirección revisada pendiente, no permisos efectivos.

2026-10-05. D-027/R-013 **RESEARCHING**. Direcciones ADR-011 y ADR-012 S2 aprobadas en alcance candidato; controles efectivos y gate administrativo pendientes. No configuración de usuarios/firewall/VM, permisos finales o implementación autorizados.

## 1. Actores y amenazas

El núcleo financiero, su operador y los servicios de admission/workflow son componentes confiables determinísticos. El modelo, contenido externo, outputs y paquetes externos antes de revisión son no confiables. Un handler también es código privilegiado: validar fuera del modelo no lo vuelve seguro automáticamente. Amenazas: inyección en texto/datos/Skill, path traversal, alias/symlink/junction, output sobredimensionado, shell/MCP/plugin heredado, configuración alterada, acceso a broker/DB/socket local, robo de credenciales, callback fabricado, job/attempt/snapshot cruzado, recuperación con output viejo y supply-chain drift. Error del host o cuota no concede permisos.

La sesión Plan Architect actual tiene permisos de desarrollo amplios: **no es el perfil operacional de jobs**. Los probes sin comandos/órdenes prueban comportamiento, no aislamiento del proceso completo.

## 2. Matriz candidata de mínimos

| Actor | Lectura | Escritura / autoridad | Prohibido |
|---|---|---|---|
| Financial core | Inputs aprobados, estado reconciliado | TradeIntent determinístico, Risk/Execution bajo A+/G1+G2 | Consumir propuesta shadow como intent, delegar riesgo a LLM |
| Scheduler/dispatcher confiable | Eventos/schedules, manifiestos y estado de jobs | Crear jobs/intentos/leases, iniciar/cancelar proceso agéntico según política versionada | Cambiar estrategia/riesgo/promover agentes por output; reanudar pausa financiera |
| Admission/audit service confiable | Snapshot sellado, manifest y outputs | Admisión/veredicto/evidencia en store agéntico; única recepción elegida | Endpoint de órdenes, alterar históricos/manifest, interpretar silencio como HOLD |
| Jobs research/quant | Export de research permitido y datasets identificados | Solo output de su rol; scratch futuro requiere permiso separado | Secrets broker/DB, shell libre heredado, promo/config writes |
| Jobs shadow/pedagogical | Snapshot pareado / trace autorizada, package/Skill readonly | Solo propuesta shadow / explicación | Champion visible antes de sellado shadow, credenciales, órdenes, control financiero |
| Onboarding | Metadata y tests sintéticos | Reporte/config permitida reversible | Instalar/activar permiso material por defecto, Git secrets, READY financiero por smoke |

Primera ruta operacional candidata: **tools concretas de lectura solamente**. Research que necesite código, web o nuevas fuentes pasa por jobs/artefactos determinísticos aprobados o nuevo contrato de permisos; este RC0 no aprueba herramientas arbitrarias. Plan Guardian manual mantiene gobierno de cambios; no otorga permisos financieros a los jobs.

## 3. Enforcement propuesto

- Separar identidad del **caller/app-server completo** de identidad/credenciales del broker y store financiero, no solo del subproceso shell. Broker keys permanecen en servicio financiero; ningún env, mount, repo, tool, config, log ni proceso hijo agéntico las recibe.
- Separar además **dominios de visibilidad**: dispatcher/admission confiables fuera del proceso del modelo; identidad/ACL/export shadow no accede al namespace pedagógico/Champion, ni a logs/resultados hermanos. Una única identidad agéntica con snapshots y outputs compartidos no prueba blinding pareado. Paquetes de rol compartidos readonly; workspace por job con export mínimo. El proceso SDK que transporta la inferencia se ejecuta en el dominio del job; el control confiable entrega solo herramientas/snapshot permitidos, no credenciales/store. Auth nativo mínimo se resuelve legítimamente en onboarding según variante; no asumir login por rol ni compartir token por Git. Contexto/permisos por job y supervisor inaccesible se especifican en RC2.
- Login nativo Codex Team en identidad permitida, realizado legítimamente por usuario cuando corresponda. La credencial Codex es un secreto distinto; acceso mínimo necesario, fuera de Git, sin copiar tokens entre usuarios. Broker credential isolation no significa proceso Codex sin su propia autenticación.
- Research/quant reciben exports con dataset/split/version explícitos y quarantine del holdout confirmatorio. Denegar lectura por tools/filesystem/namespace del holdout antes de apertura aprobada; un prompt “no peeking” no es enforcement. Scorecards de selección consumen solo muestras autorizadas. Evidencia de acceso y exposure ledger forman parte del gate.
- Read tools reciben identificadores exactos del manifiesto, sin paths/SQL/URL libres. Validar caller/job/attempt, snapshot/hash/corte, args y tamaño antes de resolver; herramientas no ofrecen acceso a broker. Lectura autorizada aún necesita política de privacidad/licencia para envío al modelo.
- Root+rol+Skill y configuración efectiva pinadas. Allowlist de métodos **y** tool names; apps/MCP/plugins/hooks/shell/desarrollo/despliegue deshabilitados salvo necesidad específica aprobada. Descubrimiento antes de inferencia: mismatch/drift → no iniciar job.
- Denegar approvals de comandos/file changes con respuesta tipada `decline`; permissions con subconjunto vacío; elicitation con `decline` cuando aplique. Solicitud desconocida: cerrar/registrar fallo, sin default-accept ni payload genérico inválido. Verificar respuestas contra versión de protocolo. Job no solicita intervención para ampliar permisos rutinariamente.
- Egress del proceso/modelo y de tools son superficies distintas. La inferencia necesita conexión autorizada OpenAI; tools no reciben red abierta. Ninguna allowlist DNS declarada prueba bloqueo de loopback/IPC o exfiltración: pruebas de red real antes de PAPER.
- Snapshot/output files y resource limits controlados por host: límites de payload/CPU/memoria/tiempo/cola, truncación identificada nunca éxito silencioso. No modelos/billing/providers fallback.

## 4. Alternativas de aislamiento (Build-vs-Reuse)

| Opción | Recursos reutilizables / coste PAPER | Capacidad y límite | Disposición candidata |
|---|---|---|---|
| S1 misma identidad Windows + prompts/read-only/tools-off | Codex existente, incremento monetario 0 | Menor setup; no prueba aislamiento de app-server/handlers ni broker secrets bajo mismo usuario | REFERENCE_ONLY para probes; **no suficiente como frontera final** |
| S2-A cuentas Windows por dominio/rol | Controles Windows; licencia incremental esperada 0, auth/operación por medir | Puede separar perfiles/SIDs; jobs del mismo SID y harness/egress aún requieren controles | REUSE_AS_IS/WRAP, alternativa condicionada a necesidad |
| **S2-B un Agent Runner restringido + contextos efectivos por job** | Windows restricted tokens/AppContainer candidatos + native Codex; integración/operación por medir | Frontera financiera externa, supervisor inaccesible, recursos/auth/cache/red mínimos; compatibilidad y blinding no probados | REUSE_AS_IS/WRAP propuesto; dirección revisada pendiente |
| S3 VM dedicada/local, usuario y filesystem separados | VM/hypervisor disponibles solo como posibilidad, guest/licencia/capacidad no verificados | Mayor separación; login y recursos/backup/bridge aumentan setup. Mounts/red/host sockets mal configurados destruyen aislamiento | REFERENCE_ONLY reserva; evaluar si S2 no satisface amenazas |

Inventario H5: Windows 11 Enterprise 10.0.26300, hypervisor presente; python/node/git/codex presentes; docker/psql/redis-server/duckdb no encontrados en PATH. wsl.exe presente **pero WSL declara no instalado**. No prueba instalación de servicios, edición de políticas permitida, VM usable ni seguridad. Ninguna nueva cuenta/servicio se creó.

Documentación oficial describe Windows elevated con usuarios de menor privilegio/ACL/firewall y unelevated más débil; setup requiere aprobación administrativa. Esto respalda reutilización de controles, **no demuestra aislamiento del proceso SDK entero**. [Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox). App-server define approvals tipadas y dynamic tools experimentales: [protocolo](https://learn.chatgpt.com/docs/app-server). No usar Agents API sandbox pago para sustituir este ensayo.

## 5. Gate y gobierno

P1: amenaza/matriz, frontera elegida y permisos base aprobados, scripts de acceptance especificados, **probe empírico de viabilidad del aislamiento elegido bajo identidad efectiva**, revisión independiente y remediación de hallazgos críticos. Una propuesta de S2 sin acceso/ACL/IPC/red probados no cierra D-027/D-024. No exige Trading OS implementado: ensayar frontera con proceso Codex y canaries sintéticas es preparación permitida tras gobierno/config concreta. P2 antes de PAPER: ampliar al runtime/core integrado y credenciales almacenadas fuera del job, auth lifecycle, handlers unknown/escalation, plugins/config drift, backup y logs. **Ninguna canary será una credencial real.** Evidencia negativa incluye cómo se lanzó el proceso y política efectiva; ausencia de tool calls no basta.

UNKNOWN sobre control obligatorio no es permiso. Si S2 falla, mantener jobs no operacionales; comparar S3 y regresar a gobierno, nunca degradar automáticamente a S1. Dirección S2 aprobada en ADR-012; no ejecutar OS setup hasta aprobar su propuesta administrativa concreta. Seguridad y blinding separados; no cerrar D-027 por elegir dirección de ensayo.

## Especificación histórica posterior S2 RC1 — gate siguiente sustituido

[Contrato S2 RC1](08_S2_isolation_spec_RC1.md) concreta dominios F/C/R/S/P/H, filesystem/IPC/egress/secrets y snapshot blinding. [SI/BL/RB](research/R-013_S2_acceptance_matrix_RC1.md) exige positivos al mismo target y negativos bajo identidad efectiva, sin timeout/archivo ausente como PASS. [Hallazgos](research/R-013_S2_findings_2026-10-05.md): 7 observaciones esperadas, incluidas counterexamples de S1/contaminación; no S2 acceptance. Próximo gate administrativo [ADM-01](research/R-013_S2_administrative_gate_ADM01.md) requiere aprobación de tres cuentas estándar/árbol canary/ACL, aún NO ejecutado. D-027/D-024 abiertos, egress/IPC/auth no probados. Dirección ADR-012 ya aprobada; no pedir otra elección S2.

## Especificación vigente por variante — 2026-10-06

[RC2](08_S2_agent_domain_contract_RC2.md) y [acceptance proyectado](research/R-013_S2_variant_acceptance_RC2.md) conservan objetivos SI/BL/RB. El bloque RC1 anterior documenta el endpoint histórico; ADM-01 no autorizado, retirado de la secuencia activa por owner. Próximo gobierno: S2-B dirección candidata revisada; no setup. Ninguna cuenta por rol obligatoria; todo proceso job sigue confinado fuera de F/control. No cierre D-027/D-024.
