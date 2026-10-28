# Persistencia, audit y observabilidad — contrato financiero RC2

2026-10-28. D-026/D-028/D-029: especificación transversal avanzada, no aceptación de store/target ni valores operacionales. Q-063 es propuesta de familias; no cambia B-RT1/A+/G1+G2. Sin implementación o servidor.

## Transacciones y autoridad por dominio

F: eventos financieros, qty/cash/claims, Risk verdict/autorización y command outbox atómicos con snapshot-version/epoch y unicidad de intent/command. Nunca afirmar exactamente una orden externa por commit SQL: dispatch incierto se reconcilia por IDs, sin reenviar ciegamente. C: manifest/due-job, attempt/lease/lifecycle, admisión/receipt únicos atómicos en su ledger. C/F no comparten writers/credenciales; analítica y jobs sin SQL operativo.

Para PostgreSQL propuesto: roles mínimos, transacciones y constraints verificadas, compare-and-commit de versión/generación y lock/aislamiento elegido con reintento acotado de conflictos **antes de dispatch**, no retry automático de envío broker. `fsync` y synchronous commit efectivos verificados, no confiar en defaults sólo por nombre. Persistir blob sellado antes de receipt; blob huérfano no admitido. Paths, schema o query del modelo no se ejecutan. Cliente y formatos deben preservar Decimal/enteros/UTC sin conversión binaria silenciosa.

Raw/licenciado/revisiones y audit con contenido protegido quedan locales bajo derechos y permisos de proveedor; Parquet/DuckDB no tienen autoridad sobre posición/orden. Cada snapshot tiene manifest, transformación/as-of, identidad/versiones/hash/canonicalización, rights policy y referencias permitidas. El hash no autentica un escritor ni reemplaza fuente; anchors fuera del namespace del job, con acceso y backups protegidos.

## Restore sin inventar continuidad

RPO/RTO por dominio, backup schedule/durabilidad/retención/espacio libre y acciones sobre incidentes se fijan antes de DoR. Requisito de proceso: un commit reconocido no se trata como durable si se configuró async o se desconoce la garantía. Power-loss y desastre no reciben RPO0 por ese requisito. Backup de DB no equivale a backup coherente de blobs/snapshots.

Nueva incarnation externa al backup cerca a workers viejos. Además comparar receipts/commands reconocidos con evidencia sellada/anchors: si falta historia o sólo queda un hash sin output verificable, marcar RECOVERY_GAP/UNKNOWN y bloquear nuevos attempts/admisión de trabajos afectados. No reconstruir un éxito desde hash solo ni volver a inferir para ocultar pérdida. Evidencia histórica completa permite reconstruir el receipt original, no nuevo ganador ni on-time retroactivo. Reconciliar estado financiero real antes de ownerresume material.

H9 y su complemento leen una copia restaurada ficticia y demuestran la pérdida conocida de receipt; no prueban seguridad del anchor, PostgreSQL, FSYNC, power loss o recuperación broker. Para corrupción, disco lleno, fallo de backup o pérdida de audit financiero: fail-closed según impacto y runbook; no borrar evidencia para liberar espacio sin política/derechos.

## Observabilidad reutilizable y local

Audit financiero durable reside en store/eventos, separado de telemetría best-effort. Logs estructurados locales con APIs estándar y correlación de event/job/attempt/snapshot/command; sin tokens, cuentas privadas, prompts internos o raw licenciado en export no permitido. Reutilizar [OpenTelemetry](https://opentelemetry.io/docs/languages/python/) para trazas/métricas cuando aporte valor; Python logs SDK sigue en Development en docs actuales, por tanto no dependencia del audit crítico. Collector/Prometheus/cloud no se vuelven obligatorios sin demanda/operación justificada; no servidor nuevo aquí.

| Señal | Denominador/semántica | Efecto permitido |
|---|---|---|
| Broker/protección/posición/cash incoherentes | Cobertura qty, estado/edad y mapping, no sólo socket conectado | G1+G2 y runbook; sin G3/resume automático |
| Audit/DB/dispatch durability desconocida | Eventos/commands pendientes y commits/versiones | Bloquear admisión/entradas afectadas; preservar protecciones vigentes |
| Job late/no-output/quota/auth | Jobs y attempts separados; deadline/receipt y causa | Estado factual y retry autorizado acotado; no HOLD o acción financiera alternativa |
| Data stale/gap/PIT/rights | Fuente/rol/instrumento/ventana y disponibilidad efectiva | Quarantine/no decisión con input requerido inválido |
| Backup/restore/drift | Última evidencia restaurable, hashes/versiones y nuevos epochs | No declarar ready/reanudar por reinicio o sólo backup exitoso |

Severidades operacionales no son prioridades P0–P4 de investigación. Alertas materiales requieren owner con runbook específico; no envío de email/Slack/cloud por este documento. SLO/latencia/cadencia/rate limits numéricos siguen ligados a B3/fuentes/Risk y target, no inventados desde throughput H9.

## Acceptance matrix y cierre de P1/P2

P1 de diseño: mappings/identidades/transacciones, rights/retención, métricas/denominadores, tabla de estados/errores y expected traces, criterios numéricos/actores/restore y revisión. P1 target: motor/pin/drivers/roles/config segura y bootstrap/smoke del mecanismo seleccionado. P2 integrado: órdenes y parciales/recovery, falla entre cada write/dispatch/ack, carga nominal/ráfaga/degradada, power/DB/disk según método seguro y restore de release/DB/blobs con broker más avanzado.

Mantener casos de timeout después de broker fill, duplicate activity, bust/revision tardía, split durante replace, pérdida de recepción, worker con epoch viejo, quota/late, postseal mutation y prohibición de datos a terceros. No todos son host-specific: fixtures/source review ahora; comportamiento real del motor/broker después. No cerrar D-029 por sumar PASS de laboratorios distintos.
