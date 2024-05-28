#Lambda functions
# lambda function is anonymus as it does not have a name ex : line16
'''def double(x):
    return x*2'''

def appl(fx, value):
    return 6+fx(value)

double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x,y:(x+y) / 2

print(double(5))
print(cube(3))
print(avg(10,20))
print(appl(lambda x: x*x*x*x,2))
print(appl(cube,2))


sum= lambda x,y : print(f'{x} + {y} ={x+y}')
sum(20,30)