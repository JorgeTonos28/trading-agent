# R-027 — escenarios de aceptación R2 y condiciones ADR-015 — RC1

2026-10-13 · P1 D-035 RESEARCHING. R2 conceptual aprobado, fórmula final/pruebas/inputs/números aún abiertos. Documento de expectativas, no Risk Engine. [ADR-015](../decisions/ADR-015-remaining-risk-reference-R2.md) gobierna.

| Caso | Evidencia/salida exigida | Fallo que debe detectarse | Estado de prueba |
|---|---|---|---|
| Posición ganadora, stop válido sobre entrada y bajo mark | R1 atribución separada, R2 positivo hasta protección y P&L observado separados | R1=0 tratado como falta de exposición futura | Algebra01 aritmética parcial; engine NOT_TESTED |
| Posición perdedora, protección válida | R2 desde equity actual, pérdida no realizada y límites independientes | R2 menor crea compra automática/oculta pérdida | Algebra01 parcial; señal/límites engine NOT_TESTED |
| Fill parcial4, remainder6 de orden10 | Cobertura exclusiva posición4 + pending6 con p_auth, fees únicos y protección por qty real/condicional | 4+6+reserva6 doble, o ignorar pending por posición4 | Algebra01 parcial; lifecycle/txn NOT_TESTED |
| Top-up autorizado por nueva señal | Eval integral de posición existente+nuevo lote, ownclaim/reprice y episodio/protección versionados | Mark favorable o caída de R2 usada como señal/tamaño automático | Contract definido; NOT_TESTED |
| Top-up sin señal/regla válida | Rechazo sin intent operativo/orden, trazabilidad | Fórmula min-cap llena presupuesto libre por sí sola | NOT_TESTED |
| Gap cruza stop sin fill verificado | UNCERTAIN, valor no evaluable, reconciliación/entradas bloqueadas según G1+G2 | Clamp a0 o asumir fill a stop; liquidación general G3 | NOT_TESTED |
| Movimiento rápido/cross/rebote entre observaciones | Preservar secuencia/provenance, trigger/fill desconocidos no borrados por marca recuperada | Último quote favorable oculta stop cruzado/orden incierta | NOT_TESTED |
| Stop ausente/qty insuficiente/pending cancel/reject | No confirmado, incertidumbre/exposición visible, protección no borrada por G2 | Desired stop contado como real o riesgo0 | NOT_TESTED |
| Estado financiero cambia después de autorización | Revalidación own claim sólo autoriz. no despachada; estado/generación/expiry, txn | Resubmit de orden viva, reserva liberada o doble cargo | Fixture papel ilustrativo; txn NOT_TESTED |
| Split/dividendo/cash settlement/costs | Raw units/qty/basis/R1/R2/P&L coherentes as-of; cash eligible sin doble débito | Falso HWM, stop crossed contable, dividendo doble o cash ficticio | NOT_TESTED |

Fuente/result algebra01 originales intactos; no rerun ni widening permissions. Próximas verificaciones desechables pueden contrastar expectativas, pero no promocionar a cobertura/ejecución real. Backtests e integración ejecutables target PC personal conforme ADR-013, acceptance agéntica R-030 separado. No valores de riesgo productivos aprobados.
