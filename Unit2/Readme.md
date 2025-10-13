# Unit 2: SOLID Principles in Python

This unit demonstrates the application of SOLID principles through a practical online shopping system implementation.

## Project Structure

```
Unit2/
├── README.md
├── shopping/
│   ├── __init__.py
│   ├── models.py        # Product and Item classes
│   ├── order.py        # Order management
│   ├── payment.py      # Payment processing
│   └── discounts.py    # Discount strategies
└── tests/
    └── test_shopping.py
```

## SOLID Principles Implementation

1. **Single Responsibility Principle (SRP)**
   - Separated order management from payment processing
   - Each class has one reason to change

2. **Open/Closed Principle (OCP)**
   - Payment system is extensible without modification
   - New payment methods can be added by implementing PaymentMethod

3. **Liskov Substitution Principle (LSP)**
   - All payment methods are substitutable
   - Consistent behavior across payment implementations

4. **Interface Segregation Principle (ISP)**
   - Focused interfaces for payments and discounts
   - No unnecessary method implementations

5. **Dependency Inversion Principle (DIP)**
   - High-level modules depend on abstractions
   - Payment processing is decoupled from order management

## Running the Code

```bash
# Run tests
python -m pytest tests/test_shopping.py

# Run example usage
python shopping/example.py
```

## Requirements
- Python 3.x
- pytest (for running tests)