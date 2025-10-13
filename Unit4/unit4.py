from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Simple coffee"

# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()

# Concrete decorators
class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

    def description(self) -> str:
        return f"{self._coffee.description()} + milk"

class Sugar(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.2

    def description(self) -> str:
        return f"{self._coffee.description()} + sugar"

class Whip(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.7

    def description(self) -> str:
        return f"{self._coffee.description()} + whip"

# Example usage
if __name__ == "__main__":
    # Create a simple coffee
    coffee = SimpleCoffee()
    print(f"{coffee.description()}: ${coffee.cost():.2f}")

    # Add milk
    coffee_with_milk = Milk(coffee)
    print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost():.2f}")

    # Add milk and sugar
    coffee_with_milk_sugar = Sugar(coffee_with_milk)
    print(f"{coffee_with_milk_sugar.description()}: ${coffee_with_milk_sugar.cost():.2f}")

    # Create a complex coffee with multiple decorators
    deluxe_coffee = Whip(Milk(Sugar(SimpleCoffee())))
    print(f"{deluxe_coffee.description()}: ${deluxe_coffee.cost():.2f}")