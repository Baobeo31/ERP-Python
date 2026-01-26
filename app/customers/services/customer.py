from app.customers.models.customer import Customer
from app.customers.repositories.customer import CustomerRepository
class CustomerService:

  @staticmethod
  def create(db, data):
    if CustomerRepository.get_by_code(db, data.code):
      raise Exception(400,"Mã khách hàng đã tồn tại")
    
    customer = Customer(**data.model_dump())
    CustomerRepository.create(db, customer)

    db.commit()
    db.refresh(customer)

    return customer

  @staticmethod
  def list(db):
    return CustomerRepository.list_active(db)


