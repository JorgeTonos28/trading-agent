# Agent Packaging — contrato candidato RC0

2026-10-05. ADR-009 requisito aprobado; D-037 RESEARCHING, D-020/D-024 no seleccionados. Documentos/instrucciones permitidos durante preparación; no implementación del Trading OS.

## Unidad de paquete

Un paquete es una unidad versionada de **rol, procedimientos, outputs y dependencias**, independiente de su forma de ejecución. `agents/<id>/AGENTS.md`, README común, `package.json`; añadir Skills/referencias/schemas/evals específicos solo cuando aporten valor. `shared/bootstrap_manifest.json` referencia assets comunes canónicos, que no se duplican por rol.

Campos: package_id/version/lifecycle, working_directory, instruction_path, global_instruction_path, contracts[], candidate_procedure_path opcional, dependencies[], authority, permissions_contract, manual_entry y programmatic_entry. Rutas relativas a raíz, normalizadas, sin `..` ni escape por symlink; scripts no se ejecutan por mencionar una dependencia. Dependencies distingue localtool, publicasset, capability y externalaccount; requisito no implica instalación ni entitlement. Pins de documentos + commit/hash se sellan en cada perfil/run, evitando commit autorreferencial en el propio manifiesto.

El estado del paquete `PLANNING_ONLY` no afirma que exista un agente operativo. Plan Guardian `DORMANT_UNTIL_APPROVED_FREEZE`; la especialidad se usa hoy para revisar el borrador como Plan Architect. Market Research se corresponde con RESEARCH_IDEA, Quant Research con QUANT_REVIEW, PM con PORTFOLIO_SHADOW y pedagogía con PEDAGOGY del contrato de evidencia. Onboarding produce perfil/reporte, sin intervenir en esas autoridades financieras.

## Uso manual y programático

| Ruta | Mecanismo candidato | Verificación y límites |
|---|---|---|
| Codex cwd dentro del clone | Discovery nativo de root→cwd y Skills `.agents/skills` | Confirmar Git root, fuentes activas, rol correcto, overrides/conflictos/truncación; app/UI concreta necesita gate propio |
| Caller SDK/app-server | Cwd del paquete o carga explícita verificada del mismo contrato | Caller fija rol/schema/tools; si sobreescribe base/developer instructions debe demostrar incorporar reglas globales. Folder no asigna ACL |
| Subagents nativos | Configuración custom agents de Codex como referencia | Config específica por versión/superficie y potencial override de settings; no habilitado/seleccionado ni necesario |
| Plugin portable | Distribución opcional posterior de Skills/MCP | Trust/auth/install/servicios separados; no copiar plugins propietarios ni asumir que rutas externas shared funcionan dentro del bundle |

El hecho documentado de que reglas locales prevalecen obliga a revisar cambios de paquete contra invariantes. La política del proyecto prohíbe reducir la autoridad global; protección técnica independiente se resolverá en D-027, no por prompt.

## Skills compartidas y específicas

Recomendación revisable: root `.agents/skills` para workflows verdaderamente comunes; paquete `.agents/skills` para procedimiento específico. Contratos/referencias comunes bajo shared o planning. No usar symlinks como requisito de onboarding. Programmatic wrapper resuelve la Skill descubierta por nombre/path/version y la pasa explícitamente si su contrato lo necesita; no asumir que el listado equivale a activación. Nombres únicos para evitar ambigüedad de dos Skills homónimas. El wrapper puede referenciar un contrato sin convertirlo en Skill obligatoria.

Los cuatro procedimientos finalistas de R-006 permanecen candidatos ADAPT/PORT; paquetes no hacen su selección final ni convierten sus fixtures en agentes de producción.

## Integridad y portability

- Clone completo, commit/manifest hash y hashes de reglas/Skill/schema/fixtures; versiones de Codex/SDK/herramientas fuera del repo registradas.
- Global personal instructions/config externos se inventarían por existencia/hash sanitizado cuando proceda, **sin copiar su contenido privado**; nunca computar/exportar hashes de credenciales.
- Config efectiva, requirements gestionados, confianza del proyecto, overrides y límites pueden cambiar el comportamiento; reportarlos sin elevar permisos.
- Fresh-clone smoke no depende de carpetas de este equipo/chat. Autenticación y capacidad de inferencia son prerequisitos explícitos, no un asset Git.
- Artefacto de release/plugin futuro debe ser autosuficiente respecto de sus rutas y preservar licencia/NOTICE. Cambios de formato upstream producen drift y regresión focalizada.

## DoR

D-024 requiere manual/programmatic entry definidos para las rutas seleccionadas, dependencias y permisos aprobados, bootstrap target verificado, fallbacks equivalentes con pruebas y review crítica. No es necesario seleccionar ambas rutas ni sesiones separadas por paquete. El contrato de empaquetado se puede endurecer antes de seleccionar un runtime; D-037 continúa abierto hasta comprobar ruta target y resolver integración final.

Fuentes primarias, 2026-10-05: [AGENTS](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Skills](https://learn.chatgpt.com/docs/build-skills), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [plugin packaging](https://developers.openai.com/plugins/build/plugins), [config](https://learn.chatgpt.com/docs/config-file/config-reference), [App Server](https://learn.chatgpt.com/docs/app-server). Recomendación de arquitectura por Plan Architect, no garantía transversal de producto.
