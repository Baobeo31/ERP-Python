from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.sales_return.schemas.sale_return_create import SaleReturnCreate
from app.sales_return.schemas.sales_return_response import SalesReturnResponse
from app.sales_return.services.sales_return import SaleReturnService
router = APIRouter(
    prefix = "/sales_returns",
    tags = ["Sales Returns"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SalesReturnResponse)
def create_sales_return(data: SaleReturnCreate, db: Session = Depends(get_db)):
    return SaleReturnService.create_sales_return(db, data)

@router.post("{sales_return_id}/confirm")
def confirm_sales_return(sales_return_id: int, db: Session = Depends(get_db)):
    return SaleReturnService.confirm_sales_return(db, sales_return_id)

@router.post("/{sales_return_id}/cancel")
def cancel_sales_return(sales_return_id: int, db: Session = Depends(get_db)):
    return SaleReturnService.cancel_sales_return(db, sales_return_id)   

