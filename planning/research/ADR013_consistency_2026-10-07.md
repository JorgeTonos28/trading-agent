# Consistencia de entornos y gates — ADR-013

2026-10-07. Owner correction registrada sin OS setup.

- D-043 DECIDED; ADR-010/D-038 supersession parcial y R-029/D-039 premisa histórica. Deployment Source Policy y decisiones financieras permanecen.
- AGENTS/instrucciones bootstrap actuales corregidos; documentos anteriores tienen nota de aplicabilidad ADR-013, cuerpos/resultados capturados preservados. Matriz histórica no concede disponibilidad target.
- Manifest/expected profile separan AI-plan/host y fases. Schema v0.3 y v0.2 histórica válidos; perfil Team capturado pasa su rama v0.2, sin migrar su scope.
- YAML válido, invariantes lock/DoR y paths manifest verificados; links locales de cambios sin roturas; Skill validada con skill-creator; `git diff --check` limpio.
- Primer intento de validación con Python global carecía de PyYAML; se usaron dependencias de investigación ya existentes en TEMP. No instalación/config global.
- Dos invocaciones de helper Setup/Rollback rechazadas **antes de cualquier acción filesystem/identity/admin**, exit 1 esperado; [resultado](probes/r013-s2b-lab-execution/defer-guard-2026-10-07.json). Es check del guard, no lab administrativo ni FS real.
- LF/SI/BL/RB/VP siguen NOT_TESTED. Estado del lab diferido, no FAIL/REJECTED; snapshot ejecución anterior y helper revisado en history. No nueva medición de residuos OS: observación 2026-10-06 preservada y explícitamente histórica. No recursos de laboratorio creados por el agente.

Pendiente de este hito: auditoría independiente de aplicabilidad/gates y madurez de diseño R-006/R-010/R-013; se incorpora al siguiente checkpoint. No afirmar target/runtime aceptado o arquitectura final congelada.
