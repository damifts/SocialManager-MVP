#!/bin/bash

# ============================================================================
# SocialManager MVP - Setup & Launch Script (Bash version)
# ============================================================================
# Questo script automatizza installazione e avvio per Linux/Mac
#
# Uso: bash setup.sh
# ============================================================================

set -e

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ============================================================================
# Funzioni helper
# ============================================================================

print_header() {
    echo ""
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║ $1${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_info() {
    echo -e "ℹ️  $1"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# ============================================================================
# STEP 1: Verifica prerequisiti
# ============================================================================

print_header "STEP 1: Verifica Prerequisiti"

print_info "Verifica Python 3.8+..."
if ! command -v python3 &> /dev/null; then
    print_error "Python non trovato. Installa Python 3.8 o superiore"
    exit 1
fi
PYTHON_VERSION=$(python3 --version 2>&1)
print_success "Python trovato: $PYTHON_VERSION"

print_info "Verifica pip..."
if ! command -v pip3 &> /dev/null; then
    print_error "pip non trovato"
    exit 1
fi
print_success "pip trovato"

# ============================================================================
# STEP 2: Crea/Attiva ambiente virtuale
# ============================================================================

print_header "STEP 2: Ambiente Virtuale"

VENV_PATH=".venv"

if [ -d "$VENV_PATH" ]; then
    print_info "Ambiente virtuale già esistente: $VENV_PATH"
else
    print_info "Creazione ambiente virtuale..."
    python3 -m venv "$VENV_PATH"
    print_success "Ambiente virtuale creato"
fi

print_info "Attivazione ambiente virtuale..."
source "$VENV_PATH/bin/activate"
print_success "Ambiente virtuale attivato"

# ============================================================================
# STEP 3: Installa dipendenze
# ============================================================================

print_header "STEP 3: Installazione Dipendenze"

if [ -f "requirements-base.txt" ]; then
    print_info "Installazione dipendenze base..."

    pip install --upgrade pip setuptools wheel > /dev/null 2>&1
    pip install -r requirements-base.txt

    if [ "$SM_FULL" = "1" ] && [ -f "requirements-full.txt" ]; then
        print_warning "Installazione FULL: include extras MongoDB/Gemini."
        pip install -r requirements-full.txt
    fi

    print_success "Dipendenze installate"
    print_info "Per extras: SM_FULL=1 bash setup.sh"
else
    print_error "requirements-base.txt non trovato"
    exit 1
fi

# ============================================================================
# STEP 4: Configura variabili d'ambiente
# ============================================================================

print_header "STEP 4: Configurazione Ambiente"

print_info "Verifica file .env..."

if [ ! -f ".env" ]; then
    print_warning "File .env non trovato. Creazione con template..."
    
    cat > .env << EOF
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
EOF
    
    print_success "File .env creato. Modifica i valori con le tue credenziali!"
    print_warning "Aggiungi GOOGLE_API_KEY e altri valori necessari nel file .env"
else
    print_success "File .env trovato"
fi

print_success "Configurazione completata"

# ============================================================================
# STEP 5: Avvio Applicazione
# ============================================================================

print_header "SETUP COMPLETATO"
print_info "Avvio app: bash start.sh"
print_info "Extras opzionali: SM_FULL=1 bash setup.sh"
