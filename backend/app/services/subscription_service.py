from typing import List
from uuid import UUID
from fastapi import HTTPException, status
from sqlmodel import Session
from app.models.subscription import Subscription
from app.repositories.subscription_repository import SubscriptionRepository
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate

class SubscriptionService:
    def __init__(self, session: Session):
        self.repository = SubscriptionRepository(session)

    def create_subscription(self, obj_in: SubscriptionCreate, user_id: UUID) -> Subscription:
        return self.repository.create(obj_in, user_id)

    def get_user_subscriptions(
        self, user_id: UUID, skip: int = 0, limit: int = 100
    ) -> List[Subscription]:
        return self.repository.get_multi_by_user(user_id, skip=skip, limit=limit)

    def get_subscription_by_id(self, subscription_id: UUID, user_id: UUID) -> Subscription:
        subscription = self.repository.get_by_id(subscription_id)
        
        if not subscription:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Subscription not found"
            )
        
        if subscription.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
            
        return subscription

    def update_subscription(
        self, subscription_id: UUID, obj_in: SubscriptionUpdate, user_id: UUID
    ) -> Subscription:
        db_obj = self.get_subscription_by_id(subscription_id, user_id)
        return self.repository.update(db_obj, obj_in)

    def delete_subscription(self, subscription_id: UUID, user_id: UUID) -> None:
        db_obj = self.get_subscription_by_id(subscription_id, user_id)
        self.repository.delete(db_obj)