from app.sales_orders.models.sales_order_item import SalesOrderItem
import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone

class SalesOrderStatus(str, enum.Enum):
  DRAFT = "DRAFT"
  CONFIRMED = "CONFIRMED"
  SHIPPED = "SHIPPED"
  CANCELLED = "CANCELLED"


class SalesOrder(Base):
  __tablename__ = "sales_orders"

  id = Column(Integer, primary_key=True)
  code = Column(String(50),unique=True, index =True)
  customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
  warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
  
  status = Column(Enum(SalesOrderStatus), default=SalesOrderStatus.DRAFT)
  
  total_amount = Column(Float, default=0)
  create_at = Column(DateTime, default = datetime.now(timezone.utc))
  update_at = Column(DateTime, default = datetime.now(timezone.utc), onupdate = datetime.now(timezone.utc))
  confirm_at = Column(DateTime, nullable=True)
  cancelled_at = Column(DateTime, nullable=True)

  item = relationship("SalesOrderItem", back_populates="sales_order")