# Secuencia para cerrar el Preparation Program

1. **A0–A1, ahora:** baseline, Plan Architect, diagnóstico, registros, dependencias y DoR desglosado. Confirmar identidad del dueño/aprobador. Salida de esta ejecución: `planning/` inicializado; aún no se declara `PLAN_UNDERSTOOD=TRUE` formal porque quedan ambigüedades P0.
2. **Mapa del Trading OS P0:** R-022 cierra funciones, ownership, fronteras y fases: investigar → datos → estrategias/backtest → señales → TradeIntent → riesgo → ejecución/reconciliación → monitoreo/desempeño → Champion/Challenger → pedagogía. R-019 suministra inspiración funcional del video y clasifica conservar/modificar/separar/descartar; sin auditoría de claims promocionales.
3. **Contratos financieros y de datos P0:** R-002/003/004/005 fijan riesgo, autoridad, órdenes, PIT y PAPER V1. R-023/021 definen taxonomía y disponibilidad temporal de señales externas; R-024 especifica Pedagogical Agent con trazas verificables y sin autoridad financiera. Revisar consistencia conjunta D-012–019.
4. **Build vs. Reuse y proveedores P1 desde ahora:** R-006 examina Skills/Plugins/Codex/MCP/Agents, Anthropic, otros labs, open source y quant. R-025 compara proveedores Smart Money **por dataset**; R-007 compara brokers, con Alpaca como candidato y elegibilidad RD/órdenes/security como gates. Ninguna plataforma se selecciona por el tutorial.
5. **Strategy V1 P0 sobre contratos comunes:** R-020 fija criterios antes de consultar resultados y compara variantes video primero, MATR_V1 y nuevos candidatos; R-001 caracteriza MATR. La selección/arquitectura final exige aprobación humana. No se fuerza una única estrategia a partir de piezas heterogéneas.
6. **Stack y operación P1:** R-008–R-014 validan market data, backtest, runtime, workflow, storage, seguridad, observabilidad, evals y pedagogía contra los contratos P0; scorecards/probes y ADRs. Decisiones de broker y datos materialmente costosos van al dueño.
7. **P2 con procedimiento:** definir en el Plan v1.0 cómo se calibrarán tipo de orden, stops y límites con paper/probes R-015; todo P2 debe estar resuelto o tener gate, responsable y evidencia explícitos antes del DoR. No se permite paper autónomo hasta cumplimiento.
8. **P3/P4 y freeze:** LIVE y búsqueda incremental de alpha quedan en R-016–018, con gates separados. Critic/Red Team de P0/P1, consistency y traceability checks, `MASTER_PLAN_RC1.md`, revisión del dueño, `MASTER_PLAN_v1.0.md` congelado y solo entonces `implementation_locked=false`.

**Regla de orden:** cerrar primero fronteras y contratos; investigar candidatos de proveedor en paralelo sin seleccionarlos antes del scorecard. Ningún resultado de plataforma modifica un invariante sin change record y aprobación correspondiente.

## Cola inmediata de decisiones P0/P1

| Orden | Decisión | Evidencia de cierre | Intervención humana |
|---|---|---|---|
| 1 — P0 | D-015/016/019 DECIDED con A+; D-018 sigue RESEARCHING | ADR-001 y contrato RC1; taxonomía y admisión PIT de señales externas en R-023/021 | Dueño aprobó alcance A+; ninguna fuente específica aprobada |
| 2 — P0 | D-012/013/014/017: riesgo, TradeIntent/órdenes, datos PIT y autonomía ante fallos | R-002/003/004/021: estados, secuencias de fallo, timestamps, controles y pruebas especificadas | Aprobación del dueño para política de riesgo y límites de autonomía |
| 3 — P1, investigación temprana | D-020/033/021: Build vs. Reuse, proveedores Smart Money y broker PAPER | R-006/025/007: documentación oficial, scorecards, elegibilidad RD, historia PIT, licencia, precio y probes | Broker y gasto material requieren aprobación; ningún candidato preseleccionado por el video |
| 4 — P0 | D-008/010/011: Strategy V1 y validación | R-019/020/001: variantes video separadas, MATR y otros candidatos, reglas falsables, protocolo OOS antes de resultados | Selección/arquitectura final aprobada por dueño |
| 5 — P1 | D-022–029: datos de mercado, backtest, runtime, workflow, storage, seguridad, pruebas y operación | R-008–014: benchmarks/probes, coste, threat model y criterios verificables | Seguridad material y datos costosos al dueño; resto por ADR técnico |

**Hito alcanzado 2026-10-01:** el propietario aprobó A+ en [ADR-001](decisions/ADR-001-paper-v1-authority.md) y [contrato PAPER V1 RC1](paper_v1_capability_contract_RC1.md). D-015/016/019 están `DECIDED`; D-018 sigue abierto. El siguiente bloque P0 es D-012/013/014/017: riesgo, órdenes, datos PIT e incidentes. R-026 detalla y evalúa el canal shadow como P1. R-023/R-025 y R-007 siguen abiertos sin selección ni gasto prematuro.
