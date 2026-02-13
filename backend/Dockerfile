FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY pyproject.toml .
# For now, strictly installing via pip for simplicity, ideally use poetry or uv later
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn[standard] sqlmodel psycopg2-binary redis passlib[argon2] python-jose[cryptography] python-multipart

COPY . .

# Environment variables are set in docker-compose, but exposed here
EXPOSE 8000