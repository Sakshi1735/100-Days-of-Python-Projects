#instance vs class variable 

class Employee:
    companyName = "Apple" #class variable #this value is in general for all the instanes present
    noofemployees = 0
    def __init__(self,name):
        self.name = name #instance variable #these values are just related to the instances #defined inside the init method usually used to store information ie specific to each instance. 
        self.raise_amount = 0.02
        Employee.noofemployees +=1 
    def showdetails(self):
        print(f"The name of the emplyoee is {self.name} and the raise amount in {self.noofemployees} sized company {self.companyName} is {self.raise_amount}")

emp1=Employee("Sakshi")
emp1.raise_amount = 0.3
emp1.companyName = "Apple india"
Employee.showdetails(emp1)

emp2=Employee("tia")
emp2.companyName = "Apple usa"
Employee.showdetails(emp2)

