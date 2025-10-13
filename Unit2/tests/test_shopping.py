import pytest
from shopping import Product, Item, Order, CreditCardPayment, PercentageDiscount

def test_product_creation():
    product = Product("Test", 10.0)
    assert product.name == "Test"
    assert product.price == 10.0

def test_order_total():
    order = Order()
    product = Product("Test", 10.0)
    order.add_item(Item(product, 2))
    assert order.calculate_total() == 20.0

def test_payment_processing():
    order = Order()
    product = Product("Test", 10.0)
    order.add_item(Item(product, 1))
    payment = CreditCardPayment()
    assert order.process_payment(payment) == True