# DD-E — especificación y límite de investigación actual

2026-10-23. Q-061 DECIDED en ADR-022. **CLAIM_AND_REPORT_CONTRACT_SPECIFIED**; método/modelo/aplicabilidad/suficiencia NOT_ACCEPTED. D-011 sigue RESEARCHING, sin PASS económico. No otra campaña DD general en Team salvo defecto material concreto.

## Claim aprobado y salidas

θ = E_P[MDD_H(S) − MDD_H(EW6-BH completo) | I0, políticas congeladas]. Tolerancia de deterioro cero; el límite superior de incertidumbre válido debe ser ≤0. P, H, I0, supuestos y versiones acompañan cada conclusión. Horizonte/calendario, estado inicial y warmup se fijan antes de F0 según aplicabilidad. DD diario no elimina gaps ni riesgo intradía. No hay garantía por trayectoria o frecuencia; DD-P no tiene gate aprobado.

Output obligatorio: drawdowns observados/diferencia, distribución estimada de diferencias, Pr(Δ>0), magnitudes y cuantiles, cada uno con modelo/método/fiabilidad. Un campo no estimable se marca UNKNOWN/NOT_ESTIMABLE_WITH_ADMITTED_METHOD, nunca cero. Mejoras extremas raras con mayoría de trayectorias peores se presentan como MATERIAL_LIMITATION al propietario; no como simple «menor riesgo» ni compensación automática.

El [contrato de reporte](DD_E_report_contract_RC0.json) fija cuantiles de diferencias 1/5/25/50/75/95/99%, magnitudes condicionales y contribuciones positivas/negativas a la esperanza. Son salidas descriptivas bajo modelo admisible, **no nuevos gates DD-P**. Cero masa positiva produce NOT_APPLICABLE para magnitudes condicionales. La identidad θ = E[max(Δ,0)] − E[max(−Δ,0)] hace visibles los componentes de la media. Este contrato no implementa un modelo ni valida una prueba estadística.

## Evidencia suficiente para especificar, no para calificar

E7/E8 preservan aritmética, tratamiento de horizonte/paths, no identificación y contraejemplo media/frecuencia. E8 contiene siete verificaciones matemáticas y un sentinel declarativo: no acredita independencia, cobertura o calibración. Revisión crítica y ADR-022 resuelven el significado del claim. QL2 muestra por qué contabilidad/fills deben admitirse antes de inferir: dividendos acreditados inmediatamente y fills completos por defecto no satisfacen nuestro contrato.

No se añaden sintéticos redundantes para acumular PASS.

## Validación pendiente y orden de ejecución

Antes de calificar se requieren: clase de procesos/modelo P y evidencia de aplicabilidad; incertidumbre de datos, parámetros, especificación y Monte Carlo separadas; replay causal o equivalencia demostrada del estimador reducido; error/cobertura en el borde, precisión/potencia/dependencia/colas/regímenes; familia/selector y sensibilidades predefinidas. Datos y modelos del motor admitidos son inputs necesarios. **Este trabajo no es sólo entitlement o host-specific**, ni se transfiere a R-030 para aparentar cierre.

Sin inputs admitidos, más trayectorias ficticias no demuestran aplicabilidad real. Modelos y suites integradas se ejecutarán bajo los gates del plan; los scripts de investigación permitidos pueden validar decisiones sin implementar Trading OS. Si ninguna ruta admisible permite inferencia, conservar NOT_EVALUATED, INSUFFICIENT_EVIDENCE o INCONCLUSIVE según causa y NO_STRATEGY_QUALIFIED cuando corresponda. No G-R2 automático, márgenes adaptados ni investigación indefinida.

Próximo foco: datos/cash/acciones/PIT, broker/protección, motor/modelos, configuración financiera y Plan v1.0. Reabrir teoría DD sólo ante evidencia que pueda cambiar una decisión material, no para forzar PASS.
