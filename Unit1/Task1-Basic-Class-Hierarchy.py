# Define the base class Vehicle
class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

# Define the subclass Car that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, fuel_type, num_doors):
        super().__init__(brand, fuel_type)
        self.num_doors = num_doors

# Instances can be created as follows:
# my_car = Car("Toyota", "Petrol", 4)

