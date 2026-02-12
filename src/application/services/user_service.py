from src.api.schemas.user_create_schema import UserCreateSchema
from src.api.schemas.user_response_schema import UserResponseSchema
from src.domain.exceptions.user_not_found_exception import UserNotFoundError
from src.infrastructure.db.models.user_model import UserModel
from src.infrastructure.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self._repo = repo

    def get_by_id(self, user_id: int) -> UserResponseSchema:
        user = self._repo.get_by_id(user_id)

        if user is None:
            raise UserNotFoundError("User not found")

        return UserResponseSchema.from_entity(user)
    
    def create(self, user: UserCreateSchema) -> UserResponseSchema:
        new_user = UserModel(name = user.name, email = str(user.email))

        self._repo.create(new_user)

        return UserResponseSchema.from_entity(new_user)