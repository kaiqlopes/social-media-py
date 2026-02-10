from fastapi import Depends
from src.application.services.user_service import UserService
from src.infrastructure.repositories.user_repository import UserRepository


def get_user_repository() -> UserRepository:
    return UserRepository()


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repository)
