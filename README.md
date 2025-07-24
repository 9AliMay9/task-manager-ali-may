# ✅ Task Manager API – ali-may (Finalized Learning Project)

A lightweight, modular task management API built with **FastAPI**, **SQLAlchemy**, and **JWT** authentication. 

🎯 This project is a **personal learning MVP**, used to explore the foundations of backend development, schema validation, and token-based authentication.

---

## 📌 Project Status

🛠️ **This project is finalized and no longer maintained.**  
It served as a foundational practice for deeper exploration into backend development, and will not receive further updates.  
A new, more systematized project is in progress, focusing on entity modeling and platform-level architecture.

---

## ✅ What Was Built

- ✅ Basic CRUD operations for tasks  
- ✅ Modular architecture with `routers`, `schemas`, and `models`  
- ✅ Token-based authentication (non-JWT)  
- ✅ Switched from SQLite to PostgreSQL  
- ✅ Implemented secure **JWT**-based auth (with permission support)  
- ✅ Used `.env` + `config.py` to manage secrets and settings  
- ✅ Integrated Alembic for database migrations

---

## 🧠 Key Learning Goals

This project helped me learn and practice:

- Structuring a FastAPI project with separation of concerns  
- Using Pydantic schemas for validation  
- Managing SQLAlchemy sessions and models  
- Handling auth securely (JWT, permissions)  
- Setting up `.env`, Docker, Alembic, and PostgreSQL  
- Version control and git hygiene (e.g. avoiding secrets in repo)

---
## 📂 Project Structure
```
task-manager/
├── main.py              # Application entry point
├── auth.py              # Auth-related logic (login, token validation)
├── config.py            # Environment config (loads from .env)
├── crud.py              # Business logic (CRUD operations)
├── database.py          # PostgreSQL session & engine config
├── init_db.py           # DB initializer script (optional seed)
├── models.py            # SQLAlchemy ORM models
├── routes.py            # API route definitions
├── schemas.py           # Pydantic request/response models
├── token_issuer.py      # JWT access token generation logic
├── alembic/
│   ├── env.py           # Alembic migration environment (uses hardcoded DB URI)
│   ├── script.py.mako   # Alembic revision template
│   └── versions/
│       └── xxxx_revision.py  # Auto-generated migration scripts
├── alembic.ini          # (git-ignored, contains DB URI)
├── LICENSE
├── README.md
├── pyproject.toml       # PDM project metadata
├── pdm.lock             # Locked dependency versions
├── tests/               # Placeholder test folder (currently empty)
└── __pycache__/         # Python bytecode cache

```


---

## 🧪 How to Run (for local testing only)

```bash
# Clone the repo
git clone https://github.com/<your-username>/task-manager-ali-may.git
cd task-manager-ali-may

# Install dependencies
pdm install

# Run with uvicorn
pdm run uvicorn main:app --reload
```

---

## 🧱 What's Next

This project laid the foundation for a more ambitious system. The next project will feature:

* 🎯 **Entity-based modeling**, including `Subject` and `Object` relationships
* 🔄 **Temporal, categorical, and descriptive attributes**
* 🔗 Relationship modeling through "Nexus" bindings (e.g. task assignments, permissions)
* 🏗️ Platform-level concerns like observability, deployment, and CI/CD

---

Built with ❤️ by ali-may
2025 · Finalized
