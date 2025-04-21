from datetime import datetime, timezone
from uuid import uuid4

from configs.database import Base
from enums.payment import PaymentMethod, PaymentStatus
from sqlalchemy import DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"), nullable=False)

    method: Mapped[PaymentMethod] = mapped_column(Enum(PaymentMethod), nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus), default=PaymentStatus.PENDING
    )

    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    transaction_id: Mapped[str] = mapped_column(String(100), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    order = relationship("Order", back_populates="payments")
