# Revisión crítica financiera — R-020/R-021/R-007/R-009/R-027

2026-10-13 · Reviewer existente `independent_hardening_review`, distinto del autor. Lectura de documentos/source/captura y contraste puntual fuente primaria; no ejecutó probes, editó, aprobó owner ni auditoría de producción. Requerida por hoja §3.16 para decisiones críticas. No expansión R-006/010/013.

| Hallazgo | Prioridad | Reparación verificada en segunda lectura |
|---|---|---|
| Reference «mark/entry» de nueva cantidad ambigua | P1 | Mark sólo posiciones llenas; remainder/reserva usa p_auth conservador único, protección condicional según mapping probado. Precio de valoración no garantiza fill market |
| C_free y reserva propia revalidation indefinidos | P1 | C_base confirmado/eligible settlement, encumbrances exclusivos y broker control separado. Reemplazo atómico own claim sin liberación global/doble cargo; broker vivo no authorization nueva |
| R-020 llamaba G2 a protección/reemplazo | P1 | G2 sólo entradas pendientes verificadas; PROTECT/replace normal por RiskDecision; excepción protección requiere regla probada/documentada/aprobada |
| Episodio/lotes/partial/top-up/splits | P1 antes de freeze de reglas | OPEN obligatorio; p0/H/q/stops/counter coherentes y rebase as-of, sin high-water de cantidad aún no existente |
| Script algebraico original sobrescribe nombre01 al rerun | P2 | Fuente/result01 íntegros, prohibir rerun original en README; next-source create-exclusive y rechaza existente, NOT_EXECUTED. No repetir para borrar hallazgo |

## Dictamen acotado

Segunda lectura confirma reparaciones y ausencia de P0/P1 que impida **presentar referencia de riesgo R2** al owner. R1/R2 ejemplos correctos; R2 puede admitir más riesgo restante en posiciones perdedoras que R1, hecho explícito que exige gobierno, no mera redacción. Mantener loss/drawdown independientes.

Fuente/hash algebra01 coincide, resultado8/8 sintético del autor. Precisión de claims/p_auth y transacciones no se atribuye a ese PASS. R-021 conserva PIT/rights UNKNOWN; R-007/R-009 broker/engine no seleccionados. No nueva autoridad LLM ni G3.

No cierre D-035 completo, approval de números/Strategy/broker/engine/Plus/host, transacciones ni ejecución. R-008 wave02 y R-011/012/014 demand posterior no revisados independientemente en este dictamen; Plan Architect verifica coherencia documental, no extender scope del reviewer.
