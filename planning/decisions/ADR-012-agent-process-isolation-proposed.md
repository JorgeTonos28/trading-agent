# ADR-012 — aislamiento PAPER: dirección candidata S2-B aprobada

## Estado vigente — confirmación explícita del propietario, 2026-10-06

**DECIDED: S2-B como dirección candidata principal de validación PAPER.** Una identidad base Agent Runner, con aislamiento efectivo por job; mantener la arquitectura simple preservando la frontera AI/Agent Domain → Trusted Financial Core. Security isolation y experimental blinding tienen contratos y evidencia separados.

El propietario autoriza diseñar/preparar pruebas; conserva S2-A como alternativa si tests demuestran insuficiencia de aislamiento por job y S3 como reserva si S2 no cumple seguridad. No selección final de mecanismo/launcher ni suficiencia operacional; D-027/D-024 RESEARCHING. Role packages no prescriben cuentas/sesiones.

**No cambios administrativos autorizados:** Windows users, ACL, firewall, credenciales o configuración global. S2-ADM-01 de tres cuentas permanece DEFERRED/NOT_AUTHORIZED, no reactivado. Antes de cualquier laboratorio que requiera esos cambios: presentar recursos/política/diff y reversión concretos y detenerse con HUMAN_ACTION_REQUIRED. No ampliar grants para lograr compatibilidad sin gate; no fallback S1 ni migración silenciosa.

[Contrato RC2](../08_S2_agent_domain_contract_RC2.md), [acceptance por variante](../research/R-013_S2_variant_acceptance_RC2.md), [comparativa y límites de evidencia](../research/R-013_S2_variants_comparison_2026-10-06.md). Q-051 está cerrada solo en dirección. El laboratorio mínimo ya está preparado y revisado: [S2B-ADM-01](../research/R-013_S2B_lab_ADM01.md), Q-052 READY_FOR_DECISION / NOT_AUTHORIZED. La siguiente prueba efectiva necesita ese permiso concreto. No implementación, gasto, main, autoridad financiera, Strategy V1 o freeze autorizado.

## Propuesta comparativa histórica — 2026-10-06, antes de confirmación

**S2: DECIDED solo dirección de frontera financiera técnica. Variante S2-B: READY_FOR_DECISION / propuesta revisada. D-027/D-024 RESEARCHING.** El propietario **no autoriza S2-ADM-01**, reabre la granularidad rol→cuenta y prefiere un Agent Runner único si satisface los contratos. No interpretar esta preferencia condicional como aceptación técnica o permiso administrativo.

Recomendación revisada: **S2-B — una identidad Windows estándar/restringida para AI Domain, core financiero fuera, contextos/permisos efectivos por job**. No está demostrada la necesidad de una cuenta por cada rol. El fallo adicional que S2-A puede impedir es lectura/alteración de recursos de un rol por otro cuando un proceso común puede saltar sus interfaces; B debe impedirlo con confinamiento efectivo del proceso completo y supervisor protegido. Workspaces/prompts/allowlists sin esa frontera no son suficientes.

Separar SECURITY ISOLATION (broker/secrets/DB/Execution/IPC/red/write) de EXPERIMENTAL BLINDING (snapshot mínimo predecisión, DAG, namespaces/cache y comparación posterior a seal). Blinding no obliga a una cuenta por rol. Windows ofrece restricted tokens/AppContainer; 10/10 checks AccessCheck en memoria muestran permisos diferentes con el mismo TokenUser. **No** demuestran compatibilidad Codex/auth ni acceso efectivo a recursos reales; SI/BL/RB siguen NOT_TESTED.

| Variante | Disposición vigente |
|---|---|
| S2-A cuentas por rol/dominio | Alternativa a reevaluar si se observa una limitación concreta de B; separación mínima por confianza/visibilidad, no por nombre de agente automáticamente |
| S2-B Agent Runner + contextos mínimos por job | **Recomendada como dirección candidata**, pendiente de aprobación de revisión, compatibilidad y acceptance |
| S3 VM | Reserva formal si S2 resulta insuficiente; VM común también requiere blinding, puentes mínimos y nueva decisión humana |

