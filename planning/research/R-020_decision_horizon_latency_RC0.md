# R-020 — Decision Horizon & Latency — RC0

2026-10-14 · contrato candidato de evaluación D008/011/021/022/025/028/034, exigido por ADR016. Sin estrategia ni SLA aprobado, sin cambios administrativos/cuentas. Target operacional personal Windows/Plus, aquí sólo diseño/probe sintético.

## Clocks y deadlines

Por oportunidad: event_time, source_available_interval, receipt_at, normalized_at, snapshot_cutoff, signal_at, risk_at, dispatch_at, broker_ack_at, fill_at. Clock quality/timezone/version y incertidumbre separadas. `usable_at` no anterior a extremo conservador de availability ni a receipt/cálculo requerido. Transcript del video y transaction_date no son source_available. Historical bar timestamp no es hora de recepción.

`DecisionHorizonCard`: familia/hipótesis, decision cadence, holding horizon, fuente/feed, cutoff, latency budget por etapa y end-to-end, expiry, **freshness_policy por input/quote/estado** con clock/edad/incertidumbre máximos, broker deadline, sessions/calendar, revalidación price/data/posición/reserva, missing/late/no-output, scenarios y evidence. Freshness se verifica aunque la señal aún no haya expirado; valores máximos siguen OPEN antes de freeze, no concedidos por holding horizon. Horizonte de mantenimiento largo no demuestra que la entrada tolere demora. Latencia admisible económica requiere evidencia; latencia técnicamente posible sólo exige cumplir clocks/deadline. Antes de expiración no basta si ya falla snapshot/protección/riesgo.

## Fichas propuestas comparables

| Familia | Cadencia/horizonte propuestos, no probados | Caducidad propuesta | Retrasos diagnósticos que preregistrar |
|---|---|---|---|
| VID-PRICE-EOD y MATR | Señal desde sesión cerrada disponible; ejecución en siguiente sesión autorizada; posiciones multisesión | Una oportunidad de ejecución definida; no arrastrar señal vencida automáticamente | Disponibilidad/cálculo+5/15/30/60min, perder auction, +1/2/5sesiones; aplicar reglas/cash/costs de nuevo |
| VID-F4-EOD / Congreso | Evento publicado/recibido, decisión EOD; holding H por cerrar | Event expiry y first eligible session explícitos; trade-date no reinicia edad | Receipt/canal+1/2/5sesiones y distribución observada si existe; decay/rights/clock gate |
| VID-13F-REBAL | Publicación nueva, holdings trimestrales conocidos, rebalance por publicación | Documento/amendment/version y próximo filing, no regla arbitraria de «vigencia trimestral» | +1/2/5/20sesiones; no quarter-end entry ficticia ni activos como muestras independientes |
| Shadow | Snapshot pareado y cutoff del comparador, queue/attempt separado | Deadline common del pairing; late no score contemporáneo | Timeout/retry/late/no-output, mismas fuentes históricas y privacidad; evaluación de trayectoria aparte |

Estos valores son escenarios de investigación, no presupuestos latency/expiry aprobados. Missing mandatory input => abstenerse de nuevas entradas y aplicar failure contract; no inventar HOLD por ausencia de output AI. Protección de posiciones vive en Financial Core/broker confirmado, nunca espera job Codex ni datos EOD delayed. Cotización delayed puede ser útil para research y aun así insuficiente para Risk/marks/protection.

## Evidencia broker que restringe diseño

[Alpaca orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca) documenta OPG, límite9:28ET y variación de auction; tabla marca combinaciones OPG con asterisco/contacto, fractional OPG no. Trailing standalone/RTH no equivale a ratchet por escalones. No asumir acceso real a auction por texto genérico. Exact deadline/tick/qty/permissions/map y parcial/replacement siguen B1–5 NOT_TESTED. Inferencia propia: si deadline se pierde, no asignar Open ideal; revaluar siguiente oportunidad **sólo** si CandidateConfig lo permite, sino EXPIRED.

SIP histórico retrasado puede servir como señal de sesión anterior; [FAQ Alpaca](https://docs.alpaca.markets/us/docs/market-data-faq) exige end fuera de últimos15min para consulta SIP sin subscription. Eso no otorga SIP actual para Risk ni histórico first-delivery/PIT/retención. La antigüedad del dato se conserva, no se cambia timestamp a receipt para fingir quote fresco.

## Scenarios y aceptación

H1 dato aún no disponible al signal cutoff -> no señal; H2 evento llega después de expiry -> EXPIRED; H3 cambia versión después de snapshot -> viejo intento no se reescribe; H4 ack tarde -> UNKNOWN/reconcile, no dispatch duplicate; H5 coste+demora altera fill -> precio nuevo/modelo validado; H6 sólo OHLC desconocido -> incertidumbre/cota conservadora, no trayectoria observada; H7 DST/early-close/holiday -> calendario exchange, no hora fija RD; H8 mandatory tool/job missing -> failure contract; H9 late Shadow -> LATE; H10 stop cruzado -> UNCERTAIN/reconcile y no0/top-up. Probe sintético evalúa sólo lógica declarada; timing/operación real target NOT_TESTED.

Contratos de finanzas G1+G2/ADR015 gobiernan incidentes. Caducidad no liquida posición ni cancela protección. Latency budgets, broker gateway resets y freshness numéricos se congelan con estrategia/datos/riesgo, antes de resultados y target workloads.
