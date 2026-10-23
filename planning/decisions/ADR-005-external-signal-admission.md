# ADR-005 — Roles y gates de admisión de señales externas

- **Fecha:** 2026-10-01.
- **Estado:** `DECIDED` por Plan Architect para D-018, como contrato abstracto coherente con las instrucciones explícitas del propietario; no se aprueba señal, Strategy V1 ni proveedor.
- **Prioridad:** P0.
- **Contrato:** [señales externas RC1](../06_external_signal_admission_RC1.md); datos PIT [ADR-004](ADR-004-point-in-time-data-lineage.md).

## Problema

La etiqueta “Smart Money” reúne hechos con distinto significado, retraso, historia y derechos. Un reporte congresual, Form 4, 13F, options flow y volumen ATS no pueden entrar en el mismo motor como si fueran transacciones instantáneas e interpretables. El video de origen los mezcla como ideas, pero el propietario ordenó separar las piezas y diseñar nuestro Trading OS sin seleccionar una fuente por inercia.

## Alternativas

| Alternativa | Beneficio | Problema |
|---|---|---|
| Elegir una plataforma/familia ahora | Reduce investigación inicial | Confunde cobertura comercial con calidad PIT y puede sesgar Strategy V1 |
| Permitir cualquier dato externo en Champion si pasa un parser | Flexibilidad aparente | No controla licencia, latencia, semántica ni aprobación humana |
| **Gates por dataset y roles graduados** | Mantiene arquitectura extensible y frontera financiera; permite comparar proveedores | Requiere fichas, probes y gobierno por fuente/regla |

## Evidencia y decisión

Fuentes primarias muestran retrasos distintos: [House Ethics](https://ethics.house.gov/periodic-transaction-report-calculator/) describe plazo de divulgación congresual; [SEC Form 4](https://www.sec.gov/files/form4.pdf) y [SEC 13F FAQ](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f) describen reportes con plazos diferentes; [FINRA](https://www.finra.org/filing-reporting/otc-transparency) publica estadísticas OTC con retraso. Son deadlines/productos, no prueba de primer acceso a cada observación. ADR-004 define el tiempo operable por canal.

Se adopta `RESEARCH_ONLY → CANDIDATE_SIGNAL → APPROVED_CHAMPION_INPUT` mediante gates semánticos, PIT, cobertura, licencia, hipótesis/OOS, operación y gobierno. `PEDAGOGICAL_CONTEXT` permite explicación factual sin causalidad inventada; `REJECTED_FOR_OPERATION` conserva la razón de exclusión. **Todas las familias empiezan como investigación**, no como señal aprobada. Un único Champion puede combinar familias si sus reglas/versiones se aprueban en D-008 y cada dataset pasa sus gates. Ningún agente ni proveedor crea `TradeIntent` o cambia capital, Champion o riesgo.

## Consecuencias

D-018 se cierra en arquitectura de roles/admisión. No se selecciona ninguna familia, proveedor, parser, Skill, plugin o MCP. R-021 y D-033/022 deben aportar pruebas por dataset antes de permitirle competir para V1; D-008 conserva la elección humana de estrategia. Cualquier ampliación de autoridad de señales externas fuera del Champion aprobado requiere nuevo registro/ADR. Capability Discovery Build-vs-Reuse continúa por fuente y componente; `implementation_locked=true`.
