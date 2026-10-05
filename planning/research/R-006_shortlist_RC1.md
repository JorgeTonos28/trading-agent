# R-006 — shortlist final propuesta y madurez RC1

**Fecha:** 2026-10-05. **Estado:** `RESEARCHING / PROPOSED_SHORTLIST_COMPLETE`, suficiente para orientación humana y aceptación de finalistas; **no** madurez final para cerrar D-020/D-024. `SELECTED=NO` en todos. Sustituye RC0 como recomendación actual; RC0 y waves/attempts conservados. No cambia A+/G1+G2, riesgo, Strategy V1, broker, datos, implementación bloqueada ni presupuesto.

## 1. Paquete autónomo completado

- Paso 1: [evidencia/caller/snapshots/lineage/estados](../06_agent_evidence_contract_RC0.md), [PM shadow/comparador](../06_shadow_portfolio_contract_RC0.md), [Pedagogical Agent completo propuesto](../06_pedagogical_contract_RC0.md). Incluye typed refs, role/schema externo, cantidades canónicas y separación estado del job/contenido/incidente.
- Paso 2: [workload WL-L/R/S y matriz de aceptación](R-006_workload_acceptance_RC0.md) C-010/C-025a y cuatro procedimientos, con GP1–7 y criterios Plus. Especificación ≠ ejecución de carga ni aprobación de la cadencia de Strategy V1.
- [Wave 06](R-006_probe_wave_06_2026-10-05.md): 39/39 checks locales v2 y 10 turnos Team. Schema 10/10, admisión v1 8/10, v2 10/10 tras aclarar citas source.field; conserva criterio enmendado después de observación. No repetir benchmark bajo Plus ni inferir superioridad de Skill.
- C-029 SDK Codex público revisado como alternativa de transporte nativo, distinto de Agents SDK API; evidencia acotada en [probe SDK](R-006_codex_sdk_findings_2026-10-05.md). Evitar wrapper JSON-RPC nuevo cuando una capa oficial satisfaga requisitos.

## 2. Finalistas, reservas y disposiciones

`YES archivo` no es inferencia/activación Plus; compatibilidad es del probe, no seguridad/operación de producción. `ECONOMICALLY_REASONABLE` separa adquisición método de cuota/runtime/datos. Disposición es recomendación, no selección definitiva.

