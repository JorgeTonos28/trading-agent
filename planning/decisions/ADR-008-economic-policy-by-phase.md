# ADR-008 — Política económica por fase y adquisición de metodologías

**Aplicación de entorno ADR-010:** PAPER usa Team actual, no Plus. La política económica decidida aquí permanece vigente; Plus individual es candidato PRE-LIVE. Ninguna suscripción implica facturación API incluida.

- **Fecha:** 2026-10-02.
- **Estado:** `DECIDED`, instrucción explícita del propietario; D-036, P0.
- **Alcance:** todas las capacidades y proveedores externos presentes y futuros. Complementa ADR-007 y prevalece sobre su anterior exigencia de aprobación para **estudiar/considerar** gasto.

## Decisión

La prioridad global es obtener la mayor calidad, fiabilidad y capacidad posible al menor coste razonable. Gratis/open source/free-tier tiene preferencia cuando cumple los requisitos; no compensa una diferencia material de calidad, fiabilidad, disponibilidad, datos o rendimiento. La selección conserva gates de seguridad, licencia, calidad y autoridad financiera.

**PAPER V1 — Zero/Low Incremental Cost First:** priorizar suscripciones existentes (entitlement verificado en el entorno objetivo), free tiers, APIs gratuitas suficientes, open source, software/infraestructura local razonable, datasets públicos y cuentas paper gratuitas. El propósito es demostrar la arquitectura, medir y aprender antes de aumentar costes. Una alternativa paga puede estudiarse y registrarse sin autorización adicional; contratar, activar facturación o generar cualquier gasto incremental requiere aprobación explícita del propietario. Un free tier que requiere cuenta de facturación/cargos automáticos no autoriza activarlos. Que una opción quede fuera del presupuesto PAPER no la convierte en `REJECT` permanente ni justifica reducir silenciosamente criterios de calidad.

**LIVE/producción — Economic Value First:** servicios pagos son candidatos válidos si evidencia suficiente muestra mejora material de calidad, cobertura, latencia, continuidad, seguridad, fiabilidad o capacidad de generar/proteger retorno. Comparar economía unitaria, coste total y beneficio esperado con incertidumbre; precio bajo por sí solo no decide. Investigar API/modelos OpenAI/Anthropic, market/alternative data, brokers, conectores, almacenamiento, cloud/infraestructura, observabilidad y otros servicios. Pagar y pasar a LIVE siguen requiriendo aprobación; este ADR no selecciona ningún proveedor, presupuesto, capital ni umbral de retorno.

**Skills, prompts, agent templates, reference workflows y metodologías:** adquirir únicamente activos gratuitos, públicos, incluidos en capacidades existentes o creados/adaptados por nosotros, con licencia compatible. No comprar una Skill/template. Puede justificarse pagar posteriormente por su modelo/runtime, datos o infraestructura; registrar esas dependencias por separado. Gratis no elimina costes de integración, mantenimiento o ejecución.

## Ficha y evaluación obligatorias

Cada candidato externo distingue `PAPER_V1_VIABLE_FREE`, `PAPER_V1_COST`, `LIVE_COST`, `FREE_ALTERNATIVE`, `PAID_INCREMENTAL_VALUE`, `ECONOMIC_JUSTIFICATION_REQUIRED`. Aplicar el [scorecard común](../economic_scorecard.md) con costes fijos, variables, estimado mensual, escala, alternativa gratuita, diferencia de calidad/capacidad, lock-in, beneficio operativo y condición concreta para justificar pago. Valores desconocidos siguen `UNKNOWN`; no escribir coste cero para datos/runtime por ser público un SDK o prompt.

La disposición Build-vs-Reuse se registra **por fase y por capa** (metodología, runtime, datos, infraestructura). `REFERENCE_ONLY` en PAPER por presupuesto no es un veto a `WRAP/ADAPT` futuro en LIVE. Documentar condiciones de reevaluación; diseñar límites e interfaces revisables antes de seleccionar componentes finales.

## Compatibilidad con decisiones vigentes

ADR-007 conserva alcance agéntico OpenAI + Anthropic, objetivo PAPER en ChatGPT Plus individual y distinción frente a Team de investigación. Tier 0/1 siguen preferidos para PAPER; Tier 2 puede estudiarse y tiene ejecución/contratación bloqueada hasta autorización de gasto. El Agent Capability Gate D-020/D-024 y el desarrollo bloqueado permanecen vigentes. Un fallo del gate Plus permite preparar alternativas pagas revisables, pero no activarlas ni aprobarlas automáticamente.

La aprobación humana de gasto deberá identificar servicio, uso/fase, presupuesto o límite de consumo, facturación y duración/condición de revisión. Ese detalle se define al presentar una opción concreta; no existe aún aprobación de gasto ni umbral económico numérico.
