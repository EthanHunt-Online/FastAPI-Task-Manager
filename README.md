# FastAPI-Task-Manager

## Backend (MVP)

Implemented a FastAPI backend under `backend/app` with:

- JWT auth (`POST /register`, `POST /login`)
- Task CRUD protected by bearer auth (`/tasks`)
- Ownership checks for every task operation
- Pagination and completion filter for listing tasks
- Structured error responses for HTTP and validation errors
- SQLite table auto-creation on startup for MVP database initialization

## Run locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open API docs at: `http://127.0.0.1:8000/docs`

## Run tests

```bash
cd backend
pytest
```
