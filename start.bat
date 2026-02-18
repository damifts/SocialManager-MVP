@echo off
REM ============================================================================
REM SocialManager MVP - Start Script (CMD)
REM ============================================================================
REM Avvia Backend + Frontend in due terminali separati.
REM Uso: start.bat
REM ============================================================================

if not exist .venv\Scripts\activate.bat (
    echo [ERR] Ambiente virtuale non trovato. Esegui prima setup.bat
    exit /b 1
)

echo [INFO] Avvio Backend e Streamlit...

start cmd /k "cd /d %cd% && .venv\Scripts\activate.bat && set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend"

timeout /t 2 /nobreak

start cmd /k "cd /d %cd% && .venv\Scripts\activate.bat && python -m streamlit run app.py"

echo [OK] Backend: http://localhost:8000/docs
echo [OK] Streamlit: http://localhost:8501
