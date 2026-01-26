from app.sales_return.models.sales_return import SalesReturn
class SalesReturnRepository:
  @staticmethod
  def create(db, return_order):
    db.add(return_order)
    return return_order
  @staticmethod
  def get_by_id(db, return_id):
    return db.query(SalesReturn).filter_by(id=return_id).first()