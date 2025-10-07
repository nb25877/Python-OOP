from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    print(f"Circle area: {circle.area():.2f}")
    print(f"Rectangle area: {rectangle.area()}")
    