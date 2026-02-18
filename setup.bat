@echo off
REM ============================================================================
REM SocialManager MVP - Setup & Launch Script (Batch version)
REM ============================================================================
REM Questo script automatizza installazione e avvio della SocialManager
REM
REM Uso: setup.bat
REM ============================================================================

setlocal enabledelayedexpansion

color 0A
title SocialManager MVP - Setup

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║         SocialManager MVP - Setup & Launch Script              ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM ============================================================================
REM STEP 1: Verifica Python
REM ============================================================================

echo [STEP 1] Verifica Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python non trovato. Installa da https://www.python.org
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ %PYTHON_VERSION% trovato

REM ============================================================================
REM STEP 2: Crea/Attiva ambiente virtuale
REM ============================================================================

echo.
echo [STEP 2] Ambiente Virtuale...

if exist .venv (
    echo ℹ️  Ambiente virtuale già esistente
) else (
    echo Creazione ambiente virtuale...
    python -m venv .venv
    echo ✅ Ambiente virtuale creato
)

call .venv\Scripts\activate.bat
echo ✅ Ambiente virtuale attivato

REM ============================================================================
REM STEP 3: Installa dipendenze
REM ============================================================================

echo.
echo [STEP 3] Installazione Dipendenze...

if exist requirements.txt (
    echo Installazione dipendenze...
    pip install --upgrade pip setuptools wheel >nul 2>&1
    pip install -r requirements.txt
    echo ✅ Dipendenze installate
) else (
    echo ❌ requirements.txt non trovato
    exit /b 1
)

REM ============================================================================
REM STEP 4: Configura .env
REM ============================================================================

echo.
echo [STEP 4] Configurazione Ambiente...

if exist .env (
    echo ✅ File .env trovato
) else (
    echo Creazione file .env...
    (
        echo # MongoDB Configuration
        echo MONGO_URI=mongodb://localhost:27017/socialmanager
        echo.
        echo # Google Gemini Configuration
        echo GOOGLE_API_KEY=your-api-key-here
        echo.
        echo # Environment
        echo ENVIRONMENT=development
    ) > .env
    echo ✅ File .env creato. Modifica i valori nel file!
)

REM ============================================================================
REM STEP 5: Menu Avvio
REM ============================================================================

echo.
echo [STEP 5] Scegli come avviare l'applicazione:
echo.
echo  1 - Avvio completo (Streamlit + Backend)
echo  2 - Solo Streamlit (Frontend)
echo  3 - Solo Backend (API)
echo  4 - Test MongoDB
echo  5 - Esci
echo.

set /p CHOICE="Seleziona (1-5): "

if "%CHOICE%"=="1" (
    echo.
    echo ℹ️  Backend: http://localhost:8000/docs
    echo ℹ️  Streamlit: http://localhost:8501
    echo.
    echo Opzione A^) Avvia in 2 terminali separati (consigliato^)
    echo Opzione B^) Avvia solo backend
    echo.
    set /p LAUNCH="Seleziona (A/B): "
    
    if /i "!LAUNCH!"=="A" (
        echo ✅ Avvio Backend in nuovo terminale...
        start cmd /k "cd /d %cd% && .venv\Scripts\activate.bat && set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend"
        
        timeout /t 3 /nobreak
        
        echo ✅ Avvio Streamlit in nuovo terminale...
        start cmd /k "cd /d %cd% && .venv\Scripts\activate.bat && python -m streamlit run app.py"
        
        echo.
        echo ✨ L'app è in avvio...
        timeout /t 2 /nobreak
        exit /b 0
    ) else (
        set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
        python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
    )
) else if "%CHOICE%"=="2" (
    echo.
    echo ℹ️  Streamlit: http://localhost:8501
    echo.
    python -m streamlit run app.py
) else if "%CHOICE%"=="3" (
    echo.
    echo ℹ️  Backend: http://localhost:8000/docs
    echo.
    set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
    python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
) else if "%CHOICE%"=="4" (
    echo.
    if exist tests\verify_mongodb.py (
        python tests\verify_mongodb.py
    ) else if exist verify_mongodb.py (
        python verify_mongodb.py
    ) else (
        echo ❌ Script verify_mongodb.py non trovato
    )
) else if "%CHOICE%"=="5" (
    exit /b 0
) else (
    echo ❌ Opzione non valida
    exit /b 1
)

pause
