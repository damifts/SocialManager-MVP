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

if [ -f "requirements.txt" ]; then
    print_info "Installazione dipendenze da requirements.txt..."
    
    pip install --upgrade pip setuptools wheel > /dev/null 2>&1
    pip install -r requirements.txt
    
    print_success "Dipendenze installate"
else
    print_error "requirements.txt non trovato"
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
# STEP 5: Mostra menu di avvio
# ============================================================================

print_header "STEP 5: Avvio Applicazione"

echo "Scegli come avviare l'applicazione:"
echo ""
echo -e "  ${CYAN}1️⃣  Avvio completo (Streamlit + Backend)${NC}"
echo -e "  ${CYAN}2️⃣  Solo Streamlit (Frontend)${NC}"
echo -e "  ${CYAN}3️⃣  Solo Backend (API)${NC}"
echo -e "  ${CYAN}4️⃣  Test connessione MongoDB${NC}"
echo -e "  ${CYAN}5️⃣  Esci${NC}"
echo ""

read -p "Seleziona un'opzione (1-5): " choice

case $choice in
    1)
        print_header "Avvio Completo: Streamlit + Backend"
        
        print_info "Il backend sarà disponibile su: http://localhost:8000"
        print_info "Streamlit sarà disponibile su: http://localhost:8501"
        echo ""
        
        echo "Scegli come avviare:"
        echo -e "  ${CYAN}A) In 2 terminali separati (consigliato)${NC}"
        echo -e "  ${CYAN}B) Avvia solo backend, lancio manuale Streamlit${NC}"
        echo ""
        
        read -p "Seleziona (A/B): " launch_choice
        
        if [ "$launch_choice" = "A" ] || [ "$launch_choice" = "a" ]; then
            echo ""
            print_info "Apertura terminali separati..."
            
            # Backend in sfondo
            print_success "Avvio Backend..."
            export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
            python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend &
            BACKEND_PID=$!
            
            sleep 3
            
            # Streamlit nel terminale attuale
            print_success "Avvio Streamlit..."
            python -m streamlit run app.py
            
            # Se Streamlit termina, termina anche Backend
            kill $BACKEND_PID 2>/dev/null || true
        else
            print_warning "Avvio Backend. Apri un altro terminale per Streamlit."
            export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
            python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
        fi
        ;;
    
    2)
        print_header "Avvio Streamlit (Frontend)"
        print_info "Streamlit sarà disponibile su: http://localhost:8501"
        echo ""
        python -m streamlit run app.py
        ;;
    
    3)
        print_header "Avvio Backend (API)"
        print_info "Backend sarà disponibile su: http://localhost:8000"
        print_info "Documentazione API: http://localhost:8000/docs"
        echo ""
        export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
        python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
        ;;
    
    4)
        print_header "Test Connessione MongoDB"
        print_info "Esecuzione test MongoDB..."
        echo ""
        
        if [ -f "tests/verify_mongodb.py" ]; then
            python tests/verify_mongodb.py
        elif [ -f "verify_mongodb.py" ]; then
            python verify_mongodb.py
        else
            print_error "Script verify_mongodb.py non trovato"
        fi
        ;;
    
    5)
        print_info "Uscita"
        exit 0
        ;;
    
    *)
        print_error "Opzione non valida"
        exit 1
        ;;
esac
