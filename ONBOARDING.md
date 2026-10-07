# Onboarding — Trading OS en un entorno nuevo

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


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

**Vigencia ADR-012 — 2026-10-05:** el propietario aprueba S2 como dirección candidata de aislamiento PAPER por dominios Windows. S3 es fallback formal sujeto a nueva decisión si S2 falla; S1 solo probes sin secretos. Las propuestas históricas S2 vs S3 quedan resueltas únicamente en dirección. Security isolation y Shadow experimental blinding requieren acceptance separado; configuración administrativa, permisos efectivos y D-027/D-024 siguen abiertos. Ningún usuario/ACL/firewall/credencial se modifica por esta aprobación. Véase [ADR-012](planning/decisions/ADR-012-agent-process-isolation-proposed.md).

## S2 — próximo gate administrativo, no instalación automática

Leer [S2 RC1](planning/08_S2_isolation_spec_RC1.md) y [matriz SI/BL/RB](planning/research/R-013_S2_acceptance_matrix_RC1.md). Detectar identidad/token/config/store efectivo con lecturas permitidas, reportar diferencias, mantener NOT_TESTED/UNKNOWN mandatory. S2 dirección aprobada; ninguna cuenta/ACL/firewall modificada. Próxima acción [ADM-01](planning/research/R-013_S2_administrative_gate_ADM01.md) es USER_ACTION_REQUIRED: aprobación específica de laboratorio sintético. Policy merge/source, IPC/egress y Team login propios requieren gates posteriores. No usar sandbox-comandos/AGENTS como prueba de aislamiento del caller ni READY financiero.

## Checkpoint vigente: variante antes de administración — 2026-10-06

El propietario **no autoriza S2-ADM-01**. La sección anterior de próximo gate es histórica y queda sustituida: no crear sus tres usuarios ni cambiar ACL/firewall/perfiles. Leer [comparativa](planning/research/R-013_S2_variants_comparison_2026-10-06.md), [contrato S2-B RC2](planning/08_S2_agent_domain_contract_RC2.md) y [acceptance RC2](planning/research/R-013_S2_variant_acceptance_RC2.md). Recomendación B pendiente de decisión Q-051, no setup; roles/paquetes no fijan cuentas/sesiones. Repo incluye evidencia AccessCheck semántica, no entorno aislado verificado. Automatizar solo checks permitidos; readiness PARTIAL, financial authority NONE, implementación bloqueada. Nueva administración se propone concretamente después de elegir variante.

## S2-B dirección aprobada — confirmación posterior 2026-10-06

Q-051 está DECIDED en dirección, no pedirla nuevamente. Preparar laboratorio mínimo/reversión con [ADR-012](planning/decisions/ADR-012-agent-process-isolation-proposed.md). S2-B principal, A/S3 condicionadas; ninguna cuenta/ACL/firewall/credencial/config global autorizada. Setup requiere propuesta concreta antes de ejecutar; S2-ADM-01 no se reactiva. Readiness efectiva sigue pendiente.

## Gate mínimo S2-B preparado — 2026-10-06

[S2B-ADM-01](planning/research/R-013_S2B_lab_ADM01.md) corresponde a una cuenta **temporal de laboratorio**, no un usuario por rol ni Runner operacional instalado. AUTHORIZED_OWNER_ADMIN_ONLY desde autorización posterior: USER_ACTION_REQUIRED para cuenta/ACL/login temporales del propietario. Bootstrap/agente no se elevan, no crean cuentas ni aplican policy; permisos operativos siguen sin aprobación. Memoria/PLAN_ONLY/readonly no prueban FS/EB/TP4. Binder local/secretos fuera de Git; rollback SID/path solo recursos nuevos. Team PAPER sin Plus, native auth/egress/full process/recovery y aceptación siguen pendientes. Paquetes no cambian autoridad ni D-024.

## Entrada vigente — ADR-013

Durante Preparation en Team/INFOTEP: leer AGENTS, manifest/perfil esperado activo y contratos; inventariar sin secretos; registrar diseño y checks permitidos. No configurar dominio operacional ni solicitar Plus/admin aquí. En transición futura autorizada: fresh clone en PC personal/Plus → gate R-030 → configuración concreta aprobada → SI/BL/RB/VP + smokes → readiness report. R-030 se requiere antes de implementación; sistema construido/carga/PAPER se validan después. LIVE no seleccionado. Históricos paper_team_profile y TP sirven de evidencia fechada, no perfil operacional vigente. Helper histórico S2B Setup/Rollback bloqueado hasta gate/rebind target.
