from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount:.2f}")
        return True

class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}")
        return True

class CryptoPayment(PaymentMethod):
    def pay(self, amount: float) -> bool:
        print(f"Processing crypto payment of ${amount:.2f}")
        return True