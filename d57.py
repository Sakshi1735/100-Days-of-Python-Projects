class Person:
    name = "Sakshi"
    occupation = "Software Developer"
    networth = 40000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        #self parameter is a referrence to the current instance of the class
        #it is used to access variables that belongs to the class
a= Person()
b= Person()
c=Person()

a.name = "Riya"
a.occupation = "Nurse"

b.name= "Sagar"
b.occupation="Accountant"

a.info()
b.info()
c.info()