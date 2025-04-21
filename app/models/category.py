from typing import Optional
from uuid import uuid4

from configs.database import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    parent_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("categories.id"), nullable=True
    )
    parent: Mapped["Category"] = relationship(
        "Category", remote_side=[id], backref="subcategories"
    )

    products = relationship("Product", back_populates="category")

    @property
    def full_path(self) -> str:
        if self.parent:
            return f"{self.parent.full_path} > {self.name}"
        return self.name if self.name else ""
