# PRICE–MATR — contrato de reglas y bindings RC2

2026-10-23. Completa ambigüedades técnicas de las hipótesis EQ3, **sin cambiar sus señales/parámetros ni seleccionar Strategy V1**. JSON RC1 y las12declaraciones se conservan byte a byte;0trials. Esta nota se incorporará al futuro manifiesto antes de F0; un cambio semántico posterior exige nueva variante, no rehash silencioso.

## Reglas deterministas fijadas para especificación

| Tema | Regla de realización |
|---|---|
| Precio/eligibilidad | Precio, SMA200 y ROC126 de la misma serie split-only as-of. SMA incluye cierre t; ROC=C_t/C_(t−126)−1; breakout PRICE usa exactamente126cierres previos, excluye t. Igualdad no supera filtro estricto |
| ATR | TR_t=max(H−L,abs(H−C_prev),abs(L−C_prev)); semilla media de20TR válidos consecutivos, Wilder después. Requiere cierre previo; no fabricar TR inicial de serie truncada. SMA200 domina warm-up MATR; elegibilidad PRICE también exige ATR válido |
| Identidad/ranking | SecurityID estable as-of, ROC descendente y ID ascendente; no ticker actual para resolver identidad histórica. Ranking de PRICE sólo nuevas entradas; MATR evalúa top3 del universo elegible completo en la última sesión semanal admitida |
| MATR salidas | Pérdida de elegibilidad diaria; pérdida de top3 en rebalance semanal; stop fijo3ATR del snapshot de entrada, con actualizaciones de parcial y corporate action ya especificadas. Supervivientes no se vuelven a pesar ni se amplían |
| Reemplazo semanal | Salir de los que pierden top3; proponer nuevas entradas por prioridad sólo con slots/cash elegibles y contexto reconciliado. Un fill parcial/remainder cuenta un security, no dos; ventas esperadas no financian compras automáticamente |
| Señal vigente | Nueva entrada no enviada caduca al cierre siguiente definido. Si ventas/settlement impiden entrar antes de expiry, registrar NO_TRADE_CASH_OR_SETTLEMENT; no posponer a día favorable ni renovar señal sin nuevo evento válido. Esto puede reducir exposición, debe simularse |
| Target | NAV financiero conocido en señal/3 por nueva posición; floor a lote entero usando p_auth. Sin top-up, redistribución de ranuras vacías o aumento por presupuesto Risk libre. Risk revalida contra snapshot actual y puede restringir/rechazar; no modifica el target para aprovechar un open futuro |
| PRICE ratchet | Comparar umbrales geométricos con aritmética decimal/racional y entero k; no depender de floor(log()) binario cerca de un umbral. Anchor=p0(1+a)(1+h)^k, a=.10/h=.05/b=.05 de research; desired=max(previous,anchor(1−b)) |
| Redondeo protector | Deseado y precio broker distintos; sell-stop se proyecta al grid declarado y Risk incluye pérdida de ajuste/tick. No bajar protección por redondeo/cambio de fills; rebase corporativo compara unidades equivalentes. Si precio válido no puede instalarse, no declarar cobertura |
| HWM/partial | Antes del seal, sólo contrato inicial de protección; p0 ex-fees de fills reconciliados. Después H usa barras completas con inicio≥seal. No high de la barra del fill ni HWM de antes de tener lote |
| Precedencia | Incertidumbre material→G1+G2/reconciliación, protección existente conservada; sin reanudación automática ni G3. Healthy→salida/protección y reemplazo seguro, después entradas |

Estas son especificaciones de research, no autorización para enviar/cancelar órdenes. Limitar una orden por pérdida del top3 no exige permiso humano trade por trade dentro de un Champion aprobado; aquí aún no hay Champion.

## Binding financiero que no se inventa

Pendientes explícitos antes de CONFIG_ADMITTED_FOR_RESEARCH: fuente/calendario/PIT/cash; order policy/venue/TIF/horas; significado y conservadurismo de p_auth; stop condicional y protección efectiva de parciales; costes/settlement/latencia; perfil numérico de riesgo y modelo de gaps/liquidez; paridad del motor. Un p_auth finito no convierte market en limit. Capped limit y market tienen probabilidad/tiempo de fill distintos: no cambiar la política después de resultados ni imponer fills next-open idénticos.

La regla inicial p0−3ATR depende del fill: un stop child fijado antes del fill no puede llamarse automáticamente esa misma regla. Declarar si el broker puede proteger proporcionalmente con ese precio, si requiere actualización posterior y qué ocurre en el intervalo. No sustituirla por signal-close−3ATR sin crear variante/gobierno aplicable. El diseño de protección no está resuelto por la existencia de bracket/OTO.

Los números de riesgo0.5%/25% del borrador no están aprobados y no se restauran aquí. D031 agrupa presupuestos/umbrales como decisión futura fundamentada; falta de datos puede impedir calibración, pero sus requisitos/configuración no desaparecen como P2 genérico.

## F0, selección y Champion: eliminar el ciclo

1. RULES_SPECIFIED: esta capa de hipótesis.
2. CONFIG_ADMITTED_FOR_RESEARCH: reglas, datos/modelos, perfil de riesgo experimental, costes/escala, método y exposición de muestra aceptados para scope explícito.
3. F0 preregistra **cada candidato de investigación**, selector/familia y protocolos antes de resultados; no exige un Champion ya aprobado.
4. CONFIG_SELECTED/F1: escoger sólo según protocolo y congelar antes de confirmación; cambio posterior necesita evidencia nueva.
5. STRATEGY_DESIGN_APPROVED: selección/diseño de la candidata y especificación congelada aprobados por el propietario para el scope de implementación; requisito de DoR, distinto de promoción operacional.
6. READY_FOR_IMPLEMENTATION requiere DoR y aceptación target aplicable. Sólo después: implementación → validación operacional → promoción/autorización de Champion PAPER según sus gates. CHAMPION_OPERATIONALLY_APPROVED nunca es un prerrequisito circular para implementar. NO_STRATEGY_QUALIFIED sigue posible.

La lista separa estados y **no es una cadena cronológica universal**: la evidencia de investigación, la decisión de diseño y la validación operacional tienen fases distintas. F0 no exige Champion operativo; tampoco autoriza históricos prematuros ni sustituye los gates de datos/método/integridad. Ninguno de estos estados se declara alcanzado aquí.

No usar F0 para llamar a datos desconocidos admitidos ni saltar validación de métodos. El master-plan puede especificar una candidata a implementar y su proceso de promoción; aprobación de diseño y promoción operativa se registran separadas, sin rebajar DoR. Form4 continúa candidato de investigación, no parte implícita de PRICE/MATR ni requerimiento para admisión de la cohorte ETF.
