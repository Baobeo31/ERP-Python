from decimal import Decimal
from typing import List
from pydantic import BaseModel 

class SalesReturnItemCreate(BaseModel):
  product_id: int
  warehouse_id: int
  quantity: int
  price: Decimal

class SaleReturnCreate(BaseModel):
  sales_order_id: int
  customer_id: int
  items: List[SalesReturnItemCreate]

