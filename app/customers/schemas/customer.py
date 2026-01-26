from typing import Optional
from pydantic import BaseModel, ConfigDict

class CustomerBase(BaseModel):
    code: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None

class CustomerResponse(CustomerBase):
    id: int
    is_active: bool
    
    model_config = ConfigDict(from_attributes=True)