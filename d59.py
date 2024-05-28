#Decorators
#Helps to modify the behaviour or functions and methods

def greet(fx): #this is a decorator function
    def mfx(*args, **kwargs):#args,kwargs is a process of taking arguments as a tuple, dictionary respectively
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet #this is a decorator function
def hello(): #this is the function on which we need to apply our decorator function
    print("Hey Sakshi") 

@greet
def add (a,b):
    print(a+b)
hello()
add(1,2)

#decorators can be used to add logging to a function
import logging

def log_fn_call(func):
    def decorated(*args,**kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_fn_call
def my_func(a,b):
    return a+b