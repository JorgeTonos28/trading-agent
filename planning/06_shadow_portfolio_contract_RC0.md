# Portfolio Manager Shadow — contrato y evaluación RC0

**Fecha:** 2026-10-05. **Estado:** `RESEARCHING` D-034/R-026. Detalla obligación ya aprobada A+, sin promover autoridad ni seleccionar runtime, estrategia, umbrales o broker. Usa [contrato común](06_agent_evidence_contract_RC0.md), ADR-004 PIT y ADR-006 controles independientes. Probe sintético != estrategia validada.

## 1. Entrada y salida

Desde fase **B4 — autonomous paper**, recibir snapshot pareado en los eventos/cadencia aprobados de cartera. Manifest y contexto financiero elegible idénticos al Champion; su decisión se une **después** del proposal. Inputs: holdings/cash/reservas/quotes disponibles, universo, señales y sus versiones, restricciones aprobadas, estado reconciliado, protección conocida y limitaciones. No secret/account credentials, herramientas de ejecución ni escritura del estado financiero. Fuente adicional exige comparación UNPAIRED, nunca ventaja atribuida al mismo contexto.

`ShadowPortfolioProposal`: identidad/job/versiones, `mode=SHADOW`, `authority=NONE`, snapshot/hash/corte, content_status, posiciones propuestas, prioridad, señales, reasons/falsifier, evidencia, riesgos/limitaciones, hipótesis de confianza, timestamps. Prioridad es ranking ordinal dentro de la propuesta (1 más alta), **no** prioridad en cola operativa. Confianza null/`UNCALIBRATED` hasta un protocolo de calibración; una etiqueta cualitativa no es probabilidad. No exportar `TradeIntent`, stop placement operativo ni orden.

## 2. Cantidades canónicas y recursos

| Action enum | Semántica usando `current_quantity` del snapshot y `target_quantity` propuesta |
|---|---|
| OPEN | current=0, target>0 |
| INCREASE | current>0, target>current |
| REDUCE | 0<target<current |
| CLOSE | current>0, target=0 |
| HOLD | target=current; delta calculada=0 |

Long-only: target nunca negativo; símbolo estable dentro del universo. Cantidades decimales en SHARE, fracciones solo si política/instrumento permite; no inventar tick/lot del broker. `ABSTAIN` pertenece al status y contiene lista de propuestas vacía con razón, **no** fila HOLD sin evidencia. NO_OUTPUT, failure y tardío son estados de entrega separados.

`quantity_delta = target - current`; `target_notional = target × reference_price`; `turnover_notional = abs(delta) × reference_price`: derivaciones verificadas, distintos nombres/unidades y quote/source ID as-of. No interpretar target_notional como cash requerido ni exposición existente como compra nueva. Precio sintético/indicativo no es fill. Recursos/costos conjuntos se evalúan a nivel propuesta para no gastar cash/reserva dos veces. Propuestas no factibles se conservan con violation flags; no se corrigen silenciosamente ni entran a riesgo operativo.

El riesgo propuesto se compara **offline** con modelo determinístico versionado separado: cash/exposure, protección estimada, gaps/slippage, liquidez y reservas relevantes, cada restricción con `EVALUABLE / UNKNOWN / VIOLATION`. No aprobación financiera ni garantías de stop/fill. No sumar pérdidas incompatibles ni tratar un límite desconocido como infinito. Parámetros y casos del probe son TOY, nunca porcentajes aprobados. Un PM puede sugerir la hipótesis de protección; no puede alterar protección real ni asumir stop ejecutado a precio perfecto.

## 3. Comparador y reloj de evaluación

Separar dos análisis:

1. **Decisión desde snapshot real común**: Champion vs propuesta de cada evento; coincidencia semántica instrumento/action/delta, divergencias, recursos y riesgos. Al evento siguiente ambos vuelven al estado real Champion. Esto mide elección local, no una cartera shadow acumulativa.
2. **Trayectoria contrafactual acumulativa**: cartera simulada shadow evoluciona con sus propias operaciones hipotéticas/fills y cash. Comparte la información exógena PIT, pero difiere en holdings; registrar esa diferencia y NO llamarla snapshot de cartera idéntico. Necesita engine y fill/cost model seleccionados en R-009/D-023 y pre-registro antes de ver resultados.

Decisión sin Champion visible, output sellado antes de evaluar outcomes. `generated_at` posterior al corte no añade información. `received_at > deadline_at` -> análisis retrospectivo, excluido de tasa on-time. Simulación comienza desde primer precio **transable después** de disponibilidad real/propuesta conforme a protocolo, con spread, fees, slippage, latencia, gaps, fills parciales, protección y corporate actions PIT. Dos vistas posibles: potencial idealizado al corte (etiquetado no ejecutable) y viabilidad desde recepción; no mezclarlas. No calcular P&L si faltan datos/fills/costos; `NOT_EVALUABLE`.

## 4. Métricas preregistradas (sin metas de retorno inventadas)

