from abc import ABC, abstractmethod
from typing import Dict, Type

# Step 1: Payment Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

# Step 2: Concrete Payment Strategies
class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount:.2f}")
        return True

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}")
        return True

class BankTransferPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing bank transfer of ${amount:.2f}")
        return True

# Step 3: Context Class
class PaymentProcessor:
    def __init__(self):
        self._strategies: Dict[str, Type[PaymentStrategy]] = {
            "credit_card": CreditCardPayment,
            "paypal": PayPalPayment,
            "bank_transfer": BankTransferPayment
        }
    
    def process_payment(self, payment_type: str, amount: float) -> bool:
        try:
            strategy = self._strategies[payment_type]()
            return strategy.process_payment(amount)
        except KeyError:
            raise ValueError(f"Invalid payment type: {payment_type}")

# Step 4: Example Usage
if __name__ == "__main__":
    processor = PaymentProcessor()
    
    # Process different types of payments
    try:
        processor.process_payment("credit_card", 100.00)
        processor.process_payment("paypal", 50.75)
        processor.process_payment("bank_transfer", 200.50)
        
        # This will raise an error
        processor.process_payment("bitcoin", 75.00)
    except ValueError as e:
        print(f"Error: {e}")