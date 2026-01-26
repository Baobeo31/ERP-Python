from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.customers.schemas.customer import CustomerCreate, CustomerResponse
from app.customers.services.customer import CustomerService
router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.post("/", response_model=CustomerResponse)
def create(data: CustomerCreate, db: Session = Depends(get_db)):
  return CustomerService.create(db, data)

@router.get("/", response_model=list[CustomerResponse])
def get_all(db: Session = Depends(get_db)):
  return CustomerService.list(db)