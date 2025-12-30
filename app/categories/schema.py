from pydantic import BaseModel,ConfigDict
from typing import Optional

class CategoryCreate(BaseModel):
    name: str 
    description: Optional[str] = None 

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class CategoryResponse(BaseModel):
    id: int 
    name: str 
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)