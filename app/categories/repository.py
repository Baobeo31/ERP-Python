from sqlalchemy.orm import Session 
from app.categories.model import Category

class CategoryRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Category).all()

    @staticmethod
    def list_active(db: Session):
        return db.query(Category).filter(Category.is_active == True).all()

    @staticmethod
    def get_by_id(db: Session, category_id: int):
        return db.query(Category).filter(Category.id == category_id).first()

    @staticmethod
    def get_by_name(db: Session, name: str):
        return db.query(Category).filter(Category.name == name).first()

    @staticmethod
    def create(db: Session, category: Category):
        db.add(category)
        return category

    @staticmethod
    def update(db: Session, category: Category):
        db.add(category)
        return category
