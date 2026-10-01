# 02 — Strategy V1 Selection: protocolo RC0

**Estado:** OPEN (D-008, P0). **Fecha:** 2026-10-01. Ninguna estrategia seleccionada; no se han consultado backtests de MATR_V1 según declaración del propietario. El enfoque del video es el **primer candidato que descomponemos y robustecemos**, no la arquitectura ni la estrategia aprobada. Este protocolo se fija **antes** de pruebas comparativas. ADR-000 establece el alcance. La selección final requiere aprobación humana.

## Candidatos mínimos

| ID | Candidato | Estado | Qué debe quedar especificado |
|---|---|---|---|
| S-VID | Familia Video-Inspired Strategy V1 | Descompuesta desde la transcripción primaria en `research/video_inspired_strategy.md` | VID-TS (stop/ladder incompleto), VID-CONG (disclosures), VID-ALERT (alertas autorizadas) y VID-WHEEL (opciones, fuera de alcance V1). Infraestructura y SIGNAL no son estrategias. Ninguna variante entra a scorecard cuantitativo sin reglas falsables. |
| S-MATR | MATR_V1 | Ficha RC0 | Reglas de §18 y pendientes M-01–M-11 en `02_MATR_V1_spec.md`; sigue como candidato/benchmark, no seleccionado. |
| S-NEW | Otros candidatos con fundamento | Admisión abierta | Hipótesis económica, reglas, datos PIT, restricciones PAPER y motivo de inclusión previo a backtest. |

La *wheel* de opciones del video no es elegible para PAPER V1 bajo el alcance actual (sin derivados). Puede investigarse como componente separado P4; solo entra en selección si el dueño aprueba cambio de alcance. Una conexión directa Codex–broker tampoco es estrategia y no satisface el invariante de autoridad financiera. Las rentabilidades alegadas de 164,99% de una cuenta y ~72% en un dashboard congresual se registran `NO VERIFICADO` y **no generan investigación autónoma para auditarlas**. Congreso es una fuente externa entre otras; R-023/R-025 investigan Smart Money como familia amplia.

## Gates de admisión antes de comparar resultados

1. **Reglas completas:** universo, señal, entrada, salida, sizing, calendario, capital, costes y condiciones de suspensión determinables sin interpretación retrospectiva.
2. **PIT y disponibilidad:** fuente, publicación/recepción y momento de uso demostrables. Para disclosures, usar fecha pública, nunca fecha de operación del tercero como si fuera conocida.
3. **Alcance:** long-only sin leverage ni derivados para PAPER V1, salvo CR y aprobación humana.
4. **Seguridad:** ninguna variante exige LLM con autoridad directa para ordenar o modificar límites.
5. **Datos y testabilidad:** historia suficiente y derechos de uso razonables; benchmark y costes aplicables; posible replay reproducible.
6. **Complejidad operativa:** ejecución, monitoreo y fallos manejables en la primera plataforma PAPER.
7. **Encaje con el sistema:** el candidato puede usar contratos de señal, datos, riesgo, ejecución, auditoría y explicación pedagógica sin crear autoridad financiera paralela.

Un candidato que falla un gate no se descarta por intuición: se registra `DEFERRED` o `REJECTED_FOR_V1` con motivo y evidencia. Un candidato incompleto no recibe reglas inventadas para forzarlo a competir.

## Comparación cualitativa previa a backtest

Para los candidatos admitidos se documentarán: (a) claridad y fundamento de la hipótesis, (b) riesgo de sesgos y overfitting, (c) datos/licencia/coste, (d) fidelidad de replay→paper, (e) riesgos de ejecución y gap, (f) complejidad del control determinístico, (g) capacidad pedagógica y (h) valor de construir infraestructura reutilizable. Los pesos/umbrales y cualquier tie-break se aprobarán **antes** de abrir un holdout. El rendimiento histórico no será el criterio único ni se usará para alterar retroactivamente esta matriz.

## Política de evidencia y OOS

- Preservar declaración del dueño: hasta 2026-10-01 no se ha visto ningún backtest de MATR_V1 en ningún período.
- Separar *diseño de candidato* de *test estadístico*. Registrar cada variante ensayada, incluso fallida, y congelar reglas/criterios antes de consultar la muestra reservada.
- Si se mira un período para escoger entre candidatos, ese período deja de ser evidencia independiente de la estrategia elegida; se requerirá un forward/OOS nuevo para confirmación.
- Las alegaciones de rentabilidad del video, si las hay, no cuentan como rendimiento validado sin datos, método, costes y resultados reproducibles.

## Entregable de decisión

El futuro paquete al propietario mostrará cada candidato, evidencia primaria, reglas exactas, gate de admisión, scorecard, pruebas, sensibilidad, riesgos, costes, alternativas, recomendación y la pregunta única: **“¿Qué estrategia autorizamos como primera Strategy V1 para especificar y construir en PAPER?”** Se registrará ADR con fecha y aprobador. Hasta entonces, `selected_strategy: null`.
