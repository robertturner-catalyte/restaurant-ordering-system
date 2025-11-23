from pydantic import BaseModel
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class OrderItem(BaseModel): 
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    menu_item_id: Mapped[int] = mapped_column(ForeignKey("menu_items.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer(), nullable= False)
    item_price: Mapped[float] = mapped_column(Float(), nullable=False)
    note: Mapped[str] = mapped_column(String(300), nullable=True)

    

    def __repr__(self):
        return f"OrderItem(id={self.id}, order_id={self.order_id}, menu_item_id={self.menu_item_id}, quantity={self.quantity}, item_price={self.item_price}, note={self.note})"
    
__all__= ["OrderItem"]