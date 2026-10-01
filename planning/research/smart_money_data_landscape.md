# R-023/R-025 — Smart Money y proveedores de datos alternativos

**Fecha:** 2026-10-01. **Estado:** RESEARCHING. **Prioridades:** contrato de señales P0 (R-023); comparación de proveedores P1 (R-025). **Decisiones:** D-014, D-018 y D-033. Ninguna familia de señales ni proveedor está seleccionado. «Smart Money» es una etiqueta de investigación, **no una señal homogénea ni sinónimo de operaciones congresuales**.

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

El resultado puede ser **varios proveedores especializados** o fuentes oficiales más normalización propia. Cada dataset recibirá disposición `REUSE_AS_IS / ADAPT / PORT / WRAP / REFERENCE_ONLY / BUILD / REJECT`, con criterio y coste. La elección de una fuente con gasto material requiere aprobación humana.

## Orden de probes (desechables, sin Trading OS)

1. Recolectar documentación, contrato y precio oficial de cada candidato.
2. Construir muestra pequeña de eventos equivalentes entre fuente oficial y agregadores; comparar campos y fechas, sin credenciales ni suscripción todavía.
3. Verificar que el histórico conserva el primer momento público y no solo el estado actual enriquecido.
4. Medir cobertura/latencia y estimar esfuerzo de integración; decidir qué familias son factibles para V1, research-only o futuras.

**Gate:** D-018 define el papel de señales externas y contrato PIT; D-033 selecciona proveedor(es) solo después del scorecard, o deja una familia diferida con razón explícita. No se requiere demostrar o refutar las cifras del video.