| Candidato | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_TARGET_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED | Recomendación |
|---|---|---|---|---|---|---|---|
| **C-010 Codex mínimo** | YES | YES native Team 15 turnos mínimo acumulados, corpus distintos | UNKNOWN configuración/carga; base documentalmente elegible | YES fixtures; desktop directo no benchmark | CONDITIONAL cuota/operación | NO | **REUSE_AS_IS** de capacidad base; benchmark permanente sin Skill |
| **C-025a native app-server / C-029 Codex SDK** | YES | C-025a YES 30 turnos; C-029 YES smoke Python 7/7 checks | UNKNOWN ruta/auth/operación target; SDK público gratis | C-025a YES fixtures; C-029 YES smoke, tools/Skills/state pendientes | CONDITIONAL runtime/local/Plus | NO | **WRAP** de transporte oficial mínimo; preferir SDK donde cubra contrato, raw app-server solo por gap concreto. No dos runtimes obligatorios |
| **C-017a idea-generation** | YES | YES archivo/activación Team, output research tipado | YES método público; UNKNOWN activación | YES regresión pequeña; no alpha validado | YES método 0; runtime conditional | NO | **ADAPT**, port del método público Apache-2.0 con PIT/falsifier/sin cartera |
| **C-017b thesis-tracker shadow** | YES | YES HOLD/abstain anteriores y OPEN toy con lineage | YES método público; UNKNOWN activación | YES ejercicio; cartera general/eval pendiente | YES método 0; runtime conditional | NO | **ADAPT**, port hacia proposal aislado; no importar autoridad Increase/Trim/Exit original |
| **C-024 pedagogía factual** | YES prototipo propio | YES traza/pregunta/causa UNKNOWN | YES método propio; UNKNOWN activación | YES B4 synthetic; DoD educativo sin probar | YES método 0; runtime conditional | NO | **ADAPT** de evidencia/enseñanza al proyecto; reportes/curriculum especificados, no declarados implementados |
| **C-028 Quant/Strategy Review** | YES prototipo propio | YES train/OOS/cost/role/failure | YES método propio; UNKNOWN activación | YES checklist; no backtest engine | YES método 0; runtime conditional | NO | **ADAPT** del protocolo research/PIT; quant engine se decide en R-009 |
| C-027 MCP oficial local | YES MIT | YES 13 checks stdio mock | YES SDK público; UNKNOWN host/connector | YES mock; Codex host no probe | YES software; datos/operación aparte | NO | **WRAP** reserva; activar solo si herramienta concreta necesita interoperabilidad |
| C-026 Data/plugins propietarios | YES | YES contenido/metadata; activación contradice superficies | UNKNOWN | PARTIAL | CONDITIONAL entitlement/licencia/deps | NO | **REFERENCE_ONLY** ahora; posible REUSE_AS_IS en entorno autorizado, nunca PORT propietario |
| Métodos Anthropic Earnings/Audit/Calendar/Model/Market | YES públicos | YES revisión primaria/licencia/limitaciones | YES archivos; UNKNOWN tools/runtime/datos | PARTIAL por tarea | YES métodos; dependencias conditional | NO | **ADAPT / PORT** reserva por necesidad; wrapper/conector premium REFERENCE_ONLY PAPER |
| Agents SDK/API, Claude/Managed, premium financial MCP | YES | YES docs/activos, consumo no ejecutado | NO como consumo API incluido Plus; otros UNKNOWN por servicio | REFERENCE_ONLY, no probes pagos | NO selección PAPER por defecto; LIVE reevaluable | NO | **REFERENCE_ONLY** PAPER, conservar ficha LIVE valor/coste/aprobación de gasto |
| Otros AI Labs/frameworks agénticos C-019–021 | YES referencias históricas | No evaluar bajo alcance | No evaluar | NOT_EVALUATED | NOT_EVALUATED | NO | **REJECT** por alcance ADR-007, no por juicio técnico |

No recomendado **BUILD** de framework de agentes, plugin financiero completo, transporte propio, research engine ni simulator durante preparación. Adaptación/contratos de proyecto requieren integración futura; investigar R-009/011/012 antes de elegir software de workflow/storage/quant. El traslado Anthropic es PORT en ejecución metodológica y ADAPT como disposición principal, debido a cambios de PIT/autoridad/output.

## 3. Arquitectura candidata para gobierno

```text
Núcleo financiero local/determinístico always-on (tecnología aún OPEN)
   datos admitidos -> Champion determinístico -> TradeIntent
       -> Deterministic Risk Engine -> Execution -> broker PAPER seleccionado después
   ledger/monitor/reconciliación/protección/G1+G2 sin esperar un LLM
       |
       +-> manifests/snapshots/trazas sanitizados e inmutables
                -> jobs Codex/Plus intermitentes (transporte oficial mínimo)
                   RESEARCH_IDEA | QUANT_REVIEW | PORTFOLIO_SHADOW | PEDAGOGY
                -> admission por caller/rol/schema/PIT/lineage
                -> research, shadow audit/eval, informes y aprendizaje
```

Roles lógicos, no cuatro LLM residentes, procesos/subagentes ni multiagent handoffs obligatorios. Disparos eventuales por cartera y ventanas de report/research con workload explícito; PM shadow operativo como capacidad desde B4, sin canal financiero. Human promotion/resume material mantienen ADRs. Pedagogía factual desde B4, contrato completo antes DoD. No-output/late/fail auditable; renderer factual de fallback no reemplaza obligaciones agénticas. Degradación prolongada falla suficiencia/DoD, sin autorizar saltarse una dependencia financiera.

