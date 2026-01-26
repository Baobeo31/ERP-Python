from app.sales_orders.models.sales_order import SalesOrder
from sqlalchemy.orm import Session
class SalesOrderRepository:

  @staticmethod
  def create (db: Session, order: SalesOrder):
    db.add(order)
    return order
  @staticmethod
  def get_by_id(db: Session, order_id: int):
    return db.query(SalesOrder).filter(SalesOrder.id == order_id).first(
      
    )