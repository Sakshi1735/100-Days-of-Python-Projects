print("Press 1 for : '+'")
print("Press 2 for : '-'")
print("Press 3 for : '*'")
print("Press 4 for : '/'")
print("Press 5 for : '%'")
print("Press 6 for : '^'")
a=int(input("Enter your choice"))
b=int(input("Enter first number: "))
c=int(input("Enter second number: "))
if a == 1:
    print("The sum is: ",b+c)
elif a == 2:
    print("The difference is: ",b-c)
elif a == 3:
    print("The product is: ",b*c)
elif a == 4:
    print("The quotient is: ",b/c)
elif a == 5:
    print("The remainder is: ",b%c)
elif a == 6:
    print("The exponent is: ",b^c)