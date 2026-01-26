from decimal import Decimal
from pydantic import BaseModel

class SalesOrderItemCreate(BaseModel):
  product_id: int
  quantity: int
  price: Decimal