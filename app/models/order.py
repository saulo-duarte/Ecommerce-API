from datetime import datetime, timezone
from uuid import uuid4

from app.configs.database import Base
from app.models.enums.order import OrderStatus
from sqlalchemy import DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )

    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=False)

    coupon_id: Mapped[str] = mapped_column(ForeignKey("coupons.id"), nullable=True)

    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), default=OrderStatus.PENDING
    )
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), default=0.00)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan"
    )
    coupon = relationship("Coupon", back_populates="orders")
    payments = relationship(
        "Payment",
        back_populates="order",
        cascade="all, delete-orphan",
    )
