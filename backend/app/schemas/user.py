import uuid
from pydantic import BaseModel, EmailStr, Field

# Base schema with shared properties
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)

# Properties to return to client (public) - NO PASSWORD HERE
class UserPublic(UserBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True