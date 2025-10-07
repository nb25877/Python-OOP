from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Example usage
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    
    print(f"Dog says: {dog.make_sound()}")
    print(f"Cat says: {cat.make_sound()}")
    
    # This would raise an error:
    # animal = Animal()  # TypeError: Can't instantiate abstract class Animal