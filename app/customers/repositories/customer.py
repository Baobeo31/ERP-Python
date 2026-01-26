from app.customers.models.customer import Customer
from sqlalchemy.orm import Session
class CustomerRepository:
  @staticmethod
  def get_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()
  
  @staticmethod
  def get_by_code(db: Session, code: str):
    return db.query(Customer).filter(Customer.code == code).first()
  
  @staticmethod
  def create(db: Session, customer: Customer):
    db.add(customer)
    return customer
  
  @staticmethod
  def list_active(db: Session):
    return db.query(Customer).filter(Customer.is_active == True).all()