# Build vs. Reuse — marco de decisión inicial

Estado 2026-10-01: **R-006 es P0 y foco inmediato**; D-024 queda abierto hasta el Agent Capability Gate. El inventario de familias y candidatos está en [capability_landscape.md](capability_landscape.md) y [fichas/probes R-006](research/R-006_initial_findings_2026-10-01.md). La mayoría de disposiciones siguen `PENDING`; [cookbook multiagente de portfolio](https://developers.openai.com/cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration) se clasifica `REFERENCE_ONLY` porque su propia página está archivada y no satisface A+/shadow como contrato operativo.

## Disposiciones permitidas

| Disposición | Significado operativo |
|---|---|
| REUSE_AS_IS | Usar sin modificación funcional tras licencia, permisos y pruebas |
| ADAPT | Modificar una pieza reutilizable para nuestros contratos |
| PORT | Trasladar procedimiento/código a otro runtime respetando licencia |
| WRAP | Integrar una API/componente tras interfaz propia y límites de permiso |
| REFERENCE_ONLY | Aprender del diseño; no incorporar artefacto ni dependencia |
| BUILD | Construir porque alternativas fallan requisitos medibles |
| REJECT | Excluir por seguridad, licencia, fiabilidad, coste o desajuste |

## Criterios de comparación

1. Seguridad y autoridad financiera: un componente generativo no puede aprobar riesgo ni enviar orden irrestricta.
2. Fidelidad al contrato funcional, PIT, reproducibilidad y auditabilidad.
3. Disponibilidad real para cuenta, región, producto y entorno PAPER.
4. Licencia, portabilidad, datos enviados, privacidad y mantenimiento.
5. Coste total: licencia, datos, integración, operaciones y salida.
6. Reversibilidad y capacidad de prueba independiente.

Una capacidad puede existir y ser técnicamente compatible, pero no estar disponible para nosotros o no ser económicamente razonable. `SELECTED` exige evidencia y decisión registrada. Un `BUILD` para componente mayor requiere comparación con alternativas y justificación explícita; el Risk Engine determinístico es una **intención arquitectónica de control propio**, pero incluso ahí se investigarán librerías de apoyo sin delegar autoridad.

## Primera cola de clasificación

OpenAI Skills/Plugins/Codex/MCP/Agents/análisis financiero; Anthropic Financial Services y Skills/templates/connectors/workflows; otros AI Labs; open source; runtimes de agentes/workflow; motores quant; broker APIs; market-data y alternative-data providers; almacenamiento/seguridad/observabilidad. Las fichas R-006 separan `EXISTS`, `AVAILABLE_TO_US`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE` y `SELECTED`. `PENDING` no equivale a clasificación final; cada disposición final tendrá evidencia y ADR cuando proceda.
