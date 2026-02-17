# backend/app/models/subscription.py
from datetime import date
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4

if TYPE_CHECKING:
    from app.models.user import User

class Subscription(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True)
    price: float
    currency: str = Field(default="BRL")
    renewal_period: str = Field(default="monthly")  # monthly, yearly, etc.
    next_payment_date: date
    status: str = Field(default="active")
    
    # Foreign Key
    user_id: UUID = Field(foreign_key="users.id", nullable=False)
    
    # Relationship
    user: Optional["User"] = Relationship(back_populates="subscriptions")