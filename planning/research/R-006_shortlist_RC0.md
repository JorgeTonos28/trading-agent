# R-006 — Shortlist condicional y revisión de madurez RC0

**Antecedente conservado:** la recomendación vigente está en [shortlist RC1](R-006_shortlist_RC1.md). Pasos autónomos 1–2 completos en especificación y regresión focalizada; RC1 detalla endpoint/gobierno/Plus y otros pendientes sin declarar selección. Esta RC0 no se elimina ni reescribe como si sus probes ya hubieran incluido el contrato posterior.

**Fecha:** 2026-10-05. **Estado:** `RESEARCHING`; suficiente evidencia para shortlist, **no** para selección/freeze. D-020 no se cierra y D-024 permanece `OPEN`. Ningún candidato tiene `SELECTED=YES`. [Wave 04](R-006_probe_wave_04_2026-10-05.md) compara veinte turnos Team; [wave 05](R-006_probe_wave_05_2026-10-05.md) completa MCP local, metadata/licencias de plugins, más activos financieros y experimento de schema por rol. ADR-001/002/006/007/008 siguen vigentes.

## 1. Recomendación técnica provisional

Investigar como alternativa principal **núcleo local/determinístico always-on + Codex/Plus intermitente por tareas auditables**. El Champion aprobado, señales/TradeIntent determinísticos, Risk Engine y ejecución pertenecen al camino financiero; research, propuestas shadow, análisis y enseñanza producen artefactos sin autoridad operativa. Esto preserva A+, no selecciona motor/lenguaje/runtime/topología ni aprueba seguridad material. No requiere un LLM permanentemente activo por definición.

Un job agéntico debe recibir snapshot inmutable asof/versionado y trazas; no actualizar su evidencia con información nueva durante la comparación shadow. El snapshot pareado permite medir coincidencias/divergencias aunque el output llegue después. Registrar retraso, missing/failed/late y cobertura: el silencio del agente no equivale a HOLD. Si una dependencia financiera obligatoria falla, siguen G1/G2 y reanudación humana de incidentes materiales; la alternativa no autoriza ignorar esa dependencia.

PAPER sigue necesitando Portfolio Manager shadow y Pedagogical Agent completo antes de DoD. Intermitente no significa opcional ni solo asesor conceptual. Cadencia, persistencia, recuperación, cuotas y objetivos operativos permanecen por especificar/aceptar; no se presume continuidad desatendida de Plus. A la vez, fallos de research no deben confundirse automáticamente con una discrepancia financiera. El comportamiento exacto se cerrará en sus contratos/gates.

**Regla de complejidad:** comenzar la comparación arquitectónica con una ruta Codex mínima y Skills breves explícitas. No hay evidencia aquí de que más subagentes, un bundle financiero entero o un LLM en cada decisión operativa aporten valor material. API/SDK pagos permanecen referencia/alternativa futura según ADR-008; no hay gasto aprobado.

## 2. Shortlist por capacidad (disposiciones recomendadas)

`AVAILABLE_TO_US` no se usa como booleano agregado: se desglosa en entorno de investigación y target. `YES` de activo público significa acceso al archivo, no activación/inferencia Plus. Compatibilidad observada tiene el alcance del probe, no de producción.

