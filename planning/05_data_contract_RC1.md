# Datos point-in-time y linaje — contrato P0 RC1

**Estado:** contrato abstracto D-014 `DECIDED` en [ADR-004](decisions/ADR-004-point-in-time-data-lineage.md), 2026-10-01. No selecciona proveedor ni declara que un dataset histórico concreto sea PIT. Baseline: [hoja §2.5 y §38](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md), [Smart Money landscape](research/smart_money_data_landscape.md), [PAPER V1 RC1](paper_v1_capability_contract_RC1.md).

## 1. Relojes que no deben confundirse

| Campo | Significado | Regla de uso |
|---|---|---|
| `event_at` | Momento del hecho económico o transacción subyacente | No demuestra que un tercero lo conociera |
| `published_at` | Momento declarado de publicación/divulgación por origen | Puede no equivaler a disponibilidad efectiva en proveedor/API |
| `source_available_at` | Primera disponibilidad demostrable en fuente primaria | Evidencia documental o captura; `UNKNOWN` si no verificable |
| `provider_available_at` | Primera disponibilidad demostrable en producto del proveedor | Específica de proveedor, dataset, canal y versión |
| `received_at` | Momento en que nuestro sistema recibió el dato en un canal concreto | Capturado con reloj sincronizado; no se inventa para períodos previos a nuestro sistema |
| `validated_at` | Momento en que la revisión pasó parsing, licencia y controles de calidad exigidos | Es el primer momento en que **nuestro** camino operativo puede consumirla |
| `decision_at` | Corte informativo de Champion o shadow | Solo observa revisiones disponibles antes de este tiempo |
| `effective_at` | Momento en que un valor/acción corporativa es válido económicamente | Se registra aparte; no adelanta su publicación |

Todos los tiempos incluyen zona u offset, precisión y procedencia. `UNKNOWN` es valor válido, nunca se rellena con `event_at` o fecha de archivo. Cada observación lleva `availability_evidence` (captura propia, timestamp proveedor verificable, documentación de difusión, estimación conservadora validada o `UNKNOWN`) y `eligible_from` calculado **para el canal y uso concretos**. No se exige un timestamp de una fuente ajena al canal si existe evidencia válida del canal usado; tampoco se confunde aceptación de un filing con recepción por nuestro sistema.

En operación capturada, `eligible_from ≥ max(received_at, validated_at, embargo/mercado aplicable)`. En replay histórico, `eligible_from` procede de evidencia PIT del proveedor/canal y una latencia conservadora preregistrada y comprobable; `received_at` propio no se falsifica retrospectivamente. Si la evidencia histórica no permite saber cuándo existía la revisión, no se habilita un backtest operable a esa resolución. Por ejemplo, un agregado con solo `filed_date` no se usa para replay intradía; podrá ensayarse con corte posterior conservador solo si se demuestra que todo el dataset estaba disponible entonces. La regla exacta de retraso por dataset se cierra en D-018/D-022/D-033 según proveedor, sin debilitar este contrato.

