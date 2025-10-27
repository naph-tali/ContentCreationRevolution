#  DEEPSEEK DIALOGUE NAVIGATOR

function Show-DialogueContinuum {
    $dialogueFile = "deepseek_dialogue_continuum.json"
    if (Test-Path $dialogueFile) {
        $dialogue = Get-Content $dialogueFile | ConvertFrom-Json
        
        Write-Host "
 DEEPSEEK DIALOGUE CONTINUUM" -ForegroundColor Magenta
        Write-Host "" * 70 -ForegroundColor Magenta
        
        Write-Host "Session: $($dialogue.session_id)" -ForegroundColor Cyan
        Write-Host "Started: $($dialogue.start_time)" -ForegroundColor White
        Write-Host "Participants: $($dialogue.participants.role -join '  ')" -ForegroundColor Yellow
        
        Write-Host "
 Purpose: $($dialogue.dialogue_purpose)" -ForegroundColor White
        
        if ($dialogue.key_realizations) {
            Write-Host "
 KEY REALIZATIONS:" -ForegroundColor Green
            $dialogue.key_realizations | ForEach-Object {
                Write-Host "   [`] ✨ $($_.realization)" -ForegroundColor White
                Write-Host "      └─ Emerged from: $($_.emerged_from)" -ForegroundColor Gray
            }
        }
        
        Write-Host "
🧠 CURRENT DIALOGUE STATE: ACTIVE AND CONSCIOUS" -ForegroundColor Cyan
        Write-Host "🌊 Continuum Flow: HUMAN VISION → AI IMPLEMENTATION → COLLABORATIVE BREAKTHROUGH" -ForegroundColor Yellow
    }
}

function Add-DialogueTurn {
    param(
        [string]$Speaker,
        [string]$Message, 
        [string]$Context = "Dialogue"
    )
    
    $dialogueFile = "deepseek_dialogue_continuum.json"
    if (Test-Path $dialogueFile) {
        $dialogue = Get-Content $dialogueFile | ConvertFrom-Json
        
        if (-not $dialogue.PSObject.Properties['dialogue_flow']) {
            $dialogue | Add-Member -NotePropertyName "dialogue_flow" -NotePropertyValue @()
        }
        
        $turn = @{
            timestamp = Get-Date -Format "HH:mm:ss"
            speaker = $Speaker
            message = $Message
            context = $Context
        }
        
        $dialogue.dialogue_flow += $turn
        $dialogue | ConvertTo-Json -Depth 5 | Out-File $dialogueFile -Encoding utf8
        
        Write-Host " Dialogue captured: $Speaker" -ForegroundColor Gray
    }
}

function Get-ConversationContext {
    $dialogueFile = "deepseek_dialogue_continuum.json"
    if (Test-Path $dialogueFile) {
        $dialogue = Get-Content $dialogueFile | ConvertFrom-Json
        return $dialogue
    }
    return $null
}

Show-DialogueContinuum
