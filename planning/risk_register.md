# Risk Register — 2026-10-01

> **Vigencia ADR-013 — 2026-10-07:** investigación = Team en workstation Windows institucional INFOTEP; target PAPER = Plus individual en PC personal del propietario; LIVE = UNKNOWN. Se conservan las notas/evidencias anteriores como historia. Team no prueba disponibilidad Plus ni seguridad del host personal. Diseño se resuelve durante Preparation; aceptación target R-030 se difiere antes de implementación/PAPER. S2B-ADM-01 = DEFERRED_TO_TARGET_PAPER_HOST; no acción administrativa institucional pendiente. `implementation_locked=true`.


**Estado vigente posterior — wave07:** [RC2 Team](research/R-006_shortlist_RC2_team.md) documenta madurez para decisión acotada: 8/8 jobs, SDK/bootstrap 14/14, evaluación 16/16; perfil PAPER PARTIAL. D-020 READY_FOR_DECISION, D-024 RESEARCHING; próximo gobierno ADR-011 dirección nativa, sin cierre final/freeze ni acceso Plus.

**Antecedente — ADR-010, 2026-10-05:** CURRENT_RESEARCH_ENVIRONMENT=Team; PAPER_RUNTIME_ENVIRONMENT=Team actual; FUTURE_LIVE_ENVIRONMENT=Plus individual candidato. Las cláusulas anteriores que exigían Plus para PAPER/D-020/D-024 quedan parcialmente SUPERSEDED. La evidencia original se conserva; Plus es gate P3 PRE-LIVE (R-029/D-039), sin dependencia para PAPER. Aceptación activa: [Team TP1–7](research/R-006_team_runtime_acceptance_RC0.md). No selección final ni implementación autorizada.

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

## Variante Agent Runner — 2026-10-06 (OPEN)

| K-054 | P1 | Job bajo usuario base común roba token/handle del supervisor o recupera history/cache/registry/peer export; grants amplios para compatibilidad invalidan contención | Media/Alta, valoración cualitativa | RC2 VP-01..08 + SI-06/07/16 y BL-06, supervisor externo protegido, contextos efectivos, auth mínimo/persistencia separada; no ampliar Users/Everyone/perfil ni confundir AccessCheck con aceptación | Security/Operations |

K-049/052 exigen aislamiento efectivo de recursos y linaje; no imponen una cuenta por nombre de rol. Complejidad/auth de múltiples cuentas y wrapper B se medirán en RB, sin afirmar menor probabilidad de misconfiguration por número de usuarios.

## Grant común y tránsito — 2026-10-06 (OPEN)

| K-055 | P1 | Grants Users/Everyone heredados en datos excluidos, default DACL/owner de scratch o SeChangeNotify omiten la barrera esperada de directorio; adaptación runtime reexpone peer | Media/Alta cualitativa | Probe de memoria observó counterexample de grant común; LF09 exige READ peer child positivo + own real + peer real, privilegios/DACL/parent declarados. RootDirectory/pin quiescente no son sandbox completo, no ampliar ACL anteriores. VP04/SI/BL efectivos pendientes. | Security/Quant |

## Ejecución del laboratorio S2B-ADM-01 — OPEN

| K-056 | P1 | Setup parcial, fuente/superficie incompatible, copia de ledger perdida o procesos de propiedad UNKNOWN impiden reversión verificable | Probabilidad desconocida / impacto acotado a recursos temporales; sin credenciales | Journal sanitizado flushed antes de crear, ledger protegido y manifest completo, receipt + copia hash/length, no retry/cleanup ciego; partial requiere atribución owner, procesos UNKNOWN bloquean delete. 5.1 policy blocked no workaround: PowerShell 7 existente validado solo memoria/compile, pruebas reales pendientes. | Owner admin / Plan Architect verificación |

Journal de repo y output BASE son candidatos de evidencia; no autenticidad adversarial ni autorización de borrado por sí solos. Quiescencia/operator confiables requeridos. No ampliar permisos/global policy para lograr PASS.

## Riesgos de transición y aceptación — ADR-013

