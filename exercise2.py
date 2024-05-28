import time
timestamp1 = int(time.strftime('%H'))
timestamp2 = int(time.strftime('%M'))
timestamp3 = int(time.strftime('%S'))
print("The time is",timestamp1,timestamp2,timestamp3,sep=": ")
if (timestamp1>0 & timestamp1<12):
    print("Good Morning")
elif (timestamp1>12 & timestamp1<17):
    print("Good Afternoon")
elif (timestamp1>17 & timestamp1<19):
    print("Good Evening")
elif (timestamp1>19 & timestamp1<24):
    print("Good Night")