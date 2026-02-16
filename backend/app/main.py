from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import engine
from sqlmodel import SQLModel

# Import the router
from app.api.v1.endpoints import auth

# Import Models
from app.models.user import User 

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

# Include the router with a prefix
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])