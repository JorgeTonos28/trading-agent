# R-028 — Protocolo de Bootstrap, Portability & Agent Packaging

2026-10-05. `RESEARCHING`, P1, D-037; prerrequisito de D-020/D-024/DoR. ADR-009 registra el requisito aprobado. Preregistro anterior a ejecutar los probes; resultados posteriores en dossier separado.

## Preguntas y alternativas

- ¿Root + nested AGENTS se cargan automáticamente? Git root, cwd, override, presupuesto de instrucciones y personalización pueden cambiar el resultado.
- ¿Skills compartidas/por rol se descubren desde `.agents/skills`? `shared/skills` arbitrario no es una garantía de discovery; probar sin `extraRoots` primero.
- ¿Paquete requiere proyecto/sesión independiente? Comparar cwd manual y app-server programático con contratos iguales; no decidir topología.
- Reutilizar discovery/config/inventario nativos y procedimientos públicos antes de construir instalador/orquestador propio. Plugin es opción posterior de distribución, no condición para clonar assets locales.

## Probes previstos

### P-A — Fixture fresca y transporte nativo Team

Crear Git root temporal con reglas globales y dos paquetes, Skill raíz, Skill local por rol y Skill en `shared/skills` fuera de discovery. No copiar auth ni modificar home/config. Usar login nativo existente solo como proveedor de inferencia Team. No imponer `baseInstructions`/`developerInstructions` para la prueba de carga automática. Shell/apps/MCP/subagents/web deshabilitados; no broker/datos reales. Responder únicamente marcadores sintéticos con schema estricto.

Casos: cwd raíz; cwd de cada rol; carpeta copiada aislada sin Git root; `AGENTS.override.md` controlado en fixture. Verificar raíz+rol correcto, ausencia de rol hermano y ausencia de falsa herencia en carpeta aislada. `instructionSources` más una respuesta observable (no chain-of-thought) cuando sea viable. Skills inventory habilitada vs activación son comprobaciones distintas; al menos una invocación explícita con marcador de cuerpo. Paths de salida relativos, cuenta solo type/plan, sin IDs/token/email.

### P-B — Contrato y readiness sin modelo

Fixtures de target UNKNOWN/Plus validado/fallo crítico/opcional ausente/fallback pendiente; validar schema, acciones manuales, prohibición de readiness heredado Team, idempotencia y detección de drift. Reusar jsonschema/stdlib, no producir instalador ni workflow financiero. Simulación no demuestra entitlement ni recovery durable del runtime.

### P-C — Fresh clone de los paquetes de planificación

Después del commit de paquetes, clonar localmente el commit exacto a TEMP; repetir inventory/root+rol y referencias/hashes sin historia de chat. Verificar ausencia de paths absolutos/secrets y manifiesto íntegro. Auth/cliente/localtools son prerequisitos externos explícitos; este probe no es una máquina nueva ni Plus.

## Criterios y límites

Registrar fallos originales antes de corregir harness; no reemplazar intentos. Un resultado negativo cambia contrato/procedimiento, no autoriza permisos extra. Pasar marcadores no prueba aislamiento ACL, suficiencia operacional o DoR. Ninguna capability queda SELECTED por este probe.

Fuentes primarias abiertas antes del diseño: [AGENTS](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Skills](https://learn.chatgpt.com/docs/build-skills), [App Server](https://learn.chatgpt.com/docs/app-server). Versiones locales fijadas en resultados. Gate Plus no se ejecuta aquí.
