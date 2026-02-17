# Dependency Coordination

Questo progetto e' aperto a tante persone e librerie diverse. Per mantenere ordine, usiamo regole leggere.

## JavaScript/TypeScript (frontend)
- Installa dipendenze dal root con workspaces:
  - `npm install`
  - `npm install -w frontend <pacchetto>`
- Aggiorna versioni con `npm update -w frontend`.
- Evita dipendenze duplicate che fanno la stessa cosa se non motivate.

## Python (backend)
- Aggiungi i pacchetti in `backend/requirements.txt`.
- Se serve un update, allinea la versione e segnala in PR.

## Regole leggere
- Ogni nuova dipendenza deve avere una motivazione breve in PR.
- Verifica la licenza prima di aggiungere librerie nuove.
- Mantieni versioni compatibili tra team e segnala breaking changes.
