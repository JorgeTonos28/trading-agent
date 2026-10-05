# R-020 / R-025 — DatasetAdmissibilityCard SEC/EDGAR RC0

2026-10-05. Candidato **de fuente** para Form4/13F y financial research, no proveedor/estrategia seleccionado. Revisión documental primaria; no scraping/API probe/dataset descargado/backtest. ADR-004/005 gobiernan.

## Hechos verificados

SEC ofrece submissions history/XBRL JSON sin autenticación/API key, actualizaciones conforme difusión y bulk nocturno. Submissions recent no contiene historia ilimitada: remite a ficheros adicionales. **Submissions discovery no equivale a transacciones Form4/13F normalizadas**: documentos/exhibits deben evaluarse aparte. [API pública](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).

SEC distingue acceptance, filed-as-of, change y period-of-report. Declara que **no hay timestamp que indique primera disponibilidad del contenido en sec.gov**; el lag habitual indicado no está garantizado. Por tanto `ACCEPTANCE-DATETIME` no prueba por sí solo `public_available_at` ni `received_at`. [FAQ/timestamps](https://www.sec.gov/about/webmaster-frequently-asked-questions).

Los archivos Feed/Oldloads permiten investigar submissions históricos con headers. Acceso automatizado exige user-agent declarado y fair access (límite actual10 requests/s, susceptible de ajuste). Eso es máximo publicado, no cuota que debamos consumir. No se inventó email/contacto del propietario para un bot. [Acceso EDGAR](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data).

## Campos de ficha y estado

| Dimensión | Evaluación RC0 |
|---|---|
| EXISTS / integración | YES, HTTP JSON/archivos públicos; no cuenta/API key para lectura de esos endpoints |
| AVAILABLE_TO_US | Docs YES; acceso programático concreto UNKNOWN hasta probe conforme política; sin bypass ante403 |
| TECHNICALLY_COMPATIBLE | Candidato WRAP/import de dataset determinístico; no MCP requerido para descargas offline antes de decisión |
| Historia / cobertura | Archivos públicos documentados; cobertura exacta Form4/13F, entidades/issuer mapping, amendments/confidential release, parseable formats y rangos por verificar |
| Clocks PIT | Economic event/period, acceptance, filed-as-of y change separados; public availability y delivery receipt no inventados. No usar transaction date como knowledge cutoff |
| Calidad | Clasificar transaction codes/nonmarket/derivative vs nonderivative, ownership, amended filings; 13F position reporting ≠ orden ejecutada. Semántica detallada aún por investigación, no parser construido |
| Latencia | Documentada variable/no SLA; acceptance clock no canal disponible. Bulk nocturno exige eligible_from del canal batch, no instante del header |
| Backtesting | **CONDITIONAL**: documentos/versiones pueden apoyar reconstrucción; historia de disponibilidad del canal elegido debe demostrarse o modelo conservador de fecha posterior declarado. No llamar PIT exacto a delay supuesto |
| Uso permitido inicial | Research/hipótesis/educación; no señal operacional hasta ADR-005 gates y reglas completas |
| SELECTED | NO; disposición propuesta **WRAP fuente oficial** + REFERENCE_ONLY si falla admisibilidad de familia; no BUILD proveedor antes de comparación |

## Plan de cierre sin mirar rendimiento

1. Mapear payloads/documentos/CIK/accessions/versiones para muestra pequeña Form4/13F, incluidos amendment y ausencia de data. Probe futuro con user-agent legítimo, rate bajo/cache, raw hashes y observación receipt; no escribir contactos privados en repo.
2. Verificar timezone/header semantics/canal histórico y diferencias de availability; construir `eligible_from` con evidencia, unknown explícito. Receipts prospectivos no reconstruyen primeros receipts de 2005.
3. Coverage/parse/revision quality y license para uso previsto frente a proveedores especializados R-025; cuantificar costo de extracción/normalización y mantenimiento, no elegir por gratis solamente.
4. Si falta timestamp histórico intradía, comparar canal EOD/batch conservador **como hipótesis**, con sensibilidad de retraso y sin cambiar clock por rentabilidad; evidencia insuficiente → no admitir estrategia que exija precisión ausente.
5. Construir ficha de dataset/precios/universo as-of antes de event-study/retorno y guardar exposure ledger. Operacionalización requiere riesgo/ejecución/datasets/governance separados.

PAPER_V1_VIABLE_FREE=CONDITIONAL a calidad/cobertura/clock; PAPER_V1_COST=0 acceso publicado, extracción/storage/tiempo por medir; LIVE_COST=0 acceso fuente pública + infraestructura/mantenimiento desconocidos por escala; FREE_ALTERNATIVE=SEC directo vs free tiers candidatos; PAID_INCREMENTAL_VALUE=normalización/canal timestamp/historia/cobertura/continuidad solo si proveedor lo demuestra; ECONOMIC_JUSTIFICATION_REQUIRED=YES antes de contratar. Ningún gasto/apertura de cuenta requerido para este review documental.
