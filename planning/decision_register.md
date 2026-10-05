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
| D-012 | Arquitectura conceptual de riesgo compuesto para PAPER V1 | P0 | DECIDED | Propietario aprobó opción B el 2026-10-01 en ADR-006: mínimo entre exposición/cash, stop estimado, gap/slippage, liquidez y reservas; fórmulas D-035, umbrales/escenarios D-031 y detalles D-021/026/030 abiertos |
| D-013 | Contrato abstracto de órdenes, `TradeIntent`, autorización, idempotencia y reconciliación | P0 | DECIDED | ADR-003 y `04_order_contract_RC1.md`: identidad interna, eventos, `UNKNOWN`, G2; mapeo broker D-021, pruebas D-030/031 |
| D-014 | Semántica abstracta de datos y linaje PIT: clocks, revisiones, ajustes as-of y snapshots | P0 | DECIDED | ADR-004 y `05_data_contract_RC1.md`; pruebas/delays por dataset/proveedor siguen R-021/D-022/D-033 |
| D-015 | Límites de componentes y autoridad; papel de Portfolio Manager, Signal y Execution | P0 | DECIDED | ADR-001 aprobado por el propietario 2026-10-01: A+; Champion/intent determinísticos, Portfolio Manager Agent SHADOW sin ruta operativa |
| D-016 | Alcance exacto PAPER V1 y gates de aceptación frente a fases B0–B7 | P0 | DECIDED | ADR-001 y contrato RC1: un Champion operativo puede combinar fuentes/señales; shadow y explicación factual desde B4, pedagogía completa antes de DoD |
| D-017 | Fronteras de autonomía PAPER V1 ante incidentes | P0 | DECIDED | Propietario aprobó G1+G2 y reanudación humana tras pausa material el 2026-10-01; ADR-002; G3/liquidación general no autorizados; umbrales D-031 abiertos |
| D-018 | Roles y gates abstractos de Smart Money/señales externas en Research/Strategy/Pedagogical | P0 | DECIDED | ADR-005 y `06_external_signal_admission_RC1.md`; ninguna familia/dataset admitido automáticamente, PIT/selección concreta D-008/022/033 |
| D-019 | Contrato del Pedagogical Agent y aprendizaje sin alterar Champion | P0 | DECIDED | ADR-001 aprobado: factual desde B4 y completo antes de DoD, sin autoridad financiera; formato/evals P1 pendientes |
| D-020 | Stack de capacidades, licencias y clasificación Build vs. Reuse | P0 | RESEARCHING | ADR-007: IA/agentes OpenAI + Anthropic y **Plus individual objetivo**; Team solo investigación. ADR-008: Tier 0/1 primero PAPER, pagos investigables y posibles en LIVE con valor probado; aprobación antes de gastar. Waves 04/05 Team ejecutadas, shortlist RC0 condicional; gap tipos/linaje/repetibilidad y Plus Acceptance de finalistas. Sin cierre/selección. Gate D-024: madurez final, revisión/gobierno |
| D-021 | Broker PAPER y elegibilidad real para residente de RD | P1 | OPEN | Gates B1–B5, pruebas API y aprobación humana |
| D-022 | Proveedor de históricos y datos para candidatos Strategy V1; validador secundario | P1 | OPEN | Cobertura, PIT, ajustes, licencia, coste y benchmark |
| D-023 | Motor(es) de investigación/backtest event-driven | P1 | OPEN | Comparativa y replay mínimo contra D-008/011 |
| D-024 | Runtime de Plan Architect/agentes y diseño del Trading OS Plugin | P1 | OPEN | **BLOQUEADO por madurez R-006/D-020** bajo alcance/coste ADR-007; no cerrar/freeze de runtime, topología, Skills, plugins, MCP, subagentes o plugin final antes de scorecards y probes; decisión material reservada a gobierno humano |
| D-025 | Workflow durable, scheduler y política de recuperación | P1 | OPEN | Fallos, persistencia, complejidad y benchmark |
| D-026 | Almacenamiento, eventos, identidad/versionado y audit trail | P1 | OPEN | Esquemas, retención, replay y recuperación |
| D-027 | Modelo de seguridad: secretos, entornos, permisos, supply chain, prompt injection | P1 | OPEN | Threat model y aprobación humana de arquitectura material |
| D-028 | Observabilidad, alertas, runbooks, backups y despliegue PAPER | P1 | OPEN | SLO/criterios y pruebas de recuperación |
| D-029 | Estrategia de tests y evals de agentes con criterios de aceptación | P1 | OPEN | Cobertura de invariantes y fallos, reviewer independiente |
| D-034 | Esquema detallado, aislamiento y evaluación PIT de `ShadowPortfolioProposal` | P1 | OPEN | ADR-001 fija obligación funcional; R-026 define comparador, métricas preregistradas, contexto pareado y pruebas de no autoridad; waves 04/05 exigen enums, trusted role, quantity semantics y OBSERVED/DERIVED. Probe sintético no cierra evaluación |
| D-035 | Especificación técnica verificable de controles de riesgo compuestos | P1 | OPEN | R-027: fórmulas, unidades, precedencia, redondeo, estado/reservas y casos límite conforme a ADR-006; sin fijar umbrales numéricos D-031 |
| D-036 | Política económica por fase y adquisición de Skills/metodologías | P0 | DECIDED | Propietario, 2026-10-02, ADR-008: calidad/fiabilidad/capacidad al menor coste razonable; PAPER zero/low incremental cost first, LIVE economic value/unit economics; Skills/templates gratuitos/incluidos/propios; pagos investigables, aprobación explícita antes de contratar o gastar |
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

Una decisión abierta pasa a `RESEARCHING` al iniciarse una tarea R; a `READY_FOR_DECISION` cuando hay comparativa, evidencia, riesgos y recomendación; a `DECIDED` tras registrar resultado, aprobador y ADR cuando corresponda. El dueño aprobó D-012 **solo en arquitectura conceptual** y D-017 en frontera G1+G2; debe aprobar D-008 (selección y arquitectura final de estrategia), D-021, D-027, parámetros materiales de D-031 y cualquier gasto material o cambio de alcance. La priorización P1 de broker PAPER concilia el gate de diseño dependiente del broker de §3.8 con la lista P2 de §3.9: el **contrato abstracto** es P0 (D-013), la **selección concreta** es P1 porque el DoR exige stack y arquitectura completos; la prueba operativa pertenece a P2 (D-030).

**Aclaración de proceso 2026-10-05 (ADR-007):** propietario autoriza probes conductuales Team y shortlist sin acceso Plus; aceptación posterior específica para finalistas. Alternativa determinístico/local always-on + Codex intermitente explícitamente OPEN. D-020 `RESEARCHING`; D-024 `OPEN`; ninguna capability seleccionada.

**Hito R-006 2026-10-05:** [wave 04](research/R-006_probe_wave_04_2026-10-05.md), [wave 05](research/R-006_probe_wave_05_2026-10-05.md) y [shortlist RC0](research/R-006_shortlist_RC0.md) incorporan evidencia Team y recomendaciones Build-vs-Reuse. No cambia estado D-020/D-024, ni A+/G1+G2/riesgo conceptual, broker, Strategy V1 o umbrales. Plus gate reservado a finalistas.
