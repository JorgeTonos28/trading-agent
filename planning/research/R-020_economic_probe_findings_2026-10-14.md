# E3 — eficiencia, exposición e inferencia: resultados sintéticos

2026-10-14 · [protocolo](probes/r020-economic-contract/README.md), [fuente](probes/r020-economic-contract/probe_attempt01.py), [captura](probes/r020-economic-contract/result-01.json). **19/19PASS según fixtures preregistrados**, cero backtests/trials de estrategias. Usa depsE2 arch8/statsmodels0.15 en workspace, sin instalación nueva ni config/runtime/billing. No acepta F0/dataset/target/alpha.

## Qué demuestra

Un portafolio ficticio exactamente λB+(1−λ)cash reduce σ frente a B, pero diferencia respecto al espejo es0: menor exposición **no** es evidencia de eficiencia incremental. Cashonly tiene exceso0; duplicar carry falsea retorno. Gates AND rechazan fixturecashonly/ratio1, ratioNaN y lowerboundNI insuficiente; expectedstate insuficiente no FAIL económico. No productionvalidator ni Risk Engine.

`StationaryBootstrap.conf_int` pin8 devuelve shape correcto, límites unilaterales y repetición con seed; intervalos son **marginales**, no jointcoverage validada. API fuente usa `tail='lower'`; texto narrativo docs menciona `type`, por lo que sourcepin y prueba cuentan, no ejemplo latest asumido igual. No cobertura nominal/errorrates/colas/censura/power de estrategia demostrado.

## Muestra: advertencia derivada de un supuesto explícito

Ilustración normal iid de observaciones anuales independientes, igualdad verdadera de medias, alphaone-sided0.025/power0.8 fixtures: `T≈(z_.975+z_.8)^2*(σ_diff/δ)^2`. Si σdiffanual5% y margen1pp, aproximación196.22observaciones anuales frente198.15por t-test solve_power. No estimación para PRICE/MATR, CAGRbootstrap o mercado real. Si σdiff1%, mismos fixtures dan7.85; con margen2pp dan1.96. Covarianza pareada y drift verdadero cambian interpretación, dependencia/cambios de régimen la pueden invalidar.

Consecuencia de diseño: **cuatro años no garantizan demostrar cualquier margen estrecho**; no inferir alpha por1000barras ni ampliar margen para poder pasar. Esta tabla no recomienda1/2pp ni una duración de196años de PAPER. Valores aprobables requieren utilidad/exposición/benchmarks elegidos y potencia/precision validada con supuestos justificables antes de resultados. Si evidencia insuficiente, conservar estado y NO_STRATEGY_QUALIFIED, sin sustituir evidencia económica por OP_PASS.

## Lo pendiente y reproducibilidad

Números de fixtureδ1pp/ε1pp/riskratio0.8,block5,reps500,seed1234 y samples500 **no aprobados para evaluación financiera**. PrimariaES, taillevel/guardrails y margins de RC3 aún propuestas. Rawsource/result/launcher/dependencyhashes preservados; source mismo no rerun. Sin secretcontext, envwhitelist y guardPython; no evento socket observado, no seguridadOS probada. Transitivas review incompleta en E2, targetcompatibility UNKNOWN. Cumplimiento de pipeline económica real requiere data/calendario/models/admission/independentreview, no número dePASS.

## Cobertura pendiente y procedencia de declaraciones

El protocolo E3 planteó inputs constantes/no finitos de conf_int, pero la captura sólo ejecutó series finitas y un ratio NaN del fixture de gates: **constant/nonfinite conf_int = NOT_TESTED**. 19/19 no significa cobertura de todo el protocolo ni de un agregador real NO_STRATEGY_QUALIFIED. No se cambia source/result ni se repite el probe para ocultar esta limitación.

QA documental detectó un ERROR inicial al contrastar hashes de declaraciones históricas: cuatro capturas eran CRLF y sus blobs Git son LF. Se conservan SHA256 originales y commit1727470; registry añade EOL capturado y SHA256 del blob Git para portabilidad, sin cambiar contenido histórico ni resultados. Nueva QA valida ambas representaciones. No es una admisión de datos o aceptación target.
