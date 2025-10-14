from fastapi import FastAPI, Depends, HTTPException, Body
from typing import List, Optional
from pydantic import BaseModel
from src.business.user_management import UserService
from src.business.product_catalog import ProductService
from src.business.order_processing import OrderService
from src.security.authentication import AuthenticationService
from src.data.database import SessionLocal, get_db
import os

# Pydantic models for request/response
class LoginResponse(BaseModel):
    token: str

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class OrderRequest(BaseModel):
    user_id: int
    items: List[OrderItem]

app = FastAPI()

# Dependency injection
def get_user_service(db = Depends(get_db)):
    return UserService(db)

def get_product_service(db = Depends(get_db)):
    return ProductService(db)

def get_order_service(db = Depends(get_db)):
    return OrderService(db)

def get_auth_service(user_service = Depends(get_user_service)):
    secret_key = os.getenv("JWT_SECRET_KEY", "default-secret-key")
    return AuthenticationService(user_service, secret_key)

@app.post("/auth/login", response_model=LoginResponse)
async def login(
    username: str = Body(...),
    password: str = Body(...),
    auth_service: AuthenticationService = Depends(get_auth_service)
):
    token = auth_service.authenticate(username, password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return LoginResponse(token=token)

@app.get("/products/search", response_model=List[ProductResponse])
async def search_products(
    query: str,
    product_service: ProductService = Depends(get_product_service)
):
    return product_service.search_products(query)

@app.post("/orders/create")
async def create_order(
    order_data: OrderRequest,
    order_service: OrderService = Depends(get_order_service)
):
    return order_service.create_order(order_data.user_id, order_data.items)