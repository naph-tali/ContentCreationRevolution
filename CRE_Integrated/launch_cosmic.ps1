#  UNIFIED COSMIC RESONANCE LAUNCHER
Write-Host " LAUNCHING UNIFIED COSMIC RESONANCE ENGINE" -ForegroundColor Magenta
Write-Host " CCR + CRE + Noetic Integration" -ForegroundColor Cyan
Write-Host " DeepSeek-Enhanced Cosmic Evaluation" -ForegroundColor Yellow

# Check environment
if (-not (Test-Path "../.env")) {
    Write-Host " Environment file missing" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "../venv")) {
    Write-Host " Virtual environment missing" -ForegroundColor Red
    exit 1
}

# Check for CRE modules
 = "C:\Users\X\Documents\cosmic-projects"
if (Test-Path ) {
    Write-Host " CRE Modules Found: " -ForegroundColor Green
     = Get-ChildItem  *.py | Measure-Object
    Write-Host "   Available Modules: 0" -ForegroundColor White
} else {
    Write-Host "⚠  CRE Modules Not Found - Using Basic Mode" -ForegroundColor Yellow
}

# Activate environment
& "../venv/Scripts/Activate.ps1"
Write-Host " Virtual environment activated" -ForegroundColor Green

# Test CRE bridge
Write-Host "
 TESTING CRE INTEGRATION..." -ForegroundColor Cyan
python -c "
import sys
sys.path.append('CRE_Integrated')
from cre_bridge import CREBridge
bridge = CREBridge()
print('CRE Bridge Status:', ' ENHANCED' if bridge.available else ' BASIC')
"

# Launch Unified Cosmic Engine
Write-Host "
 STARTING UNIFIED COSMIC ENGINE..." -ForegroundColor Green
python unified_cosmic_engine.py
