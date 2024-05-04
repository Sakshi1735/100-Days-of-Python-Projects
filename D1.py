# Numbers Guessing Game
import random
import math

lower = int(input("Enter lower bound:-  "))
upper = int(input("Enter upper bound:-   "))
x = random.randint(lower,upper)
print(f"\n\t You've only {round(math.log(upper - lower + 1,2))} chances to guess the integer!\n")
count = 0
while count < math.log(upper - lower + 1 ,2) :
    count+=1
    guess =  int(input("Guess a number:     "))
    if x == guess:
        print(f"Congratulations! you did it in {count} try.")
        break
    elif x > guess:
        print("\nYour guess is too small.\n")
    elif x < guess:
        print("\nYour guess is too high.\n")
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")