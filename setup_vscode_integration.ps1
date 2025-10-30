#  COMPLETE VS CODE INTEGRATION SETUP

Write-Host \"Setting up DeepSeek Enhanced VS Code Environment...\" -ForegroundColor Cyan

# Create necessary directories
$directories = @(\".vscode\", \"scripts\", \"backups\")
foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host \" Created directory: $dir\" -ForegroundColor Green
    }
}

# Verify all files were created
Write-Host \"
 VERIFYING INTEGRATION FILES:\" -ForegroundColor Cyan
$files = Get-ChildItem -Recurse -Include *.json, *.ps1, *.py | Where-Object { 
    $_.Directory.Name -eq \".vscode\" -or $_.Directory.Name -eq \"scripts\" 
}

$files | Format-Table Name, Directory, Length -AutoSize

Write-Host \"
🎯 VS CODE INTEGRATION COMPLETE!\" -ForegroundColor Green
Write-Host \"
Next Steps:\" -ForegroundColor Yellow
Write-Host \"1. Open the project in VS Code\" -ForegroundColor White
Write-Host \"2. The terminal will auto-load the DeepSeek Revolution environment\" -ForegroundColor White
Write-Host \"3. Use commands like 'status', 'start', 'dashboard' in the terminal\" -ForegroundColor White
Write-Host \"4. Access tasks via VS Code Command Palette (Ctrl+Shift+P)\" -ForegroundColor White
Write-Host \"5. Use launch configurations for debugging\" -ForegroundColor White

Write-Host \"
 Your VS Code environment is now DeepSeek Revolution Enhanced!\" -ForegroundColor Magenta
