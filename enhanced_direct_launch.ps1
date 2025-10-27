Write-Host " ENHANCED DIRECT COSMIC RESONANCE LAUNCH" -ForegroundColor Magenta
Write-Host " Now with Mathematical Foundation & Anti-Duplicate Protection" -ForegroundColor Cyan

.\venv\Scripts\Activate.ps1

# Install required dependencies for mathematical foundation
Write-Host "`n INSTALLING ENHANCED DEPENDENCIES..." -ForegroundColor Yellow
pip install sentence-transformers networkx scikit-learn --upgrade

if (Test-Path ".env") {
    Write-Host " Environment file found" -ForegroundColor Green
} else {
    Write-Host " Environment file missing" -ForegroundColor Red
    exit 1
}

Write-Host "`n STARTING ENHANCED UNIFIED ENGINE..." -ForegroundColor Green
python CRE_Integrated\enhanced_unified_engine.py
