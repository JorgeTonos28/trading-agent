# AST + descriptor construction in memory. Never invokes helper or native FS code.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$ownerPath = Join-Path $PSScriptRoot 'owner_lab.ps1'
$tokens = $null; $errors = $null
$ownerAst = [Management.Automation.Language.Parser]::ParseFile($ownerPath,[ref]$tokens,[ref]$errors)
if ($errors.Count) { throw 'Owner helper parser error.' }
$policy = Get-Content -LiteralPath (Join-Path $PSScriptRoot '..\r013-s2b-lab-prep\lab-policy-plan.json') -Raw | ConvertFrom-Json
$bindings = @{}
foreach ($key in @('BASE','OPERATOR','JOB_SHADOW','JOB_PEDAGOGY')) { $bindings[$key] = [string]$policy.sample_bindings.$key }
foreach ($name in @('Get-Sddl','New-Security')) {
    $function = $ownerAst.FindAll({ param($n) $n -is [Management.Automation.Language.FunctionDefinitionAst] },$true) | Where-Object {$_.Name -eq $name}
    if (@($function).Count -ne 1) { throw 'Unexpected function set.' }
    . ([scriptblock]::Create($function.Extent.Text))
}
$count = 0
foreach ($resource in @($policy.bootstrap_parents) + @($policy.resources)) {
    $sddl = Get-Sddl $resource $resource.kind
    $sec = New-Security $sddl $resource.kind
    $raw = New-Object Security.AccessControl.RawSecurityDescriptor($sec.GetSecurityDescriptorSddlForm([Security.AccessControl.AccessControlSections]::All))
    if (-not ($raw.ControlFlags -band [Security.AccessControl.ControlFlags]::DiscretionaryAclProtected) -or
        $raw.Owner.Value -ne 'S-1-5-32-544') { throw 'Synthetic descriptor differs from policy.' }
    $count += 1
}
[ordered]@{ mode='AST_AND_DESCRIPTOR_MEMORY_ONLY'; helper_parser='PASS'; synthetic_descriptors=$count;
    synthetic_descriptor_validation='PASS'; helper_sha256=(Get-FileHash -LiteralPath $ownerPath -Algorithm SHA256).Hash.ToLowerInvariant();
    actual_fs_tests_executed=$false; administrative_helper_executed=$false; configuration_changes=@(); actual_security_acceptance='NOT_TESTED' } | ConvertTo-Json
