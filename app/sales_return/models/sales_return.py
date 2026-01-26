from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone

#Chứng từ chính
class SalesReturn(Base):
  __tablename__ = "sales_returns"

  id = Column(Integer, primary_key=True)
  code = Column(String(50),unique=True, index =True)
  sales_order_id = Column(Integer, ForeignKey("sales_orders.id"), nullable=False)
  warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)

  status = Column(String, default="DRAFT")
  total_amount = Column(Numeric(12,2), default = 0)
  create_at = Column(DateTime, default=datetime.now(timezone.utc))

  items = relationship("SalesReturnItem", back_populates="sales_return", cascade="all, delete-orphan") #tự động xóa các bản ghi con khi xóa bản ghi cha