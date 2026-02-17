# backend/app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import engine
from sqlmodel import SQLModel
from app.core.config import settings

# Import Routes
from app.api.v1.api import api_router

# Import the router
from app.api.v1.endpoints import auth

# Import Models
from app.models.user import User 
from app.models.subscription import Subscription

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create Table
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="SubTrack API",
    lifespan=lifespan
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "SubTrack API is running and connected to DB"}

# Include routes
app.include_router(api_router, prefix="/api/v1")