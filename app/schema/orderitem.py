from pydantic import BaseModel, ConfigDict


class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int
    note: str | None = None

    
    model_config = ConfigDict(extra="forbid")


class OrderItemRead(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    sale_price: float
    note: str | None = None
