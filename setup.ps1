# ============================================================================
# SocialManager MVP - Setup & Launch Script
# ============================================================================
# Questo script automatizza:
# 1. Creazione dell'ambiente virtuale Python
# 2. Installazione dipendenze
# 3. Configurazione variabili d'ambiente
# 4. Avvio dell'app (Streamlit + Backend)
#
# Uso: .\setup.ps1
# ============================================================================

$ErrorActionPreference = "Stop"

# Colori per output
$Green = @{ ForegroundColor = "Green" }
$Yellow = @{ ForegroundColor = "Yellow" }
$Red = @{ ForegroundColor = "Red" }
$Cyan = @{ ForegroundColor = "Cyan" }

function Write-Header {
    param([string]$Text)
    Write-Host ""
    Write-Host "================================================================" @Cyan
    Write-Host " $Text" @Cyan
    Write-Host "================================================================" @Cyan
    Write-Host ""
}

function Write-Info {
    param([string]$Text)
    Write-Host "[INFO] $Text"
}

function Write-Success {
    param([string]$Text)
    Write-Host "[OK]  $Text" @Green
}

function Write-Error-Custom {
    param([string]$Text)
    Write-Host "[ERR] $Text" @Red
}

function Write-Warning-Custom {
    param([string]$Text)
    Write-Host "[WARN] $Text" @Yellow
}

# ============================================================================
# STEP 1: Verifica prerequisiti
# ============================================================================

Write-Header "STEP 1: Verifica Prerequisiti"

Write-Info "Verifica Python 3.8+..."
try {
    $pythonVersion = python --version 2>&1
    Write-Success "Python trovato: $pythonVersion"
} catch {
    Write-Error-Custom "Python non trovato. Installa Python 3.8 o superiore da https://www.python.org"
    exit 1
}

Write-Info "Verifica pip..."
try {
    $pipVersion = pip --version 2>&1
    Write-Success "pip trovato: $pipVersion"
} catch {
    Write-Error-Custom "pip non trovato."
    exit 1
}

# ============================================================================
# STEP 2: Crea/Attiva ambiente virtuale
# ============================================================================

Write-Header "STEP 2: Ambiente Virtuale"

$venvPath = ".venv"

if (Test-Path $venvPath) {
    Write-Info "Ambiente virtuale gia esistente: $venvPath"
} else {
    Write-Info "Creazione ambiente virtuale..."
    python -m venv $venvPath
    Write-Success "Ambiente virtuale creato"
}

Write-Info "Attivazione ambiente virtuale..."
& "$venvPath\Scripts\Activate.ps1"
Write-Success "Ambiente virtuale attivato"

# ============================================================================
# STEP 3: Installa dipendenze
# ============================================================================

Write-Header "STEP 3: Installazione Dipendenze"

$baseReq = "requirements-base.txt"
$fullReq = "requirements-full.txt"

if (Test-Path $baseReq) {
    Write-Info "Installazione dipendenze base..."
    $startTime = Get-Date

    python -m pip install --upgrade pip setuptools wheel | Out-Null
    python -m pip install -r $baseReq

    if ($env:SM_FULL -eq "1" -and (Test-Path $fullReq)) {
        Write-Warning-Custom "Installazione FULL: include extras MongoDB/Gemini."
        python -m pip install -r $fullReq
    }

    $duration = (Get-Date) - $startTime
    Write-Success "Dipendenze installate in $($duration.TotalSeconds.ToString("F1")) secondi"
    Write-Info "Per extras: SM_FULL=1 .\setup.ps1"
} else {
    Write-Error-Custom "requirements-base.txt non trovato"
    exit 1
}

# ============================================================================
# STEP 4: Configura variabili d'ambiente
# ============================================================================

Write-Header "STEP 4: Configurazione Ambiente"

Write-Info "Verifica file .env..."

if (-Not (Test-Path ".env")) {
    Write-Warning-Custom "File .env non trovato. Creazione con template..."
    
    $envTemplate = @"
# MongoDB Configuration
MONGO_URI=mongodb://localhost:27017/socialmanager

# Google Gemini Configuration
GOOGLE_API_KEY=your-api-key-here

# Environment
ENVIRONMENT=development

# Server Configuration
API_HOST=0.0.0.0
API_PORT=8000
STREAMLIT_PORT=8501
"@
    
    $envTemplate | Out-File -Encoding UTF8 ".env"
    Write-Success "File .env creato. Modifica i valori con le tue credenziali!"
    Write-Warning-Custom "Aggiungi GOOGLE_API_KEY e altri valori necessari nel file .env"
} else {
    Write-Success "File .env trovato"
}

Write-Success "Configurazione completata"

# ============================================================================
# STEP 5: Avvio Applicazione
# ============================================================================

Write-Header "SETUP COMPLETATO"
Write-Info "Avvio app (PowerShell): .\start.ps1"
Write-Info "Avvio app (CMD): start.bat"
Write-Info "Extras opzionali: SM_FULL=1 .\setup.ps1"
