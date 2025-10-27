#  C-LIGHT SPEED REVOLUTION LAUNCHER
Write-Host "Starting Content Creation Revolution..." -ForegroundColor Cyan

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    .\venv\Scripts\Activate.ps1
    Write-Host "Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host " Virtual environment not found" -ForegroundColor Red
    exit 1
}

# Validate environment first
Write-Host "Validating environment..." -ForegroundColor Yellow
python validate_environment.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "Environment validated successfully!" -ForegroundColor Green
    Write-Host "Launching revolution engine..." -ForegroundColor Cyan
    python working_revolution_engine.py
} else {
    Write-Host "❌ Environment validation failed. Check your API keys." -ForegroundColor Red
}
