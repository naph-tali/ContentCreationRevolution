#  ENHANCED PROJECT MANAGEMENT WITH DEEPSEEK INTEGRATION

function Get-ProjectHealth {
    Write-Host \"
 PROJECT HEALTH CHECK\" -ForegroundColor Cyan
    Write-Host \"==================\" -ForegroundColor Cyan
    
    $checks = @(
        @{ Name = \"Virtual Environment\"; Test = { Test-Path \"../venv\" }; Critical = $true },
        @{ Name = \"Environment File\"; Test = { Test-Path \"../.env\" }; Critical = $true },
        @{ Name = \"Twitter API Keys\"; Test = { 
            $envContent = Get-Content \"../.env\" -ErrorAction SilentlyContinue
            $envContent -match \"TWITTER_API_KEY\" -and $envContent -match \"TWITTER_API_SECRET\" 
        }; Critical = $true },
        @{ Name = \"Python Dependencies\"; Test = { 
            & \"../venv/Scripts/python.exe\" -c \"import tweepy, dotenv\" 2>$null
            $? 
        }; Critical = $true },
        @{ Name = \"Revolution Engine\"; Test = { Test-Path \"../ENGINE_CORE/working_revolution_engine.py\" }; Critical = $false },
        @{ Name = \"Session Continuity\"; Test = { Test-Path \"../session_continuity.ps1\" }; Critical = $false }
    )
    
    $allHealthy = $true
    foreach ($check in $checks) {
        $result = & $check.Test
        $status = if ($result) { \"\" } else { \"\" }
        $color = if ($result) { \"Green\" } else { if ($check.Critical) { \"Red\" } else { \"Yellow\" } }
        
        Write-Host \"$status $($check.Name)\" -ForegroundColor $color
        
        if (-not $result -and $check.Critical) {
            $allHealthy = $false
        }
    }
    
    return $allHealthy
}

function Start-SmartRevolution {
    param([switch]$UseDeepSeek)
    
    Write-Host \"
 STARTING SMART REVOLUTION ENGINE\" -ForegroundColor Cyan
    
    # Check project health first
    if (-not (Get-ProjectHealth)) {
        Write-Host \" Project health check failed. Please fix issues before starting.\" -ForegroundColor Red
        return
    }
    
    if ($UseDeepSeek) {
        Write-Host \" DeepSeek Enhancement: ENABLED\" -ForegroundColor Green
        
        # Load DeepSeek API module
        . .\deepseek_api.ps1
        
        # Initialize DeepSeek client (would need API key from environment)
        $deepSeekClient = Initialize-DeepSeek -ApiKey $env:DEEPSEEK_API_KEY
        
        if ($deepSeekClient) {
            Write-Host \" DeepSeek AI Assistant Active\" -ForegroundColor Green
        }
    }
    
    Write-Host \" Launching Revolution Engine...\" -ForegroundColor Green
    Set-Location \"..\"
    python ENGINE_CORE/working_revolution_engine.py
}

function Update-ProjectDependencies {
    Write-Host \"
 UPDATING PROJECT DEPENDENCIES\" -ForegroundColor Yellow
    
    if (-not (Test-Path \"../venv\")) {
        Write-Host \" Virtual environment not found\" -ForegroundColor Red
        return
    }
    
    & \"../venv/Scripts/Activate.ps1\"
    
    # Update pip first
    Write-Host \"Updating pip...\" -ForegroundColor White
    python -m pip install --upgrade pip
    
    # Install requirements
    if (Test-Path \"../requirements.txt\") {
        Write-Host \"Installing requirements...\" -ForegroundColor White
        pip install -r \"../requirements.txt\"
    }
    
    Write-Host \" Dependencies updated successfully\" -ForegroundColor Green
}

function Backup-ProjectState {
    param([string]$BackupName = \"auto_$(Get-Date -Format 'yyyyMMdd_HHmmss')\")
    
    Write-Host \"
 BACKING UP PROJECT STATE: $BackupName\" -ForegroundColor Cyan
    
    $backupDir = \"../backups/$BackupName\"
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
    
    $itemsToBackup = @(
        \"../.env\",
        \"../session_*.json\", 
        \"../deepseek_conversation_continuum.json\",
        \"../current_deepseek_session.json\",
        \"../logs/\",
        \"../ENGINE_CORE/\",
        \"../scripts/\"
    )
    
    foreach ($item in $itemsToBackup) {
        if (Test-Path $item) {
            Copy-Item -Path $item -Destination $backupDir -Recurse -Force
            Write-Host \"   Backed up: $($item -replace '\\.\\./','')\" -ForegroundColor Green
        }
    }
    
    Write-Host \" Project state backed up to: $backupDir\" -ForegroundColor Green
}

function Restore-ProjectState {
    param([string]$BackupName)
    
    Write-Host \"
 RESTORING PROJECT STATE: $BackupName\" -ForegroundColor Cyan
    
    $backupDir = \"../backups/$BackupName\"
    if (-not (Test-Path $backupDir)) {
        Write-Host \" Backup not found: $backupDir\" -ForegroundColor Red
        return
    }
    
    # Restore files
    Get-ChildItem $backupDir -Recurse | ForEach-Object {
        $targetPath = $_.FullName.Replace($backupDir, \"..\\\")
        $targetDir = Split-Path $targetPath -Parent
        
        if (-not (Test-Path $targetDir)) {
            New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        }
        
        Copy-Item -Path $_.FullName -Destination $targetPath -Force
        Write-Host \"   Restored: $($targetPath -replace '\\.\\./','')\" -ForegroundColor Green
    }
    
    Write-Host \" Project state restored from: $backupDir\" -ForegroundColor Green
}

# Export functions
Export-ModuleMember -Function Get-ProjectHealth, Start-SmartRevolution, Update-ProjectDependencies, Backup-ProjectState, Restore-ProjectState
