# Onboarding — Trading OS en un entorno nuevo

**Estado:** preparación, `implementation_locked=true`. Este procedimiento prepara y verifica capacidades agénticas; no instala un sistema de trading ni autoriza PAPER/LIVE. Paquetes y contratos RC0 son candidatos, no freeze D-020/D-024.

## Comenzar

Durante el Preparation Program, los artefactos nuevos están en `plan-architect`; `main` sigue siendo el baseline aprobado. En un directorio nuevo:

```powershell
git clone https://github.com/JorgeTonos28/trading-agent.git
cd trading-agent
git switch plan-architect
```

Acceso al repositorio, instalación de Codex y login son prerequisitos externos. Haz el login en la interfaz oficial con la cuenta que quieras evaluar. No copies autenticación de otro equipo ni envíes contraseñas/tokens al agente o al repo.

Abre **la raíz del clone** en Codex y pide:

> Lee AGENTS.md y ONBOARDING.md. Inicia Bootstrap Mode para PAPER_RUNTIME_ENVIRONMENT (Team), sin cambiar mi cuenta ni configuración global. Inspecciona las capacidades disponibles, identifica diferencias, guía las acciones manuales y produce el perfil/reporte de readiness. No marques un requisito como aprobado sin evidencia de este entorno.

La Skill candidata `$trading-os-bootstrap` aporta el procedimiento si aparece en el inventario. Si no aparece, el mismo procedimiento está aquí y en el [contrato](planning/07_environment_bootstrap_contract_RC0.md). Registrar ausencia y diferencia de versión; no instalar un plugin para compensarla automáticamente.

## Ruta de preparación

1. Confirmar Git root, rama/commit, etapa, reglas raíz/rol y versiones. Leer [manifiesto](shared/bootstrap_manifest.json) y [contrato de empaquetado](planning/07_agent_packaging_contract_RC0.md).
2. Inventariar capacidades **observadas** por superficie: Skills, plugins/apps, MCP, herramientas locales, permisos efectivos y límites conocidos. Separar instalado, habilitado, invocable y probado. Comparar contra el perfil esperado; no inspeccionar valores de secretos.
3. Producir plan de acciones clasificado. Automatizar lecturas, validaciones y smoke sintéticos cuando estén permitidos. Login, permisos materiales, cuentas/servicios y gasto se hacen mediante acciones del dueño. Mostrar un diff antes de cualquier configuración, conservar settings existentes; no ampliar permisos por un fallo.
4. Ejecutar [portabilidad EB-1–8](planning/07_environment_bootstrap_contract_RC0.md) y [Team TP-1–7](planning/research/R-006_team_runtime_acceptance_RC0.md) en la instancia Team PAPER. Reutilizar evidencia pertinente y repetir deltas de versión/configuración. La migración a Plus queda para [PRE-LIVE R-029](planning/research/R-029_pre_live_environment_migration_gate_RC0.md), sin bloquear PAPER.
5. Reportar evidencia, requisitos pendientes/fallidos, fallbacks y acciones exactas. Guardar perfil **sanitizado** conforme al [schema](shared/environment_profile.schema.json). Datos privados de configuración permanecen fuera de Git; reportes locales van a `.local/`, ignorado. Solo evidencia sanitizada y revisada entra en `planning/` con commit/push.

`READY_AGENT_ENVIRONMENT` exige todos los gates obligatorios del alcance evaluado. Hoy no hay selección final ni validación operacional PAPER sostenida: el resultado correcto será parcial, con gaps Team explícitos. Plus no es un requisito PAPER. La disponibilidad de roles de planificación no implica que los roles operacionales estén activados. Plan Guardian se activa después del freeze aprobado, no por abrir su carpeta.

## Roles reutilizables

Los paquetes documentales están en [agents/](agents/README.md). Para usar una especialidad, abrir su carpeta **dentro del clone completo**, conservando la raíz Git, y verificar reglas globales + locales. No copiar solo la carpeta. El mismo manifiesto/contratos permite un caller programático futuro; D-024 definirá su ejecución.

Si Codex no demuestra cargar la cadena requerida, volver a la raíz y leer explícitamente las reglas y contrato del rol. Registrar `FALLBACK_AVAILABLE` para uso manual de preparación; no tratarlo como equivalencia probada de la ruta autónoma ni como aislamiento financiero.

## Fuente de despliegue

ADR-010: preparación y probes usan commits pinados de plan-architect. main conserva el baseline aprobado. El despliegue futuro usa release/tag versionado aprobado con manifest y gates; no crear ni promover release automáticamente. CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato.

## Evidencia de planificación disponible

[Perfil PAPER Team RC0](planning/research/probes/r006-team-paper/environment-profile-PAPER-Team-RC0.json) describe el fresh clone c53a130 probado con SDK, no una release actual aprobada. Readiness PARTIAL; root/rol/Skill y target Team verificados, selección/seguridad/operación pendientes. No importar como aprobado un gate cuyo fingerprint haya cambiado.

## Contratos y checkpoint de seguridad posteriores ADR-011

ADR-011 A y disposiciones de diseño aprobados; final D-024 abierto. Revisar [seguridad](planning/08_agent_security_contract_RC0.md), [workflow/recovery](planning/08_job_workflow_recovery_contract_RC0.md) y [audit/versiones](planning/08_audit_versions_deployment_contract_RC0.md). Runtime de jobs será event/schedule-driven automático; uso manual de carpetas sirve preparación y no equivale a scheduler operacional. ADR-012 propone dominios Windows dedicados; aún no aprobados/configurados. Setup con identidad/ACL/red requiere pasos concretos y gobierno, jamás copia de broker/Codex secrets. Smoke default SDK0.160 en Team no cambia perfil observado PARTIAL ni demuestra entorno con aislamiento.
