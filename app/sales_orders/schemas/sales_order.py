from typing import List
from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from app.sales_orders.schemas.sales_order_item import SalesOrderItemCreate

class SaleOrderCreate(BaseModel):
  customer_id: int
  lines: List[SalesOrderItemCreate]

class SalesOrderResponse(BaseModel):
  id: int
  code: str
  total_amount: Decimal

  model_config = ConfigDict(from_attributes=True)