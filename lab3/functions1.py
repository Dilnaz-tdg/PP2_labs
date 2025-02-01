#1
def recipe(grams):
    return 28.3495231 * grams

""" grams = float(input())
ounces = recipe(grams)
print(f"{grams} grams = {ounces:.5f} ounces") """

#2
def centigrade(F):
    return (5/9)*(F-32)

""" F=int(input())
C = centigrade(F)
print(f"{F:.2f} Fahrenheit = {C:.2f}  centigrade") """

#3
def puzzle(numheads, numlegs):
    for chikens in range(numheads+1):
        rabbits = numheads - chikens
        if 2*chikens + 4*rabbits == numlegs:
            return chikens, rabbits
    return "no answer"
    
"""numheads = int(input())
numlegs = int(input())
result = puzzle(numheads, numlegs)
if result == "no answer":
    print("no answer")
else:
    chikens, rabbits = result
print(f"chikens = {chikens} rabbits = {rabbits}")"""

#4
def prime(mylist):
    newlist = []
    for item in mylist:
        if item < 2:
            continue
        for i in range(2, int(item * 0.5) + 1):
            if item % i == 0:
                break
        else:
            newlist.append(item)
    return newlist
   
"""mylist = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = prime(mylist)
print(prime_numbers)  """


#5
from itertools import permutations

def pemmut(s):
    perms = permutations(s)
    for perm in perms:
        print("".join(perm))

"""userint = input()
pemmut(userint)"""


#6
def reversedsen (sent):
    words = sent.split()
    reversedsentance = " ".join(reversed(words))
    return reversedsentance

"""usersen = input()
result = reversedsen(usersen)
print(result)"""

#7 
def has_33 (nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

"""print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))"""

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

"""print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))"""

#9
import math

def spherevoiume(radius):
    return (4/3)* math.pi * radius**3

"""rd = float(input())
v = spherevoiume(rd)
print(f"{v:.2f}")"""

#10
def uniquelist(l):
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    return unique

"""print(uniquelist([1, 2, 1, 5, 6, 5, 6, 7, 8]))"""

#11
def ifpalindrome(sen):
    if sen == sen[::-1]:
        return True
    return False

"""usersen = input()
print(ifpalindrome(usersen))"""

#12
def histogram(nums):
    for num in nums:
        print("*" * num)

"""histogram([4, 9, 7])"""

#13 
import random
def guessthenumber():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    secretnum = random.randint(1,20)
    attemps = 0

    while True:
        print("\nTake a guess.")
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a valid number.")
            continue
        attemps += 1

        if guess < secretnum:
            print("Your guess is too low.")
        elif guess > secretnum:
            print("Your guess is too high.")
        else:
            print(f"Good job {name}! You guessed my number in {attemps} guesses!")
            break

"""guessthenumber()"""

