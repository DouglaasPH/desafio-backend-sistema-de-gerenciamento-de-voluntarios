# Use Python 3.13 (ou 3.12 se 3.13 não estiver disponível)
FROM python:3.13-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie arquivos de dependências
COPY pyproject.toml poetry.lock* /app/

# Instale Poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Instale dependências sem dev
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copie todo o código
COPY . /app

# Porta que o Railway vai usar
ENV PORT 8000

# Comando de start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
