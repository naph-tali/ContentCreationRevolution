#  ENHANCED DEEPSEEK REVOLUTION INIT
Write-Host "DeepSeek Revolution Environment - VS Code Enhanced" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

# Activate virtual environment
if (Test-Path "../venv/Scripts/Activate.ps1") {
    & "../venv/Scripts/Activate.ps1"
    Write-Host " Virtual Environment: ACTIVATED" -ForegroundColor Green
} else {
    Write-Host " Virtual Environment: NOT FOUND" -ForegroundColor Red
}

# Enhanced status function
function Show-Status {
    Write-Host "
 PROJECT STATUS:" -ForegroundColor Yellow
    
    $checks = @(
        @{ Name = "Environment File"; Path = "../.env"; Critical = $true },
        @{ Name = "Engine Core"; Path = "../ENGINE_CORE/working_revolution_engine.py"; Critical = $true },
        @{ Name = "Virtual Environment"; Path = "../venv"; Critical = $true },
        @{ Name = "Twitter API Keys"; Test = { 
            if (Test-Path "../.env") {
                $envContent = Get-Content "../.env"
                $hasKey = $envContent -match "TWITTER_API_KEY"
                $hasSecret = $envContent -match "TWITTER_API_SECRET"
                $hasKey -and $hasSecret
            } else { $false }
        }; Critical = $true }
    )
    
    $allHealthy = $true
    foreach ($check in $checks) {
        if ($check.Test) {
            $result = & $check.Test
        } else {
            $result = Test-Path $check.Path
        }
        
        $status = if ($result) { "" } else { "" }
        $color = if ($result) { "Green" } else { if ($check.Critical) { "Red" } else { "Yellow" } }
        
        Write-Host "$status $($check.Name)" -ForegroundColor $color
        
        if (-not $result -and $check.Critical) {
            $allHealthy = $false
        }
    }
    
    if ($allHealthy) {
        Write-Host "
 PROJECT STATUS: READY FOR REVOLUTION!" -ForegroundColor Green
    } else {
        Write-Host "
  PROJECT STATUS: NEEDS SETUP" -ForegroundColor Yellow
        Write-Host "   Run setup steps above to fix critical issues" -ForegroundColor Red
    }
}

function Start-Engine {
    Write-Host "
 STARTING REVOLUTION ENGINE..." -ForegroundColor Green
    Set-Location ".."
    python ENGINE_CORE/working_revolution_engine.py
}

function Test-Environment {
    Write-Host "
 TESTING ENVIRONMENT..." -ForegroundColor Cyan
    Set-Location ".."
    
    try {
        python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(' Environment test passed'); print('API Key present:', bool(os.getenv('TWITTER_API_KEY')))"
    } catch {
        Write-Host " Environment test failed: $($_.Exception.Message)" -ForegroundColor Red
    }
}

# Set aliases
Set-Alias status Show-Status
Set-Alias start Start-Engine
Set-Alias test Test-Environment

Write-Host "
 Available commands:" -ForegroundColor Yellow
Write-Host "   status  - Check project status" -ForegroundColor White
Write-Host "   start   - Start revolution engine" -ForegroundColor White
Write-Host "   test    - Test environment" -ForegroundColor White

Show-Status
