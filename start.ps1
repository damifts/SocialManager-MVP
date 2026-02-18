# ============================================================================
# SocialManager MVP - Start Script (PowerShell)
# ============================================================================
# Avvia Backend + Frontend in due terminali separati.
# Uso: .\start.ps1
# ============================================================================

$ErrorActionPreference = "Stop"

$venvActivate = ".venv\Scripts\Activate.ps1"
if (-Not (Test-Path $venvActivate)) {
    Write-Host "[ERR] Ambiente virtuale non trovato. Esegui prima .\setup.ps1"
    exit 1
}

Write-Host "[INFO] Avvio Backend e Streamlit..."

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$pwd'; .\.venv\Scripts\Activate.ps1; $env:PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION='python'; python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend"
Start-Sleep -Seconds 2
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$pwd'; .\.venv\Scripts\Activate.ps1; python -m streamlit run app.py"

Write-Host "[OK] Backend: http://localhost:8000/docs"
Write-Host "[OK] Streamlit: http://localhost:8501"