| ID / finalista o reserva | EXISTS | AVAILABLE_IN_RESEARCH_ENVIRONMENT | AVAILABLE_IN_TARGET_PLUS | TECHNICALLY_COMPATIBLE | ECONOMICALLY_REASONABLE | SELECTED | Disposición y evidencia |
|---|---|---|---|---|---|---|---|
| C-010, workflow mínimo Codex | YES | YES conducta en app-server Team | UNKNOWN configuración/carga | YES fixtures; operación pendiente | CONDITIONAL cupo/operación Plus | NO | `REUSE_AS_IS` de capacidad base como benchmark; contrato/validación de proyecto aparte. 10/10 checks predefinidos. Uso directo desktop no benchmark de ruta aquí. |
| C-025a, app-server + login nativo ChatGPT existente | YES | YES 20 inferencias efímeras/estructura/tools | UNKNOWN | YES ruta ensayada; estado/auth/SLA pendientes | CONDITIONAL | NO | `WRAP` candidato si hace falta integración por jobs; protocol/version pin. No es nueva autorización SIWC ni conexión broker. |
| C-017a, idea-generation Anthropic adaptada | YES | YES archivo y activación Team | YES archivo gratuito; UNKNOWN activación | YES entrega; 1 mezcla de tipo de output | YES método gratis; runtime condicional | NO | `ADAPT`, research con PIT/falsifier; mejorar tipo de salida antes de aceptar. No uso as-is/shorts operativos. |
| C-017b, thesis-tracker adaptada shadow | YES | YES archivo/probe Team | YES archivo; UNKNOWN activación | YES proposal aislada en fixture | YES método gratis; runtime condicional | NO | `ADAPT` con contexto pareado, reserva, tesis, falsifier y métricas. No convertir Increase/Trim/Exit originales en autoridad. Sizing general/performance no probados. |
| C-024, procedimiento factual pedagógico | YES prototipo propio tras revisar métodos existentes | YES traza/pregunta Team | YES archivo propio; UNKNOWN activación | YES probe B4; contrato completo pendiente | YES método propio; runtime condicional | NO | `ADAPT` de métodos de explicación/trazabilidad hacia Skill breve propia. No copiar bundles propietarios ni declarar DoD completo. |
| C-028, procedimiento Quant/Strategy Review | YES prototipo propio | YES train/OOS/costes/retry Team | YES archivo propio; UNKNOWN activación | YES checklist; no motor quant | YES método propio; runtime condicional | NO | `ADAPT` de protocolo de research/PIT al análisis quant. Comparar engine/librerías en R-009; resultados/pre-registro/cálculos determinísticos. |
| C-027, SDK MCP oficial local (reserva) | YES MIT 2.3.0 | YES stdio/mock 13 checks | YES software público; UNKNOWN host/connector Plus | YES local, integración Codex no probada | YES SDK sin factura; datos aparte | NO | `WRAP` si interoperabilidad justifica coste operativo; no hacer MCP obligatorio si tool mínima basta. |
| C-026, Data analysis quality / validate-data (reserva) | YES, bundle 1.0.11 Proprietary | YES archivos; UNKNOWN activación en ruta por conflicto de superficies | UNKNOWN | PARTIAL métodos pertinentes, no workflow financiero probado | CONDITIONAL inclusión/licencia/deps | NO | `REFERENCE_ONLY` hoy; `REUSE_AS_IS` posible dentro de entitlement futuro. No `PORT` del código propietario. Alternativa: contratos/checklists propios breves con activos públicos. |

**Reservas metodológicas, no finalistas runtime ahora:** C-016/C-017 Earnings Reviewer/Earnings Analysis/Audit XLS/Catalyst Calendar/Model Update/Market Researcher, `ADAPT` por tarea o `REFERENCE_ONLY` de wrapper. Lectura primaria de métodos/licencias/dependencias sí, probes completos/workbooks/proveedores no. Activar cohortes según Strategy V1/fuentes, no fabricar demanda para importar templates. Data/visualizaciones/documentos pueden ayudar a materiales pedagógicos cuando target los admita; no son necesarios para una explicación factual básica en JSON/Markdown.

**Referencias/alternativas fuera de selección PAPER actual:** C-012/013 OpenAI Agents SDK/API con key y C-016 runtime Claude/Managed Agents, `REFERENCE_ONLY` PAPER por presupuesto/entitlement, LIVE reevaluable con valor/coste. C-018 conectores financieros premium se registran por proveedor/R-025, sin conexión ni gasto. C-025b SIWC OAuth plan usage sigue candidato documental, no finalista equivalente al login nativo observado. C-015 portfolio cookbook archivado es referencia, no contrato shadow. C-019/020/021 y otros frameworks agénticos están `REJECT` **por alcance de esta versión**, sin comparativa técnica. Brokers/datos/quant/infraestructura permanecen en investigaciones separadas.

## 3. Economía explícita por capa y fase

| Cohorte | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| C-010/C-025a ejecución Codex de finalistas | UNKNOWN hasta Plus Gate/cadencia | Potencial 0 incremental dentro de plan existente; no nueva factura API en probes. Cupo compartido y operación local por medir. | UNKNOWN fijo/variable/mensual/escala | Workflow mínimo manual/on-demand y núcleo local, sujetos a necesidad/entitlement | Posible continuidad/capacidad/control API, sin demostrar | YES antes de contratar/usar billing extra |
| C-017a/b, C-024, C-028 método/Skill | YES **adquisición de método**; runtime UNKNOWN | 0 licencia pública/propia; adaptación/mantenimiento/uso del modelo aparte | Método 0; inferencia/datos/local UNKNOWN por carga | Workflow mínimo con contrato común | Pagar Skill/template no admitido; datos/runtime mejores pueden justificarse | YES para dependencias pagas, no compra de método |
| C-027 SDK transporte MCP | YES software local; integración final UNKNOWN | 0 licencia; tiempo de integración y local sin cuantificar | Software 0; hosting/auth/datos/operación UNKNOWN a escala | Tools dinámicas/APIs directas, gate proveedor | Posible connector hospedado/operación más fiable; no probado | YES para servicio externo incremental |
| C-026 Data / C-011 Developers | UNKNOWN entitlement Plus por superficie | 0 solo si incluidos; adquisición adicional no aprobada | UNKNOWN plan/servicio/carga | Método propio/activos públicos; docs web oficial | Valor de tools extra si inclusión/fiabilidad aporta ventaja medida | YES antes de cualquier coste adicional |
| Métodos financieros públicos de reserva + fuentes | YES método; UNKNOWN datos suficientes | Método 0; free/PIT fuentes por R-008/025. Premium excluido de consumo ahora. | UNKNOWN por proveedor/unidad de carga | Filings/IR públicos + datasets admitidos, no equivalencia asumida | Consenso, cobertura/historia/latencia/QA premium si material | YES antes de contratar/datos facturables |
| SDK/API/modelos pagos de referencia | NO como entitlement incluido Plus | UNKNOWN coste por workload; sin consumo aprobado | UNKNOWN variable/fijo/mensual/escala | Finalistas anteriores, viabilidad target pendiente | Control, continuidad y calidad como hipótesis por comparar | YES |

