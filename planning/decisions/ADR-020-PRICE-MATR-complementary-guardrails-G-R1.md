# ADR-020 — G-R1: guardrails económicas complementarias PRICE–MATR

**Fecha:** 2026-10-15. **Estado:** DECIDED, aprobación explícita y acotada del propietario de Q-059/G-R1. Complementa ADR-016/017/018/019. D-011 permanece RESEARCHING; Strategy V1 OPEN.

## Contrato aprobado

- Drawdown máximo: no deterioro frente a B-EW6-BH completo, con convenciones comparables y método estadístico válido.
- Volatilidad diaria: no deterioro frente a B-EW6-BH-LAMBDA-REAL admisible. Su variabilidad incluye movimientos favorables y adversos; no reemplaza pérdidas extremas/acumuladas.
- ES95 diario conserva el objetivo primario M1 de reducción del 20%; NI y cash mantienen sus márgenes y el paquete K2. Todos los endpoints exigibles se cumplen conjuntamente, sin compensación por score.
- Reportes obligatorios de recuperación, underwater, pérdidas acumuladas, gaps, slippage y extremos; censura explícita, nunca duración cero por ausencia de recuperación. La tabla de tipos de Q-059 distingue gates cuantitativos de reportes/modelos admisibles.

## Condiciones vinculantes

1. Preferencia económica ex ante, no demostrabilidad: una trayectoria histórica o bootstrap genérico no prueban ausencia de deterioro futuro de DD.
2. DD requiere estimando, horizonte, tratamiento de trayectorias e incertidumbre explícitos y aplicabilidad validada antes de PASS. No fabricar intervalos ni confundir no significancia con equivalencia. Muestra insuficiente conserva su estado.
3. Volatilidad es guardrail complementaria; preservar ES, pérdidas acumuladas y riesgos de path.
4. Guardrails relativas no son límites absolutos del Risk Engine. DD igual al benchmark puede ser operacionalmente inaceptable; D-031 requiere definición/aprobación independiente.
5. G-R2 sigue alternativa NO APROBADA, sin fallback automático. Imposibilidad metodológica material requiere evidencia y propuesta gobernada antes de resultados relevantes; no adaptar tolerancias por potencia.
6. Cumplimiento conjunto de M1/K2/G-R1; ES no compensa deterioro DD/vol no autorizado.
7. NOT_EVALUATED, INVALID_DATA_OR_METHOD, INSUFFICIENT_EVIDENCE, INCONCLUSIVE, FAIL y PASS conservan significados; NO_STRATEGY_QUALIFIED es resultado válido, sin ganador forzoso ni holdout de reparación.

## Alcance y continuación

Aprueba criterios económicos, **no métodos estadísticos**, α, cobertura/potencia, datos/derechos/PIT, configuración financiera, broker, capital, Strategy V1, Risk limits, F0 o implementación. [Propuesta histórica](../research/D-011_complementary_guardrails_proposal_RC0.md) conserva alternativas y su revisión. Los límites superiores ≤0 sólo admiten PASS con estimando/método válidos; ausencia de precisión no es FAIL por defecto.

Continuar configuraciones, fuentes/PIT/rights, semántica broker, backtesting/paridad, factibilidad estadística, riesgo y preregistro en checkpoints materiales. No solicitar aprobación por cada parámetro menor justificado. No validar estadística desde E4/E5/E6 sintéticos.

Reserva INTEGRITY_UNKNOWN; implementation_locked=true; TARGET_ACCEPTANCE_DEFERRED. Sin cambios administrativos, gasto, Plus, main/release o autoridad financiera nueva.
