# ADR-000 — Reabrir la selección de Strategy V1

- **Fecha:** 2026-10-01
- **Estado:** DECIDED (alcance del proceso); la selección de Strategy V1 permanece OPEN
- **Aprobador:** propietario del proyecto, instrucción explícita en conversación el 2026-10-01
- **Afecta:** D-006 (SUPERSEDED), D-008/D-009 (nuevas), D-010/011, R-001/R-019/R-020, roadmap v0.2

## Contexto

La hoja v0.2 presentó MATR_V1 como primer Champion experimental y secuencia concreta de desarrollo. El propietario aclaró que MATR_V1 se introdujo por sencillez e interpretabilidad, pero nunca se seleccionó como primera estrategia. La motivación original fue [este video](https://www.youtube.com/watch?v=2Et4Ao6usbA), cuyo enfoque aún debe reconstruirse. El propietario confirmó que nadie del proyecto ha ejecutado ni visto backtests históricos de MATR_V1 en ningún período.

## Decisión de gobierno

1. `Strategy V1 Selection — OPEN`, P0. Ninguna estrategia ocupa todavía el lugar de primera estrategia de implementación.
2. Evaluar como mínimo una **Video-Inspired Strategy V1** reconstruida del material primario, MATR_V1 como candidato/benchmark alternativo, y otras estrategias que la investigación justifique.
3. Separar infraestructura/agent workflow de señales, gestión de posición/riesgo, copy trading, opciones y pedagogía antes de definir una estrategia testeable. No ensamblar componentes del video por proximidad narrativa.
4. Mantener intacto el invariante `TradeIntent → Risk Engine determinístico → Execution Engine → Broker` y los gates PAPER/LIVE.
5. La elección final de arquitectura de estrategia requerirá un paquete comparativo con criterios preregistrados y aprobación explícita del propietario.

## Evidencia y límites

La confirmación de no haber consultado backtests de MATR_V1 procede del propietario y queda registrada como declaración de alcance del proyecto. No prueba que los datos o el período 2023–2026 sean intrínsecamente limpios para **cualquier** estrategia o que una selección entre candidatos no contamine el holdout; la política OOS sigue abierta. Los capítulos públicos del video identifican temas, pero no fórmulas completas ni parámetros de entrada/salida. No se infiere rentabilidad de afirmaciones promocionales.

## Consecuencias

`02_MATR_V1_spec.md` permanece como ficha de candidato, no como contrato de implementación. Se abre investigación del video y comparación de candidatos antes de seleccionar datos, backtest engine u orden de implementación dependientes de la estrategia. Los nombres de ejemplos MATR en el roadmap se vuelven condicionales mediante enmienda documentada.
