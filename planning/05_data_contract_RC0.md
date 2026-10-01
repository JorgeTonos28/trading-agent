# Datos point-in-time y linaje — contrato P0 RC0

**Estado:** D-014 `RESEARCHING`, 2026-10-01. Documento de diseño, sin proveedor seleccionado. Baseline: [hoja §2.5 y §38](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [Smart Money landscape](research/smart_money_data_landscape.md), [PAPER V1 RC1](paper_v1_capability_contract_RC1.md).

## 1. Relojes que no deben confundirse

| Campo | Significado | Regla de uso |
|---|---|---|
| `event_at` | Momento del hecho económico o transacción subyacente | No demuestra que un tercero lo conociera |
| `published_at` | Momento declarado de publicación/divulgación por origen | Puede no equivaler a disponibilidad efectiva en proveedor/API |
| `source_available_at` | Primera disponibilidad demostrable en fuente primaria | Evidencia documental o captura; `UNKNOWN` si no verificable |
| `provider_available_at` | Primera disponibilidad demostrable en producto del proveedor | Específica de proveedor, dataset, canal y versión |
| `received_at` | Momento en que nuestro sistema recibió el dato | Capturado con reloj sincronizado; no sustituye historia previa faltante |
| `decision_at` | Corte informativo de Champion o shadow | Solo observa revisiones disponibles antes de este tiempo |
| `effective_at` | Momento en que un valor/acción corporativa es válido económicamente | Se registra aparte; no adelanta su publicación |

Todos los tiempos incluyen zona u offset, precisión y procedencia. `UNKNOWN` es valor válido, nunca se rellena con `event_at` o fecha de archivo. Para un dato que alimenta señal operativa, la elegibilidad se determina por el **último tiempo demostrable relevante** entre publicación, fuente/proveedor y recepción según el canal usado, más latencia/mercado aplicables. Un histórico agregado que solo informa `filed_date` sin primera disponibilidad intradía no habilita automáticamente replay intradía.

La [SEC distingue tiempo de aceptación, fecha de filing y cambios posteriores](https://www.sec.gov/about/webmaster-frequently-asked-questions), y advierte que no ofrece un timestamp del primer instante de disponibilidad del contenido en sec.gov. Su [API pública](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) entrega submissions y XBRL, con actualización durante el día, pero esa descripción no demuestra que un proveedor tercero o nuestro sistema recibiera cada filing en el mismo instante. Es la razón para registrar observaciones propias y evaluar cada dataset PIT.

## 2. Identidad/versionado de observación

Mínimo: `observation_id`, fuente primaria y proveedor/canal, dataset/schema/version, instrumento y entidad estable, tipo de dato/unidad, valor y moneda, clocks anteriores, ID de documento/filing/evento, versión/revisión/supersedes, ingesta y parser versionados, calidad, licencia/uso permitido, hash del payload original y snapshot ID. Datos corregidos se guardan como nuevas revisiones; no reemplazan silenciosamente el valor que vio una decisión anterior.

El snapshot de decisión fija conjunto de observaciones y sus revisiones, universo de instrumentos conocido entonces, corporate actions y versión de ajustes, calendario/market session, política de disponibilidad y hash. Champion y Portfolio Manager shadow reciben el mismo snapshot elegible cuando sus decisiones se comparen; cualquier diferencia de contexto queda explícita y esa observación no cuenta como comparación pareada.

## 3. Reglas por familia y sesgos

- **Market bars/quotes:** registrar período que cubre la barra, cierre oficial, momento de publicación/recepción y sesión; una decisión basada en cierre no se ejecuta a ese mismo cierre si el valor aún no estaba disponible.
- **Corporate actions/dividendos/splits:** separar fecha de anuncio, ex-date, pay date y versión de ajuste. Mantener precio transable y serie ajustada con política explícita; evitar aplicar retroactivamente un ajuste como dato conocido antes del anuncio.
- **SEC/Form 4/13F:** conservar período económico, aceptación/publicación, amendments y primera disponibilidad en canal usado. La posición reportada en 13F no es operación contemporánea al filing.
- **Congreso, options flow, dark pool, analyst revisions, fund flows:** contrato temporal propio por dataset; `event_at` solo no basta para backtest operable. D-018 decide rol/admisión, D-033 proveedor y derechos.
- **Universo/survivorship:** conservar miembros y tickers point-in-time, delistings, cambios de símbolo e instrumentos no elegibles; documentar cobertura faltante.

## 4. Gates de admisión y pruebas

1. Si falta fuente, licencia, versión o tiempo de disponibilidad exigido para uso operativo, dato queda en research/pedagogía con etiqueta de limitación; no habilita señal Champion.
2. Replay en `decision_at=t` rechaza cualquier revisión con tiempo operable posterior a `t`, aunque su `event_at` sea anterior.
3. Comparar snapshot live capturado con reconstrucción histórica del mismo proveedor; medir diferencias y declarar cuándo la historia no es PIT.
4. Dos proveedores con valores distintos generan diferencia registrada, no sustitución silenciosa. Definir prioridad y quarantine antes de ejecución.
5. Pruebas de close/next-open, filing amendido, split, dividend, ticker change, late arrival, clock skew y dataset backfill.

**Pendientes para cierre D-014:** umbral de frescura por familia/estrategia, fuentes de tiempo y sincronización, estructura de snapshots, convenciones de corporate actions/ajustes, tolerancias de calidad, licencia y muestras históricas. D-022/D-033 comparan proveedores; la especificación debe permitir escogerlos después. Build vs. Reuse: usar formatos/APIs de proveedor o bases oficiales como entrada bajo normalización/linaje; no seleccionar aún librería, almacenamiento ni MCP como fuente de verdad.
