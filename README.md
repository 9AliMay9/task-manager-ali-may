# Task Manager API – ali-may

A lightweight and modular task management API using FastAPI, SQLAlchemy, and SQLite. Managed with PDM.

## 🚀 Features

- CRUD support: Create / Read / Update / Delete tasks
- Simple schema-based validation using Pydantic
- Modular structure with routers and models
- Lightweight and beginner-friendly structure
- Ready for future extension: Token authentication, PostgreSQL, OAuth2, deployment, etc.

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) – Modern, fast web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database models
- [SQLite](https://www.sqlite.org/) – Lightweight embedded DB (for local development)
- [PDM](https://pdm.fming.dev/) – Python dependency manager

## 📂 Project Structure

```bash
task-manager-ali-may/
├── auth.py           # Auth-related logic
├── config.py         # Global configuration
├── crud.py           # Business logic (CRUD operations)
├── database.py       # Database connection and session management
├── init_db.py        # Initialize database
├── main.py           # Application entry point
├── models.py         # SQLAlchemy models
├── routes.py         # API routes
├── schemas.py        # Pydantic schemas for validation
├── task.db           # SQLite database file
└── tests/            # Unit tests
    └── test_main.py  # Example test file
```

## 🧪 How to Run

```bash
# Clone the repo
git clone https://github.com/<your-username>/task-manager-ali-may.git
cd task-manager-ali-may

# Install dependencies
pdm install

# Start server
pdm run uvicorn main:app --reload
```
## 🧱 Roadmap
Add basic token-based auth (non-OAuth2) √

Switch to PostgreSQL

Add OAuth2 + JWT support

### 🌟 Optional ideas

Add exception handling middleware

Add automated tests

Dockerize for deployment

Built with ❤️ by ali-may
