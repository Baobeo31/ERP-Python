from app.categories.model import Category
from app.categories.repository import CategoryRepository
from fastapi import HTTPException
class CategoryService:

  @staticmethod
  def create_category(db, data):
        if CategoryRepository.get_by_name(db, data.name):
            raise HTTPException(status_code=400, detail="Category name already exists")
        category = Category(**data.dict())
        return CategoryRepository.create(db, category)
  
  @staticmethod
  def update_category(db, category_id, data):
      category = CategoryRepository.get_by_id(db, category_id)

      if not category:
          raise HTTPException(status_code=404, detail="Category not found")

      update_data = data.dict(exclude_unset=True)

      for key, value in update_data.items():
          setattr(category, key, value) # gán giá trị mới cho các field được cập nhật

      return CategoryRepository.update(db, category)
  
  @staticmethod
  def delete_category(db, category_id):
      category = CategoryRepository.get_by_id(db, category_id)

      if not category:
          raise HTTPException(status_code=404, detail="Category not found")

      return CategoryRepository.delete(db, category)
  
  @staticmethod
  def list_categories(db):
      return CategoryRepository.get_all(db)