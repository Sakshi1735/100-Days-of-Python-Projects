class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e1= Employee("Rohan Das", 420)
e1.showDetails()
e2 = Employee("Tina",520)
e2.showDetails()
