$ErrorActionPreference = 'Stop'

if (-not (Test-Path 'input')) {
    New-Item -ItemType Directory -Path 'input' | Out-Null
}

$python = if (Test-Path '.\.venv\Scripts\python.exe') {
    '.\.venv\Scripts\python.exe'
} else {
    'python'
}

$sampleConfig = 'configs\sample_local.yaml'
Copy-Item 'configs\sample.yaml' $sampleConfig -Force

Write-Host '>>> Running VYT-PIPE sample pipeline...'
& $python -m vyt.cli make $sampleConfig
