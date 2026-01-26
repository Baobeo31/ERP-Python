from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.core.database import Base
from datetime import datetime, timezone
class Customer:
  __tablename__ = "customers"

  id = Column(Integer, primary_key=True)
  code = Column(String(50),unique=True, index =True)
  name = Column(String(255), nullable=False)
  email = Column(String(255), nullable=True)
  phone = Column(String(255), nullable=True)
  address = Column(String(255), nullable=True)

  is_active = Column(Boolean, default=True)

  created_at = Column(DateTime, default = datetime.now(timezone.utc))
  updated_at = Column(DateTime, default = datetime.now(timezone.utc), onupdate = datetime.now(timezone.utc))

