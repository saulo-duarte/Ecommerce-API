FROM python:3.12-slim AS builder

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y curl gcc libpq-dev build-essential ca-certificates

# Baixar e instalar o binário do UV
RUN curl -L https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz \
    | tar -xz && mv uv-x86_64-unknown-linux-gnu/uv /usr/local/bin/uv && rm -rf uv-x86_64-unknown-linux-gnu

# Criar diretório de trabalho
WORKDIR /app

# Copiar o projeto para dentro do container
COPY . .

# Criar o ambiente virtual e sincronizar dependências
RUN uv venv
RUN uv sync

# Adicionar diretório ao PYTHONPATH (útil para alembic/env.py etc)
ENV PYTHONPATH=/app

ENTRYPOINT ["uv", "run", "alembic"]
