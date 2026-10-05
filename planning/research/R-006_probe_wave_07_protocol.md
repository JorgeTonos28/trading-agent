# R-006 wave 07 — protocolo preregistrado Team

2026-10-05. ADR-010, PAPER_RUNTIME_ENVIRONMENT=Team. Probes desechables, no implementación. Modelo gpt-6.1-sol / medium, CLI actual 0.159.0-alpha.12.1, SDK Python público 0.160.0 pinado; no instalar/actualizar global ni activar API facturada.

## Preguntas y límites

1. ¿El cliente oficial tipado de bajo nivel cubre Skill inputs, dynamic tools, structured output y carpeta de rol sin construir un transporte JSON-RPC propio?
2. ¿Un cliente nuevo puede rehidratar un job desde commit/Skill/schema/snapshot versionados sin historia de conversación? Recuperación del contexto es distinta de almacenamiento durable y auth lifecycle.
3. ¿Un payload representativo de 20 instrumentos/40 observaciones PIT y al menos 32 KiB descubre un fallo inmediato de capacidad, latencia, cola o trazabilidad en Team?

Prueba **acotada de factibilidad**, no WL-R sostenido. Ocho jobs planeados: research mínimo, research Skill, quant Skill, shadow Skill A/B (mismo contexto, cliente reiniciado), pedagogía Skill A/B, tool failure research Skill. Los siete jobs con datos suficientes exigen entrega funcional; failure se evalúa aparte como abstención correcta. Tres jobs (shadow A/B y pedagogía A) simulan llegada en burst común, preservando tiempo de espera en cola. Máximo 2 lecturas/job, deadline interrupt 210 s desde servicio; shadow propuesta de plazo 120 s desde llegada. No SLA ni cadencia financiera aprobados.

El contexto amplio es un fixture sintético de tamaño/selección PIT; los cálculos/decisiones por rol usan el spine focal anterior. No afirma capacidad de optimización multiasset ni calidad de datos reales. Elegibilidad externa filtra revisiones futuras/UNKNOWN; metadatos de exclusión y una instrucción inyectada no conceden rol/autoridad.

## Controles preregistrados

- Login nativo `chatgpt`, plan observado Team; no claves facturadas ni fallback de proveedor/modelo. Cuenta se registra solo tipo/plan; nunca tokens/IDs de cuenta.
- CodexClient oficial con **approval_handler explícito**: solo `read_evidence` con bundle exacto y límite 2; cualquier otra solicitud bloqueada. Shell/apps/MCP/web/subagentes deshabilitados; sandbox read-only/network tools false; sin broker/secretos/órdenes.
- SDK default approval handler acepta comandos/fileChanges (inspección fuente); prueba offline de ese comportamiento y de nuestro rechazo, sin ejecutar ningún comando solicitado. No REUSE_AS_IS del default.
- Git fresh clone pinado del hito ADR-010; root+rol nativos sin base/developer override. Contrato sintético confiable suministrado por caller junto al schema fijo; Skill registrada/activada explícitamente. Las cuatro Skills siguen prototipos, no instalación final.
- Outputs: schema, marker, snapshot/hash/clocks, facts/PIT, cálculos y cantidad/notional/cancel/causa según admission v2 ya definido antes de este ensayo; no modificar evaluador después sin nueva versión y resultado separado.
- Reinicio de proceso antes del shadow B; same job manifest/snapshot, nuevo ephemeral thread. Comparar firma canónica. Dup/late/no-output se clasifican fuera del LLM con fixture de ledger; no claim durable workflow real.
- Persistir output/checks/metadata fallos por intento; no stderr/raw reasoning/historia/autenticación. Reportar latencia servicio/espera/total y accounting completo; cuota solo si lectura nativa disponible. Interrumpir si límite/acceso insuficiente, registrar faltantes; no comprar capacidad.
- Smoke adicional onboarding puede corroborar target Team/reglas/manifest desde fresh clone sin chat; no final READY_AGENT_ENVIRONMENT por selección ausente.

## Endpoint

Tras estos probes y su evaluación: matriz madurez por TP/EB, gaps de implementación/operación y dossier comparativo PAPER para D-020/D-024. Decisión material del dueño precede selección de runtime/permisos; revisión crítica independiente y otros P0/P1 preceden DoR/freeze. Plus PRE-LIVE no participa. Commit/push protocolo antes de inferencia y resultados antes de pedir decisión.
