# ADR-001 — Alcance y autoridad operativa de PAPER V1

- **Fecha:** 2026-10-01
- **Estado:** `READY_FOR_DECISION`; **propuesta sin aprobación del propietario**
- **Prioridad:** P0
- **Decisiones afectadas:** D-015, D-016, D-019; depende de D-012/013/014/017
- **Documento de soporte:** [contrato PAPER V1 RC0](../paper_v1_capability_contract_RC0.md)
- **Baseline:** [hoja v0.2 §4–9, §55–57](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md)

## Problema

La hoja define el invariante `TradeIntent → Risk Engine determinístico → Execution Engine → Broker` y asigna al Portfolio Manager Agent la coordinación de cartera y la decisión de prioridades dentro de un presupuesto autorizado (§8.1). Para PAPER V1, un único Champion hace innecesaria al principio la priorización entre estrategias; permitir a un LLM ajustar prioridad o notional operativo exige más contratos, pruebas y observabilidad. La hoja también ubica agentes/pedagogía completos en B5, pero exige un informe pedagógico para el Definition of Done final de PAPER V1 (§57), y pide Regime Detection observador desde temprano sin exigirlo para la primera orden (§8.6).

## Alternativas

| Opción | Autoridad y alcance | Beneficio | Coste/riesgo |
|---|---|---|---|
| **A — recomendada** | Un Champion; Signal e intent assembly determinísticos; Portfolio Manager Agent asesora, sin cambiar intent operativo; research/Smart Money de solo lectura salvo señal aprobada por Strategy V1; explicación factual B4 y completa antes del DoD | Reduce no determinismo y simplifica la prueba de riesgo e idempotencia; preserva expansión posterior | Restringe temporalmente una responsabilidad del Portfolio Manager Agent descrita en §8.1 |
| B — lectura amplia del baseline | Portfolio Manager Agent decide prioridad/notional dentro de límites; Risk valida cada intent | Mayor flexibilidad para múltiples señales/estrategias | Más superficie de autoridad, conflictos y pruebas desde V1 |
| C — flujo del video | Agente usa CLI/API broker directamente y modifica stops/automations por conversación | Demo rápida | Incompatible con el invariante D-002 y el gobierno de la hoja; requeriría cambio explícito del invariante |

## Recomendación y cambio propuesto

**Proponer A solo para PAPER V1.** Es una **restricción temporal documentada** de la facultad operativa de Portfolio Manager Agent en §8.1, no una reinterpretación silenciosa ni un cambio ya adoptado. El agente podrá leer, explicar conflictos y proponer planes; un ensamblador determinístico emitirá `TradeIntent` del único Champion. En futuras versiones, la opción B puede reabrirse mediante ADR, pruebas y aprobación de límites de autonomía. Risk Engine, Execution y broker mantienen sus fronteras originales.

PAPER V1 se considerará funcional solo cuando, además de autonomía paper controlada, exista aislamiento de Challengers y reporte pedagógico trazable conforme a §4 y §57. La primera orden paper de B3/B4 no equivale al DoD final. Regime Detection tendrá contrato/observación tempranos y no alterará Champion.

## Evidencia y Build vs. Reuse

- La [hoja §8.1](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md) es fuente normativa de la responsabilidad original del Portfolio Manager Agent; §7 y §5 son fuente del invariante y aprobación humana.
- [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents/sdk) ofrece orquestación, tools y tracing, pero la aplicación conserva deployment, estado y decisiones de aprobación. [Guardrails/human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) no protegen automáticamente todas las llamadas en una cadena; por ello el control financiero se ubica en el gateway determinístico. Esto justifica la **frontera funcional**, no selecciona SDK ni decide construir un runtime.
- Skills, Plugins, MCP, backtest frameworks y APIs existentes permanecen en R-006 antes de decidir `BUILD` para cualquier capacidad mayor. El contrato RC0 §7 registra opciones reutilizables; ninguna disposición final ni proveedor queda seleccionado.

## Decisión exacta solicitada

¿Aprueba el propietario la **opción A para PAPER V1**, incluyendo:

1. un único Champion operativo inicial;
2. Signal e intent assembly determinísticos, con Portfolio Manager Agent asesor en vez de decisor operativo;
3. Research/Challenger/Smart Money/Pedagogical sin acceso directo a broker ni autopromoción;
4. explicación factual mínima en B4, informe pedagógico completo y aislamiento Challenger antes del DoD final;
5. Regime Detection observador temprano, sin autoridad sobre Champion?

Una aprobación cierra solo el **alcance y las fronteras de autoridad** D-015/016/019. No aprueba Strategy V1, broker, fuente de datos, parámetros de riesgo, autonomía de liquidación, live ni tecnología. Si el propietario elige B o modifica A, se revisan contrato RC0, matriz de permisos, fases y registros antes de cerrar el ADR.

## Consecuencias y estado

Hasta recibir decisión: ADR-001 sigue propuesto; D-015/016/019 permanecen `READY_FOR_DECISION`; `implementation_locked=true`. La hoja v0.2 no se modifica por esta propuesta. La evidencia futura que podría reabrir A es una necesidad demostrada de priorización multi-estrategia en PAPER V1 con control, reproducibilidad y evaluación suficientes.
