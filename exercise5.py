#Snake Water Gun
'''The gun beats the snake, the water beats the gun, and the snake beats the water.

Write a python program to create a Snake Water Gun game in Python using if-else statements.

               S W G
computer =     0 1 2
player =  S 0  D W L 
          W 1  L D W
          G 2  W L D
'''

import random
print("<SNAKE, WATER OR GUN>")

choices = ["snake","water","gun"]
choice1 = input("Your Choice is: ")
choice2 = random.choice(choices)
print(f"The Computers choice is: {choice2}")

draw = lambda c1,c2: c1 == c2
win = lambda c1, c2: (c1 == 'snake' and c2 == 'water') or (c1 == 'water' and c2 == 'gun') or (c1 == 'gun' and c2 == 'snake')
lose = lambda c1, c2: (c1 == 'snake' and c2 == 'gun') or (c1 == 'water' and c2 == 'snake') or (c1 == 'gun' and c2 == 'water')

if draw(choice1,choice2):
    print("It is a draw!")
elif win(choice1,choice2):
    print("The user wins!")
elif lose(choice1,choice2):
    print("The computer wins!")
