from typing import List, Optional
from uuid import UUID
from sqlmodel import Session, select
from app.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate

class SubscriptionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, obj_in: SubscriptionCreate, user_id: UUID) -> Subscription:
        # Converts schema to SQLModel and attaches the user_id
        db_obj = Subscription.model_validate(obj_in, update={"user_id": user_id})
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def get_by_id(self, subscription_id: UUID) -> Optional[Subscription]:
        return self.session.get(Subscription, subscription_id)

    def get_multi_by_user(
        self, user_id: UUID, skip: int = 0, limit: int = 100
    ) -> List[Subscription]:
        statement = (
            select(Subscription)
            .where(Subscription.user_id == user_id)
            .offset(skip)
            .limit(limit)
        )
        return list(self.session.exec(statement).all())

    def update(
        self, db_obj: Subscription, obj_in: SubscriptionUpdate
    ) -> Subscription:
        # Converts schema to dict, excluding fields that were not provided (unset)
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: Subscription) -> None:
        self.session.delete(db_obj)
        self.session.commit()