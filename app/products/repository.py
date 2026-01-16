from sqlalchemy.orm import Session
from app.products.model import Product

class ProductRepository:

    @staticmethod
    def create(db: Session, product: Product):
        db.add(product)
        return product

    @staticmethod
    def get_by_id(db: Session, product_id: int):
        return (
            db.query(Product)
            .filter(
                Product.id == product_id,
                Product.is_active == True
            )
            .first()
        )

    @staticmethod
    def list_active(db: Session):
        return (
            db.query(Product)
            .filter(Product.is_active == True)
            .all()
        )

    @staticmethod
    def update(db: Session, product: Product):
        db.add(product)
        return product
