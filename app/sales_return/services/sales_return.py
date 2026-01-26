from datetime import datetime
from app.sales_return.models.sales_return import SalesReturn
from app.sales_return.models.sales_return_item import SalesReturnItem
from app.sales_return.repositories.sales_return_repository import SalesReturnRepository
from decimal import Decimal
from app.inventories.services.inventory import InventoryService
from fastapi import HTTPException
from app.sales_return.models.enum import SalesReturnStatus
class SaleReturnService:

  @staticmethod
  def create(db, data):
    return_order = SalesReturn(
      sale_order_id =data.sale_order_id,
      customer_id = data.customer_id,
      code = f"SR{int(datetime.now().timestamp())}"
    )
    total = Decimal(0)

    for line in data.items:
      item = SalesReturnItem(
        product_id = line.product_id,
        warehouse_id = line.warehouse_id,
        quantity = line.quantity,
        price = line.price
      )
      return_order.items.append(item)
      total += item.quantity * item.price

    return_order.total_amount = total
    SalesReturnRepository.create(db, return_order)
  
    db.commit()
    db.refresh(return_order)
    return return_order
  
  @staticmethod
  def confirm(db, return_id):
    return_order = SalesReturnRepository.get_by_id(db, return_id)

    if not return_order:
      raise HTTPException(404, detail="Return order not found")
    if return_order.status != "DRAFT":
      raise HTTPException(400, detail="Return order already confirmed")
    
    for item in return_order.items:
      InventoryService.inbound(
        db,
        product_id = item.product_id,
        warehouse_id = item.warehouse_id,
        quantity = item.quantity,
        ref = return_order.code
      )

    return_order.status = SalesReturnStatus.RECEIVED
    db.commit()
    return return_order
  
  @staticmethod 
  def cancelI(db, return_id):
    return_order = SalesReturnRepository.get_by_id(db, return_id)

    if not return_order:
      raise HTTPException(404, detail="Return order not found")
    
    if return_order.status != "DRAFT":
      raise HTTPException(400, detail="Only DRAFT can be canccelled")
    
    return_order.status = SalesReturnStatus.CANCELLED
    db.commit()
    return return_order