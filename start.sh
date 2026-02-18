#!/bin/bash

# ============================================================================
# SocialManager MVP - Start Script (Bash)
# ============================================================================
# Avvia Backend + Frontend. Backend in background.
# Uso: bash start.sh
# ============================================================================

set -e

if [ ! -f ".venv/bin/activate" ]; then
    echo "[ERR] Ambiente virtuale non trovato. Esegui prima: bash setup.sh"
    exit 1
fi

source ".venv/bin/activate"
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

echo "[INFO] Avvio Backend..."
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend &
BACKEND_PID=$!

sleep 2

echo "[INFO] Avvio Streamlit..."
python -m streamlit run app.py

kill $BACKEND_PID 2>/dev/null || true
