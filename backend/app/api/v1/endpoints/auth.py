from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.core.database import get_session
from app.core.security import get_password_hash, create_access_token # <--- Importe create_access_token
from app.core.config import settings
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserPublic
from app.schemas.token import Token # <--- Importe o Token

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

@router.post("/login/access-token", response_model=Token)
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_session)
):
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user_repo = UserRepository(session)
    
    # Nota: form_data.username aqui conterá o EMAIL
    user = user_repo.authenticate(
        email=form_data.username, 
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Inactive user"
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    return Token(
        access_token=create_access_token(
            subject=user.id, 
            expires_delta=access_token_expires
        ),
        token_type="bearer"
    )