param(
    [switch]$Persist,
    [switch]$Remove,
    [string]$EnvFile = ".\.env"
)

function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

function Show-Usage {
    Write-ColorOutput "`nUsage:" "Cyan"
    Write-ColorOutput "  .\set-twitter-env.ps1           # Load .env to current session" "Gray"
    Write-ColorOutput "  .\set-twitter-env.ps1 -Persist  # Persist to User environment" "Gray"
    Write-ColorOutput "  .\set-twitter-env.ps1 -Remove   # Remove all Twitter variables" "Gray"
    Write-ColorOutput "`n.env file format:" "Cyan"
    Write-ColorOutput "  TWITTER_CONSUMER_KEY=your_key_here" "DarkGray"
    Write-ColorOutput "  TWITTER_CONSUMER_SECRET=your_secret_here" "DarkGray"
    Write-ColorOutput "  TWITTER_ACCESS_TOKEN=your_access_token_here" "DarkGray"
    Write-ColorOutput "  TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here" "DarkGray"
    Write-ColorOutput "  TWITTER_BEARER_TOKEN=your_bearer_token_here  # optional" "DarkGray"
}

function Protect-Secret {
    param([string]$token, [int]$keep=4)
    if (-not $token) { return "<missing>" }
    $t = $token.Trim()
    if ($t.Length -le ($keep * 2)) { return "****" }
    return $t.Substring(0,$keep) + "..." + $t.Substring($t.Length - $keep, $keep)
}

function ConvertTo-TrimmedString {
    param([string]$s)
    if ($null -eq $s) { return $null }
    $s = $s.Trim()
    if ($s -match '^"(.*)"$' -or $s -match "^'(.*)'$") { return $matches[1] }
    return $s
}

function Get-EnvFile {
    param([string]$path)
    $ht = @{}
    if (-not (Test-Path $path)) { return $ht }
    Get-Content $path | ForEach-Object {
        $line = $_.Trim()
        if (-not $line -or $line.StartsWith('#')) { return }
        if ($line -match '^\s*([^=]+?)\s*=\s*(.*)$') {
            $key = $matches[1].Trim()
            $val = ConvertTo-TrimmedString $matches[2]
            if ($null -ne $val) { $val = $val.Trim() }
            $ht[$key] = $val
        }
    }
    return $ht
}

function Remove-TwitterEnvironment {
    param([string[]]$Keys)
    Write-ColorOutput "Removing Twitter environment variables..." "Yellow"
    $removedCount = 0
    foreach ($varName in $Keys) {
        if (Test-Path "Env:$varName") {
            Remove-Item "Env:$varName" -ErrorAction SilentlyContinue
            Write-ColorOutput "  [SESSION] Removed: $varName" "Yellow"
            $removedCount++
        }
        $currentPerm = [Environment]::GetEnvironmentVariable($varName, "User")
        if (-not [string]::IsNullOrEmpty($currentPerm)) {
            [Environment]::SetEnvironmentVariable($varName, $null, "User")
            Write-ColorOutput "  [PERMANENT] Removed: $varName" "Yellow"
            $removedCount++
        }
    }
    if ($removedCount -eq 0) {
        Write-ColorOutput "No Twitter environment variables found to remove." "Yellow"
    } else {
        Write-ColorOutput "Successfully removed $removedCount Twitter environment items." "Green"
    }
}

