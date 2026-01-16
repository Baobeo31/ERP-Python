from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime
class InventoryTransactionResponse(BaseModel):
  product_id: int
  warehouse_id: int
  quantity: int
  type: str
  created_at: datetime

  model_config = ConfigDict(from_attributes=True)  # giúp Pydantic hiểu cách lấy dữ liệu từ SQLAlchemy