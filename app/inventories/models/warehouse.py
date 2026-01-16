from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.core.database import Base
from datetime import datetime, timezone

class WareHouse(Base):
  __tablename__ = "warehouses"

  id = Column(Integer, primary_key=True)
  code = Column(String(50),unique=True, index =True)
  name = Column(String(255), nullable=False)
  location = Column(String(255))
  
  is_active = Column(Boolean, default=True)
  create_at = Column(DateTime, default = datetime.now(timezone.utc))