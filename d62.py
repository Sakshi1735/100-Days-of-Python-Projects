#access specifiers

'''
class Employee:
    def __init__(self):
        self.name = "Sakshi" #public access modifiers
        self.__lname = "Verma" #private access modifiers
        self.occ = "Software Developer"

a = Employee()
print(a.name)
print(a.occ)
#print(a.__lname) #cannot be accessed directly
print(a._Employee__lname)  #can be accessed indirectly --> name mangling --> used to protect class-private and super-class-private attributes from being accidentantly overwritten
print(a.__dir__()) 
'''

class Students:
    def __init__(self):
        self._name = "sakshi"

    def _funName(self): #protected method
        return "codewithsakshi"

class Subject(Students): #inherited class
    pass

obj = Students()
obj1 = Subject()

#calling by object of Student class
print(obj._name)
print(obj._funName())

#calling by object of Subject class
print(obj1._name)
print(obj1._funName())