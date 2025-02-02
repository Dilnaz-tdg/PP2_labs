#1
class getstring:
    def __init__(self):
        self.text = ""
    
    def userstr(self):
        self.text = input("Your string: ").strip()

    def printstr(self):
        print(self.text.upper())

"""st = getstring()
st.userstr()
st.printstr()"""

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

"""shape = Shape()
print(shape.area())

square = Square(10)
print(square.area())"""


#3
class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
"""shape = Shape()
print(shape.area())

rectangle = Rectangle(2,8)
print(rectangle.area())"""


#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"The point is located in ({self.x}, {self.y}) ")

    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    
    def dist(self,point):
        dx = self.x - point.x
        dy = self.y - point.y
        return math.sqrt(dx**2 + dy**2)
    
"""p1 = Point(3,4)
p2 = Point(6,8)

p1.show()
p2.show()

print(f"Distance between points: {p1.dist(p2):.2f}")

p1.move(10,10)
p1.show()
print(f"New distance: {p1.dist(p2):.2f}")"""

#5
class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.owner} account. New balance: {self.balance}")
        else:
            print("The deposit amount must be positive!")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} from {self.owner} account. New balance: {self.balance}")
    
    def showbalance(self):
        print(f"Account balance {self.owner}: {self.balance}")

"""at = Bankaccount("Dilnaz", 100000)

at.showbalance()
at.deposit(500)
at.withdraw(7000)
at.showbalance()"""

#6
def isprime(lst):
    if lst < 2:
        return False
    
    for i in range(2, int(lst**0.5) + 1):
        if lst % i == 0:
            return False
        
    return True

def filterpr(flst):
    return list(filter(lambda x: isprime(x), flst))

"""numbers = [1, 3 , 6, 40, 34, 35, 38, 5, 7]

prnumbers = filterpr(numbers)
print(prnumbers)"""




    



