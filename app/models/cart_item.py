from typing import TYPE_CHECKING
from uuid import uuid4

from app.configs.database import Base
from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.shopping_cart import ShoppingCart

if TYPE_CHECKING:
    from models.product import Product


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    cart_id: Mapped[str] = mapped_column(
        ForeignKey("shopping_carts.id"), nullable=False
    )
    cart: Mapped["ShoppingCart"] = relationship("ShoppingCart", back_populates="items")

    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), nullable=False)
    product: Mapped["Product"] = relationship("Product")

    def total(self) -> float:
        return self.quantity * self.price