- P1: validar accidentalmente PAPER desde Team/host institucional. Control: AI-plan/host separados, perfiles v0.3, R-030, nunca transferir PASS host-specific.
- P1: ejecutar transacción/admin histórica en host inapropiado o fresh clone. Control: lab DEFERRED_TO_TARGET_PAPER_HOST, guard Setup/Rollback, rebind target owner-only antes de ejecución.
- P1: diferir una pregunta genuina de diseño como si fuera test de host. Control: maturity audit R-006/R-010/R-013 e independiente; workflow/store/permissions/version choices siguen explícitos.
- P1/P2: Plus/quota/auth o aislamiento no suficientes. Control: target acceptance fail-closed; reevaluar arquitectura con owner, sin S1 operativo, silent S3 ni gasto automático.
- P3: asumir el host PAPER como LIVE. Control: FUTURE_LIVE_ENVIRONMENT UNKNOWN y decisión posterior a PAPER.

## Realización B-RT1 / evidencia portable — OPEN

- K-057 P1: keyring/logon session compartida transporta contenido entre attempts pese a HOME readonly. BL-AUTH arbitrary canary→relaunch y negative credential/process tests target; auth mínima no permite datos de jobs. FAIL obliga reparación/gobierno, no limpiar para ocultar.
- K-058 P1: launch cross-user/reboot exige privilegios inesperados, supervisor bajo A o credenciales/per-job login. AcquireRunnerLaunchCapability fail-closed; family/derechos/setup owner target, no servicio/privilegio automático.
- K-059 P1: report/binding falsificado o copiado entre config/instances produce aceptación aparente. Registro/validator C externo protegido, scope fijo, instance/fingerprint/gate phase; B1 no prueba protección del store.
- P2 residuo research: cleanup H7 auto-review rechazado dos veces (solo reason blocked by policy); procesos detenidos, ocho archivos TEMP ficticios/deps permanecen. H8 fixture retenido intencionalmente .local. No secreto/datos financieros ni workaround de borrado; no bloquea diseño ni implica rollback S2, que no se ejecutó.

## Riesgos de admisión de fuentes/validación — 2026-10-07

- K-060 P1: señales IEX/datos delayed y fills paper NBBO se tratan como mercado idéntico; simulación favorable omite costes/dividendos/liquidez. Pin feed/clocks y modelo económico independiente, pruebas de paridad y reconciliación; paper gratuito no prueba alpha.
- K-061 P0/P1: escoger actor/reglas con resultados vistos o transformar filing/uploaded a disponibilidad exacta sin historia. Preregistro/exposure log, fuentes/canales y revisiones pareadas, UNKNOWN o variante conservadora explícita; criterios antes de muestras. Fuente paga/gratis no salta gate PIT/licencia.

## Riesgos financieros de reglas/modelos — 2026-10-13

- K-062 P1: entry-to-stop0 en posición ganadora oculta pérdida futura de equity, o R2 en perdedora libera capacidad frente a R1. Q-054 gobierno explícito de medida, loss/drawdown y gap independientes, no valor elegido implícitamente.
- K-063 P0/P1: partial/top-up/split cambia p0/H/q/stops y crea falsa activación/cobertura. CandidateConfig episode/lot/rebase OPEN obligatorio, mapping broker probado antes de freeze.
- K-064 P1: descontar hold broker y reserve dos veces, o liberar claim propio durante revalidation. C_base/cash-claims exclusivos, projection/txn atomico y eventos reconciliados; NO PASS transaccional por algebra8/8.
- K-065 P1: engine libre/CLI pago confundidos, docs2.x vs install1.x o OHLCsyntheticpath tratado como tick observado. R009 pin/ruta económica, QP1–10 y realismo/costs explícitos, no engine construido desde cero por defecto.

## Condiciones ADR-015 — 2026-10-13

K-062 medida R2 conceptualmente resuelta; riesgo de usar presupuesto libre como señal de averaging-down permanece controlado por Champion config+fresh intent/eval/reservas. K-064 cash/claims/mappings aún pendiente de pruebas. Protección incierta/crossed no representa0; R027 RC1 espera fail-closed/trace y no liquida automáticamente. Aprobar método no acepta semántica operativa ni Risk Engine.

## Riesgos financieros wave03 — 2026-10-13

