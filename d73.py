#Magic/Dunder Methods
class Employee:
    def __init__(self, name):
        self.name = "Harry"
    def __len__(self):
        i = 0
        for c in self.name:
            i +=1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name}"
    def __repr__(self):
        return f"Employee is {self.name}"
    def __call__(self):
        print("Hey I am good")        
e = Employee("harry")
print(str(e))
print(repr(e))
e()
