from __future__ import annotations
from dataclasses import dataclass, field

from src.domain.entities.post import Post


@dataclass
class User:
    id: int
    name: str
    email: str
    friends: set[User] = field(default_factory=set)
    friend_ids: set[int] = field(default_factory=set)
    posts: set[Post] = field(default_factory=set)
    post_ids: set[int] = field(default_factory=set)
