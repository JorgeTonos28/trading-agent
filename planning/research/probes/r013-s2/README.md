# R-013 S2 — probes de preparación

Fixtures sintéticas sin secretos, cuentas/ACL/firewall/políticas nuevas, servicios, login o modelo. No módulos productivos de seguridad. [Hallazgos](../../R-013_S2_findings_2026-10-05.md), [contrato](../../../08_S2_isolation_spec_RC1.md), [acceptance](../../R-013_S2_acceptance_matrix_RC1.md).

Ejecutados desde raíz repo en PowerShell/Python stdlib:

```powershell
& planning/research/probes/r013-s2/preflight.ps1
python planning/research/probes/r013-s2/non_admin_probe.py
```

Primera evidencia existente se preserva. Para repetir, cambiar destino a `attempt-02` o mayor y registrar versión/source commit, nunca overwriting de original. Preflight inspecciona metadata sanitizada del token/SO/comandos/firewall/permisos raíz repo, no paths de secrets ni auth; usa solamente cmdlets Get. `.json` enum string clarification documenta el segundo read-only query, conservando primer dump numérico.

7 checks esperados incluyen **accesos/leaks permitidos deliberados como counterexample**, no 7 denegaciones OS. `S2_SECURITY=NOT_TESTED`, blinding OS NOT_TESTED. Egress/IPC/Team login/canary cross-identity no ejecutados. No leer broker credential real para 'ver si funciona'. No interpretar cambios al código probe como permisos administrativos.

El gate siguiente ADM-01 requiere autorización humana y operador administrativo: no existe script auto-setup habilitado por este README.

## Corrección v2 del probe env

`non_admin_probe_attempt01_source.py` preserva código ejecutado originalmente; **no ejecutarlo**: os.environ.copy() propagó env real no inspeccionada al child. No imprimió esos valores, pero su ausencia de credenciales no está probada. Attempt-02 y su fuente congelada son reparación parcial: NA-01/Git aún heredaron env real por default. `non_admin_probe.py` activo **attempt-03** limita todos los children a OS/task SystemRoot/WINDIR/TEMP/TMP + canary cuando corresponde, Git solo OS; digests dejan trazabilidad. Counterexamples/resultado S2 NOT_TESTED permanecen. Siguientes intentos deben usar nombres nuevos y mínimo env explícito.
