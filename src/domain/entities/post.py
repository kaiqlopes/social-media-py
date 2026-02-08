from dataclasses import dataclass, field

from src.domain.entities.comment import Comment
from src.domain.entities.user import User


@dataclass
class Post:
    id: int
    author_id: int
    author: User
    text: str
    image_url: str
    comment_ids: set[int] = field(default_factory=set)
    comments: list[Comment] = field(default_factory=list)