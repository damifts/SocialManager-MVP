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
echo ================================================================
echo   SocialManager MVP - Setup ^& Launch Script
echo ================================================================
echo.

REM ============================================================================
REM STEP 1: Verifica Python
REM ============================================================================

echo [STEP 1] Verifica Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERR] Python non trovato. Installa da https://www.python.org
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK]  %PYTHON_VERSION% trovato

REM ============================================================================
REM STEP 2: Crea/Attiva ambiente virtuale
REM ============================================================================

echo.
echo [STEP 2] Ambiente Virtuale...

if exist .venv (
    echo [INFO] Ambiente virtuale gia esistente
) else (
    echo Creazione ambiente virtuale...
    python -m venv .venv
    echo [OK]  Ambiente virtuale creato
)

call .venv\Scripts\activate.bat
echo [OK]  Ambiente virtuale attivato

REM ============================================================================
REM STEP 3: Installa dipendenze
REM ============================================================================

echo.
echo [STEP 3] Installazione Dipendenze...

if exist requirements-base.txt (
    echo Installazione dipendenze base...
    python -m pip install --upgrade pip setuptools wheel >nul 2>&1
    python -m pip install -r requirements-base.txt
    if /i "%SM_FULL%"=="1" if exist requirements-full.txt (
        echo [WARN] Installazione FULL: include extras MongoDB/Gemini.
        python -m pip install -r requirements-full.txt
    )
    echo [OK]  Dipendenze installate
    echo [INFO] Per extras: set SM_FULL=1 ^& setup.bat
) else (
    echo [ERR] requirements-base.txt non trovato
    exit /b 1
)

REM ============================================================================
REM STEP 4: Configura .env
REM ============================================================================

echo.
echo [STEP 4] Configurazione Ambiente...

if exist .env (
    echo [OK]  File .env trovato
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
    echo [OK]  File .env creato. Modifica i valori nel file!
)

REM ============================================================================
REM STEP 5: Avvio Applicazione
REM ============================================================================

echo.
echo [DONE] Setup completato.
echo [INFO] Avvio app: start.bat
echo [INFO] Extras opzionali: set SM_FULL=1 ^& setup.bat
exit /b 0
