#Readlines method
'''f=open('myfile.txt','r')
while True:
    line=f.readline()
    print(line)
    if not line:
        break
    print(line)'''

'''f=open('myfile.txt','r')
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    m1 =  line.split(',')[0]
    m2 =  line.split(',')[1]
    m3 =  line.split(',')[2]
    print(f"Marks of student {i} in Maths is : {m1}")
    print(f"Marks of student {i} in Maths is : {m2}")
    print(f"Marks of student {i} in Maths is : {m3}")
'''

#Writelines method

'''f= open('myfile.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()
'''

f=open('myfile.txt','w')
lines=['10,20,30','80,60,40','60,70,80']
for line in lines:
    f.write(line + '\n')
f.close()