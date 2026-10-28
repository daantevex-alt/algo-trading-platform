from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import String, ForeignKey, Text, Numeric


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "app_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    age: Mapped[int] = mapped_column(nullable=False)

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user")
    strategies: Mapped[list["Strategy"]] = relationship("Strategy", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("app_users.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="orders")


class Strategy(Base):
    __tablename__ = "strategies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    strategy_type: Mapped[str] = mapped_column(String(50), nullable=False)

    budget: Mapped[float | None] = mapped_column(Numeric(18, 8), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("app_users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="strategies")
