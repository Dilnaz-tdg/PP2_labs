import math

#1
degree = float(input("degree: "))
radian = degree * (math.pi/180)
"""print(f"radian: {radian:.6f}")"""

#2
h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))

area = ((b1+b2)*h)/2

"""print(f"Expected Output: {area:.1f}")"""

#3 
ns = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

areaofpolygon = (ns*(length**2))/4*math.tan(math.pi/ns)
"""print(f"The area of the polygon is: {areaofpolygon:.1f}")"""

#4
lengthofbase = float(input("Length of base: "))
hp = float(input("Height of parallelogram: "))

areaofparallelogram = lengthofbase*hp

"""print(f"Expected Output: {areaofparallelogram:.1f}")"""