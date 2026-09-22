# Support System

Backend do **Support System**, um projeto full-stack para gerenciamento de clientes e chamados de suporte.

O produto foi desenvolvido em dois repositórios:

- Backend: este repositório
- Frontend: https://github.com/yuridomingues/support-system-interface

No portfólio, os dois devem ser considerados um único projeto.

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT
- Pytest
- Docker / Docker Compose
- uv

## Funcionalidades

- autenticação JWT;
- cadastro e gerenciamento de clientes;
- abertura e gerenciamento de chamados;
- relacionamento entre clientes e tickets;
- migrations de banco;
- testes automatizados;
- execução local com Docker.

## Rodando localmente

### Dependências

- Python 3.12+
- Docker e Docker Compose
- uv

### Ambiente Python

```bash
uv venv
uv sync
```

### Configuração

Crie um arquivo `.env` a partir da configuração esperada pela aplicação.

Exemplo:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/support_db
SECRET_KEY=<generate-a-long-random-secret>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Nunca reutilize o valor de exemplo como segredo real.

### Executar

```bash
make up
```

API:

```text
http://localhost:8000
```

### Testes

```bash
make test
```

Os testes usam SQLite isolado para acelerar a suíte local.

## Autenticação

O login é feito pelo endpoint:

```text
POST /auth/token
```

Use uma conta criada para o ambiente de desenvolvimento ou seed de teste. O repositório não deve documentar credenciais fixas que possam ser copiadas para outros ambientes.

Depois do login:

```text
Authorization: Bearer <token>
```

## Arquitetura do produto

```text
React / Vite
     ↓
   Axios
     ↓
FastAPI
     ↓
SQLAlchemy / Alembic
     ↓
PostgreSQL
```

Frontend: https://github.com/yuridomingues/support-system-interface

## Próxima organização

A API e a interface pertencem ao mesmo produto. A direção recomendada é consolidá-las futuramente em um monorepo com `backend/` e `frontend/`, preservando o histórico dos repositórios atuais.
