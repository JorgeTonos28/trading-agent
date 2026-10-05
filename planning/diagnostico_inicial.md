# Diagnóstico integral de la hoja v0.2

**Vigencia actual — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Fecha inicial: 2026-10-01. Actualizado 2026-10-01 con la orientación funcional del propietario y un inventario preliminar de proveedores desde páginas oficiales; los datos comerciales/técnicos aún requieren fichas y probes. Los registros enlazados enumeran decisiones ([D](decision_register.md)), preguntas ([Q](open_questions.md)), investigación ([R](research_backlog.md)), supuestos ([A](assumptions.md)) y riesgos ([K](risk_register.md)).

## Estado

La hoja fija bien el propósito de **sistema agéntico de trading** (investigación, fuentes, estrategias, riesgo, ejecución, monitoreo, Champion/Challenger y enseñanza), el invariante de autoridad financiera, primera operación PAPER, controles humanos, versionado, auditabilidad y un DoR amplio. Por corrección explícita del propietario (ADR-000), **Strategy V1 Selection está OPEN (P0)**: el video es el primer referente que descomponemos, MATR_V1 sigue candidato/benchmark. Ningún broker, data vendor, motor, runtime, plugin externo o arquitectura final de estrategia ha sido seleccionado. El DoR no se cumple: todos los P0/P1 abiertos del registro requieren cierre. `implementation_locked=true`.

## Hallazgos estructurales

| Área | Fortaleza del borrador | Brecha que impide contrato de implementación |
|---|---|---|
| Cuant/estrategia | MATR candidata con reglas simples; benchmarks, stress y forward paper | Video descompuesto funcionalmente, pero ninguna variante seleccionada ni completa; MATR requiere convenciones y política OOS comparativa; D-008–011 |
| Riesgo | Motor determinístico y límites PAPER tentativos | Semántica de presupuesto con gaps, reserva entre intents, estados soft/hard, acción de kill-switch y reanudación; D-012/017 |
| Ejecución | TradeIntent, IDs, reconciliación planteados | Contratos versionados, autorización vinculante, fill/event ordering, timeout y recuperación, ownership de decisiones; D-013/015 |
| Datos | PIT y lineage son principios explícitos | Qué instante se considera disponible; ajustes/corporate actions; snapshots, revisiones y permisos; D-014/022 |
| Plataformas | Candidatos y gates de broker/data descritos | Elegibilidad del perfil real, coste/licencias actuales, probes, scorecards y ADR; D-021/022/023 |
| Agentes/capacidades | Separación conceptual de Skills/tools/risk | Inventario de disponibilidad real, licencias, permisos, runtime y evals; D-020/024 |
| Smart Money | Fuentes alternativas mencionadas | Taxonomía/roles/gates abstractos cerrados en ADR-005; proveedores especializados, PIT y utilidad por dataset siguen D-022/033/R-021; Congreso no es sinónimo |
| Pedagogía | §55 propone currículo y V1 exige explicación de cada operación | Contrato de evidencia, niveles, incertidumbre y límites del Pedagogical Agent; D-019 |
| Operaciones/seguridad | Secretos, idempotencia, runbooks y chaos nombrados | Threat model, SLO, restore, incident actions, aceptación verificable; D-027/028/029 |
| Alcance | Fases A/B y DoR descritos | PAPER V1 frente a componentes B5–B7 y Definition of Done no tienen trazabilidad completa; D-016 |

## Tensiones y contradicciones a resolver

