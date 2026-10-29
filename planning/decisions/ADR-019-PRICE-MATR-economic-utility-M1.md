# ADR-019 — M1: utilidad económica ex ante PRICE–MATR

**Fecha:** 2026-10-14. **Estado:** DECIDED, aprobación acotada del propietario. Q-058 DECIDED; D-011 RESEARCHING, Strategy V1 OPEN. Complementa ADR-016/O-B, ADR-017/B y ADR-018/K2. No selección de métodos, datos, broker, capital, estrategia, backtest o implementación.

## Valores aprobados

| Objetivo de utilidad | Valor | Unidad/estimando |
|---|---|---|
| δ_NI | 0.01 | 1 punto porcentual de CAGR anual de inferioridad máxima frente a EW6-BH |
| ε_cash | +0.01 | 1 punto porcentual anual de exceso mínimo frente al efectivo, neto de costes incrementales correspondientes |
| ρ_ES | 0.20 | 20% de reducción material del ES frente al espejo K2 admisible |
| q_ES | 0.95 | ES diario: peor masa5% de retornos/pérdidas según estimando documentado; pérdida=-retorno, pesos fraccionales/ties sin clipping |

Son utilidades preregistradas por gobierno, **no un F0 completo ni prueba de demostrabilidad**. ES95 es medida primaria de reducción material propuesta/aprobada en utilidad; estimación e inferencia aún requieren validación.

## Siete condiciones

1. Separar utilidad de demostrabilidad. Cuatro años no garantizan evidencia; no adaptar margen a potencia. Conservar INSUFFICIENT_EVIDENCE o INCONCLUSIVE según motivo.
2. Completar/validar incertidumbre, dependencia/bloques/múltiples comparaciones, cola efectiva y ES antes de PASS. E4 14/14 no calibra estadística completa.
3. ES95 no sustituye DD, pérdidas acumuladas, recuperación, volatilidad, gaps o extremos. Guardrails definidos/preregistrados antes de resultados.
4. Escenarios previos de escala/costes: incremental versus asumido, fijo/variable, sin elegir capital favorable después. Costes/escala UNKNOWN impiden calificación económica operacional completa.
5. Espejo correspondiente K2, composición/beta/factores y límites defendibles. Menor exposición sola no demuestra eficiencia adicional.
6. NOT_EVALUATED, INVALID_DATA_OR_METHOD, INSUFFICIENT_EVIDENCE, INCONCLUSIVE y FAIL distintos. Falta de precisión no demuestra inferioridad económica.
7. NO_STRATEGY_QUALIFIED con razones si nadie cumple. Sin relajar márgenes, seleccionar/reparar con holdout o ganador obligatorio.

## Continuación y límites

[Q058 original](../research/D-011_economic_margins_proposal_RC0.md) conserva alternativas/fundamento; card/perfil especifican números con unidades y aprobación, manteniendo método/muestra/guardrails/source pendientes. Continuar asuntos técnicos en Team: protocolo, DataCards, fuentes/PIT, configuraciones PRICE–MATR y comparabilidad. No reabrir B/K2/M1 sin evidencia material nueva.

Reserva **INTEGRITY_UNKNOWN**, `implementation_locked=true`, **TARGET_ACCEPTANCE_DEFERRED**. No gasto, Plus/admin institucional, main/release, operación o autoridad financiera nueva.
