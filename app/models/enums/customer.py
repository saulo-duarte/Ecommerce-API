import enum


class CustomerStatus(enum.Enum):
    ACTIVE = "active"
    BANNED = "banned"
    PENDING = "pending"
