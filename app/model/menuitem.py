from typing import Optional
from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.model import BaseModel


class MenuItem(BaseModel):
    __tablename__ = "menu_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="menu_item", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (
            f"MenuItem(id={self.id}, name={self.name}, "
            f"category={self.category}, price={self.price}, active={self.active})"
        )


__all__ = ["MenuItem"]
