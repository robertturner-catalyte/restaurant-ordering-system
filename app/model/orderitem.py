from __future__ import annotations
from typing import Optional
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.model import BaseModel


class OrderItem(BaseModel):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"), nullable=False
    )
    menu_item_id: Mapped[int] = mapped_column(
        ForeignKey("menu_items.id"), nullable=False
    )

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    item_price: Mapped[float] = mapped_column(Float, nullable=False)  
    note: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
    order: Mapped["Order"] = relationship(back_populates="items")
    menu_item: Mapped["MenuItem"] = relationship(back_populates="order_items")

    def __repr__(self) -> str:
        return (
            f"OrderItem(id={self.id}, order_id={self.order_id}, "
            f"menu_item_id={self.menu_item_id}, quantity={self.quantity}, "
            f"item_price={self.item_price})"
        )


__all__ = ["OrderItem"]
