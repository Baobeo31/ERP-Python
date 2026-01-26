from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.sales_orders.schemas.sales_order import SaleOrderCreate, SalesOrderResponse
from app.sales_orders.services.sales_order import SalesOrderService
router = APIRouter(
    prefix = "/sales_orders",
    tags = ["Sales Orders"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SalesOrderResponse)
def create(data: SaleOrderCreate, db: Session = Depends(get_db)):
    return SalesOrderService.create(db, data)

@router.post("/{sales_order_id}/confirm", response_model=SalesOrderResponse)
def confirm(sales_order_id: int, db: Session = Depends(get_db)):
    return SalesOrderService.confirm(db, sales_order_id)

@router.post("/{sales_order_id}/cancel}")
def cancel(sales_order_id: int, db: Session = Depends(get_db)):
    return SalesOrderService.cancel(db, sales_order_id)