# Unit 5: Behavioral Design Patterns - Strategy Pattern

This unit demonstrates the implementation of the Strategy Pattern using a payment processing system.

## Project Structure

```
Unit5/
├── README.md
└── Unit5.py        # Payment system implementation using Strategy pattern
```

## Strategy Pattern Implementation

### Components

1. **Strategy Interface**
   - `PaymentStrategy`: Abstract base class defining payment interface

2. **Concrete Strategies**
   - `CreditCardPayment`: Credit card processing
   - `PayPalPayment`: PayPal processing
   - `BankTransferPayment`: Bank transfer processing

3. **Context**
   - `PaymentProcessor`: Manages payment strategies

## Benefits of Strategy Pattern

1. **Open/Closed Principle**
   - New payment methods can be added without modifying existing code
   - Each strategy is encapsulated in its own class

2. **Flexibility**
   - Payment strategies can be switched at runtime
   - Easy to add or remove payment methods

3. **Maintainability**
   - Each strategy is independent
   - No complex conditional logic
   - Clear separation of concerns

## Running the Code

```bash
python Unit5.py
```

### Expected Output
```
Processing credit card payment of $100.00
Processing PayPal payment of $50.75
Processing bank transfer of $200.50
Error: Invalid payment type: bitcoin
```

## Key Improvements

1. **Eliminated Conditional Logic**
   - Replaced if-elif chains with strategy lookup
   - More maintainable and scalable

2. **Enhanced Extensibility**
   - New payment methods can be added by:
     1. Creating new strategy class
     2. Adding to strategy dictionary
   - No modification to existing code needed

3. **Better Error Handling**
   - Clear error messages for invalid payment types
   - Type hints for better code clarity

## Requirements
- Python 3.x
- ABC module (built-in)
- typing module (built-in)