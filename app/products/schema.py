from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from typing import Optional

class CategoryResponse(BaseModel): 
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ProductBase(BaseModel):
    code: str
    name: str
    price: Decimal
    stock: int


class ProductCreate(ProductBase):
    category_id: Optional[int] = None


class ProductUpdate(BaseModel): #Field nào gửi lên sẽ được cập nhật
    code: Optional[str] = None
    name: Optional[str] = None
    price: Optional[Decimal] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None


class ProductResponse(ProductBase):
    id: int
    category: Optional[CategoryResponse] 

    model_config = ConfigDict(from_attributes=True) 