- K-066 P1: licencia gratuita o paid activa prohíbe retención que audit/replay necesitan; datos o métricas persistidos indebidamente o evidencia eliminada para encajar en precio. Gate rights/retention por artefacto/origen R008RC1; Starter durable REJECT, no borrar registros broker propios ni reducir audit silenciosamente. Owner antes de contratar.
- K-067 P0: declarar intacta la reserva tras exposición incidental, seleccionar/tunear sobre confirmación o comparar CAGR de ventanas distintas como iguales. Q055 O-B propuesto/exposure ledger/INTEGRITY_UNKNOWN y reevaluación owner si no se acredita independencia, criterios antes de resultados.
- K-068 P1: parser market_trades se interpreta como compra exchange o convicción; caller-supplied form/clase y rawowners tratados como end-to-end. E1 PARTIAL, clasificación determinística versionada/UNKNOWN; full factoryerror preservado, dataset/semántica/PIT gates separados.

## ADR-016 — controles de evaluación, 2026-10-14

K067 conserva integridad UNKNOWN y O-B aprobado sólo conceptual. Riesgos adicionales: número de variantes oculto, operaciones correlacionadas tratadas como muestra independiente, sesgo por regímenes elegidos tras resultados y retrasos omitidos. Registro íntegro de ensayos, criterios previos, estados INSUFFICIENT_EVIDENCE y evaluación temporal/económica por candidato obligatorios. No comparar información de Shadow tardía como contemporánea ni trasladar returns de feed ideal a broker execution.

## Wave04 — controles estadísticos y temporales

- K-069 P0: elegir endpoint/margen/método tras ver ganador o confundir selección con confirmación. Q056gobierno, EvidenceCard/F0 y MethodApplicabilityCard previos; todas variantes/discards/attempts, no modelo favorable tardío.
- K-070 P1: holding horizon largo/expiry futuro encubre quote/estado stale o feeddelayed. Freshness por input, marcasRisk y protección independientes, deadline/reconcile y escenarios; no filledOpen ideal ni GTCeterno.
- K-071 P1: independencia ficticia por filas/partialfills/activos y p-valuesNaN/inputs inválidos. Clusters/serialdependence/pairedblocks y admissionexterno, INSUFFICIENT_EVIDENCE/NOT_EVALUATED/NO_ESTIMABLE; primitivePASS no alpha.
- K-072 P1: IBKRpresets no versionados/authweekly o AlpacaOPGpermissions/GTC90d no modelados. Contracts/source/config/recovery/B1–5target, no hiddensettings ni bypass2FA, FinancialCore fueraAI.

## Aprobación económica vigente — 2026-10-14, ADR-017

[ADR-017](decisions/ADR-017-economic-objective-return-risk-efficiency.md): Q056/B DECIDED conceptual. Retorno neto competitivo + reducción material de riesgo, no minimización del riesgo aislada. Margen de no inferioridad requiere fundamento y aprobación owner antes de resultados; cash/opportunity cost y comparadores de exposición obligatorios. A secundaria/C operacional independiente; NO_STRATEGY_QUALIFIED admitido si ninguno cumple. D011 RESEARCHING, F0 incompleto; holdout UNKNOWN, lock/targetdeferral vigentes. Continúa formulación técnica/PRICE–MATR/Form4 sin nueva elección conceptual abstracta.

## Riesgos wave05

- K-073 P0: benchmark seleccionado después de resultados o mensualmente rebalanceado presentado como baseline buy-and-hold. Q057 previo y IDs/ledgers/espejos por alternativa, ámbito ETF explícito.
- K-074 P1: carry/yield ficticio, doble cash/fees o λ de cierre que usa información futura para fabricar matched risk. R008/RC3, cashREAL y gross-minus-own-cost, intervalos conocidos/clock/delay; diagnóstico limitado si datos insuficientes.
- K-075 P0: margin ampliado para pasar muestra, ES ratio inestable convertido en0 o cola bootstrap inválida omitida. MethodApplicability previa, incertidumbre/INSUFFICIENT preservadas; probe19/19 no alpha.
- K-076 P1: flagFalse/ausente interpreta compra discrecional, P interpreta exchange, amendment reemplaza íntegramente o footnotes duplicadas sobrescritas. Raw XML/version/UNKNOWN, rowmapping y quarantine, F2 sólo componentes.
- K-077 P1: QA rehash silenciosamente declaraciones antiguas por EOL/adendas. Preserve raw SHA+capturedEOL y GitblobSHA/commit; nueva variante/hash antes de nuevos resultados, no alterar captures para PASS.

