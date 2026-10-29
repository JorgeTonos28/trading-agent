# S2-ADM-01 — primera prueba administrativa propuesta

> **2026-10-06 — DEFERRED / NOT_AUTHORIZED / OWNER_WITHHELD.** El propietario no autoriza esta propuesta y exige comparar S2-A/S2-B/S3 antes del setup. Las tres cuentas/ACL siguientes son una propuesta histórica, no la próxima acción autorizable. [Revisión ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md) y [comparativa](R-013_S2_variants_comparison_2026-10-06.md). No crear usuarios/perfiles ni modificar ACL/firewall. Nueva propuesta concreta solo después de resolver la variante.

2026-10-05. **USER_ACTION_REQUIRED / NO EJECUTADA / NO AUTORIZADA**. Dirección S2 ya aprobada; esta es la configuración concreta que el propietario reservó a un gate adicional. [ADR-012](../decisions/ADR-012-agent-process-isolation-proposed.md), [S2 RC1](../08_S2_isolation_spec_RC1.md), [acceptance](R-013_S2_acceptance_matrix_RC1.md).

## Decisión exacta y motivo

Autorizar un **laboratorio temporal con tres cuentas Windows locales estándar nuevas y ACL únicamente sobre un árbol de canaries nuevo**, para probar que un proceso Shadow no puede leer/escribir el dominio financiero sintético ni el pedagógico. El probe actual bajo la misma identidad puede leer un sibling 'core': cambiar la carpeta no es aislamiento. Sin otra identidad/token y ACL reales no podemos pasar SI-01/02/03/04 ni BL-02. No se solicita otra aprobación de S2 ni permiso para operar PAPER.

## Cambios acotados propuestos

