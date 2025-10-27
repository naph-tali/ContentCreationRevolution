Write-Host " BULLETPROOF COSMIC RESONANCE LAUNCH" -ForegroundColor Magenta
Write-Host " MULTI-ENGINE FALLBACK SYSTEM" -ForegroundColor Cyan

.\venv\Scripts\Activate.ps1

if (Test-Path ".env") {
    Write-Host " Environment file found" -ForegroundColor Green
} else {
    Write-Host " Environment file missing" -ForegroundColor Red
    exit 1
}

Write-Host "`n TESTING ENGINE OPTIONS..." -ForegroundColor Yellow

# Test each engine option
$engines = @(
    @{Name = "SIMPLE ENHANCED"; File = "simple_enhanced_engine.py"},
    @{Name = "DIRECT LAUNCH"; File = "direct_launch.ps1"},
    @{Name = "ENHANCED UNIFIED"; File = "CRE_Integrated\enhanced_unified_engine.py"}
)

foreach ($engine in $engines) {
    if (Test-Path $engine.File) {
        Write-Host " $($engine.Name): AVAILABLE" -ForegroundColor Green
    } else {
        Write-Host " $($engine.Name): MISSING" -ForegroundColor Red
    }
}

Write-Host "`n LAUNCHING SIMPLE ENHANCED ENGINE (Most Reliable)..." -ForegroundColor Green
python simple_enhanced_engine.py
