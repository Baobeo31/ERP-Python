from sqlalchemy.orm import Session
from app.inventories.models.inventory_transaction import InventoryTransaction
class InventoryTransactionRepository:

  @staticmethod
  def create(db: Session, tx: InventoryTransaction):
    db.add(tx)
    return tx
