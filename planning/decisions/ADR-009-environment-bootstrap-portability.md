# ADR-009 — Environment Bootstrap, Portability & Agent Packaging

**PARTIALLY SUPERSEDED — ADR-010 (2026-10-05):** el requisito de bootstrap/paquetes y la cohorte candidata siguen aprobados. Se sustituye únicamente Plus como target PAPER y gate previo: PAPER_RUNTIME_ENVIRONMENT=Team; Plus candidato PRE-LIVE R-029 P3. Contrato original conservado abajo; no espera de Plus para D-020/D-024/DoR/PAPER.

Fecha: 2026-10-05. Estado: **DECIDED — requisito aprobado por el propietario**. El mecanismo final D-037 está `RESEARCHING`; runtime/topología D-024 `OPEN`, stack D-020 `RESEARCHING`.

## Decisión del propietario

1. La shortlist RC1 es una **cohorte candidata aprobada para avanzar hacia Plus Acceptance**, no selección final ni aprobación implícita de todas sus alternativas arquitectónicas.
2. El repositorio debe ofrecer una ruta reproducible desde entorno nuevo + clone hasta entorno agéntico configurado y verificado: inventario, diferencias, acciones automáticas/manuales, acceptance gates, configuración permitida, preparación de roles, smoke y reporte.
3. D-024 no puede cerrarse sin esa ruta. Se incorpora al Definition of Ready; no requiere implementar Trading OS durante preparación.
4. Investigar Bootstrap Mode/Onboarding Agent y paquetes por rol con contratos compartidos. No seleccionar una sesión/proyecto Codex por agente ni un orquestador.
5. Separar Team de investigación, Plus individual objetivo y LIVE futuro. Entitlements, autenticación y servicios no viajan con Git. Los reportes no contienen secretos.

## Prioridad y alcance

**D-037 / R-028 = P1:** ruta concreta de preparación/despliegue bloquea implementación y cierre D-024; no reabre los invariantes financieros P0. Es prerrequisito explícito de la decisión arquitectónica dependiente, aunque su entrega técnica sea P1. La obligación ya está aprobada; empaquetado, mecanismos de configuración y evidencia suficiente siguen en investigación. Cambios materiales de seguridad/permisos se llevan a D-027/gobierno.

`TARGET_PLUS_ENVIRONMENT` es alias semántico de `TARGET_RUNTIME_ENVIRONMENT`, no una cuarta cuenta. `FUTURE_LIVE_ENVIRONMENT` permanece sin seleccionar y necesita gates LIVE separados.

## Requisitos de aceptación

- Entry point y procedimientos utilizables sin este chat; versiones/hashes/licencias/dependencias y rutas relativas al repo.
- Comprobar reglas globales + especialización de rol, Skills efectivamente descubiertas/activadas, plugins/apps/MCP instalados vs habilitados vs invocables, herramientas y límites conocidos.
- Perfil esperado distinto de perfil observado y reporte final. UNKNOWN/NOT_TESTED no pasan un requisito obligatorio; ausencia opcional se registra.
- Acciones `AUTOMATED / USER_ACTION_REQUIRED / UNAVAILABLE / OPTIONAL / FALLBACK_AVAILABLE`, con permisos, coste y efecto concretos; ninguna equivalencia silenciosa de fallback.
- Smoke y recovery repetibles; conservar evidencia Team reutilizable y ejecutar en Plus únicamente diferencias/entitlement/operación específicas. Reiniciar no borra fallos ni duplica admisiones.
- Readiness del entorno agéntico no habilita implementación, PAPER autónomo o LIVE.

## Impacto

Se añade un rol/modo lógico de onboarding, un manifiesto de paquetes y un gate de portabilidad. No añade un LLM always-on, autoridad financiera ni topología multiagente. La alternativa núcleo local determinístico + jobs Codex intermitentes sigue candidata. Los procedimientos de research/shadow/quant/pedagogía conservan sus contratos y gates previos.

## Paquete autónomo autorizado

1. Investigar descubrimiento nativo de instrucciones/Skills y límites de empaquetado.
2. Diseñar contratos/perfiles/paquetes y entry point de preparación.
3. Probes desechables de herencia/discovery/activación y simulación de diferencias/readiness/recovery sin credenciales ni configuración global.
4. Persistir evidencia, incorporar deltas a R-006/Plus Gate y sincronizar hitos.

Endpoint: entrega de diseño y evidencia independiente del entitlement, con siguientes acciones realmente dependientes de Plus o gobierno identificadas. No ejecutar Plus Gate en Team; continuar trabajo independiente antes de escalar un acceso pendiente.

## Enlaces

[Shortlist RC1](../research/R-006_shortlist_RC1.md), [Plus Acceptance Gate](../research/R-006_plus_runtime_gate_RC0.md), [invariantes PAPER](../paper_v1_capability_contract_RC1.md), [ADR-007](ADR-007-r006-openai-anthropic-plus-scope.md), [economía ADR-008](ADR-008-economic-policy-by-phase.md).
