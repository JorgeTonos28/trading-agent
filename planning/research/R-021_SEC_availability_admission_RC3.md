# R-021 — canal SEC, revisiones e histórico admisible RC3

2026-10-14. Form4 primera externa candidata, no dataset/provider seleccionado. Investigación documental primaria, sin filings/precios descargados, contacto ni headers ficticios. E1/F2 offline no prueban disponibilidad histórica.

## Evidencia primaria

[SEC access](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data): índices se construyen por la noche; ownership3/4/5 tiene regla de cutoff distinta. Correcciones/eliminaciones posteriores pueden no reflejarse en índices diarios antiguos, mientras full/quarterly se reconstruyen semanalmente. Índice enumera filing date/path/CIK, no un recibo de nuestro canal. [Developer](https://www.sec.gov/about/developer-resources) ofrece archivos/daily feeds/oldloads y acceso moderado; requiere identidad legítima para automatización, no contacto inventado. La política observada limita10requests/s agregados; no objetivo a saturar.

Inferencia del proyecto: **un índice trimestral actual no es snapshot PIT histórico intacto**, daily index tampoco certifica contenido actual original/complete delivery. Header acceptance, public dissemination, index build y first successful receipt son clocks distintos. Guardar scope/canal/fuente y cota de disponibilidad sustentada; un lag arbitrario no repara historia desconocida.

## Admission matrix

| Gate | Evidencia requerida | Estado actual |
|---|---|---|
| A3-01 universe/coverage | Enumeración Form4/4A por período, filtros previos y manifests; actuales no sustituyen eliminados | NOT_TESTED |
| A3-02 original/version | Raw/hash/version/header/exhibits, vínculos PAC/amendment y disponibilidad | NOT_TESTED |
| A3-03 canal | First-public/receipt o intervalo defendible del canal realmente usado; precisión/zona/DST/calendario | NOT_TESTED |
| A3-04 corrections | Vista sólo efectiva desde nueva availability, no backfill que modifica lo conocido antes | NOT_TESTED |
| A3-05 semantic | Plan/purchase/owners/rows UNKNOWN explícitos, versiones históricas, campos/clasificadores preregistrados | PARTIAL_OFFLINE |
| A3-06 mapping | Issuer/security/delisted/owner y dedup histórico, no ticker actual asignado a todo pasado | NOT_TESTED |
| A3-07 rights | Automatización/retención/redistribución/LLM export permitidos por origen y uso; filings públicos no licencia universal de vendors | DOCUMENTARY_PARTIAL |
| A3-08 prices | Cobertura/marks/corporate events del universo dinámico, benchmark propio y coste/delay | NOT_TESTED |

Public filings pueden documentar inspiración/research sin cumplir señal confirmatoria. Para2019–2022 el filtro de planes sigue UNKNOWN cuando no hay evidencia por fila, no se borra requisito. S-F4-PLANAGNOSTIC-00 continúa hipótesis separada no ejecutada; no waiver PIT ni selección. Actual provider/channel vendors necesitan scorecard y muestra comparable, no precisión asumida por campo namedtimestamp.

## Ruta y economía

Primero preparar fixtures versionados de amendment/PAC/date-only/duplicados/owners y mapping; una futura muestra histórica pequeña sólo en research declarado anterior a reserva, con acceso legítimo y fuente admitida. No abrir2023+ para escoger hipótesis. Contacto requerido para probes automatizados queda fuera de Git/secretlogs y se guía cuando realmente sea siguiente acción; trabajo documental no se bloquea ahora.

SEC/direct source EXISTS=YES/docs disponibles; datahistory/admission CONDITIONAL, SELECTED=NO, WRAP canal + ADAPT normalización candidata. PAPER_V1_VIABLE_FREE=CONDITIONAL, PAPER_V1_COST=acceso0+normalización/storage/operación UNKNOWN, LIVE_COST=volumen/continuidad UNKNOWN, FREE_ALTERNATIVE=fuentes primarias/versionadas y OSS, PAID_INCREMENTAL_VALUE=firstdelivery/history/mapping/coverage sólo si demostrado, ECONOMIC_JUSTIFICATION_REQUIRED=antes de gasto. No nuevo MCP/runtime, autoridad financiera ni contratación.
