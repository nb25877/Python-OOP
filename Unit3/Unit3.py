from abc import ABC, abstractmethod

# Abstract Car class
class Car(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass

# Concrete Car classes
class Sedan(Car):
    def drive(self) -> str:
        return "Driving a comfortable Sedan"

class SUV(Car):
    def drive(self) -> str:
        return "Driving a powerful SUV"

class Hatchback(Car):
    def drive(self) -> str:
        return "Driving an efficient Hatchback"

# Abstract Factory class
class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

# Concrete Factory classes
class SedanFactory(CarFactory):
    def create_car(self) -> Car:
        return Sedan()

class SUVFactory(CarFactory):
    def create_car(self) -> Car:
        return SUV()

class HatchbackFactory(CarFactory):
    def create_car(self) -> Car:
        return Hatchback()

# Client code demonstration
def client_code(factory: CarFactory) -> None:
    car = factory.create_car()
    print(car.drive())

# Example usage
if __name__ == "__main__":
    print("Creating cars using different factories:\n")
    
    factories = [
        SedanFactory(),
        SUVFactory(),
        HatchbackFactory()
    ]
    
    for factory in factories:
        client_code(factory)