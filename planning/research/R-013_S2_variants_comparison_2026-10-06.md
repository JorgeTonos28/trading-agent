# R-013 — S2-A, S2-B y S3: cuentas, seguridad y blinding

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


2026-10-06. **READY_FOR_DECISION: recomendar S2-B como dirección candidata revisada.** D-027/D-024 RESEARCHING. El propietario no autoriza S2-ADM-01; no crear usuarios ni modificar ACL/firewall/políticas. Comparativa de diseño, sin aceptación operacional. [ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md).

## 1. Corrección de la premisa

La aprobación S2 de 2026-10-05 exige separar técnicamente la capa agéntica del dominio financiero. El mapeo posterior de cada rol a una cuenta Windows fue una propuesta de realización, no una necesidad demostrada. El propietario reabre esa granularidad el 2026-10-06 y prefiere un Agent Runner si preserva la frontera. Conservamos RC1 y ADM-01 como antecedentes; no atribuimos su configuración al propietario.

**Respuesta:** ninguna amenaza identificada exige por sí misma una cuenta Windows por nombre de rol. La amenaza exige contextos efectivos de acceso que distingan los recursos permitidos de cada job. Una cuenta por dominio es una forma de obtenerlos. Restricted tokens o AppContainer son mecanismos alternativos que merecen probarse bajo un único usuario base; su compatibilidad integral con Codex todavía es UNKNOWN.

S2-B no equivale a una cuenta común irrestricta con carpetas de nombres diferentes. Si todo job recibe el mismo token y puede ejecutar código con acceso al perfil/store compartido, la separación documental no limita sus lecturas. Las allowlists de handlers tampoco confinan syscalls de un proceso comprometido. [DACL y access tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/how-dacls-control-access-to-an-object).

## 2. Amenazas y objetivos separados

| Ataque/fallo concreto | Objetivo afectado | S2-A | S2-B exigido | S3 |
|---|---|---|---|---|
| Job ejecuta código arbitrario e intenta leer broker secrets, escribir DB financiera o llamar Execution/control | SECURITY ISOLATION | Core fuera de cuentas agénticas + permisos/red/IPC efectivos | Core fuera del Runner + permisos/red/IPC efectivos de **todo** SDK/app-server/tools/children | Core fuera del guest + puentes, mounts y red mínimos verificados |
| Shadow lee un fichero Champion que Pedagogy recibió después de la decisión | EXPERIMENTAL BLINDING | Cuentas distintas pueden denegar fichero ajeno; aún se debe exportar snapshot correcto | Contexto por job deniega export ajeno; snapshot predecisión se crea antes del join Champion | Una VM compartida necesita la misma segregación de vistas |
| Shadow accede al proceso del supervisor o hereda un handle/token con permisos más amplios | SECURITY y, si obtiene otros exports, BLINDING | Permisos de procesos y handles siguen siendo necesarios | Proteger supervisor/IPC/handles/token/memoria/desktop es obligatorio; usuario base común no demuestra protección | También proteger supervisor guest y canales host |
| Job anterior copia información a perfil/cache y otro job la recupera | BLINDING y posible integridad del workflow | También ocurre entre jobs de la misma cuenta de rol | Estado por job; persistencia mínima autorizada separada de threads/history; tests de relaunch | Guest/profile común también permite persistencia |
| Export omite campo Champion pero lo codifica en signals/metadata o una vista contiene holdout | BLINDING | Usuarios distintos no reparan el linaje de ese export | DAG/linaje validado externamente y política de campos predecisión | VM tampoco repara el linaje |
| SDK obtiene grants amplios a Users/Everyone, perfil completo, DLL/config writable o egress libre para funcionar | SECURITY/operación | Distintos usuarios no neutralizan grants de grupo ni binarios compartidos writable | Ampliación prohibida sin diff, justificación y regresión de negativos; no compartir identidad privilegiada | Guest puede seguir exponiendo host/core por mounts/red |
| Usuario administrador local o host comprometido | Fuera de la frontera de procesos estándar considerada | No protege contra administrador host | No protege contra administrador host | Guest no elimina control del administrador del host; reevaluar threat model LIVE |

Ejemplo causal relevante: Pedagogy recibe `champion_decision_id/sizing` → lo conserva en fichero/cache permitido al usuario común → Shadow, mediante una herramienta comprometida o acceso general al filesystem, lee ese recurso antes de sellar su propuesta. El experimento pierde independencia aunque nunca se envíe una orden. S2-A puede impedir la lectura cruzada por SID. S2-B puede impedirla si todo el job opera bajo un contexto restringido que no autoriza dicho fichero, ni el proceso/cache/handler que lo sirve. Un `role=shadow` en JSON o una carpeta distinta no basta. No inferimos que el LLM necesariamente realizará ese ataque.

## 3. Comparativa operacional

Valoraciones cualitativas de ingeniería; no son probabilidades medidas ni benchmarks de despliegue.

