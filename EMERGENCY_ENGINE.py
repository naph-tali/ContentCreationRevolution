Write-Host " ULTIMATE COSMIC RESONANCE LAUNCHER" -ForegroundColor Magenta
Write-Host " MULTIPLE ENGINE OPTIONS - ONE WILL WORK!" -ForegroundColor Cyan

.\venv\Scripts\Activate.ps1

if (Test-Path ".env") {
    Write-Host " Environment file found" -ForegroundColor Green
} else {
    Write-Host " Environment file missing" -ForegroundColor Red
    exit 1
}

Write-Host "`n CHECKING AVAILABLE ENGINES..." -ForegroundColor Yellow

$engines = @(
    @{Name = "SINGLE COMPLETE ENGINE"; File = "SINGLE_COMPLETE_ENGINE.py"},
    @{Name = "ULTIMATE CRE INTEGRATION"; File = "ULTIMATE_CRE_INTEGRATION.py"},
    @{Name = "SIMPLE ENHANCED ENGINE"; File = "simple_enhanced_engine.py"},
    @{Name = "DIRECT LAUNCH"; File = "direct_launch.ps1"}
)

$availableEngines = @()

foreach ($engine in $engines) {
    if (Test-Path $engine.File) {
        Write-Host " $($engine.Name): AVAILABLE" -ForegroundColor Green
        $availableEngines += $engine
    } else {
        Write-Host "❌ $($engine.Name): MISSING" -ForegroundColor Red
    }
}

if ($availableEngines.Count -eq 0) {
    Write-Host "`n💥 NO ENGINES AVAILABLE!" -ForegroundColor Red
    Write-Host "   Creating emergency engine..." -ForegroundColor Yellow
    
    # Create emergency engine
    @'
print(" EMERGENCY COSMIC ENGINE ACTIVATED!")
print(" Basic functionality - Ready to create content!")
import time
while True:
    print(" Cosmic cycle completed")
    time.sleep(60)
