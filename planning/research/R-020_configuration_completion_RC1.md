# PRICE–MATR — cierre técnico de targets y calendario, RC1

2026-10-15. Se añaden **dos hipótesis de research EQ3** con ID/parent/version propios en [JSON RC1](candidate_configs/PRICE_MATR_rules_RC1.json), conservando10declaraciones previas e historial. Ninguna seleccionada como Strategy V1; ningún backtest. B/K2/M1/G-R1 gobiernan evaluación, no autorizan riesgo/operación.

## Target propuesto y justificación

Para nueva posición elegible, `target_notional=NAV_financial_signal/3`; cantidad target entera `floor(target_notional/p_auth)` en unidad raw, con política de lotes/tick. El adapter debe imponer floor/round_down: el redondeo bancario por defecto de un engine no puede aumentar qty autorizada. Precio conservador p_auth se fija con quote/modelo/expiry aprobados antes de dispatch; hoy presupuestos/freshness/buffer aún no aprobados. NAV signal conocido y reconciliado, no NAV al futuro open. q_target=0 es NO_TRADE_ROUNDING, no operación ficticia o aumento de capital elegido después.

Mismas3ranuras y regla para ambas hipótesis EQ3: no concentrar un tercio adicional en existentes por tener ranuras vacías; no top-ups/piramidación; no rebalancear posiciones que derivan sólo para restaurar tercios; no redistribuir automáticamente target rechazado/reducido. Risk limita/rechaza el target con cash/costes/reservas/exposición/R2/gaps/liquidez independientes. Target1/3 **no es un cap de riesgo aprobado**. Salidas futuras no liberan cash hasta reconciliación/settlement. Una misma posición parcial/remainder cuenta una ranura, no dos.

Racional ex ante: regla transparente común separa diferencias señal/salida de sizing optimizado; evita que un stop más corto produzca mayor exposición automáticamente. No prueba superioridad frente a sizing ATR/risk-budget; esa alternativa es variante distinta que requerirá parámetros/registro antes de resultados. Comparar tercios no iguala beta/factores ni riesgo; K2 mantiene límites de interpretación.

## Contrato temporal y estados

- Datos para indicadores split-only-as-of; ATR20 Wilder/tr/seed congelados en snapshot de señal, raw conversion y evento corporativo verificado.
- PRICE breakout126 excluye cierre actual; ranking de nuevas entradas ROC126/securityID, no reemplazo sólo por rank. Ratio10/5/5 ratchet sigue hipótesis propuesta, no reconstrucción literal ni números operativos aprobados.
- MATR filtros estrictos SMA200/ROC126, exit elegibilidad diaria; selección/reemplazo en última sesión semanal del calendario, no última fila existente. Si calendario/entrada requerido desconocido=>NO_SIGNAL_DATA_UNCERTAIN, no adelantar al jueves por CSV truncado.
- Warm-up individual W0 [DataCards](R-008_dataset_admission_wave04_2026-10-15.md): universo6constante, sin proxy preinception; no-ready no es cero/FAIL económico. Ambas fases2019–2022 requieren historia completa comparable; desarrollo conserva su tramo inicial con eligibility explícita.
- Propuesta de estado inicial de selección: allcash/flat con indicadores previos; sin peaks/posiciones heredados y sin resets anuales. Confirmación utiliza la misma regla fresh/flat definida **antes de F0/resultados de selección**, no elegida enF1. F1 materializa estado/configuración; carry es sensibilidad predeclarada sin escoger reset favorable. Integridad antes deF1; no abrir reserve para escoger estado.
- Expiry sólo entradas no enviadas siguiente cierre; órdenes enviadas requieren estado verificado. No expiry de protección ni venta estratégica durante pausa material. Ratchet seal/partial/HWM conserva RC0 y broker contract.

## Lo completado y lo realmente abierto

| Capa | Estado |
|---|---|
| Señales/cadencia/salidas/slots/target EQ3 | Especificados como hipótesis técnicas; no autorizados como Champion |
| Investigación de parametrizaciones |12declaraciones,0trials; family/selector no congelados |
| Inputs/datasets/rights/PIT/calendario | No admitidos; warm-up GLD contradice suponer200previos aene2005 |
| Risk numérico/cash/costes/capital | OPEN; target no los define |
| Entrada/tipo/TIF/p_auth, protección parcial/grupos | Mapping broker OPEN, QP/B3 antes de admisión |
| Método/DD claim, error/precision/calibración | NOT_ACCEPTED; no PASS estadístico desde fixtures |
| F0/Strategy/DoR | No congelados/seleccionados/alcanzados |

No llamar «configuración financiera completa» a estas reglas: todavía hay obligaciones necesarias para una ejecución determinable. El diseño agrupa decisiones técnicas menores aquí, sin pedir al propietario que invente reglas ni aprobarlas de una en una. La selección final y cambios materiales de riesgo/broker/estrategia siguen gobierno humano.
