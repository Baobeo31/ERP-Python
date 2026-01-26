from fastapi import FastAPI
from app.products.router import router as product_router  
from app.categories.router import router as category_router
from app.inventories.router import router as inventory_router
from app.sales_orders.router import router as sales_order_router
from app.sales_return.router import router as sales_return_router
from app.customers.router import router as customer_router
app = FastAPI(title="ERP API")

app.include_router(
    product_router,
    prefix="/products",
    tags=["Products"]
)

app.include_router( 
    category_router,
    prefix="/categories",
    tags=["Categories"]
)

app.include_router(
    inventory_router,
    prefix="/inventories",
    tags=["Inventories"]
)

app.include_router(
    sales_order_router,
    prefix="/sales-orders",
    tags=["Sales Orders"]
)

app.include_router(
    sales_return_router,
    prefix="/sales-returns",
    tags=["Sales Returns"]
)

app.include_router(
    customer_router,
    prefix="/customers",
    tags=["Customers"]
)


@app.get("/")
def root():
    return {"message": "ERP backend ready"}
