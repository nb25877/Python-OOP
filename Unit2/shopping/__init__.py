# __init__.py
# This file initializes the shopping package and imports key components.
# It provides a unified interface for accessing various modules related to shopping.
# Modules included: models, order, payment, discounts

from .models import Product, Item
from .order import Order
from .payment import PaymentMethod, CreditCardPayment, PayPalPayment, CryptoPayment
from .discounts import DiscountStrategy, PercentageDiscount, FixedDiscount

__all__ = [
    'Product',
    'Item',
    'Order',
    'PaymentMethod',
    'CreditCardPayment',
    'PayPalPayment',
    'CryptoPayment',
    'DiscountStrategy',
    'PercentageDiscount',
    'FixedDiscount'
]