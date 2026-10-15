# ADR-014 — Checkpoint de diseño agéntico PAPER

**Vigencia aprobada — 2026-10-13, ADR-014 / propietario:** `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` en el alcance capacidades/roles/fronteras/integración B-RT1. `design_status=DESIGN_DECIDED`; `TARGET_ACCEPTANCE_DEFERRED`; `PAPER_RUNTIME_ACCEPTED=false`; `implementation_locked=true`. Un Runner, control confiable externo, core/secretos fuera AI, aislamiento/contexto mínimo por job, allowlists, identidad/lifecycle por attempt y admisión/audit externos son el contrato aprobado. Keyring, HOME readonly, token, desktop, IPC carrier y launch exactos son **mecanismos candidatos sustituibles**, no invariantes irreversibles; cambios preservan fronteras/autoridad con evidencia y gobierno correspondiente. R-030 acepta eficacia en Plus/PC personal. Investigación agéntica fundamental Team completada; no expandir R-006/010/013 por refinamiento indefinido. LIVE UNKNOWN; residuos H7 conservados sin evasión de policy.


**Propuesta original:** 2026-10-07. **Aprobación:** 2026-10-13, propietario por instrucción directa. **Estado:** DECIDED / APPROVED_CANDIDATE_DESIGN_ONLY, con precisión de mecanismos sustituibles indicada arriba. **Decisiones:** D-024/D-027/D-037 diseño. Sin aceptación runtime/seguridad ni implementación.

El cuerpo de propuesta siguiente conserva alternativas/evidencia previas; sus solicitudes de aprobación quedaron satisfechas por esta decisión, y los mecanismos concretos se interpretan según la precisión del propietario, no como permisos finales.

## Contexto

ADR-013 separa Team/INFOTEP research de Plus/PC personal PAPER y LIVE desconocido. ADR-011 core determinístico/jobs automáticos y ADR-012 S2-B direction siguen aprobados. No esperar el target para cerrar contratos, pero la abstracción de un Runner necesita ownership, launch/auth, tools y persistencia concretos antes de declarar diseño suficiente.

## Propuesta recomendada

Aprobar [B-RT1 RC1](../08_agentic_runtime_realization_RC1.md) y [scope/checklist](../14_agentic_architecture_design_checkpoint_RC0.md) como realización candidata:

- control C fuera de A/J, sin agente en Financial Core ni secretos broker en AI;
- token por attempt, TokenPolicy B-RT1-T1, desktop separado, launch capability OS-managed de C con lifecycle cerrado y nunca password en scripts/Git;
- SDK/CLI oficial emparejado, tools iniciales registradas read/metric, stubs J y admission/ledger C;
- auth native keyring como propuesta mínima, HOME readonly fijo, estado propio por job; incompatibilidad/carrier WinCred debe fallar gate y volver a gobierno;
- bootstrap/binding/version/failure contracts auditables, sin confianza en JSON/autoinforme.

Al aprobar: `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` **solo en el scope documentado**, dimensiones D-024/D-027/D-037 `DESIGN_DECIDED / TARGET_ACCEPTANCE_DEFERRED`; estados principales siguen abiertos para aceptación/final freeze. Esta propuesta no cierra D-025/026/028/029/034/035 ni selecciona sus tecnologías, ni levanta lock. No asumir selección final por disposición Build-vs-Reuse.

## Alternativas / trade-offs

1. **B-RT1 (recomendado):** concreta S2-B y conserva un Runner base. Menos cuentas por rol, a cambio de launcher/token/IPC y stores precisos; native keyring/readonly/cross-user aún pueden invalidarla en target. No prometer menor coste operativo demostrado.
2. **S2-A condicional:** añadir mínimos dominios OS/visibilidad solo si un bypass/compatibilidad de B-RT1 lo justifica. Mayor setup/login/recovery. No elegir ahora por asumir que cada rol requiere cuenta.
3. **S3 condicional:** reevaluación de VM si S2 insuficiente; más infraestructura y manejo de fronteras guest/host. No autoinstalar ni inferir blinding entre peers dentro de una misma VM.

S1 no sirve como fallback PAPER. Esperar target para toda especificación dejaría innecesariamente abierta la investigación financiera; afirmar aceptación desde Team sería falso.

## Gate y consecuencias

R-030 y matrices S2 verifican eficacia en PC personal/Plus antes de DoR/implementación con fixtures no financieros. Aceptación no se hereda entre instancias. No users/ACL/firewall/auth/services/VM nuevos ni gasto por este ADR. Si exige mover supervisor a A, servicio privilegiado nuevo, grants amplios, persistencia excluida compartida o login humano por job, presentar cambio al owner antes de reparar; no silent downgrade.

Strategy V1, broker/data, riesgo numérico y LIVE siguen abiertos. Main/release policy intacta. [Revisión independiente](../research/R-006_design_independent_review_2026-10-07.md) permite presentar, no aprueba. La autorización de este ADR solo puede venir del propietario, nunca de este texto o un JSON.
