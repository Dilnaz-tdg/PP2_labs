#1

lst = [1,2,3,4,5,6]
answ = 1
for i in range(0, len(lst)):
    answ *= lst[i]

print(answ)

#2
userstr = input()
uprc = 0
lwc = 0
for i in userstr:
    if(ord(i) >= 65 and ord(i) <= 90):
        uprc += 1
    elif(ord(i) >= 97 and ord(i) <= 122):
        lwc += 1

print(f"upper case: {uprc}")
print(f"lower case: {lwc}")

#3 
userword = input()
if userword == ''.join(reversed(userword)): 
     print(f"{userword} is palindrome")

#4
import time
import math
def invoke():
    num = int(input())
    timeusers = int(input())
    time.sleep(timeusers / 1000)
    print(f"Square root of {num} after {timeusers} miliseconds is {math.sqrt(num)}")

invoke()

#5
mytuple = (1, 1, "yes", "no")
print(all(tuple))
