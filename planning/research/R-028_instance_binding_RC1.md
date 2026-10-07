# R-028 — Binding de instancia, fingerprint y evidencia — RC1

2026-10-07 · diseño P1 portable, independiente de Plus/host. Repara hallazgo de revisión independiente ADR-013. No se crea identidad operacional ni perfil observado ficticio.

## Identidad y fingerprint

`environment_instance_id`: UUID opaco creado por control/onboarding en el host aceptado, persistido en registro local protegido fuera de Git. No es account ID, SID, nombre de equipo, serial ni secreto. Otro host/restauración que no pueda demostrar continuidad recibe nuevo ID y gates afectados se revalidan. Restore del sistema de jobs usa además `environment_incarnation_id`/epoch según contrato 08; no confundir ambos IDs.

`effective_fingerprint`: SHA256 de manifest canónico **no secreto**: source commit/Git blob hashes, contratos/schema/Skills, SDK+CLI pair, modelo/proveedor declarado y capabilities, superficie/plan observado, tools habilitadas, policy/config IDs y versiones efectivas, imagen/proceso/token-policy y domains configurados, grants aprobados y mecanismo de aislamiento. Incluye hashes de documentos/config sanitizada, nunca contenido ni hashes de credentials/auth/broker secrets. Bindings SID/path concretos permanecen locales; el reporte portable publica IDs de policy y digest del manifest sanitizado, no valores privados. Diferencias de EOL del checkout se distinguen del Git blob.

Manifest declara `canonicalization_version`. Propuesta RC1 `canonical-json-v1`: UTF-8, claves ordenadas, sin whitespace extra, sin NaN/Infinity, tipos definidos, sin coerción numérica; listas preservan orden salvo conjuntos cuya especificación exige ordenar. No mezclar hashes de worktree/Git blob. Verifier final debe fijar vector de bytes de referencia y rechazar versión desconocida; este probe no implementa ni valida todavía canonicalización interoperable.

`gate_phase`: DESIGN / TARGET_ENVIRONMENT_ACCEPTANCE / OPERATIONAL / LIVE. Cada test v0.3 lleva environment kind, instance ID y fingerprint además de version/evidence refs/result. Copiar un PASS desde otro perfil no lo cambia de instancia ni fase. Firmar/sellar y proteger registro/reporte corresponde a C, no al modelo; un hash en archivo modificable por J no autentica evidencia.

## Reglas externas de aceptación

1. Para `PAPER_AGENT_ENVIRONMENT` actual, exigir schema v0.3, entorno TARGET_PAPER_ENVIRONMENT, plan observado Plus y host OWNER_PERSONAL_WINDOWS respaldados por evidencia del target. Perfil v0.2 Team es historia, no target aprobado.
2. Todos los requisitos mandatorios del scope deben tener resultados PASSED y refs; no basta lista tests vacía o schema válido. Toda acción obligatoria debe estar COMPLETED/NOT_APPLICABLE con justificación. DEFERRED/UNKNOWN/NOT_TESTED no son PASS ni FAIL por ausencia de acceso.
3. Cada PASS aplicable debe enlazar al instance/fingerprint actuales, gate phase correcto y fuente/versión/inputs necesarios. Fingerprint distinto → revisión de deltas; no heredar aceptación automáticamente.
4. Reusar método/fixtures conductuales Team como evidencia de diseño sin etiquetarlos target PASS. Host-specific auth/ACL/process/IPC/red/blinding/restores y entitlement/cuotas no se transfieren.
5. Cuota/capacidad y datos variables tienen ventana temporal/observación, no prueba permanente por hash estable. Declara vigencia y revalidación; TTL final depende workload/operación, no inventado aquí.
6. Readiness se calcula por verifier externo/owner review del scope. Un autoinforme/modelo no puede cambiar expected plan, requirement scope, grants, refs ni environment identity. `READY_AGENT_ENVIRONMENT` no levanta implementation lock/DoR ni autoriza PAPER/LIVE.

[B1](probes/r028-instance-binding/README.md), [fuente](probes/r028-instance-binding/binding_probe.py), [resultado original](probes/r028-instance-binding/result-01.json): 16 casos sintéticos PASS, incluidos positivo de subset ficticio y rechazos de falta de binding/cross-instance/fingerprint/fase/legacy transfer/scope sustituido. No prueban autenticidad criptográfica, protección del store, canonicalización interoperable, instancias reales ni readiness del scope completo. No se ejecutó bootstrap Plus.
