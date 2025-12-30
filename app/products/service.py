from app.products.model import Product
from app.products.repository import ProductRepository

class ProductService:

    @staticmethod
    def create_product(db, data):
        product = Product(**data.dict())
        return ProductRepository.create(db, product)

    @staticmethod
    def update_product(db, product_id, data):
        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            return None

        update_data = data.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(product, key, value) # gán giá trị mới cho các field được cập nhật

        return ProductRepository.update(db, product)
    
    @staticmethod
    def list_product(db):
        return ProductRepository.list(db)
