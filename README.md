# 💸 SpendAPI

A backend service built using **FastAPI**, **PostgreSQL**, and **Alembic**, designed to let users track and manage their financial activities — including income and categorized expenses.

---

## 🎯 Vision

Enable users to:

- Record financial transactions (credits or debits)
- Categorize debits into types such as:
  - `food`
  - `travel`
  - `rent`
  - `outing`
  - `miscellaneous`
- Retrieve or export data for personal finance analysis

This project lays the foundation for a full-featured personal finance tracker or budgeting assistant.

---

## ⚙️ Tech Stack

- **FastAPI** – High-performance async web framework
- **PostgreSQL** – Relational database for persistence
- **SQLAlchemy** – ORM for database interaction
- **Alembic** – Database migration tool
- **Pydantic** – Data validation and parsing
- **JWT Authentication** – Secure login and protected routes
- **Docker & Docker Compose** – For containerized setup

---

## 🔐 Features

- ✅ User registration and JWT-based login
- 💰 Add finance entries (credit or debit)
- 🗂️ Categorize expenses (if debit) into:
  - `food`, `travel`, `rent`, `outing`, `miscellaneous`
- 📊 View all your finance entries
- 📤 Export CSV reports:
  - All finance entries
  - Only expense entries (debits)
- 🔧 Clean modular project structure (services, repos, models, etc.)

---

## 🏁 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SohamKanjiDev/SpendAPI.git
```

### 2. Create a `.env` File

Create a `.env` file in the root of the project with the following content (replace placeholder values with your own):

```env
POSTGRES_DB=your_database_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_HOST_CONTAINER=db
POSTGRES_PORT=5432

TOKEN_SECRET=your_jwt_secret_key
TOKEN_DURATION=15
```

### 3. Run with Docker Compose

Ensure Docker and Docker Compose are installed, then run:

```bash
docker-compose up --build
```

This will spin up:

- FastAPI app
- PostgreSQL database container

Once running, access the API docs at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📘 API Documentation

Full API docs are auto-generated and accessible via FastAPI’s Swagger UI.

These docs include detailed request/response formats, auth headers, error messages, and more.

---

## 📤 CSV Export Endpoints

These endpoints allow authenticated users to export their data:

- `GET /finances/csv`: Export **all** finance entries as CSV
- `GET /finances/csv/expenses`: Export **only expenses** (debit entries) as CSV

The CSVs include fields : Name, Amount, Category.

---

> _“Track smarter. Spend wiser.”_