Transporte SDK vs raw app-server depende de tools/dynamic callbacks, auth/client lifecycle/versiones y recovery; SDK revisado no selecciona Python/TS ni lenguaje financiero. Skills pequeñas opt-in por tarea cuando aportan método, conservando mínimo como baseline. Plugins/MCP no obligatorios: incorporar solo necesidad demostrada/entitlement/licencia. Credenciales broker/Execution no están en el entorno agéntico candidato; aislamiento real y canales requieren D-027 y gobierno, no están probados por este diagrama.

## 4. Alternativas y trade-offs revisables

| Alternativa Tier 0/1 | Ventaja | Límite/riesgo | Recomendación |
|---|---|---|---|
| **Local determinístico + Codex jobs vía SDK/app-server** | Desacopla control financiero de cuota/latencia; evidencia y cobertura shadow/report medibles, integración programática | Auth/cuota/recovery target y límites de tools/lifecycle; wrapper/state local aún por investigar | Principal candidata para aceptación, condicionada |
| Local determinístico + Codex desktop/manual/on-demand | Menor integración y recuperación manual; útil baseline de investigación | Puede no cumplir cadencia shadow/report autónoma; desktop directo sin benchmark de ruta | Comparador/reserva; no dar por suficiente PAPER autónomo |
| Codex/LLM permanente en cada decisión operativa | Posible razonamiento flexible | Necesidad/continuidad no demostradas, cuotas críticas, contradice A+ si genera intent operativo | No recomendar para PAPER A+; no probar nuevo framework ni modificar autoridad |
| API/modelo pago posterior | Posible control de capacidad/continuidad, según evidencia | Billing aparte/lock-in y coste workload sin beneficio demostrado | Referencia LIVE o excepción PAPER aprobada, sin gasto aquí |

Si Plus falla: diagnosticar antes de descartar. Rediseño de carga Tier 0/1 solo si conserva requisitos aprobados; no recortar shadow/pedagogía para mantener gratis. Gasto necesita ficha ADR-008 y aprobación separada. La arquitectura futura no queda prohibida por ser paga.

## 5. Madurez por dimensión

| Dimensión | Estado real | Pendiente antes de cierre/freeze |
|---|---|---|
| Coverage IA/métodos | SUFFICIENT_FOR_PROPOSED_SHORTLIST dentro OpenAI/Anthropic | Aplicaciones específicas elegidas por Strategy V1/fuentes, no importar activos por catálogo |
| Licencia/portabilidad/coste | SUFFICIENT_METHOD_ASSETS / CONDITIONAL_RUNTIME | Entitlement por superficie, datos/servicios, coste WL-R/escala y evolución de versiones |
| Contratos por rol/shadow/pedagogía | SPECIFIED_RC0 + SPINE_PROBED | Full production schemas, reports, aislamiento/engine/data/integration según D-025/026/027/029/034 |
| Conducta/comparativa | EXECUTED_SYNTHETIC: 20 iniciales + 10 focalizados, ambos métodos útiles | No fiabilidad universal, superioridad de Skill o validación de estrategia |
| Workload/aceptación | SPECIFIED_NOT_EXECUTED_TARGET | Representativo real, latencia/cuota/estado; rebaselinar demanda con Strategy V1 |
| Seguridad/autoridad | PARTIAL_HARNESS_NEGATIVES | Threat model/ACL/segregación, red team/integration y aprobación material D-027 |
| Plus | UNKNOWN target configuration | GP1–7 finalistas; no repetir toda la conducta Team |
| Revisión/gobierno | PLAN_ARCHITECT_CONSISTENCY_REVIEW_ONLY | Revisión crítica independiente y owner antes de selección final D-020/D-024 |

