from dataclasses import dataclass
from typing import List
from datetime import datetime
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

@dataclass
class OrderItem:
    product_id: int
    quantity: int
    price: float

@dataclass
class Order:
    id: int
    user_id: int
    items: List[OrderItem]
    status: OrderStatus
    created_at: datetime
    
    def total_amount(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

class OrderService:
    def __init__(self, order_repository, product_service):
        self._repository = order_repository
        self._product_service = product_service
    
    def create_order(self, user_id: int, items: List[OrderItem]) -> Order:
        # Create new order
        order = Order(
            id=0,
            user_id=user_id,
            items=items,
            status=OrderStatus.PENDING,
            created_at=datetime.now()
        )
        return order