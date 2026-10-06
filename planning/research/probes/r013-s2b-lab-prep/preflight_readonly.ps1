$ErrorActionPreference = 'Stop'
$outputPath = Join-Path $PSScriptRoot 'preflight-attempt-01.json'
if (Test-Path -LiteralPath $outputPath) { throw 'Preserve original evidence; use a new attempt source/output.' }
$observed = [ordered]@{
    schema_version = 'r013-s2b-preflight-v1'
    captured_at = [DateTime]::UtcNow.ToString('o')
    source_sha256 = (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant()
    source_commit_base = 'b0d6818d057a024bd6fbc2573a8d9bd06c254353'
    configuration_changes = @()
    account_name = 'tos_probe_runner_b'
    account_name_available = 'UNKNOWN'
    account_query_error = $null
    fixture_root = 'C:\ProgramData\TradingOS-S2B-Probe\trial-01'
    fixture_root_exists = 'UNKNOWN'
    fixture_parent_exists = 'UNKNOWN'
    programdata_reparse = 'UNKNOWN'
    filesystem_security_acceptance = 'NOT_TESTED'
    administrator_authority = 'NOT_ESTABLISHED_BY_THIS_READONLY_PROBE'
}
try {
    $null = Get-LocalUser -Name 'tos_probe_runner_b' -ErrorAction Stop
    $observed.account_name_available = $false
} catch {
    if ($_.CategoryInfo.Category -eq 'ObjectNotFound') { $observed.account_name_available = $true }
    else { $observed.account_query_error = $_.CategoryInfo.Category.ToString() }
}
try {
    $observed.fixture_root_exists = Test-Path -LiteralPath 'C:\ProgramData\TradingOS-S2B-Probe\trial-01'
    $observed.fixture_parent_exists = Test-Path -LiteralPath 'C:\ProgramData\TradingOS-S2B-Probe'
    $programdataMetadata = Get-Item -LiteralPath 'C:\ProgramData' -Force
    $observed.programdata_reparse = (($programdataMetadata.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)
} catch { $observed.path_query_error = $_.CategoryInfo.Category.ToString() }
$observed.builtin_powershell_path = (Get-Command powershell.exe).Source
$observed.installed_python_path = (Get-Command python).Source
$observed.tool_access_for_new_runner = 'NOT_TESTED'
$observed | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $outputPath -Encoding utf8
$observed | ConvertTo-Json -Depth 5
