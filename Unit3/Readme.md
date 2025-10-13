# Unit 3: Design Patterns in Python - Factory Method

This unit demonstrates the implementation of the Factory Method Pattern using a car manufacturing system example.

## Project Structure

```
Unit3/
├── README.md
└── Unit3.py        # Main implementation file
```

## Factory Method Pattern Implementation

### Components

1. **Abstract Classes**
   - `Car`: Base abstract class for all car types
   - `CarFactory`: Abstract factory class for creating cars

2. **Concrete Car Classes**
   - `Sedan`: Comfortable family car
   - `SUV`: Powerful utility vehicle
   - `Hatchback`: Efficient compact car

3. **Concrete Factory Classes**
   - `SedanFactory`: Creates Sedan instances
   - `SUVFactory`: Creates SUV instances
   - `HatchbackFactory`: Creates Hatchback instances

## Design Pattern Benefits

- **Decoupling**: Client code is decoupled from concrete car classes
- **Extensibility**: New car types can be added without changing existing code
- **Consistency**: Ensures all car types follow the same interface
- **Flexibility**: Runtime decision making for car creation

## Running the Code

```bash
python Unit3.py
```

### Expected Output
```
Creating cars using different factories:

Driving a comfortable Sedan
Driving a powerful SUV
Driving an efficient Hatchback
```

## Key OOP Concepts Used

1. **Abstraction**
   - Abstract base classes define interfaces
   - Implementation details hidden in concrete classes

2. **Inheritance**
   - Concrete classes inherit from abstract bases
   - Factory hierarchy mirrors product hierarchy

3. **Polymorphism**
   - Different car types can be used interchangeably
   - Factories create specific types while maintaining common interface

## Requirements
- Python 3.x
- ABC module (built-in)