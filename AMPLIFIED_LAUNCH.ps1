Write-Host " DIVINE COSMIC LAUNCHER" -ForegroundColor Magenta
Write-Host " PRAISES TO THE MOST HIGH" -ForegroundColor Cyan
Write-Host " Integrating Silicon and Spirit" -ForegroundColor Yellow

.\venv\Scripts\Activate.ps1

Write-Host "`n CHECKING DIVINE COMPONENTS..." -ForegroundColor Green

$divineFiles = @(
    "ENHANCED_FINAL_UNIFIED_SYSTEM.py",
    "CLEAN_ULTIMATE_INTEGRATION.py", 
    "CLEAN_COSMIC_ENGINE.py",
    "CLEAN_TEST.py"
)

foreach ($file in $divineFiles) {
    if (Test-Path $file) {
        Write-Host " $file" -ForegroundColor Green
    } else {
        Write-Host " $file" -ForegroundColor Red
    }
}

Write-Host "`n LAUNCHING FINAL UNIFIED SYSTEM..." -ForegroundColor Cyan
Write-Host " Operating in Divine Flow..." -ForegroundColor Yellow

python ENHANCED_FINAL_UNIFIED_SYSTEM.py
