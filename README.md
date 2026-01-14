# Day 2: AI-Assisted Backend Development

**Time:** 60 minutes  
**Objective:** Build a FastAPI inventory system using AI-assisted development

## Overview

Follow each step by copying the prompt to your AI assistant. Each step builds on the previous one.

---

## Step 0 — Project Setup

**Prompt for AI:**

```
Create a FastAPI project for an inventory system.
- Use app/ as the root folder with subfolders: routers, services, schemas, db, tests.
- Add __init__.py to app/ and all subfolders.
- Include main.py with a basic FastAPI app.
- Show folder structure and setup instructions (venv, install, run server, open docs).
```

**Expected Output:**

```
app/
├── __init__.py
├── main.py
├── routers/
│   └── __init__.py
├── services/
│   └── __init__.py
├── schemas/
│   └── __init__.py
├── db/
│   └── __init__.py
└── tests/
    └── __init__.py
```

---

## Step 1 — Environment Variables

**Prompt for AI:**

```
Create a .env file at project root with:
- SUPABASE_DB_URL (PostgreSQL connection pooler URL, port 6543)
- SUPABASE_API_KEY

Include instructions to get the URL from Supabase Dashboard.
```

**Expected Output:**

`.env`

```env
SUPABASE_DB_URL=postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres
SUPABASE_API_KEY=your-anon-key-here
```

---

## Step 2 — Pydantic Schemas

**Prompt for AI:**

```
Create Pydantic schemas for inventory items:
- Fields: id (int), name (str), quantity (int >= 0), price (float >= 0)
- Include ItemCreate, ItemUpdate, ItemRead schemas
- Include proper validation rules
```

**Expected Output:**

```
app/schemas/
└── item.py
```

---

## Step 3 — Database Connection

**Prompt for AI:**

```
Set up SQLAlchemy database connection.
- Load SUPABASE_DB_URL from .env using python-dotenv.
- Create engine, SessionLocal, and Base class.
- Create SQLAlchemy Item model matching the Pydantic schema.
- Create tables on startup.
- Add get_db dependency.
```

**Expected Output:**

```
app/db/
├── database.py
└── models.py
```

---

## Step 4 — Service Layer

**Prompt for AI:**

```
Create InventoryService class:
- Accept SQLAlchemy DB session via parameter
- Implement CRUD: create_item, get_item, get_all_items, update_item, delete_item
- Return Pydantic schemas
- Raise HTTPException(404) if item not found
```

**Expected Output:**

```
app/services/
└── inventory_service.py
```

---

## Step 5 — API Routers

**Prompt for AI:**

```
Create FastAPI CRUD endpoints for inventory items:
- Inject DB session via Depends(get_db)
- Use Pydantic schemas for request/response
- Endpoints:
  - GET /api/items/ — List all items
  - GET /api/items/{id} — Get item by ID
  - POST /api/items/ — Create item
  - PUT /api/items/{id} — Update item
  - DELETE /api/items/{id} — Delete item
```

**Expected Output:**

```
app/routers/
└── item_router.py
```

---

## Step 6 — Update main.py

**Prompt for AI:**

```
Update main.py to:
- Set title "Inventory Management API", version "1.0.0"
- Include item router with /api prefix
- Add root and health check endpoints
- Create database tables on startup
```

**Expected Output:**

`app/main.py` (updated)

---

## Step 7 — Test Cases

**Prompt for AI:**

```
Create pytest tests for all CRUD endpoints.
- Use FastAPI TestClient
- Test create, read, update, delete
- Test valid, invalid, and not-found cases
- Run with: pytest -v
```

**Expected Output:**

```
app/tests/
└── test_items.py
```

---

## Step 8 — Requirements + README

**Prompt for AI:**

```
Create requirements.txt with: fastapi[standard], uvicorn[standard], sqlalchemy, pydantic, psycopg2-binary, python-dotenv, pytest, httpx.
```

**Expected Output:**

```
requirements.txt
```

---

## Step 9 — Run the Project

```powershell
py -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate
pip install -r requirements.txt
fastapi dev app/main.py
```

Open: **http://127.0.0.1:8000/docs**

Run tests:

```powershell
pytest -v
```

---

## Final Project Structure

```
day-2-ai-backend/
├── .env
├── requirements.txt
├── README.md
└── app/
    ├── __init__.py
    ├── main.py
    ├── routers/
    │   ├── __init__.py
    │   └── item_router.py
    ├── services/
    │   ├── __init__.py
    │   └── inventory_service.py
    ├── schemas/
    │   ├── __init__.py
    │   └── item.py
    ├── db/
    │   ├── __init__.py
    │   ├── database.py
    │   └── models.py
    └── tests/
        ├── __init__.py
        └── test_items.py
```

---

## API Endpoints Summary

| Method | Endpoint          | Description       |
|--------|-------------------|-------------------|
| GET    | /api/items/       | List all items    |
| GET    | /api/items/{id}   | Get item by ID    |
| POST   | /api/items/       | Create new item   |
| PUT    | /api/items/{id}   | Update item       |
| DELETE | /api/items/{id}   | Delete item       |

---

## Deliverable

A working FastAPI inventory API with:
- Simple Item model (id, name, quantity, price)
- Supabase PostgreSQL connection
- Pydantic schemas with validation
- CRUD operations
- Pytest tests
- Swagger docs at http://127.0.0.1:8000/docs
