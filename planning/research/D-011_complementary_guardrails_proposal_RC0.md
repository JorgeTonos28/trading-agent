# Q-059 — guardrails complementarias de calificación

**Vigencia 2026-10-15: Q-059/G-R1 DECIDED por [ADR-020](../decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md); G-R2 no aprobado. Este documento conserva la propuesta de 2026-10-14 y su comparación, no una decisión aún pendiente.**

2026-10-14, historial: READY_FOR_DECISION tras revisión independiente; propuesta entonces no aprobada. B/K2/M1 DECIDED y no se reabren. D011 queda abierto; utilidadES20% no aprueba tolerancia de drawdown/volatilidad. Guardrails económicos distintas de hardlimits RiskD031.

## Problema

Una candidata puede reducir ES95 promedio y empeorar drawdown/volatilidad u ocultar episodios largos de recuperación. Elegir cuánto deterioro admitir cambia el conjunto calificado y no es sólo una opción de librería. La evidencia estadística y de datos continúa siendo obligatoria; no optimizar tolerancias usando la muestra.

## G-R1 recomendado — no deterioro en los dos controles principales

1. **Drawdown máximo:** no deterioro frente a EW6-BH completo, ΔMDD=MDD(S_nettrading)-MDD(EW6-BH)≤0, con incertidumbre de path defendible y límite superior≤0. Comparar también espejo ySPY descriptivamente; no llamar0 a episodio censurado.
2. **Volatilidad diaria:** no deterioro frente a espejo K2 admisible, σ(S)-σ(M)≤0 con límite superior≤0; misma frecuencia/cash/fees/dependencia, sin√252 asumido. ES mantiene primario20% y95; no reemplazarlo porσ.
3. **Pérdidas acumuladas y recuperación:** reportes obligatorios por episodio/regímenes/underwater, censura final y salida; evitar recovery0 cuando no recuperó. Censura/incomparabilidad producen insuficiencia en el claim correspondiente, no ausencia de riesgo. No comparaciones automáticas de máximos de episodios con calendarios distintos.
4. **Gap/slippage y extremos:** stress de precios/ejecución previos, pérdida económica y estado de protección/cash/reservas visibles; pérdidas sin cota o modelo fiable bloquean admisión. Límites de pérdida operativos dependen del Riskbudget aprobado, no inventados aquí. Probar rangos de gap/intrabar/delay ex ante, sin usar mejortrayectoria; no garantía de stoploss máximo.

G-R1 agrega gatesDD/σ estrictos, no scorecompensatorio ni segunda reducción mínima20% no aprobada. Require incertidumbre válida/suficiencia: bound que cruza0=>INCONCLUSIVE/INSUFFICIENT según razón, no inferir inferioridad de un decimal ni igualdad probada por no significancia. Estos son nuevos controles de éxito económico; no liquidación automática o permiso financiero.

### Tipo y agregación por guardrail

| Control | Estimando/criterio propuesto | Agregación y alcance |
|---|---|---|
| DD | ΔMDD de paths del mismo horizonte y convención. Realizado observado es descriptivo exacto para ese período; un bound inferencial/predictivo necesita estimando y método de path explícitos/validados, no CI inventado para una sola trayectoria | Es gate cuantitativo nuevo; criterio G-R1 upper≤0. Modelo/estimando no aceptado=>NOT_EVALUATED; precisión insuficiente=>INSUFFICIENT/INCONCLUSIVE; no calificación global antes de su admisión. Observación histórica no prueba reducción futura |
| σ diario | σ(S)-σ(M), mismo retorno net_trading/fecha, población/horizonte/modelo declarado | Gate cuantitativo; G-R1 upper≤0, estados de evidencia como DD. No convertir ausencia de significancia en equivalencia |
| Recovery/underwater/pérdidas | Duración/episodios y censura del mismo calendario, lowerbound si sigue sin recuperar, pérdidas/recuperación observadas | **Reporte obligatorio**, no gate numérico adicional oculto. Censura legítima permite reporte completo con cota y bloquea claim de duración exacta/mejora, no automáticamente los gatesDD/σ/ES. Reporte ausente/inválido bloquea cierre de evaluación. Gobierno Strategy final debe considerar deterioros/riesgos visibles |
| Gap/slippage/extremos | Escenarios/fills/estado/cash/reservas previos con modelo admitido; consecuencias cuantificadas y límites no observados visibles | **Admisibilidad de modelo + reporte obligatorio**; falta de modelo defendible=>INVALID/NOT_EVALUATED, no PASS económico global. Sin umbral económico nuevo oculto; límites RiskD031 pendientes bloquean aceptación operacional/DoR en su scope, no se inventan aquí |

En RC5, «guardrails pasados» significa gates cuantitativos definidos y válidos más completitud/admisibilidad de reportes; no exigir un PASS estadístico ficticio a una duración censurada. Estrategia no se promociona automáticamente por calificación limitada. Q059 no define aún modelo DD, duración exacta futura o hardlimit financiero.

## Alternativa G-R2 y trade-off

G-R2 permitiría deterioro predefinido hasta **+1pp de MDD frente a EW6-BH** y **+5% de σ frente al espejo**, manteniendo ES20% y demás reportes/gates. Evita que una diferencia pequeña con incertidumbre bloquee utilidad de cola, pero acepta otra pérdida/riesgo que M1 no autorizó. No asumirla por «materialidad» ni ampliarla por baja potencia.

Fórmulas G-R2: upperbound[ΔMDD]≤0.01 y upperbound[σ(S)-1.05σ(M)]≤0, referencia/modelo positivos/admisibles y mismos estados. No usar ratios inestimables ni adoptar G-R2 automáticamente si G-R1 no pasa.

Recomiendo G-R1 por coherencia conservadora con pagar una pequeña inferioridad de retorno por mejorar riesgo; no evidencia de qué candidata lo supera. G-R2 es tolerancia nueva que debe elegir el propietario si la considera aceptable. Números de sensibilidad no son parámetros de Risk Engine ni escogidos por resultados.

## Decisión exacta y alcance

¿Adoptar **G-R1** como contrato complementario de calificación, o tolerar G-R2? No aprobación de método/α/power/datos/Strategy/capital. [RC5](R-020_evaluation_contract_RC5.md) preserva MVgates y [E5](R-020_E5_findings_2026-10-14.md) sólo screening; no fullstatisticalvalidation nialpha. Tras elección se valida calibración de los endpoints/guardrails definitivos y se congela F0 cuando dataset/config/evidencia permiten; no benchmark/margen readaptados.
