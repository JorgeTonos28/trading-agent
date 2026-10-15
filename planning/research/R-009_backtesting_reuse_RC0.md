# R-009 — motores quant, Build-vs-Reuse y protocolo de paridad — RC0

2026-10-13 · P1 D-023 RESEARCHING · No motor seleccionado/instalado, backtest ejecutable ni dataset consultado. Quant/datos/infra fuera de limitación de frameworks AI. Engine local es software determinístico; no recibe agente como autoridad financiera ni sustituye Risk/Execution del proyecto.

## Candidatos/rutas separados

| Ruta | Evidencia primaria / disponibilidad | Compatibilidad y trabajo pendiente | Disposición candidata |
|---|---|---|---|
| LEAN engine source | [Repo/readme](https://raw.githubusercontent.com/QuantConnect/Lean/master/readme.md), [Apache2](https://github.com/QuantConnect/Lean/blob/master/LICENSE); modular/event-driven, build Windows documentado | Pin engine/.NET/Python/deps y build reproducible; PIT/corporate actions/stop models/event adapters y export de trace deben probarse. Integración propia no autoriza bypass Risk | REUSE_AS_IS engine + WRAP/ADAPT contratos/imports |
| LEAN CLI/local-platform commercial route | [Installation](https://www.lean.io/docs/v2/lean-cli/installation/installing-lean-cli) exige paid organization y Docker para correr local vía CLI | No confundir source license con acceso gratis al wrapper/CLI/Cloud/datos. No instalar Docker/WSL/admin ni contratar. Raw build investigable sin asumir coste de mantenimiento cero | REFERENCE_ONLY / paid reserve para PAPER; no REJECT futuro LIVE |
| NautilusTrader | [Installation](https://nautilustrader.io/docs/latest/getting_started/installation/), [LGPL3](https://github.com/nautechsystems/nautilus_trader/blob/develop/LICENSE). Latest docs actualmente2.x RC, pip estable1.x con API distinta; Windows Server CI listado, personal Windows por comprobar | Pin stable version y docs correspondientes; no usar ejemplos2.x con1.x ni RC como production default. [Bar execution](https://nautilustrader.io/docs/latest/concepts/backtesting/bar-execution/) usa trayectoria sintética, no historia intrabar observada. Corporate actions/adapter/cash/mapping por probar | REUSE_AS_IS + WRAP/ADAPT candidato; sin dependencia Redis obligatoria asumida |
| Backtrader/vectorbt | Inventario previo conservado | Licence/version/maintenance, corporate actions, fills/PIT/calendario y encaje event-driven no investigados suficientemente en esta wave | REFERENCE_ONLY hasta ficha; no rechazo ni selección |
| Engine propio general | Ninguna necesidad material de BUILD demostrada | Duplicaría estados/costs/actions/fills; un fixture/calculadora no es sustituto reusable | BUILD no recomendado antes de gates de engines existentes |

EXISTS=YES source/docs LEAN/Nautilus; AVAILABLE_TO_US=source YES, build/ruta target UNKNOWN; TECHNICALLY_COMPATIBLE=CONDITIONAL; ECONOMICALLY_REASONABLE=UNKNOWN integración/operación; SELECTED=NO. Un repo licencia libre no incluye histórico comercial ni todos sus conectores con rights.

## Economia por fase

| Ruta | PAPER_V1_VIABLE_FREE | PAPER_V1_COST | LIVE_COST | FREE_ALTERNATIVE | PAID_INCREMENTAL_VALUE | ECONOMIC_JUSTIFICATION_REQUIRED |
|---|---|---|---|---|---|---|
| LEAN raw source | CONDITIONAL build/data/license | Engine US$0; fixed hardware/variable data/build/maintenance UNKNOWN | Operación/data/scale UNKNOWN | Nautilus/otros OSS por validar | Wrapper hosted/support/continuity si gap medido | YES antes de gasto |
| LEAN CLI/Cloud | NO uso CLI gratis demostrado por requisito paid | Subscription cotización UNKNOWN, no aprobada | Fees/nodes/data/scale UNKNOWN | Engine raw + datos permitidos | Menor setup/ops y support si demostrado | YES expresa |
| Nautilus pinned stable | CONDITIONAL personal-PC/data/license | Engine US$0; deps/hardware/data/ops UNKNOWN | Idem + escala UNKNOWN | LEAN raw/otros | Servicio/data/support si mejora material | YES antes de gasto |

Supuesto mensual: un investigador/candidato por proceso, volumen/history y batch desconocidos. Lock-in DTO/data catalog/event semantics/adapter, salida via raw/versioned traces; coste de portar por medir. No monetizar mejora de rapidez sin benchmark ni inferir alpha del engine. Local PC coste hundido vs mantenimiento asignado separados.

## QP1–10: benchmark de semántica, sin rendimiento de estrategia

Protocolo para target/research compute autorizado con datos **sintéticos**, previo a históricos: fuente/pin/config/seed/raw fixture/hash y expectativas independientes; mismo calendario/política/fees en cada engine. Un backtest executable real de candidatos está reservado PC personal según ADR-013.

1. QP1 barra llega tarde, next-open vs same-close y no fill antes de availability.
2. QP2 split/dividend raw vs adjusted as-of, unidades/cash y doble contabilidad.
3. QP3 gap cruza stop, stop-market vs stop-limit no-fill y orden de eventos.
4. QP4 OHLC con dos trayectorias posibles: reportar incertidumbre, no vender como tick path real. Resolución superior o cota conservadora preregistrada.
5. QP5 entry parcial/stop qty, cancel/replace/fill simultáneo y doble OCO.
6. QP6 fees/spread/cash/rounding y lotes/reservas, sin cash de venta pendiente.
7. QP7 duplicate/corrected/amended events, universe as-of/delistings y clocks externos.
8. QP8 calendarios feriados/early-close/DST/session/corporate actions.
9. QP9 trace/replay/version, estado y snapshot exportable para Quant/Shadow/Ped sin output operativo LLM.
10. QP10 repeatability/memory/time bajo volumen representativo; version regression sin latest. Perfil target, no benchmark Team=personal.

QP1–10 **NOT_TESTED**; pass syntax/docs no paridad. Ningún motor se puntúa por CAGR o chart favorable. La recomendación actual es shortlist LEAN raw y Nautilus stable con rutas económicas separadas; elección D-023 requiere fiche/pin/benchmark y coste comparables.

## OOS pendiente y secuencia

MATR propone2005–2018 research,2019–2022 selection-validation,2023–2026-09-30 confirmation; familias disclosure pueden no cubrir mismo período. Dataset insuficiente no se rellena ni cambia ventanas silenciosamente. Comparación por cohortes/data quality, política de exclusión/common period antes de resultados. Muestras usadas para escoger dejan de confirmar; freeze regla + selector + umbrales antes de la muestra confirmatoria, failed confirmation exige nueva versión y evidencia futura. [Preregistro](R-020_strategy_admission_preregistration_RC1.md).

Después de datos y configs: benchmark QP, scorecards ex ante y selection de diseño con owner D-008; no Champion operativo por selección documental. Validación cuantitativa/forward/PAPER sigue gates antes de operar/promover, según evidencia y roadmap. No reabrir arquitectura agéntica para elegir un motor quant.

## Wave08 vigente — 2026-10-15

ADR020/G-R1 y ADR021/nominal10k aprobados, sin método/Strategy/engine/broker/datos/Risknumeric aceptados. [RC6](R-020_preregistration_readiness_RC6.md), [configEQ3](R-020_configuration_completion_RC1.md), [DataCards](R-008_dataset_admission_wave04_2026-10-15.md), [brokerRC2](R-007_protection_dependency_contract_RC2.md), [RiskRC2](R-027_risk_formula_spec_RC2.md) y [engine/QE0](R-009_engine_components_wave02_2026-10-15.md) completan este bloque técnico en scope explícito.12declaraciones/0trials,4cards+6subcards NOT_ADMITTED;2nuevasEQ3 son hipótesis con target, no configuración financiera lista.

Investigar DD-E ya está autorizado, sin nueva elección humana por una definición candidata: d_obs reporte, no veto histórico agregado. Fresh/flat de selección/confirmación y carry sólo sensibilidad se fijan antes deF0, no se eligen al ver selección. E7=14/14aritmética no inferencia; QE0=2PASS2ERROR→4PASS1ERROR→6PASS0ERROR sólo componentes/initvacío, sinrun; QE1ROUND=5/5componente no adapter. P1reparados y revisión documentada, no statisticalvalidation/DoR/target.

Costes obligatorios en5escalas2k/5k/10k/25k/50k y todos modelos admitidos, conservando20celdas; principal10k no selecciona celda favorable, UNKNOWN explícito. Derechos/retención/usoIA/historia/calidad aún faltan. [Consultas de proveedor](R-008_vendor_clarification_requests_RC0.md) preparadas no enviadas; autorización/remitente personal o envío del propietario requeridos antes de contactar terceros. No declarar bloqueo global dePreparation mientras tareas independientes siguen posibles. HoldoutUNKNOWN/locktrue/targetdeferred, main/release intactos.
