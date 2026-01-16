from typing import Optional
from pydantic import BaseModel, ConfigDict

class WareHouseBase(BaseModel):
  code: str
  name: str
  localtion: Optional[str] = None

class WareHouseCreate(WareHouseBase):
  pass

class WareHouseUpdate(WareHouseBase):
  name: Optional[str] = None
  localtion: Optional[str] = None
  is_active: Optional[bool] = None

class WareHouseResponse(WareHouseBase):
  id: int
  is_active: bool
  
  model_config = ConfigDict(from_attributes=True)