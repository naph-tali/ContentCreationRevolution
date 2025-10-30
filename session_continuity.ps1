#  DEEP SEEK SESSION CONTINUITY MANAGER

function New-DeepSeekSession {
    param([string]$SessionTheme)
    
    $sessionId = "DEEPSEEK_" + (Get-Date -Format "yyyyMMdd_HHmmss")
    $sessionData = @{
        session_id = $sessionId
        start_time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        theme = $SessionTheme
        conversation_count = 0
        breakthroughs = @()
        challenges = @()
        next_session_agenda = @()
    }
    
    $sessionFile = "current_session.json"
    $sessionData | ConvertTo-Json -Depth 5 | Out-File $sessionFile -Encoding utf8
    
    # Log session start
    .\conversation_logger.ps1 -SessionId $sessionId -MessageType "SESSION_START" -Content "New DeepSeek session: $SessionTheme"
    
    Write-Host "🌌 NEW DEEP SEEK SESSION: $sessionId" -ForegroundColor Cyan
    Write-Host "🎯 Theme: $SessionTheme" -ForegroundColor Yellow
    
    return $sessionId
}

function Add-ConversationEntry {
    param(
        [string]$SessionId,
        [string]$Speaker,
        [string]$Message,
        [string]$Context = "Development"
    )
    
    $sessionFile = "current_session.json"
    if (Test-Path $sessionFile) {
        $sessionData = Get-Content $sessionFile | ConvertFrom-Json
        $sessionData.conversation_count += 1
        
        # Add to conversation continuum
        $conversationEntry = @{
            timestamp = Get-Date -Format "HH:mm:ss"
            speaker = $Speaker
            message = $Message
            context = $Context
        }
        
        if (-not $sessionData.PSObject.Properties['conversation_entries']) {
            $sessionData | Add-Member -NotePropertyName "conversation_entries" -NotePropertyValue @()
        }
        $sessionData.conversation_entries += $conversationEntry
        
        $sessionData | ConvertTo-Json -Depth 5 | Out-File $sessionFile -Encoding utf8
    }
    
    # Also log to main continuum
    .\conversation_logger.ps1 -SessionId $SessionId -MessageType "CONVERSATION" -Content "$Speaker: $Message" -Context $Context
}

function Add-Breakthrough {
    param(
        [string]$SessionId,
        [string]$Breakthrough,
        [string]$Impact = "Significant"
    )
    
    $sessionFile = "current_session.json"
    if (Test-Path $sessionFile) {
        $sessionData = Get-Content $sessionFile | ConvertFrom-Json
        
        $breakthroughEntry = @{
            timestamp = Get-Date -Format "HH:mm:ss"
            breakthrough = $Breakthrough
            impact = $Impact
        }
        
        $sessionData.breakthroughs += $breakthroughEntry
        $sessionData | ConvertTo-Json -Depth 5 | Out-File $sessionFile -Encoding utf8
    }
    
    .\conversation_logger.ps1 -SessionId $SessionId -MessageType "BREAKTHROUGH" -Content $Breakthrough -Context $Impact
    Write-Host " BREAKTHROUGH RECORDED: $Breakthrough" -ForegroundColor Green
}

function End-DeepSeekSession {
    param([string]$SessionId, [string]$Summary, [array]$NextAgenda)
    
    $sessionFile = "current_session.json"
    if (Test-Path $sessionFile) {
        $sessionData = Get-Content $sessionFile | ConvertFrom-Json
        
        $sessionData.end_time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $sessionData.summary = $Summary
        $sessionData.next_session_agenda = $NextAgenda
        
        # Archive session
        $archiveFile = "session_$SessionId.json"
        $sessionData | ConvertTo-Json -Depth 5 | Out-File $archiveFile -Encoding utf8
        
        Remove-Item $sessionFile
        
        .\conversation_logger.ps1 -SessionId $SessionId -MessageType "SESSION_END" -Content "Session completed: $Summary"
        
        Write-Host " DEEP SEEK SESSION COMPLETED: $SessionId" -ForegroundColor Cyan
        Write-Host " Summary: $Summary" -ForegroundColor Yellow
        Write-Host " Next Session Agenda: $($NextAgenda -join ', ')" -ForegroundColor Magenta
    }
}

function Show-ConversationContinuum {
    $logFile = "deepseek_conversation_continuum.json"
    if (Test-Path $logFile) {
        $continuum = Get-Content $logFile | ConvertFrom-Json
        
        Write-Host "
 DEEP SEEK CONVERSATION CONTINUUM" -ForegroundColor Cyan
        Write-Host "=" * 60 -ForegroundColor Cyan
        
        $sessions = $continuum | Group-Object session_id
        Write-Host "Total Sessions: $($sessions.Count)" -ForegroundColor Yellow
        Write-Host "Total Entries: $($continuum.Count)" -ForegroundColor Yellow
        
        $continuum | Select-Object -Last 10 | ForEach-Object {
            $color = if ($_.message_type -eq "BREAKTHROUGH") { "Green" } 
                     elseif ($_.message_type -eq "SESSION_START") { "Cyan" }
                     else { "White" }
            Write-Host "[$($_.timestamp)] [$($_.message_type)] $($_.content)" -ForegroundColor $color
        }
    } else {
        Write-Host "No conversation continuum found - starting fresh!" -ForegroundColor Yellow
    }
}
