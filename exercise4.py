"""import random
import string

a = str(input("Enter the string: \t"))
print("Press 1 for Coding your String")
print("Press 2 for Decoding your String")
choice = int(input("Enter you choice: \t"))
if choice == 1:
    if (len(a)<3):
        l = list(a)
        a= l[0]
        l[0] = l[-1]
        l[-1] = a
        a2 = ""
        for i in l:
            a2 += i
        print(a2)
    else:
        l2 = list(a)
        a = l2[0]
        l2.pop(0)
        l2.append(a)
        a3 = ""
        i = 0
        while i<3:
            l2.insert(0,(random.choice(string.ascii_letters)))
            l2.append(random.choice(string.ascii_letters))
            i += 1
        a3 = ""
        for i in l2:
            a3 += i
        print(f"Coded String is {a3}")
elif (choice == 2):
    if (len(a)<3):
        l = list(a)
        a= l[-1]
        l[-1] = l[0]
        l[0] = a
        a2 = ""
        for i in l:
            a2 += i
        print(a2)
    else:
        lt = list(a)
        i = 0
        while i<3:
            lt.pop(0)
            lt.pop(-1)
            i += 1
        b= lt[-1]
        lt.pop(-1)
        lt.insert(0,b)
        a4 = ""
        for i in lt:
            a4 += i
        print(f"Decoded String is: {a4}")
"""
import random
import string
st= input("Enter message \t")
words= st.split(" ")
coding =True
if(coding):
    nwords=[]
    for word in words:
        if len(word)>=3:
            i=0
            r1="kre"
            r2="pka"
            stnew= r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if len(word)>=3:
            stnew= word[3:-3]
            stnew = stnew[-1] +stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(words[::-1])
    print("".join(nwords))