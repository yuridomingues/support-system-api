FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
COPY .env ./

RUN pip install uv

COPY . ./

RUN uv pip install --system --editable .

CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0"]
