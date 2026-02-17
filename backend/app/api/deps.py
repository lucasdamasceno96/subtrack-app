from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError
from sqlmodel import Session

from app.core.config import settings
from app.core.database import get_session
from app.models.user import User
from app.schemas.token import TokenPayload

# Defines the scheme that looks for the header "Authorization: Bearer <token>"
# The tokenUrl must match your login endpoint path
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login/access-token"
)

async def get_current_user(
    token: Annotated[str, Depends(reusable_oauth2)],
    session: Session = Depends(get_session),
) -> User:
    """
    Validates the access token and returns the current user.
    Raises 401 if token is invalid or 404 if user not found.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    if token_data.sub is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    # In SQLModel/Postgres, we generally fetch by the UUID (primary key)
    # Ensure token_data.sub is converted to UUID if your DB expects a UUID object, 
    # though SQLModel often handles the string-to-uuid coercion automatically.
    user = session.get(User, token_data.sub)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not user.is_active: # Good practice: check if user is active
         raise HTTPException(status_code=400, detail="Inactive user")

    return user

# Helper dependency for endpoints that require explicitly a Superuser
# (Bonus tip for future implementation)
def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user