from src.domain.entities.user import User

class UserRepository:
    def __init__ (self):
        self.users: list[User] = [
            User(id=1, name="Kaique Lopes", email="kaiquelopes@python.com"),
            User(id=2, name="Gabriela Lopes", email="gabrielalopes@python.com"),
            User(id=3, name="Aurora Lopes", email="aurorinhalopes@python.com"),
            User(id=4, name="Fulano Python", email="fulanopython@python.com"),
            User(id=5, name="Sem ideias", email="comideias@python.com"),
        ]

    def get_user_by_id(self, user_id: int) -> User | None:
        return next((user for user in self.users if user.id == user_id), None)