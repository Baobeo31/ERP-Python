from datetime import datetime, timezone
from fastapi import HTTPException
from app.categories.model import Category
from app.categories.repository import CategoryRepository

class CategoryService:

    @staticmethod
    def create_category(db, data):
        if CategoryRepository.get_by_name(db, data.name):
            raise HTTPException(
                status_code=400,
                detail="Category name already exists"
            )

        category = Category(**data.model_dump())

        CategoryRepository.create(db, category)

        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def update_category(db, category_id, data):
        category = CategoryRepository.get_by_id(db, category_id)

        if not category or not category.is_active:
            raise HTTPException(status_code=404, detail="Category not found")

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(category, key, value)

        CategoryRepository.update(db, category)

        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def delete_category(db, category_id):
        category = CategoryRepository.get_by_id(db, category_id)

        if not category or not category.is_active:
            raise HTTPException(status_code=404, detail="Category not found")

        category.is_active = False
        category.deleted_at = datetime.now(timezone.utc)

        CategoryRepository.update(db, category)

        db.commit()

        return category

    @staticmethod
    def list_categories(db):
        return CategoryRepository.list_active(db)
