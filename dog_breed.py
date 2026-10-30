class Dog:
    animal = "Dog"
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    def display_details(self):
        print(f"Animal Type: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")
dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")
print("--- Dog 1 Details ---")
dog1.display_details()
print("--- Dog 2 Details ---")
dog2.display_details()
