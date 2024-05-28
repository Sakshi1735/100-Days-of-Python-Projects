#Constructors
#constructor function ie called when an object is created of a class
#paramaterised constructor : when the constructor accepts arguments along with self
#default constructor : when the constructor does not accept any argument along with self


class Person:
    def __init__(self,n,o): # here self argument takes in the value from object and the rest two are given in the object call statement.
        print("Hey i am a person")
        self.name = n
        self.occ = o
        
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Sakshi","Software Developer") #a,b,c are objects
b = Person("Divya", "HR")
c = Person("Rina","PR")
a.info()
b.info()
c.info()