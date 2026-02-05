from pydantic import BaseModel

from src.domain.entities.user import User

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    @classmethod
    def from_entity(cls, user: User) -> "UserSchema":
        return cls(
            id=user.id,
            name=user.name,
            email=user.email,
        )