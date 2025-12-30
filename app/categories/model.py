from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=True)

    # Quan hệ 1-N
    products = relationship(
        "Product",
        back_populates="category", # Thêm back_populates để liên kết hai chiều
        cascade="all, delete-orphan" # Khi xóa một danh mục, tất cả sản phẩm liên quan cũng bị xóa
    )
