from pydantic import BaseModel, ConfigDict
from decimal import Decimal

class SalesReturnResponse(BaseModel):
  id: int
  code: str
  status: str
  total_amount: Decimal

  model_config = ConfigDict(from_attributes=True) 