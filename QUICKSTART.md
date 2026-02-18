# 🚀 Guida Rapida - Come Avviare SocialManager

Questa guida è pensata per i colleghi che vogliono avviare l'app **senza complicazioni**.

---

## ⚡ Quick Start (60 secondi)

### Windows - PowerShell (Consigliato)

```powershell
# 1. Apri PowerShell nella cartella del progetto
# 2. Esegui:

.\setup.ps1
```

### Windows - Prompt dei comandi

```cmd
# 1. Apri cmd nella cartella del progetto
# 2. Esegui:

setup.bat
```

### Linux/Mac (Bash)

```bash
# 1. Apri terminale nella cartella del progetto
# 2. Esegui:

bash setup.sh

# Se non funziona, dai i permessi:
chmod +x setup.sh
```

---

## 📋 Cosa fa lo script di Setup?

Lo script automatico fa **tutto questo per te**:

✅ Verifica che Python sia installato  
✅ Crea ambiente virtuale Python  
✅ Installa tutte le dipendenze  
✅ Configura il file `.env`  
✅ Avvia l'applicazione  

**Risultato:** Invece di 10-15 minuti di comandi, **1 click per avviare l'app**.

---

## 🎯 Opzioni di Avvio

Dopo aver eseguito lo script, scegli come avviare:

### 1️⃣ **Avvio Completo** (Consigliato) 
- Frontend Streamlit (`http://localhost:8501`)
- Backend API (`http://localhost:8000`)
- Avvia in 2 finestre separate automaticamente

### 2️⃣ **Solo Frontend (Streamlit)**
- Utile se il Backend è già avviato
- Accedi a `http://localhost:8501`

### 3️⃣ **Solo Backend (API)**
- Utile per lo sviluppo del backend
- Accedi a `http://localhost:8000/docs` per la documentazione interattiva

### 4️⃣ **Test MongoDB**
- Verifica che il database sia raggiungibile
- Testa la connessione MONGO_URI

---

## 🔧 Cosa devi configurare

### 1. File `.env` (Configurazione)

Lo script crea automaticamente un file `.env`. **Devi modificarlo con i tuoi valori:**

```bash
# 📋 Apri il file .env (nella root del progetto)
# 🖊️  Modifica i valori con i tuoi:

MONGO_URI=mongodb://localhost:27017/socialmanager
GOOGLE_API_KEY=sk-...  # Aggiungi la tua chiave API Gemini
ENVIRONMENT=development
```

### 2. Google Gemini API Key

```
Come ottenerla:
1. Vai a https://aistudio.google.com/app/apikeys
2. Crea una nuova API Key (è gratis per i test)
3. Copia il valore in GOOGLE_API_KEY nel file .env
```

### 3. MongoDB Locale (Opzionale)

Se vuoi usare il database localmente:

```bash
# Windows - Installa MongoDB Community Edition
# Scarica da: https://www.mongodb.com/try/download/community

# Dopo l'installazione, MongoDB inizia automaticamente
# Chiedi ad un collega se serve help di setup
```

---

## 🆘 Troubleshooting

### ❌ "Python non trovato"

**Soluzione:**
1. Installa Python da https://www.python.org (versione 3.8+)
2. ⚠️ **IMPORTANTE:** Al setup, spunta "Add Python to PATH"
3. Riavvia il terminale e riprova

### ❌ "Permesso negato" (su Mac/Linux)

**Soluzione:**
```bash
chmod +x setup.sh
bash setup.sh
```

### ❌ "La porta 8501 è già in uso"

**Soluzione:**
```powershell
# Trova il processo che usa la porta:
netstat -ano | findstr :8501

# O riavvia il terminale/computer
```

### ❌ "ModuleNotFoundError: No module named 'streamlit'"

**Soluzione:**
```powershell
# Lo script di setup deve averlo installato, ma se capita:
pip install -r requirements.txt
```

### ❌ "Errore di connessione MongoDB"

**Soluzione:**
1. Controlla che MongoDB sia in esecuzione
2. Verifica che `MONGO_URI` nel `.env` sia corretto
3. Esegui l'opzione "Test MongoDB" dello script per diagnosticare

---

## 📚 Accesso all'Applicazione

Una volta avviata:

| Componente | URL | Che cos'è |
|-----------|-----|----------|
| **Frontend** | `http://localhost:8501` | L'interfaccia Streamlit per usare l'app |
| **Backend API** | `http://localhost:8000` | Server dati |
| **Docs API** | `http://localhost:8000/docs` | Documentazione interattiva (Swagger) |
| **Redoc API** | `http://localhost:8000/redoc` | Documentazione alternativa |

---

## 👥 Aiuto Rapido

**Problema con lo script?**
- Esegui con `-Verbose` (PowerShell):
  ```powershell
  .\setup.ps1 -Verbose
  ```

**Backend non parte?**  
- Controlla `MONGO_URI` e `GOOGLE_API_KEY` nel `.env`
- Accedi a `http://localhost:8000/docs` per diagnosticare

**Streamlit non carica?**  
- Prova a riaprire il browser
- Chiudi e riavvia lo script

**Aiuto immediato:**
- Chiedi a Damiano o al team DevOps 👈

---

## ℹ️ Comandi Avanzati (Opzionale)

Se preferisci **evitare lo script** e usare il terminale direttamente:

```powershell
# 1. Crea ambiente virtuale
python -m venv .venv

# 2. Attivalo
.\.venv\Scripts\Activate.ps1

# 3. Installa dipendenze
pip install -r requirements.txt

# 4. Imposta variabili d'ambiente
$env:PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION = "python"
$env:GOOGLE_API_KEY = "tua-chiave-api"

# 5a. Avvia Backend
python -m uvicorn main:app --reload --app-dir backend --port 8000

# 5b. In un altro terminale, avvia Streamlit
python -m streamlit run app.py
```

---

## 📖 Documentazione Completa

Per info più dettagliate, leggi:
- [README.md](../README.md) - Guida completa del progetto
- [docs/API.md](../docs/API.md) - Documentazione API Backend
- [docs/BACKEND.md](../docs/BACKEND.md) - Architettura Backend
- [docs/DATABASE.md](../docs/DATABASE.md) - Schema Database

---

**Ultima modifica:** 2026-02-18  
**Per il team:** SocialManager MVP Setup Guide
