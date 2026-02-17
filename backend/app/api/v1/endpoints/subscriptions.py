from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.subscription import SubscriptionCreate, SubscriptionRead, SubscriptionUpdate
from app.services.subscription_service import SubscriptionService

router = APIRouter()

@router.post("/", response_model=SubscriptionRead, status_code=status.HTTP_201_CREATED)
def create_subscription(
    *,
    session: Session = Depends(get_db),
    subscription_in: SubscriptionCreate,
    current_user: User = Depends(get_current_user)
):
    """
    Create a new subscription for the current user.
    """
    service = SubscriptionService(session)
    return service.create_subscription(subscription_in, current_user.id)

@router.get("/", response_model=List[SubscriptionRead])
def read_subscriptions(
    session: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve all subscriptions for the current user.
    """
    service = SubscriptionService(session)
    return service.get_user_subscriptions(current_user.id, skip=skip, limit=limit)

@router.get("/{id}", response_model=SubscriptionRead)
def read_subscription(
    *,
    session: Session = Depends(get_db),
    id: UUID,
    current_user: User = Depends(get_current_user)
):
    """
    Get a specific subscription by ID.
    """
    service = SubscriptionService(session)
    return service.get_subscription_by_id(id, current_user.id)

@router.patch("/{id}", response_model=SubscriptionRead)
def update_subscription(
    *,
    session: Session = Depends(get_db),
    id: UUID,
    subscription_in: SubscriptionUpdate,
    current_user: User = Depends(get_current_user)
):
    """
    Update an existing subscription.
    """
    service = SubscriptionService(session)
    return service.update_subscription(id, subscription_in, current_user.id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subscription(
    *,
    session: Session = Depends(get_db),
    id: UUID,
    current_user: User = Depends(get_current_user)
):
    """
    Delete a subscription.
    """
    service = SubscriptionService(session)
    service.delete_subscription(id, current_user.id)
    return None