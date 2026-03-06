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

Open API docs at: `http://127.0.0.1:8000/docs`

## Run tests

```bash
cd backend
pytest
```