| Dimensión | Medida/denominador | Protección contra interpretación equivocada |
|---|---|---|
| Cobertura | jobs requeridos, completos válidos, abstención, fallo, no-output, late, unpaired; tasa on-time = accepted_on_time / required | Faltantes no desaparecen ni se llaman HOLD |
| Coincidencia | pares válidos con mismas acciones/deltas; similitud de pesos y prioridades donde aplican | Comparar canonización, no texto literal; reportar N/intervalos |
| Divergencia | instrumento/action/sizing, señales/fuente, razones, cambios entre intentos | Igual decisión puede venir de evidencia inválida |
| Riesgo | distribución exposición/cash/reservas, protección/gap estimados, liquidez, flags por restricción | UNKNOWN separado de cumplimiento; ningún check shadow autoriza operación |
| Resultado | net return, drawdown, turnover/cost, benchmark, ventanas OOS, si simulación admisible | Sin backtest aquí; no inferir alpha de fixtures ni fills perfectos |
| Estabilidad | proporción de decisiones canónicas que cambia en repetición de idéntico contexto; sensibilidad a ruido permitido | Modelo/prompt/Skill/snapshot fijados; texto variable no basta para fallar |
| Reproducibilidad | replay determinístico de admission/cálculos/compare idéntico; variación generativa explícita | No prometer mismo output LLM bit a bit |
| Error | schema/rol/PIT/lineage, fuente inventada, tool no autorizada, presupuesto hipotético excedido | Todos se cuentan, outputs rechazados conservados |
| Utilidad incremental | calidad/cobertura/falsifiers útiles vs workflow mínimo, latencia/cupo/complejidad, evidencia OOS posterior | No seleccionar por narrativa persuasiva; revisión independiente y owner antes de autoridad B |

Congelar universo, períodos, splits/OOS, baselines, casos, costes/fills, métricas, repeticiones y criterio de promoción **antes** de resultados, una vez Strategy V1/datos/engine estén definidos. R-026 no se cierra con esta especificación ni con prueba de un OPEN toy. Cualquier promoción SHADOW→autoridad limitada requiere nuevo ADR humano, no automatismo Champion/Challenger.

## 5. Failure y gates

Fallo de tools/evidencia -> INSUFFICIENT_EVIDENCE o ABSTAIN, sin filas hipotéticas fabricadas. Snapshot de cartera incoherente/protección incierta -> proposal abstain/research limitation; reflejar incidente financiero y G1+G2, jamás reanudar/cerrar automáticamente. Falta de cuota -> pérdida de cobertura observable y recovery; DoD no completo sin shadow operante conforme a workload aprobado.

Antes de PAPER: frontera técnica aislada de Risk/Execution, trusted role/schema y lineage, late/no-output/duplicate, unpaired, múltiples posiciones/reservas simultáneas, OPEN/INCREASE/REDUCE/CLOSE/HOLD/ABSTAIN, quote stale/missing, costs/gaps/partial fills/corporate actions, restart/auth/quota y replay. RC0 especifica estos casos; wave 06 ensaya un subconjunto explícito. Plus Acceptance solo disponibilidad/operación; no sustituye estos gates financieros y de seguridad.

## 6. Build vs. Reuse

Recomendación C-017b: **ADAPT** thesis-tracker Apache-2.0 (commit 574ed362) como procedimiento breve; mantener tesis/catalyst/falsifier, retirar autoridad original. C-010 mínimo es baseline. `jsonschema` y Decimal se reutilizan para probes. Transporte C-025a **WRAP** candidato; MCP **WRAP** reserva si interoperabilidad material. Engine/eval libraries no elegidos: R-009 antes de construir simulador/portfolio analytics. No construir motor de cartera en preparación. Referencia del activo y atribución están en la Skill desechable/wave 05.

## Vigencia de entrega posterior ADR-011 / hardening RC0

Dirección core local + jobs Team automáticos aprobada; D-020 DECIDED en disposiciones de diseño, D-024 RESEARCHING. Textos anteriores de siguiente Plus/selección pendiente son historia de sus hitos. Plus solo PRE-LIVE ADR-010. [Workflow/recovery y mapping delivery-contract-v2](08_job_workflow_recovery_contract_RC0.md) separa workflow/attempt de enums de entrega originales, que se conservan para probes v1; no cambia content_status ni autoridad. Leases/identidades/epoch/namespace se validan fuera del modelo; no-output no es HOLD. Permisos finales y motor permanecen abiertos.

## S2 — blinding distinto de seguridad

[S2 RC1](08_S2_isolation_spec_RC1.md) y [BL-01–09](research/R-013_S2_acceptance_matrix_RC1.md) mantienen Shadow separado de Champion/pedagogía/join/cache/otros intentos. Contexto as-of común incluye holdings reales previos legítimos; decisión contemporánea excluida. DAG/visibility policy confiables y export invariante a decisión Champion; top-level field allowlist no evita contaminación dentro de una señal. Digest/pair-id del contexto predecisión, no hash de decisión secreta; seal en store externo antes de join. Fallo blinding invalida comparabilidad y se registra sin alterar posiciones/riesgo/denominadores. Probes NA son toy/counterexamples, no BL PASS. Cross-identity acceptance y engine/outcomes permanecen pendientes.
