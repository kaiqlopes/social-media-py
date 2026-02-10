from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.entities.post import Post
    from src.domain.entities.user import User


@dataclass
class Comment:
    id: int
    text: str
    create_at: datetime
    post_id: int
    post: "Post"
    author_id: int
    author: "User"