## Estado vigente K2 — ADR-018, 2026-10-14

[ADR-018](decisions/ADR-018-PRICE-MATR-benchmark-package-K2.md): Q057/K2 DECIDED por propietario. EW6-BH primario, cash y espejo EW6-BH-LAMBDA-REAL obligatorios; SPY/SPY-SMA200 secundarios y mensual sólo sensibilidad predefinida. Exposición no equivale a riesgo: composición/beta/factores y limitaciones, diferencia económica frente a SPY visible, políticas reproducibles/as-of y gates conjuntos sin score compensatorio. Scope sólo ETF PRICE–MATR; márgenes/modelos/datasets y Strategy no aprobados. D011 RESEARCHING, holdout UNKNOWN, lock/targetdeferral; continuar trabajo técnico sin repetir Q056/Q057.

## Riesgos wave06

- K-078 P1: fees heterogéneos/dividend reinvest restablecen equal-weight tácitamente, cash receivable gastado antes de disponibilidad. Booktargets/realizados/deriva/as-of y futura paridadengine.
- K-079 P0: ES(S-M) sustituye diferencias deES, cola95nominal50 se trata como independiente, o MC14/14 se declara calibraciónPASS. RC4 estimando, referencepositive/mass/clusters y pilotlimits; incertidumbre/métodos previos.
- K-080 P1: inputsInf producen outputs finitos y pasan admission por error. Validación finitud/escala/clocks antes de librería; E4observación preservada.
- K-081 P1: índices SEC actuales/revisados reescriben universo histórico; acceptance/dailydate usado como receipt. PAC/version/canal gates, M11unknown no reservaabierta.
- K-082 P0: overhead del sistema cargado a cash/EWpasivo para esconder oportunidad, o gastos/scaleUNKNOWN tratados como0. NI/cash net_after_incremental_ops deS contra costespropios debenchmark, ES net_trading; gobiernoeconómico no capital elegido.
- K-083 P1: pagar por historia se confunde con derechos/PIT/quality; retención al terminar y sourceindicative ignoradas. R008wave03/phasedscorecards, no contratación ni eliminación de audit para encajar en precio.

## Vigencia M1 — ADR-019, 2026-10-14

[ADR-019](decisions/ADR-019-PRICE-MATR-economic-utility-M1.md): Q058/M1 DECIDED sólo utilidad ex ante ETF PRICE–MATR: δNI1ppCAGR/año, εcash+1ppneto/año, ρES20%, q95. Siete condiciones: no adaptar a potencia, inferencia válida antes dePASS, guardrails complementarias, escala/costes previos sin capital favorable, espejo defendible, estados separados y NO_STRATEGY_QUALIFIED. Números no equivalen a método/datos/Strategy/backtest aceptados; D011RESEARCHING/F0incompleto, reservaUNKNOWN/lock/targetdeferral. Continuar técnica sin reabrir B/K2/M1.

## Riesgos wave07

- K-084 P0: NULLconjunta/AND0 oculta error marginal de CI o baja potencia de otrogate. E5/E6screen, MVleastfavourable/familia/MCprecision antes dePASS; no elegir método por backtestfavor.
- K-085 P0: recoverycensurado convierte a0/FAILtotal o DDhistórico se trata como maxDD futuroestimado sin modelo. TablaQ059/RC5 tipos/scope/agregación yestimando/path explícito.
- K-086 P1: expiry deentrada caduca protección o señal de exit elude materialpause; slots/remains dobles/cashventa no reconciliado usados. Configsemánticas y G1G2precedence, broker mapping stillNOT_ADMITTED.
- K-087 P1: Riskcap genera por sísolo target, menorR2 causaadds, partialavg baja protección oATR seactualiza retroactivamente. Strategytarget OPEN/cutoffATR/rawrebase/desiredmonotone/qtyconfirmed, no autoridadagent ni G3.
- K-088 P0: parámetros propuestos se presentan como Strategy seleccionada o se rehacen hashdeclarado tras revisión. IDs/parents nuevos yrawcapture+activerevision, configuraciónfalse y0trials.
- K-089 P1: elegir capital/coste postresultado para calificar o atribuir mismosoverhead areferencia.20celdaspredefinidas noanchor elegido, UNKNOWNoperational ystreams separados.

