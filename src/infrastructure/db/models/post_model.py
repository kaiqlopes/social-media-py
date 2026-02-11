from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Text
from src.infrastructure.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.infrastructure.db.models.user_model import UserModel
    from src.infrastructure.db.models.post_comment_model import PostCommentModel


class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)

    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )

    author: Mapped["UserModel"] = relationship("UserModel", back_populates="posts")

    comments: Mapped[list["PostCommentModel"]] = relationship(
        "PostCommentModel", 
        back_populates="post", 
        cascade="all, delete-orphan", 
        passive_deletes=True
    )
