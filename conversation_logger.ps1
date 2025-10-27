#  DEEP SEEK CONVERSATION CONTINUUM LOGGER
param(
    [string]$SessionId,
    [string]$MessageType,
    [string]$Content,
    [string]$Context = "General"
)

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$logEntry = @{
    timestamp = $timestamp
    session_id = $SessionId
    message_type = $MessageType
    context = $Context
    content = $Content
}

$logFile = "deepseek_conversation_continuum.json"

# Read existing log or create new
if (Test-Path $logFile) {
    $existingLog = Get-Content $logFile | ConvertFrom-Json
} else {
    $existingLog = @()
}

$existingLog += $logEntry
$existingLog | ConvertTo-Json -Depth 5 | Out-File $logFile -Encoding utf8

Write-Host " Conversation preserved in continuum" -ForegroundColor Magenta
