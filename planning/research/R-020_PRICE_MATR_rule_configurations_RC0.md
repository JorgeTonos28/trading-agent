# PRICE–MATR — configuraciones de research propuestas y obligaciones restantes

2026-10-14. **Research rule configurations**, no Strategy V1 aprobada/freeze o backtest ejecutable. [Config JSON](candidate_configs/PRICE_MATR_rules_RC0.json) fija hipótesis propuestas; presupuestos de riesgo/source/broker/estimadores siguen abiertos. Nuevas parametrizaciones tienen IDs/parent/hash separados; no reescribir declaracionesS-PRICE-01/S-MATR-01.

## Común

Cohorte6ETF, long-only sin adds/leverage/shorts/derivados. Indicadores split-onlyas-of, raw orderunits/cashdividends y warm-up consecutivo/validatedcalendar. SMA200 incluyendo cierre, ROC126, WilderATR20 seeded20TR; parámetros de research de baseline, no óptimos ni aprobados para operar. Dailydecision después de availability; siguiente sesión, expiry al siguiente cierre; modelo de fill conservador y orden real quedan dependientes de broker/paridad, no Open(t+1) garantizado.

Una entryintent viva porsecurity/episode, retries mismoevento idempotentes. Protección inicial3ATR20 candidata porfilledqty inmediata, p_auth/conditionalstop y R2 aprobado conceptual; nums de cap/riskbudgets **NULL**. MAX_POSITIONS3 es propuesta de comparación, no cap financiero aprobado. Risk multipolicymin/claims y cashsettlementexternos, falla/reconciliaciónG1+G2 sin G3; no sizing del LLM.

Stop inicial propuesto: ATR20 congelado en snapshot elegible del cutoff que genera señal; convertido a raw con factor as-of y rebasado sólo por evento corporativo verificado posterior. p0 provisional = promedio de fills reconciliados ponderado porqty **sin fees** (fees en ledger separado). Paraqtyllenada, desired_initial=max(previous_desired,p0_provisional-3*ATR_signal_raw_rebased), sin bajar protección de fills previos por modificar promedio. Remainder/nuevaentrada conserva p_auth conservador y stopconditionalautorizado, no marcarse filledqty. Deseado/confirmado distintos; si formula/qty/cancelreplace no tiene mapping broker seguro, variante NOT_ADMITTED. No permiso para crear/reemplazar protección por documentación; obligación efectiva requiere pruebas/contrato broker.

Precedencia: UNCERTAIN/materialpause→reconciliación y sólo G1+G2 autorizados, conservación de órdenes protectoras y reanudación humana; no nuevos exits/ratchet/entries de estrategia mientras siga pausa material. Broker puede ejecutar protección ya vigente. Healthy reconciliado→salidas/protección primero→reemplazo verificable→entrada. Desirednuevo sobre mark genera razón estratégica sólo cuando healthy, no salida durante pausa ni retroactivefill; protección existente cruzada/no ejecución sigue incidente antes de esa ruta.

Expiry por tipo: NEXT_SESSION_CLOSE sólo para nueva señal/intención de entrada no enviada o autorización caducada; entrada ya enviada exige cancel/reconcile verificados, no borrarla ni reutilizarcash por reloj. Protección de posición no expira con señal; GTC/brokerexpiry específico queda OPEN obligatorio y monitorizado antes de freeze. Salidas/reconciliación y materialpause tienen estados propios, no «expiran» para autorizar órdenes nuevas. Slots cuentan securities únicos con posiciónqty>0 **o** entrypendiente/reservada; remainder de misma posición no dobleslot. Ventas esperadas/settlement no cash disponible hasta reconciliación.

Target de Strategy no lo genera Risk: allocation/notional target determinístico debe fijarse con numericbudget/config aprobada; hoy **OPEN obligatorio**, no «tomar máximo riesgo disponible». Risk sólo limita/rechaza ese target bajo controles independientes. Por ello rules detalladas no son configuración financiera completa ni ejecutable.

## S-PRICE-01-CFG-P1, parent PRICE01

Close(t)>max126closes previos excluyendo t. Hasta3posiciones, orden ROC126desc ysecurityIDestable entre nuevas entradas; no desplazar posición existente sólo porque nuevo ranking cambia. Una señal ya consumida no vuelve a ordenar. Reentrada exige nuevo cutoff/signalID tras flat reconciliado y estado healthy.

Ratchet porcentual escalonado **propuesto** a=.10,h=.05,b=.05: inspira los mecanismos narrados, no declara reconstrucción literal/resultado ni parámetros aprobados. Activar cuandoH≥p0(1+a), k=floor(log(H/[p0(1+a)])/log(1+h)), anchor=p0(1+a)(1+h)^k, desiredstop=max(previous_desired,anchor(1-b)). Precisión en unidades/threshold/ties y round conservador hacia abajo a tick grid en modelo de orden, sin llevar desired a confirmed por default.

Seal trasentryfill completo o remainder cancelado verificado. H inicialp0 y luego highs de **barras completas cuyo inicio≥seal**; no heredar high anterior al lote ni toda la barra del fill parcial. Se reconoce retraso/conservadurismo de ese modelo; datos intrabar permitirían otra variante, no cambiar tras resultados. Initial protection cubre parcial antes de seal. Rebase de split de p0/H/stop/qty; dividendocash no ratchetretroactivo.

Si desiredstopnuevo está sobre el mark actual, no instalar stop como si hubiera protegido antes: generar razón de salida por regla en siguiente oportunidad autorizada, con price/gap/fill admisible. No cancelar protección vigente mientras no haya ruta probada. Stopvigente cruzado/missing/unconfirmed produce incertidumbre y financiero fail-closed, no riesgo0. Entradas no se permiten por menorR2; ladderaveragingdown excluido deesta variante, permanece research aparte.

## S-MATR-01-CFG-M1, parent MATR01

Filtros estrictos Close>SMA200 yROC126>0, top3ranking ROC126/securityID. Exit elegibilidad diaria; ranking/reemplazos al cierre de última sesión de semana del calendario, ejecución siguiente oportunidad. No rellenar slots intraseamana en esta parametrización; original baseline de entrada/cadence permanece referenciado, no se sustituye silenciosamente. Stopinicial3ATR20 fijo yrebase corporativo, sin ratchet. Sizing/protección/p_auth/failure samecommoncontracts.

## Reglas detalladas, configuración financiera incompleta

No confundir RULES_PROPOSED_WITH_NUMBERS con F0_CONFIG_FROZEN o financialconfigcomplete. Falta risknumeric, brokerordermapping/fees/slippage/latency/freshness, fuente prices/actions/cash, formatos/paridad y approvedStrategy. Ambas realizaciones se registran como nuevas variantes no ejecutadas, propuestas para comparación y sensibilidad previa; hipótesis que falloDataCard permanece NOT_EVALUATED, no económicamenteFAIL. No seleccionar S-PRICE porque sea interpretable niMATRporque lahojalonombró.

Comparación integral usa las salidas diferentes; ablations mantienen **reglas/políticas**, permitiendo ledgers divergentes. Forzar mismosfills/qty para aislar mecánica =MODULE_ONLY, no cartera factible. Gap/intrabar ambiguity model y costes se preregistran, no stops fills perfectos retrospectivos. Todo cambio posterior genera versión/trial y posiblemente nueva confirmación.
