# Decision Register — inicialización

Fecha: 2026-10-01. Fuente base: [hoja de ruta v0.2](../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md). `DECIDED` significa que la hoja fija el principio; no implica que su implementación esté especificada. Los candidatos nombrados por la hoja siguen abiertos. Estados: `OPEN`, `RESEARCHING`, `READY_FOR_DECISION`, `DECIDED`, `DEFERRED`, `SUPERSEDED`. P0/P1 bloquean el Plan v1.0.

| ID | Decisión y estado actual | Prioridad | Estado | Cierre / autoridad |
|---|---|---|---|---|
| D-001 | Preparation Program, DoR y bloqueo de implementación | P0 | DECIDED | Hoja §3, §56; dueño aprueba freeze |
| D-002 | Invariante TradeIntent → riesgo determinístico → ejecución → broker | P0 | DECIDED | Hoja §2, §7; cualquier cambio requiere aprobación humana |
| D-003 | Primera versión operativa PAPER; LIVE por gate separado | P0 | DECIDED | Hoja §0, §24–25; LIVE requiere aprobación |
| D-004 | Autonomía por operación dentro de estrategia y límites aprobados | P0 | DECIDED | Hoja §5; incidentes PAPER V1 delimitados en ADR-002/D-017 |
| D-005 | Research separado de Champion; promoción humana | P0 | DECIDED | Hoja §2, §26 |
| D-006 | MATR_V1 como primera estrategia/Champion experimental | P0 | SUPERSEDED | ADR-000: era una hipótesis del borrador; propietario reabrió selección el 2026-10-01 |
| D-007 | Capa Trading OS Plugin propia sujeta a Build vs. Reuse | P1 | DECIDED | Hoja §3.14, §9; formato y contenido abiertos en D-024 |
| D-008 | **Strategy V1 Selection**: variantes inspiradas en el video primero, MATR_V1 y otros candidatos justificados | P0 | OPEN | Comparación preregistrada, evidencia y aprobación humana; la primera descomposición no implica selección |
| D-009 | Extracción funcional del video: capacidades, mecanismos, estrategias y pedagogía | P0 | RESEARCHING | Transcripción primaria revisada; cerrar con mapa conservar/modificar/separar/descartar, sin auditar claims promocionales salvo necesidad decisoria |
| D-010 | Especificación de MATR_V1 como candidato/benchmark | P0 | RESEARCHING | RC0 en `02_MATR_V1_spec.md`; no es contrato de implementación salvo selección D-008 |
| D-011 | Metodología de backtest: datos point-in-time, OOS, costes, benchmark, sesgos | P0 | RESEARCHING | RC0 en `02_MATR_V1_spec.md`; protocolo reproducible y revisión crítica |
| D-012 | Arquitectura de riesgo: precedencia de reglas, estados, reserva de presupuesto, protección y acciones ante fallos | P0 | RESEARCHING | `03_risk_policy_RC1.md`; D-017 fija solo frontera G1+G2; falta calibración/escenarios y aprobación humana de política material |
| D-013 | Contratos de órdenes, `TradeIntent`, autorización, idempotencia y reconciliación | P0 | RESEARCHING | `04_order_contract_RC0.md`; falta máquina formal, broker semantics y pruebas de fallos |
| D-014 | Contrato de datos y linaje: timestamps, ajustes, corporate actions, snapshots | P0 | RESEARCHING | `05_data_contract_RC0.md`; falta resolver clocks, proveedores y muestras PIT |
| D-015 | Límites de componentes y autoridad; papel de Portfolio Manager, Signal y Execution | P0 | DECIDED | ADR-001 aprobado por el propietario 2026-10-01: A+; Champion/intent determinísticos, Portfolio Manager Agent SHADOW sin ruta operativa |
| D-016 | Alcance exacto PAPER V1 y gates de aceptación frente a fases B0–B7 | P0 | DECIDED | ADR-001 y contrato RC1: un Champion operativo puede combinar fuentes/señales; shadow y explicación factual desde B4, pedagogía completa antes de DoD |
| D-017 | Fronteras de autonomía PAPER V1 ante incidentes | P0 | DECIDED | Propietario aprobó G1+G2 y reanudación humana tras pausa material el 2026-10-01; ADR-002; G3/liquidación general no autorizados; umbrales D-012/031 abiertos |
| D-018 | Papel de Smart Money y señales externas en Research/Strategy/Pedagogical, con contrato PIT y admisión | P0 | RESEARCHING | R-023; Congreso, Form 4, 13F, options flow, dark pool, revisions, flows y otros separados |
| D-019 | Contrato del Pedagogical Agent y aprendizaje sin alterar Champion | P0 | DECIDED | ADR-001 aprobado: factual desde B4 y completo antes de DoD, sin autoridad financiera; formato/evals P1 pendientes |
| D-020 | Stack de capacidades, licencias y clasificación Build vs. Reuse | P1 | RESEARCHING | Fichas C-001–009 y contrato RC0 §7; faltan landscape completo, scorecards y decisión por capacidad |
| D-021 | Broker PAPER y elegibilidad real para residente de RD | P1 | OPEN | Gates B1–B5, pruebas API y aprobación humana |
| D-022 | Proveedor de históricos y datos para candidatos Strategy V1; validador secundario | P1 | OPEN | Cobertura, PIT, ajustes, licencia, coste y benchmark |
| D-023 | Motor(es) de investigación/backtest event-driven | P1 | OPEN | Comparativa y replay mínimo contra D-008/011 |
| D-024 | Runtime de Plan Architect/agentes y diseño del Trading OS Plugin | P1 | OPEN | Capacidades, permisos, portabilidad, evals y coste |
| D-025 | Workflow durable, scheduler y política de recuperación | P1 | OPEN | Fallos, persistencia, complejidad y benchmark |
| D-026 | Almacenamiento, eventos, identidad/versionado y audit trail | P1 | OPEN | Esquemas, retención, replay y recuperación |
| D-027 | Modelo de seguridad: secretos, entornos, permisos, supply chain, prompt injection | P1 | OPEN | Threat model y aprobación humana de arquitectura material |
| D-028 | Observabilidad, alertas, runbooks, backups y despliegue PAPER | P1 | OPEN | SLO/criterios y pruebas de recuperación |
| D-029 | Estrategia de tests y evals de agentes con criterios de aceptación | P1 | OPEN | Cobertura de invariantes y fallos, reviewer independiente |
| D-034 | Esquema detallado, aislamiento y evaluación PIT de `ShadowPortfolioProposal` | P1 | OPEN | ADR-001 fija obligación funcional; R-026 define comparador, métricas preregistradas, contexto pareado y pruebas de no autoridad |
| D-033 | Proveedores Smart Money/alternative data y clasificación Build vs. Reuse por dataset | P1 | RESEARCHING | R-025; scorecards PIT, API, cobertura, calidad, latencia, licencia y coste; aprobación humana si gasto material |
| D-030 | Ejecución PAPER concreta: tipo de orden, stops, slippage y fill parity | P2 | OPEN | Protocolo antes de paper autónomo; decisión puede afectar D-010/011 |
| D-031 | Umbrales PAPER calibrados y kill switches ensayados | P2 | OPEN | Evidencia backtest/paper y aprobación humana de política |
| D-032 | Ventana y reglas de promoción desde replay a paper autónomo | P2 | OPEN | Métricas, incidentes y procedimiento explícito en DoR |
| D-040 | Broker LIVE, elegibilidad/custodia/funding y permisos | P3 | DEFERRED | Gate LIVE, pruebas y aprobación humana |
| D-041 | Capital live, riesgo live, fiscalidad y obligaciones RD/EE.UU. | P3 | DEFERRED | Asesoramiento competente y aprobación humana antes de LIVE |
| D-042 | SLO, disaster recovery y criterios paper→shadow→live | P3 | DEFERRED | Evidencia operacional y aprobación humana |
| D-050 | Alpha incremental y nuevos Challengers sobre datos alternativos tras alcance V1 | P4 | DEFERRED | No sustituye D-018/D-033: taxonomía, PIT y selección de fuentes V1 son P0/P1 |
| D-051 | Opciones, shorts, leverage, futuros, cripto y regímenes avanzados | P4 | DEFERRED | Cambio de alcance y aprobación humana futura |

## Reglas de cierre

Una decisión abierta pasa a `RESEARCHING` al iniciarse una tarea R; a `READY_FOR_DECISION` cuando hay comparativa, evidencia, riesgos y recomendación; a `DECIDED` tras registrar resultado, aprobador y ADR cuando corresponda. El dueño debe aprobar D-008 (selección y arquitectura final de estrategia), D-012, D-017, D-021, D-027 y cualquier gasto material o cambio de alcance. La priorización P1 de broker PAPER concilia el gate de diseño dependiente del broker de §3.8 con la lista P2 de §3.9: el **contrato abstracto** es P0 (D-013), la **selección concreta** es P1 porque el DoR exige stack y arquitectura completos; la prueba operativa pertenece a P2 (D-030).
