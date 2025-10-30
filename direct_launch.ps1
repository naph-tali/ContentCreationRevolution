#  DIRECT COSMIC LAUNCH - NO PATH ISSUES
Write-Host " DIRECT COSMIC RESONANCE LAUNCH" -ForegroundColor Magenta

# Activate environment directly
if (Test-Path "venv\Scripts\Activate.ps1") {
    & "venv\Scripts\Activate.ps1"
    Write-Host " Virtual environment activated" -ForegroundColor Green
} else {
    Write-Host " Virtual environment not found" -ForegroundColor Red
    exit 1
}

# Check .env
if (Test-Path ".env") {
    Write-Host " Environment file found" -ForegroundColor Green
} else {
    Write-Host " .env file missing - creating template" -ForegroundColor Red
    @' 
TWITTER_API_KEY=your_key_here
TWITTER_API_SECRET=your_secret_here
TWITTER_ACCESS_TOKEN=your_token_here  
TWITTER_ACCESS_SECRET=your_secret_here
'@ | Out-File -FilePath ".env" -Encoding utf8
    Write-Host " Please edit .env with your API keys" -ForegroundColor Yellow
    exit 1
}

# Launch directly
Write-Host " Starting Unified Cosmic Engine..." -ForegroundColor Green
python "CRE_Integrated\unified_cosmic_engine.py"
