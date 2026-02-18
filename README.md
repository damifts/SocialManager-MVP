# 📱 Social Manager - MVP

Piattaforma completa per la **gestione social con automazione AI**. Generazione contenuti ottimizzati per ogni social network con backend Python e interfaccia Streamlit.

## 🎯 Quick Start

### ⚡ Metodo Rapido (Consigliato)

```powershell
# Windows PowerShell
.\setup.ps1

# Oppure Windows CMD
setup.bat

# Oppure Mac/Linux
bash setup.sh
```

**Setup automatico in ~60 secondi:**
- Crea environment virtuale Python
- Installa tutte le dipendenze
- Configura `.env`
- Menu interattivo per avvio app

👉 **[Leggi QUICKSTART.md per guida dettagliata](QUICKSTART.md)**

### Metodo Manuale (Alternativa)

```bash
# 1. Clone e setup
git clone <repo>
cd SocialManager-MVP
python -m venv .venv
.venv\Scripts\activate  # Windows / source .venv/bin/activate (Mac/Linux)

# 2. Installa dipendenze
pip install -r requirements.txt

# 3. Avvia (in due terminali)
streamlit run app.py              # Terminal 1: Frontend (http://localhost:8501)
python -m uvicorn main:app --reload --app-dir backend --port 8000  # Terminal 2: Backend
```

---

## 📋 Indice

