from app.inventories.models.warehouse import WareHouse
from app.inventories.repositories.warehouse import WareHouseRepository
class WareHouseService:

  @staticmethod 
  def create(db, data): 
    warehouse = WareHouseRepository.get_by_code(db, data.code)
    if warehouse:
      raise Exception("Mã kho đã tồn tại")
    
    warehouse = WareHouse(**data.dict()) # tạo đối tượng kho hàng từ dữ liệu đầu vào
    WareHouseRepository.create(db, warehouse)
    db.commit()
    return warehouse

  @staticmethod
  def update(db, warehouse_id, data):
    warehouse = WareHouseRepository.get_by_code(db, warehouse_id)
    if not warehouse:
      raise Exception("Mã kho không tồn tại")
    for key, value in data.dict(exclude_unset=True).items():
      setattr(warehouse, key, value)

      db.commit()
      db.refresh(warehouse)
      return warehouse
    
  @staticmethod
  def disable(db, warehouse_id):
    warehouse = WareHouseRepository.get_by_id(db, warehouse_id)
    if not warehouse:
      raise Exception("Mã kho không tồn tại")
    warehouse.is_active = False
    db.commit()
    db.refresh(warehouse) 
    return warehouse
  
  @staticmethod 
  def list(db):
    return WareHouseRepository.list_active(db)