**Endpoint alcanzado del paquete autónomo**, no del Preparation Program. D-020 RESEARCHING y D-024 OPEN; ninguna capability SELECTED. R-006 lista para **presentar shortlist/dirección candidata**, no para declarar runtime maduro/congelado.

## 6. Pendientes exclusivos Plus y pendientes distintos

**Solo cuenta/superficie Plus objetivo:** confirmar identidad/entitlement/cliente; disponibilidad y activación de Skills/modelo/tools; auth y lifecycle legítimos, quota/reset/cupo compartido; persistencia/restart/recovery de ruta; carga representativa y suficiencia operacional GP1–7. Pedir al propietario iniciar sesión allí; **no** mandar contraseña/token/API key al chat/repo. Team no llena estos campos.

**No son un gate Plus:** Strategy V1/broker/proveedores/engine, parámetros/formulas financieras, simulator/costos/evaluación de retorno shadow, seguridad real/aislamiento y review independiente, reports/curriculum completos y durable state general. Tienen backlog P0/P1/P2 propio; este paquete no los cierra. Saber si una Skill se activa bajo Plus no valida una estrategia o protección.

## 7. Intervención humana exacta

`HUMAN_ACTION_REQUIRED`

**Decisión propuesta:** aprobar como dirección candidata para la siguiente aceptación PAPER la separación núcleo determinístico/local always-on + Codex/Plus por jobs auditables, con C-010 baseline, cuatro procedimientos adaptados y transporte oficial mínimo SDK/app-server según cobertura, conservando alternativas y gates. Es orientación arquitectónica material condicionada, **no** selección final/freeze de runtime/plugin/Skills, ni cierre D-020/D-024, ni implementación, gasto, nueva autoridad, Strategy V1 o broker.

**Input posterior necesario:** habilitar una sesión de la cuenta **Plus individual objetivo** para GP1–7. Hasta entonces `AVAILABLE_IN_TARGET_PLUS=UNKNOWN`. Recomendación principal frente a desktop/manual: ofrece camino medible a cobertura shadow/report autónoma sin depender de un LLM permanente; la cuenta objetivo y criterios propuestos deben confirmarla. No iniciar el gate ni cambiar autenticación de esta cuenta Team automáticamente.

Tras decisión/acceso: registrar orientación aprobada sin dar por cerradas selecciones; smoke finalistas y workload, review independiente/seguridad, comparativa final para D-020/024; mientras no afecte el bloqueo, seguir R-020/D-008 y plataforma/datos según secuencia, sin implementar.

## 8. Actualización vigente — cohorte candidata aprobada y portabilidad

El propietario aprobó la **cohorte** para continuar hacia Plus Acceptance; no aprobó selección final/freeze D-020/D-024 ni necesariamente toda la dirección arquitectónica de §3/§7. El pedido de aprobación de cohorte de §7 queda atendido en ese alcance. ADR-009 añade R-028/D-037 P1 antes de continuar: onboarding reproducible y paquetes por rol, sin fijar sesiones/proyectos ni runtime. Plus no se ejecuta en Team. La nueva secuencia y gate prevalecen sobre el endpoint histórico de este documento.

## 9. Impacto técnico de R-028

[Bootstrap/packaging RC0 y probes](R-028_bootstrap_findings_2026-10-05.md): añadir discovery nativo C-030 REUSE_AS_IS, modo/Skill/manifiesto C-031 ADAPT; roles nativos C-032 y plugin distribución REFERENCE_ONLY. Seis paquetes documentales reutilizables + shared; raíz/rol/Skill probados en fixture Team, no un LLM por carpeta. Config/permisos efectivos son externos a AGENTS. D-037/R-028 P1 y EB1–8 bloquean D-024/DoR. La arquitectura candidata ahora incorpora ruta de onboarding/perfil/diff/gates, sin congelar runtime/topología. Próximo hito autónomo: fresh clone de assets reales y reporte parcial; luego gates de entorno objetivo.
