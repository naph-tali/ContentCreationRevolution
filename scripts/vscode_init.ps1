#  DEEPSEEK REVOLUTION - VS CODE ENHANCED ENVIRONMENT
Write-Host \"

\" -ForegroundColor Cyan
Write-Host \"        \" -ForegroundColor Magenta
Write-Host \"     \" -ForegroundColor Magenta  
Write-Host \"               \" -ForegroundColor Magenta
Write-Host \"               \" -ForegroundColor Magenta
Write-Host \"        \" -ForegroundColor Magenta
Write-Host \"         \" -ForegroundColor Magenta
Write-Host \"

              CONTENT CREATION REVOLUTION - VS CODE ENHANCED\" -ForegroundColor Cyan
Write-Host \"                     DeepSeek API Integrated Environment\" -ForegroundColor Yellow
Write-Host \"
\" -ForegroundColor White

# Check environment
if (Test-Path \"../.env\") {
    Write-Host \" Project Environment: LOADED\" -ForegroundColor Green
} else {
    Write-Host \" Project Environment: MISSING .env file\" -ForegroundColor Red
}

# Activate virtual environment
if (Test-Path \"../venv/Scripts/Activate.ps1\") {
    & \"../venv/Scripts/Activate.ps1\"
    Write-Host \" Virtual Environment: ACTIVATED\" -ForegroundColor Green
} else {
    Write-Host \" Virtual Environment: NOT FOUND\" -ForegroundColor Red
}

# Load DeepSeek enhancement functions
function Show-RevolutionStatus {
    Write-Host \"
 REVOLUTION STATUS\" -ForegroundColor Cyan
    Write-Host \"================\" -ForegroundColor Cyan
    
    $sessionFiles = Get-ChildItem \"../session_*.json\" -ErrorAction SilentlyContinue
    $continuumFiles = Get-ChildItem \"../deepseek_conversation_continuum.json\" -ErrorAction SilentlyContinue
    
    Write-Host \"Active Sessions: $($sessionFiles.Count)\" -ForegroundColor White
    Write-Host \"Continuum Entries: $(if ($continuumFiles) { (Get-Content $continuumFiles[0] | ConvertFrom-Json).Count } else { 0 })\" -ForegroundColor White
    Write-Host \"Project Health: $(if (Test-Path \"../.env\") { 'HEALTHY' } else { 'NEEDS SETUP' })\" -ForegroundColor $(if (Test-Path \"../.env\") { 'Green' } else { 'Red' })
}

function Start-RevolutionEngine {
    Write-Host \"
🚀 STARTING REVOLUTION ENGINE...\" -ForegroundColor Green
    Set-Location \"..\"
    python ENGINE_CORE/working_revolution_engine.py
}

function Start-TranscendentalEngine {
    Write-Host \"
 STARTING TRANSCENDENTAL CONTINUUM ENGINE...\" -ForegroundColor Magenta
    Set-Location \"..\"
    python transcendental_engine_continuum.py
}

function Show-ContinuumDashboard {
    Write-Host \"
 OPENING CONTINUUM DASHBOARD...\" -ForegroundColor Cyan
    Set-Location \"..\"
    python control_dashboard.py
}

function Test-DeepSeekAPI {
    Write-Host \"
 TESTING DEEPSEEK API CONNECTION...\" -ForegroundColor Yellow
    # Placeholder for DeepSeek API testing
    Write-Host \"DeepSeek API: READY FOR INTEGRATION\" -ForegroundColor Green
}

function Update-RevolutionEnvironment {
    Write-Host \"
 UPDATING REVOLUTION ENVIRONMENT...\" -ForegroundColor Yellow
    Set-Location \"..\"
    & \"scripts/install_requirements.ps1\"
}

# Display available commands
Write-Host \"
 AVAILABLE COMMANDS:\" -ForegroundColor Cyan
Write-Host \"   status          - Show revolution status\" -ForegroundColor White
Write-Host \"   start           - Start revolution engine\" -ForegroundColor White  
Write-Host \"   transcendental  - Start transcendental engine\" -ForegroundColor White
Write-Host \"   dashboard       - Open continuum dashboard\" -ForegroundColor White
Write-Host \"   test-api        - Test DeepSeek API connection\" -ForegroundColor White
Write-Host \"   update          - Update environment\" -ForegroundColor White
Write-Host \"   help            - Show this help\" -ForegroundColor White

# Set up command aliases
Set-Alias status Show-RevolutionStatus
Set-Alias start Start-RevolutionEngine
Set-Alias transcendental Start-TranscendentalEngine
Set-Alias dashboard Show-ContinuumDashboard
Set-Alias test-api Test-DeepSeekAPI
Set-Alias update Update-RevolutionEnvironment
Set-Alias help Get-CommandHelp

function Get-CommandHelp {
    Write-Host \"
 DEEPSEEK REVOLUTION - VS CODE COMMANDS\" -ForegroundColor Cyan
    Write-Host \"=========================================\" -ForegroundColor Cyan
    Get-Alias | Where-Object { $_.Definition -like \"*-*\" } | Format-Table Name, Definition -AutoSize
}

# Show initial status
Show-RevolutionStatus

Write-Host \"
 VS Code DeepSeek Environment Ready! Type 'help' for commands.\" -ForegroundColor Green
