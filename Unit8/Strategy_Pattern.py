# refactored using encapsulating discount rules into separate classes which adhers to the Open/Closed Principle and improving extensibility.

class DiscountStrategy:
    def apply_discount(self, price):
        return price

class BookDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9

class ElectronicsDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.8

def calculate_total_price(items):
    discount_strategies = {
        'book': BookDiscount(),
        'electronics': ElectronicsDiscount()
    }
    total = 0
    for item in items:
        strategy = discount_strategies.get(item['type'], DiscountStrategy())
        total += strategy.apply_discount(item['price'])
    return total