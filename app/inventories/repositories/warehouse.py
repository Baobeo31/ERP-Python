from sqlalchemy.orm import Session
from app.inventories.models.warehouse import WareHouse
class WareHouseRepository:
    @staticmethod
    def get_by_id(db: Session, warehouse_id: int):
        return db.query(WareHouse).filter(WareHouse.id == warehouse_id).first()
    
    @staticmethod
    def create(db: Session, warehouse_id):
        return db.query(WareHouse).filter(WareHouse.id == warehouse_id).first()
    
    @staticmethod
    def get_by_code(db: Session, code: str):
        return db.query(WareHouse).filter(WareHouse.code == code).first()
    
    @staticmethod
    def list_active(db: Session):
        return db.query(WareHouse).filter(WareHouse.is_active == True).all()