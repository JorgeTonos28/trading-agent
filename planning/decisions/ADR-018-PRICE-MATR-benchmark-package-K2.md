# ADR-018 — paquete K2 de benchmarks PRICE–MATR

**Fecha:** 2026-10-14. **Estado:** DECIDED, aprobación acotada del propietario. **Q-057:** DECIDED. D-008 OPEN, D-011 RESEARCHING. Complementa ADR-016/O-B y ADR-017/B; no selecciona Strategy V1, parámetros, datasets, broker, capital ni márgenes numéricos.

## Paquete aprobado

- **B-EW6-BH primario:** SPY, QQQ, IWM, EFA, TLT y GLD, pesos iniciales iguales y buy-and-hold con deriva natural. Política de dividendos, costes y contabilidad deberá definirse reproduciblemente.
- **B-CASH obligatorio:** referencia monetaria apropiada para exceso neto y coste de oportunidad. Fuente y modelo pendientes, separados del interés real de la cuenta.
- **B-EW6-BH-LAMBDA-REAL obligatorio:** comparación de exposición con ledger/cash/costes propios, para distinguir desinversión de eficiencia adicional.
- **Secundarios explícitos:** SPY buy-and-hold y SPY/SMA200. EW6 mensual sólo sensibilidad predefinida, nunca sustituto silencioso del buy-and-hold.

## Siete condiciones de aprobación

1. Exposición equivalente **no equivale a riesgo equivalente**. Evaluar composición, beta y factores relevantes; documentar limitaciones y no afirmar eficiencia cuando la comparación no sea defendible.
2. Mostrar cualquier diferencia económica importante frente a SPY, aunque no sea el gate primario. No ocultarla detrás del multiactivo.
3. Fijar pesos iniciales/deriva/dividendos/corporate actions/costes/calendario/efectivo/valoración. No rebalance mensual sin preregistro y gobierno pertinente.
4. Misma ventana admisible, información as-of, contabilidad y supuestos de ejecución. El benchmark tampoco conoce el futuro.
5. Cumplimiento conjunto de competitividad, exceso frente al efectivo, mejora material de riesgo y guardrails independientes; ningún score compensa automáticamente un gate incumplido.
6. Márgenes antes de resultados, precisión/suficiencia explícitas. Si no alcanza la muestra, INSUFFICIENT_EVIDENCE sin relajar criterios.
7. Sólo cohorte ETF PRICE–MATR inicialmente. Form4, Congreso y13F necesitarán benchmarks/admisión propios.

## Evidencia, pendientes y gobierno

[Propuesta Q057](../research/D-011_benchmark_qualification_decision_RC0.md) conserva K1/K2/K3 y review independiente. Se aprueba el paquete conceptual, no la implementación numérica de benchmarks, datos o inferencia. Continuar diseño reproducible, métricas/modelos/MethodApplicabilityCard, fuentes/PIT/rights, formulación de márgenes y evidencia antes de resultados relevantes. No volver a solicitar preferencias económicas Q056/Q057 decididas.

Reserva **PROPOSED_RESERVE / INTEGRITY_UNKNOWN**. `implementation_locked=true`, **TARGET_ACCEPTANCE_DEFERRED**. No implementación, gasto, acceso Plus, administración institucional, cambios main o autorización financiera adicional. Presentar próximo HUMAN_ACTION_REQUIRED sólo por decisión material nueva y fundamentada.
