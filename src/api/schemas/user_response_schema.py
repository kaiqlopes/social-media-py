from pydantic import BaseModel

from src.infrastructure.db.models.user_model import UserModel

class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str

    @classmethod
    def from_entity(cls, user: UserModel) -> "UserResponseSchema":
        return cls(
            id=user.id,
            name=user.name,
            email=user.email,
        )