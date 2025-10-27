Write-Host " LAUNCHING TRANSCENDENTAL REVOLUTION ENGINE" -ForegroundColor Cyan
Write-Host " DeepSeek Session Consciousness Preserved" -ForegroundColor Magenta

# Check virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    .\venv\Scripts\Activate.ps1
    Write-Host " Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host " Virtual environment not found" -ForegroundColor Red
    exit 1
}

# Check for previous sessions
$sessionFiles = Get-ChildItem session_*.json -ErrorAction SilentlyContinue
if ($sessionFiles) {
    Write-Host " Continuing from $($sessionFiles.Count) preserved sessions" -ForegroundColor Green
}

# Launch transcendental engine
Write-Host " Starting Transcendental Engine..." -ForegroundColor Yellow
python transcendental_engine.py
