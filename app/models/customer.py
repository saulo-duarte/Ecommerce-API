from datetime import datetime, timezone
from uuid import uuid4

from app.configs.database import Base
from app.models.enums.customer import CustomerStatus
from sqlalchemy import DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)

    classification: Mapped[str] = mapped_column(String(50), default="standard")
    status: Mapped[CustomerStatus] = mapped_column(
        Enum(CustomerStatus), default=CustomerStatus.ACTIVE
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    addresses = relationship(
        "Address", back_populates="customer", cascade="all, delete-orphan"
    )

    orders = relationship(
        "Order", back_populates="customer", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (
            f"<Customer(id={self.id!r}, name={self.name!r}, email={self.email!r}, "
            f"classification={self.classification!r}, status={self.status.name})>"
        )
