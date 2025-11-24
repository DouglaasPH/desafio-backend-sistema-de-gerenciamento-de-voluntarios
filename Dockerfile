# Use a imagem base Python
FROM python:3.13-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de dependências
COPY pyproject.toml poetry.lock /app/

# Instale o Poetry
RUN pip install --no-cache-dir poetry

# Configure o Poetry para não criar virtualenv
RUN poetry config virtualenvs.create false

# Instale apenas as dependências (sem instalar o projeto atual)
RUN poetry install --without dev --no-root

# Copie o restante do código
COPY . /app

# Exponha a porta que a aplicação vai usar
EXPOSE 8000

# Comando para rodar sua aplicação (exemplo FastAPI com uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
