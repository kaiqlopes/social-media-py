from fastapi import Depends
from src.application.services.user_service import UserService
from src.infrastructure.db.session import get_session
from src.infrastructure.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session


def get_user_repository(db: Session = Depends(get_session)) -> UserRepository:
    return UserRepository(db)


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repository)
