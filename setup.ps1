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
    Write-Host "╔════════════════════════════════════════════════════════════════╗" @Cyan
    Write-Host "║ $($Text.PadRight(62)) ║" @Cyan
    Write-Host "╚════════════════════════════════════════════════════════════════╝" @Cyan
    Write-Host ""
}

function Write-Info {
    param([string]$Text)
    Write-Host "ℹ️  $Text"
}

function Write-Success {
    param([string]$Text)
    Write-Host "✅ $Text" @Green
}

function Write-Error-Custom {
    param([string]$Text)
    Write-Host "❌ $Text" @Red
}

function Write-Warning-Custom {
    param([string]$Text)
    Write-Host "⚠️  $Text" @Yellow
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
    Write-Info "Ambiente virtuale già esistente: $venvPath"
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

if (Test-Path "requirements.txt") {
    Write-Info "Installazione dipendenze da requirements.txt..."
    $startTime = Get-Date
    
    pip install --upgrade pip setuptools wheel | Out-Null
    pip install -r requirements.txt
    
    $duration = (Get-Date) - $startTime
    Write-Success "Dipendenze installate in $($duration.TotalSeconds.ToString("F1")) secondi"
} else {
    Write-Error-Custom "requirements.txt non trovato"
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
# STEP 5: Mostra istruzioni di avvio
# ============================================================================

Write-Header "STEP 5: Avvio Applicazione"

Write-Host "Scegli come avviare l'applicazione:" @Yellow
Write-Host ""
Write-Host "  1️⃣  Avvio completo (Streamlit + Backend)" -ForegroundColor Cyan
Write-Host "  2️⃣  Solo Streamlit (Frontend)" -ForegroundColor Cyan
Write-Host "  3️⃣  Solo Backend (API)" -ForegroundColor Cyan
Write-Host "  4️⃣  Test connessione MongoDB" -ForegroundColor Cyan
Write-Host "  5️⃣  Esci" -ForegroundColor Cyan
Write-Host ""

$choice = Read-Host "Seleziona un'opzione (1-5)"

switch ($choice) {
    "1" {
        Write-Header "Avvio Completo: Streamlit + Backend"
        
        Write-Info "Il backend sarà disponibile su: http://localhost:8000"
        Write-Info "Streamlit sarà disponibile su: http://localhost:8501"
        Write-Host ""
        
        Write-Host "Scegli come avviare:" @Yellow
        Write-Host "  A) In 2 terminali separati (consigliato)" -ForegroundColor Cyan
        Write-Host "  B) Avvia solo backend, lancio manuale Streamlit" -ForegroundColor Cyan
        Write-Host ""
        
        $launchChoice = Read-Host "Seleziona (A/B)"
        
        if ($launchChoice -eq "A" -or $launchChoice -eq "a") {
            Write-Host ""
            Write-Info "Apertura terminali separati..."
            
            # Backend in nuovo terminale
            Write-Success "Avvio Backend..."
            Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$pwd'; .\.venv\Scripts\Activate.ps1; $env:PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION='python'; python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend"
            
            Start-Sleep -Seconds 3
            
            # Streamlit in nuovo terminale
            Write-Success "Avvio Streamlit..."
            Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$pwd'; .\.venv\Scripts\Activate.ps1; python -m streamlit run app.py"
            
            Write-Host ""
            Write-Success "✨ Molti saluti! L'app è in avvio..."
            Write-Info "Backend: http://localhost:8000/docs"
            Write-Info "Streamlit: http://localhost:8501"
        } else {
            Write-Host ""
            Write-Info "Avvio Backend..."
            $env:PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION = "python"
            python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
        }
    }
    
    "2" {
        Write-Header "Avvio Streamlit (Frontend)"
        Write-Info "Streamlit sarà disponibile su: http://localhost:8501"
        Write-Host ""
        python -m streamlit run app.py
    }
    
    "3" {
        Write-Header "Avvio Backend (API)"
        Write-Info "Backend sarà disponibile su: http://localhost:8000"
        Write-Info "Documentazione API: http://localhost:8000/docs"
        Write-Host ""
        $env:PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION = "python"
        python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
    }
    
    "4" {
        Write-Header "Test Connessione MongoDB"
        Write-Info "Esecuzione test MongoDB..."
        Write-Host ""
        
        if (Test-Path "verify_mongodb.py") {
            python verify_mongodb.py
        } elseif (Test-Path "tests/verify_mongodb.py") {
            python tests/verify_mongodb.py
        } else {
            Write-Error-Custom "Script verify_mongodb.py non trovato"
        }
    }
    
    "5" {
        Write-Info "Uscita"
        exit 0
    }
    
    default {
        Write-Error-Custom "Opzione non valida"
        exit 1
    }
}
