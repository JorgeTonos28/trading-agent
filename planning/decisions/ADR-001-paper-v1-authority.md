# ADR-001 — A+ / Shadow Portfolio Manager en PAPER V1

- **Fecha:** 2026-10-01
- **Estado:** `DECIDED`; aprobación explícita del propietario el 2026-10-01
- **Prioridad:** P0
- **Decisiones afectadas:** D-015, D-016, D-019; depende de D-012/013/014/017
- **Documento de soporte:** [contrato PAPER V1 RC1](../paper_v1_capability_contract_RC1.md)
- **Baseline:** [hoja v0.2 §4–9, §55–57](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md)

## Problema

La hoja define el invariante `TradeIntent → Risk Engine determinístico → Execution Engine → Broker` y asigna al Portfolio Manager Agent la coordinación de cartera y la decisión de prioridades dentro de un presupuesto autorizado (§8.1). Para PAPER V1, un único Champion hace innecesaria al principio la priorización entre estrategias; permitir a un LLM ajustar prioridad o notional operativo exige más contratos, pruebas y observabilidad. La hoja también ubica agentes/pedagogía completos en B5, pero exige un informe pedagógico para el Definition of Done final de PAPER V1 (§57), y pide Regime Detection observador desde temprano sin exigirlo para la primera orden (§8.6).

## Alternativas

| Opción | Autoridad y alcance | Beneficio | Coste/riesgo |
|---|---|---|---|
| A — propuesta original | Un Champion; Signal e intent assembly determinísticos; Portfolio Manager Agent asesor conceptual, sin cambiar intent operativo | Frontera financiera simple | No produce evidencia estructurada del valor incremental del Portfolio Manager Agent |
| **A+ — aprobada** | A más Portfolio Manager Agent en **shadow mode**, con propuestas estructuradas auditables y comparación hipotética | Mantiene frontera determinística y genera evidencia para posible evolución futura | Exige aislamiento estricto, evaluación PIT y medición de divergencias |
| B — lectura amplia del baseline | Portfolio Manager Agent decide prioridad/notional dentro de límites; Risk valida cada intent | Mayor flexibilidad para múltiples señales/estrategias | Más superficie de autoridad, conflictos y pruebas desde V1 |
| C — flujo del video | Agente usa CLI/API broker directamente y modifica stops/automations por conversación | Demo rápida | Incompatible con el invariante D-002 y el gobierno de la hoja; requeriría cambio explícito del invariante |

## Decisión aprobada

El propietario aprueba **A+** solo para PAPER V1. Habrá una única **configuración/estrategia Champion operativa aprobada** al inicio; esa estrategia puede consumir varias fuentes o familias de señales. Signal e intent assembly que pueden llegar a Risk Engine serán determinísticos. Risk Engine conserva la única autoridad financiera para aprobar, reducir o rechazar intents; Execution/Broker solo reciben autorización válida. No hay aprobación humana por cada operación Champion dentro de límites aprobados.

Portfolio Manager Agent no queda pasivo: correrá en **shadow mode** cuando corresponda, con el mismo contexto elegible para la decisión de cartera y producirá `ShadowPortfolioProposal` versionada: aperturas/cierres hipotéticos, prioridad, notional/sizing, señales, razonamiento estructurado, confianza cuando proceda, fuentes/snapshot y timestamps. Estas propuestas se registran y auditan, pero **no pueden transformarse en `TradeIntent` operativo, llegar a Execution, modificar posiciones, Champion, política de riesgo o asignaciones**. Research Agents, Smart Money, Challengers y Pedagogical Agent tampoco tienen autoridad directa de órdenes.

Es una **restricción temporal documentada** de la facultad operativa del Portfolio Manager Agent descrita en §8.1, no una eliminación de su papel. Una evolución futura de `SHADOW/ADVISORY` a autoridad limitada similar a B requerirá evidencia comparativa, nueva decisión y aprobación humana. Risk Engine, Execution y broker mantienen sus fronteras originales.

PAPER V1 se considerará funcional solo cuando, además de autonomía paper controlada, exista aislamiento de Challengers y reporte pedagógico trazable conforme a §4 y §57. Pedagogical Agent producirá explicación factual desde B4 y cumplirá el contrato completo antes del DoD. La primera orden paper de B3/B4 no equivale al DoD final. Regime Detection tendrá contrato/observación tempranos y no alterará Champion.

## Evidencia y Build vs. Reuse

- La [hoja §8.1](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md) es fuente normativa de la responsabilidad original del Portfolio Manager Agent; §7 y §5 son fuente del invariante y aprobación humana.
- [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) ofrece orquestación, tools y tracing, pero la aplicación conserva deployment, estado y decisiones de aprobación. [Guardrails/human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) no protegen automáticamente todas las llamadas en una cadena; por ello el control financiero se ubica en el gateway determinístico. Esto justifica la **frontera funcional**, no selecciona SDK ni decide construir un runtime.
- Skills, Plugins, MCP, backtest frameworks y APIs existentes permanecen en R-006 antes de decidir `BUILD` para cualquier capacidad mayor. El contrato RC1 §7 registra opciones reutilizables; ninguna disposición final ni proveedor queda seleccionado.

## Especificación de detalle durante preparación — 2026-10-05

[Contrato común RC0](../06_agent_evidence_contract_RC0.md), [PM shadow RC0](../06_shadow_portfolio_contract_RC0.md) y [Pedagogical RC0](../06_pedagogical_contract_RC0.md) detallan evidence/caller, snapshots ciegos pareados, target quantity/derivaciones, failure/late/no-output, comparación de decisión vs trayectoria contrafactual y formatos/curriculum completo. Mantienen esta decisión aprobada; especificaciones propuestas no seleccionan runtime, aprueban seguridad material ni convierten probes sintéticos en DoD. R-026/D-034 RESEARCHING; D-029/025/026/027 y validación PAPER conservan gates.

## Evaluación shadow exigida

Comparar Champion determinístico y propuestas del Portfolio Manager Agent en decisiones coincidentes/divergentes, riesgo propuesto, rendimiento hipotético **con datos point-in-time y costes**, estabilidad, reproducibilidad, errores y utilidad incremental. El shadow no se puntúa con información posterior al momento de la propuesta. No existe promoción automática por buen resultado.

Esta aprobación cierra solo el **alcance y las fronteras de autoridad** D-015/016/019. No selecciona Strategy V1, broker, market/Smart Money data provider, runtime ni umbrales de riesgo; tampoco aprueba una política de liquidación o LIVE.

## Consecuencias y estado

ADR-001 queda `DECIDED`; D-015/016/019 se cierran en el alcance funcional aprobado. La [frontera de incidentes D-017](ADR-002-paper-v1-incident-autonomy.md) fue aprobada después y no concede autoridad de orden al shadow. `implementation_locked=true` y la hoja v0.2 se conserva como baseline con estas decisiones documentadas. La promoción de autoridad del Portfolio Manager Agent exige nuevo ADR y gobierno humano; los umbrales cuantitativos para considerar esa promoción permanecen investigación posterior.
