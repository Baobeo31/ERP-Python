from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from .schema import ProductUpdate, ProductCreate, ProductResponse
from .service import ProductService
from fastapi import HTTPException
router = APIRouter(prefix="/products", tags=["Products"])

def get_db(): 
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
# Tạo sản phẩm
@router.post("/", response_model=ProductResponse) 
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
  return ProductService.create_product(db, data)

# Lấy tất cả sản phẩm
@router.get("/", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
  return ProductService.list_product(db)
# Cập nhật sản phẩm
@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return ProductService.update_product(db, product_id, data)
@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = ProductService.delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product