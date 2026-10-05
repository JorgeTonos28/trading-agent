# ADR-011 — dirección agéntica PAPER Team propuesta

2026-10-05. Estado **READY_FOR_DECISION**, aprobación pendiente del propietario. D-020 selección propuesta / D-024 dirección arquitectónica; **no cierre final de D-024 ni freeze**. ADR-010 ya aprobó Team PAPER, no esta elección de ejecución/permisos.

## Decisión exacta solicitada

Adoptar como dirección de diseño PAPER **núcleo financiero local determinístico + jobs Codex Team intermitentes**, con roles lógicos empaquetados en repo, transporte nativo oficial preferentemente Codex SDK, herramientas concretas de lectura de snapshots/trazas y admission externo. Incorporar las disposiciones propuestas de la shortlist RC2 como referencia para especificación del stack; no agregar un framework agéntico o un plugin operativo residente por defecto.

Esta decisión determina cómo se invocará el componente agéntico y dónde se establece la frontera con el núcleo financiero. AGENTS exige gobierno para arquitectura material de runtime/permisos; la cohorte aprobada previamente no aprobó esta dirección completa. No volver a pedir aprobación de aquella cohorte.

## Evidencia relevante

- Waves 04–06: comportamiento de research/quant/shadow/pedagogía, PIT/lineage/output/fallo, sin superioridad general demostrada de Skills; evaluador enmendado con resultados originales conservados.
- Wave 07: **8/8** jobs de carga acotada pasan (7 funcionales, 1 error/abstención); callbacks/Skills/structured output con SDK oficial, payloads normales >32 KiB, restart del contexto shadow y acciones/cantidades iguales con prosa variable.
- R-028 y completion SDK: fresh-clone native root/rol/Skills; no requerimiento de chat previo. El entorno objetivo PAPER es la ruta Team probada, sin gate Plus.
- Handler SDK default accept identificado; jobs exigen handler explícito fail-closed. Autoridad cero en outputs no sustituye aislamiento técnico.
- [Matriz RC2](../research/R-006_shortlist_RC2_team.md), [contrato candidato](../research/R-006_native_job_boundary_RC0.md), [wave 07](../research/R-006_probe_wave_07_2026-10-05.md) registran límites y pendientes.

## Alternativas

| Alternativa | Ventaja | Trade-off / evidencia | Recomendación |
|---|---|---|---|
| **A. Núcleo local + jobs nativos Team** | Separación determinística/LLM, pipeline automatizable sin factura API, snapshots y auditoría explícitos | Integrar caller/workflow/secret isolation; cuota compartida y dynamic tools experimental | **Preferida**, familia nativa probada; diseño material requiere dueño |
| B. Codex manual únicamente | Menor integración inicial, útil Plan Architect/research/pedagogía manual | No demuestra shadow oportuno en cada snapshot pertinente sin intervención; operación propuesta WL-R no validada con uso manual | Fallback de preparación; equivalencia autónoma PAPER no probada |
| C. LLM residente/multiagentes/plugin como orquestador financiero | Posible coordinación generativa richer | Sin valor incremental probado, más permisos/estado/cupo y complejidad; no puede asumir autoridad Champion/riesgo | REFERENCE_ONLY; no justificar como requisito de autonomía |
| D. Agents SDK/API facturada o runtime Anthropic | Posible control/continuidad mayor | Gasto separado, beneficios/costos no probados; fuera de ejecución paga PAPER por defecto ADR-008 | REFERENCE_ONLY PAPER, futuro LIVE con ficha/aprobación |

## Lo que la aprobación NO cerraría

- DoR, implementación, PAPER inmediato o LIVE; todos sus gates permanecen.
- Strategy V1, broker, datos/Smart Money, umbrales ni cambio A+/G1+G2/ADR-006.
- Versiones finales cliente/modelo, topología/concurrencia, scheduler/workflow/storage, aislamiento OS/secretos y totalidad de permisos D-027; config de plugin/MCP y método de deploy final.
- Capacidad sostenida, quota/auth lifecycle, todos los reportes/curriculum/evals y validación financiera real.
- Tampoco dispensa evidencia de capacidad/runtime exigible **antes del cierre final P1**. La distribución de TP por etapa debe revisarse al especificar el gate final; el burst de ocho jobs no permite darlo por aprobado.
- Compra/gasto, API billing, baseline main o deployment release/tag.

Después de aprobación, continuar especificación/probes de esos P1, revisar independientemente el paquete y cerrar D-024 solo con requisitos satisfechos. La selección de familia/roles para diseño no debe presentarse como freeze final de agentes/runtime/plugin. Si el dueño prefiere B/C, documentar cómo satisface shadow/pedagogía/carga y revisar comparativa; no bajar obligaciones silenciosamente.

## Gobierno y siguiente trabajo

**HUMAN_ACTION_REQUIRED:** aprobar A como dirección arquitectónica candidata para PAPER, o escoger una alternativa con su impacto. Propuesta técnica: A.

Tras esa decisión: D-024/R-010 junto a seguridad/workflow/storage por necesidad; siguiente P0 R-020/Strategy V1 y protocolo comparativo con Build-vs-Reuse continuo. R-029 Plus sigue DEFERRED P3. Este ADR no incorpora aprobación por silencio.
