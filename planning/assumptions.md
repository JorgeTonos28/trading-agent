# Assumptions Register — 2026-10-01

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Estado vigente posterior — wave07:** [RC2 Team](research/R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

**Antecedente — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Las hipótesis siguientes **no** son decisiones aprobadas. Su posible falsedad tiene que evaluarse antes del gate señalado. Estado inicial `UNVERIFIED`, salvo filas marcadas `REFUTADO`.

| ID | P | Supuesto / prueba de falsación | Impacto si es falso |
|---|---|---|---|
| A-001 | P0 | MATR_V1 puede especificarse sin optimización retrospectiva y ejecutarse a frecuencia diaria **si resulta seleccionada**; preregistro + replay. | Rediseñar el candidato o descartarlo en Strategy V1 Selection. |
| A-002 | P0 | La división 2005–2018 / 2019–2022 / 2023–2026 puede servir como protocolo OOS tras seleccionar entre candidatos; preregistrar comparación. El propietario confirma cero backtests de MATR_V1 consultados hasta 2026-10-01. | Nueva política OOS/forward si la comparación contamina el período. |
| A-003 | P0 | Close/SMA/ROC/ATR pueden calcularse con una única convención consistente de ajustes y disponibilidad; comparar data vendors. | Cambian señales/resultados. |
| A-004 | P0 | **REFUTADO:** un stop `3×ATR20` no garantiza pérdida ≤ budget 0.5%; gaps/overnight/fills pueden excederla. ADR-006 trata stop-risk como estimación y añade escenarios independientes. | D-035/031 aún deben definir fórmulas y escenarios; no presentar stop como límite real garantizado. |
| A-005 | P0 | Se puede proteger cada orden con autorización/versión verificable sin crear carrera entre risk y execution; prototipo de secuencia. | Rediseño de contratos. |
| A-006 | P1 | Un residente de RD con el perfil concreto del propietario puede obtener paper API y, después, live donde corresponda; confirmación oficial. | Candidato broker inviable. |
| A-007 | P1 | Históricos de ETFs 2005–2026 con timestamps, ajustes y derechos de uso son obtenibles dentro de presupuesto; muestras y cotización. | Cambia dataset/ventana/coste. |
| A-008 | P1 | Un motor reutilizable puede representar estrategia, órdenes y stops con fidelidad suficiente; benchmark. | BUILD/ADAPT más costoso. |
| A-009 | P0 | **SUPERSEDED por ADR-007:** que Agents SDK/Temporal y stack Python reduzcan complejidad no justifica su selección. Agents SDK/API son referencia Tier 2; Temporal pertenece a infraestructura R-011, no al comparativo agéntico R-006. | Evaluar rutas Codex/Skills y contenido Anthropic Tier 0/1 antes de D-024; el stack sigue abierto. |
| A-010 | P0 | Skills/plantillas de terceros pueden usarse legal y técnicamente en Codex; auditoría de licencia/formatos/permisos y probe real de portabilidad. | REFERENCE_ONLY o REJECT; formato similar no basta. Wave 04 probó activación de adaptaciones concretas en Team; no licencia/activación Plus de bundles propietarios. |
| A-011 | P1 | Dos fuentes permiten detectar errores materiales sin discrepancias irreconciliables; cross-check. | Más controles o cambio proveedor. |
| A-012 | P2 | Paper fills representan suficientemente la mecánica requerida para validar ejecución; shadow quotes y gap analysis. | Mayor fase shadow/limitaciones. |
| A-013 | P2 | Los límites PAPER 25%/0.5%/2% y soft/hard son coherentes con volatilidad y gaps; stress. | Recalibración humana. |
| A-014 | P3 | Resultados paper y shadow pueden transferirse parcialmente a capital live; análisis execution gap. | Live se aplaza. |
| A-015 | P4 | Alguna familia Smart Money/alternative data aporta señal post-publicación neta de costes; estudio incremental por candidato, después de factibilidad PIT. | Puede usarse solo para research/pedagogía o descartarse como señal. |
| A-016 | P0 | **REFUTADO por la transcripción primaria:** el video presenta varios componentes y estrategias distintas, sin una especificación única reproducible. | Tratar VID-TS, VID-CONG, VID-ALERT y VID-WHEEL por separado; no ensamblarlos implícitamente. |
| A-017 | P0 | El enfoque del video puede cumplir restricciones PAPER V1 sin opciones ni autoridad directa de LLM sobre broker; mapa de componentes y permisos. | Solo reutilizar workflow/metodología o exigir cambio de alcance humano. |
| A-018 | P0 | Una variante de copy trading congresual o de alertas puede reconstruirse con tiempo de publicación/recepción y universo histórico suficientes. R-021 debe intentar falsarlo antes de backtest. | Diferir la variante V1 aunque el tutorial muestre dashboards atractivos. |
| A-019 | P0 | Una interfaz común puede representar fuentes externas heterogéneas sin borrar su fecha real de disponibilidad, revisiones y nivel de confianza. R-023/004 prueban semántica. | Contratos por familia y adaptación del diseño de datos. |
| A-020 | P1 | Uno o varios proveedores especializados permitirán cubrir señales externas con derechos y coste razonables. R-025 compara contra fuentes oficiales. | Reducir alcance de fuentes V1 o construir normalización propia. |
| A-021 | P1 | PARTIAL solo fixtures: shadow con contexto versionado y canonización/derivación verificadas; no prueba cartera general/reproducibilidad generativa/aislamiento real. RC0 exige Champion oculto y distingue decisiones desde cartera real vs trayectoria contrafactual. | Parear solo hashes/contextos iguales; métricas/sealed outcomes y engine/seguridad R-026 antes DoD. |
| A-022 | P0 | **REFUTADO como inferencia válida:** la mera visibilidad de un plugin/MCP en documentación o catálogo no implica acceso a datos ni licencia para backtest. Verificar entitlement, costes y probe por dataset. | `AVAILABLE_IN_TARGET_PLUS` o `ECONOMICALLY_REASONABLE` queda NO/UNKNOWN hasta evidencia; buscar API/fuente alternativa. |
| A-023 | P3 | SUPERSEDED para PAPER por ADR-010: transferencia Team→Plus pasa a hipótesis PRE-LIVE P3, no disponibilidad PAPER. | Medir gates Team por etapa o R-029 PRE-LIVE; no gasto ni rebaja silenciosa de obligaciones. |
| A-024 | P1 | UNVERIFIED: native Codex en Team soporta demanda PAPER sostenida y recovery; identidad/acceso/probes no prueban cuotas/continuidad. | Medir gates Team por etapa o R-029 PRE-LIVE; no gasto ni rebaja silenciosa de obligaciones. |
| A-025 | P0 | **UNVERIFIED:** una ruta zero/low incremental cost puede cumplir los requisitos de calidad/fiabilidad PAPER V1. Probar capacidades, datos, límites y recovery; gratis no es evidencia de suficiencia. | Documentar brecha y opciones pagas revisables; no reducir silenciosamente gates ni comprar sin aprobación ADR-008. |
| A-026 | P0 | **PARTIAL:** wave 04 muestra valor cualitativo de procedimiento/pedagogía y más contexto; mínimo 10/10 checks vs Skill 9/10. No se demostró superioridad general ni fiabilidad. | Shortlist condicional; canonizar outputs/linaje y conservar baseline. Ver research/R-006_probe_wave_04_2026-10-05.md. |
| A-027 | P1 | **HYPOTHESIS:** el núcleo determinístico puede operar autónomamente con Codex intermitente. No equivale a continuidad probada ni runtime seleccionado. | Evaluar dependencias operativas, cadencia, estado/recovery y degradación en D-024/025; Team TP por etapa; Plus PRE-LIVE. |
| A-028 | P1 | UNVERIFIED: WL-R propuesto 40/63 jobs y deadlines son representativos/sostenibles en Team; benchmark acotado no sustituye multi-sesión/Strategy V1. | Medir gates Team por etapa o R-029 PRE-LIVE; no gasto ni rebaja silenciosa de obligaciones. |
| A-029 | P1 | **PARTIAL:** Codex SDK Python oficial puede reemplazar transporte propio; un smoke Team 7/7 y auth/schema compatibles, sin tool callbacks/full Skills/state/recovery probados. | SDK si cubre job contract; gap documentado justifica raw app-server/otra integración Tier 0/1, no construir por defecto. |

| A-030 | P1 | UNVERIFIED: abrir un paquete como cwd conserva automáticamente reglas raíz y Skills compartidas en todas las superficies/versiones. Documentación establece condiciones Git root/cwd/override y límite; R-028 lo prueba. | Verificar cadena/activación; entry point explicita raíz y contratos cuando discovery falla. No confundir instrucciones con ACL. |
| A-031 | P1 | UNVERIFIED: un clone y los assets públicos bastan para reproducir el entorno, aunque auth, dependencias, plugins, MCP y cuotas son externos. | Manifest/perfil/deltas y gates separados; fresh clone Team no transfiere auth ni prueba continuidad; Plus PRE-LIVE por separado. |
| A-032 | P1 | UNVERIFIED: el perfil acotado Team mantiene continuidad/cuota/auth y calidad en workload PAPER definitivo. Wave07 8/8 no prueba operación sostenida ni igualdad generativa. | P1 protocolo/política de versión; P2 carga/recovery/auth y regresión reales, sin gasto ni bajar obligaciones. |

## Hechos de baseline, no supuestos

La hoja declara el bloqueo de implementación, el invariante financiero, primera operación PAPER y autoridad humana sobre promoción/riesgo/live. Son reglas del proyecto hasta cambio documentado y aprobado; no afirmaciones sobre rendimiento de mercado.

El propietario declaró el 2026-10-01 que **nunca se ejecutaron ni consultaron resultados históricos de MATR_V1 o variantes cercanas**, para 2023–septiembre de 2026 ni para otro período. Esto es un hecho reportado sobre el proceso del proyecto, no evidencia de rendimiento ni garantía de que la futura comparación entre candidatos preserve un holdout.

**A-030 actualizado R-028:** PARTIAL — CLI Team probó root+rol y Skill en fixture, metadata y cinco respuestas; carpeta aislada no hereda. No generalizar a cada superficie/config/Plus; fresh clone real y target quedan pendientes. A-031 sigue parcial: assets versionados se transportan, auth/servicios externos no.

**A-030/031 tras fresh clone:** CLI app-server confirmó seis cadenas raíz+rol y Skill común; dos roles respondieron invariantes. Assets Git portables comprobados, con 31 cambios EOL del checkout; auth/localtools siguen prerequisitos externos. Desktop UI/SDK directo y Plus no demostrados. No tratar raw worktree hash como identidad portable.

## Supuestos adicionales P1 — hardening

| A-033 | P1 | UNVERIFIED: identidades/ACL/IPC/egress Windows por dominio pueden aislar todo SDK/app-server/handlers y mantener Team login legítimo sin filtrar Champion/holdout/secrets. | S2 dirección candidata aprobada ADR-012; configuración administrativa y probe empírico antes de freeze aún pendientes. Native sandbox de comandos no demuestra proceso completo. |
| A-034 | P1 | PARTIAL: SDK/CLI0.160 publicado emparejado soporta roles/Skills/tools necesarios. | H4 2/2 research/shadow correctos, no todos los roles/requests/OS ni cuota sostenida; pin final abierto. |
| A-035 | P1 | UNVERIFIED: prioridad y una cola no preemptiva bastan para demanda PAPER. | H3 virtual muestra fallos de deadline en burst/carga amplificada; no seleccionar concurrencia por promedio ni falsificar capacidad nativa. |

| A-036 | P1 | UNVERIFIED: acceso gratuito a filings SEC permite reconstruir precisión PIT necesaria para una Strategy V1 aún no definida. | SEC documenta no timestamp first-available; DatasetCard R-020 exige canal/historia/método de disponibilidad y no confundir acceptance con receipt. No dataset descargado ni API probe. |

| A-037 | P1 | PARTIAL/UNVERIFIED: controles red Windows pueden aplicarse por dominio completo sin cambiar políticas globales/empresariales. | ActiveStore reporta AllowLocalFirewallRules=False y outbound Allow; cmdlets disponibles no prueban enforcement. SI-09/10 y ADM-02 después de store competente. |
| A-038 | P1 | UNVERIFIED: identidad por dominio más export por job mantiene separación de históricos/cache y capacidad suficiente. | SIDs iguales comparten permisos; S2 exige serialización/revocación o frontera job demostrada, SI-16/BL-06/TP-6 antes de freeze; ninguna concurrencia final aprobada. |

## Revisión de supuestos S2 — 2026-10-06

| A-039 | P1 | UNVERIFIED: un único Agent Runner con contextos restringidos por job puede operar Codex Team sin grants inseguros y mantener security/blinding/recovery. | Restricted-token AccessCheck semántico 10/10 confirma mecanismo disponible, no compatibilidad/operación. SI/BL/RB/VP reales y auth/egress pendientes; no asumir una cuenta por rol necesaria. |

A-033/038 conservados como históricos: cuenta común con token irrestricto puede compartir recursos, pero TokenUser común con restricting SID/contexto diferente puede tener permisos diferentes. Revocar/serializar o borrar exports solos no prueban aislamiento de cache/perfil. A-039 se cierra únicamente con tests efectivos RC2; coste total B<A no demostrado.

## Supuesto concreto de laboratorio — 2026-10-06

| A-040 | P1 | UNVERIFIED: token con restricting SID privado y cero privilegios puede acceder a sus recursos por RootDirectory relativo sin ampliar ACL Windows y mantener tránsito/own-scratch/peer deny. | NtCreateFile oficial + harness AST-only; todos positivos/negativos reales NOT_TESTED. SeChangeNotify retirado puede romper paths/DLL/runtime; no full Codex compatibility ni grants comunes seleccionados. |

## Separación de superficie PowerShell — 2026-10-06

| A-041 | P1 | PARTIAL/UNVERIFIED: helper owner-only puede aplicar exactamente los descriptores nuevos y revertirlos mediante PowerShell 7 existente. | AST + 15 descriptores en memoria + compilación de adapter Win32 sin llamadas nativas PASS; creación/ACL efectivas/rollback NOT_TESTED. Windows PowerShell 5.1 bloqueó el QA por execution policy, aunque la superficie 7 tiene RemoteSigned. No asumir equivalencia, no cambiar/bypass policy ni instalar. |

## Corrección de entorno — 2026-10-07

La workstation INFOTEP no es host PAPER ni dispone de privilegios administrativos requeridos (declaración owner). Team no garantiza Plus. Plus/personal es target PAPER, no LIVE seleccionado. Evidencia Team de conducta/método permanece aplicable dentro de su scope; auth/ACL/IPC/red/quota/host readiness se verifican en target. No asumir que un contrato de diseño demuestra aislamiento efectivo. ADR-013/R-030.

## Auth/launch/binding del candidato B-RT1

- A-042 P1 UNVERIFIED: native keyring + HOME mínimo readonly/redirects privados puede operar Plus/restricted token sin carrier peer/Champion. Código pinado confirma HOME-derived namespace; WinCred tiene session namespace, no aislamiento por restrict SID demostrado. R-030/BL-AUTH puede invalidar candidato.
- A-043 P1 UNVERIFIED: C obtiene capacidad legítima de launch A y mantiene lifecycle sin password en scripts, privilegios J, servicio privilegiado tácito o intervención por job. Family CreateProcessAsUserW definida; derechos/setup/compatibilidad target pendientes.
- A-044 P1 PARTIAL: instance/fingerprint/fase y scope externo rechazan transferencia ficticia de evidencia. B1 16 casos sintéticos, no autenticidad/store protegido, Plus ni readiness completo.

## Admisión financiera — 2026-10-07

- A-045 P1 UNVERIFIED: los feeds/broker paper gratuitos satisfacen clocks, cobertura2005/warm-up, corporate actions, licencia y granularidad de los candidatos. Wave01 verifica ofertas/limitaciones, no datasets o fills reales; no sustituir feed de señal por NBBO simulado ni cambiar períodos sin decisión.
- A-046 P1 UNVERIFIED: date/fileDate/uploaded de agregador permite reconstruir availability exacta. Probe público Quiver solo prueba declaración de campos, no valores/historia/revisiones/delivery. Contrastar canal primario-vendor y documentar supuestos conservadores, nunca PIT exacto ficticio.

## Wave financiera02 — 2026-10-13

- A-047 P1 UNVERIFIED: free histórico anunciado satisface cobertura2005/warm-up/revisiones/rights de candidatos. Tiingo Starter durable incompatibilidad identificada R008retención; otros free con gaps/rights UNKNOWN y ningún dataset admitido.
- A-048 P1 UNVERIFIED: broker bracket/trailing soportado equivale al ratchet/partial/replacement requerido. MatrizR007 identifica gaps/races, B1–5 NOT_TESTED.
- A-049 P1 PARTIAL: álgebra de riesgo/reservas reduce ambigüedad. A1 8/8 ficticio y review no prueban engine, broker/cash mapping, concurrenttxn o benchmarks; R2 conceptual aprobado ADR-015; fórmulas/tests restantes pendientes.

## R2 conceptual — ADR-015

Referencia principal DECIDED por owner. No asumir que toda marca/stop en datos es protección confirmada, que menor R2 genera autorización de compra, ni que el registro de escenario prueba ejecución. R1/P&L y loss/drawdown independientes, p_auth y claims tienen pruebas/mapping pendientes.

## Supuestos wave03 — 2026-10-13

- A-050 P1 PARTIAL: parser público de Form4 puede ser reutilizable. E1 sólo tablas, full factoryerror, enriquecimiento/footnotes/owners/mapping/PIT no demostrados; no REUSE_AS_IS como señal.
- A-051 P0 UNVERIFIED: reserva2023–2026-09-30 tiene independencia suficiente. Exposure ledger/M-11 debe considerar exposición incidental; estado INTEGRITY_UNKNOWN. Q055 O-B conceptual no lo certifica ni fija sample/thresholds.
- A-052 P1 UNVERIFIED: existe ruta gratuita suficiente para histórico durable/as-of. Starter candidato refutado para ese rol; alternativas no agotadas, no justificar gasto por descarte de una sola fuente.

## ADR-016 — 2026-10-14

A051 integridad de reserva permanece UNVERIFIED, no resuelta por aprobación O-B. A-053 P0 UNVERIFIED: suficientes señales/regímenes independientes y ventaja robusta a retrasos/costes para cada candidato. Debe evaluarse con criterios previos y métodos que contemplen dependencia/múltiples ensayos; INSUFFICIENT_EVIDENCE no equivale a fallo económico.

## Wave04 — 2026-10-14

- A-054 P0 UNVERIFIED: muestra efectiva/precision y beneficio económico suficiente del candidato.19/19primitives no informa power/alpha; endpoint preferenciaQ056 y EvidenceCard previos requeridos.
- A-055 P1 PARTIAL: delayedhistoricalSIP puede servir a señalEOD. Docs acceso15min/no subscription, pero rights/coverage2005/firstdelivery/PIT/freshRisk no demostrados; no stack free certificado.
- A-056 P1 PARTIAL: statsmodels/arch primitives compatibles research. Toyrepeat yknownvectorPASS no prueba estimadores/modelo/runtime personal ni licencias transitivas completas.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Supuestos wave05

- A-057 P0 UNVERIFIED: cuatro años tienen precisión suficiente para márgenes económicamente razonables. E3 ilustra dependencia de dispersión/covarianza, no la estima en estrategias; jamás ampliar margen por conveniencia.
- A-058 P1 UNVERIFIED: yield público equivale a retorno realizable/cash broker. R008 distingue descuento/constant maturity/roll/carry real; vintages y modelo no admitidos.
- A-059 P0 UNVERIFIED: bajar volatilidad/exposición demuestra eficiencia incremental. Counterexample E3, espejo REAL con ledger/clock propios; beta/mix y cola permanecen pendientes.
- A-060 P1 PARTIAL: Form4 public parser preserva información necesaria. F2 flags/footnote substrings sólo componentes; None ambiguo, duplicados y planes anteriores a2023 UNKNOWN. No dataset admitido.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Supuestos wave06

- A-061 P1 PARTIAL: benchmark equal-weight y reinversión preservan contabilidad comparable. Targets1/6 no garantizan pesos realizados exactos; policy/data/engine aún no aceptados, fixturesE4 no ledger completo.
- A-062 P0 UNVERIFIED: inferencia de CAGR/ES con bloques tiene cobertura/power adecuados. Piloto de media evidencia fragilidad iid, no valida método; Inf puede producir límite finito, admission previa obligatoria.
- A-063 P1 UNVERIFIED: full/quarterlyindex SEC actual acredita availability histórica. PAC/rebuilds generan diferencias; raw versions/channel/receipt pendientes.
- A-064 P1 UNVERIFIED: coste operativo incrementa cero o se puede cargar también a benchmark pasivo. Uso/escala/K/accrual pendientes; net_after_ops y net_trading separados, UNKNOWN bloquea claim operacional.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.

## Supuestos wave07

- A-065 P0 UNVERIFIED: CI de CAGR/ES tiene cobertura suficiente bajo dependencia/regímenes y familia real. E5/E6 no aceptan método; AND bajo no valida nullmarginal/leastfavourable supremum.
- A-066 P1 UNVERIFIED: dos rulepresets con parámetros especificados son configuraciones financieras ejecutables. Target/caps/broker/source/protección/fees siguen OPEN;10declaraciones no10estrategias admitidas.
- A-067 P0 UNVERIFIED: ES menor implica DD/vol/recuperación adecuados. Q059 guardrails nueva materialidad, censura y tiposde evidencia separados.
- A-068 P1 UNVERIFIED: coste/capital pueden elegirse porcelda favorable oF0significa costo0 real. Scenariosprevios y anchorowner antes de resultados; costos/scaleUNKNOWN→operacionalNOT_EVALUATED.

## Vigencia G-R1 — ADR-020, 2026-10-15

[ADR-020](decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md): Q-059/G-R1 DECIDED en preferencia económica ex ante: no deterioro de DD frente a EW6-BH completo ni de volatilidad diaria frente al espejo K2 admisible. ES95/M1 primario y NI/cash/K2 conjuntos; recuperación/underwater/pérdidas/gaps/slippage/extremos obligatorios. DD exige estimando/horizonte/path/incertidumbre y aplicabilidad válidos; una trayectoria/bootstrap genérico no demuestra futuro. Volatilidad incluye upside/downside. Guardrails relativas no son límites absolutos Risk D-031. G-R2 no aprobado ni fallback. Estados separados y NO_STRATEGY_QUALIFIED; ningún método/dato/broker/Strategy/F0/implementación aceptado. Continuar P0/P1 financieros en checkpoints agrupados; holdout UNKNOWN/lock/targetdeferral.

## Supuestos wave08

- A-069 P0 UNVERIFIED: DD-E candidato admite modelo/método con cobertura/suficiencia PRICE–MATR. No garantía de futuros arbitrarios ni aceptación desde14fixtures.
- A-070 P1 REFUTED en scope: cambiar sólo orden de retornos no cambiaDD. E7samewealth/ES/var peroDD19vs10.9, sóloficticio.
- A-071 P1 REFUTED en scope: make_qty default conserva cota de cantidad decimal. QE1ROUNDmuestra1.6→2; floor1, pendienteadapter entero/tick/fees.
- A-072 P1 REFUTED por metadata/cota: GLDpuede200sesionesprevias aenero2005; listar18nov2004loimpide. Cobertura real sigueNOT_TESTED.
- A-073 P1 UNVERIFIED: derechos de dosvendors permiten rawarchive/replaydurable/usoIApersonal. Consultas listas, sin enviar ni asumir permisos por acceso público.
- A-074 P1 DECIDED_INPUT: referencia nominalPAPER10k y costes evaluados en5escalas porADR021; no fundedcapital o costeactual demostrado.

## Supuestos wave09 — fuentes y comunicación

- A-075 P1 UNVERIFIED: revisión/alta del registro equivalen a disponibilidad al cliente. Separar clocks y backfills por versión; no afirmar PIT por latest-only o por una etiqueta comercial.
- A-076 P1 UNVERIFIED: una fuente complementaria de acciones cubre desarrollo2005+ o seis ETF por cobertura global. Verificar cada ventana/componente y subcard; no cambiar ventanas.
- A-077 P1 UNVERIFIED: licencia local o uso interno non-display habilita IA externa/retención post-terminación. Evidencia por producto, plan, uso y seis categorías; respuesta genérica insuficiente.
- A-078 P1 DECIDED_INPUT: propietario enviará consultas personalmente; preparación aprobada, envío automático NO autorizado. No envío demostrado, no EXTERNAL_CLARIFICATION_PENDING todavía.
- A-079 P1 UNVERIFIED: petición de lectura no consume asignaciones/cuota ni omite filas. Gate previo de scope/licencia/budget; matriz CA07 sin ejecutar.

## Supuestos cuestionados por wave10 — 2026-10-23

- REFUTED en scope nativoQE2: consumoL1=True impone cap estricto de tamaño topofbook. El matcher continúa sintéticamente más profundo; L1 no prueba liquidez total real.
- REFUTED en código LEAN pinado: modo Raw por sí solo separa receivable/pay-date. ApplyDividend requiere adaptación para ese contrato.
- REFUTED lógicamente: mismo DD esperado implica misma frecuencia de deterioro. E8 muestra90%/10% con la misma esperanza, no datos de candidatos.
- REFUTED como modelo: qty, lifecycle y encumbrance son estados mutuamente excluyentes. RiskRC3 separa dimensiones; R3 no prueba atomicidad.
- NO_DEMONSTRADO: respuesta comercial genérica concede retención, IA/non-display, PIT y calidad. Vendor state sólo AWAITING_VENDOR_RESPONSE por owner; fecha exactaUNKNOWN.
- UNKNOWN mantenidos: muestras reales/derechos, paridad, capacidad target, costes totales/variables, integridadholdout. Resultados sintéticos/builds no los cierran.
