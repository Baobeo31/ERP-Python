from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from app.core.database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Inventory(Base):
  __tablename__ = "inventories"

  id = Column(Integer, primary_key=True)
  product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
  warehouse_id = Column(Integer, ForeignKey("warehouses.id", ondelete="CASCADE"), nullable=False)
  
  quantity = Column(Integer, default=0) # Số lượng hiện có trong kho
  reserved_quantity = Column(Integer, default=0) # Số lượng đã được đặt trước

  updated_at = Column(DateTime, default = datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc)) 


  product = relationship("Product", back_populates="inventories")
  warehouse = relationship("Warehouse", back_populates="inventories")


  __table_args__ = (UniqueConstraint("product_id", "warehouse_id"),) # Đảm bảo mỗi sản phẩm trong mỗi kho chỉ có một bản ghi