No convertir tokens Team en coste mensual Plus/API. Las fichas LIVE necesitan carga real, tarifa vigente, fijo+variable, beneficio neto, escala, lock-in y salida según ADR-008; no hay estimación mensual aprobable todavía. Lock-in: formatos Markdown/JSON/PIT portables; límites/auth/schema app-server ligados a OpenAI/versiones; MCP interoperable pero cada proveedor mantiene licencia/PIT; assets Anthropic portados no requieren Claude, aunque sus MCP premium no se portan por descargar prompts. Una ruta paga no se descarta permanentemente.

## 4. Madurez y gates restantes

| Criterio | Estado para shortlist | Antes de selección/cierre |
|---|---|---|
| Cobertura research, quant, shadow, pedagogía y herramientas | SUFFICIENT_CONDITIONAL: candidatos/métodos y mínimo comparados | Completar contratos funcionales, no inferir engine/estrategia seleccionados |
| Fuentes/versiones/licencias/coste | PARTIAL suficiente para cohorte breve | Plus Gate, dependencias/datos específicos; resolver surfaces propietarias si necesarias |
| Prueba conductual Team | EXECUTED con fallo conservado; 20 turnos, revisión no ciega | No repetir toda bajo Plus; ampliar casos solo por riesgo concreto |
| Permisos/autoridad/inyección | PARTIAL: contenido, tool allowlist, negativos MCP/schema sintéticos | D-027/D-034 y controles reales; texto correcto no prueba separación técnica final |
| Repetibilidad | PARTIAL: facts/PIT estables; etiquetas/formatos variables | Canonización, versiones/snapshots, linaje de derivaciones y comparación semántica |
| Runtime, cuotas, auth, persistencia/recovery | OPEN target; no requisito para esta shortlist | [Plus Acceptance Gate](R-006_plus_runtime_gate_RC0.md) solo finalistas + suficiencia por jobs/cadencia |
| Revisión crítica independiente y gobierno | OPEN | Requeridos antes de paquetes finales D-020/D-024; esta revisión es del Plan Architect |

**Resultado:** no declarar R-006 cerrado/maduro para selección final, no `READY_FOR_DECISION` de D-024, no freeze. Sí hay evidencia suficiente para reducir el universo a una cohorte de aceptación y diseñar la siguiente prueba sin pedir una cuenta Plus para todo discovery.

## 5. Siguiente trabajo inmediato

**Seguimiento 2026-10-05:** pasos 1–2 ahora especificados en [contrato común](../06_agent_evidence_contract_RC0.md), [shadow](../06_shadow_portfolio_contract_RC0.md), [pedagogía](../06_pedagogical_contract_RC0.md) y [workload/aceptación](R-006_workload_acceptance_RC0.md). [Wave 06 preregistrada](R-006_probe_wave_06_protocol.md) verificará las correcciones antes de revisión de shortlist. Esta RC0 se conserva como antecedente, no evidencia de que los probes posteriores ya estén ejecutados.

1. Preparar contratos de evidencia por rol y snapshot pareado para D-034/R-026 y pedagogía: enums, OBSERVED/DERIVED, unidad/fórmula/inputs, quantity semantics, fuente/clocks/versiones, trusted role y failure/late/no-output. Incorporar hallazgos wave 04; son documentos/probes, no Trading OS.
2. Definir workload mínimo representativo para research/shadow/pedagogía y matriz de aceptación de **C-010/C-025a + cuatro procedimientos**. Cadencia se enlaza a Strategy V1 aún OPEN; no inventar SLA ni prometer cuota. MCP/Data quedan reservas si no aportan una necesidad concreta.
3. Cuando haya finalistas concretos/configuración revisable, ejecutar Plus Acceptance Gate: identidad sanitizada, disponibilidad/activación/tools/auth, cuotas, estado/recovery y suficiencia. Un smoke de Skill/estructura valida compatibilidad de entorno; no repetir veinte pruebas comparativas. Diferencias materiales requieren regresión focalizada. Hasta entonces seguir trabajo independiente en Team.
4. Presentar después comparativa técnica y económica y arquitectura material al propietario. No hay ahora una aprobación de runtime/Skill/plugin/MCP, ni de broker/Strategy V1/riesgo numérico, ni gasto, ni desbloqueo. No se requiere intervención humana para terminar documentos/probes de los pasos 1–2.
