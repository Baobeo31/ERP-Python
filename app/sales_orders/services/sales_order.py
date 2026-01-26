from app.inventories.services.inventory import InventoryService
from app.sales_orders.models.sales_order import SalesOrder
from app.sales_orders.models.sales_order_item import SalesOrderItem
from app.sales_orders.repositories.sales_order_repository import SalesOrderRepository
from app.customers.repositories.customer import CustomerRepository
from app.sales_orders.schemas.sales_order import SaleOrderCreate
from app.sales_orders.models.sales_order import SalesOrderStatus
from fastapi import HTTPException
from datetime import datetime
from decimal import Decimal
class SalesOrderService:
  @staticmethod
  def create(db, data: SaleOrderCreate):
    customer = CustomerRepository.get_by_id(db, data.customer_id)
    if not customer: 
      raise HTTPException(400, "Khách hàng không tồn tại")
    order = SalesOrder(customer_id = data.customer_id, code = f"SO{int(datetime.now().timestamp())}" ) # tạo mã đơn hàng
    total = Decimal(0)  #Tổng tiền đơn hàng

    for line in data.lines: #Tính tiền từng sản phẩm
      InventoryService.reserve( #Đặt hàng
        db,
        product_id = line.product_id,
        warehouse_id = line.warehouse_id,
        quantity = line.quantity,
        ref = order.code #Mã đơn hàng
      )
      order_item = SalesOrderItem( #Tạo chi tiết đơn hàng
        product_id = line.product_id,
        quantity = line.quantity,
        price = line.price,
      )
    
      total += line.price * line.quantity #Tính tổng tiền
      order.lines.append(order_item) #Thêm chi tiết đơn hàng vào đơn hàng

    order.total_amount = total 

    SalesOrderRepository.create(db, order)
    db.commit()
    db.refresh(order)
    return order

  @staticmethod
  def confirm(db, order_id: int):
    order = SalesOrderRepository.get_by_id(db, order_id)

    if not order:
      raise HTTPException(404, "Đơn hàng không tồn tại")
    if order.status != SalesOrderStatus.DRAFT:
      raise HTTPException(404, "Đơn hàng không thể xác nhận")
    if order.lines:
      raise HTTPException(404, "Đơn hàng không có sản phẩm")
    
    #Xử lý xác nhận đơn hàng

    for lines in order.lines: 
      InventoryService.release( # Trừ đi số lượng đặt hàng
        db,
        product_id = lines.product_id,
        warehouse_id = lines.warehouse_id,
        quantity = lines.quantity,
        ref = order.code
      )
      
      #Xuất kho thật
      InventoryService.outbound( # Trừ đi số lượng thật
        db,
        product_id = lines.product_id,
        warehouse_id = lines.warehouse_id,
        quantity = lines.quantity,
        ref = order.code
      )

    #Cập nhật trạng thái đơn hàng 

    order.status = SalesOrderStatus.CONFIRMED
    order.confirm_at = datetime.now()

    db.commit()
    db.refresh(order)
    return order
  
  @staticmethod
  def cancel(db, order_id: int):
      order = SalesOrderRepository.get_by_id(db, order_id)
      if not order:
        raise HTTPException(404, "Đơn hàng không tồn tại")
      if order.status == SalesOrderStatus.CANCEL:
        raise HTTPException(404, "Đơn hàng đã hủy")
      if order.status!= SalesOrderStatus.DRAFT:
        raise HTTPException(404, "Đơn hàng không thể hủy")
      if order.lines:
        raise HTTPException(404, "Đơn hàng không có sản phẩm")
      #Xử lý hủy đơn hàng
      for line in order.lines:
        InventoryService.release( #Hủy đặt hàng
          db,
          product_id = line.product_id,
          warehouse_id = line.warehouse_id,
          quantity = line.quantity,
          ref = order.code
        )
      order.status = SalesOrderStatus.CANCELLED
      order.cancelled_at = datetime.now()

      db.commit()
      db.refresh(order)
      return order