[Comparativa completa y fuentes](../research/R-013_S2_variants_comparison_2026-10-06.md), [contrato candidato RC2](../08_S2_agent_domain_contract_RC2.md), [acceptance RC2](../research/R-013_S2_variant_acceptance_RC2.md), [probe/evidencia](../research/probes/r013-s2-variants/README.md). Los antecedentes de 2026-10-05 siguientes se conservan para trazabilidad; su mapeo de cuentas y próximo gate no son el plan activo.

**S2-ADM-01 DEFERRED / NOT_AUTHORIZED.** Ningún usuario/perfil AppContainer, ACL/firewall/IPC/política/secret/credencial se configura. Próxima decisión humana: confirmar S2-B como dirección candidata revisada, sin autorizar setup. Después preparar una propuesta mínima de laboratorio concreta; no reactivar ADM-01 ni cambiar silenciosamente a S3. No cierre D-027/D-024, implementación, gasto, main, A+, G1+G2, ADR-006 o Strategy V1.

## Antecedentes conservados — 2026-10-05

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

## Decisión histórica del propietario — 2026-10-05 (objetivo S2 conservado)

El propietario aprueba **opción S2 como dirección candidata PAPER**, no como aislamiento ya demostrado. Identidades/procesos Windows separados por dominio de confianza, permisos mínimos efectivos y separación de filesystem, secretos, IPC y red. S3 VM dedicada permanece fallback formal sujeto a nueva decisión si S2 falla; S1 solo investigación/probes sin secretos, nunca fallback operativo PAPER.

Antes de cerrar D-027/D-024 deben probarse: inaccesibilidad de broker credentials y secretos core; ausencia de escritura de estados financieros; bloqueo directo de Execution/broker endpoints; ACL explícitas; control/IPC restringido; egress mínimo; allowlists/fail-closed; ausencia de permisos heredados de desarrollo; separación de workspaces/stores; exports mínimos versionados por job; negative tests entre dominios/namespaces y auditoría de rechazos. Crear usuarios distintos, prompts, AGENTS o `authority=NONE` no satisfacen el gate.

**Security isolation** y **experimental blinding de Shadow** son objetivos/gates separados. Shadow no recibe información contemporánea Champion fuera del snapshot pareado. Se especificarán criterios objetivos de insuficiencia S2 y reevaluación S3 antes de ejecutar acceptance.

Autorizado: especificación y pruebas no administrativas/destructivas con fixtures sintéticas. **No autorizado todavía:** crear usuarios, modificar ACL/firewall/políticas/credenciales, mover secretos o configurar privilegios. Primero preparar propuesta concreta revisable; detenerse con `HUMAN_ACTION_REQUIRED` al necesitar ese cambio. No solicitar otra aprobación de la dirección S2. No cierre D-027/D-024, implementación, gasto ni cambios a A+, G1+G2 o ADR-006.

## Contratos y siguiente acción administrativa histórica — 2026-10-05

2026-10-05: [S2 RC1](../08_S2_isolation_spec_RC1.md), [acceptance SI/BL/RB y escalamiento](../research/R-013_S2_acceptance_matrix_RC1.md), [hallazgos](../research/R-013_S2_findings_2026-10-05.md) y [S2-ADM-01](../research/R-013_S2_administrative_gate_ADM01.md). Preflight read-only + siete observaciones sintéticas completados; S2_SECURITY/SHADOW_BLINDING siguen NOT_TESTED. Configuración firewall efectiva requiere store/policy competente; no asumir reglas locales aplicadas. La próxima aprobación es únicamente laboratorio temporal de tres cuentas estándar y ACL en árbol nuevo, no dirección S2, permisos PAPER finales ni modificación de firewall.

## Laboratorio preparado después de aprobación de dirección — 2026-10-06

[S2B-ADM-01](../research/R-013_S2B_lab_ADM01.md), Q-052 **READY_FOR_DECISION / NOT_AUTHORIZED**, sustituye únicamente la próxima solicitud administrativa, no la decisión candidata S2-B. Una cuenta temporal estándar + árbol/ACL nuevos + pruebas FS confiables y reversión; no red/auth/administración global. [Hallazgos nuevos](../research/R-013_S2B_lab_preparation_2026-10-06.md) precisan grants comunes/tránsito y límites del harness. Q-051 DECIDED en dirección; D-027/D-024 abiertos. Viejo ADM-01 DEFERRED, pruebas reales NOT_TESTED.
