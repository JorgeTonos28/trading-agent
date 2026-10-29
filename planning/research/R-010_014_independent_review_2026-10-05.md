# Revisión crítica independiente — P1 PAPER hardening

2026-10-05. Propietario solicitó revisión independiente. Reviewer: agente separado `independent_hardening_review`, read-only; Plan Architect autor de contratos. **No auditoría humana, aprobación de arquitectura, ejecución de tests por reviewer ni cierre de decisiones.** Inspeccionó contratos, ADR-011/012, gates, preregistro R-020, código/resultados preservados y H4 posteriormente. H6 fue añadido al alcance después; revisión posterior se registra abajo.

## Hallazgos y remediación

| ID | Prioridad | Hallazgo | Remediación documental/probe / gate restante |
|---|---|---|---|
| IR-01 | P1 | Enums distintos entre 06 evidence y 08 workflow | Mapping delivery-contract-v2 explícito; transport/workflow/attempt/admission separados; evidencia v1 preservada. Consumers finales aún por implementar/verificar |
| IR-02 | P1 | Generación sola no cubre lease expiry/current attempt/owner/lifecycle; faltaba race | Contrato ampliado y suplemento SQLite 11/11 incl. dos recepciones concurrentes. Lease renovación/clock/engine real pendientes |
| IR-03 | P1 | Restore revive workers/leases o pierde receipts confirmados | Epoch externo en envelope y RECOVERY_GAP/UNKNOWN; job_id/manifest original intactos, outputs históricos preservados. Fixture lógico 4/4 incluye policy assignment, no garantía backup real |
| IR-04 | P1 | Aislamiento real podía quedar totalmente diferido a P2 | P1 exige probe empírico de viabilidad de frontera elegida bajo identidad efectiva antes de freeze; P2 integra core runtime |
| IR-05 | P1 | Namespace compartido revela Champion/holdout pese a tools exactas | S2 por dominios/export mínimo; shadow separado de pedagogía/Champion; holdout quarantine/acceso denegado. Test físico aún pendiente |
| IR-06 | P1 | Vigencia Team mezclada con endpoints históricos Plus/ADR-011 | Adendas y rotulado históricos; D-020 cerrado solo dirección, D-024 abierto; Plus P3. Probes originales no reescritos |
| IR-07 | P2 | 13 cargas abstractas tratadas como jobs, ventanas nuevas no ensayan retry | v1 conservado; v2 63 service requests, workload 50 jobs + hasta13 reserve, denominador requerido incluye missing. Actual retry conserva parent/deadline; acceptance real pendiente |

Reviewer adicionalmente señaló at-most-one frente a exactly-one y definición de job que excluía no-output; ambos corregidos. No identificó concesión nueva de autoridad ni contradicción que invalide dirección ADR-011. Las reparaciones reducen ambigüedad; enforcement permanece gate empírico.

## Evidencia revisada y límites

H4 SDK/CLI0.160 emparejado por resolver default, 2/2 research/shadow, Skill/read tool/schema, cleanup; compatibilidad acotada, no aislamiento/quota/pin final. H2 11/11 y restore4/4 inspeccionados como fixtures, no ejecución independiente. No fuente de rendimiento real ni gate pedagógico/financiero completo.

S2 configuration/identity/ACL/IPC/egress/canaries; motor/store y backup/migración; workload/cupo/auth/continuidad; blinding/holdout; permisos/config efectivos y validación integrada permanecen abiertos. La dirección requiere gobierno de ADR-012; no concluir READY FOR IMPLEMENTATION de esta revisión.

## Addendum de coherencia

Reviewer confirmó H3 v2 y workload reparados sin claim de retry/rate. Incarnation se propagó a dispatch/envelope/lease/tool receipts/admission, separado de fingerprint; no cambia job_id ni manifest histórico ni rechaza retroactivamente outputs admitidos.

Addendum final recibido: reviewer inspeccionó código y resultados H6; 10/10 respaldan duplicate-ID rejection, una acción automática de schedule y persistencia de workflow/run, **longitud de history** y estado tras kill/restart, con cleanup. No compara todos los eventos del history, worker/Activities/retries, Codex integrado, aislamiento ni despliegue productivo. No hallazgo documental crítico adicional identificado; D-024/D-027 siguen abiertos. No ejecución independiente ni aprobación final.

## Revisión posterior a dirección S2 aprobada

La revisión read-only continúa en [R-013 S2](R-013_S2_independent_review_2026-10-05.md): persistencia propia del SID, env de probes, controles positivos y full-process egress. Reparaciones documentales/source activas verificadas; no S2 acceptance ni permisos finales concedidos.
