from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

class Order(BaseModel):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    order_type: Mapped[str] = mapped_column(String(50), nullable=False)
    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)
    total_amount: Mapped[float] = mapped_column(Float(), nullable= False)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="new")
    created_at: Mapped[str] = mapped_column(DateTime(50), nullable=False)
    updated_at: Mapped[str] = mapped_column(DateTime(50), nullable=False)
    picked_up_at: Mapped[str] = mapped_column(DateTime(50), nullable=True)

    

    def __repr__(self):
        return f"Order(id={self.id}, order_type={self.order_type}, customer_name={self.customer_name}, total_amount={self.total_amount}, status={self.status}, created_at={self.created_at}, updated_at={self.updated_at}, picked_up_at={self.picked_up_at})"

__all__= ["Order"]