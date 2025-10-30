#  DEEP SEEK CONVERSATION CONTINUUM DASHBOARD

function Show-ContinuumDashboard {
    Clear-Host
    Write-Host "

 DEEP SEEK CONVERSATION CONTINUUM DASHBOARD" -ForegroundColor Cyan
    Write-Host "=" * 70 -ForegroundColor Cyan
    
    # Load current session
    $currentSession = if (Test-Path "current_session.json") { 
        Get-Content "current_session.json" | ConvertFrom-Json 
    } else { $null }
    
    # Load continuum
    $continuum = if (Test-Path "deepseek_conversation_continuum.json") {
        Get-Content "deepseek_conversation_continuum.json" | ConvertFrom-Json
    } else { @() }
    
    # Display current session
    if ($currentSession) {
        Write-Host "
🌌 CURRENT DEEP SEEK SESSION" -ForegroundColor Yellow
        Write-Host "   Session ID: $($currentSession.session_id)" -ForegroundColor White
        Write-Host "   Theme: $($currentSession.theme)" -ForegroundColor White
        Write-Host "   Start Time: $($currentSession.start_time)" -ForegroundColor White
        Write-Host "   Conversations: $($currentSession.conversation_count)" -ForegroundColor White
        Write-Host "   Breakthroughs: $($currentSession.breakthroughs.Count)" -ForegroundColor Green
        
        if ($currentSession.breakthroughs) {
            Write-Host "
   Recent Breakthroughs:" -ForegroundColor Yellow
            $currentSession.breakthroughs | Select-Object -Last 3 | ForEach-Object {
                Write-Host "    $($_.breakthrough)" -ForegroundColor Green
            }
        }
    }
    
    # Display continuum statistics
    Write-Host "
 CONVERSATION CONTINUUM STATISTICS" -ForegroundColor Yellow
    if ($continuum) {
        $sessions = $continuum | Group-Object session_id
        $totalEntries = $continuum.Count
        $breakthroughs = $continuum | Where-Object { $_.message_type -eq "BREAKTHROUGH" }
        
        Write-Host "   Total Sessions: $($sessions.Count)" -ForegroundColor White
        Write-Host "   Total Entries: $totalEntries" -ForegroundColor White
        Write-Host "   Breakthroughs: $($breakthroughs.Count)" -ForegroundColor Green
        Write-Host "   First Entry: $($continuum[0].timestamp)" -ForegroundColor White
        Write-Host "   Last Entry: $($continuum[-1].timestamp)" -ForegroundColor White
    } else {
        Write-Host "   No continuum data yet - begin a DeepSeek session!" -ForegroundColor Yellow
    }
    
    # Recent activity
    Write-Host "
 RECENT ACTIVITY" -ForegroundColor Yellow
    if ($continuum) {
        $continuum | Select-Object -Last 10 | ForEach-Object {
            $icon = switch ($_.message_type) {
                "SESSION_START" { "" }
                "BREAKTHROUGH" { "" }
                "SESSION_END" { "" }
                default { "" }
            }
            Write-Host "   $icon [$($_.timestamp)] $($_.content)" -ForegroundColor White
        }
    }
}

function Start-ContinuumEngine {
    Write-Host "
 STARTING TRANSCENDENTAL CONTINUUM ENGINE..." -ForegroundColor Green
    .\venv\Scripts\Activate.ps1
    python transcendental_engine_continuum.py
}

function Show-ContinuumHistory {
    Write-Host "
 FULL CONVERSATION CONTINUUM HISTORY" -ForegroundColor Cyan
    Write-Host "=" * 70 -ForegroundColor Cyan
    
    $continuum = if (Test-Path "deepseek_conversation_continuum.json") {
        Get-Content "deepseek_conversation_continuum.json" | ConvertFrom-Json
    } else { @() }
    
    $continuum | ForEach-Object {
        $color = switch ($_.message_type) {
            "SESSION_START" { "Cyan" }
            "BREAKTHROUGH" { "Green" }
            "SESSION_END" { "Yellow" }
            "CONVERSATION" { "White" }
            default { "Gray" }
        }
        Write-Host "[$($_.timestamp)] [$($_.message_type)] $($_.content)" -ForegroundColor $color
    }
}

# Main dashboard loop
while ($true) {
    Show-ContinuumDashboard
    
    Write-Host "
 CONTINUUM CONTROLS" -ForegroundColor Magenta
    Write-Host "1. Start Transcendental Continuum Engine" -ForegroundColor Yellow
    Write-Host "2. View Full Continuum History" -ForegroundColor Yellow
    Write-Host "3. Refresh Dashboard" -ForegroundColor Yellow
    Write-Host "4. Exit" -ForegroundColor Yellow
    
    $choice = Read-Host "
Select option"
    
    switch ($choice) {
        "1" { Start-ContinuumEngine }
        "2" { Show-ContinuumHistory; Read-Host "Press Enter to continue" }
        "3" { continue }
        "4" { 
            Write-Host "
 Preserving conversation continuum... Goodbye!" -ForegroundColor Cyan
            break 
        }
        default { Write-Host "Invalid option" -ForegroundColor Red }
    }
}
