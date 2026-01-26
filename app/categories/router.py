from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from .schema import CategoryCreate, CategoryResponse, CategoryUpdate
from .service import CategoryService


router = APIRouter(prefix="/categories", tags=["Categories"])
def get_db(): # Hàm phụ trợ để lấy phiên làm việc cơ sở dữ liệu
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Tạo danh mục
@router.post("/", response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return CategoryService.create_category(db, data)

# Sửa danh mục
@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    return CategoryService.update_category(db, category_id, data)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)): 
     CategoryService.delete_category(db, category_id)
     return {"message" : "Category deleted successfully"}

# Lấy tất cả danh mục
@router.get("", response_model=list[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    return CategoryService.list_categories(db)