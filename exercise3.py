questions=[["What is your name","Sakshi","Mansi","Tanya","Anshika",1],
["What is your name","Sakshi","Mansi","Tanya","Anshika",2],
["What is your name","Sakshi","Mansi","Tanya","Anshika",3],
["What is your name","Sakshi","Mansi","Tanya","Anshika",4],
["What is your name","Sakshi","Mansi","Tanya","Anshika",1],
["What is your name","Sakshi","Mansi","Tanya","Anshika",2],
["What is your name","Sakshi","Mansi","Tanya","Anshika",3],
["What is your name","Sakshi","Mansi","Tanya","Anshika",4],
["What is your name","Sakshi","Mansi","Tanya","Anshika",1],
["What is your name","Sakshi","Mansi","Tanya","Anshika",2],
["What is your name","Sakshi","Mansi","Tanya","Anshika",3],
["What is your name","Sakshi","Mansi","Tanya","Anshika",4],
["What is your name","Sakshi","Mansi","Tanya","Anshika",1],
["What is your name","Sakshi","Mansi","Tanya","Anshika",2],
["What is your name","Sakshi","Mansi","Tanya","Anshika",3]]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}    b. {question[2]}")
    print(f"a. {question[3]}    b. {question[4]}")
    reply = int(input("Enter your answer(1-4):  "))
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i==4):
            money = 10000
        elif (i==9):
            money = 320000
        elif (i==14):
            money = 10000000
    else:
        print("Wrong Answer!")
        break
print(f"Your take home money is {money}")