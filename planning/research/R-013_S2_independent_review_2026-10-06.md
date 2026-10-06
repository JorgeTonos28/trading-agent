# R-013 RC2 — revisión independiente de cuentas y contextos

2026-10-06. Reviewer `/root/independent_hardening_review`, agente distinto del autor, continuidad de revisión crítica P1 requerida en roadmap §3.16 y solicitada por propietario. **Solo lectura**, sin editar, ejecutar probes ni modificar sistema. Revisión de fuentes primarias, comparativa A/B/S3, contrato/acceptance RC2, ADR-012, fuente/JSON/README de AccessCheck y focal owner. No auditoría humana, aprobación arquitectónica, prueba operacional o aceptación de aislamiento.

## Hallazgos, reparación y verificación

| ID | Prioridad | Hallazgo / criterio | Resolución verificada / evidencia pendiente |
|---|---|---|---|
| IR-RC2-01 | P1 | Seguridad financiera y blinding no imponen una cuenta Windows por rol; mismo SID irrestricto con store compartido sí expone datos | Comparativa/ADR/RC2 distinguen TokenUser y contexto efectivo; B candidato condicionado, core/control fuera del modelo. No necesidad de rol→cuenta demostrada |
| IR-RC2-02 | P1 | Supervisor bajo A y job con TokenUser=A: owner es principal/rights, no PID; ausencia de grant explícito WRITE_DAC no acredita protección | RC2 explicita owner/DACL/OWNER RIGHTS/integrity; VP-03/04 prueban READ_CONTROL/WRITE_DAC/WRITE_OWNER, DACL/process/token/IPC/handles. Config/pruebas reales pendientes; sin bypass operacional observado |
| IR-RC2-03 | P2 evidencia | Descriptor `financial_canary` no tiene positivo autorizado; dos denials no muestran diferencia frente al token base | README/dossier lo rotulan **ungranted object**, no protección financiera. JSON/source originales preservados; comparativa útil usa positivos y cross-view deny con mismo usuario |
| IR-RC2-04 | P1 | Auth/DLL/registry/cert/refresh podría exigir grants amplios, perfil/history compartido o recuperar estado ajeno | RC2 exige auth mínimo, no Users/Everyone/perfil por conveniencia; DPAPI CurrentUser no barrera entre jobs same-user; persistencia J/registry/cache/history y relaunch VP/RB pendientes |
| IR-RC2-05 | P1 | Contener shell no contiene SDK/caller/app-server/model/auth/connectors/children; supervisor/desktop/IPC no protegidos por role JSON | Contrato/matriz exige full harness, control externo, procesos/handles/egress/IPC/desktop; native compatibilidad UNKNOWN, ningún framework/launcher seleccionado |
| IR-RC2-06 | P1 decisión | Menos cuentas puede ahorrar onboarding/login, pero wrapper/supervisor añade trabajo y superficie trusted | Comparativa distingue coste operativo/auth/recovery/trabajo propio; no promesa B<A ni menor probabilidad de misconfiguration. S2-A por necesidad; S3 no automático |

## Verificación del focal owner y evidencia

Reviewer confirmó SHA256 de fuentes 01/02 contra README/JSON y del focal owner `0a2e8db519c803190c9ea9b180640cb5921e5793257c493ed26d55991ebd80a4`. Fuente/JSON/tabla contienen **27 observaciones** (tres tokens × tres políticas × tres derechos): token base owner propio permite READ_CONTROL/WRITE_DAC; OWNER RIGHTS cero los deniega; ambos restringidos deniegan los tres derechos en los fixtures. Diez checks originales repetidos marcados como regresión, sin contarlos como evidencia independiente nueva.

No bypass observado bajo estos tokens restringidos; no protección de supervisor/process/IPC/filesystem reales demostrada. No launch, impersonación efectiva, objetos reales modificados o políticas ejecutadas. AccessCheck no genera audit OS. Todos SI/BL/RB/VP efectivos NOT_TESTED; VP03/04 siguen obligatorios.

**Conclusión del reviewer:** S2-B sustentada como dirección candidata para investigar, sin compatibilidad Codex/contención operacional ni selección de mecanismo. Hallazgos P1/P2 reparados documentalmente y verificados; no otro defecto material que impida presentar el dossier. ADM-01 DEFERRED/NOT_AUTHORIZED, D-027/D-024 abiertos; sin permiso administrativo ni gasto. La recomendación requiere gobierno humano de dirección revisada antes de nuevo laboratorio.

[Comparativa](R-013_S2_variants_comparison_2026-10-06.md), [RC2](../08_S2_agent_domain_contract_RC2.md), [acceptance](R-013_S2_variant_acceptance_RC2.md), [fuentes/resultados](probes/r013-s2-variants/README.md). Mantener revisión 2026-10-05 como antecedente; esta revisión no reescribe su evidencia.