| Criterio | S2-A: cuentas por dominio/rol | S2-B: Runner + contención efectiva por job | S3: VM agéntica |
|---|---|---|---|
| Seguridad financiera | Frontera OS respecto del core; depende de grants, IPC/red y harness completo | Misma frontera OS respecto del core posible; supervisor y token por job requieren pruebas | Frontera guest/host más fuerte; depende de puentes/mounts/red |
| Amenaza adicional mitigada | Acceso directo entre procesos/perfiles de usuarios distintos, si permisos correctos | Puede mitigar lo mismo por contexto restringido; viabilidad nativa pendiente | Aislamiento de recursos host/guest; no garantiza separación entre roles guest |
| Amenazas remanentes | Grupos amplios, children, stores por rol, cache entre jobs, export contaminado, auth/egress | Escape al supervisor/token, mismo perfil persistente, integración Codex/DPAPI/IPC/egress, export contaminado | Shared folders/clipboard/bridge, guest compartido, auth, export contaminado |
| Complejidad y onboarding | Más cuentas, bindings SID, logins y políticas repetidos; mecanismo de separación conocido | Menos cuentas/login domains; más cuidado del supervisor y launcher/contención por job | Guest, versiones, recursos, bridge, backups, login y controles dentro de VM |
| Recovery/mantenibilidad | Restore de múltiples identidades/perfiles; controlar jobs dentro de cada SID | Rehidratar jobs/contextos y persistencia mínima; no elevar job para recovery | Restore guest y configuración host/guest; controles de snapshot y epoch siguen necesarios |
| Reproducibilidad/configuración | Matriz de cuentas/grants/auth crece con dominios; nombres no son SIDs portables | Matriz de recursos/capabilities por job; coste del wrapper y capacidad nativa por verificar | Imagen/versiones + host integration + bridge; no snapshot con secretos en Git |
| Misconfiguration | Más bindings repetidos; un permiso de grupo puede invalidar todos | Menos cuentas no implica menos errores: grants compatibles con runtime y supervisor son críticos | Más capas; un mount/red amplio puede reconectar el core |
| PAPER | Factible candidato, no probado; no exigir una cuenta por rol sin necesidad | **Preferido para investigar** por preferencia del propietario y ausencia de necesidad probada de cuentas por rol | Reserva si frontera verificable S2 no es viable |
| LIVE | Reevaluar seguridad, operativa, coste y migración Plus | Reevaluar mismos criterios; aprobación PAPER no implica suficiencia LIVE | Puede justificar coste/recursos con evidencia; no seleccionada automáticamente |

S2-A aporta valor cuando una capacidad no puede restringirse por job de forma verificable bajo un usuario común: por ejemplo, Codex solo funciona con acceso irrestricto al perfil que contiene history Champion o un servicio IPC autenticado únicamente por SID no puede diferenciar jobs. Esto es una **condición a probar**, no un resultado observado. Primero evaluar una separación mínima por dominio de confianza/visibilidad (por ejemplo Shadow vs otros), no multiplicar cuentas por todos los nombres de rol. S3 requiere nueva decisión si S2 es insuficiente.

## 4. Build-vs-Reuse y evidencia práctica

### Hechos documentados

