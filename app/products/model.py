from sqlalchemy import (
    Column, Integer, String, Numeric,
    ForeignKey, Boolean, DateTime
)
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    sku = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)

    price = Column(Numeric(12, 2), nullable=False)

    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True
    )

    category = relationship(
        "Category",
        back_populates="products"
    )

    # ERP soft delete
    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime, nullable=True)

    # Audit
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )

    inventories = relationship("Inventory", back_populates="product", lazy="selectin") #tránh n+1 query problem
