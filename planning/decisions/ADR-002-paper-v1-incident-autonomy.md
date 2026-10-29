# ADR-002 — G1 + G2 y reanudación humana tras incidente material en PAPER V1

- **Fecha y aprobador:** 2026-10-01, propietario del proyecto mediante instrucción explícita.
- **Estado:** `DECIDED` para D-017, limitado a PAPER V1.
- **Prioridad:** P0.
- **Contrato afectado:** [política de riesgo RC1](../03_risk_policy_RC1.md), [PAPER V1 RC1](../paper_v1_capability_contract_RC1.md), [orden RC1](../04_order_contract_RC1.md).
- **Baseline:** [hoja v0.2 §5, §11–12, §32–33, §54](../../docs/master/hoja_de_ruta_sistema_trading_agentes_ia_v0.2.md) y ADR-001.

## Problema y alternativas

La hoja permite suspender, cancelar, reducir o liquidar según kill switch, pero advierte que `CLOSE_ALL` puede agravar un incidente. Sin una frontera aprobada, un componente podría convertir un timeout o una discrepancia de posiciones en órdenes de venta sobre estado incierto. [FINRA explica que un stop no garantiza el precio de ejecución](https://www.finra.org/investors/insights/stop-orders-factors-consider-during-volatile-markets); reducir exposición automáticamente tampoco garantiza un resultado financiero concreto.

| Alternativa | Alcance | Trade-off |
|---|---|---|
| G1 | Bloquear nuevas entradas y reconciliar | Minimiza acciones sobre estado incierto; deja exposición existente |
| G2 | G1 más cancelación automática de entradas pendientes identificadas y verificadas | Evita exposición nueva; exige controlar carreras cancelación/fill |
| G3 | G2 más reducción o cierre automáticos de posiciones | Puede disminuir exposición; puede empeorar ejecución, duplicar salidas o actuar sobre una posición errónea |

## Decisión aprobada

1. Ante **incertidumbre material**, el sistema bloquea nuevas entradas y pasa a reconciliación (G1). No infiere posición, cancelación o protección a partir de un timeout o silencio del stream.
2. Puede cancelar automáticamente **solo órdenes de entrada pendientes** cuya identidad, propósito y estado actual hayan sido identificados y verificados. La orden de cancelación y su respuesta se auditan; `cancel requested` no significa `cancel confirmed`. Si entra un fill durante la cancelación, se reconcilia el fill real antes de liberar presupuesto o tomar otra acción (G2).
3. Las órdenes protectoras se conservan. Cancelarlas o reemplazarlas requiere una regla específica documentada, probada y aprobada; G2 por sí solo no lo autoriza. Si falla o se desconoce su estado, se bloquean nuevas entradas, se verifica con broker y se escala conforme al runbook.
4. **G3 no está autorizado.** No existe permiso general de `REDUCE_EXPOSURE`, `CLOSE_ALL` ni liquidación automática por incidentes. Una reducción ordinaria prevista por una estrategia Champion aprobada sigue pasando por `TradeIntent → Risk → Execution`; no se considera permiso de liquidación de emergencia.
5. Tras pausa por discrepancia material de posiciones/órdenes, hard limit, fallo de protección u otro incidente clasificado como material, la vuelta a operación exige **autorización humana registrada**, además de reconciliación y checks de salud. Un heartbeat o reconexión no reanuda por sí solo. Incidentes transitorios no materiales podrán tener procedimiento distinto únicamente cuando esté especificado y probado.
6. Esta decisión no fija umbrales numéricos, tipo de orden, broker, ni reglas de reducción/liquidación automática. D-012, D-013, D-030 y D-031 conservan esos trabajos. Cambiar esta frontera exige nuevo ADR y aprobación humana.

## Responsabilidad y pruebas exigidas

Monitoring/Data Quality pueden **solicitar** suspensión o reportar incidente; un controlador determinístico aplica el estado aprobado. El Risk Engine deniega nueva exposición mientras el estado sea bloqueante. Execution solo emite cancelación elegible tras verificación y conserva trazas. Ningún agente LLM, Portfolio Manager shadow, Skill o MCP obtiene permiso de cancelación o reanudación.

Antes de PAPER autónomo se requieren pruebas de: timeout antes/después de aceptación broker, entrada con fill parcial durante cancelación, identificación errónea de orden protectora, stream caído, discrepancia de posición, hard limit, protección no verificable y reinicio con estado persistido. Cada caso debe demostrar ausencia de nueva entrada, ausencia de cancelación protectora por G2 y ausencia de reanudación automática de pausa material.

## Consecuencias

D-017 queda `DECIDED` para la **frontera de autoridad** de PAPER V1. El detalle de clasificación de incidentes, clocks, pruebas y runbooks se cierra en D-012/013/028/031 sin ampliar autoridad. `implementation_locked=true`. No se selecciona proveedor ni tecnología; Capability Discovery sigue activo para reglas, broker APIs, workflow y auditoría.
