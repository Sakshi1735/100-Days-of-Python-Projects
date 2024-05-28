#Single inheritance --> class inherits properties and behaviours from a single parent class

class Animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

d = Dog("Tuffy", "Dog")
d.make_sound()

a = Animal("Ales", "Shih Tzu")
a.make_sound()

#Quick Quiz: Implement a Cat class by using the animal class.
# Add some methods specific to cats.

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
    
    def sleep(self):
        print(f"{self.name} only sleeps when her hoomans are sleep.")
    
    def make_sound(self):
        print("Meow!")
    
c = Cat("Whispers", "Cat")
c.make_sound()
c.sleep()
