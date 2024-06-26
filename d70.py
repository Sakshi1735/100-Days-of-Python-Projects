#Class Methods as alternative constructors

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
e1 = Employee("Sakshi",120000)
print(e1.name)
print(e1.salary)

string = "Saksham-1200"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)