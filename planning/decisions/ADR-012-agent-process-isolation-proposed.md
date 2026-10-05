# ADR-012 — aislamiento del proceso agéntico PAPER (propuesta)

2026-10-05. D-027 P1 **READY_FOR_DECISION para dirección de aislamiento**; controles finales, verificaciones y cierre de D-027 siguen pendientes. D-024 RESEARCHING. No permiso concedido por este documento.

## Problema y evidencia

ADR-011 permite automatizar jobs sin autoridad financiera. Un JSON `authority=NONE`, prompts y read-only de comandos no aíslan por sí solos el caller/app-server/handler bajo el usuario de desarrollo. Necesitamos evitar lectura de broker secrets, writes financieros, IPC/red/control del núcleo y permisos heredados. Wave07 observa SDK default-accept; la documentación Windows describe controles de comandos con usuarios/ACL/firewall, pero no verifica aislamiento del harness completo. [Contrato y fuentes](../08_agent_security_contract_RC0.md).

Host observado Windows 11 Enterprise; WSL no instalado y Docker no encontrado. Hypervisor presente no prueba una VM lista. Cambiar identidad/ACL/red es arquitectura material bajo AGENTS; ningún cambio OS se realizó.

## Alternativas y recomendación

| Opción | Ventaja | Trade-off |
|---|---|---|
| S1 misma identidad + tools-off/read-only | Setup mínimo para investigación | Insuficiente evidencia de separación de secretos y servicios; no recomendada como seguridad final |
| **S2 identidades Windows dedicadas por dominio para SDK/app-server + ACL/IPC/egress separados** | Reutiliza host/controles existentes, coste incremental de licencia esperado 0; broker/DB financial y dispatcher/admission confiables fuera del dominio agéntico | Shadow separado de pedagogía/Champion, exports por job; setup/login Team y ACL efectivos por verificar. Codex elevated refuerza comandos, no reemplaza frontera del proceso |
| S3 VM local dedicada | Mayor separación de recursos | Más recursos/administración, login/config guest y networking; disponibilidad/coste exactos desconocidos. Reserva si S2 falla |

**Recomendación: S2 como dirección de diseño/ensayo de seguridad PAPER**, conservando S3 como alternativa explícita si no pasa. No dar fallback operacional S1. Roles/scheduler jobs nunca obtienen broker credentials ni endpoints. No requiere comprar runtime/servicio; tiempo/hardware local por medir. La elección no promete que ACL/firewall/Windows policy actual permitan todo; ese resultado será un gate.

Revisión independiente detectó que una única identidad agéntica con store compartido podría revelar Champion al shadow. S2 incluye segregación por dominio de visibilidad y export mínimo por job; no basta cambiar el nombre del usuario. Probar acceso denegado a namespaces hermanos y decisión contemporánea Champion antes de seal. La matriz/config exacta y su suficiencia permanecen gates P1/P2.

## Decisión humana exacta

**HUMAN_ACTION_REQUIRED:** aprobar S2 como frontera candidata a especificar y verificar, con S3 reserva y S1 solo investigación, o preferir S3. AGENTS exige aprobación explícita de arquitectura material de seguridad. No se pide aprobación por job rutinario ni otra aprobación ADR-011.

Esta decisión **no** autoriza aún creación de usuarios, UAC, reglas firewall, transferencia de autenticación, instalación de VM, modificación de secretos o configuración global. Tras dirección aprobada se documentará configuración concreta revisable y pasos manuales/privilegios necesarios; no dar permisos efectivos por lectura del ADR. El owner realizará login legítimo cuando toque; no copiar tokens ni Git secrets. No cierre D-027/D-024, implementación, gasto o main.
