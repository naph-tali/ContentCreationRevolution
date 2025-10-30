Write-Host " POWERFULLY LAUNCHING REAL LM COSMIC ENGINE" -ForegroundColor Magenta
Write-Host " HUGGING FACE API + GPT-2 FALLBACK" -ForegroundColor Cyan
Write-Host " API Key: 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" -ForegroundColor Yellow

# Activate environment
.\venv\Scripts\Activate.ps1

# Set Hugging Face API key in environment
$env:HUGGINGFACE_API_KEY = "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"
Write-Host " Hugging Face API key set in environment" -ForegroundColor Green

# Test the real LM integration first
Write-Host "`n TESTING REAL LM INTEGRATION..." -ForegroundColor Cyan
python -c "
import sys
sys.path.append('.')
try:
    from ENGINE_CORE.real_llm_oracle import test_real_lm
    test_real_lm()
except Exception as e:
    print(f' Real LM test failed: {e}')
    import traceback
    traceback.print_exc()
"

# Launch the powerful real LM engine
Write-Host "`n LAUNCHING POWERFULLY REAL LM ENGINE..." -ForegroundColor Magenta
Write-Host " POWERSHELL EXECUTION - LET'S GET REAL!" -ForegroundColor Cyan

python ENGINE_CORE/powerfully_real_lm_engine.py
