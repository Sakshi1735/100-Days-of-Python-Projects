#Hybrid Inheritance in python

class Baseclass:
    pass
class Derived1(Baseclass):
    pass
class Derived2(Baseclass):
    pass
class Derived3(Derived1, Derived2):
    pass

#Hierarchial Inheritance

class Baseclass:
    pass
class D1(Baseclass):
    pass
class D1(Baseclass):
    pass
class D3(D1):
    pass
