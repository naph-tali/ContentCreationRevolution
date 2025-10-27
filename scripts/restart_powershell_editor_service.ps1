# Safely find and optionally terminate PowerShell Editor Services / pwsh processes used by the VS Code PowerShell extension.

param(
    [switch]$Force
)

Write-Host "Searching for PowerShell Editor Services / pwsh processes..." -ForegroundColor Cyan

# Look for known process names or command lines referencing PowerShellEditorServices
$pses = Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
    Where-Object {
        ($_.Name -like '*PowerShellEditorServices*') -or
        ($_.CommandLine -and $_.CommandLine -match 'PowerShellEditorServices') -or
        ($_.Name -ieq 'pwsh.exe' -and ($_.CommandLine -and $_.CommandLine -match 'PowerShellEditorServices'))
    } | Select-Object ProcessId, Name, CommandLine

if (-not $pses -or $pses.Count -eq 0) {
    Write-Host "No PowerShell Editor Services processes detected." -ForegroundColor Yellow
    Write-Host "If you still see 'Connection to PowerShell Editor Services was closed', try: Reload Window in VS Code (Developer: Reload Window) or restart VS Code." -ForegroundColor Gray
    return
}

Write-Host "`nFound the following candidate processes:`n" -ForegroundColor Cyan
$pses | ForEach-Object {
    Write-Host (" PID: {0}  Name: {1}" -f $_.ProcessId, $_.Name) -ForegroundColor White
    if ($_.CommandLine) {
        Write-Host ("    Cmd: {0}" -f ($_.CommandLine.Length -gt 200 ? ($_.CommandLine.Substring(0,200) + '...') : $_.CommandLine)) -ForegroundColor DarkGray
    }
}

if (-not $Force) {
    $confirm = Read-Host "`nTerminate these processes? Type 'yes' to confirm"
    if ($confirm -ne 'yes') {
        Write-Host "Aborted. No processes were terminated." -ForegroundColor Yellow
        Write-Host "Tip: In VS Code run: Developer: Reload Window" -ForegroundColor Gray
        return
    }
}

foreach ($p in $pses) {
    try {
        Stop-Process -Id $p.ProcessId -Force -ErrorAction Stop
        Write-Host ("Terminated PID {0} ({1})" -f $p.ProcessId, $p.Name) -ForegroundColor Green
    } catch {
        Write-Host ("Failed to terminate PID {0}: {1}" -f $p.ProcessId, $_.Exception.Message) -ForegroundColor Red
    }
}

Write-Host "`nDone. Please reload VS Code: Developer: Reload Window (or close and re-open VS Code) to restart the PowerShell extension." -ForegroundColor Cyan
Write-Host "If problems persist, ensure the PowerShell extension is installed and up-to-date, and that your workspace PowerShellSettings are valid." -ForegroundColor Gray
