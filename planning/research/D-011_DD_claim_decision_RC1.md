# Q-061 — claim final de drawdown bajo G-R1

**Vigencia owner 2026-10-23:** Q061 DECIDED, DD-E condicionado aprobado con siete condiciones en [ADR022](../decisions/ADR-022-conditional-expected-drawdown-claim.md). Las propuestas anteriores se conservan como antecedentes. Método/modelo/suficiencia no aceptados; DD-P sin aprobar. Foco siguiente datos/broker/engine/reglas, sin investigación DD indefinida.

2026-10-23. **P0 / READY_FOR_DECISION**, propietario; D-011 RESEARCHING. Propuesta material de significado, no cambio de tolerancia G-R1 ni permiso para seguir investigando DD-E. No ADR aprobado por anticipado. B/K2/M1/G-R1, implementación bloqueada y target diferido intactos.

## Problema y evidencia nueva

G-R1 aprueba no deterioro del drawdown, pero la realización inferencial no estaba seleccionada. [Contrato de aplicabilidad](R-020_drawdown_method_applicability_RC0.md) distingue DD observado, DD-E y DD-P. [E8 reproducible](probes/r020-dd-identification/README.md) construye dos leyes válidas, ambas con DD diferencial esperado de **−0.1punto porcentual**:

| Ley ficticia | Diferencia de máximos DD, S−EW6 | Probabilidad de DD peor |
|---|---|---|
| A |+1pp con prob.90%; −10pp con prob.10% |90% |
| B |+8pp con prob.10%; −1pp con prob.90% |10% |

La misma mejora media no asegura una baja frecuencia de deterioro. Un95% de confianza sobre una media no significa95% de trayectorias con mejor DD. El ejemplo no informa rentabilidad ni frecuencia real de ningún candidato.

## Alternativas y trade-offs

| Alternativa | Criterio | Qué permite afirmar / límite |
|---|---|---|
| **DD-E condicionado, recomendado** | θ_D(H;P,I0)=E_P[MDD_H(S)−MDD_H(EW6)]≤0, con upper bound válido≤0 | Ausencia de deterioro de la **esperanza de máximos DD** bajo modelo/horizonte/estado declarados. No pathwise ni probabilidad de pérdida. Exige método/modelo admisible, puede quedar inconcluso |
| DD-P / cuantil predictivo | Probabilidad de diferencia>0 o cuantil de la diferencia | Responde a frecuencia/magnitud de deterioro futuro; exige seleccionar tolerancia de probabilidad/cola y suficiente evidencia nueva. No autorizadas aquí; no derivables de α estadístico |
| Mantener claim pendiente | Sólo reporte observado, sin PASS inferencial DD | No inventa garantía. D-011/F0 de calificación sigue incompleto; no sustituir por G-R2 o quitar el endpoint |

Una garantía en todas las trayectorias no se infiere de una historia finita sin restricciones demostradas del diseño/modelo. No se ofrece como «resultado95%» ni se declara imposible todo método DD.

## Recomendación concreta

Adoptar **DD-E como significado inferencial condicionado** de G-R1, manteniendo cero deterioro y EW6 completo; reportar obligatoriamente d_obs, distribución de diferencias, frecuencia de deterioro y cuantiles cuando exista un modelo admisible. Esos reportes **no añaden un umbral DD-P** ni un veto histórico no aprobado. Toda calificación debe decir explícitamente «esperanza bajo P,H,I0», sin promesa sobre cada trayectoria o ausencia de deterioro futuro.

La aprobación del claim **no acepta método/modelo**, no fija umbral de probabilidad ni certifica muestra suficiente. MV01–08/revisión/aplicabilidad y todos los otros endpoints siguen necesarios; UNKNOWN/INSUFFICIENT_EVIDENCE/INCONCLUSIVE permanecen resultados válidos. No utilizar retornos/holdout para elegir este significado.

## Decisión exacta solicitada

¿Acepta el propietario **DD-E condicionado** como realización final del claim inferencial G-R1, con los reportes obligatorios anteriores y sin interpretarlo como control de la frecuencia de deterioro? Si esa frecuencia debe ser un gate adicional, deberá especificarse como DD-P con una propuesta posterior de tolerancia justificada; no se inventa aquí. No repetir aprobación de B/K2/M1/G-R1, capital10k o cinco escalas.
