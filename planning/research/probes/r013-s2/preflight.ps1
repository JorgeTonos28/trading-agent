# Read-only, sanitized inventory. No account, ACL, firewall or audit policy changes.
$ErrorActionPreference = 'Stop'
$taskResult = [ordered]@{
    schema_version = 'r013-preflight-v1'
    observed_at = [DateTime]::UtcNow.ToString('o')
    environment = 'CURRENT_RESEARCH_ENVIRONMENT_TEAM'
    configuration_changes = @()
    limitations = @('Current developer identity only; not S2 acceptance', 'No credential paths/values inspected', 'No system policies modified')
}
$taskIdentity = [Security.Principal.WindowsIdentity]::GetCurrent()
$taskPrincipal = [Security.Principal.WindowsPrincipal]::new($taskIdentity)
$taskResult.token = [ordered]@{
    authenticated = $taskIdentity.IsAuthenticated
    elevated_admin_role = $taskPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    group_count = $taskIdentity.Groups.Count
    own_account_name_recorded = $false
    own_sid_recorded = $false
}
$taskResult.os = Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture
$taskResult.commands = @('Get-LocalUser','New-LocalUser','Get-Acl','Set-Acl','Get-NetFirewallProfile','Get-NetFirewallRule','Get-NetFirewallSecurityFilter','New-NetFirewallRule','Get-WinEvent','Get-NetTCPConnection') | ForEach-Object {
    $taskCommand = Get-Command $_ -ErrorAction SilentlyContinue
    [ordered]@{name=$_; available=($null -ne $taskCommand)}
}
try {
    $taskResult.firewall_services = Get-Service BFE,MpsSvc | Select-Object Name,Status
    $taskResult.firewall_profiles = Get-NetFirewallProfile -PolicyStore ActiveStore | Select-Object Name,Enabled,DefaultInboundAction,DefaultOutboundAction,AllowLocalFirewallRules,LogBlocked,LogAllowed
    $taskResult.firewall_read_status = 'OBSERVED_READ_ONLY'
} catch {
    $taskResult.firewall_read_status = 'UNKNOWN_READ_FAILED'
    $taskResult.firewall_read_error_type = $_.Exception.GetType().Name
}
$taskRepo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../../../..')).Path
$taskAcl = Get-Acl -LiteralPath $taskRepo
$taskResult.repo_acl = [ordered]@{
    inheritance_protected = $taskAcl.AreAccessRulesProtected
    ace_count = $taskAcl.Access.Count
    inherited_ace_count = @($taskAcl.Access | Where-Object IsInherited).Count
    full_control_ace_count = @($taskAcl.Access | Where-Object {($_.FileSystemRights -band [Security.AccessControl.FileSystemRights]::FullControl) -eq [Security.AccessControl.FileSystemRights]::FullControl}).Count
    actual_principals_recorded = $false
    security_acceptance = 'NOT_TESTED'
}
$taskDestination = Join-Path $PSScriptRoot 'preflight-attempt-01.json'
if (Test-Path -LiteralPath $taskDestination) { throw 'Evidence exists; choose a new attempt filename instead of overwriting.' }
$taskResult | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $taskDestination -Encoding utf8
Write-Output ($taskResult | ConvertTo-Json -Depth 8)
