from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy import Enum
from app.core.database import Base

class SalesReturnItem(Base):
  __tablename__ = "sales_return_items"

  id = Column(Integer, primary_key=True)

  sales_returns_id = Column(Integer, ForeignKey("sales_returns.id"), nullable=False)
  product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
  warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)

  quantity = Column(Integer, default=0)
  price = Column(Float, default=0)
  
  sales_returns = relationship("SalesReturn", back_populates="item")