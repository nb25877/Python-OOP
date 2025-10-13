# order.py
# This module defines the Order class for managing shopping orders.
# It includes methods to add items, calculate the total cost, and process payments.
# It depends on the Item class from models.py and PaymentMethod class from payment.py.

from typing import List
from .models import Item
from .payment import PaymentMethod

class Order:
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def calculate_total(self) -> float:
        return sum(item.total for item in self.items)

    def process_payment(self, payment_method: PaymentMethod) -> bool:
        total = self.calculate_total()
        return payment_method.pay(total)