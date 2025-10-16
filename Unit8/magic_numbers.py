# Refactoring using named constants to improve readability and maintainability.
BOOK_DISCOUNT = 0.9
ELECTRONICS_DISCOUNT = 0.8

def calculate_total_price(items):
    total = 0
    for item in items:
        if item['type'] == 'book':
            total += item['price'] * BOOK_DISCOUNT
        elif item['type'] == 'electronics':
            total += item['price'] * ELECTRONICS_DISCOUNT
        else:
            total += item['price']
    return total