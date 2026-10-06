# R-013 — prueba AccessCheck en memoria, 2026-10-06

Experimento desechable Python stdlib/ctypes Windows, **no Trading OS ni launcher**. Base de investigación `46cc4a5889747ddfec9731200283f1a94d2b77bd`, Team/desarrollo; no cuenta Runner ni setup privilegiado. [Comparativa](../../R-013_S2_variants_comparison_2026-10-06.md).

## Alcance real y resultados

| Intento | Fuente preservada | Resultado | Hash SHA256 de bytes usados |
|---|---|---|---|
| 01 | accesscheck_attempt01_source.py | ERROR WinError5: handle duplicado no conserva TOKEN_DUPLICATE para CreateRestrictedToken | 50e0b41b114499dc3ca8c9eab5433d7a3935b99c0f93f37028c0a8b32147b063 |
| 02 | accesscheck_probe.py | PASS_SEMANTIC_SCOPE_ONLY, 10/10 | 7b707c5135af1af1fd59165e1c87bc9e9ff07ad954a3bc267fab2ed4b9bebe1d |
| Owner 01 | owner_accesscheck_probe.py | 27 observaciones focales de derechos estándar; vuelve a ejecutar los 10 checks base, sin sumarlos como evidencia independiente | 0a2e8db519c803190c9ea9b180640cb5921e5793257c493ed26d55991ebd80a4 |

Se lee el token del proceso actual con TOKEN_QUERY/TOKEN_DUPLICATE. Se crean handles de tokens restringidos con `DISABLE_MAX_PRIVILEGE` y un restricting SID sintético diferente por vista; el TokenUser sigue siendo el mismo. Se duplica a token de impersonation solo para `AccessCheck`; nunca se impersona el proceso ni se lanza un child. Descriptores DACL sintéticos se evalúan en memoria; no se asignan a archivos, procesos, registry, IPC o red. Restriction SIDs arbitrarios en memoria no crean cuentas/grupos ni perfiles.

Token ordinario permite ambas vistas sintéticas, cada token restringido permite la propia y deniega la ajena. Ambos deniegan descriptor `financial_canary` con otro restricting SID: **no** demuestra protección del core o identidad financiera real. SID real se usa internamente para comparación, no se guarda ni imprime. No secretos/credenciales consultados. No modelo/API/coste adicional. Se cierran handles y liberan memoria; configuration_changes=[] en JSON.

El nombre `financial_canary` se conserva en el JSON original, pero es un control **ungranted object**: el descriptor solo concede a un SID sintético ausente de los tokens, sin positivo autorizado ni diferencial probado frente al token base. Sus dos denials no sustentan reducción de acceso financiero. La evidencia comparativa útil son los accesos positivos propios y denegación cruzada de las dos vistas con el mismo TokenUser. El probe tampoco pide derechos de owner/WRITE_DAC: no prueba protección del supervisor.

## Comprobación focal de propietario — mismo scope no administrativo

`owner-accesscheck-attempt-01.json` mantiene TokenUser y los mismos dos restricting SID, cambiando **solo descriptores en memoria y derechos solicitados**. Tres actores × tres políticas owner × READ_CONTROL/WRITE_DAC/WRITE_OWNER = 27 observaciones, no 27 tests operacionales PASS.

| Descriptor / actor | READ_CONTROL | WRITE_DAC | WRITE_OWNER |
|---|---|---|---|
| Owner=usuario base, default / token base | ALLOW | ALLOW | DENY |
| Owner=usuario base, ACE OWNER RIGHTS con máscara cero / token base | DENY | DENY | DENY |
| Owner=usuario base, default / ambos tokens restringidos | DENY | DENY | DENY |
| Owner=usuario base, ACE OWNER RIGHTS cero / ambos restringidos | DENY | DENY | DENY |
| Owner=SYSTEM / los tres tokens | DENY | DENY | DENY |

La fuente usa grants de datos 0x1, sin grants explícitos de esos derechos estándar. Observación coherente con derechos implícitos owner y doble comprobación del token restringido. **No bypass observado bajo los tokens restringidos de este fixture**. No inferir protección de objetos reales: owner/DACL/process token/integrity/IPC/handles de un supervisor real no fueron configurados o ensayados. Mantener VP-03/04. [Owner](https://learn.microsoft.com/en-us/windows/win32/secauthz/owner-of-a-new-object), [OWNER RIGHTS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers).

Este focal deriva de fuente 02 y conserva sus 10 checks como regresión del harness; no contarlos como otras diez observaciones independientes de aislamiento. No genera audit OS, auth ni procesos nuevos.

`AccessCheck` comprueba descriptor/token y no genera audit OS. No prueba Codex/auth, filesystem/proceso/network/IPC reales, bootstrap, performance, lectura cache bajo otro proceso, recovery o blinding operacional. Todos SI/BL/RB/VP NOT_TESTED. [Microsoft AccessCheck](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-accesscheck), [restricted tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/restricted-tokens).

## Reproducción acotada

Leer fuente antes de ejecutar en Windows con Python. La fuente preservada usa `OUT = ...accesscheck-attempt-02.json` y rechaza sobrescribirlo. Para otro intento, crear una copia de experimento, cambiar únicamente OUT a un filename nuevo y ejecutar esa copia con Python; conservar su fuente/hash y resultado nuevos. No reescribir los intentos originales. Crea únicamente un JSON de resultados, además de handles/descriptores transitorios. No usar esta prueba para autorizar launch bajo token, ACL reales, AppContainer profile o setup de usuarios; requieren otro gate. Errores anteriores se preservan.

Los hashes de tabla corresponden a bytes ejecutados locales, no necesariamente a bytes del checkout con conversión EOL. Para transporte/release usar SHA256 del Git blob al commit pinado según política del repositorio; una reejecución debe registrar el hash de sus propios bytes/versiones/resultados. No editar JSON histórico para acomodar hashes tras commit.
