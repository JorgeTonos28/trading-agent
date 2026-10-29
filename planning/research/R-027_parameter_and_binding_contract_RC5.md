# Risk / PRICE–MATR — parámetros y binding RC5

2026-10-29. Especificación candidata, **PARAMETER_PROFILE_NOT_APPROVED / CONFIG_NOT_ADMITTED**. Conserva R2/RC3–4, M1/K2/G-R1/DD-E, G1/G2 y no G3. No producción ni nuevos ensayos de estrategias.

## Fórmulas y redondeo determinables ahora

PRICE y MATR comparten cantidades raw enteras. q_target=floor((NAV_signal/3)/p_auth), luego restricciones actuales; target no se recalcula con un precio futuro. Buy-limit cap se redondea hacia abajo al grid vigente (no aumentar el cap por redondeo); si deja de ser marketable/no cumple spread, registrar no-fill/rechazo según política, no convertir a market. Un stop sell se redondea al grid sin aflojar previous confirmed protection; si la proyección hacia arriba cruza mark o viola regla broker, UNCERTAIN, no floor arbitrario que oculte riesgo. Sólo una salida normal de Champion en estado healthy y autorizada conserva su vía definida; incertidumbre/incidente no crea emergency exit. Regla final de tick/spread/p_auth/order policy sigue D030 antes de F0.

Reserva condicional q(p_auth−s_floor)+costes futuros no pagados sólo con floor protector defendible. R2 efectivo de qty descubierta es UNKNOWN. Si p0_running cae, no bajar desired anterior; si desired ≥mark, no calcular max(0,m−s) como riesgo0. Dividendo no rebasa stop automáticamente. Split transforma qty/precios/ATR de forma recíproca y exige confirmar órdenes; no asumir cobertura por conservación algebraica.

### Precio, ATR y factores en LEAN

Mantener input raw para órdenes/cash/contabilidad. Indicadores usan SPLIT_ONLY_ASOF construido desde acciones conocidas en cutoff; no confiar en una serie latest-adjusted o factor file con futuro porque el motor tenga un nombre SplitAdjusted. Declarar vintage/as-of y convertir ATR/stop a raw en el mismo corte. DailyPreciseEndTime/calendar/EndTime/cutoff explícitos; no fill al cierre que produjo la señal. Raw API volume versus volumen ajustado y dividendos reexpresados se normalizan conforme a DataCards. Los providers/handlers LEAN se envuelven sin sustituir Risk/Execution del proyecto.

## Registro completo de familias de parámetros

| Familia | Valor/modelo que falta | Cómo se cierra sin usar retornos para acomodarlo |
|---|---|---|
| Capital | USD10k referencia; cinco sensibilidades obligatorias ya aprobadas | Costes en todos2/5/10/25/50k, principal no elegible ex post |
| Exposición/cash | Gross, security, efectivo mínimo, settled cash elegible, denominador NAV/version | Preferencia económica absoluta+map broker; no margin BP ni dividendos modelados |
| R2/new/aggregate | Presupuestos por security/cartera y reserva condicional | Perfil dueño ex ante + escenarios/fórmulas; no interpretar menor R2 como add |
| Pérdida/DD absolutos | Soft/hard diario y HWM; reset/día/zona/depósitos/costes; precio/NAV para decisión | Política D031 con fuente fiable, sin equivalencia con DD relativo G-R1 |
| Protección PF | Tiempos, qty/cobertura, efectivo stop, incidente/acciones | Q064 dirección primero; bounds no se inventan desde SQLite o medias de red |
| Gaps/slippage | Shock conjunto por activo/FX/factor y costes de ejecución bajo congestión | Datos/modelo admisible y estrés explícito; stop-distance no garantía de pérdida máxima |
| Liquidez | ADV/volumen en unidades históricas, participación/spread/quote age | Fuente compatible y denominador no futuro; price-only EOD no prueba ejecución de stop |
| Concurrentes | Claims/replace equivalence, costes conjuntos, compare-and-commit/epoch | Contrato SQL/ledger+pruebas reales y reconciliación broker |
| Inputs/operación | Quote/staleness/skew, señal expiry, retry/cancel/replace clocks | Horizon/source/route y test target; SQL deadline no límite protector |

### Perfil del borrador: sensibilidad, no aprobación automática

El roadmap §11.3 propone25% por security,0.50% riesgo por posición,2% agregado, soft/hard diario1.5/2%, DD8/10%. Se conservan como **BASELINE_PROPOSAL_NOT_SELECTED**, no política restaurada ni parámetros finales. Para USD10k eso equivale respectivamente a2500/50/200/150/200/800/1000 dólares. Sin protector/floor/cash admisibles, esos importes no habilitan ninguna orden. No exigir aprobación de cada número aislado: presentar perfil integrado fundamentado cuando ruta/inputs/escenarios estén suficientemente definidos.

Especificar ex ante también sensibilidades de distancias de protección2/6/12% y shocks conjuntos5/10/20% como **ejemplos aritméticos adversos, no escenarios calibrados o límites aprobados**. Con precio ficticio100 y distancia6, un presupuesto50 admite como máximo8 shares antes de costes, aunque target3333 y cap2500 permitan más. Tres tramos iguales suman24% nominal del NAV, no75%; menor exposición puede explicar menor ES/DD y K2 debe mostrarlo. Con sólo capgross75%, shock10% equivale a7.5%NAV antes de costes: harddaily2% no garantiza cerrar a2%, especialmente sin G3. No ocultar esta diferencia al proponer perfil.

Si estos perfiles se usaran para evaluar resultados de estrategias, registrar todas las variantes/ensayos/multiplicidad **antes**, no elegir el mejor cap luego. Aquí son álgebra ficticia sin series/retornos; registro mantiene12declaraciones/0trials y JSON de reglas intacto.

## Binding por stage y fail-closed

Señal sellada → target congelado → quote/order cap/floor/cost snapshot → todos los controles → compare-and-commit durable autorización+claims+outbox F → dispatch sólo vigente → eventos broker reconciliados → book de posición/claims/protección. No flujo directo de LEAN, modelo, scheduler o SQL C a broker. Si DB no permite registro durable no seguir desde memoria. Si luego el broker puede haber ejecutado, conservar UNKNOWN y reconciliar, no liberar por fallo del proceso.

Antes de aceptar: inputs conocidos, relaciones entre controles/ratios/NAV y monotonía probadas, cantidades/fees redondeados coherentemente, escenarios de ganadora/perdedora/partial/gap/rápido adverso/crossed/replace/topup-reject; después APIs/DB/capacidad target. D035-T3: fórmulas de proyección/redondeo y parámetros requeridos especificados, no solver/engine/calibración aceptados. D035 y D031 permanecen abiertos.
