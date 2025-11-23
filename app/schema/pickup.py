from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.schema.orderitem import OrderItemCreate, OrderItemRead


class PickupCreate(BaseModel):
    customer_name: Optional[str] = None
    customer_phone_number: Optional[str] = None
    items: List[OrderItemCreate]

    model_config = ConfigDict(extra="forbid")


class PickupRead(BaseModel):
    id: int
    order_type: str
    customer_name: Optional[str] = None
    customer_phone_number: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime
    picked_up_at: Optional[datetime] = None
    items: List[OrderItemRead]
