# R-008 — respuestas comerciales, planes y admisión RC1

2026-10-28. Evidencia aportada por el propietario, disponible para investigación desde hoy; no se conocen las fechas reales de recepción ni se inspeccionó el correo original. [Registro fiel del resumen](vendor_inquiries/owner_response_evidence_2026-10-28.json), [estados](vendor_inquiries/status.json). No envío de consultas, cuenta o gasto por el agente.

## Qué confirma cada fuente

| Evidencia | Confirmación en su alcance | Lo que no demuestra |
|---|---|---|
| Twelve Data, resumen del propietario | Solicita empresa/web, mercados/delay y usos. Proyecto personal sin empresa/web pública. Aclaración preparada por el propietario, envío pendiente | No precio, licencia ni acceso concedido. VENDOR_INFORMATION_REQUESTED |
| EODHD ventas, resumen del propietario | Recomienda All-in-One 99.99/mes; seis ETF raw/adjusted/actions sujetos a historia. Reporta uso personal automatizado, almacenamiento privado y retención tras cancelar; sin Commercial Non-Display adicional para usos descritos | No contrato específico revisado, derechos trasladados a planes baratos, cobertura/completitud/calidad por fila ni dataset admitido |
| EODHD respuesta técnica reportada | Pay-dates/completitud variables; no vintages completos ni timestamps originales/archivo íntegro de revisiones; precios pueden ser indicativos | No replay PIT original, precios ejecutables ni permiso de transmitir raw a IA cloud |
| [Tarifario oficial](https://eodhd.com/pricing), consultado 2026-10-28 | Mensual EOD19.99, EOD+Intraday29.99, All-in-One99.99. Tabla incluye dividends/splits en EOD; intraday no incluido allí | No elegibilidad particular ni suficiencia de un único plan. No compra autorizada |

## Compatibilidad contractual: revisión documental, no dictamen legal

[Términos públicos](https://eodhd.com/financial-apis/terms-conditions), secciones PERSONAL AND COMMERCIAL USE, NO WARRANTIES, TERMINATION y AMENDMENTS: uso privado personal admite almacenar/manipular/analizar; prohíbe redistribuir o dar acceso, incluida información reempaquetada. No se encontró una cláusula expresa de conservación después de cancelar en esa página. La aclaración comercial reportada es evidencia adicional compatible en principio con uso privado, pero falta vincular su alcance al producto económico y a los términos vigentes al contratar. No se declara un permiso contractual definitivo ni se inventa una contradicción de borrado.

El disclaimer de precios indicativos exige QA por rol; no convierte al proveedor en fuente de fills ejecutables. La página pública no contiene autorización específica de envío de datasets a OpenAI/Team/Codex/otros clouds. **EXTERNAL_AI_RAW_TRANSFER=DENY_UNCONFIRMED**. La existencia de MCP/Skills/ChatGPT Assistant del proveedor no concede ese derecho.

Preparar aceptación exige conservar localmente la versión aplicable de términos y evidencia comercial/alcance, sin datos personales en Git. No se necesita acceder a buzón o credenciales durante esta investigación. Respuesta genérica o favorable no equivale a DATASET_ADMITTED.

## Selección por rol y coste

Prioridad: evaluar EOD Historical19.99 para señales/indicadores y acciones antes de All-in-One. Datos de ejecución/parciales/gaps/stops, eventos Form4, feed paper Alpaca y referencia monetaria son roles separados. Intraday29.99 sólo si la granularidad/cobertura/semántica requerida se demuestra; All-in-One99.99 necesita un valor incremental específico no cubierto por alternativas. No sumar planes redundantes ni imponer uno para cubrir todos los roles.

El plan económico continúa PLAN_SCOPE_CLARIFICATION_PENDING; todos los datasets TECHNICAL_ADMISSION_PENDING / NOT_ADMITTED. Falta confirmar retención/licencia por producto, seis ETF e inception/warmup, raw/unidades/actions/pay-date, PIT/revisiones, granularidad de ejecución y QA independiente. Una declaraciónDate sin hora/vintage no prueba disponibilidad original; un lag arbitrario no repara revisiones futuras.

Las cinco escalas y los tres precios públicos se calculan en [escenarios wave12](source_cost_scenarios_wave12.json). Son costes de componente hipotéticos, no CAGR ni coste total. Los planes anuales publicados se registran aparte, sin asumir renovación o prepago. El caso de una sola compra mensual con retención es condicional y no resuelve actualizaciones/feed continuo.

## Corrección tras revisión independiente

DENY externo también cubre información licenciada derivada, reempaquetada o reconstruible, incluidos snapshots, cálculos y resúmenes. Cada campo/uso/destino requiere permiso aplicable; transformar o agregar no concede autorización. Los outputs propios sin contenido licenciado se evalúan por su linaje, no por su extensión o etiqueta. La afirmación de almacenamiento local permanece REPORTED_ALLOWED / PRODUCT_CONTRACT_SCOPE_PENDING, no derecho técnico admitido.
