from app.inventories.models.inventory import Inventory

class InventoryRepository:
  @staticmethod
  def get(db, product_id, warehouse_id):
    return db.query(Inventory).filter(
      Inventory.product_id == product_id,
      Inventory.warehouse_id == warehouse_id
    ).first()
  
  # Tạo hoặc cập nhật tồn kho cho một sản phẩm
  @staticmethod
  def create(db, inventory):
    db.add(inventory)
    return inventory
  # Cập nhật số lượng tồn kho
  @staticmethod
  def increase(inventory: Inventory, qty: int):
    inventory.quantity += qty
  # Giảm số lượng tồn kho
  @staticmethod
  def decrease(inventory: Inventory, qty: int):
    inventory.quantity -= qty
# Cập nhật số lượng tồn kho đã được đặt trước
  @staticmethod
  def reserve(inventory: Inventory, qty: int):
    inventory.reserved_quantity += qty
# Hủy đặt trước
  @staticmethod
  def release(inventory: Inventory, qty: int):
    inventory.reserved_quantity -= qty
# Tính toán số lượng có sẵn
  @staticmethod
  def available_quantity(inventory: Inventory) -> int:
    return inventory.quantity - inventory.reserved_quantity