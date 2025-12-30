from fastapi import FastAPI
from app.products.router import router as product_router  
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI(title="ERP API")

app.include_router(
    product_router,
    prefix="/products",
    tags=["Products"]
)

@app.get("/")
def root():
    return {"message": "ERP backend ready"}
