from sqlalchemy.orm import Session
from app.products.model import Product

class ProductRepository:

    @staticmethod
    def create(db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_by_id(db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def list(db: Session):
        return db.query(Product).all()
    @staticmethod
    def update(db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    