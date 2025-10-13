# shopping/models.py
# This module defines the data models for a shopping application.
# It includes classes for Product and Item with relevant attributes and methods.

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Item:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    @property
    def total(self) -> float:
        return self.product.price * self.quantity