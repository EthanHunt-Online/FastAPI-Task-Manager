# FastAPI Task Manager

A full-stack task manager app with:
- a **FastAPI + SQLAlchemy backend** (`backend/`)
- a **static HTML/CSS/JS frontend** (`frontend/`)

It supports registration/login with JWT authentication and per-user task CRUD.

## Current Project Status

### ✅ Implemented
- User registration (`POST /register`) and login (`POST /login`).
- JWT-based auth (`Authorization: Bearer <token>`).
- Task create/list/get/update/delete endpoints under `/tasks`.
- Per-user task ownership checks.
- Pagination (`skip`, `limit`) and completion filtering (`completed`) on task listing.
- API tests in `backend/tests/`.

### ⚠️ Notes
- There are **two app folders**: root `app/` and `backend/app/`.
  - The functional task-manager API lives in `backend/app/`.
  - Root `app/` currently only exposes a simple `/health` endpoint and is not used by backend tests.
- Test/dependency installation may fail in restricted environments without package index access.

## Folder Structure

```text
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── app.js
│   ├── config.template.js
│   ├── config.js
│   ├── index.html
│   ├── serve.sh
│   └── styles.css
├── app/
├── tests/
├── requirements.txt
└── README.md
```

## Local Setup

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Docs: `http://127.0.0.1:8000/docs`

### 2) Frontend

```bash
cd frontend
cp config.template.js config.js
# edit config.js and set API_BASE_URL to your backend URL if needed
./serve.sh
```

Then open: `http://127.0.0.1:3000`

## Running Tests

Backend API tests:
```bash
cd backend
pytest
```

Root config tests:
```bash
cd /path/to/FastAPI-Task-Manager
pytest tests/test_config.py
```

## Quick API Smoke Flow

```bash
# register
curl -X POST http://127.0.0.1:8000/register \
  -H 'Content-Type: application/json' \
  -d '{"email":"alice@example.com","password":"password123"}'

# login
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"alice@example.com","password":"password123"}' | jq -r .access_token)

# create task
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"title":"My task","description":"demo"}'
```
