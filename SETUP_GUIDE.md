# 📋 SETUP GUIDE - Issues Predisposte

Questa guida mostra come configurare il progetto per tutte le issue #5-#25.

---

## 🎯 Issues Predisposte nel Progetto

### ✅ Backend - MongoDB (Issues #5, #11, #17-#25)
- **#5**: Preparazione ambiente backend → `backend/` structure
- **#11**: Verificare MongoDB locale → `verify_mongodb.py`
- **#17**: Collegamento DB → `backend/database/connection.py`
- **#18**: Connessione MongoDB → `backend/database/connection.py`
- **#19**: Test ping/query → `verify_mongodb.py`
- **#16, #20**: Creazione DAO → `backend/dao/base_dao.py`
- **#21**: INSERT documenti → `BaseDAO.insert_one/many()`
- **#22**: READ documenti → `BaseDAO.find_one/many()`
- **#23**: UPDATE documenti → `BaseDAO.update_one/many()`
- **#24, #25**: DELETE documenti → `BaseDAO.delete_one/many()`

### ✅ Backend - Gemini AI (Issues #6, #10, #12, #15, #16)
- **#15**: Gemini Setup → `backend/ai/gemini_config.py`
- **#10, #13**: Prompt e ruolo agente → `backend/ai/prompts.py`
- **#12**: Generazione Post → `backend/ai/generator.py`
- **#6**: Model AI per GUI → Integrato in `app.py`
- **#16**: Generazione immagini → Stub in `generator.py`

### ✅ Frontend - Streamlit (Issues #7, #8, #9)
- **#7**: Sidebar → Implementata in `app.py` (linea ~80-110)
- **#8**: Body → Sezioni separate per ogni page
- **#9**: Header → Header per ogni page con titoli e descrizioni

---

## 🚀 Installazione e Setup

### 1. Prerequisiti

```bash
# Python 3.10+
python --version

# MongoDB Community Server
# Download: https://www.mongodb.com/try/download/community
```

### 2. Clone e Dipendenze

```bash
# Clone repo
git clone https://github.com/damifts/SocialManager-MVP.git
cd SocialManager-MVP

# Virtual environment
python -m venv .venv

# Attiva venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

**requirements.txt include:**
- `motor` + `pymongo` per MongoDB
- `google-generativeai` per Gemini AI
- `streamlit` per UI
- Tutti i moduli necessari

---

## 🔧 Configurazione

### Issue #11, #18: Setup MongoDB

1. **Installa MongoDB localmente**
   - Windows: [Download MSI](https://www.mongodb.com/try/download/community)
   - Mac: `brew install mongodb-community`
   - Linux: Segui [docs ufficiali](https://www.mongodb.com/docs/manual/installation/)

2. **Avvia MongoDB**
   ```bash
   # Windows (parte automaticamente come servizio)
   # Verifica in Task Manager → Servizi → MongoDB

   # Mac
   brew services start mongodb-community

   # Linux
   sudo systemctl start mongod
   ```

3. **Verifica installazione**
   ```bash
   python verify_mongodb.py
   ```
   
   Output atteso:
   ```
   ✅ Connessione OK!
   ✅ Versione MongoDB: 7.x
   ✅ Tutti i test CRUD completati!
   ```

4. **Configura .env**
   ```bash
   cp .env.example .env
   ```
   
   Modifica `.env`:
   ```env
   MONGO_URI=mongodb://localhost:27017
   MONGO_DB_NAME=social_manager_db
   ```

### Issue #15, #12, #10: Setup Gemini AI

1. **Ottieni API Key**
   - Vai su [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Crea una nuova API key
   - Copia la key

2. **Configura .env**
   Aggiungi in `.env`:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   GEMINI_MODEL_NAME=gemini-pro
   ```

3. **Testa Gemini**
   ```bash
   python test_gemini.py
   ```
   
   Output atteso:
   ```
   ✅ API Key trovata
   ✅ Gemini configurato
   ✅ Gemini Response: [risposta AI]
   ✅ TEST COMPLETATO
   ```

---

## 🎯 Sviluppo per Issue

### Issue #5: Preparazione ambiente backend
```bash
# Struttura creata:
backend/
  ├── database/      # Issue #17, #18
  ├── dao/           # Issue #16, #20-25
  ├── ai/            # Issue #15, #12, #10
  ├── schemas/       # Pydantic models
  └── app/           # Routes (legacy FastAPI)
```

### Issue #20-25: Implementare CRUD nel DAO

**Esempio utilizzo PostDAO:**

```python
from backend.dao import PostDAO
from backend.database import connect_to_mongodb

# Setup
await connect_to_mongodb()
post_dao = PostDAO()

# Issue #21: CREATE
post_id = await post_dao.create_post(
    testo="Contenuto post",
    social_target="linkedin",
    status="draft"
)

# Issue #22: READ
posts = await post_dao.find_many({"status": "draft"})
post = await post_dao.find_by_id(post_id)

# Issue #23: UPDATE
await post_dao.update_by_id(post_id, {"status": "published"})

# Issue #24, #25: DELETE
await post_dao.delete_by_id(post_id)
```

