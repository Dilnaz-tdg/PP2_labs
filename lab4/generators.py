#1 
def square(n):
    for i in range(1, n + 1):
        yield i ** 2

n = int(input("your number1: "))
for sq in square(n):
    """print(sq)"""

#2
def evennum(n):
    for i in range(0, n+1, 2):
        yield str(i)

"""n = int(input("your number2: "))"""
print(",".join(evennum(n)))

#3
def divisible(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i 

n= int(input("your number3: "))
for num in divisible(n):
    print(num)

#4 
def sqr(a,b):
    for i in range(a, b+1):
        yield i**2

a = int(input("a: "))
b = int(input("b: "))

for num in sqr(a,b):
    print(num)

#5 
def numreversed(n):
    for i in range(n, -1, -1):
        yield i
n = int(input("your number5: "))

for ns in numreversed(n):
    print(ns)
