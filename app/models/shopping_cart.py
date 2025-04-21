from datetime import datetime, timezone
from typing import TYPE_CHECKING, List
from uuid import uuid4

from configs.database import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.cart_item import CartItem
    from models.customer import Customer


class ShoppingCart(Base):
    __tablename__ = "shopping_carts"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    customer: Mapped["Customer"] = relationship(
        "Customer", back_populates="shopping_cart"
    )
    items: Mapped[List["CartItem"]] = relationship(
        "CartItem", back_populates="cart", cascade="all, delete-orphan"
    )

    def total(self) -> float:
        return sum(float(item.total()) for item in self.items)
