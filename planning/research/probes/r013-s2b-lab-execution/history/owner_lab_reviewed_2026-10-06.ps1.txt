#requires -Version 7.0
<# Disposable owner-only S2B-ADM-01 setup/rollback. No password parameters,
credential API, user creation, process launch, policy/firewall/auth changes.
Agent may read/parse/Plan; owner alone executes Setup/Rollback with elevation.
#>
[CmdletBinding()]
param([ValidateSet('Plan','Inspect','Setup','Rollback')][string]$Phase = 'Plan')
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT' -or -not [Environment]::Is64BitProcess) {
    throw 'Use existing 64-bit PowerShell 7 on Windows; no installation or policy changes.'
}
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..\..'))
$authFile = Join-Path $PSScriptRoot 'authorization.json'
$auth = Get-Content -LiteralPath $authFile -Raw | ConvertFrom-Json
$labRoot = 'C:\ProgramData\TradingOS-S2B-Probe\trial-01'
$labParent = 'C:\ProgramData\TradingOS-S2B-Probe'
$accountName = 'tos_probe_runner_b'
if ($auth.gate -ne 'S2B-ADM-01' -or $auth.status -ne 'AUTHORIZED_OWNER_ADMIN_ONLY_NOT_EXECUTED' -or
    $auth.root -ne $labRoot -or $auth.new_parent -ne $labParent -or $auth.account_name -ne $accountName -or
    $auth.agent_administrative_execution_allowed -or $auth.transaction_id -ne 's2b-20261006-a6d74b2b') {
    throw 'Authorization/scope mismatch; no mutation.'
}
$policyFile = Join-Path $repoRoot 'planning\research\probes\r013-s2b-lab-prep\lab-policy-plan.json'
if ((Get-FileHash -LiteralPath $policyFile -Algorithm SHA256).Hash.ToLowerInvariant() -ne
    'ade0ac46b2967c6f2e5e05df3d3d93b41de7e699ed921ffb78beeb636d02d6c7') {
    throw 'Pinned policy bytes differ; review clone EOL/source before apply, never silently repin.'
}
$policy = Get-Content -LiteralPath $policyFile -Raw | ConvertFrom-Json
$fsSource = Join-Path $repoRoot 'planning\research\probes\r013-s2b-lab-prep\filesystem_probe.py'
$fsHash = (Get-FileHash -LiteralPath $fsSource -Algorithm SHA256).Hash.ToLowerInvariant()
if ($fsHash -ne 'ce2a39ad0bfc7ad7cb86fd8e2a78d570bdafc6bd9c5117f37569ca45cf24fb93') {
    throw 'Pinned filesystem source differs; reviewed source required.'
}
if (@($policy.resources).Count -ne 14 -or @($policy.bootstrap_parents).Count -ne 1 -or
    $policy.bootstrap_parents[0].absolute_path -ne $labParent) { throw 'Unexpected resources.' }
$wid = [Security.Principal.WindowsIdentity]::GetCurrent()
$operatorSid = $wid.User.Value
$principal = New-Object Security.Principal.WindowsPrincipal($wid)
$elevated = $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if ($Phase -in @('Setup','Rollback') -and -not $elevated) { throw 'OWNER_ACTION_REQUIRED: elevated owner session only.' }

