# Social Manager - MVP

Piattaforma per la gestione social con automazione AI. Il progetto utilizza un'architettura monorepo con FastAPI per il backend e Next.js per il frontend.

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
- /backend: API FastAPI e logica di integrazione AI.
- /frontend: Interfaccia Next.js con design system basato su Tailwind.

## Avvio Rapido (locale)

Backend:

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate | Unix: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Backend: http://localhost:8000 (Docs: /docs)
Frontend: http://localhost:3000

## Configurazione
Duplica `.env.example` in `.env` e inserisci le variabili richieste.

## Tecnologie
- Backend: FastAPI + Python
- Frontend: Next.js + Tailwind CSS
- AI: OpenAI/Gemini API tramite LangChain
- Icons: Lucide React