1. **Ruta y ubicación canónica:** la primera lectura detectó que `AGENTS.md` apuntaba a un roadmap inexistente y exigía `.project/`, mientras la hoja propone `planning/`. Por instrucción posterior del propietario se corrigió `AGENTS.md` y se trasladó el estado a `planning/`; Q-028/029 quedaron resueltas. Los nombres sin prefijo siguen el ejemplo de §3.5; §3.23 permite que cambien los nombres sin omitir contenido.
2. **Prioridad del paper broker:** §3.8 lo llama P0, §3.9 P2, §63 lo pone primero. Se separó el contrato de ejecución P0, selección concreta P1 (DoR exige stack), validación PAPER P2. No cambia el requisito funcional.
3. **Holdout “sealed”:** el propietario confirmó que nadie ha ejecutado ni visto resultados de MATR_V1. Eso elimina una fuente concreta de contaminación previa, pero la selección entre varios candidatos puede introducir sesgo si se consultan resultados reservados antes de fijar criterios; R-020/001 deben preregistrar comparación y forward test.
4. **Stop y pérdida presupuestada:** §18 asocia 3×ATR con 0.5% de equity, pero una orden stop no garantiza ejecución al stop ante gaps. Risk policy debe expresar pérdida estimada frente a peor caso y prohibir promesa implícita de límite duro.
5. **Autonomía de cierre (resuelto en autoridad PAPER V1 el 2026-10-01):** §5 permite liquidar con kill switch; §11 advierte que `CLOSE_ALL` puede agravar incidentes. ADR-002 aprueba G1+G2 y reanudación humana tras pausa material; G3/liquidación automática general no autorizados. Faltan clasificación detallada, runbooks y pruebas D-012/013/028/031.
6. **Responsabilidad duplicada:** Portfolio Manager Agent “decide prioridades”, Signal Engine produce señales, Risk Engine puede reducir notional y Execution Engine traduce órdenes. Faltan límites precisos sobre quién altera el plan/qty y cómo se versiona la aprobación.
7. **Alcance versus fase:** §8.6 dice construir Regime Detection desde el principio; §18 lo excluye como ajuste de V1; §56 coloca agentes/plugin en B5 tras PAPER autónomo B4, mientras §57 requiere reporte pedagógico para terminar PAPER V1. D-016 debe fijar qué piezas son requisito de V1 y cuáles son observación o fase posterior.
8. **Datos y fill model:** señal al cierre t y ejecución siguiente sesión son correctos en principio, pero una fuente de datos ajustada retroactivamente y calendario/corporate actions sin definición pueden generar look-ahead; D-014/030.
9. **Criterios vagos:** “suficiente número de observaciones”, “forward paper consistente”, “estabilidad”, “cero incidentes críticos” y “costos razonables” necesitan umbrales o procedimiento de aceptación definidos antes de test.
10. **Arquitectura tecnológica tentantiva:** Python, Agents SDK, Temporal, Postgres, Redis, LEAN/Nautilus y proveedores son hipótesis (§62), no decisiones. Build vs. Reuse debe preceder ADRs tecnológicos.

## Dependencias principales

```text
Mapa de sistema (D-015/016/018/019) ──> contratos de datos, agentes y pedagogía
Video descompuesto + MATR + criterios (D-008/009/010/011)
                                ├─> requisitos de datos (D-014/022/033)
                                ├─> motor de backtest (D-023)
                                └─> orden/fill PAPER (D-030)
Risk + autoridad (D-012/017) ──┬─> TradeIntent/reconciliación (D-013)
                                └─> broker API/seguridad (D-021/027)
Capability discovery (D-020) ──┬─> agentes/plugin (D-024)
                                └─> motores/workflow/storage (D-023/025/026)
Todo P0/P1 + revisión crítica ─────> DoR → RC1 → aprobación/freeze → implementación
```

No hay dependencia circular necesaria si los **contratos funcionales** se definen antes de seleccionar implementaciones y se validan con probes. La selección de broker puede avanzar temprano sin fijar estrategia por accidente.

## Próxima investigación compartida

**R-022/R-023/R-024 / D-015/018/019:** cerrar primero el mapa del Trading OS, las fronteras de autoridad, el papel de señales externas y el contrato pedagógico. R-025/R-007 investigan proveedores/broker en paralelo. R-020 compara Strategy V1 después de fijar gates y criterios; el video aporta inspiración funcional, no rendimientos que debamos auditar.

## Actualización de portabilidad — ADR-009 / R-028

D-037 P1 añade prerequisito reproducible de D-024/DoR: fresh environment + repo hasta entorno agéntico configurado/verificado. Diseño RC0 y evidence native/fresh clone disponibles; target Plus UNKNOWN y perfiles no heredados de Team. Discovery de raíz/cwd/Skill es reutilizable, no una ACL ni una sesión obligatoria por rol. Ruta/config/entitlement operacionales y final runtime/gobierno siguen abiertos. Esto no introduce dependencia circular con implementar Trading OS: acceptance de herramientas/roles utiliza assets y fixtures de preparación; integración trading/PAPER/DoD se verifica después en sus gates.

## Estado vigente de Capability Discovery Team — wave07

RC2/ADR-011 presentan arquitectura candidata material con reutilización nativa, Skills/metodologías públicas y paquetes repo. Evidencia SDK/Skills/tools/restart/carga acotada y bootstrap Team suficiente para decidir dirección, no para seguridad/operación/freeze. D-020 READY_FOR_DECISION/D-024 RESEARCHING; next input ADR-011, sin acceso Plus.
