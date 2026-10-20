$ErrorActionPreference = 'Stop'
winget install --id Git.Git -e --accept-package-agreements --accept-source-agreements
winget install --id Python.Python.3.12 -e --accept-package-agreements --accept-source-agreements
winget install --id Gyan.FFmpeg -e --accept-package-agreements --accept-source-agreements
Write-Host 'Close and reopen PowerShell, then run install-project.ps1'
