class Person:
    def __init__(self, name):
        self.name = name
        print(f"Hello, {self.name}!")
    
    def __del__(self):
        print(f"Goodbye, {self.name}!")

# Example usage
if __name__ == "__main__":
    # Create a person
    person1 = Person("Alice")
    
    # Explicitly delete the object
    del person1
    
    # Create another person (will be deleted automatically when program ends)
    person2 = Person("Bob")


    