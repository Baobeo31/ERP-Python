from datetime import datetime, timezone
import enum
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from app.core.database import Base

class InventoryTransactionType(str, enum.Enum):
    INBOUND = "INBOUND" # Nhập hàng
    OUTBOUND = "OUTBOUND" # Xuất hàng
    ADJUST = "ADJUST" # Sửa đổi
    RESERVE = "RESERVE" # Đặt hàng
    RELEASE = "RELEASE" # Hủy đặt hàng


class InventoryTransaction(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    type = Column(Enum(InventoryTransactionType), nullable=False)

    ref_type = Column(String, nullable=True)  # Loại tham chiếu, ví dụ: 'order', 'purchase', v.v.
    ref_id = Column(Integer, nullable=True)  # ID tham chiếu đến đơn hàng, phiếu nhập kho, v.v.
    note = Column(String, nullable=True)  # Ghi chú bổ sung về giao dịch

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
