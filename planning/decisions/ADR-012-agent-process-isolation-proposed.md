# ADR-012 — aislamiento del proceso agéntico PAPER (dirección S2 aprobada)

2026-10-05. **DECIDED: dirección candidata S2 aprobada por el propietario**; D-027 P1 RESEARCHING: controles finales, verificaciones y cierre siguen pendientes. D-024 RESEARCHING. No permiso concedido por este documento.

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

## Propuesta original — resuelta por aprobación posterior

**Pregunta histórica, ya resuelta:** aprobar S2 como frontera candidata a especificar y verificar, con S3 reserva y S1 solo investigación, o preferir S3. AGENTS exige aprobación explícita de arquitectura material de seguridad. No se pide aprobación por job rutinario ni otra aprobación ADR-011.

Esta decisión **no** autoriza aún creación de usuarios, UAC, reglas firewall, transferencia de autenticación, instalación de VM, modificación de secretos o configuración global. Tras dirección aprobada se documentará configuración concreta revisable y pasos manuales/privilegios necesarios; no dar permisos efectivos por lectura del ADR. El owner realizará login legítimo cuando toque; no copiar tokens ni Git secrets. No cierre D-027/D-024, implementación, gasto o main.

## Decisión vigente del propietario — 2026-10-05

El propietario aprueba **opción S2 como dirección candidata PAPER**, no como aislamiento ya demostrado. Identidades/procesos Windows separados por dominio de confianza, permisos mínimos efectivos y separación de filesystem, secretos, IPC y red. S3 VM dedicada permanece fallback formal sujeto a nueva decisión si S2 falla; S1 solo investigación/probes sin secretos, nunca fallback operativo PAPER.

Antes de cerrar D-027/D-024 deben probarse: inaccesibilidad de broker credentials y secretos core; ausencia de escritura de estados financieros; bloqueo directo de Execution/broker endpoints; ACL explícitas; control/IPC restringido; egress mínimo; allowlists/fail-closed; ausencia de permisos heredados de desarrollo; separación de workspaces/stores; exports mínimos versionados por job; negative tests entre dominios/namespaces y auditoría de rechazos. Crear usuarios distintos, prompts, AGENTS o `authority=NONE` no satisfacen el gate.

**Security isolation** y **experimental blinding de Shadow** son objetivos/gates separados. Shadow no recibe información contemporánea Champion fuera del snapshot pareado. Se especificarán criterios objetivos de insuficiencia S2 y reevaluación S3 antes de ejecutar acceptance.

Autorizado: especificación y pruebas no administrativas/destructivas con fixtures sintéticas. **No autorizado todavía:** crear usuarios, modificar ACL/firewall/políticas/credenciales, mover secretos o configurar privilegios. Primero preparar propuesta concreta revisable; detenerse con `HUMAN_ACTION_REQUIRED` al necesitar ese cambio. No solicitar otra aprobación de la dirección S2. No cierre D-027/D-024, implementación, gasto ni cambios a A+, G1+G2 o ADR-006.
