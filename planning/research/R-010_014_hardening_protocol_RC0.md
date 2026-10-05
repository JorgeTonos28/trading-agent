# R-010–014 — paquete autónomo de hardening PAPER RC0

2026-10-05. Preregistro después de ADR-011 A. Documentación y experimentos desechables; `implementation_locked=true`. D-024 no se congela. CURRENT_RESEARCH_ENVIRONMENT y PAPER_RUNTIME_ENVIRONMENT = Team; Plus solo PRE-LIVE.

## Preguntas y endpoint

¿Cómo ejecutar automáticamente jobs nativos sin exponer el núcleo financiero, reconstruirlos tras fallos y medir su suficiencia? Entregables: threat model/permisos y alternativas de aislamiento; contrato workflow/recovery; storage/audit/versiones/deploy; criterios de carga; probes y revisión crítica independiente. Resolver hallazgos documentales sin cambiar decisiones aprobadas. Endpoint de gobierno esperado: elegir frontera material de seguridad D-027; no pedir otra vez ADR-011.

## Probes preregistrados

| ID | Experimento | Aceptación / límite |
|---|---|---|
| H1 | Ledger SQLite temporal con subprocess terminada antes/después de commit, relectura y backup/restore | No registro parcial antes del commit; registro confirmado sobrevive terminación del proceso. No prueba power loss, PostgreSQL ni runtime productivo |
| H2 | Duplicados, lease/fencing, deadline, no-output, permisos del tool y hashes en fixtures | Un output admisible máximo por job lógico, intentos históricos preservados; intento vencido rechazado; deadline del caller; no-output ≠ HOLD; ninguna interfaz financiera. No prueba ACL/red real |
| H3 | Simular llegadas WL-R y burst utilizando latencias medidas wave07 | 100% accounting; separar espera/servicio/total. Sensibilidad explícita; no inferir cuota o aceptación sostenida de una simulación |
| H4 | SDK publicado y CLI emparejado: metadata/hash y preflight oficial | Versiones, modelo/proveedor/login y outputs/Skills/tools sobre ruta pinada si ejecutable disponible. No cambiar instalación/global config, copiar auth ni facturar API. Conservar intento fallido |
| H5 | Inventario local solo metadata | Presencia binarios ≠ servicio instalado/configurado/listo. Sin habilitar WSL, VM, firewall, cuentas ni elevar permisos |

SQLite es instrumento de prueba independiente, **no selección de D-026**. No construir worker/scheduler financiero ni broker adapter. Fixtures, reloj virtual y permisos simulados se identifican como tales. Números de carga/deadlines/retries son experimentales, no límites aprobados. Nuevos resultados se evalúan contra este protocolo; toda enmienda posterior se registra.

## Revisión y siguiente P0

Revisor independiente solicitado por propietario: leer contratos, resultados y ADR; buscar autoridad oculta, defaults inseguros, claims no probados, recuperación ambigua, dependencia de chat y circularidad de gates. No puede seleccionar arquitectura/aprobar riesgo. Avanzar en paralelo documental el preregistro R-020/D-008 sin inventar entrada de VID-TS ni seleccionar estrategia/datos. Evidencia de resultado de trading no pertenece a este paquete.

## Extensión preregistrada H6 — motor reusable, antes de ejecutar

Temporal es candidato del roadmap. Probar CLI oficial standalone en workspace temporal, sin instalación global/service/cloud/credenciales. Development server headless loopback, store SQLite temporal persistido; iniciar un workflow sintético **sin worker ni tools/modelos**; repetir ID para comprobar rechazo de duplicado; terminar proceso y reiniciar mismo store; confirmar run/history/status conservados. Si factible, schedule automático dispara workflow sintético y sobrevive restart. No probar órdenes ni efectos externos. Conservar fallos/errores sanitizados, versión/hash/licencia y stop/cleanup de PID propio. Este ensayo no valida Temporal production ni ejecuta jobs Codex desde scheduler: prueba pequeña de persistencia del motor antes de seleccionarlo. [CLI server](https://docs.temporal.io/cli/command-reference/server).

Revisión H3: fuente/result v1 permanecen; v2 aclara que son 50 jobs + 13 cargas abstractas = 63 **service requests**, no 63 éxitos funcionales ni retries reales. Próximo gate de carga exige parent job/deadline original en reintentos. H2 adicional responde a expiry/concurrencia; restore epoch fixture es semántica (policy assignment identificado), no prueba store real.
