# 🚀 CAMBIO ARCHITETTURA: NEXT.JS → STREAMLIT

## ⚠️ IMPORTANTE - Letto da tutti!

Il team ha deciso di **cambiare stack tecnologico** per semplificare lo sviluppo e permettere a tutti di lavorare con **un unico linguaggio (Python)**.

---

## 🔄 COSA È CAMBIATO

### ❌ RIMOSSO
- **Next.js** frontend (TypeScript/React)
- **npm workspaces** e package.json nel frontend
- **Tailwind CSS** compilato
- Task separati backend/frontend

### ✅ NUOVO STACK
- **Streamlit** come UI framework (Python puro!)
- **Python** per tutto: UI + backend + AI
- **Un solo requirements.txt** per tutte le dipendenze
- **Sviluppo semplificato**: un comando per far girare tutto

---

## 🎯 VANTAGGI

1. **Un solo linguaggio** → Python per tutto, niente context-switch
2. **Setup velocissimo** → `pip install -r requirements.txt` e vai
3. **Prototipazione rapida** → Streamlit permette iterazioni veloci
4. **Grafici integrati** → Plotly built-in per analytics
5. **Meno complessità** → No build, no bundler, no transpiling

---

## 🛠️ NUOVO SETUP

```bash
# 1. Crea virtual environment (se non esiste)
python -m venv .venv

# 2. Attiva venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# 3. Installa dipendenze (nuovo requirements.txt!)
pip install -r requirements.txt

# 4. Avvia app
streamlit run app.py
```

**URL**: http://localhost:8501

---

## 📂 NUOVA STRUTTURA

```
app.py              ← Main app Streamlit (UI + logica)
requirements.txt    ← Tutte le dipendenze Python
.streamlit/
  config.toml       ← Configurazione colori/tema
backend/
  schemas/          ← Modelli Pydantic (invariati)
  app/              ← Logica business (opzionale)
```

---

## 🎨 FILE PRINCIPALE: app.py

L'app ha **4 sezioni**:
- 🏠 **Home** → Dashboard con metriche quick
- ✨ **Genera Post** → UI per AI content generation
- 📅 **Calendario** → Vista editoriale (TODO)
- 📊 **Analytics** → Grafici engagement (TODO)

---

## 👥 TASK AGGIORNATI

### Andrea & Filippo → AI Integration
- File: `app.py` funzione `generate_content_mock()`
- Integrare LangChain vera con OpenAI/Gemini
- Sostituire mock con chiamata AI reale

### Thomas → Calendario
- Sezione `"📅 Calendario"` in `app.py`
- Creare vista calendario con post programmati
- Usare `st.date_input()` e logica filtri

### Danilo → Analytics
- Sezione `"📊 Analytics"` in `app.py`
- Espandere grafici Plotly (ora sono mock)
- Integrare metriche da `backend/schemas/post.py`

### Patrick → Preview Post
- In sezione "✨ Genera Post" di `app.py`
- Creare preview formattata per ogni social
- Tag `# TODO: Patrick` presente

### Mohamed & Alessandro → Dashboard
- Migliorare sezione Home
- Aggiungere widgets e metriche real-time
- Integrare con database quando pronto

### Cristian Pola → Social Selector
- In sezione "✨ Genera Post"
- Estendere selector con icone e preview
- Tag `# TODO: Cristian Pola` presente

---

## 🔥 TECNOLOGIE PRINCIPALI

| Componente | Tecnologia |
|-----------|-----------|
| **UI** | Streamlit 1.40.2 |
| **Backend** | Python + Pydantic |
| **AI** | LangChain + OpenAI |
| **Charts** | Plotly + Pandas |
| **Database** | MongoDB (Motor) |

---

## 📖 DOCUMENTI AGGIORNATI

- ✅ [README.md](README.md) → Nuove istruzioni setup
- ✅ [DEPENDENCIES.md](DEPENDENCIES.md) → Solo Python ora
- ✅ [CONTRIBUTING.md](CONTRIBUTING.md) → Convenzioni Streamlit
- ✅ `.streamlit/config.toml` → Tema custom (colori brand)

---

## ⚡ QUICK START

```bash
git pull origin main
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Apri browser su http://localhost:8501 e sei pronto!

---

## 🎯 PROSSIMI STEP

1. **Tutti**: Testare nuova app e familiarizzare con Streamlit
2. **Andrea/Filippo**: Integrare AI vera (priorità alta)
3. **Altri dev**: Seguire TODO nel codice con vostro nome
4. **DB Team**: Setup MongoDB per persistenza

---

## 💬 DOMANDE?

- 📘 Docs Streamlit: https://docs.streamlit.io
- 💡 Esempi: https://streamlit.io/gallery
- 🐛 Issues: Apri issue su GitHub se blocchi

---

**LET'S BUILD! 🚀**

P.S. Il backend FastAPI è ancora presente (può servire per API esterne), ma l'UI principale è ora Streamlit.
