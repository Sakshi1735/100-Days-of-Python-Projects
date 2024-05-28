#Multi level inheritance --> type of inheritence in oops where derived class inherits from another derived class.
#Example:

class Animal:
    def __iinit__(self, name, species):
        self.name = name
        self.species = species
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
    
class GoldenRetreiver(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name,breed="Golden Retreiver")
        self.color = color
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o= GoldenRetreiver("tommy","golden")
o.show_details()