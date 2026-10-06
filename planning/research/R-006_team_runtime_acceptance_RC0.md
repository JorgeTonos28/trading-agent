# R-006 — Team Runtime Acceptance & Architecture Readiness RC0

2026-10-05. PAPER_RUNTIME_ENVIRONMENT = **Team actual**, ADR-010. ADR-011 A y disposiciones RC2 aprobadas para diseño; D-020 DECIDED en ese alcance. D-024 y controles finales siguen abiertos. No dependencias de Plus para PAPER.

## Tres niveles de evidencia

1. **Capability discovery / decisión arquitectónica P0/P1:** cobertura, licencia/coste, probes relevantes de acceso/Skills/output/tools/autoridad, matriz comparativa, bootstrap y recovery conceptual probado en harness. Permite presentar paquete material para gobierno; no significa operación validada.
2. **Definition of Ready P1:** arquitectura/contratos/tecnologías seleccionados y especificados, bootstrap Team reproducible, permisos/seguridad aprobados, protocolos de tests y operación con responsables. No exigir implementación financiera de producción para cerrar un plan: specs/probes de preparación y gates explícitos son evidencia adecuada donde proceda.
3. **Acceptance operacional P2 antes de PAPER autónomo:** implementación ya construida contra plan congelado, integración durable/financiera real, workload de Strategy V1, observación de cuota/ventanas/continuidad, informes/curriculum y fallos. Los ensayos de varias sesiones/días no se simulan ni se dan por aprobados por un burst. Política numérica/gates financieros requieren su gobierno.

No cambiar el significado de los gates históricos silenciosamente: ADR-010 elimina dependencia de Plus, **no exime criterios de acceso, permisos, recovery, cuota o suficiencia**. Esta distribución por etapa es una propuesta de especificación que requiere validación en el cierre D-024; no una dispensa ya aprobada. Antes de freeze P1 se debe justificar con evidencia la viabilidad de la ruta y carga representativas seleccionadas; un protocolo pendiente o ocho fixtures no aseguran ese cierre. La operación financiera completa y su continuidad integrada se verifican P2, después de construirla. Si evidence detecta un gap material que invalida la arquitectura, vuelve a P0/P1.

| Gate Team | Evidencia para arquitectura / pendiente inmediato | Gate operacional posterior |
|---|---|---|
| TP-1 identidad/acceso | Account/read sanitizado Team, cliente/modelo/ruta nativa. Waves 03–06/R-028 disponibles | Revalidar en instancia de despliegue seleccionada, no todos los Team equivalentes |
| TP-2 discovery/activación | Cuatro procedimientos, Bootstrap Mode y paquetes; inventario vs cuerpo activado, versiones/pins | Verificar assets finales de release y tooling necesarios |
| TP-3 outputs/tools | Schemas confiables, PIT/lineage, cuatro roles; SDK low-level Skill/tool wave07 probado, raw reservado por gap | Fuentes/engine/report contracts completos en integración real |
| TP-4 autoridad/permiso | Sin broker/secretos/órdenes; allowlist y admission fuera del modelo; revisión de gaps | Aislamiento técnico D-027/034, red team e integración, no garantía por prompt |
| TP-5 contexto/recovery | Rehidratar job desde repo/snapshot después de reiniciar cliente, no depender de chat; intento/late/fail auditables | Durable workflow/storage/auth lifecycle D-025/026; revocación/login del dueño no se altera automáticamente |
| TP-6 carga/viabilidad | Benchmark Team **acotado** para decidir dirección; antes de cierre final P1, workload representativo/criterios seleccionados y evidencia de suficiencia exigible, actualmente PARTIAL | WL-R integrado y varias sesiones/días según Strategy V1; reserva/cupo/reset y uso compartido, no inferir sostenibilidad desde tokens |
| TP-7 operación/economía | Ruta nativa local documentada, sin API billing, licencias/permisos; integración/versiones y límites explícitos | SLO/continuidad/alertas/backups/operación legítima de configuración final |