function Set-TwitterEnvironment {
    param([string]$Path, [string[]]$Keys, [bool]$PersistMode = $false)

    if (-not (Test-Path $Path)) {
        # Avoid "$Path:" interpolation issue by using formatted string
        Write-ColorOutput (" ERROR: {0} not found in current directory!" -f $Path) "Red"
        Show-Usage
        return $false
    }

    Write-ColorOutput (" Loading Twitter environment variables from {0}..." -f $Path) "Cyan"
    $envVars = Get-EnvFile -Path $Path
    if ($envVars -eq $null) {
        # Avoid "$Path:" interpolation issue by using formatted string
        Write-ColorOutput (" ERROR: Failed to parse {0}" -f $Path) "Red"
        return $false
    }

    # Alias mapping: allow older or alternate names in .env
    $aliases = @{
        "TWITTER_CONSUMER_KEY"         = @("TWITTER_CONSUMER_KEY","TWITTER_API_KEY")
        "TWITTER_CONSUMER_SECRET"      = @("TWITTER_CONSUMER_SECRET","TWITTER_API_SECRET")
        "TWITTER_ACCESS_TOKEN"         = @("TWITTER_ACCESS_TOKEN")
        "TWITTER_ACCESS_TOKEN_SECRET"  = @("TWITTER_ACCESS_TOKEN_SECRET","TWITTER_ACCESS_SECRET")
        "TWITTER_BEARER_TOKEN"         = @("TWITTER_BEARER_TOKEN")
    }

    # Resolve canonical keys from aliases
    $resolved = @{}
    foreach ($target in $Keys) {
        if (-not $aliases.ContainsKey($target)) { continue }
        foreach ($alias in $aliases[$target]) {
            if ($envVars.ContainsKey($alias) -and -not [string]::IsNullOrWhiteSpace($envVars[$alias])) {
                $resolved[$target] = $envVars[$alias]
                break
            }
        }
    }

    # Required set: consumer_key, consumer_secret, access_token, access_token_secret
    $required = @(
        "TWITTER_CONSUMER_KEY",
        "TWITTER_CONSUMER_SECRET",
        "TWITTER_ACCESS_TOKEN",
        "TWITTER_ACCESS_TOKEN_SECRET"
    )

    $missingVars = @()
    foreach ($r in $required) {
        if (-not $resolved.ContainsKey($r)) { $missingVars += $r }
    }

    if ($missingVars.Count -gt 0) {
        # Avoid "$Path:" interpolation issue by using formatted string
        Write-ColorOutput (" ERROR: Missing required variables in {0}:" -f $Path) "Red"
        foreach ($missing in $missingVars) { Write-ColorOutput "  - $missing" "Yellow" }
        return $false
    }

    # Set resolved canonical variables into session and optionally User env
    $setCount = 0
    foreach ($kv in $resolved.GetEnumerator()) {
        $varName = $kv.Key
        $value = $kv.Value
        $maskedValue = Protect-Secret $value

        # Set for current session
        Set-Item -Path "Env:$varName" -Value $value
        Write-ColorOutput "  [SESSION] Set: $varName = $maskedValue" "Green"

        # Persist if requested
        if ($PersistMode) {
            [Environment]::SetEnvironmentVariable($varName, $value, "User")
            Write-ColorOutput "  [PERMANENT] Set: $varName = $maskedValue" "Green"
        }

        $setCount++
    }

    if ($setCount -gt 0) {
        if ($PersistMode) {
            Write-ColorOutput " Successfully persisted $setCount Twitter variables to User environment!" "Green"
            Write-ColorOutput " Restart PowerShell to see permanent variables in new sessions." "Cyan"
        } else {
            Write-ColorOutput " Successfully loaded $setCount Twitter variables for current session!" "Green"
        }
        return $true
    }

    return $false
}

function Show-CurrentState {
    param([string[]]$Keys)
    Write-ColorOutput "`nCurrent Environment Status:" "White"
    Write-ColorOutput "===========================" "White"

    Write-ColorOutput "Session Variables (Current PowerShell):" "Cyan"
    $sessionVars = 0
    foreach ($varName in $Keys) {
        $value = [Environment]::GetEnvironmentVariable($varName, "Process")
        if (-not [string]::IsNullOrEmpty($value)) {
            $maskedValue = Protect-Secret $value
            Write-ColorOutput "   $varName = $maskedValue" "Gray"
            $sessionVars++
        }
    }
    if ($sessionVars -eq 0) { Write-ColorOutput "   No Twitter variables set in current session" "DarkGray" }

    Write-ColorOutput "`nPermanent Variables (User Environment):" "Cyan"
    $permVars = 0
    foreach ($varName in $Keys) {
        $value = [Environment]::GetEnvironmentVariable($varName, "User")
        if (-not [string]::IsNullOrEmpty($value)) {
            $maskedValue = Protect-Secret $value
            Write-ColorOutput "   $varName = $maskedValue" "Gray"
            $permVars++
        }
    }
    if ($permVars -eq 0) { Write-ColorOutput "   No permanent Twitter variables set" "DarkGray" }
}

# Main
$TwitterVars = @(
    "TWITTER_CONSUMER_KEY",
    "TWITTER_CONSUMER_SECRET",
    "TWITTER_ACCESS_TOKEN",
    "TWITTER_ACCESS_TOKEN_SECRET",
    "TWITTER_BEARER_TOKEN"
)

try {
    Write-ColorOutput " Twitter Environment Manager" "White"
    Write-ColorOutput "==============================" "White"

    if ($Remove) {
        if ($Persist) {
            Write-ColorOutput " ERROR: Cannot use -Remove and -Persist together" "Red"
            Show-Usage
            exit 1
        }
        Remove-TwitterEnvironment -Keys $TwitterVars
    }
    elseif ($Persist) {
        Set-TwitterEnvironment -Path ${EnvFile} -Keys $TwitterVars -PersistMode $true | Out-Null
    }
    else {
        Set-TwitterEnvironment -Path ${EnvFile} -Keys $TwitterVars -PersistMode $false | Out-Null
    }

    Show-CurrentState -Keys $TwitterVars

    if (-not $Remove -and -not $Persist) {
        Write-ColorOutput "`nTip: Use -Persist to make these variables permanent" "Cyan"
    }
}
catch {
    Write-ColorOutput (" ERROR: {0}" -f $_.Exception.Message) "Red"
    exit 1
}
