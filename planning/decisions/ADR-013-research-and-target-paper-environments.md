# ADR-013 — Entornos de investigación y PAPER; diseño y aceptación separados

2026-10-07 · D-043 · P0 · **DECIDED — instrucción explícita del propietario**.

## Decisión

| Dimensión | Entorno aprobado / estado |
|---|---|
| RESEARCH_AI_ENVIRONMENT | ChatGPT Team |
| RESEARCH_HOST | Workstation Windows institucional administrada por INFOTEP |
| TARGET_PAPER_AI_ENVIRONMENT | ChatGPT Plus individual |
| TARGET_PAPER_COMPUTE_HOST | PC personal Windows administrada por el propietario |
| FUTURE_LIVE_ENVIRONMENT | UNKNOWN; se decidirá después de PAPER |

Team/institucional sirve para Preparation, investigación, arquitectura, estrategia y proveedores. No será host PAPER. Bootstrap, aceptación Plus, pruebas administrativas de seguridad, implementación después de DoR, backtests ejecutables, integración, carga/recovery y PAPER corresponden al target personal/Plus. No se solicita acceso Plus ni administración institucional en esta fase.

## Supersession y continuidad

Supersede **parcialmente ADR-010/D-038**: Team deja de ser PAPER; Plus deja de estar reservado exclusivamente a PRE-LIVE. Supersede la premisa Team→Plus post-PAPER de R-029/D-039; esos registros quedan históricos. La Deployment Source Policy de ADR-010 permanece vigente: `plan-architect` candidato; `main` baseline estable aprobado; release/tag aprobado para despliegue. Sin merge, tag ni promoción automática.

Conserva ADR-011 A, sus disposiciones RC2 y automatización por eventos/calendario; sustituye únicamente el plan/superficie operacional: **núcleo local determinístico + jobs Codex nativos en el target Plus, sujetos a aceptación**. A+, G1+G2, ADR-006, Shadow sin autoridad, admisión externa y aislamiento S2-B candidato continúan. Ninguna transferencia de entitlement, credenciales o aceptación de seguridad desde Team.

ADR-007/008 y el scope OpenAI+Anthropic siguen vigentes. Tier 0 operacional significa incluido en Plus objetivo o assets públicos; lo observado en Team sirve como evidencia conductual/de diseño. API separadamente facturada no se convierte en Tier 0. LIVE runtime/host/coste pendientes, sin gasto autorizado.

## Modelo de estados y gates

Se mantienen los seis estados del Decision Register. Se añaden dimensiones independientes:

- `design_status`: RESEARCHING / READY_FOR_DECISION / DESIGN_DECIDED.
- `target_acceptance_status`: TARGET_ACCEPTANCE_DEFERRED / NOT_TESTED / PARTIAL / ACCEPTED / FAILED.
- `operational_status`: NOT_IMPLEMENTED / NOT_TESTED / ACCEPTED / FAILED.

`DESIGN_DECIDED / TARGET_ACCEPTANCE_DEFERRED` no significa runtime aceptado ni autorización de implementar. No se cierra una pregunta arquitectónica realmente abierta renombrándola como aceptación futura.

| Etapa | Evidencia requerida | Efecto |
|---|---|---|
| Preparation / design | Contratos, alternativas/Build-vs-Reuse, versiones/política de actualización, permisos propuestos, protocolos, dependencias y revisión crítica; pruebas independientes del target en Team | Permite cerrar decisiones de diseño con el gobierno correspondiente y preparar MASTER_PLAN; no habilita implementación |
| Target transition / antes de implementación | Fresh clone en PC personal, identidad/acceso/entitlement Plus, permisos efectivos SI/BL/RB/VP, native auth y full-process/network/IPC, smoke/recovery no financiero; aprobación del plan y gates DoR | Requisito previo a READY_FOR_IMPLEMENTATION; no debe depender de que ya exista Trading OS |
| Sistema construido / antes de PAPER autónomo | Backtests, broker/datos, integración financiera, carga representativa, recovery/observabilidad, seguridad y calidad de reports del sistema final | PAPER_RUNTIME_ACCEPTED cuando todos los gates operacionales aplicables pasen |
| Después de PAPER / LIVE | Elegir host/runtime, economía y gates LIVE específicos | Nueva decisión humana; no hereda aceptación de PAPER automáticamente |

P0/P1 de diseño deben cerrarse durante Preparation. Obligaciones de aceptación target siguen **P1**, programadas en R-030 antes de implementación. Preparar o revisar el master plan con esas obligaciones explícitas no levanta `implementation_locked=true`. El checkpoint `AGENTIC_ARCHITECTURE_DESIGN_COMPLETE` es acotado y necesita contratos completos/revisión; jamás equivale a `PAPER_RUNTIME_ACCEPTED`, DoR global ni freeze financiero.

## S2B-ADM-01

**DEFERRED_TO_TARGET_PAPER_HOST**. No FAIL ni REJECTED. Razones: el host institucional no concede los privilegios requeridos y no será operacional; evidencia específica del host tendría que repetirse. La autorización del 2026-10-06 se conserva como historia del scope temporal, no como permiso para ejecutar ahora en INFOTEP. Se retira la solicitud pendiente de crear cuenta local en este host.

Preservar runbook, harness, acceptance matrix, contratos, QA y rollback. Antes de ejecutar en PC personal, onboarding debe comprobar fuente/bytes revisados, estado fresco, binds SID/path/transaction y confirmación del administrador propietario para esa instancia. No copiar SID, journal de transacción, autenticación ni passwords del host de investigación. Nuevas policies/permisos requieren sus gates específicos; FS PASS solo no acepta S2-B.

## Trazabilidad y trabajo siguiente

- R-030: P1 Target PAPER Environment Transition & Acceptance; diseño hoy, ejecución diferida.
- R-006/R-010/R-013: terminar preguntas arquitectónicas resolubles en Team; revisar workflow/store, frontera nativa y contratos antes del checkpoint de diseño.
- D-024/D-027/D-037: registrar diseño y aceptación separados, sin declarar DECIDED global por esta corrección.
- Continuar R-020/D-008 y P0/P1 financieros sin esperar target. Selección final de estrategia/broker/riesgo/arquitectura material conserva gobierno humano.

No se ejecutaron usuarios, ACL, firewall, servicios, autenticación o integración financiera para registrar esta decisión.
