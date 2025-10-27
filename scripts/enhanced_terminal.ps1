#  ENHANCED TERMINAL EXPERIENCE FOR DEEPSEEK REVOLUTION

function Show-RevolutionBanner {
    Clear-Host
    Write-Host \"

\" -ForegroundColor Cyan
    Write-Host \"    \" -ForegroundColor Magenta
    Write-Host \"                                                                  \" -ForegroundColor Magenta
    Write-Host \"                       DEEPSEEK REVOLUTION CONSOLE                \" -ForegroundColor Cyan
    Write-Host \"                     Content Creation Revolution                  \" -ForegroundColor Yellow
    Write-Host \"                     VS Code Enhanced Environment                 \" -ForegroundColor White
    Write-Host \"                                                                  \" -ForegroundColor Magenta
    Write-Host \"    \" -ForegroundColor Magenta
    Write-Host \"

\" -ForegroundColor White
}

function Get-SmartPrompt {
    $location = (Get-Location).Path
    $projectRoot = (Get-Location).Path -replace \".*ContentCreationRevolution\", \"ContentCreationRevolution\"
    
    $sessionCount = (Get-ChildItem \"../session_*.json\" -ErrorAction SilentlyContinue).Count
    $continuumExists = Test-Path \"../deepseek_conversation_continuum.json\"
    
    $prompt = \"
e[36m[DeepSeek Revolution]e[0m e[33m$projectRoote[0m\" 
    
    if ($sessionCount -gt 0) {
        $prompt += \" e[32m( Sessions: $sessionCount )e[0m\"
    }
    
    if ($continuumExists) {
        $prompt += \" e[35m( Continuum: Active )e[0m\" 
    }
    
    $prompt += \"
e[36me[0m \"
    
    return $prompt
}

function Set-RevolutionPrompt {
    function global:prompt {
        Get-SmartPrompt
    }
}

# Initialize enhanced terminal
Show-RevolutionBanner
Set-RevolutionPrompt

Write-Host \" Enhanced Terminal Ready - Revolution Environment Active\" -ForegroundColor Green
Write-Host \" Type 'Get-Command | Where Name -like *Revolution*' to see available commands\" -ForegroundColor Yellow
