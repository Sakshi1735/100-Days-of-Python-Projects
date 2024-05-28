#Getters and Setters

class Myclass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"Value is{self._value}")

    @property #THIS PROPERTY IS USED TO GET A VALUE ie IT IS A GETTER
    def ten_value(self):
        return 10*self._value
        
    @ten_value.setter #THIS PROPERTY IS USED TO SET THE VALUE OF THE PROPERTY ie IT IS A SETTER.
    def ten_value(self,new_value):
        self._value = new_value/10
    
obj = Myclass(10)
obj.ten_value = 69
print(obj.ten_value)
obj.show() 

