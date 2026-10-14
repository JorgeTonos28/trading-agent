# R-023/R-025 — Smart Money y proveedores de datos alternativos

**Fecha:** 2026-10-01. **Estado:** roles/admisión P0 cerrados en [ADR-005](../decisions/ADR-005-external-signal-admission.md) y [contrato RC1](../06_external_signal_admission_RC1.md); proveedores y datasets P1 `RESEARCHING` en R-025/D-033. **Decisiones:** D-014/D-018 `DECIDED` en semántica abstracta, D-033 abierta. Ninguna familia de señales ni proveedor está seleccionado. «Smart Money» es una etiqueta de investigación, **no una señal homogénea ni sinónimo de operaciones congresuales**.

## Familias de señales a investigar

| Familia | Fuente/evento subyacente | Pregunta de viabilidad |
|---|---|---|
| Divulgaciones congresuales | Operación declarada por legislador y fecha de divulgación | ¿Cuándo estuvo realmente disponible, qué activo/tamaño se conoce y qué lag existe? |
| Insider transactions | SEC Forms 3/4/5, especialmente Form 4 | ¿Se distinguen compras discrecionales de grants, ejercicios, planes 10b5-1 y ventas? |
| Posiciones institucionales / hedge funds | 13F y enmiendas | ¿Es útil una tenencia trimestral publicada con retraso, sin tratarla como operación en tiempo real? |
| Unusual options activity | Flow de opciones, blocks/sweeps, open interest | ¿Se distinguen coberturas/spreads de apuestas direccionales y cuál es la historia utilizable? |
| Block/off-exchange/dark-pool | Prints y agregaciones fuera de bolsa | ¿Conocemos lado/agresor y momento de publicación, o solo volumen no interpretable? |
| Analyst revisions | Cambios de recomendación, estimados y precio objetivo | ¿Cuál fue el primer timestamp comercialmente accesible y el coste/licencia? |
| Fund flows | ETF/fondo, creación/redención, holdings | ¿Frecuencia, retraso, revisiones y atribución soportan una señal? |
| Otras | Contratos públicos, lobbying, short interest, FTD, noticias u otras con fundamento | ¿Aportan información incremental, legalmente utilizable y operacionalmente mantenible? |

Para todas: **fecha del hecho ≠ fecha de publicación ≠ fecha de recepción ≠ primer momento operable**. Una fuente puede servir al Research Agent o al Pedagogical Agent sin alimentar al Signal Engine. La utilidad predictiva se estudiará solo después de aprobar calidad, PIT, licencia y coste; no se presupone alpha.

## Proveedores / rutas Build vs. Reuse (inventario inicial)

