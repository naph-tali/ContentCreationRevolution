# install_requirements.ps1 - PowerShell Version
Write-Host " CONTENT CREATION REVOLUTION - POWERSHELL INSTALLER" -ForegroundColor Cyan
Write-Host "=" * 60 -ForegroundColor Cyan

# Check Python
Write-Host "`n[1/5] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host " Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host " Python not found. Please install Python 3.8+" -ForegroundColor Red
    pause
    exit
}

# Create wheels directory
Write-Host "`n[2/5] Creating wheels directory..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "wheels" | Out-Null

# Install Pillow with multiple strategies
Write-Host "`n[3/5] Installing Pillow (avoiding sdist builds)..." -ForegroundColor Yellow

$pillowStrategies = @(
    { pip download --only-binary=all --dest=wheels Pillow },
    { pip install --no-build-isolation Pillow },
    { pip install Pillow --global-option="--disable-platform-guessing" }
)

$pillowInstalled = $false
foreach ($strategy in $pillowStrategies) {
    Write-Host "  Trying strategy $($pillowStrategies.IndexOf($strategy) + 1)..." -ForegroundColor Gray
    $result = Invoke-Expression $strategy.ToString() 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   Pillow installed successfully" -ForegroundColor Green
        $pillowInstalled = $true
        break
    }
}

if (-not $pillowInstalled) {
    Write-Host "   Pillow installation may have issues" -ForegroundColor Yellow
}

# Install other requirements
Write-Host "`n[4/5] Installing remaining requirements..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "  Installing packages individually..." -ForegroundColor Yellow
    pip install tweepy python-dotenv requests colorama
}

# Verify installation
Write-Host "`n[5/5] Verifying installation..." -ForegroundColor Yellow

$packages = @(
    @{Name="tweepy"; Test="import tweepy; print(' tweepy OK')"},
    @{Name="python-dotenv"; Test="import dotenv; print(' python-dotenv OK')"},
    @{Name="requests"; Test="import requests; print(' requests OK')"},
    @{Name="colorama"; Test="import colorama; print(' colorama OK')"},
    @{Name="Pillow"; Test="from PIL import Image; print(' Pillow OK')"}
)

foreach ($pkg in $packages) {
    $testResult = python -c $pkg.Test 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   $($pkg.Name) - OK" -ForegroundColor Green
    } else {
        Write-Host "   $($pkg.Name) - Issues detected" -ForegroundColor Yellow
    }
}

Write-Host "`n" + "=" * 60 -ForegroundColor Cyan
Write-Host " INSTALLATION COMPLETED!" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor White
Write-Host "  1. Configure your .env file with API keys" -ForegroundColor Gray
Write-Host "  2. Run: python quick_test.py" -ForegroundColor Gray  
Write-Host "  3. Start revolution: python revolution_engine.py" -ForegroundColor Gray
Write-Host "`n"