File da modificare:
- `backend/dao/post_dao.py` - Estendere metodi
- `app.py` - Decommentare imports DAO e integrare

### Issue #12: Generazione Post con Gemini

**Esempio utilizzo ContentGenerator:**

```python
from backend.ai import get_content_generator

generator = get_content_generator()

# Genera post
result = await generator.generate_post(
    topic="Annuncio nuovo prodotto SaaS",
    social="linkedin",
    tone="professionale",
    temperature=0.7
)

if result["success"]:
    print(result["generated_text"])
    print(f"Caratteri: {result['metadata']['char_count']}")
```

File da modificare:
- `app.py` linea ~30 - Decommentare import generator
- `app.py` linea ~40 - Sostituire mock con Gemini reale
- `backend/ai/prompts.py` - Personalizzare prompt

### Issue #7, #8, #9: Frontend Streamlit

**Sidebar (Issue #7):**
- Implementata: `app.py` linee 80-110
- TODO: Aggiungere filtri, stats, notifiche

**Body (Issue #8):**
- Home page: linee 115-155
- Genera Post: linee 160-240
- Calendario: linee 245-280
- Analytics: linee 285-320

**Header (Issue #9):**
- Ogni page ha header con:
  - Titolo principale
  - Descrizione
  - Separatore `---`

Per estendere:
```python
# In app.py, sezione della page
st.title("📊 Titolo Page")
st.markdown("Descrizione page")
st.markdown("---")

# Poi contenuto...
```

### Issue #16: Generazione Immagini (Future)

Stub preparato in:
- `backend/ai/generator.py` → `generate_image_description()`
- `backend/ai/prompts.py` → `IMAGE_GENERATION_PROMPT`

Per implementare:
1. Integrare DALL-E o Stable Diffusion API
2. Passare descrizione generata da Gemini
3. Salvare immagine in storage (S3, Cloudinary)
4. Collegare a post in MongoDB

---

## ▶️ Avvio Applicazione

```bash
# Assicurati che MongoDB sia attivo
# Assicurati che GEMINI_API_KEY sia in .env

# Avvia Streamlit
streamlit run app.py
```

App disponibile su: **http://localhost:8501**

---

## 🧪 Testing

```bash
# Test MongoDB
python verify_mongodb.py

# Test Gemini
python test_gemini.py

# Test integrazione (TODO: creare test suite)
# pytest tests/
```

---

## 📂 Struttura File per Issue

```
├── app.py                       # Frontend Streamlit (#7, #8, #9)
├── requirements.txt             # Dipendenze (#5)
├── .env.example                 # Template configurazione
├── verify_mongodb.py            # Test MongoDB (#11, #19)
├── test_gemini.py               # Test Gemini (#15)
│
├── backend/
│   ├── database/
│   │   ├── connection.py        # Issue #17, #18, #19
│   │   └── __init__.py
│   │
│   ├── dao/
│   │   ├── base_dao.py          # Issue #16, #20, #21-25
│   │   ├── post_dao.py          # DAO specifico Post
│   │   └── __init__.py
│   │
│   ├── ai/
│   │   ├── gemini_config.py     # Issue #15
│   │   ├── prompts.py           # Issue #10, #13
│   │   ├── generator.py         # Issue #12, #6, #16
│   │   └── __init__.py
│   │
│   └── schemas/
│       └── post.py              # Pydantic models
│
└── SETUP_GUIDE.md               # This file
```

---

## 🐛 Troubleshooting

### MongoDB non si connette
```bash
# Windows: Verifica servizio
services.msc → cerca MongoDB → Avvia

# Verifica porta 27017 libera
netstat -ano | findstr :27017

# Prova connessione diretta
mongo  # oppure mongosh
```

### Gemini API errori
```bash
# Verifica API key valida
python test_gemini.py

# Errore "API key not valid"
# → Rigenera key su Google AI Studio

# Errore "Quota exceeded"
# → Controlla limiti su https://ai.google.dev/pricing
```

### Streamlit non trova moduli backend
```bash
# Verifica path in app.py (linea 9-10)
sys.path.append(str(Path(__file__).parent / "backend"))

# Oppure installa in editable mode
pip install -e .
```

---

## 📞 Supporto

- **Issues progetto**: GitHub Issues tab
- **MongoDB docs**: https://www.mongodb.com/docs/
- **Gemini docs**: https://ai.google.dev/docs
- **Streamlit docs**: https://docs.streamlit.io

---

## ✅ Checklist Completa

- [ ] MongoDB installato e running
- [ ] `python verify_mongodb.py` passa tutti i test
- [ ] Gemini API key configurata in `.env`
- [ ] `python test_gemini.py` passa tutti i test
- [ ] `pip install -r requirements.txt` completato
- [ ] `streamlit run app.py` avvia app senza errori
- [ ] Testato "Genera Post" con AI reale
- [ ] (Opzionale) Testato salvataggio post in MongoDB

---

**Progetto pronto per sviluppo! 🚀**
