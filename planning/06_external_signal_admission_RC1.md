# Señales externas y Smart Money — contrato de roles y admisión P0 RC1

**Estado:** D-018 `DECIDED` en [ADR-005](decisions/ADR-005-external-signal-admission.md), 2026-10-01. Cierra **roles y gates abstractos**, no selecciona familia, dataset, proveedor ni señal para Strategy V1. `implementation_locked=true`. Baseline: [hoja §2.5, §8 y §38](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [PAPER V1 RC1](paper_v1_capability_contract_RC1.md), [datos PIT/ADR-004](05_data_contract_RC1.md) y [R-023/R-025](research/smart_money_data_landscape.md).

## 1. Vocabulario y fronteras

“Smart Money” es una **etiqueta de descubrimiento**, no un feed o una señal homogénea. Una observación externa es dato; una señal es una transformación falsable, versionada y admitida por la estrategia Champion aprobada. Research Agent, Smart Money Agent, proveedor, MCP y Portfolio Manager shadow no pueden crear `TradeIntent` operativo, alterar sizing o cursar órdenes. Un Champion inicial **puede** combinar varias familias si cada entrada está aprobada en su especificación y pasa gates; no se exige que use alguna.

| Nivel | Uso permitido | Autoridad |
|---|---|---|
| `RESEARCH_ONLY` | Describir hipótesis, cobertura, calidad, sesgos y candidatos; exploración con limitaciones explícitas | Sin señal operativa |
| `PEDAGOGICAL_CONTEXT` | Explicar con fuente y fecha una observación relevante, sin atribuirle causalidad no demostrada | Sin cambio de Champion o riesgo |
| `CANDIDATE_SIGNAL` | Regla falsable, datos PIT, costes y protocolo OOS en Strategy Lab/Challenger | Sin capital ni promoción automática |
| `APPROVED_CHAMPION_INPUT` | Fuente/regla/versiones enumeradas en Strategy V1 aprobada, después de datos, validación y riesgo | Solo Signal Engine determinístico; intent sigue Risk Engine |
| `REJECTED_FOR_OPERATION` | Evidencia temporal, licencia, semántica o fiabilidad insuficientes | Puede conservarse como caso educativo si los derechos lo permiten |

La promoción entre niveles no la decide el agente. `APPROVED_CHAMPION_INPUT` requiere D-008 (estrategia final aprobada por humano), D-022/D-033 para proveedor/datos, D-011 para validación y D-012 para riesgo aplicable. Un cambio posterior de familia o regla central es cambio de Champion y requiere gobierno humano.

## 2. Matriz de familias y cautelas semánticas

| Familia | Hecho que realmente representa | Riesgo de interpretación / gate adicional | Rol inicial |
|---|---|---|---|
| Divulgación congresual | Transacción reportada después del hecho; Cámara exige reportar dentro de 30 días de conocerla o 45 días de la transacción, lo primero que ocurra, para operaciones cubiertas ([House Ethics](https://ethics.house.gov/periodic-transaction-report-calculator/)) | Fecha de trade ≠ publicación ni recepción; rangos de importe, correcciones, selección ex post de político | `RESEARCH_ONLY`; candidato solo con publicación/canal PIT y regla ex ante |
| SEC Form 4 / insiders | Cambio reportado de titularidad; Form 4 normalmente se presenta antes del fin del segundo día hábil ([SEC Form 4](https://www.sec.gov/files/form4.pdf)) | Código `P` compra abierta difiere de grant, ejercicio, retención fiscal o plan; filing tardío/amendment | `RESEARCH_ONLY`; reglas por código/transacción y `eligible_from` |
| 13F / hedge-fund holdings | Tenencia al cierre trimestral; filing hasta 45 días después ([SEC 13F FAQ](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f)) | Tenencia no demuestra momento/precio de compra ni cartera completa de riesgo; amendments y universo de gestores | `RESEARCH_ONLY`; no tratar como flow inmediato |
| Unusual options activity | Transacciones/quotes de opciones observadas o inferidas por proveedor | Spread/hedge/multi-leg y dirección de agresor no equivalen a apuesta direccional; opciones **como órdenes** fuera de PAPER V1 | `RESEARCH_ONLY`; una señal sobre equities requeriría hipótesis separada |
| Block/off-exchange/dark pool | Prints, agregados o volumen ATS/no ATS; FINRA publica transparencia OTC con retraso ([FINRA](https://www.finra.org/filing-reporting/otc-transparency)) | Volumen agregado no identifica automáticamente comprador, intención, dirección ni timing en tiempo real | `RESEARCH_ONLY`; verificar granularidad/publicación de cada dataset |
| Analyst revisions | Revisión de estimado/recomendación publicada o redistribuida | Primer timestamp comercial, revisiones posteriores, conflictos de cobertura y coste/licencia | `RESEARCH_ONLY`; candidato con captura/archivo PIT |
| Fund flows / ETF holdings | Flujo/creación/redención o cambio de cartera reportado | Frecuencia, lag, atribución y revisión; holdings no necesariamente señal de demanda inmediata | `RESEARCH_ONLY`; contrato específico por dataset |
| Otras fuentes externas | Evento definido en su fuente primaria | Se evalúa con los mismos gates; no se admite por pertenecer a la etiqueta “Smart Money” | `RESEARCH_ONLY` inicialmente |

Los plazos normativos describen **deadline de reporte**, no cuándo un evento concreto estuvo visible en un API o para nuestra decisión. [SEC distingue aceptación y disponibilidad](https://www.sec.gov/about/webmaster-frequently-asked-questions). Ningún lag fijo de marketing se sustituye por `eligible_from` del contrato PIT.

## 3. Gates acumulativos antes de una señal operativa

1. **Semántica:** definición de hecho, unidad, código/tipo, entidad e instrumento; reglas de normalización y casos ambiguos. Una operación de tercero no se transforma en compra nuestra sin hipótesis y reglas propias.
2. **PIT:** evidencia por canal de primera disponibilidad, revisiones, cutoff y latencia conservadora conforme a ADR-004; histórico suficientemente fiel. Si falta, bajar resolución con justificación o permanecer `RESEARCH_ONLY`.
3. **Cobertura y calidad:** universo histórico, missingness, amendments, survivorship, ticker/entity mapping, duplicados y comparación con fuente primaria.
4. **Derechos y economía:** API/volumen/historia permitidos, almacenamiento/uso automatizado, coste total y plan de salida; gasto material requiere aprobación humana.
5. **Hipótesis y validación:** regla falsable, benchmark, costes, sensibilidad y OOS preregistrado con control de múltiples pruebas D-011; no inferir alpha de un dashboard ni de una correlación retrospectiva.
6. **Encaje operativo:** horizonte y latencia compatibles, instrumento long-only permitido, señal determinística, explicación auditada, manejo de stale/outage y controles D-012/013/017.
7. **Gobierno:** candidato pasa por Challenger; solo Strategy V1/Champion aprobada puede usarlo. Cambios de peso/fuente que alteren comportamiento financiero requieren nueva versión y gate humano.

Un fallo de gate se documenta con motivo y estado, sin sustituir datos inexistentes por supuestos optimistas. El papel `PEDAGOGICAL_CONTEXT` no legitima usar una fuente como señal; pedagogía distingue observación, hipótesis y razón efectiva de la orden.

## 4. Build vs. Reuse y trabajos pendientes

Para cada dataset se compararán fuentes primarias (SEC/EDGAR, registros oficiales, FINRA cuando aplique), Quiver, Unusual Whales, Capitol Trades y especialistas adicionales. Las rutas posibles son `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT`, con las cinco dimensiones `EXISTS`, `AVAILABLE_TO_US`, `TECHNICALLY_COMPATIBLE`, `ECONOMICALLY_REASONABLE`, `SELECTED`. Un API/MCP puede ser `WRAP` para ingestión de solo lectura; no adquiere autoridad de órdenes. Ningún proveedor está seleccionado y no se presupone una plataforma única.

**Pendientes fuera de D-018:** R-021 intenta demostrar PIT de candidatos; D-033/R-025 compara proveedores por dataset; D-022 evalúa mercado/históricos; D-008 selecciona Strategy V1 con aprobación humana. La utilidad predictiva de familias que no entren en V1 permanece D-050 P4; la factibilidad de una fuente que sí pueda alimentar V1 debe resolverse antes de seleccionarla.
