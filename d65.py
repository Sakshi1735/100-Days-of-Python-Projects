#static method usage

class Maths:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num = self.num +n
    
    @staticmethod #the method can be called on the class itself, (it is not associated with the class)
    def add(a,b): #no self is used here because of using of the staticmethod decorator.
        return a+b
    
a=Maths(5)
print(a.num)
a.addtonum(6)
print(a.num)   
print(Maths.add(7,2))
