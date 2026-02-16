from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import engine
from sqlmodel import SQLModel

# Importar modelos para que o SQLModel os reconheça
from app.models.user import User 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Cria as tabelas se não existirem
    SQLModel.metadata.create_all(engine)
    yield
    # Shutdown: (Limpeza se necessário)

app = FastAPI(
    title="SubTrack API",
    lifespan=lifespan
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "SubTrack API is running and connected to DB"}