| Candidato | Evidencia oficial inicial | Capacidades aparentes | API/integración | Estado de las dimensiones decisivas |
|---|---|---|---|---|
| Quiver Quantitative | [API](https://api.quiverquant.com/), [planes/MCP](https://api.quiverquant.com/pricing/) | Congreso, Form 4, 13F/hedge funds, off-exchange y otras series según oferta actual | REST y MCP anunciados | Histórico, timestamps PIT, cobertura, límites, precios aplicables y licencia: **por verificar en ficha/probe** |
| Unusual Whales | [Developers/API](https://unusualwhales.com/developers) | Options flow, dark pool, Congreso, insider, instituciones/13F, ETF y más categorías anunciadas | API y MCP anunciados | Verificar profundidad histórica por endpoint, `filed_at` vs `available_at`, latencia observada, plan/coste y uso automatizado |
| Capitol Trades | [Sitio del proveedor](https://www.capitoltrades.com/about-us) | Exploración y agregación de operaciones congresuales | API/licencia para integración **no confirmadas** | Verificar oferta comercial, términos de extracción, timestamps y backfill; no asumir scraping permitido |
| SEC/EDGAR directo | [Developer Resources](https://www.sec.gov/about/developer-resources), [APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | Presentaciones oficiales Form 4, 13F y otros filings | API de submissions/XBRL y archivos/feeds oficiales; la normalización de Form 4/13F requiere evaluación | Acceso público documentado; evaluar parsing, rate limits, enmiendas, primera publicación y coste operativo |
| Fuentes oficiales Cámara/Senado | Sitios de divulgación a identificar y comprobar | Registros primarios del Congreso | Formato, acceso automatizado y términos **por verificar** | Necesaria referencia para auditar agregadores y cronología |
| Disclosed Capitol | [API oficial](https://www.disclosedcapitol.com/data-files/api) | Endpoint de operaciones congresuales y fechas declaradas | API anunciada | Candidato adicional; comprobar procedencia, historia, timestamps, precio y licencia |
| Otros por descubrir | Pendiente | Revisions, fund flows, institucional, opciones y mercados alternativos | Pendiente | Identificar proveedores especializados, no forzar proveedor único |

**Hechos e inferencias:** Las capacidades de Quiver, Unusual Whales y Disclosed Capitol son declaraciones de sus páginas de producto, no comprobaciones independientes de calidad. EDGAR es fuente primaria de filings, pero sus APIs públicas documentadas no equivalen a una API normalizada lista para todas las señales. El inventario no implica que Capitol Trades tenga API pública. Ningún precio anunciado se adopta como coste final ni se contrata un servicio.

## Scorecard obligatorio por dataset y proveedor

1. **Cobertura:** activos, geografía, períodos, entidades, versiones/enmiendas, survivorship y huecos.
2. **Semántica temporal:** `event_at`, `filed_at`, `published_at`, `vendor_first_seen_at`, `received_at`, revisiones y zona horaria; backfill históricamente fiel.
3. **Latencia y confiabilidad:** distribución medida, disponibilidad, errores, correcciones y SLA.
4. **Integración:** API, bulk, streaming/webhooks, MCP, límites, esquema, autenticación y mantenimiento.
5. **Economía/licencia:** precio vigente, escalado, almacenamiento, derivados, uso interno/automatizado, redistribución y salida del proveedor.
6. **Calidad para backtest:** enlace a documento primario, identificadores estables, universo histórico, exclusiones, replay y controles de sesgo.
7. **Utilidad en el sistema:** research, pedagogía, señal candidata, validación cruzada o descarte; valor marginal frente a otras fuentes.

El resultado puede ser **varios proveedores especializados** o fuentes oficiales más normalización propia. Cada dataset recibirá disposición `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT` **por fase**, con criterio y coste. ADR-008 permite estudiar alternativas pagas; contratar/consumir con gasto incremental requiere aprobación humana. PAPER prioriza fuentes incluidas/gratuitas suficientemente fiables; LIVE admite valor incremental pago, sin presuponer alpha.

## Scorecard económico por proveedor y después por dataset

Aplicar [ADR-008/ficha común](../economic_scorecard.md): fijo/variable/mensual/escala, coste de backfill/almacenamiento, planes/add-ons, licencia automatizada, calidad/latencia/PIT frente a fuente gratuita, mantenimiento/lock-in, beneficio y condición para pagar. Las filas siguientes no actualizan precios; `UNKNOWN` requiere documentación/cotización vigente.

| Candidato | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| Quiver | UNKNOWN por dataset/plan | UNKNOWN | UNKNOWN | SEC/EDGAR/registros oficiales según familia | Hipótesis: normalización, cobertura/PIT/latencia; medir | YES antes de gasto |
| Unusual Whales | UNKNOWN por dataset/plan | UNKNOWN | UNKNOWN | Fuentes oficiales para filings; flow equivalente UNKNOWN | Hipótesis: flow/cobertura/historia/PIT; medir | YES antes de gasto |
| Capitol Trades | UNKNOWN integración/licencia | UNKNOWN | UNKNOWN | Registros oficiales Congreso | Hipótesis: limpieza/entidades/cronología; medir | YES antes de gasto |
| SEC/EDGAR directo | PARTIAL acceso público; workflow por probar | Acceso público; normalización/operación UNKNOWN | UNKNOWN operación/escala | Esta fuente primaria | Agregador solo si mejora calidad/continuidad/esfuerzo con evidencia | YES si gasto complementario |
| Cámara/Senado oficial | UNKNOWN automatización/historia | UNKNOWN | UNKNOWN operación | Esta fuente primaria candidata | Agregador solo si mejora cronología/cobertura con evidencia | YES si gasto complementario |
| Disclosed Capitol | UNKNOWN plan/licencia/PIT | UNKNOWN | UNKNOWN | Registros oficiales Congreso | Hipótesis: normalización/history/API; medir | YES antes de gasto |
| Otros por descubrir | UNKNOWN | UNKNOWN | UNKNOWN | Por familia | Pendiente de diferencia medible | YES antes de gasto |

La necesidad de pagar puede justificarse por fiabilidad o datos aun sin demostrar retorno predictivo; admitir la fuente como señal operativa sigue requiriendo los gates PIT/licencia/OOS de ADR-005 y selección Strategy V1. Un proveedor caro/gratis no obtiene admisión automática.

## Orden de probes (desechables, sin Trading OS)

1. Recolectar documentación, contrato y precio oficial de cada candidato.
2. Construir muestra pequeña de eventos equivalentes entre fuente oficial y agregadores; comparar campos y fechas, sin credenciales ni suscripción todavía.
3. Verificar que el histórico conserva el primer momento público y no solo el estado actual enriquecido.
4. Medir cobertura/latencia y estimar esfuerzo de integración; decidir qué familias son factibles para V1, research-only o futuras.

**Gate:** D-018/ADR-005 define roles y admisión abstracta; ADR-004 fija semántica PIT. D-033 selecciona proveedor(es) solo después del scorecard, o deja una familia diferida con razón explícita. D-008 aprueba cualquier uso operativo en Strategy V1. No se requiere demostrar o refutar las cifras del video.

## SEC/EDGAR — avance R-020/R-025 documental, 2026-10-05

[DatasetAdmissibilityCard](R-020_SEC_dataset_admissibility_RC0.md): APIs de lectura públicas sin key y archives históricos verificadas documentalmente; no dataset/probe/selección. SEC declara ausencia de timestamp que indique primera disponibilidad del contenido en sec.gov, de modo que acceptance no equivale a publicación o recepción. Historia PIT/canal/quality/normalización siguen CONDITIONAL; comparar specialized vendors antes de construir extractor importante. Congresional, Form4,13F y demás familias siguen abiertas independientemente.

## Evidencia y scorecard vigente parcial — 2026-10-07

[Wave 01](R-025_provider_evidence_wave01_2026-10-07.md) actualiza precios/rutas/restricciones y seis campos económicos para Quiver/UW/Capitol/SEC. Las tablas anteriores son inventario inicial, no precios vigentes. Probe único de schema público Quiver sin auth observa campos temporales, **no** acceso a dataset, PIT ni licencia de uso. Documentación pública no habilita automáticamente MCP/API/servicios.

Quiver/UW son REFERENCE_ONLY actualmente y WRAP futuros condicionados; SEC WRAP/ADAPT candidato sujeto a normalizador reusable, no BUILD por defecto. Capitol conserva integración/licencia UNKNOWN tras error de acceso documental, sin rechazo. Ningún proveedor ni familia seleccionado. Congreso, Form4,13F/hedge funds, options/blocks, revisions y flows siguen separados; faltan evidencia de clocks históricos, derechos y utilidad por familia.

## Normalización y admisión — 2026-10-13

[R-021 RC1](R-021_external_dataset_admission_RC1.md): Form4 códigoP no prueba por sí mismo exchange transaction; 13F holdings no whole portfolio/trade timing. EdgarTools MIT es ADAPT/WRAP candidato **de datos**, no selector de MCP/Skill/runtime. Probe XML sintético aún preparado/no ejecutado; no parser construido ni datos admitidos. [Wave data02](R-008_market_data_evidence_wave02_2026-10-13.md) añade reserva especializada analyst/news/imbalance paga, sin gasto, entitlement o PIT demostrados.

## E1 normalizador SEC — 2026-10-13

[EdgarTools findings](R-021_edgartools_findings_2026-10-13.md):7/7table-only sintéticos y full factory ERROR; no disponibilidad histórica/PIT demostrada. ADAPT/WRAP normalizador candidato, ningún proveedor/familia seleccionado. Footnotes/planes/owners/mapping temporal y primary-vendor siguen gates; no extraer «conviction» del label market_trades.

## Form4 candidata externa — wave05

[Form4 candidata externa](R-021_Form4_semantic_admission_RC2.md) añade condiciones de semántica, disponibilidad histórica/PIT y costes; no admisión de fuente ni selección de proveedor. E3/F2 sólo fixtures/componentes; datos/historia/rights y target no probados. Las fuentes restantes conservan su prioridad/alcance, no exclusión general por este probe.
