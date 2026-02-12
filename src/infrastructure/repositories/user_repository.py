from sqlalchemy import select
from sqlalchemy.orm import Session

from src.infrastructure.db.models.user_model import UserModel

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: UserModel) -> UserModel:
        self.session.add(user)
        self.session.commit()

        return user

    def get_by_id(self, id: int) -> UserModel | None:
        query = select(UserModel).where(UserModel.id == id)
        return self.session.execute(query).scalar_one_or_none()
    