| Cambio | Detalle revisable |
|---|---|
| Cuentas nuevas | `tos_probe_core`, `tos_probe_shadow`, `tos_probe_ped`; locales, distintas, no reutilizar ni alterar cuentas existentes. Si nombre existe, detener y presentar nuevo nombre, nunca reset de cuenta ajena |
| Membresía | Solo grupo estándar Users según política host, sin Administrators, Remote Desktop Users, Backup Operators ni privilegios de servicio/debug/impersonación asignados. No cambios a grupos existentes ni logon rights globales |
| Contraseñas | Propietario/admin usa entrada segura local para contraseñas únicas; jamás chat/Git/argumentos/logs. No passwords hard-coded, `.env`, auth import ni claves broker. Testlauncher usa prompt seguro/OS logon autorizado; no guardar credential en repo |
| Árbol nuevo | `C:\ProgramData\TradingOS-S2-Probe\trial-01\` (si existe, no reutilizar a ciegas). Solo fixture sintética, binarios/scripts públicos necesarios y resultados sanitizados |
| ACL raíz y padres del árbol nuevo | Administrators/SYSTEM control y propiedad; sin herencia de Users/Everyone/Authenticated Users con permisos amplios. Tres SIDs solo traversal mínimo donde sea necesario; nada sobre repo, perfiles personales, Windows o carpetas existentes fuera de esta raíz |
| `core/` | Cuenta core lectura/escritura de canary; Shadow/Ped sin acceso; parent protegido impide reemplazo de core por DeleteChild |
| `shadow/export/` | Cuenta Shadow R, operador/admin crea/sella; otros usuarios de prueba sin acceso. Contexto ficticio predecisión sin Champion |
| `shadow/scratch-output/` | Cuenta Shadow RW limitado al directorio; sin modificar ACL de exports/root ni evidencia sellada |
| `ped/` | Cuenta Ped R a canary Champion-contemporary ficticia; Shadow/Core sin acceso, operador controla fixture |
| `code/` / `trusted-evidence/` | Code R/X para procesos test, archivos/config no writable por cuentas de prueba; evidence controlada por operador, sin grants job write |
| Lanzamiento | Procesos cortos bajo cada cuenta con token estándar mediante login/launch oficial Windows; no service/task instalado, sin Team login ni inferencia. Ejecución bajo usuario operador no sustituye ese test |

La ACL final se expresa por SID resuelto en esa instancia y se revisa antes de aplicar; bindings/SDDL quedan en reporte local protegido con versión y digest sanitizado en Git. Ningún `FullControl/WRITE_DAC/WRITE_OWNER` para cuentas de prueba sobre objetos protegidos. No assume que 'Users' es inocuo: medir grants efectivos y grupos reales de token. La configuración derivada se documenta desde repositorio, no conocimiento del chat.

## Pruebas de este gate y límite de evidencia

1. Positivos: Core accede canary propia, Ped lee propia, Shadow lee export y escribe output; operador lee evidencia. Sin positivos válidos no PASS de negativos.
2. Negativos bajo SIDs reales: Shadow lee/escribe core/ped, Ped lee Shadow, jobs modifican code/export/receipt/ACL; intentar acceso a archivo presente y registrar error OS específico. No usar secrets reales.
3. Separación entre export readonly y output writable, intento de replace/delete desde padre y replay tras relanzar; token/groups/privileges e identidad parent/child registrados sin valores credenciales.
4. Blinding: canary Champion existe/accesible a Ped; Shadow no la lee antes/después de producir propuesta sintética. Esto prueba namespace blinding; DAG/semantic contamination/native Codex siguen gates aparte.
5. Auditoría del laboratorio: observador confiable conserva comando/operación/error/clock y resultado; cuentas prueba no modifican receipt. **No habilita SACL/auditpol/global logging**. Audit OS completo pendiente ADM-02.

No red/IPC endpoint/servicio instalado; ningún broker, runtime financiero, Codex login o API pagada. No modificar firewall/GPO/local merge/default profiles, secrets, permisos de cuenta de desarrollo ni baseline main. Egress, process-memory IPC, launch autónomo/control, auth native Team, cuota y runtime real permanecen NOT_TESTED. Es un subconjunto de viabilidad S2, no aceptación final.

## Secuencia, rollback y condiciones de parada

- Primero verificar autorización y capacidad admin legítima. El preflight actual no está elevado; **no intentar UAC ni setup automático** antes de respuesta. Admin puede ser propietario u operador autorizado del host; no suponer que este es un host administrado personalmente.
- Presentar script/config con diff de cuentas/SID/ACL y hashes de fixtures antes de ejecutar; instrucciones reproducibles derivan de este gate. Si sistema requiere cambio adicional de logon policy/privilegios, **detener**, no ampliar el permiso.
- Crear y aplicar únicamente recursos nuevos autorizados; ejecutar controles/negativos y guardar errores reales. Un FAIL no provoca VM ni fallback operativo.
- Terminar procesos propios y deshabilitar las tres cuentas de prueba al terminar; preservar resultados sanitizados. Eliminación final de cuentas/perfiles o árbol se propone separadamente con paths/SIDs verificados; sin recursive delete por nombre/patrón ni afectar cuenta existente. No modificar directorios con reparse hacia fuera.
- Para reapertura/reintento verificar mismos SIDs/recursos y nueva evidencia; no reset/cambiar passwords desde agente ni borrar FAIL. Si owner prefiere realizar el setup manualmente, onboarding verifica estado observado antes del test.

## Gates posteriores separados

**ADM-02**: propuesta específica de IPC/process handles, audit y egress tras esclarecer policy store competente; incluye scope/rollback. `AllowLocalFirewallRules=False` hace insuficiente prometer reglas locales. No autorizar aquí cambios globales/enterprise policy. Nunca 'block-all explícito + allow OpenAI' como si allow ganara sobre block.

**ADM-03**: login native Codex Team legítimo en dominios de prueba/seleccionados y smoke SDK/app-server bajo permisos probados, sin copiar auth de desarrollo; owner account action separada. ADM-01 no da acceso al plan ni obliga a nuevas suscripciones.

**HUMAN_ACTION_REQUIRED:** aprobar o rechazar **solo el laboratorio S2-ADM-01** (tres cuentas estándar + ACL en raíz nueva + procesos/tests sintéticos + deshabilitar cuentas al terminar), o indicar quién realizará ese setup. Es necesario por la reserva administrativa explícita del propietario en ADR-012 y AGENTS. D-027/D-024 siguen abiertos.

### Checklist previo a aplicación

Antes de crear/aplicar, presentar y revisar script/ACL concreta por SID con scope exacto, inventario de objetos, propietario, rights y rollback. Esta autorización solicitada cubre únicamente cambios definidos arriba; scripts posteriores no pueden ampliarlos. Perfil/cache/TEMP propios deben mapearse para el posterior test de persistencia; ADM-01 no autoriza modificar ACL global de perfiles ni auth. Si se requiere esa mutación adicional, presentar otro gate. Un PASS de canaries ACL no satisface SI-16/BL-06 persistencia ni egress.
