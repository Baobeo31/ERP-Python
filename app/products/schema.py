from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
class ProductCreate(BaseModel):
  code: str
  name: str
  price: Decimal
  stock: int

class ProductUpdate(BaseModel):
   #update từng field một cách tùy chọn
   code: Optional[str] = None
   name: Optional[str] = None
   price: Optional[Decimal] = None
   stock: Optional[int] = None
class ProductResponse(ProductCreate):
  id:int

  class Config:
        orm_mode = True