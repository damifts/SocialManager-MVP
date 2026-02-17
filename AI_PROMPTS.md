# Prompt per Generazione Codice con AI

Usa questi prompt template con **Claude**, **ChatGPT** o altri LLM per generare codice coerente con il progetto Streamlit.

## 🎯 Prompt Generico Base

```
Crea una sezione/funzionalità per Social Manager MVP (Streamlit) con queste specifiche:

CONTESTO PROGETTO:
- Piattaforma per gestione contenuti social con AI
- Stack: Streamlit, Python, Pydantic schemas
- Backend: LangChain + OpenAI per AI, Motor per MongoDB
- Design: Custom CSS in st.markdown() con palette amber/brand

FUNZIONALITÀ DA CREARE:
[Descrivi qui, es: "Dashboard analytics con grafici engagement Plotly"]

REQUISITI TECNICI:
- Python con type hints
- Streamlit components (st.columns, st.metric, st.button, etc.)
- Plotly per grafici interattivi
- Session state con st.session_state
- Validazione dati con Pydantic schemas
- Responsive layout con st.columns()

STILE VISIVO (CSS inline):
- Bordi arrotondati (border-radius: 1rem)
- Palette: background gradient brand, card bianche con shadow
- Bottoni arancione/amber (#f59e0b) con hover (#d97706)
- Spacing generoso, padding 1.5rem per card

ESEMPIO OUTPUT ATTESO:
Codice Python per inserire in app.py o nuovo file in backend/
```

## 📋 Prompt per Funzionalità Specifiche

### Dashboard/Analytics
```
Crea una sezione Analytics per Social Manager MVP (Streamlit) che mostri:
- 3 metriche principali con st.metric() (views, engagement, reach)
- Grafico Plotly linea per trend settimanale
- Grafico Plotly barre per performance per social
- Filtri temporali con st.date_input()
- Layout a 2 colonne responsive con st.columns()
- Custom CSS per card bianche con shadow
- Dati mock per ora (lista dict Python)
```

### Form/Editor Avanzato
```
Crea un PostEditor avanzato per Social Manager MVP (Streamlit):
- st.text_area() per contenuto con counter caratteri
- st.multiselect() per piattaforme social (LinkedIn, Twitter, Instagram, Facebook)
- st.date_input() + st.time_input() per programmazione
- st.selectbox() per tono di voce (Professionale, Casual, Ispirazionale)
- Bottone "Genera con AI" che chiama funzione mock
- Preview live del post in st.container() con emoji social
- Validazione inline con st.warning() se campi vuoti
- State management con st.session_state
```

### Calendario Editoriale
```
Crea un Calendar component per Social Manager MVP (Streamlit):
- Vista mensile con st.columns() per layout griglia
- st.date_input() per navigazione mese
- Lista post programmati per data con st.expander()
- Badge colorati per social (emoji o st.markdown con CSS)
- Click su giorno mostra dettagli in sidebar con st.sidebar
- Filtri per social e status
- Dati mock in dizionario Python {data: [lista_post]}
```

### Tabella Post con CRUD
```
Crea una PostList per Social Manager MVP (Streamlit):
- st.dataframe() interattiva con post (testo, social, data, status)
- Filtri in st.sidebar (social, status, range date)
- Bottoni azione per ogni riga (Edit, Delete) con st.button()
- Modal edit con st.form() per modifiche
- Empty state con st.info() se nessun post
- Paginazione custom con st.session_state
- Export CSV con st.download_button()
- Dati mock in pandas DataFrame
```

### Integrazioni AI
```
Crea funzione AI generation per Social Manager MVP:
- Funzione async che usa LangChain + OpenAI
- Input: prompt (str), social_target (str), tono (str)
- Output: testo generato + suggerimenti hashtag
- Error handling con try/except
- Logging per debug
- Mock version per testing senza API key
- Integrazione in UI Streamlit con st.spinner()
- Cache con @st.cache_data per richieste duplicate
```

## 🎨 Riferimenti Streamlit Components

**Layout:**
```python
# Colonne responsive
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Metric", "1234", "+5%")

# Tabs
tab1, tab2 = st.tabs(["📊 Analytics", "📅 Calendario"])
with tab1:
    st.write("Contenuto tab")

# Sidebar
with st.sidebar:
    st.title("Navigazione")
    option = st.selectbox("Scegli", ["Opzione 1", "Opzione 2"])

# Expander
with st.expander("Mostra dettagli"):
    st.write("Contenuto nascosto")
```

**Inputs:**
```python
# Text
testo = st.text_area("Label", placeholder="Placeholder...", height=150)
nome = st.text_input("Nome")

# Select
social = st.selectbox("Social", ["LinkedIn", "Twitter", "Instagram"])
socials = st.multiselect("Socials", ["LinkedIn", "Twitter", "Instagram"])

# Date/Time
data = st.date_input("Data")
ora = st.time_input("Ora")

# Number
numero = st.number_input("Numero", min_value=0, max_value=100)

# Boolean
check = st.checkbox("Accetto")
toggle = st.toggle("Enable feature")
```

**Output:**
```python
# Metrics
st.metric("Views", "1.2K", "+12%")

# Charts Plotly
import plotly.express as px
fig = px.line(df, x="data", y="views")
st.plotly_chart(fig, use_container_width=True)

# Messages
st.success("Operazione completata!")
st.error("Errore!")
st.warning("Attenzione!")
st.info("Info utile")

# Spinner
with st.spinner("Caricamento..."):
    time.sleep(2)
    st.success("Fatto!")
```

**Custom CSS:**
```python
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #fef3c7 0%, #f8fafc 100%);
    }
    .stButton>button {
        background-color: #f59e0b;
        color: white;
        border-radius: 9999px;
        padding: 0.75rem 1.5rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)
```

## 💡 Best Practices Streamlit

**Session State:**
```python
# Inizializzazione
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Utilizzo
st.session_state.counter += 1
st.write(f"Counter: {st.session_state.counter}")
```

**Caching:**
```python
# Cache dati (si invalida se input cambia)
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

# Cache risorse (connessioni DB, modelli AI)
@st.cache_resource
def init_mongodb():
    return motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
```

**Forms per input multipli:**
```python
with st.form("my_form"):
    name = st.text_input("Nome")
    age = st.number_input("Età")
    submitted = st.form_submit_button("Invia")
    if submitted:
        st.success(f"Ciao {name}, hai {age} anni!")
```

## 🚫 Cosa NON chiedere

- ❌ Frontend separato (es. React) - usiamo solo Streamlit
- ❌ Dipendenze extra pesanti senza approvazione team
- ❌ Codice senza type hints
- ❌ Dati hardcoded senza possibilità di configurazione

## 🚀 Workflow Consigliato

1. **Genera** codice con AI usando prompt sopra
2. **Testa** localmente: `streamlit run app.py`
3. **Aggiungi** sezione in `app.py` o crea file in `backend/`
4. **Valida** con Pydantic schemas se gestisci dati
5. **Committa** su branch `feat/nome-feature`
6. **PR** con descrizione e screenshot
