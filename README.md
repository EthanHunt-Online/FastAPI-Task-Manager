# FastAPI-Task-Manager

## Frontend

A simple responsive frontend is available in `frontend/` with:

- Registration form
- Login form (stores JWT in `localStorage`)
- Create task form
- List tasks
- Mark task complete
- Delete task

### Run locally

```bash
cd frontend
cp .env.example .env # optional reference
API_BASE_URL="https://your-deployed-fastapi.example.com" PORT=4173 ./serve.sh
```

Then open `http://localhost:4173`.

### API base URL configuration

The frontend reads the backend URL from `API_BASE_URL` at serve time. `serve.sh` writes `config.js` from `config.template.js` so all API calls are routed to your deployed FastAPI backend.
