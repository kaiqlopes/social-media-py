from src.api.schemas.user_schema import UserSchema
from src.domain.exceptions.user_not_found_exception import UserNotFoundError
from src.infrastructure.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> UserSchema:
        user = self._user_repository.get_user_by_id(user_id)

        if user is None:
            raise UserNotFoundError("User not found")

        return UserSchema.from_entity(user)