# M-11 — auditoría parcial de exposición, scope repositorio

2026-10-14. Snapshot de inventario Git **e9b36dc**; no apertura de datos reservados para intentar verificar su integridad. [Exposure ledger](exposure_ledger.md) sigue siendo inventario parcial, no certificado de muestra intacta.

## Evidencia observable

- `git ls-files` no encontró archivos CSV, Parquet, Feather, notebooks, XLSX o JSONL tracked en ese snapshot. Esto sólo describe formatos/rutas, no prueba ausencia de datos en Markdown/JSON/imágenes ni de exposición fuera de Git.
- Historia de decisiones/pruebas financieras desde ADR015/016/017 hasta ADR018 conserva aprobación conceptual, hipótesis no ejecutadas y probes sintéticos. [Registry](experiment_registry.json) declara8 hipótesis y0trials/attempts de estrategias; history_complete=false, no extrapolar a búsquedas externas desconocidas.
- E1/F2 usan XML/fixtures propios; E2/E3/E4 y riesgo usan datos ficticios/componentes. E4 aún es wave posterior a este snapshot y tendrá source/hash propio. No presentar sus tasas como returns de candidatos.
- Dossier video y docs primarios de emisores/API/metodología han mostrado claims/ejemplos/snippets externos. X01–X11 mantienen exposiciones; no borrar por considerarlos incidentales.

## Lo que no cierra esta auditoría

No se examinaron stores privados, otros dispositivos/cuentas/chats fuera repositorio, logs del navegador o archivos ignorados para certificar no-exposure. Ninguna inspección de secretos ni nueva solicitud Plus/admin. Declaración del propietario de que MATR nunca tuvo resultados se preserva, no equivale a un ledger externo exhaustivo. Tampoco se conoce alcance completo de cualquier búsqueda del creador o proveedor.

Antes de F1: reconstruir persona/source/fecha/intervalo/campos vistos/uso en hipótesis o parámetros; distinguir video/public benchmark/contexto de propioresultado/selección. Resolver UNKNOWN sólo para scope defendible con evidencia; si no se acredita independencia suficiente, alternativa prospectiva con freeze/criterios y gobierno. No abrir reserva para decidir cuánto está contaminada ni usarla para estimar la potencia que queremos conseguir.

**Resultado:** M-11 PARTIAL_REPOSITORY_PROCESS_AUDIT, reserva **PROPOSED_RESERVE / INTEGRITY_UNKNOWN**. No FAIL/CONTAMINATED ni INTEGRITY_PASS por ausencia de ficheros. Q058 de utilidad numérica puede decidirse antes de resultados sin cerrar esa auditoría; confirmación sigue bloqueada.
