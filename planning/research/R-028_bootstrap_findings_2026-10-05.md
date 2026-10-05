# R-028 — Environment Bootstrap, Portability & Agent Packaging

Fecha: 2026-10-05. Estado: **RESEARCHING**, P1, D-037; contrato/diseño RC0 y evidencia local. ADR-009 aprueba requisito y cohorte candidata; no cierre D-020/D-024/037 ni selección final. Fresh-clone verification pendiente en este hito.

## 1. Conclusión técnica candidata

Usar **Bootstrap Mode**, Skill repo breve y manifiesto/perfiles versionados, reutilizando Codex para discovery/inventory y eventual transporte oficial. Paquetes por rol desacoplados de ejecución; shared declara contratos canónicos. No instalar un framework agéntico ni construir un discovery engine propio. La ruta preserva tanto cwd manual como caller programático futuro; no sesiones separadas obligatorias.

La raíz Git importa: la especialización local funciona dentro del repo completo. Una carpeta suelta pierde políticas/Skills de la raíz. Reglas locales/overrides pueden prevalecer; se exige inspección de cadena y revisión de conflictos, junto con autoridad técnica externa D-027. Instrucciones no prueban ACL.

## 2. Fuentes primarias consultadas

| Fuente, abierta 2026-10-05 | Hecho pertinente / efecto |
|---|---|
| [AGENTS](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Cadena root→cwd dentro del proyecto; override por carpeta y presupuesto por defecto 32 KiB. Sin proyecto detectado solo cwd. Más cerca prevalece: revisar conflictos |
| [Skills](https://learn.chatgpt.com/docs/build-skills) | Discovery `.agents/skills` en cwd/ancestros hasta Git root; nombre duplicado no se fusiona. `shared/skills` arbitrario requiere otra integración. Listado no demuestra activación |
| [config reference](https://learn.chatgpt.com/docs/config-file/config-reference) | Root markers, `project_doc_max_bytes` y trust efectivos influyen; capa `.codex/` de proyecto untrusted se omite. Evitar asumir que clone aplica config |
| [App Server](https://learn.chatgpt.com/docs/app-server) | Inventario/estado/config y thread/turn nativos; observar superficies y enabled/callable, sin conceder permisos por metadata |
| [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Declaraciones nativas de roles/TOML son opción de configuración, distinta de paquete lógico portable; no elegidas ni probadas aquí |
| [plugin packaging](https://developers.openai.com/plugins/build/plugins) | Distribución portátil y configuración local/marketplace disponibles; trust/auth/servicios son distintos. Reservar para D-024, no requisito para assets locales |

`skill-installer` público disponible en el entorno actual fue inspeccionado como alternativa de adquisición de assets externos. El clone ya transporta la Skill propia; no ejecutamos instalación global. Creador/validador de Skills existente reutilizado: frontmatter de bootstrap válido. No copiar bundles propietarios Data o entitlement Team.

## 3. Probe nativo preregistrado

[Protocolo](R-028_bootstrap_probe_protocol.md). Fixture Git temporal, raíz + dos roles, Skill común `.agents/skills`, Skill local research y Skill fuera de discovery en shared. Sin inyectar `baseInstructions`/`developerInstructions`; sin extraRoots. Shell/apps/web/MCP/subagents deshabilitados, sandbox read-only, login nativo ChatGPT, sin API key/billing, no broker/secretos. CLI **0.159.0-alpha.12.1**, modelo **gpt-6.1-sol**, medium; cuenta `type=chatgpt`, `planType=team` en intento 04.

| Caso | `instructionSources` observado | Respuesta observable |
|---|---|---|
| root | repo/AGENTS.md | Marker raíz, rol NONE, autoridad NONE |
| research | raíz + agents/research/AGENTS.md | Marker raíz + research + cuerpo Skill local invocada |
| shadow | raíz + agents/shadow/AGENTS.md | Marker raíz + shadow; sin Skill/rol research |
| aislado sin Git | solo isolated-shadow/AGENTS.md | Global NONE, rol shadow; sin Skills raíz |
| override controlado | raíz + AGENTS.override.md local | Marker raíz + override; archivo local AGENTS.md anterior sustituido |

**5/5 turnos completados**, marcadores esperados en los cinco, cero solicitudes de herramientas. Solo conteos de tipo `reasoning` se conservan; no contenido de razonamiento. Latencias 19.804/11.919/6.152/35.981/7.250 s son de smoke Team, no quota/SLA Plus.

Skill común descubierta en root/research/shadow; local solo research; shared arbitrary no aparecía; aislado vacío para estas Skills. Registro completo sanitizado: [intento 04](probes/r006-portability/result-native-attempt-04.json), [metadata intento 03](probes/r006-portability/result-native-attempt-03.json).

## 4. Fallos y calibración conservados

- Intento 01: `account/read` error interno -32603 antes de inferencia. Resultado y script conservados.
- Intento 02: el mismo error no impidió inventory/metadata, cuatro cwds; formato `instructionSources` era string/path y el harness no lo parseaba. No se produjo inferencia; no claim de activación.
- Intento 03: parser corregido conforme al schema generado de la CLI; metadata-only, sin repetir lectura de cuenta. Root+roles y override visibles. Primeros resultados no se reemplazaron.
- Lectura CLI `login status` readonly: exit 0, logged-in; respuesta original no retenida. Comprobación posterior `account/read` se recuperó sin login/config/autorización nueva. No atribuir causalidad a credenciales o entitlement.
- Intento 04: los cinco turnos y resultado se guardaron, **proceso del harness salió 1 por cleanup TEMP Windows WinError 32** después de cerrar app-server. No borrar resultado ni presentar exit 0. El lifecycle/cleanup de una ruta nativa es un caso a validar en GP5/EB6; esta prueba no demuestra recovery limpio.

## 5. Contrato/readiness offline

[Resultado](probes/r006-portability/result-offline-attempt-01.json): **31/31 checks** con jsonschema y stdlib reutilizados. Manifiesto/refs válidos, seis roles únicos, presupuesto root+rol menor de 32 KiB (global personal adicional no evaluado); paths que escapan rechazados. Schema/semántica simulada discrimina Team vs target, UNKNOWN/fail/NOT_TESTED, evidencia vacía, requisito omitido/downgrade, manifest drift, gates duplicados/de otro entorno, autoridad/lock, campo secreto sintético, login pendiente, optional y fallback propuesto. Igual input serializado produce igual clasificación; no es recovery durable.

Fixtures **SIMULATED_NOT_EXECUTED_TARGET**. Un fixture synthetic Plus válido no prueba acceso Plus. Schema no es detector universal de secretos dentro de strings ni verifica veracidad de evidencia: revisión/admisión externa reales son requeridas. No construir validador operativo desde este probe.

## 6. Artefactos y límites

Entry point [ONBOARDING](../../ONBOARDING.md); [contrato bootstrap](../07_environment_bootstrap_contract_RC0.md), [packaging](../07_agent_packaging_contract_RC0.md); seis paquetes bajo agents; shared manifest/schema/expected Plus; Skill propia candidata; `.local/` ignorado para perfiles/config privados. Roles actuales solo planificación; Plan Guardian inactivo hasta freeze.

**PAPER coste** adquisición/licencia de documentos propios 0; runtime/cuota/cómputo condicional GP. **LIVE coste** UNKNOWN operación/escala; manual gratuito como fallback de preparación, no equivalencia shadow autónomo. Pago solo si ADR-008 justifica capacidad material y dueño lo aprueba. No cambio broker/data/Strategy/riesgo/autoridad ni producción.

## 7. Impacto R-006 y gates

Shortlist permanece candidata aprobada, SELECTED=NO. Añadir C-030 native instruction/discovery REUSE_AS_IS, C-031 Bootstrap Mode/paquetes ADAPT y C-032 roles nativos REFERENCE_ONLY. Plugin distribution es reserva C-002. Assets gratuitos y método independientes de plan; disponibilidad/activación y suficiencia **target Plus UNKNOWN**. El transporte final deberá conservar contratos globales/rol y reportar entorno/gates, pero no se congela topología.

Antes de D-024/DoR: EB1–8 para ruta seleccionada más GP1–7, permisos/review críticos y decisiones correspondientes. Fresh clone local valida transporte de assets y discovery en este equipo; no es una máquina recién instalada ni aceptación Plus.

## 8. Próximo trabajo autónomo de este paquete

Commit/push del diseño y evidencia focal; clonar ese commit a TEMP, comprobar manifiesto/rules/Skill reales y referencias desde clone sin este chat. Persistir perfil sanitizado/readiness parcial y deltas a Plus Gate. Después del endpoint, acceso Plus y gobierno material según evidencia; no pedir otra aprobación de cohorte ni repetir investigación conductual completa.
