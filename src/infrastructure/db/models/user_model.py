from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import String
from src.infrastructure.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from src.infrastructure.db.models.post_model import PostModel   
    from src.infrastructure.db.models.post_comment_model import PostCommentModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True, index=True
    )

    posts: Mapped[list["PostModel"]] = relationship(
        "PostModel", 
        back_populates="author", 
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    comments: Mapped[list["PostCommentModel"]] = relationship(
        "PostCommentModel", 
        back_populates="author", 
        cascade="all, delete-orphan",
        passive_deletes=True
    )
