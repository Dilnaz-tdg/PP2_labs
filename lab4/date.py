from datetime import datetime, timedelta

#1 
x = datetime.now()
y = x - timedelta(days = 5)

"""print("current date:", x.strftime("%Y.%m.%d"))
print("date 5 days ago:", y.strftime("%Y.%m.%d"))"""

#2
today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

"""print("today:", today.strftime("%Y.%m.%d"))
print("yesterday:", yesterday.strftime("%Y.%m.%d"))
print("tomorrow:", tomorrow.strftime("%Y.%m.%d"))"""

#3
current = datetime.now()

withoutmicrosec = current.replace(microsecond=0)

"""print("with microseconds:", current)
print("without microseconds:", withoutmicrosec)"""

#4

firstdate = input("first date: ")
seconddate = input("second date:")
fd = datetime.strptime(firstdate, "%Y.%m.%d %H:%M")
sd = datetime.strptime(seconddate, "%Y.%m.%d %H:%M")
difference = abs((fd - sd).total_seconds())
"""print(difference)"""



