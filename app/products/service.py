from app.products.model import Product
from app.products.repository import ProductRepository
from app.categories.repository import CategoryRepository
from fastapi import HTTPException

class ProductService:

    @staticmethod
    def create_product(db, data):
        if data.category_id:
            category = CategoryRepository.get_by_id(db, data.category_id)
            if not category:
                raise HTTPException(status_code=400, detail="Category does not exist")
        product = Product(**data.dict())
        return ProductRepository.create(db, product)

    @staticmethod
    def update_product(db, product_id, data):
        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            return None

        update_data = data.model_dump(exclude_unset=True) 
        if "category_id" in update_data:
            if update_data["category_id"] is not None:
                category = CategoryRepository.get_by_id(db, update_data["category_id"])
                if not category:
                    raise HTTPException(status_code=400, detail="Category does not exist")

        for field, value in update_data.items():
            setattr(product, field, value) # gán giá trị mới cho các field được cập nhật

        return ProductRepository.update(db, product)
    @staticmethod
    def delete_product(db, product_id):
        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            return None

        return ProductRepository.delete(db, product)

    @staticmethod
    def list_product(db):
        return ProductRepository.list(db)
