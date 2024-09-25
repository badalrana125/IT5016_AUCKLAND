""""
program which calculate the area of circle 
Author: Aashish
"""

# radius = float (input("Enter the number:"))
radius= 10
pi = 3.14159265359
area = pi* radius *2
print("Area of a circle is", area)

"""
Calculates the area of a rectangle.
Author: Aashish
"""

width = 5.3
height = 9.3
area = width * height

print("Area of rectangle", area)

#practise3
result1 = 25 % 3
result2 = 20 % 34
result3 = 20 // 3
result4 = 5 // 7 
result5 = (25 // 5) % 5

print(result1,result2,result3,result4,result5)


#Python Library

"""
Calculate the radius of a circle, given the area
Author: Aashish
"""

import math
area= float(input("Enter the area value:"))  #here area
radius= math.sqrt(area / math.pi)

print("the radius of circle", radius)