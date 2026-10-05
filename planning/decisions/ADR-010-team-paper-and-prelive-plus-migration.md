# ADR-010 — Team para preparación/PAPER; Plus candidato PRE-LIVE

Fecha: 2026-10-05. Estado: **DECIDED**, instrucción explícita del propietario. D-038 P0. **Supersede parcialmente** las cláusulas de entorno objetivo PAPER y dependencia Plus de ADR-007/ADR-009; conserva alcance OpenAI/Anthropic, economía ADR-008, portabilidad y todas las pruebas originales.

## Decisión

| Identificador | Entorno / fase |
|---|---|
| CURRENT_RESEARCH_ENVIRONMENT | Team actual, investigación y Preparation Program |
| PAPER_RUNTIME_ENVIRONMENT | Team actual, futura implementación inicial, backtests y PAPER V1 |
| FUTURE_LIVE_ENVIRONMENT | ChatGPT Plus individual, **candidato** para migración antes de LIVE |

El entorno Team actual también es el objetivo PAPER; las pruebas válidas allí son evidencia aplicable de disponibilidad/comportamiento en esa ruta. No equivalen a fiabilidad sostenida, a todas las herramientas/superficies Team, ni a seguridad financiera completa. Plus permanece desconocido donde no hay prueba específica.

El antiguo `TARGET_RUNTIME_ENVIRONMENT = Plus` y el alias `TARGET_PLUS_ENVIRONMENT` para PAPER quedan **SUPERSEDED**. En artefactos actuales usar PAPER_RUNTIME_ENVIRONMENT; el identificador legacy solo explica evidencia histórica. No transferir automáticamente resultados entre instancias/superficies ni hacia Plus.

## Gates y trazabilidad

- Plus Acceptance Gate queda **reclasificado P3 PRE-LIVE**: [R-029 Pre-Live Environment Migration & Acceptance](../research/R-029_pre_live_environment_migration_gate_RC0.md), D-039 DEFERRED. No bloquea R-006/D-020/D-024, implementación, backtest ni PAPER Team.
- PAPER conserva aceptación **Team** de capacidades/runtime. [Gate Team](../research/R-006_team_runtime_acceptance_RC0.md) distingue evidence suficiente para decisión arquitectónica, DoR y acceptance operacional previa a PAPER. No eliminar requisitos por mover el target.
- La distribución detallada P1/P2 de pruebas es una propuesta para especificar, no una dispensa de suficiencia/runtime aprobada por esta corrección. D-024 final necesita sus criterios/evidencia completos y gobierno; un probe acotado solo habilita presentar una dirección candidata.
- ADR-009/D-037/R-028 siguen vigentes: fresh-clone bootstrap Team, paquetes, configuración/restauración desde repo y ausencia de dependencia del chat. Team→Plus se prueba posteriormente PRE-LIVE.
- Estudios/probes/results previos se preservan. Documentos históricos se marcan explícitamente; los contratos/registros/perfiles operativos actuales se actualizan. No reinterpretar un fixture Plus sintético como prueba real.
- Mantener el desarrollo bloqueado hasta DoR/freeze. Esta decisión no autoriza implementación anticipada, PAPER inmediato, LIVE, gasto, Strategy V1/broker/datos/umbral financiero ni selección final de runtime.

## Deployment Source Policy

`plan-architect` = trabajo de preparación/candidato. `main` = baseline estable aprobado. **Release/tag versionado e inmutable** = snapshot reproducible para despliegue tras checkpoint/aprobación, con commit, manifest y evidencia/gates asociados. Un clone de commit candidato sirve para probes, no es una release aprobada. No merge a main ni creación/promoción de release de despliegue en esta ejecución.

## Impacto económico

Tier 0 PAPER = capacidades ya incluidas en Team actual y assets gratuitos; no presupuestar otra suscripción ni API facturada por compartir proveedor. LIVE Plus es candidato y se evaluará por calidad/operación/economía unitaria ADR-008; no una compra/migración aprobada. Skills/templates siguen gratuitos/incluidos/propios.

## Siguiente paquete autónomo R-006

Reevaluar evidence Team existente sin repetir corpus completo; investigar/probar gaps prioritarios del transporte oficial (Skills/tools/read-only context), recovery sin chat, carga representativa acotada, fallos y trazabilidad. Construir matriz requisito→evidencia→etapa/gap y propuesta revisable de arquitectura PAPER. Límite: autoridad/seguridad material y runtime/topología finales necesitan gobierno humano; no cerrar D-020/D-024 por cambiar el nombre del entorno.
