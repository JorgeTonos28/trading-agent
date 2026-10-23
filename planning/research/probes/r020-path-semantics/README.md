# E7 — semántica de trayectorias, no inferencia

Preregistro 2026-10-15 antes de ejecutar `probe_attempt01.py`. Datos íntegramente ficticios, sin fuentes de precios, red, modelos ajustados o estrategias ejecutables. Python stdlib/Decimal, sin instalar paquetes. Una ejecución; conservar fallos y fuente/hash, sin repetir para mejorar resultados.

Preguntas: mismos retornos marginales pueden tener DD diferente; incluir NAV inicial y peaks heredados; recuperar/censurar sin ceros ficticios; enumerar una población finita conocida sin llamarla historia; pairing no se reemplaza por permutaciones independientes; un prefijo observado idéntico no determina futuro arbitrario. Control de calendario: menos de200 días calendario entre fecha de listado de GLD y enero2005 no pueden contener200 sesiones anteriores.

Expectativas previas: clustered `+.1,+.1,-.1,-.1` MDD=.19; alternado `+.1,-.1,+.1,-.1` MDD=.109; misma riqueza final=.9801, ES95=.1 y varianza marginal. NAV inicial1 seguido de.9 tiene DD.1. Peak previo1.2/NAV inicial1 difiere del fresh-window peak1. Una trayectoria sin recuperación conserva cota inferior/censura. En6 permutaciones únicas la media de DD es promedio exacto de esa población ficticia, no CI de la media futura. Invalid NAV/returns no se interpretan como riesgo cero.

Salida `result-01.json` guarda todos los checks y valores. PASS aquí sólo valida estas propiedades/cálculos; **no acepta θ_D, horizonte, bootstrap, α, cobertura, potencia, ES/vol inferencia, engine o PAPER**. Límite≤0 de G-R1 y M1 no se cambian. Future DD law UNKNOWN; F0 no congelado, holdoutUNKNOWN, locktrue/targetdeferred.
