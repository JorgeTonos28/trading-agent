# ADR-022 — DD-E condicionado como interpretación inferencial de G-R1

- Estado: **DECIDED**, aprobado expresamente por el propietario.
- Fecha de registro: 2026-10-23.
- Pregunta: Q-061; decisión padre D-011 permanece RESEARCHING.
- Alcance: cohorte ETF PRICE–MATR; interpretación del criterio G-R1 de ADR-020, sin cambiar sus márgenes.

## Decisión

Se adopta `θ_D(H;P,I0)=E_P[MDD_H(S)−MDD_H(B-EW6-BH)]` como claim de drawdown inferencial: tolerancia de deterioro **cero** y límite superior de incertidumbre **válido ≤0**. Comparador EW6-BH completo; horizonte H, estado inicial I0, modelo P, políticas y supuestos explícitos. No es una garantía de menor DD en la mayoría de trayectorias ni de menores pérdidas futuras.

## Condiciones obligatorias del propietario

1. Toda conclusión declara P/modelo, H, I0 y supuestos. DD-E no equivale a dominancia por trayectoria, frecuencia favorable o ausencia de pérdidas futuras.
2. Cuando exista modelo admisible, reportar DD observado, distribución estimada de diferencias, probabilidad de deterioro, magnitud de deterioros y cuantiles relevantes. Si no son fiables o estimables, declararlo; nunca completar campos con certeza inventada.
3. Una mejora esperada sostenida por mejoras extremas infrecuentes mientras la mayoría empeora es una **limitación material visible**. No resumirla como «menor riesgo» sin esa advertencia ni ocultarla en selección/promoción.
4. DD-P sigue alternativa **no aprobada**. No crear tolerancia probabilística o criterio retrospectivo; si la frecuencia necesita gate formal, propuesta gobernada **antes** de resultados relevantes.
5. Una historia, bootstrap genérico o muchos paths de un modelo sin validar no admiten el método. Separar incertidumbre de datos, parámetros, especificación/modelo y MonteCarlo.
6. M1/G-R1/ES/volatilidad, límites absolutos Risk y demás controles son independientes. PASS DD-E no compensa otros gates ni autoriza promoción.
7. Selección Strategy V1 mantiene visibles riesgos por trayectoria y toda evidencia adversa material. Calificación económica no sustituye revisión humana ni gates operacionales.

## Límites y efectos

Q-061 pasa a DECIDED sólo como significado inferencial. No selecciona modelo/método, Strategy, engine, broker, datos o parámetros Risk. No certifica suficiencia de muestra ni permite usar holdout. `INTEGRITY_UNKNOWN`, `implementation_locked=true` y `TARGET_ACCEPTANCE_DEFERRED` se conservan.

La investigación DD queda acotada: completar especificación y pruebas viables en Team, registrar lo que requiera evidencia posterior y avanzar datos utilizables/broker/engine/reglas financieras/Plan v1.0. No expandir indefinidamente DD ni ocultar método abierto bajo aceptación host-specific.

## Referencias

- [Propuesta Q061 y ejemplo E8](../research/D-011_DD_claim_decision_RC1.md).
- [Aplicabilidad y dimensiones de incertidumbre](../research/R-020_drawdown_method_applicability_RC0.md).
- [Preregistro RC7](../research/R-020_preregistration_readiness_RC7.md).
- [G-R1](ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md).
