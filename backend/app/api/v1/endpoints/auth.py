from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.core.security import get_password_hash
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserPublic

router = APIRouter()

@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register_new_user(
    user_in: UserCreate,
    session: Session = Depends(get_session)
):
    """
    Register a new user.
    """
    user_repo = UserRepository(session)

    # 1. Check if user already exists
    if user_repo.get_by_email(user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # 2. Hash password
    hashed_password = get_password_hash(user_in.password)

    # 3. Save to DB
    new_user = user_repo.create(user_in, hashed_password)

    return new_user