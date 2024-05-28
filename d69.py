#Class methods -->that is bound to the class and not the instance of the class

class Employee:
    company = "Nestle"
    def show(self):
        print(f"The name of the employee is {self.name} and the company name is {self.company}")

    def changecompany(cls, newcompany):  #instead of self, we can write anything(cls) as the first argument provided is taken in as an object.
        cls.company = newcompany

e1 = Employee()
e1.name = "sakshi"
e1.show()
e1.changecompany("Dairy milk")
e1.show()
print(Employee.company)