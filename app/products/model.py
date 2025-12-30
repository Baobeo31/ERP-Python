from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    stock = Column(Integer, default=0)

    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="SET NULL"), # Khi danh mục bị xóa, đặt category_id thành NULL
        nullable=True
    )

    category = relationship(
        "Category",
        back_populates="products" # Thêm back_populates để liên kết hai chiều
    )
