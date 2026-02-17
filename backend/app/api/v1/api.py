from fastapi import APIRouter
from app.api.v1.endpoints import auth, users # Import users, auth

api_router = APIRouter()
# Register Auth
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# Register Auth
api_router.include_router(users.router, prefix="/users", tags=["users"]) # Add this