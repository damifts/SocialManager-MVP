# Dependency Coordination

Questo progetto e' aperto a tante persone e librerie diverse. Per mantenere ordine, usiamo regole leggere.

## Installazione Backend (Python)

Dal root del progetto:

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Unix/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

Dipendenze principali:
- `fastapi` - Framework web
- `uvicorn` - ASGI server
- `pydantic` - Validazione dati
- `langchain` - Orchestrazione AI
- `openai` - API OpenAI (o Gemini)
- `motor` - Driver MongoDB async
- `python-dotenv` - Gestione .env

## Installazione Frontend (Node.js)

Dal root del progetto:

```bash
npm install
# oppure per installare solo nel workspace frontend:
npm install -w frontend
```

Per aggiungere nuove librerie:
```bash
npm install -w frontend <pacchetto>
```

Dipendenze principali:
- `next` - Framework React
- `react` / `react-dom` - UI library
- `tailwindcss` - CSS utility-first
- `lucide-react` - Icon set (OBBLIGATORIO per coerenza UI)
- `typescript` - Type safety

## Regole leggere
- Ogni nuova dipendenza deve avere una motivazione breve in PR.
- Verifica la licenza prima di aggiungere librerie nuove.
- Mantieni versioni compatibili tra team e segnala breaking changes.
- Per le icone usa SOLO `lucide-react` (non altre librerie di icone).