function Assert-PlainPath([string]$Path, [switch]$New) {
    $full = [IO.Path]::GetFullPath($Path)
    if ($full -ne $labParent -and $full -ne $labRoot -and
        -not $full.StartsWith($labRoot + '\',[StringComparison]::OrdinalIgnoreCase)) {
        throw 'Target outside exact authorized parent/tree.'
    }
    $cursor = $full
    while ($cursor) {
        if (Test-Path -LiteralPath $cursor) {
            $item = Get-Item -LiteralPath $cursor -Force
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Reparse detected; no mutation.' }
            if ([IO.Path]::GetFullPath($item.FullName) -ne $cursor) { throw 'Path alias drift.' }
        }
        $next = [IO.Path]::GetDirectoryName($cursor)
        if ($next -eq $cursor) { break }
        $cursor = $next
    }
    if ($New -and (Test-Path -LiteralPath $full)) { throw 'Existing resource; do not reuse or overwrite.' }
    return $full
}
function Get-NewAccount {
    $u = Get-LocalUser -Name $accountName -ErrorAction Stop
    if ($u.Description -ne $auth.account_description -or $u.Name -ne $accountName -or
        $u.SID.Value -eq $operatorSid -or $u.Enabled) {
        throw 'Account must be transaction-tagged, disabled and different from operator.'
    }
    $memberships = @()
    foreach ($g in @(Get-LocalGroup -ErrorAction Stop)) {
        # Inspect membership only; never change any group or existing account.
        $found = @(Get-LocalGroupMember -SID $g.SID -ErrorAction Stop | Where-Object { $_.SID.Value -eq $u.SID.Value })
        if ($found.Count) { $memberships += $g.SID.Value }
    }
    if ($memberships.Count -ne 1 -or $memberships[0] -ne 'S-1-5-32-545') {
        throw 'Membership unknown/nonstandard: only Users permitted; no automatic repairs.'
    }
    return $u
}
function Get-Sddl($Resource, [string]$Kind) {
    $aces = @()
    foreach ($g in @($policy.common_protected_control) + @($Resource.extra_allow)) {
        $key = [string]$g.principal
        $sid = if ($bindings.ContainsKey($key)) { $bindings[$key] } else { $key }
        if ($key -notin @('BASE','OPERATOR','JOB_SHADOW','JOB_PEDAGOGY','SY','BA')) { throw 'Principal not allowlisted.' }
        $mask = [uint32]$policy.rights_masks.($g.rights)
        if ($key -in @('BASE','JOB_SHADOW','JOB_PEDAGOGY') -and ($mask -band 0xC0000)) { throw 'Role control rights forbidden.' }
        $flags = if ($Kind -eq 'directory') { [string]$g.inherit } else { '' }
        if ($flags -notin @('','OICI')) { throw 'Unexpected inheritance.' }
        $aces += ('(A;{0};0x{1:x};;;{2})' -f $flags,$mask,$sid)
    }
    return 'O:BAG:BAD:P' + ($aces -join '') + '(A;;0x0;;;OW)'
}
function New-Security([string]$Sddl,[string]$Kind) {
    $type = if ($Kind -eq 'directory') { 'System.Security.AccessControl.DirectorySecurity' } else { 'System.Security.AccessControl.FileSecurity' }
    $sec = New-Object $type
    $sections = [Security.AccessControl.AccessControlSections]::Access -bor
        [Security.AccessControl.AccessControlSections]::Owner -bor [Security.AccessControl.AccessControlSections]::Group
    $sec.SetSecurityDescriptorSddlForm($Sddl,$sections)
    return $sec
}
function Initialize-DirectoryApi {
    # Windows API reused for create-new semantics: existing directory fails rather
    # than the idempotent DirectoryInfo.Create route. Owner process only, no driver.
    if (-not ('TOS_S2B_ADM01_Native' -as [type])) {
        Add-Type -TypeDefinition @'
using System;
using System.IO;
using System.ComponentModel;
using System.Runtime.InteropServices;
using Microsoft.Win32.SafeHandles;
public static class TOS_S2B_ADM01_Native {
 [StructLayout(LayoutKind.Sequential)] public struct SA { public int Length; public IntPtr SD; [MarshalAs(UnmanagedType.Bool)] public bool Inherit; }
 [DllImport("advapi32.dll", CharSet=CharSet.Unicode, SetLastError=true)] [return:MarshalAs(UnmanagedType.Bool)]
 public static extern bool ConvertStringSecurityDescriptorToSecurityDescriptor(string s,int revision,out IntPtr sd,out int length);
 [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)] [return:MarshalAs(UnmanagedType.Bool)]
 public static extern bool CreateDirectory(string path,ref SA attributes);
 [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
 public static extern SafeFileHandle CreateFile(string path,uint access,uint share,ref SA attributes,uint disposition,uint flags,IntPtr template);
 [DllImport("kernel32.dll")] public static extern IntPtr LocalFree(IntPtr p);
 public static void NewFile(string path,string sddl,byte[] bytes) {
   IntPtr sd = IntPtr.Zero; int length;
   if (!ConvertStringSecurityDescriptorToSecurityDescriptor(sddl,1,out sd,out length))
     throw new Win32Exception(Marshal.GetLastWin32Error());
   try {
     SA sa = new SA {Length=Marshal.SizeOf<SA>(),SD=sd,Inherit=false};
     using (SafeFileHandle handle = CreateFile(path,0x40000000,0,ref sa,1,0x80,IntPtr.Zero)) {
       if (handle.IsInvalid) throw new Win32Exception(Marshal.GetLastWin32Error());
       using (FileStream output = new FileStream(handle,FileAccess.Write)) {
         output.Write(bytes,0,bytes.Length); output.Flush(true);
       }
     }
   } finally { LocalFree(sd); }
 }
}
'@
    }
}
function New-DirectoryAtomic([string]$Path,[string]$Sddl) {
    $ptr = [IntPtr]::Zero; $length = 0
    if (-not [TOS_S2B_ADM01_Native]::ConvertStringSecurityDescriptorToSecurityDescriptor($Sddl,1,[ref]$ptr,[ref]$length)) {
        throw 'Descriptor conversion failed before create.'
    }
    try {
        $sa = New-Object TOS_S2B_ADM01_Native+SA
        $sa.Length = [Runtime.InteropServices.Marshal]::SizeOf($sa)
        $sa.SD = $ptr; $sa.Inherit = $false
        if (-not [TOS_S2B_ADM01_Native]::CreateDirectory($Path,[ref]$sa)) {
            $err = [Runtime.InteropServices.Marshal]::GetLastWin32Error()
            throw ('Create-new directory failed, Windows error {0}; no reuse or ACL repair.' -f $err)
        }
    } finally { $null = [TOS_S2B_ADM01_Native]::LocalFree($ptr) }
}
function Assert-Policy([string]$Path,[string]$Sddl) {
    $actualAcl = Get-Acl -LiteralPath $Path
    $actual = New-Object Security.AccessControl.RawSecurityDescriptor($actualAcl.Sddl)
    $expected = New-Object Security.AccessControl.RawSecurityDescriptor($Sddl)
    if ($actual.Owner.Value -ne $expected.Owner.Value -or $actual.Group.Value -ne $expected.Group.Value -or
        -not ($actual.ControlFlags -band [Security.AccessControl.ControlFlags]::DiscretionaryAclProtected)) { throw 'Owner/group/protection mismatch.' }
    $aa = @($actual.DiscretionaryAcl | ForEach-Object { '{0}|{1}|{2}|{3}' -f $_.AceType,[int]$_.AceFlags,$_.AccessMask,$_.SecurityIdentifier.Value } | Sort-Object)
    $ee = @($expected.DiscretionaryAcl | ForEach-Object { '{0}|{1}|{2}|{3}' -f $_.AceType,[int]$_.AceFlags,$_.AccessMask,$_.SecurityIdentifier.Value } | Sort-Object)
    if (@(Compare-Object $aa $ee).Count) { throw 'Effective DACL differs from exact plan.' }
}
$account = Get-NewAccount
$bindings = @{
    BASE = $account.SID.Value
    OPERATOR = $operatorSid
    JOB_SHADOW = $policy.sample_bindings.JOB_SHADOW
    JOB_PEDAGOGY = $policy.sample_bindings.JOB_PEDAGOGY
}
if (@($bindings.Values | Select-Object -Unique).Count -ne 4) { throw 'Binding collision.' }
$targets = @([pscustomobject]@{ Path=$labParent; Kind='directory'; Resource=$policy.bootstrap_parents[0] })
foreach ($res in $policy.resources) {
    $rel = [string]$res.relative_path
    if ($rel -match '(^[/\\]|(^|[/\\])\.\.([/\\]|$)|:)') { throw 'Unsafe policy path.' }
    $target = if ($rel -eq '') { $labRoot } else { Join-Path $labRoot $rel }
    $targets += [pscustomobject]@{ Path=$target; Kind=$res.kind; Resource=$res }
}
if ($Phase -eq 'Plan') {
    foreach ($t in $targets) {
        $null = Assert-PlainPath $t.Path -New
        $null = New-Security (Get-Sddl $t.Resource $t.Kind) $t.Kind
    }
    [ordered]@{ gate=$auth.gate; transaction_id=$auth.transaction_id; phase='PLAN_ONLY'; account_disabled=$true; standard_membership_verified=$true; resource_count=$targets.Count; pinned_filesystem_sha256=$fsHash; elevated=$elevated; configuration_changes=@(); acceptance='NOT_TESTED' } | ConvertTo-Json
    exit 0
}

$ledgerPath = Join-Path $labRoot 'trusted-evidence\ledger-local.json'
$controlFileResource = [pscustomobject]@{ extra_allow=@() }
$controlSddl = Get-Sddl $controlFileResource 'file'
$journalPath = Join-Path $PSScriptRoot 'owner-transaction-local.jsonl'
function Get-TextHash([string]$Text) {
    $sha = [Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($Text)))).Replace('-','').ToLowerInvariant() }
    finally { $sha.Dispose() }
}
function Assert-RepositoryPath([string]$Path) {
    $full = [IO.Path]::GetFullPath($Path)
    if (-not $full.StartsWith($repoRoot + '\',[StringComparison]::OrdinalIgnoreCase)) { throw 'Evidence path outside repository.' }
    $cursor = $full
    while ($cursor) {
        if (Test-Path -LiteralPath $cursor) {
            $item = Get-Item -LiteralPath $cursor -Force
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw 'Evidence path reparse; stop.' }
        }
        $next = [IO.Path]::GetDirectoryName($cursor)
        if ($next -eq $cursor) { break }; $cursor = $next
    }
    return $full
}
function Write-Journal([string]$Event,[string]$Path='', [string]$Kind='', [string]$Sddl='') {
    # Sanitized repository evidence only: no account SID, secret, ACL mutation or
    # configuration outside the approved OS tree. INTENT is flushed BEFORE create.
    $null = Assert-RepositoryPath $journalPath
    $script:sequence += 1
    $entry = [ordered]@{ sequence=$script:sequence; gate=$auth.gate; transaction_id=$auth.transaction_id;
        at=[DateTime]::UtcNow.ToString('o'); event=$Event; path=$Path; kind=$Kind;
        descriptor_sha256=(Get-TextHash $Sddl); base_sid_fingerprint=(Get-TextHash $bindings.BASE);
        operator_sid_fingerprint=(Get-TextHash $operatorSid); helper_sha256=(Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant();
        policy_sha256=(Get-FileHash -LiteralPath $policyFile -Algorithm SHA256).Hash.ToLowerInvariant();
        original_parent_absent=$true; original_root_absent=$true; raw_sids_in_journal=$false }
    $bytes = [Text.Encoding]::UTF8.GetBytes(($entry | ConvertTo-Json -Compress) + [Environment]::NewLine)
    $mode = if ($script:sequence -eq 1) { [IO.FileMode]::CreateNew } else { [IO.FileMode]::Append }
    $out = New-Object IO.FileStream($journalPath,$mode,[IO.FileAccess]::Write,[IO.FileShare]::Read)
    try { $out.Write($bytes,0,$bytes.Length); $out.Flush($true) } finally { $out.Dispose() }
}
function Assert-Journal {
    $null = Assert-RepositoryPath $journalPath
    $rows = @(Get-Content -LiteralPath $journalPath | ForEach-Object { $_ | ConvertFrom-Json })
    if (-not $rows.Count -or $rows[0].event -ne 'SETUP_BEGIN' -or $rows[0].sequence -ne 1) { throw 'Missing durable transaction header; no rollback.' }
    $number = 0
    foreach ($r in $rows) {
        $number += 1
        if ($r.sequence -ne $number -or $r.gate -ne $auth.gate -or $r.transaction_id -ne $auth.transaction_id -or
            $r.base_sid_fingerprint -ne (Get-TextHash $bindings.BASE) -or
            $r.operator_sid_fingerprint -ne (Get-TextHash $operatorSid) -or
            -not $r.original_parent_absent -or -not $r.original_root_absent -or
            $r.helper_sha256 -ne (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant()) { throw 'Journal identity/source/sequence mismatch; no rollback.' }
    }
    return $rows
}
if ($Phase -eq 'Inspect') {
    $rows = @(Assert-Journal)
    if (@($rows | Where-Object { $_.event -eq 'SETUP_COMPLETE' }).Count -ne 1) { throw 'Setup incomplete: collect journal and reconcile; no Runner launch.' }
    foreach ($t in $targets) {
        $null = Assert-PlainPath $t.Path
        Assert-Policy $t.Path (Get-Sddl $t.Resource $t.Kind)
    }
    Assert-Policy $ledgerPath $controlSddl
    $localLedger = Get-Content -LiteralPath $ledgerPath -Raw | ConvertFrom-Json
    if ($localLedger.account_sid -ne $account.SID.Value -or $localLedger.operator_sid -ne $operatorSid -or
        $localLedger.transaction_id -ne $auth.transaction_id -or
        $localLedger.status -ne 'SETUP_COMPLETE_ACCOUNT_DISABLED_NO_FS_ACCEPTANCE' -or
        $localLedger.source_sha256 -ne $fsHash -or @($localLedger.created_resources).Count -ne 18 -or
        $localLedger.helper_source_sha256 -ne (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant()) {
        throw 'Collector SID/ledger/source mismatch; owner action required, never expand ACL.'
    }
    $copySource = Join-Path $labRoot 'code\filesystem_probe.py'
    if ((Get-FileHash -LiteralPath $copySource -Algorithm SHA256).Hash.ToLowerInvariant() -ne $fsHash) { throw 'Lab source drift.' }
    $codeRes = @($policy.resources | Where-Object { $_.relative_path -eq 'code' })[0]
    foreach ($name in @('filesystem_probe.py','local-binding.json')) { Assert-Policy (Join-Path $labRoot ('code\' + $name)) (Get-Sddl $codeRes 'file') }
    $localBinding = Get-Content -LiteralPath (Join-Path $labRoot 'code\local-binding.json') -Raw | ConvertFrom-Json
    if ($localBinding.transaction_id -ne $auth.transaction_id -or $localBinding.bindings.BASE -ne $account.SID.Value -or
        $localBinding.bindings.OPERATOR -ne $operatorSid -or $localBinding.source_sha256 -ne $fsHash) { throw 'Binding mismatch.' }
    [ordered]@{ gate=$auth.gate; transaction_id=$auth.transaction_id; phase='READONLY_SETUP_INSPECTION';
        descriptors_verified=$targets.Count; account_disabled=$true; standard_membership_verified=$true;
        source_sha256=$fsHash; configuration_changes=@(); filesystem_acceptance='NOT_TESTED'; runner_launch_permitted_for_owner_test_only=$true } | ConvertTo-Json
    exit 0
}
function Write-NewFile([string]$Path,[byte[]]$Bytes,[string]$Sddl) {
    $full = Assert-PlainPath $Path -New
    $parentPath = [IO.Path]::GetDirectoryName($full)
    if ($parentPath -notin @($created | Where-Object { $_.kind -eq 'directory' } | ForEach-Object { $_.path })) {
        throw 'Creation parent was not created in this transaction.'
    }
    Write-Journal 'CREATE_INTENT' $full 'file' $Sddl
    # Apply exact SD at CREATE_NEW; no idempotent open or post-create ACL repair.
    # Account disabled, lab quiescent; pending INTENT survives a write failure.
    [TOS_S2B_ADM01_Native]::NewFile($full,$Sddl,$Bytes)
    $created.Add([ordered]@{path=$full;kind='file';sddl=$Sddl})
    Assert-Policy $full $Sddl
    Write-Journal 'CREATE_VERIFIED' $full 'file' $Sddl
}
function Save-Ledger {
    $ledger.created_resources = @($created.ToArray())
    if (Test-Path -LiteralPath (Split-Path -Parent $ledgerPath)) {
        $null = Assert-PlainPath $ledgerPath
        $json = $ledger | ConvertTo-Json -Depth 12
        if (-not (Test-Path -LiteralPath $ledgerPath)) {
            Write-NewFile $ledgerPath ([Text.Encoding]::UTF8.GetBytes($json)) $controlSddl
            $ledger.created_resources = @($created.ToArray())
        } else { Assert-Policy $ledgerPath $controlSddl }
        [IO.File]::WriteAllText($ledgerPath,($ledger | ConvertTo-Json -Depth 12),(New-Object Text.UTF8Encoding($false)))
    }
}
if ($Phase -eq 'Setup') {
    foreach ($t in $targets) { $null = Assert-PlainPath $t.Path -New }
    $null = Assert-RepositoryPath $journalPath
    if (Test-Path -LiteralPath $journalPath) { throw 'Transaction journal already exists: reconcile, never blind Setup retry.' }
    $script:sequence = 0
    Write-Journal 'SETUP_BEGIN'
    $created = New-Object 'Collections.Generic.List[object]'
    $ledger = [ordered]@{
        schema_version='s2b-private-ledger-v1'; gate=$auth.gate; transaction_id=$auth.transaction_id
        created_at=[DateTime]::UtcNow.ToString('o'); status='SETUP_IN_PROGRESS'
        account_name=$accountName; account_sid=$account.SID.Value; account_description=$auth.account_description
        operator_sid=$operatorSid; root=$labRoot; new_parent=$labParent
        original_account_absent_baseline=$true; original_parent_absent=$true; original_root_absent=$true
        owner_created_account_in_Windows_UI=$true; account_enabled_by_helper=$false
        source_sha256=$fsHash; policy_sha256=(Get-FileHash $policyFile -Algorithm SHA256).Hash.ToLowerInvariant()
        created_resources=@(); financial_credentials=$false; Team_auth=$false; scope_expansion=$false
        helper_source_sha256=(Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant()
    }
    try {
        Initialize-DirectoryApi
        # Create trusted evidence immediately after root; descriptors unchanged.
        $orderedTargets = @($targets | Where-Object { $_.Path -in @($labParent,$labRoot,(Join-Path $labRoot 'trusted-evidence')) }) +
            @($targets | Where-Object { $_.Path -notin @($labParent,$labRoot,(Join-Path $labRoot 'trusted-evidence')) })
        foreach ($t in $orderedTargets) {
            $sddl = Get-Sddl $t.Resource $t.Kind
            if ($t.Kind -eq 'directory') {
                $full = Assert-PlainPath $t.Path -New
                $parentPath = [IO.Path]::GetDirectoryName($full)
                if ($parentPath -ne 'C:\ProgramData' -and $parentPath -notin @($created | Where-Object { $_.kind -eq 'directory' } | ForEach-Object { $_.path })) { throw 'Missing transaction parent.' }
                Write-Journal 'CREATE_INTENT' $full 'directory' $sddl
                New-DirectoryAtomic $full $sddl
                $created.Add([ordered]@{path=$full;kind='directory';sddl=$sddl})
                Assert-Policy $full $sddl
                Write-Journal 'CREATE_VERIFIED' $full 'directory' $sddl
            } else {
                $payload = [ordered]@{ fixture='SYNTHETIC_NO_SECRET'; transaction_id=$auth.transaction_id; resource=$t.Resource.relative_path; gate=$auth.gate }
                Write-NewFile $t.Path ([Text.Encoding]::UTF8.GetBytes(($payload | ConvertTo-Json -Compress))) $sddl
            }
        }
        Save-Ledger
        $codeResource = @($policy.resources | Where-Object { $_.relative_path -eq 'code' })[0]
        $codeSddl = Get-Sddl $codeResource 'file'
        Write-NewFile (Join-Path $labRoot 'code\filesystem_probe.py') ([IO.File]::ReadAllBytes($fsSource)) $codeSddl
        $binding = [ordered]@{ gate=$auth.gate; owner_approval_reference='OWNER_DIRECT_APPROVAL_2026_10_06_S2B_ADM01'; transaction_id=$auth.transaction_id; root=$labRoot; source_sha256=$fsHash; bindings=$bindings }
        Write-NewFile (Join-Path $labRoot 'code\local-binding.json') ([Text.Encoding]::UTF8.GetBytes(($binding | ConvertTo-Json -Depth 6))) $codeSddl
        $ledger.status = 'SETUP_COMPLETE_ACCOUNT_DISABLED_NO_FS_ACCEPTANCE'
        Save-Ledger
        Write-Journal 'SETUP_COMPLETE'
        [ordered]@{ gate=$auth.gate; transaction_id=$auth.transaction_id; status=$ledger.status; new_resources_created=$created.Count; account_disabled=$true; account_created_by_helper=$false; ledger_protected=$true; actual_security_acceptance='NOT_TESTED' } | ConvertTo-Json
    } catch {
        $ledger.status = 'SETUP_ERROR_ACCOUNT_DISABLED_REVIEW_PARTIAL_LEDGER'
        $ledger.error_type = $_.Exception.GetType().Name
        $ledgerPersistence = 'NOT_AVAILABLE_OR_FAILED'
        try { Save-Ledger; if (Test-Path -LiteralPath $ledgerPath) { $ledgerPersistence = 'PRIVATE_LEDGER_PRESENT_REQUIRES_VERIFY' } }
        catch { $ledgerPersistence = 'PRIVATE_LEDGER_WRITE_ERROR' }
        try { Write-Journal 'SETUP_ERROR' } catch { Write-Warning 'Journal write failed: preserve file and resources; explicit owner reconciliation required.' }
        [ordered]@{ gate=$auth.gate; transaction_id=$auth.transaction_id; status=$ledger.status; error_type=$ledger.error_type; created_paths=@($created | ForEach-Object { $_.path }); partial_resources_require_owner_review=$true; durable_journal_path=$journalPath; private_ledger_status=$ledgerPersistence; automatic_retry_allowed=$false } | ConvertTo-Json -Depth 4
        throw 'Owner setup stopped: preserve partial ledger/resources, no blind retry or scope expansion.'
    }
    exit 0
}

# Rollback: owner only. Journal precedes every mutation and supports partial setup.
$journal = @(Assert-Journal)
$known = @{}
foreach ($t in $targets) { $known[$t.Path] = @{ Kind=$t.Kind; Sddl=(Get-Sddl $t.Resource $t.Kind) } }
$codeResource = @($policy.resources | Where-Object { $_.relative_path -eq 'code' })[0]
$known[$ledgerPath] = @{ Kind='file'; Sddl=$controlSddl }
$known[(Join-Path $labRoot 'code\filesystem_probe.py')] = @{ Kind='file'; Sddl=(Get-Sddl $codeResource 'file') }
$known[(Join-Path $labRoot 'code\local-binding.json')] = @{ Kind='file'; Sddl=(Get-Sddl $codeResource 'file') }
foreach ($r in @($journal | Where-Object { $_.event -eq 'CREATE_INTENT' })) {
    if (-not $known.ContainsKey($r.path) -or $r.kind -ne $known[$r.path].Kind -or
        $r.descriptor_sha256 -ne (Get-TextHash $known[$r.path].Sddl)) { throw 'Journal contains unapproved target; no cleanup.' }
    $null = Assert-PlainPath $r.path
    if (Test-Path -LiteralPath $r.path) { Assert-Policy $r.path $known[$r.path].Sddl }
}
$setupComplete = @($journal | Where-Object { $_.event -eq 'SETUP_COMPLETE' }).Count -eq 1
if ($setupComplete) {
    Assert-Policy $ledgerPath $controlSddl
    $ledger = Get-Content -LiteralPath $ledgerPath -Raw | ConvertFrom-Json
    if ($ledger.transaction_id -ne $auth.transaction_id -or $ledger.gate -ne $auth.gate -or
        $ledger.operator_sid -ne $operatorSid -or $ledger.account_sid -ne $account.SID.Value -or
        $ledger.root -ne $labRoot -or $ledger.new_parent -ne $labParent -or
        $ledger.status -ne 'SETUP_COMPLETE_ACCOUNT_DISABLED_NO_FS_ACCEPTANCE' -or
        $ledger.source_sha256 -ne $fsHash -or
        $ledger.policy_sha256 -ne (Get-FileHash -LiteralPath $policyFile -Algorithm SHA256).Hash.ToLowerInvariant() -or
        $ledger.helper_source_sha256 -ne (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant() -or
        -not $ledger.original_parent_absent -or -not $ledger.original_root_absent -or -not $ledger.original_account_absent_baseline) { throw 'Private ledger mismatch; no cleanup.' }
    if (@($ledger.created_resources).Count -ne $known.Count) { throw 'Private ledger incomplete manifest; no cleanup.' }
    foreach ($path in @($known.Keys)) {
        $entries = @($ledger.created_resources | Where-Object { $_.path -eq $path })
        $events = @($journal | Where-Object { $_.event -eq 'CREATE_VERIFIED' -and $_.path -eq $path })
        if ($entries.Count -ne 1 -or $events.Count -ne 1 -or $entries[0].kind -ne $known[$path].Kind -or
            $entries[0].sddl -ne $known[$path].Sddl -or $events[0].descriptor_sha256 -ne (Get-TextHash $known[$path].Sddl)) {
            throw 'Protected manifest/journal expected resource mismatch; no cleanup.'
        }
        $null = Assert-PlainPath $path
        Assert-Policy $path $known[$path].Sddl
    }
    $receiptPath = Join-Path $labRoot 'trusted-evidence\export-verified.json'
    Assert-Policy $receiptPath $controlSddl
    $export = Get-Content -LiteralPath $receiptPath -Raw | ConvertFrom-Json
    $copyPath = Join-Path $repoRoot ('.local\s2b-execution-private\' + $auth.transaction_id + '\ledger-copy.json')
    $null = Assert-RepositoryPath $copyPath
    if ($export.transaction_id -ne $auth.transaction_id -or $export.gate -ne $auth.gate -or
        -not $export.sanitized_evidence_export_verified -or $export.private_ledger_copy_path -ne $copyPath -or
        -not (Test-Path -LiteralPath $copyPath) -or
        $export.ledger_sha256 -ne (Get-FileHash -LiteralPath $ledgerPath -Algorithm SHA256).Hash.ToLowerInvariant() -or
        $export.ledger_sha256 -ne (Get-FileHash -LiteralPath $copyPath -Algorithm SHA256).Hash.ToLowerInvariant() -or
        $export.ledger_bytes -ne (Get-Item -LiteralPath $copyPath).Length -or
        $export.ledger_bytes -ne (Get-Item -LiteralPath $ledgerPath).Length) { throw 'External ledger copy not verified; no cleanup.' }
    $publicPath = Join-Path $PSScriptRoot 'filesystem-evaluation.json'
    $null = Assert-RepositoryPath $publicPath
    if ($export.sanitized_evidence_path -ne $publicPath -or -not (Test-Path -LiteralPath $publicPath) -or
        $export.sanitized_evidence_sha256 -ne (Get-FileHash -LiteralPath $publicPath -Algorithm SHA256).Hash.ToLowerInvariant()) { throw 'Sanitized evidence export missing/drift; no cleanup.' }
} else {
    # No runner tests permitted before Setup complete. Partial rollback is always
    # blocked by this helper until explicit owner attribution/reconciliation;
    # journal INTENT/VERIFIED alone does not prove who created an object.
    [ordered]@{ gate=$auth.gate; transaction_id=$auth.transaction_id; status='PARTIAL_SETUP_REQUIRES_OWNER_RECONCILIATION';
        journal_retained=$true; no_deletion_performed=$true; filesystem_acceptance='NOT_TESTED' } | ConvertTo-Json
    throw 'OWNER_ACTION_REQUIRED: inspect INTENT/VERIFIED, real SID/marker and exact paths. Journal alone is not deletion authority. Agent prepares exact partial reversal only after owner confirms attribution; no blind cleanup/retry.'
}
$profiles = @(Get-CimInstance Win32_UserProfile -Filter ("SID='{0}'" -f $account.SID.Value))
if ($profiles.Count) { throw 'OWNER_ACTION_REQUIRED: remove only exact new SID unloaded nonspecial profile in Windows UI first; no automatic profile deletion.' }
$active = @(); $unknown = @()
foreach ($p in @(Get-CimInstance Win32_Process -Property ProcessId,Name,CreationDate)) {
    try {
        $owner = Invoke-CimMethod -InputObject $p -MethodName GetOwnerSid -ErrorAction Stop
        if ($owner.ReturnValue -eq 0 -and $owner.Sid) {
            if ($owner.Sid -eq $account.SID.Value) { $active += $p.ProcessId }
        } else { $unknown += [ordered]@{pid=$p.ProcessId; name=$p.Name; created_at=[string]$p.CreationDate; return_code=$owner.ReturnValue} }
    } catch {
        # A process may disappear between enumeration and query. Only its absence
        # resolves that race; errors/denied ownership are never another user.
        $still = @(Get-CimInstance Win32_Process -Filter ('ProcessId={0}' -f $p.ProcessId))
        if ($still.Count) { $unknown += [ordered]@{pid=$p.ProcessId;name=$p.Name;created_at=[string]$p.CreationDate;return_code='QUERY_ERROR'} }
    }
}
if ($active.Count) { throw 'OWNER_ACTION_REQUIRED: close only temporary-account test processes/session; no global kill.' }
if ($unknown.Count) {
    [ordered]@{ gate=$auth.gate; transaction_id=$auth.transaction_id; status='ROLLBACK_BLOCKED_PROCESS_OWNERSHIP_UNKNOWN'; processes=$unknown; no_deletion_performed=$true } | ConvertTo-Json -Depth 5
    throw 'OWNER_ACTION_REQUIRED: verify unknown PIDs/creation times in Windows; do not widen policy or kill system processes. Record evidence and reconcile before a revised, scoped cleanup.'
}
# Validate every descendant without following reparse links before any recursive delete.
$stack = New-Object 'Collections.Generic.Stack[string]'
if (Test-Path -LiteralPath $labRoot) { $stack.Push($labRoot) }
while ($stack.Count) {
    $directory = $stack.Pop(); $null = Assert-PlainPath $directory
    foreach ($entry in @(Get-ChildItem -LiteralPath $directory -Force)) {
        $null = Assert-PlainPath $entry.FullName
        if (-not $setupComplete -and $entry.FullName -notin @($journal | Where-Object { $_.event -eq 'CREATE_INTENT' } | ForEach-Object { $_.path })) { throw 'Foreign partial-setup child; no cleanup.' }
        if ($entry.PSIsContainer) { $stack.Push($entry.FullName) }
    }
}
if (Test-Path -LiteralPath $labRoot) {
$null = Assert-PlainPath $labRoot
if ([IO.Path]::GetFullPath((Get-Item -LiteralPath $labRoot -Force).FullName) -ne $labRoot) { throw 'Rollback root drift.' }
# Exact approved target checked above; account disabled, no active writer, owner lab quiescent.
Remove-Item -LiteralPath $labRoot -Recurse -Force -ErrorAction Stop
}
if (Test-Path -LiteralPath $labParent) {
$null = Assert-PlainPath $labParent
if (@(Get-ChildItem -LiteralPath $labParent -Force).Count) { throw 'Parent not empty: stop, no parent recursive cleanup.' }
Remove-Item -LiteralPath $labParent -Force -ErrorAction Stop
}
# Recheck captured SID/name/marker immediately before removing only this account.
$again = Get-NewAccount
if ((Get-TextHash $again.SID.Value) -ne $journal[0].base_sid_fingerprint) { throw 'Account SID changed; no removal.' }
Remove-LocalUser -SID $again.SID -ErrorAction Stop
[ordered]@{ gate=$auth.gate; transaction_id=$auth.transaction_id; status='ROLLBACK_COMMANDS_COMPLETED_REQUIRES_EXTERNAL_VERIFY'; account_sid_removed=$true; root_removed=$true; new_empty_parent_removed=$true; new_profile_remaining=$false; normal_windows_audit_events_preserved=$true } | ConvertTo-Json
