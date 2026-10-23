# E8 — identificación del claim DD y precisión, antes de resultados

2026-10-23. Experimento matemático ficticio: leyes discretas conocidas y cota de media para variables acotadas independientes. No precios, strategy/backtest, fitted market model ni nuevo bootstrap. No valida inferencia CAGR/ES/DD real.

Población A: ΔMDD=+0.01 con p=.9 y −.10 con p=.1; B: +.08 con p=.1 y −.01 con p=.9. Ambas tienen esperanza−.001 pero probabilidades de deterioro90% y10%. Construir NAVs de dos estados contra benchmark MDD.20 sólo verifica que los valores representan diferencias posibles de MDD relativo. No decidir por estas probabilidades ficticias ni introducir nuevo guardrail.

Para Z=MDD_S−MDD_B en[−1,1] y n paths independientes bajo una ley fija, cota Hoeffding unilateral: U=mean(Z)+sqrt(2*log(1/alpha)/n), truncable a1. Con n1/alpha.05 es vacua, no PASS incluso si media−1; para media−.2, n149 aún cruza0 y n150 no. Es limitación de **esta ruta sin supuestos adicionales**, no imposibilidad general de G-R1/DD-E. Simular150paths de un P ajustado no aporta150 observaciones independientes del mercado.

Se guardan cálculos exactos/rangos y hash, create-exclusive. No campaña MC/calibración/potencia/método aceptado. B/K2/M1/G-R1 inalterados; propuesta DD-E requiere decisión material de claim, datos/modelo/uncertainty antes de PASS.

Resultado01:8checks marcadosPASS en captura: siete verificaciones matemáticas y un sentinel False/False que declara no asumir independencia; **no la comprueba**. [Hoeffding1963](https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830) es referencia primaria de la desigualdad para variables independientes acotadas; aquí se usa su forma unilateral con rango2. No se afirma validación de supuestos reales, lectura de evidencia de mercado ni calibración completa por estos cálculos.
