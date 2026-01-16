from app.inventories.repositories.inventory_repository import InventoryRepository
from app.inventories.repositories.inventory_transaction_repository import InventoryTransactionRepository
from app.inventories.models.inventory import Inventory
from app.inventories.models.inventory_transaction  import InventoryTransaction, InventoryTransactionType
class InventoryService:

# Hàm này xử lý việc nhập kho hàng
  def inbound(db, prodduct_id: int, warehouse_id: int, quantity: int, ref = None):
    inventory = InventoryRepository.get(db, prodduct_id, warehouse_id)
    if quantity <= 0:
      raise Exception("Số lượng nhập phải lớn hơn 0")
    if not inventory:
      inventory = Inventory(product_id=prodduct_id, warehouse_id=warehouse_id, quantity=0)
      InventoryRepository.create(db, inventory)

      InventoryRepository.increase(inventory, quantity)
    tx = InventoryTransaction(
          product_id=prodduct_id,
          warehouse_id=warehouse_id,
          quantity=quantity,
          type=InventoryTransactionType.INBOUND,
          ref_id=ref
    )
    InventoryTransactionRepository.create(db, tx)

    db.commit()
    return inventory

#
  def outbound(db, product_id: int, warehouse_id: int, quantity: int, ref = None):
    inventory = InventoryRepository.get(db, product_id, warehouse_id)
    if quantity <= 0:
      raise Exception("Số lượng xuất phải lớn hơn 0")
    if not inventory: 
      raise Exception("Không đủ hàng")
    available = inventory.quantity - inventory.reserved_quantity
    if available < quantity: # kiểm tra hàng tồn kho khả dụng
      raise Exception("Không đủ hàng")

    InventoryRepository.decrease(inventory, quantity)

    tx = InventoryTransaction(
          product_id=product_id,
          warehouse_id=warehouse_id,
          quantity=quantity,
          type=InventoryTransactionType.OUTBOUND,
          ref_id=ref
    )
    InventoryTransactionRepository.create(db, tx)

    db.commit()
    return inventory
    

# Hàm này xử lý việc đặt hàng (dự trữ hàng)
  def reserve(db, product_id: int, warehouse_id: int, quantity: int, ref = None):
    inventory = InventoryRepository.get(db, product_id, warehouse_id)

    if quantity <= 0:
      raise Exception("Số lượng đặt phải lớn hơn 0")
    
    if not inventory:
      raise Exception("Không đủ hàng")
    
    avalible = inventory.quantity - inventory.reserved_quantity 
    if avalible < quantity:
      raise Exception("Không đủ hàng")
    
    InventoryRepository.reserve(inventory, quantity)
    
    tx = InventoryTransaction(
          product_id=product_id,
          warehouse_id=warehouse_id,
          quantity=quantity,
          type=InventoryTransactionType.RESERVE,
          ref_id=ref
    )
    InventoryTransactionRepository.create(db, tx)

    db.commit()
    return inventory

#Hàm này xử lý việc hủy đặt hàng (giải phóng hàng đã đặt)
  def release(db, product_id: int, warehouse_id: int, quantity: int, ref = None):
    inventory = InventoryRepository.get(db, product_id, warehouse_id)
    if quantity <= 0:
      raise Exception("Số lượng hủy đặt phải lớn hơn 0")
    if not inventory or inventory.reserved_quantity < quantity: # kiểm tra hàng đã đặt và tồn kho khả dụng
      raise Exception("Không đủ hàng đã đặt")
    
    InventoryRepository.release(inventory, quantity) # Giải phóng hàng đã đặt
    
    tx = InventoryTransaction(
          product_id=product_id,
          warehouse_id=warehouse_id,
          quantity=quantity,
          type=InventoryTransactionType.RELEASE,
          ref_id=ref
    )
    InventoryTransactionRepository.create(db, tx)
    db.commit()
    return inventory
    
  # Hàm này xử lý việc điều chỉnh tồn kho
  def adjust(db, product_id: int, warehouse_id: int, new_quantity: int, ref = None):
    inventory = InventoryRepository.get(db, product_id, warehouse_id)

    if new_quantity < 0:
      raise Exception("Số lượng tồn kho không được âm")
     
    if not inventory:
      raise Exception("Tồn kho không tồn tại")
    
    if inventory.reserved_quantity > new_quantity:
      raise Exception("Số lượng đã đặt trước lớn hơn số lượng tồn kho mới")
    
    delta = new_quantity - inventory.quantity

    if delta == 0 :
      return inventory  # Không có thay đổi
    
    tx = InventoryTransaction(
          product_id=product_id,
          warehouse_id=warehouse_id,
          quantity=delta,
          type=InventoryTransactionType.ADJUST,
          ref_id=ref
    )
    InventoryTransactionRepository.create(db, tx)
    inventory.quantity = new_quantity
    db.commit()
    return inventory