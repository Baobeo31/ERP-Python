from pydantic import BaseModel, ConfigDict 

class InventoryInbound(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int

class InventoryOutbound(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int

class InventoryReserve(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int

class InventoryResponse(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int
    reserved_quantity: int

model_config = ConfigDict(from_attributes=True) # giúp Pydantic hiểu cách lấy dữ liệu từ SQLAlchemy