- [📱 Quick Start](#-quick-start) ← **Inizia da qui!**
- [🏗️ Architettura](#architettura)
- [⚙️ Setup Automatizzato](#-setup-automatizzato) (Nuovo!)
- [🚀 Setup Completo](#setup-completo)
- [⚙️ Configurazione Servizi](#configurazione-servizi)
- [📌 Issues Predisposte](#issues-predisposte)
- [👥 Team & Responsabilità](#team--responsabilità)
- [💻 Sviluppo](#sviluppo)
- [🔧 Troubleshooting](#troubleshooting)

---

## ⚙️ Setup Automatizzato

### 📖 Guida Rapida per Colleghi

👉 **[VEDI QUICKSTART.md](QUICKSTART.md)** per una guida semplificata e adatta a chi non ha familiarità con il terminale.

### 🤖 Script Disponibili

Abbiamo creato script automatici per tutte le piattaforme:

| Piattaforma | Script | Comando |
|-----------|--------|----------|
| **Windows (PowerShell)** | `setup.ps1` | `.\setup.ps1` |
| **Windows (CMD)** | `setup.bat` | `setup.bat` |
| **Mac/Linux (Bash)** | `setup.sh` | `bash setup.sh` |

### Cosa Fa il Setup Automatico

✅ Verifica Python 3.8+  
✅ Crea ambiente virtuale `.venv`  
✅ Installa dipendenze da `requirements.txt`  
✅ Crea file `.env` con template  
✅ Mostra menu per avvio app  

### Menu Interattivo

Dopo il setup, scegli:

1. **Avvio Completo** → Streamlit + Backend in 2 finestre
2. **Solo Streamlit** → Frontend (http://localhost:8501)
3. **Solo Backend** → API (http://localhost:8000/docs)
4. **Test MongoDB** → Verifica connessione DB
5. **Esci**

---

## 🏗️ Architettura

### Stack Tecnologico
- **Frontend**: Streamlit (Python + UI components)
- **Backend**: FastAPI + Python
- **AI**: Google Gemini API (LangChain optional)
- **Database**: MongoDB (Motor async driver)
- **Charts**: Plotly per analytics
- **Schemas**: Pydantic per validation

### Struttura Progetto
```
SocialManager-MVP/
├── app.py                      # Streamlit app principale
├── requirements.txt            # Python dependencies
├── verify_mongodb.py          # Test MongoDB connection
├── test_gemini.py             # Test Gemini API
├── backend/
│   ├── main.py                # FastAPI app entry
│   ├── ai/
│   │   ├── gemini_config.py   # Gemini setup & auth
│   │   ├── generator.py       # Post generation logic
│   │   └── prompts.py         # System prompts & tones
│   ├── app/
│   │   └── routes.py          # API endpoints
│   ├── dao/
│   │   ├── base_dao.py        # MongoDB CRUD base
│   │   └── post_dao.py        # Post operations
│   ├── database/
│   │   └── connection.py      # MongoDB connection
│   └── schemas/
│       └── post.py            # Pydantic models
└── .env                       # Configuration (create from .env.example)
```

---

## 🚀 Setup Completo

### Prerequisiti
- **Python 3.10+** (3.12+ recommended)
- **MongoDB Community** (local o cloud)
- **Gemini API Key** (Google AI Studio)
- **Git**

### 1️⃣ Clona Repository

```bash
git clone https://github.com/damifts/SocialManager-MVP.git
cd SocialManager-MVP
```

### 2️⃣ Python Environment

```bash
# Crea virtual environment
python -m venv .venv

# Attiva venv
# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate
```

### 3️⃣ Installa Dipendenze

```bash
pip install -r requirements.txt
```

**Dipendenze principali:**
- `streamlit==1.40.2` - Frontend UI
- `fastapi==0.115.0` + `uvicorn==0.30.6` - Backend API
- `pymongo==4.10.1` + `motor==3.7.0` - MongoDB drivers
- `google-generativeai==0.3.2` - Gemini AI
- `pydantic==2.10.5` - Data validation
- `plotly==5.24.1` - Charts
- `python-dotenv==1.0.1` - Environment variables

### 4️⃣ Configurazione Variabili Ambiente

```bash
# Crea .env (da .env.example)
cp .env.example .env
```

**Edita `.env` con:**
```env
# MongoDB
MONGO_URI=mongodb://localhost:27017
MONGO_DB=socialmanager

# Gemini AI
GEMINI_API_KEY=your_api_key_here

# Optional
STREAMLIT_SERVER_PORT=8501
UVICORN_PORT=8000
```

### 5️⃣ Avvia Applicazione

**Terminal 1 - Frontend Streamlit:**
```bash
streamlit run app.py
# Accedi: http://localhost:8501
```

**Terminal 2 - Backend FastAPI:**
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
# Swagger API: http://localhost:8000/docs
```

---

## ⚙️ Configurazione Servizi

### MongoDB Setup

#### Windows
1. Download [MongoDB Community MSI](https://www.mongodb.com/try/download/community)
2. Installa con default settings (MongoDB Community Server)
3. MongoDB parte automaticamente come servizio
4. Verifica: `mongod --version`

#### Mac
```bash
brew install mongodb-community
brew services start mongodb-community

# Verifica
mongo --version
```

#### Linux (Ubuntu/Debian)
```bash
# Importa GPG key
curl https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Aggiungi repo
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Installa
sudo apt-get update
sudo apt-get install mongodb-org

# Avvia
sudo systemctl start mongod
```

### Gemini AI Setup

1. Vai su [Google AI Studio](https://aistudio.google.com/)
2. Clicca "Get API Key" → "Create API key in new project"
3. Copy API key in `.env`:
   ```env
   GEMINI_API_KEY=sk-xxx...
   ```

### Verifica Connessioni

```bash
# Test MongoDB
python verify_mongodb.py
# Output atteso: ✅ Connected! Status: {...}

# Test Gemini AI
python test_gemini.py
# Output atteso: ✅ Working! Message: "Hello..."
```

---

## 📌 Issues Predisposte

### Backend - Database (Issues #5, #11, #17-25)

| Issue | Descrizione | File | Status |
|-------|------------|------|--------|
| #5 | Struttura backend | `backend/` | ✅ |
| #11 | MongoDB local test | `verify_mongodb.py` | ✅ |
| #17-18 | DB connection | `backend/database/connection.py` | ✅ |
| #19 | Query test | `verify_mongodb.py` | ✅ |
| #20-21 | DAO CRUD base | `backend/dao/base_dao.py` | ✅ |
| #22 | READ operations | `BaseDAO.find_one/many()` | ✅ |
| #23-24 | UPDATE/DELETE | `BaseDAO.update(), delete()` | ✅ |

### Frontend - Streamlit (Issues #7-9)

| Issue | Descrizione | Location | Status |
|-------|------------|----------|--------|
| #7 | Sidebar navigation | `app.py` (line 80-110) | ✅ |
| #8 | Page bodies | `app.py` (Home/Genera/Calendar/Analytics) | ✅ |
| #9 | Header per page | `st.title()` + `st.markdown()` | ✅ |

### AI - Gemini Integration (Issues #6, #10, #12, #15-16)

| Issue | Descrizione | File | Status |
|-------|------------|------|--------|
| #6 | AI model GUI | `app.py` (Genera Post) | 🟡 Mock |
| #10 | Toni/istanze | `backend/ai/prompts.py` | ✅ |
| #12 | Generazione post | `backend/ai/generator.py` | 🟡 Stub |
| #15 | Setup Gemini | `backend/ai/gemini_config.py` | ✅ |
| #16 | Image generation | `backend/ai/generator.py` | 🔴 TODO |

---

## 👥 Team & Responsabilità

### Core & DevOps (Damiano, Daniele, Davide)
- ✅ Repository setup & CI/CD
- ✅ Environment configuration
- ✅ Monorepo management

### Backend & AI (Andrea, Alessio M., Filippo, Danilo)
- ✅ FastAPI endpoints
- 🟡 Gemini integration (in progress)
- 🔴 LinkedIn API integration (future)
- ✅ MongoDB schema & DAO

### Frontend (Thomas, Patrick, Mohamed, Alessandro, Cristian P.)
- ✅ Streamlit UI structure
- 🟡 Calendar view (Thomas)
- 🟡 Analytics dashboard (Danilo)
- 🟡 Post editor (Patrick)

### Strategy & QA (Alessio, Cristian V.)
- Requisiti & validazione
- Testing & QA
- PM & roadmap

---

## 💻 Sviluppo

### Aggiungere Nuova Feature

1. **Crea branch**
   ```bash
   git checkout -b feature/issue-XX-description
   ```

2. **Sviluppa feature**
   - Frontend: modifica `app.py` per UI
   - Backend: aggiungi logica in `backend/`
   - Schemas: define models in `backend/schemas/`

3. **Test locali**
   ```bash
   # Verifica sintassi
   python -m py_compile backend/module.py
   
   # Run app
   streamlit run app.py
   ```

4. **Push & PR**
   ```bash
   git add .
   git commit -m "fix: issue #XX - description"
   git push origin feature/issue-XX
   ```

### File Importanti

| File | Responsabilità |
|------|---|
| `app.py` | Streamlit UI (pages + sidebar) |
| `backend/main.py` | FastAPI entry point |
| `backend/ai/prompts.py` | System prompts per toni |
| `backend/dao/base_dao.py` | MongoDB CRUD operations |
| `.venv/` | Python virtual environment |
| `.env` | Configuration (DON'T commit!) |

### Comandi Utili

```bash
# Verifica sintassi Python
python -m py_compile app.py

# Format codice
pip install black
black app.py backend/

# Linting
pip install pylint
pylint app.py

# Run tests
pytest backend/tests/

# Clean cache
rm -rf .streamlit/__pycache__ backend/__pycache__
```

---

## 🔧 Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'streamlit'"
```bash
# Assicurati che venv sia attivo
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Reinstalla
pip install -r requirements.txt
```

### ❌ "ConnectionFailure: MongoDB connection error"
```bash
# Verifica MongoDB sia avviato
python verify_mongodb.py

# Windows: Check Task Manager → Services → MongoDB
# Mac: brew services list
# Linux: sudo systemctl status mongod
```

### ❌ "TypeError: Metaclasses with custom tp_new are not supported" (Python 3.14)
```bash
# Fix: Set environment variable
$env:PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION="python"

# Oppure aggiungi in .env:
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```

### ❌ "Gemini API Error: 403 Permission Denied"
```bash
# Verifica GEMINI_API_KEY in .env
# Rigenerato la key da Google AI Studio
python test_gemini.py
```

### ❌ Streamlit Hot Reload non funziona
```bash
# Streamlit monitor file changes automaticamente
# Se non funziona: riavvia
streamlit run app.py

# O disabilita cache
import streamlit as st
st.set_page_config(cache_resource_ttl=0)
```

---

## 📚 Linee Guida Sviluppo

### Setup Progetto
- **Per Team Members**: Usa script automatico (`setup.ps1`, `setup.bat`, `setup.sh`)
- **Per Developers**: Leggi [Sviluppo → Aggiungere Nuova Feature](#aggiungere-nuova-feature)
- **Guida Rapida**: [QUICKSTART.md](QUICKSTART.md)

### Style Guide
- **Python**: PEP 8 (use `black` formatter)
- **Commits**: Conventional Commits (`fix:`, `feat:`, `docs:`)
- **Branches**: `feature/`, `bugfix/`, `docs/`

### Testing
- Unit tests in `backend/tests/`
- Test database queries con `pytest`
- Test Gemini con `test_gemini.py`
- Usa `python verify_mongodb.py` per test MongoDB

### Documentation
- README aggiornato ad ogni major release
- QUICKSTART.md per onboarding team members
- Docstrings in tutte le funzioni
- Issues linkate nei commits

---

## 📖 Documentazione Progetto

### 🚀 Per Iniziare
- **[QUICKSTART.md](QUICKSTART.md)** - Guida rapida per nuovi team members
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Come contribuire

### 📚 Approfondimenti
- **[docs/API.md](docs/API.md)** - Documentazione API FastAPI
- **[docs/BACKEND.md](docs/BACKEND.md)** - Architettura backend
- **[docs/DATABASE.md](docs/DATABASE.md)** - Schema MongoDB
- **[docs/INDEX.md](docs/INDEX.md)** - Hub documentazione centralizzato
- **[scripts/README.md](scripts/README.md)** - DevOps & webhook testing

### 🔗 Risorse Esterne
- [Streamlit Docs](https://docs.streamlit.io/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [MongoDB Python Docs](https://pymongo.readthedocs.io/)
- [Google AI Studio](https://aistudio.google.com/)

---

## 📄 License

MIT License - Vedi [LICENSE](LICENSE)

---

## 🤝 Contribuire

Leggi [CONTRIBUTING.md](CONTRIBUTING.md) per le linee guida complete.

**Tl;dr**:
1. Fork il repo
2. Crea branch `feature/issue-XX`
3. Commit con Conventional Commits
4. Push e apri PR con descrizione

---

**Versione**: 0.3.0 (MVP + DevOps)  
**Team**: ITS Angelo Rizzoli - MOD-10 Laboratorio d'Impresa  
**Setup Scripts**: ✅ PowerShell | ✅ Batch | ✅ Bash  
**Last Updated**: Feb 18, 2026
