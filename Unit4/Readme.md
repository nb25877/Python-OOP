# Unit 4: Structural Design Patterns - Decorator Pattern

This unit demonstrates the implementation of the Decorator Pattern using a coffee shop example.

## Project Structure

```
Unit4/
├── README.md
└── unit4.py        # Coffee shop implementation using Decorator pattern
```

## Decorator Pattern Implementation

### Components

1. **Abstract Base Class**
   - `Coffee`: Defines interface for all components
   - `CoffeeDecorator`: Base decorator class

2. **Concrete Components**
   - `SimpleCoffee`: Basic coffee implementation

3. **Concrete Decorators**
   - `Milk`: Adds milk and cost
   - `Sugar`: Adds sugar and cost
   - `Whip`: Adds whipped cream and cost

## Pattern Benefits

- **Flexibility**: Add/remove features dynamically
- **Single Responsibility**: Each decorator handles one addition
- **Open/Closed**: New features without modifying existing code
- **Composition**: Complex combinations through simple decorators

## Running the Code

```bash
python unit4.py
```

### Expected Output
```
Simple coffee: $2.00
Simple coffee + milk: $2.50
Simple coffee + milk + sugar: $2.70
Simple coffee + sugar + milk + whip: $3.40
```

## Key Concepts

1. **Composition over Inheritance**
   - Uses object composition for extending functionality
   - Avoids class explosion problem

2. **Dynamic Behavior**
   - Features can be added/removed at runtime
   - Flexible combination of behaviors

3. **Maintainability**
   - Each decorator is independent
   - Easy to add new decorators

## Requirements
- Python 3.x
- ABC module (built-in)