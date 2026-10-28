# H9 — demanda D1, transacciones y restauración de ledger ficticio

Protocolo previo 2026-10-28. SQLite stdlib como instrumento de laboratorio, **no selección del store**, no Financial Core, dinero o ejecución. Reutiliza semánticas H7/H8; no repite discovery agéntico. No servidor, puerto, task, daemon, credencial o cambio global.

Workload fijo:1200 jobs ficticios (300 slots×4 roles) y2400 propuestas de inserción en cuatro threads, un archivo local. Verificar identidad/únicos y atomicidad job/outbox; compare-and-commit de attempt/generación; un receipt por job y rechazo stale/late; rollback; backup por API y restauración con nueva incarnation externa; pérdida de receipt posterior a backup visible como RECOVERY_GAP. No inferir exactly-once de inferencia o efectos, ni auth/ACL por un ID de fixture.

Se usa journal DELETE y synchronous FULL explícitos. SQLite local3.50.4 cae en el rango del WAL-reset bug publicado; no usar WAL para esta prueba ni aceptar ese pin para un futuro uso WAL. Esta prueba no reproduce/valida el fix. DBs quedan en `.local/h9-demand-ledger` para inspección; ninguna eliminación de residuos H7.

Medir elapsed de los2400 intentos únicamente como observación local, sin PASS de capacidad: no hay SLO aprobado ni hardware target. No power-loss/FSYNC real, PostgreSQL, filesystem denial, broker, LLM, quota, disk-full o carga sostenida aceptados.

## Resultado H9 y alcance de restore

Result01:13/13 expectativas;1200 jobs/2400 propuestas,20.14s de inserción observados, sin SLO. El chequeo de epoch se aplicó al ledger original con epoch externo nuevo; el archivo restaurado se inspeccionó por separado. No se presenta ese chequeo como recepción integrada sobre la copia restaurada. La copia pierde un receipt confirmado después del backup: nueva incarnation por sí sola no reconstruye historia ni autoriza repetir el job.

## Restore complementario, protocolo previo

Script separado lee efectivamente el archivo restaurado y el anchor de fixture externo: rechazar envelope de epoch viejo; si existe evidencia de ack posterior pero falta output sellado, bloquear nuevos attempts/receipts por RECOVERY_GAP. Hash aislado no reconstruye evidencia. Con evidencia histórica completa verificada, sólo reconstruir el receipt original; sin anchors, historia UNKNOWN. Son controles de contrato con fixtures, no autenticación de anchors, storage productivo ni restore financiero.

Cuatro producers prueban writers concurrentes, no una colisión forzada sobre la misma key. CAS/admisión son controles secuenciales; la concurrencia completa de recepción y PostgreSQL siguen pendientes. No declarar race acceptance desde este conteo.