## Bootstrap y source policy

EB1–8 se evalúan contra Team para PAPER. EB7 ahora depende de TP1–7, no GP Plus. El fresh clone debe verificar root/rol/Skill/refs y reportar diferencias, incluyendo herramientas/settings externos y hashes Git frente a bytes locales. `plan-architect` permite probes de candidatos; despliegue futuro utiliza release/tag aprobado desde baseline promovido con gobierno. No merge/tag de despliegue ahora.

## Paquete autónomo restante y criterio de parada

- Registrar supersession/perfiles/contratos y preservar evidence histórica.
- Probar gaps oficiales SDK/Skill/tool y recovery con fixtures permitidos; reuse antes de WRAP/BUILD.
- Construir payload representativo y ejecutar carga acotada suficiente para revelar un cuello de botella concreto; conservar errores y cuotas como observaciones.
- Revisar consistencia/amenazas y preparar propuesta comparativa de arquitectura PAPER con gap por gate/etapa, sin fingir revisión independiente.
- Commit/push hitos. Detenerse ante decisión **material** de arquitectura/autoridad/permisos que requiera dueño; no pedir acceso Plus.

No cierre automático de D-020/D-024, ni implementación ni selección de Strategy/broker/datos/umbrales. Un problema en componente opcional no exige instalarlo ni pausa discovery.

## Hito histórico antes de aprobación ADR-011 — wave07

8/8 jobs y SDK/bootstrap 14/14 verifican factibilidad acotada y fresh clone; 16 checks consolidan evidencia y recepción offline. TP3/5/6 focales cubiertos en ese scope; TP4 seguridad real, TP5 durable/auth y TP6 carga sostenida siguen pendientes por etapa. RC2/ADR-011 listos para decisión material; perfil PARTIAL, SELECTED=NO.

## Paquete P1 posterior ADR-011

Contratos 08 seguridad/workflow/audit: permisos materiales D-027 requieren gobierno y probe de viabilidad empírico bajo frontera elegida antes de freeze, no solo protocolo P2 pendiente. SDK/CLI publicados emparejados H4 aporta regresión focal, no capacidad sostenida. H1/H2 SQLite prueba semántica/desconexión/race toy; H3 simulado no aprueba TP6. D-025/026 exigen evidencia de motor escogido; RPO/restore y autenticación integrada P2. Review independiente documentada en R-010_014 dossier, no auditoría humana/aprobación final.

## TP-4 y bootstrap — S2 posterior ADR-012

S2 dirección aprobada; controles finales no. [Contrato concreto](../08_S2_isolation_spec_RC1.md), [SI/BL/RB](R-013_S2_acceptance_matrix_RC1.md), [hallazgos](R-013_S2_findings_2026-10-05.md). ADM-01 requiere owner para tres cuentas estándar/ACL canary; no Plus, no papel financiero implementado. TP-4 sigue PARTIAL/NOT_TESTED en enforcement; RB/TP-6 exige permisos/domain launch reales, no importar capacidad S1. Gate red considera AllowLocalFirewallRulesFalse; no decisión S3 por falta de aprobación. R-006 madura contratos de diseño, no fuerza D-024 cerrado.

## Gate S2 revisado — 2026-10-06

[Comparativa A/B/S3](R-013_S2_variants_comparison_2026-10-06.md) y [RC2](../08_S2_agent_domain_contract_RC2.md) proponen **Agent Runner común con contextos efectivos por job**, sin cuenta obligatoria por rol. No cambiar disposiciones D-020/ADR-011 ni congelar D-024. **ADM-01 DEFERRED/NOT_AUTHORIZED**, no próximo gate: Q-051 dirección candidata revisada antes de laboratorio nuevo. AC10/10 es semántica, no TP4/EB/SI/BL/RB efectivo ni TP6 capacidad bajo permisos. Plus PRE-LIVE, PAPER Team, futuros native auth/egress/cache/recovery/workload pendientes.
