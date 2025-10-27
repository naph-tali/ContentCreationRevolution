#  ULTRA SIMPLE DEEPSEEK REVOLUTION INIT
Write-Host "DeepSeek Revolution - VS Code" -ForegroundColor Cyan
Write-Host "=============================" -ForegroundColor Cyan

# Activate environment
if (Test-Path "../venv/Scripts/Activate.ps1") {
    & "../venv/Scripts/Activate.ps1"
    Write-Host " Venv: ACTIVE" -ForegroundColor Green
}

# Simple status check
function Show-SimpleStatus {
    Write-Host "
 SIMPLE STATUS:" -ForegroundColor Yellow
    
    $envOk = Test-Path "../.env"
    $engineOk = Test-Path "../ENGINE_CORE/working_revolution_engine.py"
    $venvOk = Test-Path "../venv"
    
    Write-Host "Environment: " -ForegroundColor 
    Write-Host "Engine: " -ForegroundColor 
    Write-Host "Virtual Env: " -ForegroundColor 
    
    if ($envOk -and $engineOk -and $venvOk) {
        Write-Host "
🎯 STATUS: READY TO START!" -ForegroundColor Green
    } else {
        Write-Host "
⚠️  STATUS: SETUP NEEDED" -ForegroundColor Red
    }
}

function Start-SimpleEngine {
    Write-Host "
🚀 STARTING ENGINE..." -ForegroundColor Green
    Set-Location ".."
    python ENGINE_CORE/working_revolution_engine.py
}

Set-Alias sstatus Show-SimpleStatus
Set-Alias sstart Start-SimpleEngine

Write-Host "
 Commands: sstatus, sstart" -ForegroundColor Yellow
Show-SimpleStatus
