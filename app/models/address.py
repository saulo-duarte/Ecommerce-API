from datetime import datetime, timezone
from uuid import uuid4

from app.configs.database import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )
    customer_id: Mapped[str] = mapped_column(ForeignKey("customers.id"), nullable=False)

    street: Mapped[str] = mapped_column(String(150))
    number: Mapped[str] = mapped_column(String(20))
    complement: Mapped[str] = mapped_column(String(100), nullable=True)
    city: Mapped[str] = mapped_column(String(100))
    state: Mapped[str] = mapped_column(String(100))
    country: Mapped[str] = mapped_column(String(100))
    zipcode: Mapped[str] = mapped_column(String(20))

    is_primary: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    customer = relationship("Customer", back_populates="addresses")
