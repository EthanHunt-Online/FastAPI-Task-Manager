# FastAPI-Task-Manager

A full-stack task manager application with a FastAPI backend and a lightweight static frontend. It supports user registration/login with JWT authentication and task CRUD operations scoped to the authenticated user.

## Project Overview

This repository contains:
- **Backend API** built with FastAPI + SQLAlchemy for authentication and task management.
- **Frontend client** (vanilla HTML/CSS/JS) that calls the backend API.
- **Basic tests** for configuration behavior.

Core backend capabilities include:
- User registration and login.
- JWT bearer token issuance and verification.
- Task create/read/update/delete endpoints.
- Per-user authorization checks (users can only access their own tasks).
- Pagination and completion-status filtering on task listing.

## Folder Structure

```text
.
├── backend/
│   ├── app/
│   │   ├── api/         # Route handlers (auth + tasks)
│   │   ├── core/        # Settings and security helpers
│   │   ├── db/          # Database session/engine wiring
│   │   ├── models/      # SQLAlchemy models
│   │   ├── schemas/     # Pydantic request/response models
│   │   └── main.py      # FastAPI app entrypoint
│   └── requirements.txt
├── frontend/
│   ├── app.js
│   ├── config.template.js
│   ├── config.js
│   ├── index.html
│   ├── serve.sh         # Static frontend server helper script
│   └── styles.css
├── tests/
└── README.md
```

## Local Setup Instructions

### 1) Backend setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in `backend/` (optional if using defaults):

```env
APP_NAME=FastAPI Task Manager
DATABASE_URL=sqlite:///./task_manager.db
JWT_SECRET_KEY=change-this-in-production
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 2) Frontend setup

From the repository root:

```bash
cd frontend
chmod +x serve.sh
```

Set the API URL in one of two ways:
- edit `frontend/config.js` directly, or
- pass `API_BASE_URL` while starting `serve.sh` (recommended).

## Environment Variables

### Backend (`backend/app/core/config.py`)

| Variable | Default | Description |
|---|---|---|
| `APP_NAME` | `FastAPI Task Manager` | FastAPI application title. |
| `DATABASE_URL` | `sqlite:///./task_manager.db` | SQLAlchemy database connection string. |
| `JWT_SECRET_KEY` | `change-this-in-production` | Secret used to sign JWT access tokens. |
| `JWT_ALGORITHM` | `HS256` | JWT signing algorithm. |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `60` | Access token expiration time in minutes. |

### Frontend (`frontend/serve.sh`)

| Variable | Default | Description |
|---|---|---|
| `API_BASE_URL` | `http://localhost:8000` | Base URL used by frontend API calls. |
| `PORT` | `4173` | Port used by the local static frontend server. |

## Run Commands

### Run backend

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run frontend

```bash
cd frontend
API_BASE_URL=http://localhost:8000 PORT=4173 ./serve.sh
```

Frontend will be available at `http://localhost:4173` by default.

## Test Commands

From repository root:

```bash
pytest -q
```

You can also run a specific file:

```bash
pytest -q tests/test_config.py
```

## API Endpoint Summary

### Authentication
- `POST /register` — create a new user account.
- `POST /login` — validate credentials and return bearer token.

### Tasks (Bearer token required)
- `POST /tasks` — create a task.
- `GET /tasks` — list tasks for current user.
- `GET /tasks/{task_id}` — fetch a single task.
- `PUT /tasks/{task_id}` — update a task.
- `DELETE /tasks/{task_id}` — delete a task.

## `/docs` Availability and Auth Flow for Testing

When backend is running locally, interactive Swagger docs are available at:
- `http://localhost:8000/docs`

Recommended auth test flow:
1. Call `POST /register` with email/password.
2. Call `POST /login` with the same credentials.
3. Copy `access_token` from login response.
4. Click **Authorize** in `/docs` and enter: `Bearer <access_token>`.
5. Test protected `/tasks` endpoints from the docs UI.

If you skip authorization, `/tasks` endpoints should return `401 Unauthorized`.

## Pagination & Filter Query Parameters

`GET /tasks` supports:
- `skip` (integer, default `0`, min `0`) — number of records to offset.
- `limit` (integer, default `20`, min `1`, max `100`) — max records to return.
- `completed` (boolean, optional) — filter by completion status.

Sample requests:

```bash
# First page (default limit)
curl -H "Authorization: Bearer <token>" \
  "http://localhost:8000/tasks"

# Page with offset and custom limit
curl -H "Authorization: Bearer <token>" \
  "http://localhost:8000/tasks?skip=20&limit=10"

# Only completed tasks
curl -H "Authorization: Bearer <token>" \
  "http://localhost:8000/tasks?completed=true"

# Only incomplete tasks with pagination
curl -H "Authorization: Bearer <token>" \
  "http://localhost:8000/tasks?completed=false&skip=0&limit=5"
```

## Links

- **Deployment URL**: _TODO: add deployed app/API link_
- **Public Repository URL**: _TODO: add public repository link_
