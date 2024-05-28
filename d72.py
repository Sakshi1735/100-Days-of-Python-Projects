#Super keyword in python
class Parentclass:
    def parent_method(self):
        print("This is the parent method1.")

class Childclass(Parentclass):
    def parent_method(self):
        print('Sakshi')
        super().parent_method()  # Calling the parent's parent_method using 'super()'
    def child_method(self):
        print("This is the child method2.")
        super().parent_method()  #Calling the parent's parent_method using 'super()'

child_object = Childclass()
child_object.child_method()
child_object.parent_method()

#Example2
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id) #--> parent class ke constructor se name , id lelia
        self.lang = lang

rohan = Employee("Rohan Das",420)
harry = Programmer("Harry Panday", 555, "BhaiLang")
print(rohan.name)
print(harry.id)
print(harry.lang)