- Windows permite restricted tokens con restricción de privilegios/SIDs y comprobación doble del acceso. `WRITE_RESTRICTED` limita escrituras: es insuficiente para proteger lectura de información Champion. [Restricted tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/restricted-tokens), [CreateRestrictedToken](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken).
- AppContainer admite aplicaciones Win32 no empaquetadas y aporta un contexto de aislamiento distinto sin exigir una cuenta Windows por rol. Profile/capabilities, persistencia y compatibilidad requieren setup/pruebas autorizados. [AppContainer isolation](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation), [Win32 legacy applications](https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-for-legacy-applications-).
- La frontera de comandos de Codex Windows no equivale a confinamiento completo de model/auth/client/connectors/MCP/browser. El sandbox unelevated bajo token restringido es una referencia útil, con límites documentados de red; no prueba un Agent Runner operativo. [Windows sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox), [tráfico y approvals](https://learn.chatgpt.com/docs/agent-approvals-security).
- El app-server puede exponer ejecución fuera de su sandbox de comandos; declarar external sandbox no crea una barrera por sí solo. [App-server](https://learn.chatgpt.com/docs/app-server).

### Probe no administrativo realizado

[Fuentes, intentos y alcance](probes/r013-s2-variants/README.md). Se crearon **handles de tokens restringidos y security descriptors transitorios en memoria**, manteniendo el mismo TokenUser, sin ejecutar procesos bajo esos tokens ni aplicar descriptores a objetos reales. `AccessCheck` permitió vistas distintas para dos restriction SID sintéticos con el mismo usuario base: **10/10 checks semánticos** en intento 02. Intento 01 ERROR WinError5 conservado; corregida duplicación del handle de token con derechos adecuados.

**Conclusión acotada:** cuentas distintas no son la única forma disponible en Windows de distinguir permisos. No acredita filesystem/process/IPC/network reales, Codex/auth, audit, bootstrap, cuotas o blinding operacional. La canary financiera es un descriptor sintético, no un core protegido ni una credencial. `AccessCheck` no genera auditoría OS. Todos los SI/BL/RB efectivos permanecen NOT_TESTED. [AccessCheck](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-accesscheck).

Revisión independiente añadió dos precisiones: owner definido por principal/rights, no PID, y tests de WRITE_DAC/WRITE_OWNER/READ_CONTROL sobre supervisor/proceso/token/IPC; control `financial_canary` de la toy es **ungranted object** sin positivo autorizado ni comparación base, no evidencia financiera. Incorporados en RC2/VP y README; fuentes/resultados históricos conservados. [Revisión](R-013_S2_independent_review_2026-10-06.md).

Focal posterior: 27 observaciones AccessCheck in-memory de derechos estándar/owner. Token base con owner=usuario permitió READ_CONTROL/WRITE_DAC; ACE OWNER RIGHTS cero los denegó. Ambos tokens restringidos denegaron esos derechos y WRITE_OWNER en los descriptores ensayados. No bypass observado en ese fixture; demuestra por qué importa el contexto efectivo y no solo la cuenta. No prueba procesos/IPC/supervisor reales ni elimina VP-03/04. Los diez checks originales repetidos por el harness no se suman como evidencia única nueva. [Detalle fuente/resultados](probes/r013-s2-variants/README.md).

Disposiciones candidatas: controles Windows `REUSE_AS_IS / WRAP`; restricted tokens `WRAP` sujeto a compatibilidad; AppContainer `REFERENCE_ONLY` hasta probe autorizado; Job Objects lifecycle `REFERENCE_ONLY / WRAP`, nunca barrera por sí solos. No construir un sandbox propio ni seleccionar launcher, servicio o runtime definitivo a partir del probe. Codex base/SDK y metodología gratuitos mantienen las disposiciones ADR-011.

## 5. Economía por fase

| Campo | S2-A | S2-B | S3 |
|---|---|---|---|
| PAPER_V1_VIABLE_FREE | CONDITIONAL: host/licencia + native Team y gates | CONDITIONAL: host/licencia + native Team, wrapper viable y gates | UNKNOWN: host/guest/licencia/recursos no validados |
| PAPER_V1_COST | Sin compra activada; licencia incremental esperada 0, operación/auth/ingeniería no medidos | Sin compra activada; licencia incremental esperada 0, integración/contención/operación no medidas | Sin compra activada; licencia guest/hardware/backup/operación desconocidos |
| LIVE_COST | Migración Plus + recursos/operación y posibles servicios por evaluar | Mismos campos; no prometer menor coste total que A | Licencia/compute/storage/operación + servicios por evaluar |
| FREE_ALTERNATIVE | S2-B condicionado | S2-A condicionado, separación mínima por necesidad | S2 verificado; virtualización local si licenciada/suficiente |
| PAID_INCREMENTAL_VALUE | Sin propuesta paga nueva | Sin propuesta paga nueva | Posible aislamiento/continuidad material; no medido |
| ECONOMIC_JUSTIFICATION_REQUIRED | Antes de gasto y si coste operativo cambia elección | Antes de gasto y si wrapper/soporte cambia elección | Sí para recursos/licencias/servicios adicionales |

Coste fijo/variable/mensual/escalado: no servicio externo contratado ni precio mensual inventado; tiempo y recursos UNKNOWN hasta laboratorio. Dependencia: Windows policy/native Codex; exit hacia otro aislamiento exige revalidación. Beneficio esperado B: reducir cuentas/auth repetidos conservando los contratos. Pagar se justificaría ante mejora material demostrada y aprobación ADR-008. Skills/templates siguen gratuitos. PAPER Team; Plus exclusivamente PRE-LIVE.

## 6. Recomendación y decisión exacta

**Recomendar S2-B como dirección candidata revisada**, con [contrato RC2](../08_S2_agent_domain_contract_RC2.md) y [proyección de acceptance](R-013_S2_variant_acceptance_RC2.md). Una identidad Windows restringida para AI Domain; core/control financiero fuera; permisos/estado/contextos por job efectivamente verificables. Los paquetes de roles no determinan cuentas, sesiones ni topología D-024.

No afirmar que B satisface ya los contratos. Compatible Codex/auth/refresh + red/IPC/proceso + persistencia/blinding + bootstrap/workload es el gate real. Preservar S2-A como alternativa condicionada a una insuficiencia concreta de B y S3 como reserva formal si S2 no puede demostrar la frontera. Sin fallback PAPER S1 ni migración silenciosa.

**HUMAN_ACTION_REQUIRED:** confirmar esta dirección candidata S2-B revisada antes de sustituir el laboratorio administrativo. Esta decisión no autoriza setup; S2-ADM-01 queda DEFERRED/NOT_AUTHORIZED por instrucción expresa. Una futura propuesta de laboratorio tendrá diff, permisos, controles positivos/negativos, alcance y rollback propios. D-027/D-024 siguen abiertos; no implementación, gasto, main, Strategy V1 o autoridad financiera modificados.
