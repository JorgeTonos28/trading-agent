# Risk Register — 2026-10-01

**Estado vigente posterior — wave07:** [RC2 Team](research/R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

**Vigencia actual — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

**Lectura:** registros/tablas actuales y esta adenda gobiernan; notas fechadas de hitos previos se conservan como historia, incluidos sus antiguos siguientes pasos Plus.

Escala inicial cualitativa: `Alta/Media/Baja`; se calibrará después. Dueño indicado por **función**, no persona asignada. El riesgo residual seguirá abierto hasta prueba/control documentado.

| ID | P | Riesgo | Prob./Impacto | Control o evidencia exigida | Dueño funcional |
|---|---|---|---|---|---|
| K-001 | P0 | Look-ahead por cierres, ajustes, releases o timestamps | Alta/Alta | ADR-004 fija `eligible_from`/revisiones as-of; faltan muestras PIT y pruebas por dataset D-018/022/033 | Data/Quant |
| K-002 | P0 | Holdout contaminado y overfitting por búsqueda agéntica masiva | Alta/Alta | Registro de experimentos, holdout sellado/forward, multiple testing | Quant |
| K-003 | P0 | Riesgo de gap excede `0.5%` pese a stop teórico | Alta/Alta | ADR-006 aprueba controles compuestos como arquitectura; riesgo residual abierto hasta escenarios/umbrales aprobados y probes de orden D-030/031 | Risk |
| K-004 | P0 | Duplicación u omisión de orden tras timeout, DB/stream caída | Media/Alta | ADR-003 fija identidad interna, `UNKNOWN` y ledger; faltan probes broker y replay/chaos D-021/030 | Execution |
| K-005 | P0 | Autoridad ambigua de agente sobre qty, liquidación o reanudación | Media/Alta | ADR-001/002/006 fijan A+, G1+G2, control compuesto y reanudación humana; faltan especificación/pruebas D-035/013 | Architecture/Risk |
| K-006 | P1 | Broker no elegible para dueño RD o paper/live difieren | Media/Alta | Confirmación de elegibilidad y probes antes de selección | Broker research |
| K-007 | P1 | Licencia/coste/derechos de mercado impiden uso de datos | Media/Alta | Due diligence contractual, coste y alternativas | Data research |
| K-008 | P1 | Datos ajustados/total return o dividendos mal tratados | Alta/Alta | Reconciliación entre fuentes y casos corporativos | Data/Quant |
| K-009 | P1 | Dependency/plugin/MCP comprometido o prompt injection | Media/Alta | Threat model, permisos mínimos, sandbox y evals | Security |
| K-010 | P1 | Stack propuesto sobredimensiona V1 y consume operación | Alta/Media | Build-vs-Reuse, benchmark y coste total | System architecture |
| K-011 | P1 | Audit trail incompleto tras fallos o cambios de versiones | Media/Alta | Event lineage, replay, backup/restore probado | Data/Operations |
| K-012 | P1 | Monitoreo/alertas sin dueño ni acción medible | Media/Alta | Runbooks y SLO asignados, tabletop | Operations |
| K-013 | P2 | Paper fills/quotes ocultan slippage y disponibilidad real | Alta/Media | Shadow comparación y escenarios stressed | Execution/Quant |
| K-014 | P2 | Kill switch `CLOSE_ALL` agrava error o mercado ilíquido | Media/Alta | ADR-002 prohíbe G3 general en PAPER V1; probar G1+G2 y drills; cualquier G3 futuro requiere ADR humano | Risk/Operations |
| K-015 | P3 | Error legal, fiscal o de elegibilidad en RD/EE.UU. | Media/Alta | Revisión profesional antes de live | Owner/Legal |
| K-016 | P3 | Escalamiento live prematuro por métricas favorables | Media/Alta | Gates y autorización explícita | Owner/Risk |
| K-017 | P4 | Datos alternativos con disclosures tardíos crean falso alpha | Alta/Media | Publicación observada y backtest neto | Alternative data |
| K-018 | P1 | Baseline referenciado por ruta inexistente y duplicación `.project/`/`planning/` | Alta/Media | MITIGADO: `AGENTS.md` corregido y estado trasladado a `planning/`; verificar referencias al compilar RC1 | Plan Architect |
| K-019 | P0 | Elegir MATR_V1 por inercia del borrador y cerrar falsamente Strategy V1 | Alta/Alta | ADR-000, D-008 OPEN, comparativa R-020 con aprobación humana | Plan Architect/Owner |
| K-020 | P0 | Tratar un tutorial promocional como una estrategia completa o resultados auditados | Alta/Alta | Reconstrucción primaria con timestamps, separar reglas y claims; no inferir alpha | Quant/Plan Architect |
| K-021 | P0 | Seleccionar entre múltiples candidatos mirando el holdout, aunque MATR_V1 nunca se haya backtesteado | Media/Alta | Preregistrar criterios y acceso OOS para todo el torneo; registrar experimentos | Quant |
| K-022 | P0 | Video induce a tratar stop 10/20%, trailing y compras tras caída como política de riesgo coherente; posible exposición creciente y gap no cubierto | Alta/Alta | Especificación de precedencia, sizing y escenarios antes de admitir VID-TS | Risk/Quant |
| K-023 | P0 | Backtest congresual selecciona ex post al político ganador o usa fecha de operación antes de disclosure | Alta/Alta | Selección ex ante, publicación/ingestión PIT y evaluación OOS | Quant/Data |
| K-024 | P1 | Copiar claves de broker al chat o habilitar agente/CLI con autoridad directa sobre órdenes | Alta/Alta | Secretos aislados, permisos mínimos e invariante D-002; flujo del tutorial solo como referencia | Security/Architecture |
| K-025 | P2 | Automatización de cinco minutos se interpreta como stop continuo; falla ante gaps, caída rápida o indisponibilidad | Alta/Alta | Protección broker-side cuando corresponda, estados de fallo y pruebas de ejecución | Risk/Execution |
| K-026 | P0 | Reducir Smart Money a Congreso crea arquitectura de datos estrecha y obliga a rediseño al añadir Form 4, 13F u otras fuentes | Alta/Media | ADR-005 fija familias/roles/gates y ADR-004 clocks/revisiones; faltan probes y scorecards D-033 | Architecture/Data |
| K-027 | P1 | Seleccionar agregador por marketing sin comprobar timestamp PIT, licencia o backfill histórico | Alta/Alta | R-025: scorecard por dataset, comparación con fuente oficial y probes; ninguna selección por presencia en video | Data/Procurement |
| K-028 | P0 | Pedagogical Agent explica causas inventadas o transforma aprendizaje en cambio no aprobado de Champion | Media/Alta | Trazas verificables, incertidumbre explícita y separación estricta de autoridad D-019/D-005 | Pedagogy/Architecture |
| K-029 | P1 | Una propuesta shadow cruza por error la frontera hacia `TradeIntent`, órdenes o asignaciones | Media/Alta | Aislamiento por permisos/esquema/canal, pruebas negativas, auditoría y alerta; D-034/ADR-001 | Security/Architecture |
| K-030 | P1 | Comparación del shadow usa datos posteriores, fills ideales o contexto distinto y exagera utilidad | Alta/Alta | Contexto pareado PIT, costes/fills hipotéticos versionados, protocolo preregistrado y replay; R-026 | Quant/Data |
| K-031 | P0 | Una entrada ejecuta sin protección aceptada o un cancel/replace elimina stop existente y deja exposición inadvertida | Media/Alta | ADR-002 conserva protección bajo G2; estado explícito, reconciliación y runbook D-012/013; probes D-030 | Risk/Execution |
| K-032 | P0 | Congelar runtime/topología/plugin por inercia antes de descubrir Skills, conectores y workflows reutilizables | Alta/Alta | Agent Capability Gate en AGENTS.md; R-006/D-020 P0, D-024 abierto hasta fichas, coste/licencia, probes y revisión crítica | Plan Architect/Architecture |
| K-033 | P1 | Portar Skill financiera de tercero con recomendaciones operativas, datos no PIT o permisos excesivos | Media/Alta | Auditar licencia, instrucciones, dependencias y tool scopes; probe de inyección/no autoridad; ADR-001/004/006 y D-027 | Security/Research |
| K-034 | P0 | Confundir suscripción Team/Plus con API facturada o activar gasto no aprobado | Media/Alta | ADR-010: TP por etapa, evidencia por instancia; R-029 solo PRE-LIVE. ADR-008 aprobación antes de gastar. | Plan Architect/Operations |
| K-035 | P1 | Portar contenido Apache-2.0 Anthropic suponiendo que conectores, datos, scripts y runtime comparten licencia o acceso | Media/Alta | Auditoría por archivo/dependencia; separar contenido público de servicios externos y preservar atribución al portar | Research/Security |
| K-036 | P3 | Migración LIVE candidata Plus basada en entitlement Team inferido; reclasificado de PAPER por ADR-010 | Media/Alta | ADR-010: TP por etapa, evidencia por instancia; R-029 solo PRE-LIVE. ADR-008 aprobación antes de gastar. | Plan Architect/Operations |
| K-037 | P0 | Convertir ahorro PAPER en veto permanente a pagos LIVE o escoger gratis pese a brecha material de calidad/fiabilidad | Media/Alta | ADR-008, fichas económicas por fase/capa, comparación de suficiencia, economía unitaria y condición evidenciada para pagar; aprobación antes de gasto | Architecture/Owner |
| K-038 | P0 | Mantener gate Plus histórico como bloqueo PAPER después de supersession | Media/Alta | ADR-010: TP por etapa, evidencia por instancia; R-029 solo PRE-LIVE. ADR-008 aprobación antes de gastar. | Plan Architect/Operations |
| K-039 | P0 | Interpretar buena conducta LLM o sandbox sintético como garantía de seguridad financiera | Alta/Alta | Medir respuestas e intentos de herramientas por separado; no dar broker/secretos; negativos de harness no prueban producción | Architecture/Security |
| K-040 | P1 | Convertir LLM/cuotas en dependencia permanente del trading sin evidencia de necesidad | Media/Alta | Conservar núcleo local determinístico + Codex intermitente como alternativa; separar fallos de agente e incidentes materiales ADR-002 | Architecture/Operations |
| K-041 | P1 | Schema genérico mezcla tareas research con propuestas, traduce rol/acciones y oculta derivaciones numéricas | Alta/Alta | Contratos RC0 + wave 06 trusted role/schema, targets/Decimal/lineage y refs tipadas; admission v1 falso rechazo conservado. Numeric spine no valida prosa/seguridad completa; D-034/029 abiertos | Architecture/Research |
| K-042 | P1 | Catálogo/plugins/permisos de superficies distintas y contenido propietario producen una falsa selección portable | Media/Media | Wave 05 Data: catálogo instalado vs inspector not_installed, manifest Proprietary. Verificar superficie/licencia/Team, no copiar bundle; Plus PRE-LIVE | Architecture/Licensing |
| K-043 | P1 | Shadow se ancla al resultado Champion o compara cartera acumulativa distinta como si snapshot fuera idéntico | Alta/Alta | Ocultar Champion al generador, sealed outputs/hashes; separar decisión desde cartera real de trayectoria contrafactual, futuros outcomes no entran al corte; contrato shadow RC0/R-026 | Quant/Architecture |
| K-044 | P1 | Smoke/burst Team se interpreta como cuota sostenible, seguridad o cumplimiento de PAPER completo | Media/Alta | ADR-010: TP por etapa, evidencia por instancia; R-029 solo PRE-LIVE. ADR-008 aprobación antes de gastar. | Plan Architect/Operations |

| K-045 | P1 | Paquete aislado pierde reglas raíz, overrides/truncación cambian autoridad o se asume que AGENTS aplica permisos técnicos | Media/Alta | R-028 prueba root/cwd/override/discovery; manifiesto de reglas y contrato global explícito; aislamiento técnico D-027 independiente | Architecture/Security |
| K-046 | P1 | Bootstrap hereda readiness Team, copia secretos/settings personales o oculta dependencias/manual actions, haciendo irreproducible el target | Media/Alta | ADR-009; perfiles separados, outputs sanitizados, UNKNOWN bloquea requisito obligatorio, drift/recovery y fresh-clone probes, nunca auth/secrets Git | Operations/Plan Architect |
| K-047 | P1 | SDK default auto-accept de command/file requests amplía autoridad si se reutiliza sin handler explícito | Alta/Alta | Código pinado/probe offline wave07; fail-closed explícito y denegación válida de cada método, permisos D-027/034 y upgrade regression. No promesa por prompt. | Security/Architecture |

Todos los riesgos salvo K-018 siguen `OPEN`; una arquitectura aprobada aún requiere datos, parámetros y pruebas para mitigar riesgo operativo.

**K-045/046, evidencia inicial R-028:** root/nested/aislado/override y Skills probados en fixture Team; 31 checks offline. No cierre por prompt/schema. Cleanup WinError 32 tras inferencia añade caso lifecycle a EB6/GP5; nuevo entorno requiere evidencia propia.

**K-045/046 tras fresh clone:** seis paquetes correctamente descubiertos y dos smoke con bloqueo/autoridad; 31 deltas CRLF/LF exigen hashes Git del commit + observación local separada. Errores de cleanup y manifest hash preservados. Perfil PARTIAL, full target gates y modelo de seguridad siguen abiertos.

## Riesgos adicionales P1 — hardening (OPEN)

| K-048 | P1 | Trabajo background largo bloquea shadow pese a prioridad; retries/interaction agotan cuota o deadlines | Media/Alta | Separar queue/service/total, gate burst durante quant, parent/deadline originales, dimensionamiento real; scheduler/concurrencia final pendientes | Architecture/Operations |
| K-049 | P1 | Identidad/namespace compartido revela Champion al shadow o holdout confirmatorio a research/quant | Media/Alta | Dominios ACL/export mínimo, admission y store externo; prueba lectura prohibida antes de freeze, no garantía por prompt | Security/Quant |
| K-050 | P1 | Restore revive lease viejo o reacepta/recuenta output perdido por RPO | Media/Alta | Incarnation externo en envelope, job ID/manifest histórico intactos, fencing y RECOVERY_GAP/UNKNOWN; restauración real del motor final | Operations/Architecture |

**K-027 evidencia adicional R-020:** la propia SEC indica que no hay timestamp first-available en sec.gov; API pública/acceptance no prueba availability de canal histórico. Fuente/canal conservador modelado explícito y comparación proveedor siguen gates, no elegir gratis por defecto. Ver DatasetCard SEC.

## S2 — riesgos adicionales (OPEN)

| K-051 | P1 | Allowlist red de comandos se confunde con egress del proceso completo; reglas locales ignoradas por policy merge o block/allow diseñado incorrectamente | Media/Alta | S2 SI-09/10, ActiveStore/source y acceso positivo/negativo real; no cambiar política global ni construir driver; ADM-02; UNKNOWN bloquea aceptación | Security/Operations |
| K-052 | P1 | Permitted field/caché/history/same-SID job filtra decisión Champion pese a separación de roles | Media/Alta | BL-01/03/06 + SI-16: DAG/version/causal export antes de decisión, contexto constante, sesiones/stores separados, revocar vistas y terminar handles | Security/Quant |
| K-053 | P1 | Logger controlado por job o LogBlocked=False deja intentos rechazados sin reconstrucción confiable | Media/Alta | SI-14 observer externo + eventos OS donde aplique, receipts protegidos; gate explícito de audit/SACL/red si necesario; no prometer logging existente | Security/Operations |
