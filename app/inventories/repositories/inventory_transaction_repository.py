from sqlalchemy.orm import Session
from app.inventories.models.inventory_transaction import InventoryTransaction
class InventoryTransactionRepository:

  @staticmethod
  def create(db: Session, tx: InventoryTransaction):
    db.add(tx)
    return tx

  @staticmethod
  def filter(db:Session, product_id: int = None, warehouse_id: int = None):
    query = db.query(InventoryTransaction)

    if product_id is not None:
      query = query.filter(InventoryTransaction.product_id == product_id)

    if warehouse_id is not None:
      query = query.filter(InventoryTransaction.warehouse_id == warehouse_id)

    return query.order_by(InventoryTransaction.created_at.desc()).all()