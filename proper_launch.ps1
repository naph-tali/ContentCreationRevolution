#  PROPER REVOLUTION LAUNCH SCRIPT
Write-Host "Starting Content Creation Revolution..." -ForegroundColor Green

# Check if engine exists
if (-not (Test-Path "ENGINE_CORE/working_revolution_engine.py")) {
    Write-Host " Engine file not found!" -ForegroundColor Red
    exit 1
}

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host " Virtual environment not found!" -ForegroundColor Red
    exit 1
}

# Activate and run
.\venv\Scripts\Activate.ps1
Write-Host "✅ Virtual environment activated" -ForegroundColor Green

Write-Host "🚀 Launching revolution engine..." -ForegroundColor Cyan
python ENGINE_CORE/working_revolution_engine.py
