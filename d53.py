#map(),filter() and reduce()

'''def cube(x):
    return x*x*x
print(cube(2))

l=[1,2,3,4,5,6,7]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl) '''

l=[1,2,3,4,5,6,7]
cube = lambda x : x*x*x
newl=list(map(cube,l)) #map applies function cube to each element in the iterable argument l
print(l)
print(newl)

filter_fn =  lambda a: a>4
newl2= list(filter(filter_fn,l)) #filter applies the condition to each element in the iterable argument l
print(newl2)

from functools import reduce

sum = lambda x,y:x+y
s = reduce(sum,l) #takes first two elemnts from the input l and replaces them by the sum value of the both 
print(s) #reduce return the list/tuple by performing the particular function on the entire iterable 'l'
