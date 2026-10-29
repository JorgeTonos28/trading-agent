# R-021/R-025 — admisión de datos externos y normalización reusable — RC1

2026-10-13 · P0/P1 D-008/011/022/033 · Documentary research, SELECTED=NO. Financial data layer, fuera de restricción de frameworks agénticos; no activar MCP/Skills de terceros ni reabrir R-006. Source metadata ≠ derecho de uso ni PIT validado.

## Semántica primaria que cambia las reglas

| Fuente | Hecho de fuente primaria | Consecuencia de diseño, propuesta del proyecto |
|---|---|---|
| Form4 | Código P incluye compra en exchange **o a otra persona**; F pago fiscal/exercise y M exercise/conversion son distintos. Filing puede contener equity y derivados. [Investor.gov](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69) | No convertir todo P en open-market conviction, ni cantidad positiva en compra. Registrar purchase_class/plan/footnotes/ownership y UNKNOWN; filtro explícito preregistrado por hipótesis |
| 13F | Holdings de clases reportables; excluye shorts, admite tratamiento confidencial. Valores cambian unidades de reporte tras reforma2023. [SEC FAQ](https://www.sec.gov/rules-regulations/staff-guidance/frequently-asked-questions-about-form-13f) | Holdings no son cartera completa/hedge ni trade timing. Normalizar unidades por versión; ausencia/amendment/confidential release no se transforma automáticamente en venta o cero |
| Congress | Rangos/importes/fechas y actores, según documento/fuente; historia/rights actuales incompletos | Lista de actores ex ante; no seleccionar por resultado. Event amount range no sizing de nuestra cuenta; ETF/option/asset ambiguous mantiene UNKNOWN |
| Filings/aggregator | SEC no acredita first-public timestamp; Quiver schema declara clocks sin prueba de valores/history. [Card SEC](R-020_SEC_dataset_admissibility_RC0.md), [wave01](R-025_provider_evidence_wave01_2026-10-07.md) | acceptance/transaction/report/uploaded separados. No sustituir por timestamp más temprano porque mejora resultados |

## Contrato as-of y revisión

Unidad source_event = documento + versión + fila/identificador + issuer/instrument + reporting owner(s). Múltiples owners del mismo hecho no se cuentan como compras independientes; dedup-key y límites son predefinidos, UNKNOWN joint mapping evita cluster artificial. Corrección pública crea evento nuevo con effective_from de su availability, conservando la vista anterior; snapshot anterior no se reescribe.

`eligible_from` exige evidencia del canal usado y regla de disponibilidad. Si precisión date-only, no inventar medianoche: zona/fin del intervalo de incertidumbre y siguiente sesión permitida conservadores documentados, **sin garantía PIT exacta**. Si no existe cota defendible, no admitir dataset como señal confirmatoria; puede servir a research/reference. Lag sensitivity es prueba de fragilidad, no reconstrucción de historia desconocida. Un receipt prospectivo no revela qué estaba disponible en2005.

Raw documento/hash/path públicamente referenciable, transform/version, clocks, security mapping as-of, unidades/moneda, revisions y exclusiones se conservan. Current-ticker/company metadata no reescribe instrumentos del pasado; delisted/missing prices no se eliminan para mejorar retorno. Security identifier ambiguo => QUARANTINED, no resolución por LLM. Source/canal completo requerido antes de inferir ausencia de compras/ventas.

## Build-vs-Reuse — candidato E-SEC-01 EdgarTools

[Repositorio](https://github.com/dgunning/edgartools), [MIT license](https://raw.githubusercontent.com/dgunning/edgartools/main/LICENSE.txt), [Form4 docs](https://edgartools.readthedocs.io/en/latest/insider-filings/). Biblioteca pública propone objetos/filas estructuradas Form4 y13F, footnotes y planes. **EXISTS=YES; AVAILABLE_TO_US=public-source YES / SEC-data CONDITIONAL; TECHNICALLY_COMPATIBLE=CONDITIONAL; ECONOMICALLY_REASONABLE=UNKNOWN esfuerzo; SELECTED=NO.** ADAPT/WRAP candidato para normalizador de datos, REFERENCE_ONLY hasta probe; no construir parser general primero. No seleccionar MCP/workflow/agent templates anunciados en el repo.

Probe prioritario preparado: pin release/commit, fixture XML sintético y filas esperadas (P privado vs exchange/no evidencia, F/M, joint owners, derivative, amendment, datos desconocidos), sin llamadas SEC ni contacto falso. Parser output se compara con fuente/nuestras reglas; una tabla limpia no resuelve availability. Luego muestra primaria-vendor histórica con user-agent legítimo/local-contact privado y rights, en entorno autorizado. No instalado ni probado el parser en esta wave, ni reclamada accuracy/coverage automática.

| Candidato | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| EdgarTools + SEC | CONDITIONAL a parse/rights/clocks/dataset | License US$0; fixed/variable hardware/maintenance/storage UNKNOWN | Misma fuente/license US$0 + operación/escala UNKNOWN | Archivos SEC + otros OSS a comparar, no BUILD default | Vendor/canal con historia/normalización/continuidad mejor demostrada | YES antes de gastar; NO gasto por solo leer source público |

Escenario mensual: un investigador, lotes EOD y caching; volumen todavía UNKNOWN, no inventar coste total0. Dependencia formatos/API/library y mappings, salida raw/documents+versioned transforms; costo de migración por medir. Servicios de consultoría/MCP/premium no incluidos. Paid vendors pueden justificar calidad pero no están aprobados.

## Próximos gates independientes de IA

1. Fichas dataset/rights por familia y clocks por canal; comparar vendors especializados revisions/flows/options/blocks sin proveedor único.
2. Probe normalizador offline con pin/fixture (sin datos reales/retorno), después cobertura/revisiones/primary-vendor.
3. Dataset de precios y benchmark compatibles, granularidad/acciones corporativas y engine paridad.
4. Regla/actor/threshold/decay/config y OOS pre-registrados; admission ADR-005 y Strategy selection D-008 con owner. Ningún proveedor seleccionado por fecha declarada ni gratuitidad.

## Evidencia posterior E1 — 2026-10-13

[Probe offline pin5.62.0](R-021_edgartools_findings_2026-10-13.md) ejecutado:7/7checks de tablas sintéticas, factory completo ERROR/IdentityNotSetError. P privado permanece market_trades; form/clase de tabla son caller-supplied. TECHNICALLY_COMPATIBLE=PARTIAL, ADAPT/WRAP candidato, SELECTED=NO. Software público probado parcialmente, no extracción histórica/ownership/PIT/rights admitidos. La nota anterior «no instalado ni probado» describe la wave documental previa. Footnotes completas, plan trivaluado, mappings as-of/amendments y canal/receipts siguen pendientes.

## Semántica Form4 posterior — wave05

[Semántica Form4 posterior](R-021_Form4_semantic_admission_RC2.md) añade condiciones de semántica, disponibilidad histórica/PIT y costes; no admisión de fuente ni selección de proveedor. E3/F2 sólo fixtures/componentes; datos/historia/rights y target no probados. Las fuentes restantes conservan su prioridad/alcance, no exclusión general por este probe.

## Canal SEC y revisiones — wave06

[Canal SEC y revisiones](R-021_SEC_availability_admission_RC3.md) añade especificación y límites; Q057 aprobado en paquete, Q058 números propuestos. Sin fuente/modelo/Strategy admitidos ni performance. E4 sólo cálculo/meanpilot, no cobertura CAGR/ES/DD; M11 parcial/holdoutUNKNOWN. Versiones/declaraciones anteriores conservadas, no rehash histórico.

## Avance técnico posterior — wave07

[R-020_dataset_cards_RC0.md](R-020_dataset_cards_RC0.md) especifica propuestas/gates, no método/dataset/Strategy admitidos. M1 aprobado/ADR019; Q059 guardrails distintas propuestas. E5/E6screens no statisticalacceptance, costos/scale/fuente/financialtarget pendientes. Versiones anteriores conservadas; no benchmark/margen cambiados por resultados.
