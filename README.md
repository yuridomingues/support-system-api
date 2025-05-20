
# Support System API

API developed in **FastAPI** for registering and managing clients and support tickets.

---

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [Python-Jose (JWT)](https://python-jose.readthedocs.io/en/latest/)
- [Pytest + pytest-asyncio](https://docs.pytest.org/)
- [Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/)
- [uv](https://github.com/astral-sh/uv)

---

## Installation and Local Execution

### Prerequisites

- Python 3.12+
- Docker and Docker Compose
- `uv` (optional, but recommended)

## Virtual Environment Setup with `uv`

It is recommended to use [`uv`](https://github.com/astral-sh/uv) to simplify virtual environment creation and dependency synchronization.

### Create and activate the virtual environment

```bash
uv venv
```

### Activate the virtual environment

- On Linux/macOS:

```bash
source .venv/bin/activate
```

- On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Synchronize dependencies

```bash
uv sync
```
---

## `.env` File Configuration

To run the application, you need to create a `.env` file in the project root with the following environment variables:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/support_db
SECRET_KEY=ana
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Local Setup with Docker

```bash
make up

# Access the API at:
http://localhost:8000
```

### Run Automated Tests

```bash
# Using Makefile
make test

```

> The tests use **in-memory SQLite** to ensure isolation and speed.

---

## Authentication

Authentication is done via JWT. Use the endpoint:

```
POST /auth/token
```

**Request body (x-www-form-urlencoded):**

```
username=admin
password=1234
```

**Usage example:**

Add the token to the header of protected requests:

```
Authorization: Bearer <token>
```

---

## Database

- **Production:** PostgreSQL (port 6543 in `docker-compose.yml`)
- **Tests:** In-memory SQLite (`test.db` may be generated locally)

---

## Useful Commands

```bash
# Start application
make up

# Stop containers and remove volumes
make down

# Run tests
make test
```

---

## Notes

- Project focused on best practices, clarity, and complete API functionality.
- Authentication protects sensitive routes.
- Independent tests using local SQLite.
