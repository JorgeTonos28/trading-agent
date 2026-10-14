# R-008 — derechos de retención frente a auditabilidad — RC1

2026-10-13 · P1 D-022/026/028, fuente/data no seleccionado. Actualiza el UNKNOWN de [wave02](R-008_market_data_evidence_wave02_2026-10-13.md); no se descarga dato ni contrata. Revisión documental técnica de compatibilidad, no dictamen jurídico.

## Hallazgo primario y disposición por scope

[Tiingo ToS](https://app.tiingo.com/tos/), updated2026-10-06, §1.6: Starter/trial restringen persistir **datos y Derived Products**; paid plans permiten retención condicionada a vigencia y borrado al terminar/downgrade; excepciones por acuerdo separado tienen alcance limitado. Aggregate output puede permitirse bajo paid si no sustituye/reconstruye underlying data, no permiso universal. No copiar terms íntegros.

Inferencia de diseño: Starter/trial **no satisfacen nuestra ruta persistente de snapshots, inputs/outputs/metrics, lineage y replay**. PAPER_V1_VIABLE_FREE=NO **para ese scope durable**; coste acceso0 no arregla la incompatibilidad. Disposición **REJECT Starter como proveedor del core/audit/backtest persistente** bajo términos observados, REFERENCE_ONLY para investigación documental. No REJECT permanente de Tiingo ni permiso de usar/free data en memoria y luego guardar resultados prohibidos.

Power/otros paid: **CONDITIONAL**, no seleccionados; retención tras cancelación y granularidad de traces/retornos son gates, no solución automática por pagar30/mes. §1.6 excluye expresamente **Starter y Power** de la excepción contractual de retención; ésta se limita a Startup/Enterprise/Institutional mediante acuerdo separado. Se preservan precios wave02 y LIVE alternativas. Necesidad de históricos no autoriza contratar ni enviar datos a LLM. Auditoría de transacciones broker propia y data de vendor tienen rights distintos; no destruir broker record legítimo por confundir procedencias ni guardar vendor prices encubiertos en trace.

## Matriz de alternativas antes de recomendar gasto

| Ruta | Cobertura/rights verificados en scope actual | Próximo gate / disposición |
|---|---|---|
| Tiingo Starter/trial | Restricción de retención incompatible, docs/pricing gratuitos no suficientes | REJECT durable role, no data call |
| Tiingo paid | Vigencia/deletion/derived restrictions; acuerdos requeridos según scope | REFERENCE_ONLY/WRAP condicional si terms/retención y economía aceptables; owner antes de gasto |
| Alpaca Basic | History desde2016, cobertura/feed facts wave01 | WRAP candidato; 2005–2015 no resuelto, licence/durable replay/AI use por verificar |
| Massive Basic | Free2años, no toda ventana confirmatoria o 2005 | WRAP candidato acotado; rights/retention/quality pendiente; no cambiar fechas silently |
| Alpha Vantage | Full daily/adjusted premium; compact100 insuficiente SMA200, edu exception no concedida | REFERENCE_ONLY/free partial; no asumir premium gratis |
| Yahoo/yfinance | [Repo original](https://github.com/ranaroussi/yfinance) Apache2 código, uso personal de datos y remite a Yahoo terms; [terms](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html) devuelve999 en herramienta | API/data rights/storage/automated use/PIT/history UNKNOWN, no código Apache=licencia de datos. ADAPT/WRAP candidato research, no aceptación/op output ni bypass |
| Stooq | [Download portal](https://stooq.com/db/h/) pide verificación JS | History/licence/retención/admisión UNKNOWN; no scraping/bypass ni REJECT por acceso bloqueado |
| Broker-native IBKR/otras fuentes/públicas o vendors especializados | No ficha completa validada para2005+ y requirements | Continuar comparación; **no conclusión de que no existe ninguna alternativa gratis** |

## Economía y condición para pagar

Tiingo free durable:NO, acceso0/opsUNKNOWN; paid30personal/50internal-commercial mensuales publicados y otros términos, escala/durable retention/lock-in/beneficio UNKNOWN. FREE_ALTERNATIVE=filas candidatas sin suficiencia certificada. PAID_INCREMENTAL_VALUE=historia/calidad/rights utilizables/continuidad si demostrado; ECONOMIC_JUSTIFICATION_REQUIRED=YES. LIVE costo/exit/deletion/contract por cotizar según scope; vendor pago no evita PIT/data-quality gates. Mensual un investigador/seisETF, volumen y usos no cerrados.

Antes de proponer excepción económica: comparar rutas Tier0/1 restantes y demostrar gap material + costo/beneficio/rights + aprobación owner. No presupuesto ni ninguna activación de API. Mantener contratos durables/versionados del proyecto; no reducir auditoría silenciosamente para declarar viable una fuente gratuita.

## Extensión de retención — wave06

[Extensión de retención](R-008_sources_evidence_wave03_2026-10-14.md) añade especificación y límites; Q057 aprobado en paquete, Q058 números propuestos. Sin fuente/modelo/Strategy admitidos ni performance. E4 sólo cálculo/meanpilot, no cobertura CAGR/ES/DD; M11 parcial/holdoutUNKNOWN. Versiones/declaraciones anteriores conservadas, no rehash histórico.
