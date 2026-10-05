# Contratos y assets compartidos — RC0

- [bootstrap_manifest.json](bootstrap_manifest.json): requisitos, gates, roles y rutas relativas; no credenciales ni settings de una máquina.
- [environment_profile.schema.json](environment_profile.schema.json): perfil observado/reporte sanitizado con evidencia y estados.
- [target_plus_profile.json](target_plus_profile.json): expectativa de Plus individual; sus valores no son observaciones.
- Contratos de evidencia, shadow y pedagogía se mantienen canónicamente en `planning/06_*_contract_RC0.md`; el manifiesto los referencia, no copia.
- Skill compartida de bootstrap está en `../.agents/skills/trading-os-bootstrap/`, ruta nativa investigada. `shared/skills` arbitrario no se presume autodetectado. Skills específicas futuras pueden vivir en `agents/<role>/.agents/skills/`; evaluar antes de activarlas/seleccionarlas.

Los probes previos bajo `planning/research/probes/` son **fixtures/prototipos sintéticos**, no Skills operacionales. Licencia/atribución Anthropic se conserva en sus dossiers y prototipos; el manifiesto no concede derechos sobre datos/conectores. No empaquetar plugins propietarios del entorno Team.

El futuro empaquetado en plugin puede generar/copiar assets desde este catálogo con integridad/licencia verificadas. No depender de links simbólicos Windows ni de rutas `C:/Users/...`; empaquetado portable y activación nativa son requisitos diferentes.
