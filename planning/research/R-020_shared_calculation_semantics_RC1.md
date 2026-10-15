# R-020/R-001 — semánticas cuantitativas previas a rendimiento — RC1

2026-10-13 · D-010/D-011 RESEARCHING. Especificación candidata, no elección MATR/Strategy V1, códigos operativos o backtest. Separa inputs/calculaciones técnicas de parámetros/arquitectura que requieren selección. [ADR-015 R2](../decisions/ADR-015-remaining-risk-reference-R2.md).

## Prices, unidades y accounting

Raw price/qty/corporate events y cash ledger son base contable. Una serie para indicadores puede normalizarse sólo con eventos conocidos/elegibles en ese cutoff, usando factor/version as-of explícitos. No usar el adjusted-history actual de vendor como vista conocida en2005 sin reconstrucción/evidencia. Indicador normalizado y stop raw se convierten con factor declarado; añadir dividend cash al P&L de una posición **una vez**, distinto de usar total-return para señal/benchmark. No duplicar P&L por posiciones raw y adjusted returns.

Stop confirmado y market marks están en la misma unidad raw/calendario/moneda; split rebase cambia precio/stop/H/entry y q inversamente bajo snapshot/evento verificado, no activa ratchet por artificial price discontinuity. Dividend accounting no trata caída ex-date como alpha/no-alpha por intuición; variante raw/split-only/total-return es dimensión preregistrada. Third-party `adjClose` útil para validación secundaria no prueba historical as-of ni legal retention.

## Fórmulas candidatas documentadas

Para closes elegibles C_t, `SMA200(t)=sum(C_(t-i),i=0..199)/200`; `ROC126(t)=C_t/C_(t-126)-1`. Equality de filtros (> estricto) no elegible. Warm-up mínimo según cada cálculo y calendario; 200 filas no equivalen a200sesiones si hay gaps/duplicados. Missing bar no relleno forward de retorno sin regla/data-status; failed calculation no señal.

`TR_t=max(H_t-L_t,abs(H_t-C_(t-1)),abs(L_t-C_(t-1)))` con inputs en escala as-of coherente. **Wilder ATR20 propuesto para baseline benchmark**, initial seed media de20 TR válidos consecutivos, luego `ATR_t=(19*ATR_(t-1)+TR_t)/20`. Media móvil simple20TR es variante distinta, no misma definición. Seed/order/calendar/gaps y precision deben pasar QP paridad antes de congelar M-03; no método seleccionado por retorno. ATR<=0/NaN o escala no validada bloquea elegibilidad/sizing, no división con0.

Ranking decreciente ROC126 y tie-break estable de ticker/securityID configurado; máximo3 y semana/día definido en CandidateConfig, no último día de filas existentes. Elegibilidad de salida diaria vs ranking de reemplazo semanal es propuesta pendiente, no default Champion aprobado. Señal sólo después de availability; orden jamás fill del mismo cierre que calculó señal. MOO/next-open/marketable-limit tienen clocks/límites distintos y sólo una semántica final se congela tras elegir broker/contract; precio OHLC no demuestra que la orden llegó a auction.

## Sizing y episodios

La ecuación histórica de MATR `0.005*E/stop_distance` y cap0.25 son cifras del borrador **no aprobadas**. Future config usa presupuestos aprobados y constraints independientes R2, exposure/cash/gap/liquidity/reservations. Posiciones llenas → mark verificado/protección confirmada; remainder/nueva autorización → p_auth conservador/condicional. El Risk Engine puede reducir/rechazar el target; espacio de riesgo libre no causa nuevo target ni top-up.

Episode/lot policy debe definir referencia/HWM al llenar, ante partials/adds y al salir; el P&L medio de posición no permite heredar high-water previo a la existencia de un lote sin regla específica. Un stop cruzado sin execution verificable da UNCERTAIN antes de clamp a0, incluso si siguiente precio rebotó. Protección/riesgo confirmados son estados efectivos y no desired values. Esas reglas vinculan candidatosvideo/MATR al mismo contrato de riesgo sin seleccionar estrategia.

## Dependencias y cierre pendiente

M-01/02/03 semánticas se proponen; M-04–08 requieren configuración exacta/episodios/órdenes/lotes/datos. M-09/10 requiere DatasetCard as-of/inception/liquidez/costs; M-11 sigue [OOS propuesto](D-011_OOS_policy_decision_RC0.md), ninguna muestra reservada abierta ni suficiente por parser PASS. R-009 QP1–10 y revisión independiente antes de selección técnica; mantener open fields en decision register sin convertir documento en aprobación por silencio. Pedagogía podrá mostrar raw-vs-adjusted, stops y clocks con fuentes/contrafactuales etiquetados.

## Avance técnico posterior — wave07

[R-020_PRICE_MATR_rule_configurations_RC0.md](R-020_PRICE_MATR_rule_configurations_RC0.md) especifica propuestas/gates, no método/dataset/Strategy admitidos. M1 aprobado/ADR019; Q059 guardrails distintas propuestas. E5/E6screens no statisticalacceptance, costos/scale/fuente/financialtarget pendientes. Versiones anteriores conservadas; no benchmark/margen cambiados por resultados.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](R-020_preregistration_readiness_RC6.md), [configEQ3](R-020_configuration_completion_RC1.md), [DataCards](R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](R-007_protection_dependency_contract_RC2.md), [RiskRC2](R-027_risk_formula_spec_RC2.md) y [engine/QE0](R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.
