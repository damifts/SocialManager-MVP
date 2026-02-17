# Dependency Coordination

Progetto ora full-stack Python con Streamlit. Coordinazione semplificata con un unico `requirements.txt`.

## Installazione (Python)

Dal root del progetto:

```bash
# Crea virtual environment
python -m venv .venv

# Attiva venv
# Windows:
.venv\Scripts\activate
# Unix/macOS:
source .venv/bin/activate

# Installa dipendenze
pip install -r requirements.txt
```

## Dipendenze Principali

**Core:**
- `streamlit` - Framework UI interattivo
- `pydantic` - Validazione dati e schemas
- `python-dotenv` - Gestione variabili env

**AI & Backend:**
- `langchain` - Orchestrazione AI
- `openai` - API OpenAI (o Gemini)
- `motor` - Driver MongoDB async
- `fastapi` + `uvicorn` - API backend (opzionale)

**Visualizzazione:**
- `plotly` - Grafici interattivi
- `pandas` - Manipolazione dati

## Aggiungere Nuove Dipendenze

```bash
# Installa pacchetto
pip install nome-pacchetto

# Aggiorna requirements.txt
pip freeze > requirements.txt
```

**IMPORTANTE**: Specifica versioni esatte per reproducibilità (es: `streamlit==1.40.2`)

## Regole Leggere
- Ogni nuova dipendenza deve avere una motivazione breve in PR
- Verifica la licenza prima di aggiungere librerie nuove
- Mantieni versioni esatte per reproducibilità
- Testa compatibilità prima di aggiornare versioni major
