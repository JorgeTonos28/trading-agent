# Read-only metadata. No password/token/auth files, ACL changes or account changes.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$accountName = 'tos_probe_runner_b'
$account = @(Get-LocalUser -ErrorAction Stop | Where-Object { $_.Name -eq $accountName })
$wid = [Security.Principal.WindowsIdentity]::GetCurrent()
$wp = New-Object Security.Principal.WindowsPrincipal($wid)
$parent = 'C:\ProgramData\TradingOS-S2B-Probe'
$root = Join-Path $parent 'trial-01'
$accountState = 'ABSENT'
$disabled = $null; $marker = $null
if ($account.Count -eq 1) {
    $accountState = 'PRESENT'; $disabled = -not $account[0].Enabled
    $marker = $account[0].Description -eq 'TOS S2B-ADM-01 s2b-20261006-a6d74b2b'
}
if ($account.Count -gt 1) { throw 'Ambiguous account query; no state conclusion.' }
[ordered]@{
    schema_version='s2b-readonly-preflight-v1'; captured_at=[DateTime]::UtcNow.ToString('o')
    gate='S2B-ADM-01'; transaction_id='s2b-20261006-a6d74b2b'; account_state=$accountState
    account_disabled=$disabled; account_transaction_marker_matches=$marker
    parent_exists=(Test-Path -LiteralPath $parent); root_exists=(Test-Path -LiteralPath $root)
    current_process_elevated=$wp.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    observed_surface='CURRENT_OPERATOR_SESSION_NOT_RUNNER'
    configuration_changes=@(); filesystem_tests_executed=$false; actual_security_acceptance='NOT_TESTED'
} | ConvertTo-Json
