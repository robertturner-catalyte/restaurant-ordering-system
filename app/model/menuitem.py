from sqlalchemy import Boolean, Float, Integer, String, null
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel


class MenuItem(BaseModel):
    __tablename__= "menu_items"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, auto_increment=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean(), nullable= False, default= True)

    def __repr__(self):
        return f"MenuItem(id={self.id}, name={self.name}, category={self.category}, price={self.price}, active={self.active})"
    
__all__= ["MenuItem"]