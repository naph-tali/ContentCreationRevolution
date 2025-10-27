#  DEEPSEEK CONVERSATION CONTINUUM CAPTURE

function Add-ConversationTurn {
    param(
        [string]$Speaker,
        [string]$Message,
        [string]$Context = "Dialogue"
    )
    
    $sessionFile = "current_deepseek_session.json"
    if (Test-Path $sessionFile) {
        $session = Get-Content $sessionFile | ConvertFrom-Json
        
        if (-not $session.PSObject.Properties['conversation_turns']) {
            $session | Add-Member -NotePropertyName "conversation_turns" -NotePropertyValue @()
        }
        
        $turn = @{
            timestamp = Get-Date -Format "HH:mm:ss"
            speaker = $Speaker
            message = $Message
            context = $Context
        }
        
        $session.conversation_turns += $turn
        $session | ConvertTo-Json -Depth 5 | Out-File $sessionFile -Encoding utf8
        
        Write-Host "💬 Conversation turn captured: $($Speaker)" -ForegroundColor Gray
    }
}

function Show-ConversationFlow {
    $sessionFile = "current_deepseek_session.json"
    if (Test-Path $sessionFile) {
        $session = Get-Content $sessionFile | ConvertFrom-Json
        
        Write-Host "
 CURRENT DEEPSEEK CONVERSATION FLOW" -ForegroundColor Cyan
        Write-Host "=" * 60 -ForegroundColor Cyan
        
        if ($session.conversation_turns) {
            $session.conversation_turns | ForEach-Object {
                $color = if ($_.speaker -eq "Human") { "Yellow" } else { "White" }
                Write-Host "[$($_.timestamp)] $($_.speaker): $($_.message)" -ForegroundColor $color
            }
        } else {
            Write-Host "No conversation turns yet - begin the dialogue!" -ForegroundColor Yellow
        }
    }
}

function Save-ConversationSummary {
    param([string]$Summary, [string]$NextIntent)
    
    $sessionFile = "current_deepseek_session.json"
    if (Test-Path $sessionFile) {
        $session = Get-Content $sessionFile | ConvertFrom-Json
        
        $session.conversation_summary = $Summary
        $session.next_session_intent = $NextIntent
        $session.end_time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        
        # Archive the session
        $archiveFile = "deepseek_conversation_$($session.session_id).json"
        $session | ConvertTo-Json -Depth 5 | Out-File $archiveFile -Encoding utf8
        
        Remove-Item $sessionFile
        
        Write-Host " CONVERSATION ARCHIVED: $archiveFile" -ForegroundColor Green
        Write-Host " Summary: $Summary" -ForegroundColor Yellow
        Write-Host " Next Intent: $NextIntent" -ForegroundColor Magenta
    }
}

# Export functions for use
Export-ModuleMember -Function Add-ConversationTurn, Show-ConversationFlow, Save-ConversationSummary
