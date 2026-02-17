from datetime import date
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict

# Common fields for Subscription
class SubscriptionBase(BaseModel):
    name: str
    price: float
    currency: str = "BRL"
    renewal_period: str = "monthly"
    next_payment_date: date
    status: str = "active"

    model_config = ConfigDict(from_attributes=True)

# Properties to receive via API on creation
class SubscriptionCreate(SubscriptionBase):
    pass

# Properties to receive via API on update (All optional)
class SubscriptionUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    renewal_period: Optional[str] = None
    next_payment_date: Optional[date] = None
    status: Optional[str] = None

# Properties to return via API
class SubscriptionRead(SubscriptionBase):
    id: UUID
    user_id: UUID