from app.core.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
class SalesOrderItem(Base):
    __tablename__ = "sales_order_items"

    id = Column(Integer, primary_key=True)
    sales_order_id = Column(Integer, ForeignKey("sales_orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable = False)
    price = Column(Numeric(12, 2), nullable=False)
    subtotal = Column(Numeric(14, 2), nullable=False)

    order = relationship("SalesOrder", back_populates="item")