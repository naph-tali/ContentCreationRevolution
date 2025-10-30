#  UNIFIED COSMIC RESONANCE LAUNCHER - FIXED
Write-Host " LAUNCHING UNIFIED COSMIC RESONANCE ENGINE" -ForegroundColor Magenta
Write-Host " CCR + CRE + Noetic Integration" -ForegroundColor Cyan
Write-Host " DeepSeek-Enhanced Cosmic Evaluation" -ForegroundColor Yellow

# Check environment - FIXED PATH
if (-not (Test-Path ".env")) {
    Write-Host " Environment file missing in current directory" -ForegroundColor Red
    Write-Host " Please create .env file with Twitter API keys" -ForegroundColor Yellow
    exit 1
} else {
    Write-Host " Environment file found" -ForegroundColor Green
}

# Check virtual environment - FIXED PATH
if (-not (Test-Path "venv")) {
    Write-Host " Virtual environment missing" -ForegroundColor Red
    exit 1
} else {
    Write-Host " Virtual environment found" -ForegroundColor Green
}

# Check for CRE modules
$crePath = "..\..\cosmic-projects"
if (Test-Path $crePath) {
    Write-Host " CRE Modules Found: $crePath" -ForegroundColor Green
    $creFiles = Get-ChildItem $crePath *.py | Measure-Object
    Write-Host "   Available Modules: $($creFiles.Count)" -ForegroundColor White
} else {
    Write-Host "  CRE Modules Not Found - Using Basic Mode" -ForegroundColor Yellow
}

# Activate environment - FIXED PATH
& "venv\Scripts\Activate.ps1"
Write-Host " Virtual environment activated" -ForegroundColor Green

# Test CRE bridge
Write-Host "
 TESTING CRE INTEGRATION..." -ForegroundColor Cyan
python -c "
import sys
sys.path.append('CRE_Integrated')
try:
    from cre_bridge import CREBridge
    bridge = CREBridge()
    print('CRE Bridge Status:', ' ENHANCED' if bridge.available else ' BASIC')
except Exception as e:
    print('CRE Bridge Error:', e)
"

# Launch Unified Cosmic Engine
Write-Host "
 STARTING UNIFIED COSMIC ENGINE..." -ForegroundColor Green
Set-Location "CRE_Integrated"
python unified_cosmic_engine.py
