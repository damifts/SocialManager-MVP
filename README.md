# Social Manager - MVP

Piattaforma per la gestione social con automazione AI. Il progetto utilizza **Streamlit** come interfaccia principale con backend Python per logica business.

Progetto pensato per tanti contributor: architettura semplificata con Python/Streamlit per prototipazione rapida.

## Team & Task Distribution

### Core & DevOps (Damiano, Daniele, Davide)
- Setup: Inizializzazione monorepo, Dockerfile e docker-compose.yml.
- CI/CD: Configurazione GitHub Actions e gestione environment (.env).
- Repository: Manutenzione del workflow Git e review delle PR.

### Backend & AI (Andrea, Alessio Mizzan, Filippo, Danilo)
- API: Sviluppo endpoint in FastAPI (CRUD post, gestione calendario).
- AI Integration: Logica di generazione contenuti (System Instruction sull'identita' aziendale).
- Social: Integrazione API LinkedIn (scelto come primo social per l'MVP).
- DB: Definizione modelli e persistenza dati dello storico/programmazione.

### Frontend & UI (Thomas, Patrick, Mohamed, Alessandro, Cristian Pola)
- Interface: Sviluppo UI con Next.js, Tailwind CSS e Lucide React.
- Components: Editor AI assisted, Dashboard metriche e Calendario interattivo.
- State: Gestione dello stato globale e integrazione con le API del backend.

### Strategy & QA (Alessio, Cristian Vecchi)
- Requisiti: Definizione dei flussi di pubblicazione e logica dei suggerimenti (news/trend).
- Testing: Test funzionali sulla pubblicazione e validazione dell'output AI.
- PM: Monitoraggio roadmap MVP e pianificazione release.

## Struttura del Progetto
- `app.py`: Applicazione Streamlit principale (UI + logica)
- `/backend`: Moduli Python per business logic e schemas
- `requirements.txt`: Dipendenze Python unificate

## Stack Tecnologico
- **Frontend/UI**: Streamlit (Python)
- **Backend Logic**: Python + Pydantic schemas
- **AI**: LangC

```bash
# 1. Crea virtual environment
python -m venv .venv

# 2. Attiva venv
# Windows:
.venv\Scripts\activate
# Unix/macOS:
source .venv/bin/activate

# 3. Installa dipendenze
pip install -r requirements.txt

# 4. Avvia Streamlit
streamlit run app.py
```

L'app sarà disponibile su: http://localhost:8501

## Configurazione
Duplica `.env.example` in `.env` e inserisci le variabili richieste.

## Sviluppo
- Modifica `app.py` per UI e flussi
- Aggiungi logica business in `backend/`
- Schemas Pydantic in `backend/schemas/`
- Config Streamlit in `.streamlit/config.toml`
Frontend: http://localhost:3000

## Configurazione
Duplica `.env.example` in `.env` e inserisci le variabili richieste.

## Contribuire
Linee guida in [CONTRIBUTING.md](CONTRIBUTING.md).

## Tecnologie
- Backend: FastAPI + Python
- Frontend: Next.js + Tailwind CSS
- AI: OpenAI/Gemini API tramite LangChain
- UI: Streamlit
- Backend: Python + Pydantic
- AI: LangChain + OpenAI/Gemini
- Charts: Plotly
- Database: MongoDB (Motor)