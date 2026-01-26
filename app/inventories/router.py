from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.inventories.repositories.inventory_transaction_repository import InventoryTransactionRepository
from app.inventories.schemas.warehouse import WareHouseCreate, WareHouseResponse
from app.inventories.services.warehouse import WareHouseService
from app.inventories.services.inventory import InventoryService
router = APIRouter(
    prefix = "/inventories",
    tags = ["Inventories"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

#WAREHOUSE

@router.post("/warehouse", response_model= WareHouseResponse)
def create_warehouse(data: WareHouseCreate, db: Session = Depends(get_db)):
    return WareHouseService.create(db, data)

@router.get("/warehouse", response_model= list[WareHouseResponse])
def list_warehouse(db: Session = Depends(get_db)):
    return WareHouseService.list(db)

@router.delete("/warehouse/{warehouse_id}", response_model= WareHouseResponse)
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    return WareHouseService.disable(db, warehouse_id)


#INVENTORY

#Xử lý kho hàng 
@router.post("/inbound")
def inbound(data: dict, db: Session = Depends(get_db)):
    return InventoryService.inbound(db, data)

#Xử lý đặt hàng
@router.post("/outbound")
def outbound(data: dict, db: Session = Depends(get_db)):
    return InventoryService.outbound(db, data)

#Xử lý điều chỉnh tồn kho
@router.post("/adjust")
def adjustment(data: dict, db: Session = Depends(get_db)):
    return InventoryService.adjust(db, data)

#Xử lý hủy đặt hàng
@router.post("/release")
def release(data: dict, db: Session = Depends(get_db)):
    return InventoryService.release(db, data)

#Xử lý đặt hàng
@router.get("/reserve")
def reserve(data: dict, db: Session = Depends(get_db)):
    return InventoryService.reserve(db, data)

#TRANSACTION

@router.get("/transaction")
def stock_movement(db: Session = Depends(get_db)):
    def get_inventory_transation(
        product_id: int | None = None,
        warehouse_id: int |None = None,
        db: Session = Depends(get_db),
    ):
       return InventoryTransactionRepository.filter(db, product_id, warehouse_id)