La [SEC distingue tiempo de aceptación, fecha de filing y cambios posteriores](https://www.sec.gov/about/webmaster-frequently-asked-questions), y advierte que no ofrece un timestamp del primer instante de disponibilidad del contenido en sec.gov. Su [API pública](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) entrega submissions y XBRL, con actualización durante el día, pero esa descripción no demuestra que un proveedor tercero o nuestro sistema recibiera cada filing en el mismo instante. Es la razón para registrar observaciones propias y evaluar cada dataset PIT.

## 2. Identidad/versionado de observación

Mínimo: `observation_id`, fuente primaria y proveedor/canal, dataset/schema/version, instrumento y entidad estable, tipo de dato/unidad, valor y moneda, clocks anteriores, `eligible_from`, `availability_evidence`, ID de documento/filing/evento, versión/revisión/supersedes, ingesta y parser versionados, calidad, licencia/uso permitido, hash del payload original y snapshot ID. Datos corregidos se guardan como nuevas revisiones; no reemplazan silenciosamente el valor que vio una decisión anterior.

El snapshot de decisión fija conjunto de observaciones y sus revisiones, universo de instrumentos conocido entonces, corporate actions y versión de ajustes, calendario/market session, política de disponibilidad y hash. Un join temporal solo admite la revisión cuyo `eligible_from ≤ decision_at` y que aún no había sido superseded **a ese instante**. Champion y Portfolio Manager shadow reciben el mismo snapshot elegible cuando sus decisiones se comparen; cualquier diferencia de contexto queda explícita y esa observación no cuenta como comparación pareada.

## 3. Reglas por familia y sesgos

- **Market bars/quotes:** registrar período que cubre la barra, cierre oficial, momento de publicación/recepción y sesión; una decisión basada en cierre no se ejecuta a ese mismo cierre si el valor aún no estaba disponible.
- **Corporate actions/dividendos/splits:** separar fecha de anuncio, ex-date, pay date y versión de ajuste. Conservar precio transable bruto; crear una vista de indicadores ajustada **as-of** que solo use acciones conocidas en el corte de decisión, y libro de posiciones/cash coherente con el evento económico. [LEAN documenta que su modo `Adjusted` usa toda la historia futura de splits/dividendos, mientras `ScaledRaw` usa historia anterior al tiempo del algoritmo](https://www.quantconnect.com/docs/v2/writing-algorithms/securities/asset-classes/us-equity/requesting-data); esto exige configurar y probar el motor, no asumir que todo precio ajustado es PIT.
- **SEC/Form 4/13F:** conservar período económico, aceptación/publicación, amendments y primera disponibilidad en canal usado. La posición reportada en 13F no es operación contemporánea al filing.
- **Congreso, options flow, dark pool, analyst revisions, fund flows:** contrato temporal propio por dataset; `event_at` solo no basta para backtest operable. D-018 decide rol/admisión, D-033 proveedor y derechos.
- **Universo/survivorship:** conservar miembros y tickers point-in-time, delistings, cambios de símbolo e instrumentos no elegibles; documentar cobertura faltante.

## 4. Gates de admisión y pruebas

1. Si falta fuente, licencia, versión o tiempo de disponibilidad exigido para uso operativo, dato queda en research/pedagogía con etiqueta de limitación; no habilita señal Champion.
2. Replay en `decision_at=t` rechaza cualquier revisión con tiempo operable posterior a `t`, aunque su `event_at` sea anterior.
3. Comparar snapshot live capturado con reconstrucción histórica del mismo proveedor; medir diferencias y declarar cuándo la historia no es PIT.
4. Dos proveedores con valores distintos generan diferencia registrada, no sustitución silenciosa. Definir prioridad y quarantine antes de ejecución.
5. Pruebas de close/next-open, filing amendido, split, dividend, ticker change, late arrival, clock skew y dataset backfill.
6. Join temporal con revisión futura y universo reconstruido: la revisión o constituyente posterior no aparece en snapshot anterior.
7. Paridad Champion/shadow: mismo snapshot/corte y mismo universo elegible; si difieren, el par se marca no comparable y no se calcula ventaja hipotética.

## 5. Build vs. Reuse y dependencias

[SEC EDGAR API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) es fuente directa candidata para filings; su timestamp de aceptación y su disponibilidad efectiva no son el mismo dato. Market/alternative-data APIs y conectores/MCP serán `WRAP` solo si entregan origen, revisiones, licencia y evidencia temporal suficiente. [LEAN](https://www.quantconnect.com/docs/v2/writing-algorithms/securities/asset-classes/us-equity/requesting-data) ofrece modos de normalización útiles pero requiere selección/configuración/probe; queda `REFERENCE_ONLY` hasta D-023. No se selecciona proveedor ni se declara `BUILD` para almacenamiento/normalización. D-020/022/023/026/033 conservan scorecards y pruebas.

**D-014 queda cerrado como semántica y gates abstractos.** Frescura por familia/estrategia, sincronización concreta, convenciones específicas de mercado/proveedor, tolerancias de calidad, licencia y muestras históricas se cierran en D-018/D-022/D-033 y con la Strategy V1 aprobada. Si la fuente elegida no puede satisfacer `eligible_from` verificable, no entra en señales/backtest operable; un cambio de esta regla requiere change record y reabrir D-014.
