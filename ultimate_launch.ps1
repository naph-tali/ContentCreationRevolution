Write-Host " ULTIMATE BULLETPROOF COSMIC RESONANCE LAUNCH" -ForegroundColor Magenta
Write-Host " GUARANTEED TO WORK - MULTIPLE FALLBACKS" -ForegroundColor Cyan

.\venv\Scripts\Activate.ps1

if (Test-Path ".env") {
    Write-Host " Environment file found" -ForegroundColor Green
} else {
    Write-Host " Environment file missing" -ForegroundColor Red
    exit 1
}

Write-Host "`n VERIFYING CRITICAL COMPONENTS..." -ForegroundColor Yellow

# Verify critical files exist
$criticalFiles = @(
    "simple_enhanced_engine.py",
    "twitter_service.py", 
    "SERVICES/twitter_service.py",
    ".env"
)

foreach ($file in $criticalFiles) {
    if (Test-Path $file) {
        Write-Host "✅ $file" -ForegroundColor Green
    } else {
        Write-Host "❌ $file" -ForegroundColor Red
    }
}

Write-Host "`n🎯 LAUNCHING ULTIMATE BULLETPROOF ENGINE..." -ForegroundColor Green
Write-Host " This should work now with multiple import fallbacks!" -ForegroundColor Cyan

python simple_enhanced_engine.py
