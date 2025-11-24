# Use Python 3.13 (ou 3.12 se 3.13 não estiver disponível)
FROM python:3.13-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copia dependências + README
COPY pyproject.toml poetry.lock* README.md /app/

RUN pip install --upgrade pip \
    && pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --without dev

# Copie todo o código
COPY . /app

# Porta que o Railway vai usar
ENV PORT 8000

# Comando de start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
