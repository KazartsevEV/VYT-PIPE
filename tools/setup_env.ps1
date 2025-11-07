$ErrorActionPreference = 'Stop'
Write-Host '>>> Creating venv and installing requirements...'
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install -r requirements.txt

Write-Host '>>> Checking external tools...'
$ink = (Get-Command inkscape -ErrorAction SilentlyContinue)
$ptr = (Get-Command potrace  -ErrorAction SilentlyContinue)
if (-not $ink) { Write-Warning 'Inkscape not found in PATH — EMF export will be disabled (fallback PNG 600 DPI).' }
if (-not $ptr) { Write-Warning 'potrace not found in PATH — vectorization disabled (stub). Install from https://potrace.sourceforge.net/' }

Write-Host 'Done.'
