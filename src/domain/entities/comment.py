from dataclasses import dataclass
from datetime import datetime

from src.domain.entities.post import Post
from src.domain.entities.user import User


@dataclass
class Comment:
    id: int
    text: str
    create_at: datetime
    post_id: int
    post: Post
    author_id: int
    author: User