## Vigencia G-R1 — ADR-020, 2026-10-15

[ADR-020](decisions/ADR-020-PRICE-MATR-complementary-guardrails-G-R1.md): Q-059/G-R1 DECIDED en preferencia económica ex ante: no deterioro de DD frente a EW6-BH completo ni de volatilidad diaria frente al espejo K2 admisible. ES95/M1 primario y NI/cash/K2 conjuntos; recuperación/underwater/pérdidas/gaps/slippage/extremos obligatorios. DD exige estimando/horizonte/path/incertidumbre y aplicabilidad válidos; una trayectoria/bootstrap genérico no demuestra futuro. Volatilidad incluye upside/downside. Guardrails relativas no son límites absolutos Risk D-031. G-R2 no aprobado ni fallback. Estados separados y NO_STRATEGY_QUALIFIED; ningún método/dato/broker/Strategy/F0/implementación aceptado. Continuar P0/P1 financieros en checkpoints agrupados; holdout UNKNOWN/lock/targetdeferral.

## Riesgos wave08

- K-090 P0: añadir veto d_obs o sustituir claim esperado/predictivo sin gobierno. Review elimina veto no aprobado; DD-E sólo investigación, no PASS.
- K-091 P0: elegir fresh/carry o reset tras resultados de selección. Regla antes deF0; F1 sólo materializa estado, sin resets anuales favorables.
- K-092 P1: G2 cancela protección por dependencia parent/children; semánticaFIX transferidaTWS. Grafo/API/version/qty/efectos yB3; sin efecto seguro no cancelación automática.
- K-093 P1: make_qty por defecto redondea hacia arriba. QE1ROUND prueba componente; futuro adapter floor validlot y boundRisk, no QP6 aceptado.
- K-094 P1: GLD2004 se rellena con proxy para cumplir200sesionesenero2005; universe/window alterados. W0eligibility/subcards, sinwarmup completo ficticio ni fuente admitida por metadata.
- K-095 P1: 10k principal oculta costes de otras escalas o UNKNOWN=0, se interpreta como funding/LIVE aprobado. ADR021 cobertura5obligatoria,20celdas+todosmodelos, scope explícito y no cherry-pickK.
- K-096 P1: constructor6/6se presenta como engineparity/aceptaciónWindowsPlus o entorno de dependencias completo. QE0scope/import/init, clickfaltante, no QP/backtest/runtimeacceptance.
- K-097 P1: storageprivado/derivedpermissions implican retención perpetua o compartirrawconIA. AclaracionesR008 pendientes, no vendor elegido; sin mensajes externos sin autorización.

## Riesgos wave09 — fuentes/PIT y entrega

- K-098 P1: latest-only o backfill se usa como conocido en el pasado. CA01–03: versiones, clocks, disponibilidad demostrable, reconstrucción etiquetada; matriz aún NOT_EXECUTED.
- K-099 P1: fecha de security-master o profundidad global se transfiere a acciones/precios y cambia ventanas. Admisión por componente/período/seis subcards, no datos admitidos.
- K-100 P1: autoasignación de ISIN/scope amplio consume cuota o modo sin asignar omite datos. Scope explícito y gate antes de llamada, completitud no inferida de respuesta vacía.
- K-101 P1: preparar correos se interpreta como autorización para enviarlos o se marca pendiente sin envío. AGENTS/ledger: owner delivery, 0envíos, automatic_send_authorized=false; actualizar sólo con evidencia real.
- K-102 P1: respuesta comercial genérica admite dataset o archivo/IA/terminación por inferencia. Derechos contractuales, cobertura, calidad y evidencia técnica/PIT independientes; sin respuesta específica, no admisión. Investigación no bloqueada globalmente.
