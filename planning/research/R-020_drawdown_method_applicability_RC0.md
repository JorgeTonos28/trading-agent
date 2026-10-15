# Drawdown — estimando, horizonte y admisión metodológica

2026-10-15. G-R1 aprobado en [ADR-020](../decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md). **METHOD_NOT_ACCEPTED**. Este documento concreta propuestas técnicas; no demuestra futuro, no selecciona Strategy V1, no abre histórico/holdout. B/K2/M1/G-R1 no se relajan.

## Tres preguntas distintas

Para NAV financiero net_trading positivo V, `MDD_H(V)=max_(0≤u≤v≤H)(1−V_v/V_u)`, incluyendo V0. Comparador: EW6-BH **completo**, no espejo de exposición. Mantener extremos intradía/gaps como riesgo adicional: MDD diario no observa la peor pérdida intradía.

| Claim | Definición | Qué puede sostener |
|---|---|---|
| Observado | d_obs(H)=MDD_H(S)−MDD_H(B) | Comparación exacta de esos paths, datos/modelo contable admitidos; no CI ficticio o ausencia de deterioro futuro |
| **DD-E, recomendado para investigar** | θ_D(H;P,I0)=E_P[MDD_H(S)−MDD_H(B)\|I0, políticas congeladas] | No deterioro **de la esperanza de máximos** bajo P/estado/horizonte declarados, si upper confidence bound≤0 y método admitido |
| DD-P | P_P(MDD_H(S)>MDD_H(B)\|I0) o cuantil de diferencia futura | Probabilidad/pérdida predictiva, otro estimando. Requiere umbral de probabilidad/cola aprobado; no se deduce del CI de θ_D |

DD-E no afirma `MDD(S)≤MDD(B)` en cada trayectoria futura; tampoco dominancia de distribuciones. Es una realización **candidata** del claim, no implícitamente aprobada por elegir tolerancia0. DD-P/CED/CDaR no sustituyen DD-E o G-R1 por conveniencia. Si se cambia el claim, gobierno material antes de resultados. No existe aquí prueba de imposibilidad general de G-R1; futuro arbitrario sin supuestos no es identificable desde un prefijo finito.

## Horizonte, estado y paths

H se fija por **fase y calendario admitido**: selección2019-01-01–2022-12-31 y confirmación propuesta2023-01-01–2026-09-30 tienen diferente cantidad de sesiones/horizonte. No llamar a ambos cuatro años ni reescalar MDD por√T. H exacto se obtiene del calendario validado antes de F0; el n1008 de E5/E6 era ficticio. θ_D(H_selection) y θ_D(H_confirmation) son claims distintos con el mismo criterio≤0, sin extrapolación automática entre horizontes. No acortar H para obtener más ventanas independientes.

Propuesta para la comparación principal: comienzo de cada fase con NAV unitizado, cash y sin posiciones/peaks heredados; warm-up sólo de indicadores. EW6 y S arrancan en la primera oportunidad autorizada según sus reglas, con costes propios. Una simulación de desarrollo continua se distingue de selección fresh; no resetear cada año o fold ni borrar drawdown abierto. La regla fresh de selección y confirmación se fija como propuesta principal **antes de F0/resultados de selección**. F1 sólo materializa el estado de la configuración elegida; no elige fresh versus carry después. Carry/peak anterior es únicamente sensibilidad predeclarada antes de F0, sin selector favorable ni sustitución de gates. Cambiar esta regla tras resultados exige nueva versión/evidencia confirmatoria.

Simular P significa paths **pareados** de fuentes/mercado, actions/calendario/disponibilidad y ejecutar reglas/ledgers/costes de S y B causalmente. Bootstrap de retornos de carteras ya realizadas conserva sólo una hipótesis estadística reducida; no es nueva ejecución de EW6-BH con deriva, señales, stops o reservas. Requiere demostrar que ese estimador reducido corresponde al claim; no conceder equivalencia por defecto.

## Método: alternativas y gate

| Ruta | Ventaja | Riesgo/admisión |
|---|---|---|
| Paths observados sin inferencia | Contabilidad inspeccionable, sin modelo predictivo inventado | Sólo descriptivo. No PASS inferencial G-R1 |
| Bloques pareados de retornos de cartera | Preserva parte de dependencia; reutiliza arch | Longitud de path/H, cost/estado no estacionario, diferencia entre sampling uncertainty y empirical prediction. No aprobado por remuestrear una vez |
| Modelo de mercado/estados + replay de políticas | Puede representar contratos causales y estado de cartera | P/parametrización/acciones/costes deben validarse; riesgo de misspecification y calibración. Simulaciones no son nuevos años observados |
| Confirmación prospectiva | Evidencia nueva con reglas congeladas | Una sola trayectoria sigue sin estimar ley futura por sí sola. No arregla automáticamente DD-P ni reserva contaminada |

Antes de admitir: P/clase de procesos y supuestos de dependencia/colas/cambios de régimen; I0/H/calendario; método/estimador; cobertura/error al borde θ=0; precisión/potencia, parámetros y sensibilidad; incertidumbre de datos/modelo/parámetros **y** MonteCarlo distinguidas; múltiples candidatas/selección/familia; pruebas de degeneración/NAV≤0/censura; revisión independiente. Muchos paths de P ajustado sólo reducen error MonteCarlo condicional; no eliminan error del modelo o de su ajuste.

Puede haber evidencia insuficiente incluso con muchos días: ventanas H solapadas no son observaciones independientes. No aplicar bootstrap genérico ni bounds de normalidad sin aplicabilidad. Upperbound que cruza0 no demuestra deterioro; mantener INSUFFICIENT_EVIDENCE/INCONCLUSIVE. Ausencia de método aplicable => NOT_EVALUATED; datos/método inválidos => INVALID_DATA_OR_METHOD. FAIL sólo con evidencia válida contraria/violación de criterio según protocolo; no `noPASS=FAIL`.

## Evidencia actual y reuse

[E7](probes/r020-path-semantics/README.md)14/14: propiedades aritméticas/path de datos ficticios, misma riqueza/ES/varianza con MDD19% vs10.9%, media exacta de6paths=.148, peaks/censura/futuro no identificado. **No calibración estadística**. E4/E5/E6 siguen sus límites. arch/statsmodels/numpy candidatos ADAPT/REUSE_AS_IS para componentes; ninguna biblioteca vuelve válido un estimando inadecuado. Motor quant R009 antes de BUILD de simulator general.

[Goldberg y Mahmoud](https://arxiv.org/abs/1404.7493) fundamenta el análisis de distribuciones de máximos de paths y su dependencia de horizonte/orden. Sus definiciones aditivas y teoría de CED no son automáticamente el MDD relativo compuesto ni un procedimiento de CI validado para este proyecto. No se adopta CED como nuevo objetivo. Evidencia de la literatura no equivale a admisión empírica.

**Continuación técnica autorizada por ADR020 condición2:** investigar DD-E como candidata con P/H explícitos, sin pedir otro permiso para definir un estimando candidato. d_obs sigue reporte exacto, no se añade un veto histórico independiente. No equiparar media con probabilidad predictiva; una adopción final/cambio material de claim requiere checkpoint sustentado. No pedir otra preferencia de tolerancia ni adoptar G-R2. D011 sigue RESEARCHING/F0 no congelado, holdoutUNKNOWN/locktrue/targetdeferred.
