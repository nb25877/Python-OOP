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